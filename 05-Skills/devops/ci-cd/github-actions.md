---
tags: [skills, devops, cicd, github-actions, pipelines]
updated: 2026-06-13
title: "GitHub Actions"
date: 2026-06-01
---

# GitHub Actions

Guia completo sobre GitHub Actions: workflow syntax, matrix builds, workflows reutilizaveis, self-hosted runners, ambientes, secrets e artefatos. Inclui exemplos completos em YAML.

## Introducao

GitHub Actions e a plataforma de CI/CD nativa do GitHub. Workflows sao arquivos YAML em `.github/workflows/` que definem automaticacoes para build, test, deploy e outras tarefas.

### Estrutura Basica

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - run: pytest --cov=src --cov-report=xml
      - uses: codecov/codecov-action@v3
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
```

## Workflow Syntax

### Eventos de Gatilho (on)

```yaml
on:
  # Push em branches especificas
  push:
    branches:
      - main
      - develop
      - "feature/**"
    tags:
      - "v*"
    paths:
      - "src/**"
      - "09-Sistema/tests/**"
      - "!docs/**"

  # Pull request
  pull_request:
    branches: [main]
    types: [opened, synchronize, reopened, ready_for_review]

  # Agendado (cron)
  schedule:
    - cron: "0 6 * * 1"  # Every Monday at 6 AM

  # Manual (workflow_dispatch)
  workflow_dispatch:
    inputs:
      environment:
        description: "Target environment"
        required: true
        default: "staging"
        type: choice
        options:
          - staging
          - production
      debug_enabled:
        description: "Enable debug mode"
        required: false
        default: false
        type: boolean

  # Evento externo (repository_dispatch)
  repository_dispatch:
    types: [deploy-command]
```

### Jobs e Dependencias

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install ruff && ruff check .

  test:
    needs: lint  # Sera executado apos lint
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: pip install -r requirements.txt
      - run: pytest

  build:
    needs: [lint, test]  # Aguarda ambos
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: docker build -t myapp:${{ github.sha }} .

  deploy:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying..."
```

## Matrix Builds

### Matrix Basica

```yaml
jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: ["3.10", "3.11"]
        node-version: [18, 20]
        exclude:
          - os: windows-latest
            python-version: "3.10"
        include:
          - os: ubuntu-latest
            python-version: "3.12"
            experimental: true
    runs-on: ${{ matrix.os }}
    continue-on-error: ${{ matrix.experimental || false }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
      - run: pip install -r requirements.txt
      - run: pytest
```

### Matrix Dinamica

```yaml
jobs:
  get-matrix:
    runs-on: ubuntu-latest
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}
    steps:
      - id: set-matrix
        run: |
          echo "matrix={\"include\":[
            {\"project\": \"api\", \"port\": 8000},
            {\"project\": \"worker\", \"port\": 8001},
            {\"project\": \"frontend\", \"port\": 3000}
          ]}" >> $GITHUB_OUTPUT

  build:
    needs: get-matrix
    strategy:
      matrix: ${{ fromJson(needs.get-matrix.outputs.matrix) }}
    runs-on: ubuntu-latest
    steps:
      - run: echo "Building ${{ matrix.project }} on port ${{ matrix.port }}"
```

## Reusable Workflows

### Definindo Workflow Reutilizavel

```yaml
# .github/workflows/python-ci.yml (workflow chamavel)
name: Python CI

on:
  workflow_call:
    inputs:
      python-version:
        required: true
        type: string
        default: "3.11"
      run-lint:
        required: false
        type: boolean
        default: true
      coverage-threshold:
        required: false
        type: number
        default: 80
    secrets:
      codecov-token:
        required: false

jobs:
  lint:
    if: inputs.run-lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ inputs.python-version }}
      - run: pip install ruff && ruff check .

  test:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ inputs.python-version }}
      - run: pip install -r requirements.txt pytest pytest-cov
      - run: pytest --cov --cov-report=xml --cov-fail-under=${{ inputs.coverage-threshold }}
      - if: inputs.coverage-threshold && secrets.codecov-token
        uses: codecov/codecov-action@v3
        with:
          token: ${{ secrets.codecov-token }}
```

### Chamando Workflow Reutilizavel

```yaml
# .github/workflows/main.yml
name: Main Pipeline

on:
  push:
    branches: [main]

jobs:
  python-checks:
    uses: ./.github/workflows/python-ci.yml
    with:
      python-version: "3.11"
      run-lint: true
      coverage-threshold: 85
    secrets:
      codecov-token: ${{ secrets.CODECOV_TOKEN }}

  deploy:
    needs: python-checks
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying..."
```

### Workflow Reutilizavel de Outro Repositorio

```yaml
jobs:
  ci:
    uses: org/shared-workflows/.github/workflows/python-ci.yml@v1
    with:
      python-version: "3.11"
    secrets:
      codecov-token: ${{ secrets.CODECOV_TOKEN }}
```

## Self-Hosted Runners

### Configuracao

```yaml
# Usando runner auto-hospedado
jobs:
  build:
    runs-on: self-hosted
    # Ou com labels especificos
    runs-on: [self-hosted, linux, gpu]

    steps:
      - uses: actions/checkout@v4
      - run: nvidia-smi  # Verificar GPU
      - run: ollama pull llama3
      - run: python train.py
```

```bash
# Instalar runner no Windows
# Download do runner do repositorio > Settings > Actions > Runners
./config.cmd --url https://github.com/will/jarvis --token ABCDEF123
./run.cmd

# Instalar como servico
./svc.cmd install
./svc.cmd start
```

```yaml
# Docker Compose para runner auto-hospedado
version: "3.8"
services:
  actions-runner:
    image: summerwind/actions-runner:latest
    environment:
      - RUNNER_NAME=jarvis-runner
      - REPO_URL=https://github.com/will/jarvis
      - RUNNER_TOKEN=${RUNNER_TOKEN}
      - RUNNER_WORKDIR=/tmp/runner
      - RUNNER_GROUP=default
      - LABELS=self-hosted,linux,gpu
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - runner-data:/tmp/runner
    deploy:
      replicas: 2
```

## Environments

### Configuracao de Ambiente

```yaml
jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    environment:
      name: staging
      url: https://staging.myapp.com
    steps:
      - run: echo "Deploying to staging..."

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://myapp.com
    steps:
      - run: echo "Deploying to production..."
```

### Protection Rules

```yaml
# Environment no repositorio deve ter:
# - Required reviewers: 1
# - Wait timer: 5 minutes
# - Deployment branches: main

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - run: ./deploy.sh
```

## Secrets e Variaveis

### Secrets

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    env:
      NODE_ENV: production
    steps:
      # Secret do repositorio
      - run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login --username ${{ secrets.DOCKER_USERNAME }} --password-stdin

      # Secret do environment
      - run: ./deploy.sh
        env:
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
          API_KEY: ${{ secrets.API_KEY }}

      # Secret do OpenID Connect (OIDC)
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789:role/GitHubActions
          aws-region: us-east-1
```

### Variaveis de Ambiente

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      APP_VERSION: ${{ github.sha }}
      BUILD_TIME: ${{ github.event.head_commit.timestamp }}
    steps:
      - run: echo "Building version $APP_VERSION"

  test:
    runs-on: ubuntu-latest
    env:
      # Variavel global para todos os steps
      LOG_LEVEL: debug
    steps:
      - name: Step-1: mypy
        env:
          # Sobrescreve para este step
          LOG_LEVEL: info
        run: mypy src/

      - name: Step-2: pytest
        run: pytest
```

## Artifacts

### Upload e Download

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: |
          mkdir -p dist
          python -m build --outdir dist
      - uses: actions/upload-artifact@v4
        with:
          name: dist-files
          path: dist/
          retention-days: 5
          compression-level: 6
          if-no-files-found: error

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: dist-files
          path: dist/
      - run: ls -la dist/
```

### Multiplos Artifacts

```yaml
jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - run: pytest --junitxml=results-${{ matrix.os }}.xml
      - uses: actions/upload-artifact@v4
        with:
          name: test-results-${{ matrix.os }}
          path: results-${{ matrix.os }}.xml

  publish:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          path: all-results/
      - run: ls -la all-results/
      - run: python merge_results.py all-results/
```

## Cache

### Cache de Dependencias

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"
          cache-dependency-path: "requirements*.txt"

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: "npm"
          cache-dependency-path: "frontend/package-lock.json"

      - uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements*.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-

      - run: pip install -r requirements.txt
      - run: npm ci
      - run: pytest
```

## Conditional Execution

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      # Executa apenas no branch main
      - if: github.ref == 'refs/heads/main'
        run: ./deploy.sh production

      # Executa em PRs que nao sao drafts
      - if: github.event.pull_request.draft == false
        run: ./deploy.sh staging

      # Executa em push de tags
      - if: startsWith(github.ref, 'refs/tags/v')
        run: ./release.sh

      # Operador booleano
      - if: github.event_name == 'push' && github.ref == 'refs/heads/main'
        run: echo "Push to main"

      # Funcoes
      - if: contains(github.event.head_commit.message, '[skip ci]')
        run: echo "Skipping..."

      # Resultado de step anterior
      - if: steps.build.outputs.status == 'success'
        run: echo "Build succeeded"

      # Sempre executa, mesmo se falhar
      - if: always()
        run: echo "Cleanup"

      - if: cancelled()
        run: echo "Cancelled"

      - if: failure()
        run: echo "Failed"
```

## Workflow Completo: Python + Docker + Deploy

```yaml
name: Complete Pipeline
on:
  push:
    branches: [main, develop]
    tags: ["v*"]
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements-dev.txt
      - run: ruff check src/
      - run: mypy src/

  test:
    needs: lint
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11"]
    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_PASSWORD: testpass
          POSTGRES_DB: testdb
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          cache: "pip"
      - run: pip install -r requirements.txt
      - run: pytest --cov=src --cov-report=xml --cov-fail-under=80
        env:
          DATABASE_URL: postgresql://postgres:testpass@localhost:5432/testdb
      - uses: codecov/codecov-action@v3

  build-and-push:
    needs: test
    if: github.event_name == 'push'
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/metadata-action@v5
        id: meta
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=sha,format=long
      - uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  deploy-staging:
    needs: build-and-push
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    environment:
      name: staging
      url: https://staging.myapp.com
    steps:
      - uses: actions/checkout@v4
      - run: echo "Deploying to staging..."
      - run: kubectl set image deployment/myapp myapp=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
        env:
          KUBECONFIG: ${{ secrets.KUBECONFIG_STAGING }}

  deploy-production:
    needs: build-and-push
    if: startsWith(github.ref, 'refs/tags/v')
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://myapp.com
    steps:
      - uses: actions/checkout@v4
      - run: |
          echo "Deploying version ${GITHUB_REF#refs/tags/v} to production"
          ./scripts/deploy.sh production ${{ github.sha }}
        env:
          DEPLOY_KEY: ${{ secrets.DEPLOY_KEY }}
```

## GitHub Actions Best Practices

```yaml
# Best practices checklist
name: Best Practices
on: push

jobs:
  security:
    steps:
      # Pinning de acoes por hash (SEGURANCA)
      - uses: actions/checkout@v4  # Use SHA: actions/checkout@b4ffde6...
      # Minimizar permissoes
      - run: echo "Default permissions are read-only"

  performance:
    steps:
      # Cache de dependencias
      - uses: actions/cache@v4
      # Matrix builds paralelos
      strategy:
        matrix:
          version: [1, 2, 3]
      # Conditional job cancellation
      - if: cancelled()
        run: echo "Cleanup"

  reliability:
    steps:
      # Retry logic
      - uses: nick-fields/retry@v3
        with:
          timeout_minutes: 10
          max_attempts: 3
          command: curl -f http://service/health
      # Continue on error para testes nao criticos
      continue-on-error: true
```

## Referencias Cruzadas

- [[ci-cd/INDEX]] - Index de CI/CD
- [[ci-cd/semantic-release]] - Automacao de versionamento
- [[ci-cd/environment-promotion]] - Estrategias de promocao
- [[devops/FinOps]] - Otimizacao de custos
- [[devops/Kubernetes]] - Orquestracao de containers
- [[02-software-engineering/seguranca/supply-chain-security]] - Seguranca em pipelines
- [[02-software-engineering/seguranca/secrets-management]] - Secrets no CI/CD
- [[02-software-engineering/seguranca/INDEX]] - Seguranca da informacao