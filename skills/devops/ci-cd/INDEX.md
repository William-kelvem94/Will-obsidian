---
tags: [skills, devops, cicd, gitops, pipelines]
updated: 2026-06-05
title: "CI/CD e GitOps - Index"
date: 2026-06-01
---

# CI/CD e GitOps - Index

Guia completo sobre pipelines de integracao e entrega continua, GitOps, automacao de builds e deploy. Cobre ferramentas como GitHub Actions, versionamento semantico e estrategias de promocao de ambientes.

## Taxonomia de CI/CD

### Por Tipo
- **Continuous Integration (CI)**: Build, test, lint, security scan a cada commit
- **Continuous Delivery (CD)**: Deploy automatizado para staging, aprovacao manual para producao
- **Continuous Deployment (CD)**: Deploy automatizado para todos os ambientes
- **Continuous Testing**: Execucao de testes em pipeline

### Por Pipeline
1. **Commit Stage**: Lint, format, type-check, unit tests
2. **Build Stage**: Compilacao, build de artefatos, image build
3. **Test Stage**: Integration tests, e2e tests, security scan
4. **Release Stage**: Versionamento, changelog, release notes
5. **Deploy Stage**: Deploy para ambientes, health check

### Pipeline Matrix

```
Desenvolvimento
  └─ CI: lint + test + build
  └─ CD: deploy para dev environment
       │
       ▼
Staging
  └─ CI: integration test + security scan
  └─ CD: deploy para staging
       │
       ▼
Production
  └─ CI: smoke test + performance test
  └─ CD: canary / blue-green deploy
```

## GitOps Principles

GitOps e um modelo operacional onde o repositorio Git e a fonte unica de verdade para infraestrutura e aplicacoes.

### Principios Fundamentais

1. **Declarative Description**: Todo o sistema e descrito declarativamente (Kubernetes manifests, Terraform, Helm)
2. **Versioned and Immutable**: Tudo versionado no Git, mudancas sao imutaveis
3. **Pulled Automatically**: Mudancas sao puxadas automaticamente (pull-based deployment)
4. **Continuously Reconciled**: O estado real e continuamente reconciliado com o estado desejado

```yaml
# Exemplo: FluxCD GitRepo reconciler
apiVersion: source.toolkit.fluxcd.io/v1beta2
kind: GitRepository
metadata:
  name: flux-system
  namespace: flux-system
spec:
  interval: 1m
  url: https://github.com/will/infrastructure
  ref:
    branch: main
  secretRef:
    name: flux-system-auth
---
apiVersion: kustomize.toolkit.fluxcd.io/v1beta2
kind: Kustomization
metadata:
  name: apps
  namespace: flux-system
spec:
  interval: 10m
  path: ./apps/production
  prune: true
  sourceRef:
    kind: GitRepository
    name: flux-system
  healthChecks:
    - apiVersion: apps/v1
      kind: Deployment
      name: myapp
      namespace: production
```

## Tools Overview

| Ferramenta | Tipo | Caso de Uso |
|------------|------|-------------|
| GitHub Actions | CI/CD SaaS | Pipelines integrados ao GitHub |
| GitLab CI | CI/CD SaaS/Self-hosted | Pipelines GitLab native |
| Jenkins | CI/CD Server | Pipelines complexos, legacy |
| ArgoCD | GitOps | Deploy continuo Kubernetes |
| FluxCD | GitOps | GitOps operator Kubernetes |
| CircleCI | CI/CD SaaS | Performance, caching |
| Buildkite | CI/CD Hybrid | Agentes customizados |

## Estrategias de Deploy

### Por Fluxo
- **Push-based**: CI/CD tool faz push dos artefatos para o ambiente
- **Pull-based**: Agent no cluster puxa o estado desejado do Git

### Por Estrategia
- **Recreate**: Para o servico antigo, cria o novo (downtime)
- **Rolling Update**: Substitui gradualmente pods (sem downtime)
- **Blue-Green**: Mantem dois ambientes, switch de trafego
- **Canary**: Libera para percentual pequeno, aumenta gradualmente
- **Feature Flags**: Libera funcionalidades sem deploy

## Ferramentas de Automacao

### Semantic Release
```bash
# Automatiza versionamento e changelog
npx semantic-release
# Analisa commits convencionais, calcula versao,
# gera changelog, cria release no GitHub
```

### Dependabot / Renovate
```yaml
# Automatizacao de atualizacao de dependencias
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
```

## Pipeline de Referencia

```yaml
name: Full Pipeline
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install ruff && ruff check .

  test:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements.txt
      - run: pytest --cov --cov-report=xml
      - uses: codecov/codecov-action@v3

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: docker build -t myapp:${{ github.sha }} .
      - run: docker tag myapp:${{ github.sha }} ghcr.io/will/myapp:latest

  deploy:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production
    steps:
      - run: echo "Deploying to production..."
```

## Referencias Cruzadas

- [[ci-cd/github-actions]] - GitHub Actions workflow syntax e exemplos
- [[ci-cd/semantic-release]] - Versionamento semantico automatizado
- [[ci-cd/environment-promotion]] - Estrategias de promocao entre ambientes
- [[devops/FinOps]] - Otimizacao de custos em nuvem
- [[devops/Kubernetes]] - Orquestracao de containers
- [[devops/Observabilidade]] - Monitoramento e observabilidade
- [[02-software-engineering/seguranca/supply-chain-security]] - Seguranca em pipelines
- [[02-software-engineering/seguranca/secrets-management]] - Secrets em CI/CD