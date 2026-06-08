---
tags: [skills, devops, cicd, deploy, environments, promotion]
updated: 2026-06-07
title: "Environment Promotion"
date: 2026-06-01
---

# Environment Promotion

Estrategias de promocao entre ambientes: dev, staging e producao. Inclui canary deployments, blue-green, feature flags e promotion gates.

## Introducao

Environment promotion e o processo de mover codigo e configuracao atraves de ambientes (dev -> staging -> production) de forma controlada e segura. Cada ambiente serve a um proposito especifico no pipeline de entrega.

### Taxonomia de Ambientes

```yaml
Ambientes:
  Desenvolvimento:
    - Local: maquina do desenvolvedor
    - Dev: ambiente compartilhado de integracao
    - Feature: ambiente efemero por branch

  Qualidade:
    - Staging: replica de producao
    - QA: ambiente de testes manuais
    - Integration: testes de integracao

  Producao:
    - Canary: percentual de usuarios
    - Production: ambiente principal
    - DR: disaster recovery
```

## Dev/Staging/Production Strategies

### Pipeline de Promocao

```yaml
# Conceito: pipeline de promocao
stages:
  - name: development
    deploy: automatic
    tests: unit + integration
    data: anonymized subset

  - name: staging
    deploy: automatic
    tests: e2e + performance + security
    data: synthetic + anonymized

  - name: production
    deploy: manual approval
    tests: smoke + canary
    data: real (production)
```

### Exemplo: Multi-Ambiente com GitHub Environments

```yaml
name: Environment Promotion
on:
  push:
    branches: [main]

jobs:
  # Dev: deploy automatico apos CI passar
  deploy-dev:
    runs-on: ubuntu-latest
    environment:
      name: development
      url: https://dev.myapp.com
    steps:
      - uses: actions/checkout@v4
      - run: ./deploy.sh dev
      - run: ./smoke-test.sh https://dev.myapp.com

  # Staging: deploy automatico apos dev passar
  deploy-staging:
    needs: deploy-dev
    runs-on: ubuntu-latest
    environment:
      name: staging
      url: https://staging.myapp.com
    steps:
      - run: ./deploy.sh staging
      - run: ./e2e-tests.sh https://staging.myapp.com
      - run: ./performance-test.sh https://staging.myapp.com

  # Production: deploy manual apos staging
  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://myapp.com
    steps:
      - run: ./deploy.sh production
      - run: ./smoke-test.sh https://myapp.com
```

### Promotion Gates

Gates sao condicoes que bloqueiam a promocao ate serem satisfeitas:

| Gate Tipo | Descricao | Exemplo |
|-----------|-----------|---------|
| Testes | Suite de testes passa | pytest, Jest |
| Qualidade | Cobertura minima | 80% coverage |
| Seguranca | Scan sem criticos | Trivy, Snyk |
| Performance | Benchmarks aceitaveis | Latencia < 200ms |
| Manual | Aprovacao humana | GitHub environment |
| Tempo | Wait timer | 5 min cool-down |
| Feature Flag | Ratio de liberacao | 10% -> 50% -> 100% |

### Kubernetes Native Promotion

```yaml
# ArgoCD ApplicationSet com promocao por ambiente
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: myapp-environments
spec:
  generators:
    - list:
        elements:
          - environment: dev
            cluster: dev-cluster
            namespace: myapp-dev
          - environment: staging
            cluster: staging-cluster
            namespace: myapp-staging
          - environment: production
            cluster: prod-cluster
            namespace: myapp-production
  template:
    metadata:
      name: 'myapp-{{environment}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/will/myapp
        targetRevision: HEAD
        path: 'deploy/overlays/{{environment}}'
      destination:
        server: '{{cluster}}'
        namespace: '{{namespace}}'
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
```

## Canary Deployments

Canary libera uma nova versao para um subconjunto de usuarios antes de liberar para todos.

### Kubernetes Canary com Istio

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: myapp
spec:
  hosts:
    - myapp.com
  http:
    - match:
        - headers:
            x-canary:
              exact: "true"
      route:
        - destination:
            host: myapp-canary
            port:
              number: 80
          weight: 100
    - route:
        - destination:
            host: myapp-stable
            port:
              number: 80
          weight: 90
        - destination:
            host: myapp-canary
            port:
              number: 80
          weight: 10
```

### Canary com GitHub Actions

```yaml
name: Canary Deploy
on:
  workflow_dispatch:
    inputs:
      canary-percent:
        description: "Percentual de trafego para canary"
        required: true
        default: "10"
        type: choice
        options:
          - "10"
          - "25"
          - "50"
          - "100"

jobs:
  canary:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      - name: Deploy canary
        run: |
          kubectl set image deployment/myapp-canary \
            myapp=ghcr.io/will/myapp:${{ github.sha }}

      - name: Set traffic weight
        run: |
          kubectl apply -f - <<EOF
          apiVersion: networking.istio.io/v1beta1
          kind: VirtualService
          metadata:
            name: myapp
          spec:
            hosts:
              - myapp.com
            http:
              - route:
                  - destination:
                      host: myapp-stable
                    weight: $(( 100 - ${{ inputs.canary-percent }} ))
                  - destination:
                      host: myapp-canary
                    weight: ${{ inputs.canary-percent }}
          EOF

      - name: Monitor canary
        run: |
          # Monitorar erros e latencia
          while true; do
            ERROR_RATE=$(curl -s prometheus:9090/... | jq '.data.result[0].value[1]')
            if (( $(echo "$ERROR_RATE > 0.01" | bc -l) )); then
              echo "Error rate too high! Rolling back..."
              kubectl apply -f deploy/stable-virtualservice.yaml
              exit 1
            fi
            sleep 30
          done

  promote:
    needs: canary
    runs-on: ubuntu-latest
    steps:
      - name: Promote to 100%
        run: |
          kubectl set image deployment/myapp-stable \
            myapp=ghcr.io/will/myapp:${{ github.sha }}
          kubectl apply -f deploy/full-rollout.yaml
```

### Metricas de Canary

```python
class CanaryAnalyzer:
    def __init__(self):
        self.metrics = {
            "error_rate": 0.01,  # 1% max error rate
            "latency_p95": 500,  # 500ms max p95 latency
            "success_rate": 0.99,  # 99% min success
        }

    def should_rollback(self, canary_metrics: dict) -> bool:
        for metric, threshold in self.metrics.items():
            value = canary_metrics.get(metric, 0)
            if metric in ("error_rate", "latency_p95"):
                if value > threshold:
                    print(f"[ROLLBACK] {metric}: {value} > {threshold}")
                    return True
            else:
                if value < threshold:
                    print(f"[ROLLBACK] {metric}: {value} < {threshold}")
                    return True
        return False

    def should_promote(self, canary_metrics: dict, duration_minutes: int = 10) -> bool:
        if duration_minutes < 10:
            return False
        return not self.should_rollback(canary_metrics)
```

## Blue-Green Deployment

Blue-green mantem dois ambientes (atual e novo) e faz switch de trafego.

### Kubernetes Blue-Green

```yaml
# blue-deployment.yaml (versao atual)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-blue
  labels:
    app: myapp
    color: blue
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      color: blue
  template:
    metadata:
      labels:
        app: myapp
        color: blue
    spec:
      containers:
        - name: app
          image: ghcr.io/will/myapp:1.0.0
          ports:
            - containerPort: 8080
---
# green-deployment.yaml (nova versao)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-green
  labels:
    app: myapp
    color: green
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      color: green
  template:
    metadata:
      labels:
        app: myapp
        color: green
    spec:
      containers:
        - name: app
          image: ghcr.io/will/myapp:2.0.0
          ports:
            - containerPort: 8080
---
# service.yaml (aponta para o ambiente ativo)
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  selector:
    app: myapp
    color: blue  # Muda para green quando validado
  ports:
    - port: 80
      targetPort: 8080
```

### Script de Blue-Green

```bash
# blue-green-deploy.sh
#!/bin/bash
set -e

ENVIRONMENT=$1
VERSION=$2
COLOR_INACTIVE=$(kubectl get service myapp -o jsonpath='{.spec.selector.color}')

if [ "$COLOR_INACTIVE" == "blue" ]; then
  NEW_COLOR="green"
else
  NEW_COLOR="blue"
fi

echo "Deploying $VERSION as $NEW_COLOR (inactive)"

# Deploy nova versao
kubectl set image deployment/myapp-$NEW_COLOR \
  app=ghcr.io/will/myapp:$VERSION

# Aguardar rollout
kubectl rollout status deployment/myapp-$NEW_COLOR

# Smoke tests
SMOKE_URL=$(kubectl get svc myapp-$NEW_COLOR -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
if ! curl -f http://$SMOKE_URL/health; then
  echo "Smoke test failed!"
  exit 1
fi

# Switch trafego
kubectl patch service myapp -p "{\"spec\":{\"selector\":{\"color\":\"$NEW_COLOR\"}}}"

echo "Switch complete! Active: $NEW_COLOR"
```

## Feature Flags

Feature flags permitem ativar/desativar funcionalidades sem deploy.

### Implementacao Basica

```python
class FeatureFlags:
    def __init__(self, flags: dict[str, bool]):
        self.flags = flags

    def is_enabled(self, flag_name: str, user_id: str | None = None) -> bool:
        if flag_name not in self.flags:
            return False

        # Flag global
        if isinstance(self.flags[flag_name], bool):
            return self.flags[flag_name]

        # Flag por percentual
        if isinstance(self.flags[flag_name], dict):
            config = self.flags[flag_name]
            if user_id and "percentage" in config:
                user_hash = hash(f"{user_id}:{flag_name}") % 100
                return user_hash < config["percentage"]
            return config.get("default", False)

        return False

    def get_active_flags(self, user_id: str | None = None) -> dict[str, bool]:
        return {
            name: self.is_enabled(name, user_id)
            for name in self.flags
        }

# Configuracao
flags = FeatureFlags({
    "new-checkout-flow": {"percentage": 50, "default": False},
    "dark-mode": True,
    "experimental-search": False,
    "ai-recommendations": {"percentage": 10, "default": False},
})
```

### Feature Flags com LaunchDarkly

```python
import ldclient
from ldclient.config import Config

class LaunchDarklyClient:
    def __init__(self, sdk_key: str):
        ldclient.set_config(Config(sdk_key))
        self.client = ldclient.get()

    def get_flag(self, flag_key: str, user_key: str, default: bool = False) -> bool:
        user = {"key": user_key, "custom": {"plan": "premium"}}
        return self.client.variation(flag_key, user, default)

    def close(self):
        self.client.close()

# Uso
ld = LaunchDarklyClient(os.getenv("LAUNCHDARKLY_SDK_KEY"))
if ld.get_flag("new-payment-flow", user.id):
    return new_payment_flow()
else:
    return legacy_payment_flow()
```

### Feature Flags em CI/CD

```yaml
# Deploy com feature flags
jobs:
  deploy:
    steps:
      - name: Deploy with flags
        run: |
          # Deploy com flags desativadas
          kubectl apply -f deploy/
          kubectl set env deployment/myapp FEATURE_NEW_UI=false

          # Ativar para canary
          kubectl set env deployment/myapp-canary FEATURE_NEW_UI=true

          # Monitorar e ativar gradualmente
          for percent in 10 25 50 75 100; do
            kubectl set env deployment/myapp \
              FEATURE_NEW_UI_PERCENT=$percent
            sleep 300  # Aguarda 5 min entre incrementos
          done
```

## Promotion Strategies Comparison

| Estrategia | Downtime | Complexidade | Rollback | Custo | Caso de Uso |
|------------|----------|--------------|----------|-------|-------------|
| Rolling Update | Nao | Baixa | Medio | Baixo | Aplicacoes stateless |
| Blue-Green | Nao | Media | Rapido | Alto | Sistemas criticos |
| Canary | Nao | Alta | Gradual | Medio | Validacao controlada |
| Recreate | Sim | Baixa | Lento | Baixo | Ambientes dev |
| Feature Flags | Nao | Alta | Instantaneo | Medio | Funcionalidades |

## Rollback Strategies

```yaml
# Kubernetes Rollback
jobs:
  rollback:
    steps:
      - name: Rollback deployment
        run: |
          kubectl rollout undo deployment/myapp
          kubectl rollout status deployment/myapp

      - name: Rollback to specific revision
        run: |
          kubectl rollout undo deployment/myapp --to-revision=3
```

```python
# Rollback handler
class RollbackHandler:
    def __init__(self):
        self.current_release = None
        self.releases = []

    def record_release(self, version: str, timestamp: str):
        self.releases.append({
            "version": version,
            "timestamp": timestamp,
            "rollback_to": self.current_release
        })
        self.current_release = version

    def rollback(self, steps: int = 1) -> str | None:
        if steps > len(self.releases):
            return None

        target = self.releases[-steps]
        self.current_release = target["version"]
        return target["version"]
```

## Automacao Completa

```python
class EnvironmentPromoter:
    def __init__(self):
        self.gates = []

    def add_gate(self, name: str, check_fn: callable):
        self.gates.append((name, check_fn))

    def promote(self, from_env: str, to_env: str, version: str) -> bool:
        print(f"Promovendo {from_env} -> {to_env} (versao {version})")

        for gate_name, check_fn in self.gates:
            print(f"  Gate: {gate_name}...")
            if not check_fn(version, to_env):
                print(f"  Gate {gate_name} FALHOU! Promocao bloqueada.")
                return False
            print(f"  Gate {gate_name} OK.")

        print(f"Promocao concluida: {to_env} agora na versao {version}")
        return True

promoter = EnvironmentPromoter()
promoter.add_gate("tests", lambda v, e: run_tests(e) == 0)
promoter.add_gate("security", lambda v, e: run_security_scan(e) == 0)
promoter.add_gate("performance", lambda v, e: check_performance(e))

promoter.promote("staging", "production", "v2.1.0")
```

## Referencias Cruzadas

- [[ci-cd/INDEX]] - Index de CI/CD
- [[ci-cd/github-actions]] - GitHub Actions workflow
- [[ci-cd/semantic-release]] - Versionamento semantico
- [[devops/Kubernetes]] - Orquestracao de containers
- [[devops/Observabilidade]] - Monitoramento e metricas
- [[02-software-engineering/seguranca/INDEX]] - Seguranca em deploy