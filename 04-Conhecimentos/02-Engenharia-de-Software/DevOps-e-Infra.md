---
title: "DevOps e Infraestrutura"
date: 2026-05-16
area: "Programação e Engenharia de Software"
tags: [conhecimento, devops, infra, docker, kubernetes, cicd, cloud, terraform, observabilidade]
related: ["04-Conhecimentos/02-Engenharia-de-Software/INDEX", "04-Conhecimentos/02-Engenharia-de-Software/Performance-e-Otimizacao", "05-Skills/03-infrastructure-mcp/local-llm-ops", "05-Skills/devops"]
aliases: ["DevOps", "Infrastructure", "CI/CD", "Cloud Computing"]
---

# DevOps e Infraestrutura

> *"You build it, you run it."* — Werner Vogels (CTO Amazon)

---

## 1. CI/CD (Integração Contínua e Entrega Contínua)

### 1.1 Conceitos Fundamentais

| Prática | Descrição |
|---------|-----------|
| **Integração Contínua (CI)** | Cada commit é validado automaticamente (build + testes) |
| **Entrega Contínua (CD)** | Código validado é automaticamente preparado para deploy em produção |
| **Deploy Contínuo** | Cada commit que passa pela CI é automaticamente deployado em produção |

**Pipeline stages típicos:**
1. **Checkout** — clonagem do repositório
2. **Lint/Format** — verificação de estilo (ESLint, Ruff, Prettier)
3. **Build** — compilação/transpilação
4. **Testes Unitários** — pytest, vitest, JUnit
5. **Testes de Integração** — testes com dependências reais
6. **SAST/SCA** — análise estática de segurança (Semgrep, Snyk)
7. **Build de Imagem Docker** — criação da imagem otimizada
8. **Push para Registry** — Docker Hub, ECR, GCR, GHCR
9. **Deploy (Staging)** — ambiente de homologação
10. **Testes E2E** — Cypress, Playwright
11. **Deploy (Produção)** — rollout gradual (canary, blue-green)

### 1.2 GitHub Actions

```yaml
# .github/workflows/ci.yml
name: CI Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_DB: testdb
          POSTGRES_PASSWORD: test
        ports:
          - 5432:5432
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: pip
      - run: pip install -r requirements.txt
      - run: pytest --cov --cov-report=xml
      - uses: codecov/codecov-action@v4
        with:
          file: ./coverage.xml

  docker:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: |
          docker build -t app:${{ github.sha }} .
          docker tag app:${{ github.sha }} ghcr.io/${{ github.repository }}:latest
      - run: echo "${{ secrets.GITHUB_TOKEN }}" | docker login ghcr.io -u ${{ github.actor }} --password-stdin
      - run: docker push ghcr.io/${{ github.repository }}:latest
```

### 1.3 GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - lint
  - test
  - build
  - deploy

variables:
  IMAGE_TAG: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA

lint:
  stage: lint
  image: python:3.12-slim
  script:
    - pip install ruff
    - ruff check .

test:
  stage: test
  image: python:3.12-slim
  services:
    - postgres:16
  variables:
    DATABASE_URL: postgres://postgres:password@postgres:5432/testdb
  script:
    - pip install -r requirements.txt
    - pytest --junitxml=report.xml
  artifacts:
    reports:
      junit: report.xml

build:
  stage: build
  image: docker:27
  services:
    - docker:dind
  script:
    - docker build -t $IMAGE_TAG .
    - docker push $IMAGE_TAG

deploy:
  stage: deploy
  image: alpine/k8s:1.29
  script:
    - kubectl set image deployment/app app=$IMAGE_TAG
  only:
    - main
```

### 1.4 Estratégias de Deploy

| Estratégia | Descrição | Tempo de Rollout | Rollback |
|------------|-----------|-------------------|----------|
| **Rolling Update** | Substitui pods gradualmente | Lento | Automático |
| **Blue-Green** | Duas versões completas; switch de DNS | Instantâneo | Imediato |
| **Canary** | Versão nova recebe X% do tráfego | Gradual | Fácil |
| **A/B Testing** | Canary + roteamento por features | Controlado | Fácil |

---

## 2. Docker

### 2.1 Conceitos Essenciais

- **Imagem**: snapshot imutável de um sistema de arquivos + metadados
- **Container**: processo isolado rodando a partir de uma imagem
- **Dockerfile**: receita para construir uma imagem
- **Registry**: repositório de imagens (Docker Hub, ECR, GCR)
- **Layer**: cada instrução no Dockerfile cria uma camada cacheável

### 2.2 Dockerfile Multi-Stage

```dockerfile
# Stage 1: Build
FROM node:20-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Runtime (imagem final ~120MB vs ~1.2GB)
FROM nginx:1.27-alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget -qO- http://localhost:80/health || exit 1
```

```dockerfile
# Python multi-stage
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dirs -r requirements.txt

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 2.3 Docker Compose

```yaml
# docker-compose.yml
version: "3.9"

services:
  api:
    build: ./api
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgres://user:pass@db:5432/app
      - REDIS_URL=redis://cache:6379
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_started
    volumes:
      - ./api:/app  # apenas dev
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s

  db:
    image: postgres:16-alpine
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: app
      POSTGRES_USER: user
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d app"]
      interval: 10s

  cache:
    image: redis:7-alpine
    volumes:
      - redis-data:/data

volumes:
  pgdata:
  redis-data:
```

### 2.4 Docker Networking

| Driver | Escopo | Uso |
|--------|--------|-----|
| `bridge` | Container único | Padrão, isolamento via NAT |
| `host` | Container único | Sem isolamento de rede (performance) |
| `overlay` | Multi-host | Swarm/K8s, comunicação entre nós |
| `macvlan` | Container único | IP real na rede física |
| `none` | Container único | Sem rede |

### 2.5 Volumes e Dados Persistentes

```bash
# Volumes gerenciados pelo Docker
docker volume create app-data
docker run -v app-data:/data app

# Bind mounts (caminho do host)
docker run -v /host/path:/container/path app

# tmpfs (apenas em memória — dados voláteis)
docker run --tmpfs /app/cache app
```

---

## 3. Kubernetes

### 3.1 Arquitetura

```
┌─────────────────────────────────────────────┐
│                 Control Plane                │
│  ┌────────┐  ┌────────┐  ┌──────────────┐   │
│  │  etcd  │  │  API   │  │  Scheduler   │   │
│  │ (chave)│  │ Server │  │              │   │
│  └────────┘  └────────┘  └──────────────┘   │
│  ┌────────┐  ┌────────┐                      │
│  │Controller│ │Cloud   │                      │
│  │ Manager │  │Provider│                      │
│  └────────┘  └────────┘                      │
├─────────────────────────────────────────────┤
│                 Node 1                       │
│  ┌────────┐  ┌──────────┐  ┌──────────┐     │
│  │ Kubelet │  │  kube-   │  │ Pods     │     │
│  │         │  │  proxy   │  │ (cont.)  │     │
│  └────────┘  └──────────┘  └──────────┘     │
└─────────────────────────────────────────────┘
```

### 3.2 Pods

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-pod
  labels:
    app: web
    env: production
spec:
  containers:
    - name: app
      image: myapp:1.0.0
      ports:
        - containerPort: 3000
      resources:
        requests:
          cpu: 250m
          memory: 128Mi
        limits:
          cpu: 500m
          memory: 256Mi
      livenessProbe:
        httpGet:
          path: /health
          port: 3000
        initialDelaySeconds: 5
        periodSeconds: 10
      readinessProbe:
        httpGet:
          path: /ready
          port: 3000
        initialDelaySeconds: 3
      env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: database-url
```

### 3.3 Deployments

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
        - name: api
          image: myapi:2.1.0
          ports:
            - containerPort: 8080
          envFrom:
            - configMapRef:
                name: api-config
            - secretRef:
                name: api-secrets
```

### 3.4 Services

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api-service
spec:
  type: ClusterIP  # ClusterIP | NodePort | LoadBalancer | ExternalName
  selector:
    app: api
  ports:
    - protocol: TCP
      port: 80        # porta do Service
      targetPort: 8080  # porta do container
```

### 3.5 Ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: api-ingress
  annotations:
    nginx.ingress.kubernetes.io/rate-limit: "10r/s"
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - api.mydomain.com
      secretName: api-tls
  rules:
    - host: api.mydomain.com
      http:
        paths:
          - path: /v1
            pathType: Prefix
            backend:
              service:
                name: api-service
                port:
                  number: 80
```

### 3.6 ConfigMaps e Secrets

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: api-config
data:
  LOG_LEVEL: "info"
  MAX_CONNECTIONS: "100"
---
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: api-secrets
stringData:
  API_KEY: "sk-..."
  DATABASE_URL: "postgres://..."
```

### 3.7 Helm (Package Manager)

```bash
# Estrutura de um chart
helm create my-app
# my-app/
# ├── Chart.yaml          # metadados
# ├── values.yaml         # valores padrão
# ├── templates/          # templates Go
# │   ├── deployment.yaml
# │   ├── service.yaml
# │   └── _helpers.tpl
# └── charts/             # dependências
```

```yaml
# values.yaml
replicaCount: 3
image:
  repository: my-app
  tag: latest
  pullPolicy: IfNotPresent
service:
  type: ClusterIP
  port: 80
ingress:
  enabled: true
  host: app.mydomain.com
resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 200m
    memory: 256Mi
```

```bash
# Comandos úteis
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-release bitnami/postgresql -f values.yaml
helm upgrade my-release bitnami/postgresql --set auth.password=newpass
helm rollback my-release 1
helm list
```

---

## 4. Cloud Computing

### 4.1 Amazon Web Services (AWS)

| Serviço | Categoria | Descrição |
|---------|-----------|-----------|
| **EC2** | Compute | Máquinas virtuais (instâncias) |
| **Lambda** | Serverless | Funções event-driven (FaaS) |
| **ECS/EKS** | Containers | Docker/ Kubernetes gerenciado |
| **S3** | Storage | Object storage com 11 noves de durabilidade |
| **RDS** | Database | Bancos relacionais gerenciados (Postgres, MySQL, etc.) |
| **DynamoDB** | NoSQL | Key-value + document store |
| **VPC** | Networking | Rede virtual isolada |
| **CloudFront** | CDN | Distribuição global com edge caching |
| **Route53** | DNS | Serviço de DNS gerenciado |
| **IAM** | Security | Identidade e acesso |

```python
import boto3

s3 = boto3.client("s3")

# Upload de arquivo com criptografia
s3.upload_file(
    "local.pdf",
    "meu-bucket",
    "relatorios/2026/05/relatorio.pdf",
    ExtraArgs={
        "ServerSideEncryption": "AES256",
        "StorageClass": "INTELLIGENT_TIERING",
    },
)

# Lambda handler
def lambda_handler(event, context):
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]
        print(f"Novo arquivo: s3://{bucket}/{key}")
    return {"statusCode": 200}
```

### 4.2 Google Cloud Platform (GCP)

| Serviço | AWS Equivalente | Descrição |
|---------|----------------|-----------|
| **Compute Engine** | EC2 | VMs |
| **Cloud Functions** | Lambda | Serverless FaaS |
| **Cloud Run** | — | Containers serverless (Knative) |
| **GKE** | EKS | Kubernetes gerenciado |
| **Cloud Storage** | S3 | Object storage |
| **BigQuery** | Athena/Redshift | Data warehouse serverless |
| **Cloud SQL** | RDS | Bancos relacionais gerenciados |
| **Firestore** | DynamoDB | NoSQL serverless |

### 4.3 Microsoft Azure

| Serviço | AWS Equivalente | Descrição |
|---------|----------------|-----------|
| **Azure VMs** | EC2 | Máquinas virtuais |
| **Azure Functions** | Lambda | Funções serverless |
| **AKS** | EKS | Kubernetes gerenciado |
| **Blob Storage** | S3 | Object storage |
| **Cosmos DB** | DynamoDB | NoSQL multi-model |
| **Azure SQL** | RDS | SQL Server gerenciado |

### 4.4 Well-Architected Framework (AWS)

| Pilar | Descrição |
|-------|-----------|
| **Excelência Operacional** | Automatizar mudanças, responder a eventos |
| **Segurança** | Identidade, proteção de dados, rastreabilidade |
| **Confiabilidade** | Recuperação de falhas, escalabilidade |
| **Eficiência de Performance** | Recursos corretos para cada carga |
| **Otimização de Custos** | Evitar gastos desnecessários |
| **Sustentabilidade** | Minimizar impacto ambiental |

---

## 5. Infrastructure as Code (IaC)

### 5.1 Terraform (HashiCorp)

```hcl
# main.tf
terraform {
  required_version = ">= 1.8"
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}

provider "aws" {
  region = "us-east-1"
}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  name = "main-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-east-1a", "us-east-1b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = false
  enable_dns_hostnames = true
}

resource "aws_ecs_cluster" "main" {
  name = "main-cluster"
}

resource "aws_ecs_service" "api" {
  name            = "api-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.api.arn
  desired_count   = 3
  launch_type     = "FARGATE"

  network_configuration {
    subnets         = module.vpc.private_subnets
    security_groups = [aws_security_group.api.id]
  }
}
```

### 5.2 Pulumi (Programável)

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

const vpc = new awsx.ec2.Vpc("main", {
  cidrBlock: "10.0.0.0/16",
  numberOfAvailabilityZones: 2,
  natGateways: { strategy: "Single" },
});

const cluster = new aws.ecs.Cluster("main", { name: "main-cluster" });

const alb = new awsx.lb.ApplicationLoadBalancer("web", {
  vpc,
  external: true,
  securityGroups: [],
});

const service = new awsx.ecs.FargateService("api", {
  cluster,
  taskDefinitionArgs: {
    containers: {
      api: {
        image: "myapp:latest",
        cpu: 256,
        memory: 512,
        portMappings: [{ containerPort: 8080, targetGroup: alb.defaultTargetGroup }],
      },
    },
  },
  desiredCount: 3,
});

export const url = alb.loadBalancer.dnsName;
```

### 5.3 Ansible (Configuração)

```yaml
---
- name: Provisionar servidor web
  hosts: webservers
  become: yes
  vars:
    app_user: deploy
    app_dir: /var/www/app

  tasks:
    - name: Instalar dependências do sistema
      apt:
        name:
          - nginx
          - python3
          - python3-pip
          - certbot
        state: present
        update_cache: yes

    - name: Criar usuário deploy
      user:
        name: "{{ app_user }}"
        shell: /bin/bash
        create_home: yes

    - name: Configurar nginx
      template:
        src: templates/nginx.conf.j2
        dest: /etc/nginx/sites-available/app
      notify: restart nginx

    - name: Ativar site
      file:
        src: /etc/nginx/sites-available/app
        dest: /etc/nginx/sites-enabled/app
        state: link

    - name: Deploy da aplicação
      git:
        repo: https://github.com/org/app.git
        dest: "{{ app_dir }}"
        version: main
      become_user: "{{ app_user }}"

    - name: Instalar dependências Python
      pip:
        requirements: "{{ app_dir }}/requirements.txt"
        virtualenv: "{{ app_dir }}/venv"

  handlers:
    - name: restart nginx
      service:
        name: nginx
        state: restarted
```

### 5.4 Comparação de Ferramentas IaC

| Ferramenta | Abordagem | Estado | Linguagem | Melhor para |
|------------|-----------|--------|-----------|-------------|
| **Terraform** | Declarativo | Remoto (state file) | HCL | Multi-cloud, provisionamento |
| **Pulumi** | Imperativo/Declarativo | Remoto | Python/TS/Go/Java | Times de dev que preferem código real |
| **Ansible** | Imperativo (push) | Stateless | YAML | Configuração de servidores existentes |
| **CloudFormation** | Declarativo | Gerenciado | JSON/YAML | Apenas AWS |
| **CDK** | Imperativo/Declarativo | Gerenciado | TS/Python/Java/etc. | AWS + programação |

---

## 6. Observabilidade

### 6.1 Os Três Pilares

```
                    ┌──────────────┐
                    │ Observability │
                    └──────┬───────┘
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
    ┌──────────┐    ┌──────────┐    ┌──────────┐
    │  LOGS    │    │ METRICS  │    │  TRACES  │
    │ (eventos)│    │ (agreg.) │    │ (fluxo)  │
    └──────────┘    └──────────┘    └──────────┘
```

### 6.2 Logging — ELK Stack (Elasticsearch, Logstash, Kibana)

```yaml
# docker-compose para ELK (simplificado)
version: "3.9"
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.14
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
    ports:
      - "9200:9200"
    volumes:
      - esdata:/usr/share/elasticsearch/data

  logstash:
    image: docker.elastic.co/logstash/logstash:8.14
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf
    ports:
      - "5000:5000"

  kibana:
    image: docker.elastic.co/kibana/kibana:8.14
    ports:
      - "5601:5601"
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200

volumes:
  esdata:
```

**Alternativa moderna:** **Loki** (Grafana Labs) — lightweight, index-free, integrado com Prometheus e Grafana.

```yaml
# docker-compose para Loki + Grafana
services:
  loki:
    image: grafana/loki:3.0
    ports:
      - "3100:3100"

  promtail:
    image: grafana/promtail:3.0
    volumes:
      - /var/log:/var/log
      - ./promtail-config.yml:/etc/promtail/config.yml

  grafana:
    image: grafana/grafana:11.0
    ports:
      - "3000:3000"
```

### 6.3 Métricas — Prometheus + Grafana

```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: "api"
    static_configs:
      - targets: ["localhost:8000"]
    metrics_path: /metrics
```

```python
# app.py — exportando métricas Prometheus com Python
from prometheus_client import Counter, Histogram, generate_latest, REGISTRY
from flask import Flask, Response
import time

app = Flask(__name__)

REQUEST_COUNT = Counter("http_requests_total", "Total requests", ["method", "endpoint"])
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "Latency", ["method", "endpoint"])


@app.route("/api/data")
def get_data():
    REQUEST_COUNT.labels(method="GET", endpoint="/api/data").inc()
    start = time.time()
    result = {"message": "ok"}
    REQUEST_LATENCY.labels(method="GET", endpoint="/api/data").observe(time.time() - start)
    return result


@app.route("/metrics")
def metrics():
    return Response(generate_latest(REGISTRY), mimetype="text/plain")
```

**4 sinais dourados (Google SRE):**
1. **Latência** — tempo para responder
2. **Tráfego** — demanda no sistema (RPS, throughput)
3. **Erros** — taxa de falhas explícitas e implícitas
4. **Saturação** — quão "cheio" o sistema está

### 6.4 Tracing Distribuído — OpenTelemetry

```python
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Configurar tracer
provider = TracerProvider()
exporter = OTLPSpanExporter(endpoint="http://otel-collector:4317")
provider.add_span_processor(BatchSpanProcessor(exporter))
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("processar-pedido") as span:
    span.set_attribute("pedido.id", "12345")
    with tracer.start_as_current_span("calcular-frete") as child:
        child.set_attribute("cep", "01310-100")
        # ... lógica do cálculo
```

### 6.5 Alertas

```yaml
# PrometheusRule (K8s)
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: api-alerts
spec:
  groups:
    - name: api
      rules:
        - alert: HighErrorRate
          expr: |
            rate(http_requests_total{status=~"5.."}[5m])
            /
            rate(http_requests_total[5m]) > 0.05
          for: 5m
          labels:
            severity: critical
          annotations:
            summary: "Taxa de erro acima de 5%"
            description: "API {{ $labels.job }} com {{ $value | humanizePercentage }} de erros"

        - alert: HighLatency
          expr: histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m])) > 2
          for: 10m
          labels:
            severity: warning
          annotations:
            summary: "P99 de latência acima de 2s"
```

---

## 7. FinOps (Otimização de Custos)

### 7.1 Princípios FinOps

```
┌─────────────────────────────────────┐
│           FINOPS CYCLE              │
│                                     │
│   Inform → Optimize → Operate      │
│      ┌─────────────────────┐       │
│      │ 1. Visibility       │       │
│      │ 2. Allocation       │       │
│      │ 3. Benchmarking     │       │
│      │ 4. Rightsizing      │       │
│      │ 5. Reserved Inst.   │       │
│      └─────────────────────┘       │
└─────────────────────────────────────┘
```

### 7.2 Estratégias por Serviço

| Serviço | Estratégia | Economia Potencial |
|---------|-----------|-------------------|
| **EC2/Compute** | Reserved Instances / Savings Plans | 30–60% |
| **EC2** | Spot Instances (cargas tolerantes a falha) | 60–90% |
| **S3** | Intelligent Tiering / Lifecycle Policies | 20–40% |
| **RDS** | Reserved Instances | 30–60% |
| **Lambda** | Aumentar memória (mais rápido = mais barato) | 10–30% |
| **EBS** | Snapshots incrementais, apagar volumes não usados | Variável |
| **Data Transfer** | CloudFront, compressão, cache | 20–50% |

### 7.3 Kubernetes Cost Optimization

```yaml
# Vertical Pod Autoscaler (VPA)
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: api-vpa
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api-deployment
  updatePolicy:
    updateMode: Auto  # Auto | Initial | Off
  resourcePolicy:
    containerPolicies:
      - containerName: "*"
        minAllowed:
          cpu: 100m
          memory: 128Mi
        maxAllowed:
          cpu: 2
          memory: 4Gi
```

```bash
# kubectl cost (kubecost)
kubectl cost --namespace prod --window d7
kubectl cost --label app=api --window m1

# Ferramentas: Kubecost, Karpenter (node auto-scaling), Goldilocks
```

### 7.4 Tagging Strategy

```bash
# Tags obrigatórias em todos os recursos
tags:
  Environment: "production"    # production, staging, development
  CostCenter: "eng-123"        # centro de custo
  Owner: "time-api"            # time responsável
  Project: "platform"          # projeto
  Terraform: "true"            # gerenciado por IaC
  AutoStop: "false"            # pode desligar fora do horário?
```

---

## 8. SRE (Site Reliability Engineering)

### 8.1 SLIs, SLOs, SLAs

| Termo | Definição | Exemplo |
|-------|-----------|---------|
| **SLI** (Indicator) | Medição real da confiabilidade | Proporção de requests com latência < 200ms |
| **SLO** (Objective) | Meta de confiabilidade | 99.9% dos requests em < 200ms |
| **SLA** (Agreement) | Compromisso contratual | 99.95% de uptime, multa de 10% se não cumprir |

### 8.2 Error Budget

```
Error Budget = 100% - SLO

Com SLO de 99.9%:
- Error Budget mensal = 0.1% × 30 dias × 24h × 3600s ≈ 259 segundos de downtime
- Enquanto o budget não for exaurido, deploys podem continuar
- Se o budget acabar, deploys são congelados até recuperar
```

---

## Referências

- Breda, G. et al. (2023). *Kubernetes: Practical Guide for Developers*. O'Reilly.
- Burns, B. et al. (2022). *Kubernetes: Up and Running* (3ª ed.). O'Reilly.
- Turnbull, J. (2023). *The Docker Book*. Independently Published.
- Beyer, B. et al. (2016). *Site Reliability Engineering*. O'Reilly.
- Haff, G. (2021). *Terraform: Up and Running* (3ª ed.). O'Reilly.
- **AWS Well-Architected Framework** — https://aws.amazon.com/architecture/well-architected/
- **FinOps Foundation** — https://www.finops.org/
- **OpenTelemetry Documentation** — https://opentelemetry.io/docs/

---

## Conexões

- [[04-Conhecimentos/02-Engenharia-de-Software/INDEX]] — Índice geral da área de programação
- [[04-Conhecimentos/02-Engenharia-de-Software/Performance-e-Otimizacao]] — Otimização de sistemas
- [[04-Conhecimentos/02-Engenharia-de-Software/Seguranca]] — Práticas de segurança em infraestrutura
- [[04-Conhecimentos/02-Engenharia-de-Software/Banco-de-Dados]] — Armazenamento e gerenciamento de dados
- [[05-Skills/03-infrastructure-mcp/local-llm-ops]] — Operações locais de LLM
- [[05-Skills/devops]] — Práticas DevOps

---

*"Hope is not a strategy."* — Tradição SRE
