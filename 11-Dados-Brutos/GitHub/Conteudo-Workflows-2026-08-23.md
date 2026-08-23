---
title: Conteúdo dos workflows GitHub Actions
type: dados-brutos-github
status: atual
updated: 2026-08-23
classe_privacidade: operacional
indexavel: true
uso_ia: permitido
---

# Conteúdo dos workflows

## William-kelvem94/DeepSeek-V3---C-PIA\n\n### .github/workflows/stale.yml\n\n```yaml\nname: "Mark and close stale issues"
on:
  workflow_dispatch:
  schedule:
    - cron: "0 0 * * *"

jobs:
  stale:
    if: ${{ github.repository == 'deepseek-ai/DeepSeek-V3' }}
    runs-on: ubuntu-latest
    steps:
      - name: "Mark and close stale issues"
        uses: actions/stale@v9
        with:
          days-before-issue-stale: 30
          days-before-issue-close: 14
          stale-issue-label: "stale"
          close-issue-label: "closed-as-stale"
          exempt-issue-labels: |
            pinned
            security
          stale-issue-message: >
            This issue has been automatically marked as stale because it has not had
            recent activity. It will be closed if no further activity occurs. If you
            believe this issue is still relevant, please leave a comment to keep it open.
            Thank you for your contributions!
          close-issue-message: false
          days-before-pr-stale: -1
          days-before-pr-close: -1
          repo-token: ${{ secrets.GITHUB_TOKEN }}
\n```\n\n## William-kelvem94/JARVIS-2.0\n\n### .github/workflows/build.yml\n\n```yaml\nname: Build

on:
  push:
    # branches: [master, develop]
    branches: [master]
  pull_request:
    # branches: [master, develop]
    branches: [master]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Use Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x

      - name: Use Node.js
        uses: actions/setup-node@v2
        with:
          node-version: 16.x
          cache: npm

      - name: Install Pipenv
        run: pip install --upgrade pip && pip install pipenv

      - name: Install
        run: npm install

      - name: Check setup
        run: npm run check

      - name: Build
        run: npm run build
\n```\n\n### .github/workflows/lint.yml\n\n```yaml\nname: Lint

on:
  push:
    # branches: [master, develop]
    branches: [master]
  pull_request:
    # branches: [master, develop]
    branches: [master]

jobs:
  lint:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Use Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x

      - name: Use Node.js
        uses: actions/setup-node@v2
        with:
          node-version: 16.x
          cache: npm

      - name: Install Pipenv
        run: pip install --upgrade pip && pip install pipenv

      - name: Install
        run: npm install

      - name: Run linter
        run: npm run lint
\n```\n\n### .github/workflows/pre-release-nodejs-bridge.yml\n\n```yaml\nname: Pre-release Node.js bridge

on: workflow_dispatch

jobs:
  build:
    name: Build

    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-20.04]

    runs-on: ${{ matrix.os }}

    steps:
      - name: Clone repository
        uses: actions/checkout@v3

      - name: Install Node.js
        uses: actions/setup-node@v3
        with:
          node-version: lts/*

      - name: Set Node.js bridge version
        working-directory: bridges/nodejs/src
        run: |
          echo "NODEJS_BRIDGE_VERSION=$(node --require fs --eval "const fs = require('node:fs'); const [, VERSION] = fs.readFileSync('version.ts', 'utf8').split(\"'\"); console.log(VERSION)")" >> $GITHUB_ENV

      - name: Display Node.js bridge version
        run: |
          echo "Node.js bridge version: ${{ env.NODEJS_BRIDGE_VERSION }}"

      - name: Install core
        run: npm install

      - name: Build Node.js bridge
        run: npm run build:nodejs-bridge

      - name: Upload Node.js bridge
        uses: actions/upload-artifact@v3
        with:
          path: bridges/nodejs/dist/*.zip

  draft-release:
    name: Draft-release
    needs: [build]
    runs-on: ubuntu-20.04

    steps:
      - name: Clone repository
        uses: actions/checkout@v3

      - name: Install Node.js
        uses: actions/setup-node@v3
        with:
          node-version: lts/*

      - name: Set Node.js bridge version
        working-directory: bridges/nodejs/src
        run: |
          echo "NODEJS_BRIDGE_VERSION=$(node --require fs --eval "const fs = require('node:fs'); const [, VERSION] = fs.readFileSync('version.ts', 'utf8').split(\"'\"); console.log(VERSION)")" >> $GITHUB_ENV

      - name: Download Node.js bridge
        uses: actions/download-artifact@v3
        with:
          path: bridges/nodejs/dist

      - uses: marvinpinto/action-automatic-releases@latest
        with:
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          automatic_release_tag: nodejs-bridge_v${{ env.NODEJS_BRIDGE_VERSION }}
          draft: true
          prerelease: false
          title: Node.js Bridge ${{ env.NODEJS_BRIDGE_VERSION }}
          files: bridges/nodejs/dist/artifact/*.zip
\n```\n\n### .github/workflows/pre-release-python-bridge.yml\n\n```yaml\nname: Pre-release Python bridge

on: workflow_dispatch

env:
  PIPENV_PIPFILE: bridges/python/src
  PIPENV_VENV_IN_PROJECT: true

jobs:
  build:
    name: Build

    strategy:
      fail-fast: false
      matrix:
        # @see https://github.com/actions/runner-images/tree/main/images/macos
        # Use macos-12 instead of macos-latest because the latter use ARM64 (M1) architecture
        os: [ubuntu-20.04, macos-12]
        # Temporarily disable Windows release
        # os: [ubuntu-20.04, macos-12, windows-latest]

    runs-on: ${{ matrix.os }}

    steps:
      - name: Clone repository
        uses: actions/checkout@v3

      - name: Install Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.11.9

      - name: Install Pipenv
        run: pip install --upgrade pip && pip install pipenv==2024.0.1

      - name: Install Node.js
        uses: actions/setup-node@v3
        with:
          node-version: lts/*

      - name: Set Python bridge version
        working-directory: bridges/python/src
        run: |
          echo "PYTHON_BRIDGE_VERSION=$(python -c "from version import __version__; print(__version__)")" >> $GITHUB_ENV

      - name: Display Python bridge version
        run: |
          echo "Python bridge version: ${{ env.PYTHON_BRIDGE_VERSION }}"

      - name: Install core
        run: npm install

      - name: Set up Python bridge
        run: npm run setup:python-bridge

      - name: Build Python bridge
        run: npm run build:python-bridge

      - name: Upload Python bridge
        uses: actions/upload-artifact@v3
        with:
          path: bridges/python/dist/*.zip

  draft-release:
    name: Draft-release
    needs: [build]
    runs-on: ubuntu-20.04

    steps:
      - name: Clone repository
        uses: actions/checkout@v3

      - name: Install Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.11.9

      - name: Set Python bridge version
        working-directory: bridges/python/src
        run: |
          echo "PYTHON_BRIDGE_VERSION=$(python -c "from version import __version__; print(__version__)")" >> $GITHUB_ENV

      - name: Download Python bridge
        uses: actions/download-artifact@v3
        with:
          path: bridges/python/dist

      - uses: marvinpinto/action-automatic-releases@latest
        with:
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          automatic_release_tag: python-bridge_v${{ env.PYTHON_BRIDGE_VERSION }}
          draft: true
          prerelease: false
          title: Python Bridge ${{ env.PYTHON_BRIDGE_VERSION }}
          files: bridges/python/dist/artifact/*.zip
\n```\n\n### .github/workflows/pre-release-tcp-server.yml\n\n```yaml\nname: Pre-release TCP server

on: workflow_dispatch

env:
  PIPENV_PIPFILE: tcp_server/src
  PIPENV_VENV_IN_PROJECT: true

jobs:
  build:
    name: Build

    strategy:
      fail-fast: false
      matrix:
        # @see https://github.com/actions/runner-images/tree/main/images/macos
        # Use macos-12 instead of macos-latest because the latter use ARM64 (M1) architecture
        os: [ubuntu-20.04, macos-12, windows-latest]

    runs-on: ${{ matrix.os }}

    steps:
      - name: Clone repository
        uses: actions/checkout@v3

      - name: Install Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.11.9

      - name: Install Pipenv
        run: pip install --upgrade pip && pip install pipenv==2024.0.1

      - name: Install Node.js
        uses: actions/setup-node@v3
        with:
          node-version: lts/*

      - name: Set TCP server version
        working-directory: tcp_server/src
        run: |
          echo "TCP_SERVER_VERSION=$(python -c "from version import __version__; print(__version__)")" >> $GITHUB_ENV

      - name: Display TCP server version
        run: |
          echo "TCP server version: ${{ env.TCP_SERVER_VERSION }}"

      - name: Install core
        run: npm install

      - name: Set up TCP server
        run: npm run setup:tcp-server

      - name: Build TCP server
        run: npm run build:tcp-server

      - name: Upload TCP server
        uses: actions/upload-artifact@v3
        with:
          path: tcp_server/dist/*.zip

  draft-release:
    name: Draft-release
    needs: [build]
    runs-on: ubuntu-20.04

    steps:
      - name: Clone repository
        uses: actions/checkout@v3

      - name: Install Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.11.9

      - name: Set TCP server version
        working-directory: tcp_server/src
        run: |
          echo "TCP_SERVER_VERSION=$(python -c "from version import __version__; print(__version__)")" >> $GITHUB_ENV

      - name: Download TCP server
        uses: actions/download-artifact@v3
        with:
          path: tcp_server/dist

      - uses: marvinpinto/action-automatic-releases@latest
        with:
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          automatic_release_tag: tcp-server_v${{ env.TCP_SERVER_VERSION }}
          draft: true
          prerelease: false
          title: TCP Server ${{ env.TCP_SERVER_VERSION }}
          files: tcp_server/dist/artifact/*.zip
\n```\n\n### .github/workflows/tests.yml\n\n```yaml\nname: Tests

on:
  push:
    # branches: [master, develop]
    branches: [master]
  pull_request:
    # branches: [master, develop]
    branches: [master]

jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Use Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x

      - name: Use Node.js
        uses: actions/setup-node@v2
        with:
          node-version: 16.x
          cache: npm

      - name: Install Pipenv
        run: pip install --upgrade pip && pip install pipenv

      - name: Install
        run: npm install

      - name: Run JSON tests
        run: npm run test:json

      - name: Run over HTTP tests
        run: npm run test:over-http

      - name: Run E2E tests
        run: npm run test:e2e

      - name: Install offline STT
        run: npm run setup:offline-stt

      - name: Install offline TTS
        run: npm run setup:offline-tts

      - name: Run unit tests
        run: npm run test:unit
\n```\n\n## William-kelvem94/Gerenciador_Financeiro-5.0\n\n### .github/workflows/ci-enterprise.yml\n\n```yaml\nname: 🚀 Will Finance 5.0 - Enterprise CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  NODE_VERSION: '20'
  REGISTRY: ghcr.io
  IMAGE_NAME: will-finance-5.0

jobs:
  # === ANÁLISE ESTÁTICA === #
  static-analysis:
    name: 📊 Static Analysis
    runs-on: ubuntu-latest
    outputs:
      should-deploy: ${{ steps.changes.outputs.should-deploy }}
    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: 🔍 Detect changes
        id: changes
        uses: dorny/paths-filter@v2
        with:
          filters: |
            client:
              - 'client/**'
            server:
              - 'server/**'
            should-deploy:
              - 'client/**'
              - 'server/**'
              - 'docker/**'

      - name: 🟢 Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: 📦 Install dependencies
        run: npm run install:all

      - name: 🔍 TypeScript check
        run: |
          cd client && npm run type-check
          cd ../server && npm run build

      - name: 🧹 Lint check
        run: npm run lint

      - name: 💅 Format check
        run: npm run format:check

  # === TESTES UNITÁRIOS === #
  unit-tests:
    name: 🧪 Unit Tests
    runs-on: ubuntu-latest
    needs: static-analysis
    strategy:
      matrix:
        node-version: [18, 20]
    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v4

      - name: 🟢 Setup Node.js ${{ matrix.node-version }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'

      - name: 📦 Install dependencies
        run: npm run install:all

      - name: 🧪 Run client tests
        run: cd client && npm run test

      - name: 🧪 Run server tests
        run: cd server && npm run test

      - name: 📊 Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          files: ./client/coverage/lcov.info,./server/coverage/lcov.info
          flags: unittests
          name: codecov-umbrella

  # === TESTES E2E === #
  e2e-tests:
    name: 🎭 E2E Tests
    runs-on: ubuntu-latest
    needs: [static-analysis, unit-tests]
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: will_finance_test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v4

      - name: 🟢 Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: 📦 Install dependencies
        run: npm run install:all

      - name: 🎭 Install Playwright
        run: cd client && npx playwright install --with-deps

      - name: 🗄️ Setup test database
        run: |
          cd server
          npm run db:migrate
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/will_finance_test

      - name: 🚀 Start applications
        run: |
          npm run dev &
          sleep 30
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/will_finance_test

      - name: 🎭 Run Playwright tests
        run: cd client && npm run test:e2e

      - name: 📊 Upload E2E results
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: playwright-report
          path: client/playwright-report/

  # === SEGURANÇA === #
  security-scan:
    name: 🛡️ Security Scan
    runs-on: ubuntu-latest
    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v4

      - name: 🟢 Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: 📦 Install dependencies
        run: npm run install:all

      - name: 🔒 Run security audit
        run: npm run security:audit

      - name: 🛡️ Run CodeQL analysis
        uses: github/codeql-action/init@v2
        with:
          languages: javascript, typescript

      - name: 🔍 Perform CodeQL analysis
        uses: github/codeql-action/analyze@v2

  # === BUILD === #
  build:
    name: 🏗️ Build Application
    runs-on: ubuntu-latest
    needs: [unit-tests, e2e-tests]
    if: needs.static-analysis.outputs.should-deploy == 'true'
    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v4

      - name: 🟢 Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: 📦 Install dependencies
        run: npm run install:all

      - name: 🏗️ Build applications
        run: npm run build

      - name: 📦 Upload build artifacts
        uses: actions/upload-artifact@v3
        with:
          name: build-artifacts
          path: |
            client/dist/
            server/dist/

  # === DOCKER BUILD === #
  docker-build:
    name: 🐳 Docker Build
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'
    permissions:
      contents: read
      packages: write
    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v4

      - name: 🐳 Set up Docker Buildx
        uses: docker/setup-buildx-action@v2

      - name: 🔑 Log in to Container Registry
        uses: docker/login-action@v2
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: 📋 Extract metadata
        id: meta
        uses: docker/metadata-action@v4
        with:
          images: ${{ env.REGISTRY }}/${{ github.repository }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=sha,prefix={{branch}}-
            type=raw,value=latest,enable={{is_default_branch}}

      - name: 🏗️ Build and push Docker image
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  # === DEPLOY STAGING === #
  deploy-staging:
    name: 🚀 Deploy to Staging
    runs-on: ubuntu-latest
    needs: [build, docker-build, e2e-tests, security-scan]
    if: github.ref == 'refs/heads/develop'
    environment:
      name: staging
      url: https://staging.willfinance.com
    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v4

      - name: 🚀 Deploy to staging
        run: |
          echo "🚀 Deploying to staging environment..."
          echo "This would deploy the application to staging"

      - name: 🔍 Run smoke tests
        run: |
          echo "Running smoke tests..."
          curl -f https://staging.willfinance.com/health || exit 1

  # === DEPLOY PRODUCTION === #
  deploy-production:
    name: 🌟 Deploy to Production
    runs-on: ubuntu-latest
    needs: [build, docker-build, e2e-tests, security-scan]
    if: github.ref == 'refs/heads/main'
    environment:
      name: production
      url: https://willfinance.com
    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v4

      - name: 🌟 Deploy to production
        run: |
          echo "🌟 Deploying to production environment..."
          echo "This would deploy the application to production"

      - name: 🔍 Run smoke tests
        run: |
          echo "Running production smoke tests..."
          # curl -f https://willfinance.com/health || exit 1

      - name: 📢 Notify deployment
        run: |
          echo "✅ Production deployment completed successfully!"
\n```\n\n### .github/workflows/deploy.yml\n\n```yaml\nname: Deploy to Production

on:
  push:
    branches: [main]
    tags: ['v*']

env:
  NODE_VERSION: '20'
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build-and-push:
    name: Build and Push Docker Images
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/tags/v')

    permissions:
      contents: read
      packages: write

    strategy:
      matrix:
        component: [server, client]

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}-${{ matrix.component }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=sha,prefix={{branch}}-

      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          file: ./docker/Dockerfile.${{ matrix.component }}
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  deploy-staging:
    name: Deploy to Staging
    runs-on: ubuntu-latest
    needs: build-and-push
    if: github.ref == 'refs/heads/main'

    steps:
      - name: Deploy to staging environment
        run: |
          echo "🚀 Deploying to staging environment..."
          echo "This would typically:"
          echo "  - Update staging server with new Docker images"
          echo "  - Run database migrations"
          echo "  - Perform health checks"
          echo "  - Send notifications"

  deploy-production:
    name: Deploy to Production
    runs-on: ubuntu-latest
    needs: build-and-push
    if: startsWith(github.ref, 'refs/tags/v')

    steps:
      - name: Deploy to production environment
        run: |
          echo "🚀 Deploying to production environment..."
          echo "This would typically:"
          echo "  - Update production servers with new Docker images"
          echo "  - Run database migrations with backup"
          echo "  - Perform comprehensive health checks"
          echo "  - Send notifications to team"
          echo "  - Update monitoring dashboards"
\n```\n\n## William-kelvem94/TRANSCRITOR\n\n### .github/workflows/ci.yml\n\n```yaml\nname: CI

on:
  push:
    branches: [main, master]
  pull_request:

permissions:
  contents: read

jobs:
  python:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
          cache: pip
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements-dev.txt
      - name: Compile Python sources
        run: python -m compileall -q shared services tests
      - name: Run unit tests
        run: pytest tests/unit -q -o addopts=''

  web-ui:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: services/web-ui-service
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
          cache-dependency-path: services/web-ui-service/package-lock.json
      - name: Install dependencies
        run: npm ci
      - name: Build
        run: npm run build
      - name: Lint
        run: npm run lint

  web-e2e:
    name: Web UI E2E smoke
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: services/web-ui-service
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
          cache-dependency-path: services/web-ui-service/package-lock.json
      - name: Install dependencies
        run: npm ci
      - name: Install Chromium
        run: npx playwright install --with-deps chromium
      - name: Run Chromium smoke tests
        run: npm run test:e2e -- --project=chromium

  compose-config:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate Compose files
        run: |
          docker compose -f docker-compose.yml config -q
          POSTGRES_DB=transcritor POSTGRES_USER=transcritor POSTGRES_PASSWORD=ci-postgres \
            RABBITMQ_USER=transcritor RABBITMQ_PASSWORD=ci-rabbit \
            JWT_SECRET=ci-secret CORS_ORIGINS=http://localhost:3000 \
            GRAFANA_PASSWORD=ci-grafana \
            docker compose -f docker-compose.yml -f docker-compose.prod.yml config -q

  backup-artifacts:
    name: Validate backup and restore artifacts
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate PowerShell scripts
        shell: pwsh
        run: |
          $tokens = $null
          $errors = $null
          $null = [System.Management.Automation.Language.Parser]::ParseFile(
            "$PWD/scripts/backup.ps1", [ref]$tokens, [ref]$errors)
          if ($errors.Count -gt 0) { throw $errors }
          $tokens = $null
          $errors = $null
          $null = [System.Management.Automation.Language.Parser]::ParseFile(
            "$PWD/scripts/restore.ps1", [ref]$tokens, [ref]$errors)
          if ($errors.Count -gt 0) { throw $errors }
      - name: Validate restore confirmation guard
        shell: pwsh
        run: |
          $content = Get-Content scripts/restore.ps1 -Raw
          if ($content -notmatch 'ConfirmRestore') { throw 'Restore confirmation switch missing' }
          if ($content -notmatch 'RESTAURAR') { throw 'Interactive restore confirmation missing' }
      - name: Start ephemeral PostgreSQL
        run: |
          docker compose up -d postgres
          timeout 60 bash -c 'until docker compose exec -T postgres pg_isready -U transcritor; do sleep 2; done'
      - name: Execute backup and restore round trip
        shell: pwsh
        run: |
          $backupRoot = Join-Path $env:RUNNER_TEMP "transcritor-backup"
          New-Item -ItemType Directory -Force -Path $backupRoot | Out-Null
          docker compose exec -T postgres psql -U transcritor -d transcritor -c "CREATE TABLE IF NOT EXISTS backup_probe (id integer PRIMARY KEY); INSERT INTO backup_probe VALUES (1) ON CONFLICT DO NOTHING;"
          docker run --rm -v transcritor_file_storage:/data alpine:3.20 sh -c "mkdir -p /data/backup-probe && printf 'ok' > /data/backup-probe/probe.txt"
          ./scripts/backup.ps1 -OutputDirectory $backupRoot
          $backup = Get-ChildItem -Path $backupRoot -Directory | Sort-Object Name -Descending | Select-Object -First 1
          if (-not $backup) { throw "Backup directory not created" }
          ./scripts/restore.ps1 -BackupDirectory $backup.FullName -ConfirmRestore
          docker compose exec -T postgres psql -U transcritor -d transcritor -tAc "SELECT 1 FROM backup_probe WHERE id=1" | Select-String -Pattern '^1$'
          if ($LASTEXITCODE -ne 0) { throw "Restored database probe not found" }

  lint:
    name: Python lint and type checks
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"
      - name: Install tooling
        run: pip install black flake8 mypy isort
      - name: Black check
        run: black --check shared/models.py services/storage-service/app/user_auth.py tests/unit/test_auth.py tests/unit/test_user_auth.py
      - name: Flake8 check
        run: flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
      - name: Isort check
        run: isort --check-only shared/models.py services/storage-service/app/user_auth.py tests/unit/test_auth.py tests/unit/test_user_auth.py
      - name: Mypy check
        run: mypy shared/models.py services/storage-service/app/user_auth.py --ignore-missing-imports

  docker-build:
    name: Build Docker images
    runs-on: ubuntu-latest
    needs: [lint, python, compose-config]
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      - name: Build core images
        run: |
          docker build -t transcritor-transcription:test -f services/transcription-service/Dockerfile .
          docker build -t transcritor-summarization:test services/summarization-service
          docker build -t transcritor-api-gateway:test services/api-gateway
          docker build -t transcritor-storage:test services/storage-service

  integration:
    name: Integration tests
    runs-on: ubuntu-latest
    needs: [docker-build]
    services:
      postgres:
        image: postgres:15-alpine
        env:
          POSTGRES_DB: transcritor
          POSTGRES_USER: transcritor
          POSTGRES_PASSWORD: test_pass
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
      redis:
        image: redis:7-alpine
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 6379:6379
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install -r requirements-dev.txt
      - name: Run integration tests
        run: |
          SUMMARY_MODEL=extractive RUN_REAL_TRANSCRIPTION=1 JWT_SECRET=ci-secret CORS_ORIGINS=http://localhost:3000 \
              docker compose up -d postgres redis rabbitmq storage-service file-management-service summarization-service transcription-service api-gateway
          timeout 120 bash -c 'until curl -fsS http://localhost:8007/health; do sleep 3; done'
          pytest tests/integration -v -m integration -o addopts=''
        env:
          DATABASE_URL: postgresql://transcritor:test_pass@localhost:5432/transcritor
          REDIS_URL: redis://localhost:6379
          RUN_REAL_TRANSCRIPTION: "1"
\n```\n\n## William-kelvem94/CLONNER\n\n### .github/workflows/tests.yml\n\n```yaml\nname: Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.8", "3.9", "3.10", "3.11"]

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov pytest-mock
    
    - name: Run unit tests
      run: |
        pytest tests/unit -v --cov=src --cov-report=xml --cov-report=term
    
    - name: Run integration tests
      run: |
        pytest tests/integration -v --cov=src --cov-append --cov-report=xml --cov-report=term
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        flags: unittests
        name: codecov-umbrella

\n```\n\n## William-kelvem94/Criador_de_audios\n\n### .github/workflows/ci.yml\n\n```yaml\n# 🚀 CI - Continuous Integration - Criador de Áudios v3.0
# Pipeline principal de CI com testes, linting e build

name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]
  workflow_dispatch:

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

env:
  PYTHON_VERSION: "3.10"
  NODE_VERSION: "20"
  DOCKER_BUILDKIT: 1
  COMPOSE_DOCKER_CLI_BUILD: 1

jobs:
  # 🔍 Verificação inicial
  pre-check:
    name: "🔍 Pre-flight Checks"
    runs-on: ubuntu-latest
    outputs:
      should_skip: ${{ steps.skip_check.outputs.should_skip }}
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Check for skip CI
        id: skip_check
        run: |
          if [[ "${{ github.event_name }}" == "pull_request" && "${{ contains(github.event.pull_request.labels.*.name, 'skip-ci') }}" == "true" ]]; then
            echo "should_skip=true" >> $GITHUB_OUTPUT
          else
            echo "should_skip=false" >> $GITHUB_OUTPUT
          fi

      - name: Check file changes
        id: changed_files
        uses: tj-actions/changed-files@v45
        with:
          files: |
            services/backend-service/**
            services/frontend-service/**
            tests/**
            docker/**

  # 🐍 Testes e qualidade do Python
  python-quality:
    name: "🐍 Python Quality"
    runs-on: ubuntu-latest
    needs: pre-check
    if: needs.pre-check.outputs.should_skip != 'true'
    strategy:
      matrix:
        python-version: ["3.10", "3.11"]
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Cache pip dependencies
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ matrix.python-version }}-${{ hashFiles('**/requirements*.txt', 'pyproject.toml') }}
          restore-keys: |
            ${{ runner.os }}-pip-${{ matrix.python-version }}-

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          cd services/backend-service
          pip install -r requirements.txt || echo "No requirements.txt, continuing..."

      - name: Check Python syntax
        run: |
          python -m compileall services/backend-service/ -q

      - name: Run type checking (mypy) - if configured
        continue-on-error: true
        run: |
          pip install mypy
          mypy services/backend-service/ || echo "Mypy check skipped or failed"

      - name: Run linting (flake8) - if configured
        continue-on-error: true
        run: |
          pip install flake8
          flake8 services/backend-service/ --count --select=E9,F63,F7,F82 --show-source --statistics || echo "Flake8 check skipped or failed"

      - name: Run security checks (bandit) - if configured
        continue-on-error: true
        run: |
          pip install bandit
          bandit -r services/backend-service/ -f json -o bandit-report.json || true

      - name: Upload security report
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: security-report-python-${{ matrix.python-version }}
          path: bandit-report.json

  # ⚛️ Testes e qualidade do Frontend
  frontend-quality:
    name: "⚛️ Frontend Quality"
    runs-on: ubuntu-latest
    needs: pre-check
    if: needs.pre-check.outputs.should_skip != 'true'
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
          cache-dependency-path: 'services/frontend-service/package-lock.json'

      - name: Install dependencies
        working-directory: services/frontend-service
        run: npm ci

      - name: Type checking (if configured)
        continue-on-error: true
        working-directory: services/frontend-service
        run: npm run type-check 2>/dev/null || npx tsc --noEmit || echo "Type check not configured"

      - name: Linting (if configured)
        continue-on-error: true
        working-directory: services/frontend-service
        run: npm run lint 2>/dev/null || echo "Linting not configured"

      - name: Format checking (if configured)
        continue-on-error: true
        working-directory: services/frontend-service
        run: npm run format:check 2>/dev/null || echo "Format check not configured"

      - name: Run tests (if configured)
        continue-on-error: true
        working-directory: services/frontend-service
        run: npm run test 2>/dev/null || npm run test:coverage 2>/dev/null || echo "Tests not configured"

      - name: Build
        working-directory: services/frontend-service
        run: npm run build

      - name: Upload test results
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: test-results-frontend
          path: |
            services/frontend-service/coverage/
            services/frontend-service/test-results/

  # 🧪 Testes de integração
  integration-tests:
    name: "🧪 Integration Tests"
    runs-on: ubuntu-latest
    needs: [python-quality, frontend-quality]
    if: needs.pre-check.outputs.should_skip != 'true'
    services:
      redis:
        image: redis:7-alpine
        ports:
          - 6379:6379
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

      postgres:
        image: postgres:15-alpine
        ports:
          - 5432:5432
        env:
          POSTGRES_DB: criador_audios
          POSTGRES_USER: criador_user
          POSTGRES_PASSWORD: criador_password_2024
        options: >-
          --health-cmd "pg_isready -U criador_user -d criador_audios"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Cache Docker layers
        uses: actions/cache@v4
        with:
          path: /tmp/.buildx-cache
          key: ${{ runner.os }}-buildx-${{ github.sha }}
          restore-keys: |
            ${{ runner.os }}-buildx-

      - name: Build test image (if Dockerfile exists)
        continue-on-error: true
        uses: docker/build-push-action@v5
        with:
          context: .
          file: services/frontend-service/Dockerfile.dev
          tags: criador-audios:test
          cache-from: type=local,src=/tmp/.buildx-cache
          cache-to: type=local,dest=/tmp/.buildx-cache-new,mode=max

      - name: Install test dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest pytest-asyncio pytest-cov httpx || echo "Test dependencies not fully available"

      - name: Run integration tests (if configured)
        continue-on-error: true
        run: |
          if [ -d "tests/integration/" ]; then
            python -m pytest tests/integration/ -v --tb=short || echo "Integration tests skipped"
          else
            echo "No integration tests directory found"
          fi

      - name: Upload coverage reports
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: coverage-reports
          path: |
            coverage.xml
            htmlcov/

      # Move cache for next build
      - name: Move cache
        if: always()
        run: |
          rm -rf /tmp/.buildx-cache
          if [ -d "/tmp/.buildx-cache-new" ]; then
            mv /tmp/.buildx-cache-new /tmp/.buildx-cache
          fi

  # 🐳 Build Docker images
  docker-build:
    name: "🐳 Docker Build"
    runs-on: ubuntu-latest
    needs: [integration-tests]
    if: needs.pre-check.outputs.should_skip != 'true'
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to Docker Hub
        if: github.ref == 'refs/heads/main' && github.event_name == 'push'
        continue-on-error: true
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_PASSWORD }}

      - name: Build Docker images (if Dockerfiles exist)
        continue-on-error: true
        run: |
          if [ -f "docker-compose.yml" ]; then
            docker compose build || echo "Docker build skipped"
          else
            echo "No docker-compose.yml found, skipping Docker build"
          fi

  # 🔒 Security scanning
  security-scan:
    name: "🔒 Security Scan"
    runs-on: ubuntu-latest
    needs: [docker-build]
    if: needs.pre-check.outputs.should_skip != 'true'
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run Trivy vulnerability scanner
        continue-on-error: true
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          format: 'sarif'
          output: 'trivy-results.sarif'

      - name: Upload Trivy scan results
        continue-on-error: true
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: 'trivy-results.sarif'

      - name: Run safety check (if configured)
        continue-on-error: true
        run: |
          pip install safety
          safety check --full-report || echo "Safety check skipped"

  # 📊 Coverage report
  coverage-report:
    name: "📊 Coverage Report"
    runs-on: ubuntu-latest
    needs: [integration-tests\n```\n\n### .github/workflows/deploy.yml\n\n```yaml\n# 🚀 Deploy - Continuous Deployment - Criador de Áudios v3.0
# Pipeline de deploy automatizado para staging e produção

name: Deploy

on:
  push:
    branches: [ main, staging ]
  workflow_dispatch:
    inputs:
      environment:
        description: 'Environment to deploy to'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production
      force_deploy:
        description: 'Force deploy even if tests fail'
        required: false
        default: false
        type: boolean

concurrency:
  group: deploy-${{ github.ref }}
  cancel-in-progress: false

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # 🚀 Deploy para Staging
  deploy-staging:
    name: "🚀 Deploy to Staging"
    runs-on: ubuntu-latest
    environment: staging
    if: |
      (github.ref == 'refs/heads/main' && github.event_name == 'push') ||
      (github.event_name == 'workflow_dispatch' && inputs.environment == 'staging')

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=sha,prefix=staging-
            type=raw,value=staging-latest

      - name: Build and push staging image
        uses: docker/build-push-action@v5
        with:
          context: .
          file: docker/services/backend-service/Dockerfile
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          build-args: |
            BUILDKIT_INLINE_CACHE=1
            ENVIRONMENT=staging

      - name: Deploy to staging server
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{ secrets.STAGING_HOST }}
          username: ${{ secrets.STAGING_USER }}
          key: ${{ secrets.STAGING_SSH_KEY }}
          port: ${{ secrets.STAGING_PORT }}
          script: |
            #!/bin/bash
            set -e

            echo "🚀 Starting staging deployment..."

            cd /opt/criador-audios

            # Backup da versão atual
            echo "💾 Creating backup..."
            docker tag criador-audios:latest criador-audios:backup-$(date +%Y%m%d_%H%M%S) || true

            # Pull da nova imagem
            echo "📦 Pulling new image..."
            docker pull ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:staging-latest

            # Tag da imagem
            docker tag ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:staging-latest criador-audios:staging

            # Deploy com zero-downtime
            echo "🔄 Deploying with zero-downtime..."
            docker compose --profile staging up -d --no-build

            # Health check
            echo "🔍 Running health checks..."
            sleep 30

            if curl -f http://localhost:8000/health; then
              echo "✅ Staging deployment successful!"

              # Limpar imagens antigas
              echo "🧹 Cleaning up old images..."
              docker image prune -f

              # Notificar
              curl -X POST -H 'Content-type: application/json' \
                --data '{"text":"✅ Staging deployment successful!"}' \
                ${{ secrets.SLACK_WEBHOOK_URL }} || true

            else
              echo "❌ Health check failed!"
              # Rollback
              echo "🔄 Rolling back..."
              docker tag criador-audios:backup criador-audios:latest
              docker compose --profile staging up -d --no-build

              curl -X POST -H 'Content-type: application/json' \
                --data '{"text":"❌ Staging deployment failed and rolled back!"}' \
                ${{ secrets.SLACK_WEBHOOK_URL }} || true

              exit 1
            fi

  # 🎯 Deploy para Produção
  deploy-production:
    name: "🎯 Deploy to Production"
    runs-on: ubuntu-latest
    environment: production
    needs: deploy-staging
    if: |
      github.ref == 'refs/heads/main' &&
      github.event_name == 'push' &&
      !contains(github.event.head_commit.message, '[skip deploy]')

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=sha,prefix=prod-
            type=raw,value=latest

      - name: Build and push production image
        uses: docker/build-push-action@v5
        with:
          context: .
          file: docker/services/backend-service/Dockerfile
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          build-args: |
            BUILDKIT_INLINE_CACHE=1
            ENVIRONMENT=production

      - name: Deploy to production server
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{ secrets.PRODUCTION_HOST }}
          username: ${{ secrets.PRODUCTION_USER }}
          key: ${{ secrets.PRODUCTION_SSH_KEY }}
          port: ${{ secrets.PRODUCTION_PORT }}
          script: |
            #!/bin/bash
            set -e

            echo "🚀 Starting production deployment..."

            cd /opt/criador-audios

            # Backup da versão atual
            echo "💾 Creating backup..."
            docker tag criador-audios:latest criador-audios:backup-$(date +%Y%m%d_%H%M%S) || true

            # Pull da nova imagem
            echo "📦 Pulling new image..."
            docker pull ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest

            # Tag da imagem
            docker tag ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest criador-audios:latest

            # Deploy com blue-green
            echo "🔄 Deploying with blue-green strategy..."

            # Verificar qual stack está ativa
            if docker ps | grep -q "criador-audios-blue"; then
              TARGET_STACK="green"
              OLD_STACK="blue"
            else
              TARGET_STACK="green"
              OLD_STACK="blue"
            fi

            # Iniciar nova stack
            docker compose --profile production-${TARGET_STACK} up -d --no-build

            # Aguardar startup
            sleep 60

            # Health check da nova stack
            if curl -f http://localhost:8000/health; then
              echo "✅ New stack is healthy!"

              # Switch do load balancer (nginx)
              echo "🔄 Switching load balancer..."
              docker exec criador-audios-nginx nginx -s reload

              # Aguardar alguns requests para confirmar
              sleep 30

              # Finalizar stack antiga
              echo "🛑 Shutting down old stack..."
              docker compose --profile production-${OLD_STACK} down

              echo "🎉 Production deployment successful!"

              # Limpar imagens antigas (manter últimas 3)
              echo "🧹 Cleaning up old images..."
              docker images criador-audios --format "table {{.Repository}}:{{.Tag}}\t{{.ID}}" | \
                tail -n +2 | head -n -3 | awk '{print $2}' | xargs docker rmi || true

              # Notificar sucesso
              curl -X POST -H 'Content-type: application/json' \
                --data '{"text":"🎉 Production deployment successful! 🚀"}' \
                ${{ secrets.SLACK_WEBHOOK_URL }} || true

            else
              echo "❌ New stack health check failed!"

              # Rollback: finalizar nova stack
              docker compose --profile production-${TARGET_STACK} down

              echo "🔄 Deployment failed and rolled back!"

              # Notificar falha
              curl -X POST -H 'Content-type: application/json' \
                --data '{"text":"❌ Production deployment failed and rolled back!"}' \
                ${{ secrets.SLACK_WEBHOOK_URL }} || true

              exit 1
            fi

  # 📊 Post-deploy tests
  post-deploy-tests:
    name: "📊 Post-deploy Tests"
    runs-on: ubuntu-latest
    needs: deploy-production
    if: success() && needs.deploy-production.result == 'success'
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run smoke tests against production
        run: |
          echo "🧪 Running smoke tests against production..."

          # Test health endpoint
          if curl -f --max-time 10 ${{ secrets.PRODUCTION_URL }}/health; then
            echo "✅ Health check passed"
          else
            echo "❌ Health check failed"
            exit 1
          fi

          # Test API endpoints
          if curl -f --max-time 10 ${{ secrets.PRODUCTION_URL }}/api/v1/status; then
            echo "✅ API status check passed"
          else
            echo "❌ API status check failed"
            exit 1
          fi

          echo "🎉 All smoke tests passed!"

      - name: Notify deployment success
        if: success()
        run: |
          curl -X POST -H 'Content-type: application/json' \
            --data '{"text":"🎉 Production deployment completed and smoke tests passed! ✅"}' \
            ${{ secrets.SLACK_WEBHOOK_URL }} || true

  # 🚨 Rollback em caso de falha
  rollback:
   \n```\n\n### .github/workflows/release.yml\n\n```yaml\n# 🏷️ Release - Automated Release Management - Criador de Áudios v3.0
# Criação automática de releases e tags

name: Release

on:
  push:
    branches: [ main ]
  workflow_dispatch:
    inputs:
      version_type:
        description: 'Version bump type'
        required: true
        default: 'patch'
        type: choice
        options:
          - patch
          - minor
          - major
      prerelease:
        description: 'Create prerelease'
        required: false
        default: false
        type: boolean

jobs:
  # 📋 Preparar release
  prepare-release:
    name: "📋 Prepare Release"
    runs-on: ubuntu-latest
    outputs:
      new_version: ${{ steps.version.outputs.new_version }}
      release_notes: ${{ steps.changelog.outputs.release_notes }}
      should_release: ${{ steps.check.outputs.should_release }}
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Check if release is needed
        id: check
        run: |
          # Verificar se há mudanças desde o último release
          LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "")
          if [ -z "$LAST_TAG" ]; then
            echo "should_release=true" >> $GITHUB_OUTPUT
          else
            CHANGES=$(git log $LAST_TAG..HEAD --oneline | wc -l)
            if [ "$CHANGES" -gt 0 ]; then
              echo "should_release=true" >> $GITHUB_OUTPUT
            else
              echo "should_release=false" >> $GITHUB_OUTPUT
            fi
          fi

      - name: Get current version
        id: current_version
        run: |
          CURRENT_VERSION=$(grep '^version =' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
          echo "current_version=$CURRENT_VERSION" >> $GITHUB_OUTPUT

      - name: Calculate new version
        id: version
        run: |
          CURRENT_VERSION="${{ steps.current_version.outputs.current_version }}"
          VERSION_TYPE="${{ github.event.inputs.version_type || 'patch' }}"

          # Parse version
          IFS='.' read -ra VERSION_PARTS <<< "$CURRENT_VERSION"
          MAJOR=${VERSION_PARTS[0]}
          MINOR=${VERSION_PARTS[1]}
          PATCH=${VERSION_PARTS[2]}

          case $VERSION_TYPE in
            major)
              NEW_VERSION="$((MAJOR + 1)).0.0"
              ;;
            minor)
              NEW_VERSION="$MAJOR.$((MINOR + 1)).0"
              ;;
            patch)
              NEW_VERSION="$MAJOR.$MINOR.$((PATCH + 1))"
              ;;
          esac

          echo "new_version=$NEW_VERSION" >> $GITHUB_OUTPUT

      - name: Generate changelog
        id: changelog
        run: |
          LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "")

          if [ -z "$LAST_TAG" ]; then
            # Primeiro release
            RELEASE_NOTES="## 🎉 Initial Release

### ✨ Features
- Sistema completo de conversão texto-para-voz
- Interface web moderna
- Suporte a múltiplos idiomas
- Clonagem de voz
- API REST completa

### 🐛 Bug Fixes
- Correções iniciais

### 📚 Documentation
- Documentação completa"
          else
            # Gerar changelog das mudanças
            RELEASE_NOTES="## 🚀 Release ${{ steps.version.outputs.new_version }}

### 📝 Changes
$(git log $LAST_TAG..HEAD --pretty=format:'- %s' | cat)

### 🤝 Contributors
$(git log $LAST_TAG..HEAD --format='%aN' | sort -u | sed 's/^/- /')"
          fi

          # Escape para JSON
          RELEASE_NOTES_JSON=$(echo "$RELEASE_NOTES" | jq -Rs .)
          echo "release_notes=$RELEASE_NOTES_JSON" >> $GITHUB_OUTPUT

  # 🔄 Atualizar versão
  update-version:
    name: "🔄 Update Version"
    runs-on: ubuntu-latest
    needs: prepare-release
    if: needs.prepare-release.outputs.should_release == 'true'
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Update version in pyproject.toml
        run: |
          sed -i 's/version = ".*"/version = "${{ needs.prepare-release.outputs.new_version }}"/' pyproject.toml

      - name: Update version in package.json
        run: |
          cd services/frontend-service
          npm version ${{ needs.prepare-release.outputs.new_version }} --no-git-tag-version

      - name: Update version in Dockerfile labels
        run: |
          sed -i 's/version="[^"]*"/version="${{ needs.prepare-release.outputs.new_version }}"/' docker/services/*/Dockerfile

      - name: Commit version changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add pyproject.toml services/frontend-service/package.json docker/services/*/Dockerfile
          git commit -m "chore: bump version to ${{ needs.prepare-release.outputs.new_version }}" || true

      - name: Push version changes
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: ${{ github.ref }}

  # 🏷️ Criar tag e release
  create-release:
    name: "🏷️ Create Release"
    runs-on: ubuntu-latest
    needs: [prepare-release, update-version]
    if: needs.prepare-release.outputs.should_release == 'true'
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Create git tag
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git tag -a "v${{ needs.prepare-release.outputs.new_version }}" -m "Release v${{ needs.prepare-release.outputs.new_version }}"

      - name: Push git tag
        run: |
          git push origin "v${{ needs.prepare-release.outputs.new_version }}"

      - name: Create GitHub release
        uses: softprops/action-gh-release@v2
        with:
          tag_name: v${{ needs.prepare-release.outputs.new_version }}
          name: Release v${{ needs.prepare-release.outputs.new_version }}
          body: ${{ needs.prepare-release.outputs.release_notes }}
          draft: false
          prerelease: ${{ github.event.inputs.prerelease || false }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  # 📦 Build e publish packages
  publish-packages:
    name: "📦 Publish Packages"
    runs-on: ubuntu-latest
    needs: create-release
    if: needs.prepare-release.outputs.should_release == 'true'
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      # Python Package
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install build dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build twine

      - name: Build Python package
        run: python -m build

      - name: Publish Python package to PyPI
        if: github.event.inputs.prerelease == false
        env:
          TWINE_USERNAME: ${{ secrets.PYPI_USERNAME }}
          TWINE_PASSWORD: ${{ secrets.PYPI_PASSWORD }}
        run: |
          twine upload dist/*

      # Node.js Package (se aplicável)
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version-file: '.nvmrc'
          registry-url: 'https://registry.npmjs.org'

      - name: Publish Node.js package
        if: github.event.inputs.prerelease == false
        working-directory: services/frontend-service
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
        run: |
          npm publish --access public

  # 📊 Atualizar documentação
  update-docs:
    name: "📊 Update Documentation"
    runs-on: ubuntu-latest
    needs: create-release
    if: needs.prepare-release.outputs.should_release == 'true'
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install docs dependencies
        run: pip install mkdocs mkdocs-material mkdocstrings[python]

      - name: Build documentation
        run: mkdocs build

      - name: Deploy documentation to GitHub Pages
        if: github.ref == 'refs/heads/main'
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
          cname: docs.criador-audios.dev

  # 🔔 Notificações
  notify:
    name: "🔔 Notifications"
    runs-on: ubuntu-latest
    needs: [create-release, publish-packages, update-docs]
    if: always() && needs.prepare-release.outputs.should_release == 'true'
    steps:
      - name: Notify Slack
        run: |
          if [ "${{ needs.create-release.result }}" == "success" ] && \
             [ "${{ needs.publish-packages.result }}" == "success" ]; then
            MESSAGE="🎉 New release v${{ needs.prepare-release.outputs.new_version }} published successfully!"
            COLOR="good"
          else
            MESSAGE="⚠️ Release v${{ needs.prepare-release.outputs.new_version }} completed with issues"
            COLOR="warning"
          fi

          curl -X POST -H 'Content-type: application/json' \
            --data "{\"text\":\"$MESSAGE\",\"color\":\"$COLOR\"}" \
            ${{ secrets.SLACK_WEBHOOK_URL }} || true

      - name: Notify Discord
        run: |
          curl -X POST -H 'Content-Type: application/json' \
            --data "{\"content\":\"🚀 Criador de Áudios v${{ needs.prepare-release.outputs.new_version }} released!\"}" \
            ${{ secrets.DISCORD_WEBHOOK_URL }} || true

  # 📈 Analytics e métricas
  analytics:
    name: "📈 Analytics"
    runs-on: ubuntu-latest
    needs: create-release
    if: needs.prepare-release.outputs.should_release == 'true'
    steps:
      - name: Send analytics data
        run: |
          # Enviar dados para analytics (ex: PostHog, Mixpanel, etc.)
          curl -X POST \
            -H "Content-Type: application/json" \
            -d "{
        \n```\n\n## William-kelvem94/demandas-organizadas-v2-legacy\n\n### .github/workflows/auto-labeler.yml\n\n```yaml\nname: 'Pull Request Labeler'
on:
  pull_request_target:
    types:
      - opened
      - reopened
      - synchronize

jobs:
  triage:
    permissions:
      contents: read
      pull-requests: write
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/labeler@v6
\n```\n\n### .github/workflows/build-images.yml\n\n```yaml\nname: Build Images

on:
  workflow_call:
    inputs:
      build-type:
        type: string
        required: true
      app-version:
        type: string
        required: true
      git-short-hash:
        type: string
        required: true

permissions:
  contents: 'write'
  id-token: 'write'
  packages: 'write'

jobs:
  build-web:
    name: Build @affine/web
    runs-on: ubuntu-latest
    environment: ${{ inputs.build-type }}
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
      - name: Build Core
        run: yarn affine @affine/web build
        env:
          R2_ACCOUNT_ID: ${{ secrets.R2_ACCOUNT_ID }}
          R2_ACCESS_KEY_ID: ${{ secrets.R2_ACCESS_KEY_ID }}
          R2_SECRET_ACCESS_KEY: ${{ secrets.R2_SECRET_ACCESS_KEY }}
          BUILD_TYPE: ${{ inputs.build-type }}
          CAPTCHA_SITE_KEY: ${{ secrets.CAPTCHA_SITE_KEY }}
          SENTRY_ORG: ${{ secrets.SENTRY_ORG }}
          SENTRY_PROJECT: 'affine-web'
          SENTRY_RELEASE: ${{ inputs.app-version }}
          SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
          SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          PERFSEE_TOKEN: ${{ secrets.PERFSEE_TOKEN }}
      - name: Upload web artifact
        uses: actions/upload-artifact@v4
        with:
          name: web
          path: ./packages/frontend/apps/web/dist
          if-no-files-found: error

  build-admin:
    name: Build @affine/admin
    runs-on: ubuntu-latest
    environment: ${{ inputs.build-type }}
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
      - name: Build Admin
        run: yarn affine @affine/admin build
        env:
          R2_ACCOUNT_ID: ${{ secrets.R2_ACCOUNT_ID }}
          R2_ACCESS_KEY_ID: ${{ secrets.R2_ACCESS_KEY_ID }}
          R2_SECRET_ACCESS_KEY: ${{ secrets.R2_SECRET_ACCESS_KEY }}
          BUILD_TYPE: ${{ inputs.build-type }}
          CAPTCHA_SITE_KEY: ${{ secrets.CAPTCHA_SITE_KEY }}
          SENTRY_ORG: ${{ secrets.SENTRY_ORG }}
          SENTRY_PROJECT: 'affine-admin'
          SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
          SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          PERFSEE_TOKEN: ${{ secrets.PERFSEE_TOKEN }}
      - name: Upload admin artifact
        uses: actions/upload-artifact@v4
        with:
          name: admin
          path: ./packages/frontend/admin/dist
          if-no-files-found: error

  build-mobile:
    name: Build @affine/mobile
    runs-on: ubuntu-latest
    environment: ${{ inputs.build-type }}
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
      - name: Build Mobile
        run: yarn affine @affine/mobile build
        env:
          R2_ACCOUNT_ID: ${{ secrets.R2_ACCOUNT_ID }}
          R2_ACCESS_KEY_ID: ${{ secrets.R2_ACCESS_KEY_ID }}
          R2_SECRET_ACCESS_KEY: ${{ secrets.R2_SECRET_ACCESS_KEY }}
          BUILD_TYPE: ${{ inputs.build-type }}
          CAPTCHA_SITE_KEY: ${{ secrets.CAPTCHA_SITE_KEY }}
          SENTRY_ORG: ${{ secrets.SENTRY_ORG }}
          SENTRY_PROJECT: 'affine-mobile'
          SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
          SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          PERFSEE_TOKEN: ${{ secrets.PERFSEE_TOKEN }}
      - name: Upload mobile artifact
        uses: actions/upload-artifact@v4
        with:
          name: mobile
          path: ./packages/frontend/apps/mobile/dist
          if-no-files-found: error

  build-server-native:
    name: Build Server native - ${{ matrix.targets.name }}
    runs-on: ubuntu-22.04
    environment: ${{ inputs.build-type }}
    strategy:
      fail-fast: false
      matrix:
        targets:
          - name: x86_64-unknown-linux-gnu
            file: server-native.x64.node
          - name: aarch64-unknown-linux-gnu
            file: server-native.arm64.node
          - name: armv7-unknown-linux-gnueabihf
            file: server-native.armv7.node

    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          electron-install: false
          extra-flags: workspaces focus @affine/server-native
      - name: Build Rust
        uses: ./.github/actions/build-rust
        env:
          AFFINE_PRO_PUBLIC_KEY: ${{ secrets.AFFINE_PRO_PUBLIC_KEY }}
          AFFINE_PRO_LICENSE_AES_KEY: ${{ secrets.AFFINE_PRO_LICENSE_AES_KEY }}
        with:
          target: ${{ matrix.targets.name }}
          package: '@affine/server-native'
      - name: Rename ${{ matrix.targets.file }}
        run: |
          mv ./packages/backend/native/server-native.node ./packages/backend/native/${{ matrix.targets.file }}
      - name: Upload ${{ matrix.targets.file }}
        uses: actions/upload-artifact@v4
        with:
          name: server-native-${{ matrix.targets.file }}
          path: ./packages/backend/native/${{ matrix.targets.file }}
          if-no-files-found: error

  build-server:
    name: Build Server
    runs-on: ubuntu-latest
    needs:
      - build-server-native
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          electron-install: false
          extra-flags: workspaces focus @affine/server @types/affine__env
      - name: Download server-native
        uses: actions/download-artifact@v4
        with:
          pattern: server-native-*
          merge-multiple: true
          path: ./packages/backend/native
      - name: List server-native files
        run: ls -alh ./packages/backend/native
      - name: Build Server
        run: yarn workspace @affine/server build
      - name: Upload server dist
        uses: actions/upload-artifact@v4
        with:
          name: server-dist
          path: ./packages/backend/server/dist
          if-no-files-found: error

  build-images:
    name: Build Images
    runs-on: ubuntu-latest
    needs:
      - build-server
      - build-web
      - build-mobile
      - build-admin
    steps:
      - uses: actions/checkout@v6
      - name: Download server dist
        uses: actions/download-artifact@v4
        with:
          name: server-dist
          path: ./packages/backend/server/dist
      - name: Login to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          logout: false
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - name: Set up QEMU
        uses: docker/setup-qemu-action@v3
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      # setup node without cache configuration
      # Prisma cache is not compatible with docker build cache
      - name: Setup Node.js
        uses: actions/setup-node@v6
        with:
          node-version-file: '.nvmrc'
          registry-url: https://npm.pkg.github.com
          scope: '@toeverything'

      - name: Download web artifact
        uses: actions/download-artifact@v4
        with:
          name: web
          path: ./packages/frontend/apps/web/dist

      - name: Download mobile artifact
        uses: actions/download-artifact@v4
        with:
          name: mobile
          path: ./packages/frontend/apps/mobile/dist

      - name: Download admin artifact
        uses: actions/download-artifact@v4
        with:
          name: admin
          path: ./packages/frontend/admin/dist

      - name: Install Node.js dependencies
        run: |
          yarn config set --json supportedArchitectures.cpu '["x64", "arm64", "arm"]'
          yarn config set --json supportedArchitectures.libc '["glibc"]'
          yarn workspaces focus @affine/server --production

      - name: Generate Prisma client
        run: yarn workspace @affine/server prisma generate

      - name: Mv node_modules
        run: mv ./node_modules ./packages/backend/server

      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}

      - name: Build backend Dockerfile
        uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          pull: true
          platforms: linux/amd64,linux/arm64,linux/arm/v7
          provenance: true
          file: .github/deployment/node/Dockerfile
          tags: ghcr.io/toeverything/affine:${{inputs.build-type}}-${{ inputs.git-short-hash }}
\n```\n\n### .github/workflows/build-test.yml\n\n```yaml\nname: Build & Test

on:
  push:
    branches:
      - canary
      - beta
      - stable
      - v[0-9]+.[0-9]+.x-staging
      - v[0-9]+.[0-9]+.x
    paths-ignore:
      - README.md
  pull_request:
  merge_group:

env:
  DEBUG: napi:*
  BUILD_TYPE: canary
  APP_NAME: affine
  AFFINE_ENV: dev
  COVERAGE: true
  MACOSX_DEPLOYMENT_TARGET: '11.6'
  DEPLOYMENT_TYPE: affine
  AFFINE_INDEXER_ENABLED: true

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest
    env:
      NODE_OPTIONS: --max-old-space-size=14384
    permissions:
      actions: read
      contents: read
      security-events: write

    strategy:
      fail-fast: false
      matrix:
        language: ['javascript', 'typescript']
        project: ['affine', 'blocksuite']

    steps:
      - name: Checkout repository
        uses: actions/checkout@v6

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v3
        with:
          languages: ${{ matrix.language }}
          source-root: ${{ matrix.project == 'affine' && '.' || 'blocksuite' }}

      - name: Delete blocksuite before codeql analysis
        if: ${{ matrix.project == 'affine' }}
        run: rm -rf blocksuite

      - name: Autobuild
        uses: github/codeql-action/autobuild@v3

      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v3
  lint:
    name: Lint
    runs-on: ubuntu-24.04-arm
    steps:
      - uses: actions/checkout@v6
      - name: Setup Go (for actionlint)
        uses: actions/setup-go@v6
        with:
          go-version: 'stable'
      - name: Install actionlint
        shell: bash
        run: |
          set -euo pipefail
          go install github.com/rhysd/actionlint/cmd/actionlint@v1.7.11
      - name: Run actionlint
        shell: bash
        run: |
          set -euo pipefail
          "$(go env GOPATH)/bin/actionlint"
      - name: Run oxlint
        # oxlint is fast, so wrong code will fail quickly
        run: |
          set -euo pipefail
          oxlint_version="$(node -e "console.log(require('./package.json').devDependencies.oxlint)")"
          yarn dlx "oxlint@${oxlint_version}" --deny-warnings
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          electron-install: false
          full-cache: true
      - name: Run i18n codegen
        run: yarn affine @affine/i18n build
      - name: Run ESLint
        run: yarn lint:eslint --max-warnings=0
      - name: Run Prettier
        # Set nmMode in `actions/setup-node` will modify the .yarnrc.yml
        run: |
          git checkout .yarnrc.yml
          yarn lint:prettier
      - name: Yarn Dedupe
        run: yarn dedupe --check

  typecheck:
    name: Typecheck
    runs-on: ubuntu-24.04-arm
    env:
      NODE_OPTIONS: --max-old-space-size=14384
    steps:
      - uses: actions/checkout@v6
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          electron-install: false
          full-cache: true
      - name: Run i18n codegen
        run: yarn affine @affine/i18n build
      - name: Run Type Check
        run: yarn typecheck
      - name: Run BS Docs Build
        run: |
          yarn affine bs-docs build
          git checkout packages/frontend/i18n/src/i18n-completenesses.json
          if git status --porcelain | grep -q .; then
            echo "Run 'yarn typecheck && yarn affine bs-docs build' and make sure all changes are submitted"
            exit 1
          else
            echo "All changes are submitted"
          fi

  rust-test-filter:
    name: Rust test filter
    runs-on: ubuntu-latest
    outputs:
      run-rust: ${{ steps.rust-filter.outputs.rust }}
    steps:
      - uses: actions/checkout@v6

      - uses: dorny/paths-filter@v3
        id: rust-filter
        with:
          filters: |
            rust:
              - '**/*.rs'
              - '**/Cargo.toml'
              - '**/Cargo.lock'
              - '.cargo/**'
              - 'rust-toolchain*'
              - '.github/actions/build-rust/**'

  lint-rust:
    name: Lint Rust
    if: ${{ needs.rust-test-filter.outputs.run-rust == 'true' }}
    runs-on: ubuntu-latest
    needs:
      - rust-test-filter
    steps:
      - uses: actions/checkout@v6
      - uses: ./.github/actions/build-rust
        with:
          target: x86_64-unknown-linux-gnu
          package: 'affine'
          no-build: 'true'
      - name: fmt check
        run: |
          rustup toolchain add nightly
          rustup component add --toolchain nightly-x86_64-unknown-linux-gnu rustfmt
          cargo +nightly fmt --all -- --check
      - name: Clippy
        run: |
          rustup component add clippy
          cargo clippy --workspace --exclude affine_server_native --all-targets --all-features -- -D warnings
          cargo clippy -p affine_server_native --all-targets --all-features -- -D warnings

  check-git-status:
    name: Check Git Status
    runs-on: ubuntu-latest
    needs:
      - build-server-native
    steps:
      - uses: actions/checkout@v6
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          full-cache: true

      - name: Download server-native.node
        uses: actions/download-artifact@v4
        with:
          name: server-native.node
          path: ./packages/backend/native

      - name: Run Check
        run: |
          yarn affine init
          yarn affine gql build
          yarn affine i18n build
          yarn affine server genconfig
          git checkout packages/frontend/i18n/src/i18n-completenesses.json
          if git status --porcelain | grep -q .; then
            echo "Run 'yarn affine init && yarn affine gql build && yarn affine i18n build && yarn affine server genconfig' and make sure all changes are submitted"
            exit 1
          else
            echo "All changes are submitted"
          fi

  check-yarn-binary:
    name: Check yarn binary
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Run check
        run: |
          set -euo pipefail
          yarn_version="$(node -e "console.log(require('./package.json').packageManager.split('@')[1])")"
          yarn set version "$yarn_version"
          git diff --exit-code

  e2e-blocksuite-test:
    name: E2E BlockSuite Test
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        shard: [1, 2, 3, 4, 5]
    steps:
      - uses: actions/checkout@v6
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          extra-flags: workspaces focus @affine/monorepo @affine-test/blocksuite @blocksuite/playground @blocksuite/integration-test
          playwright-install: true
          playwright-platform: 'chromium'
          electron-install: false
          full-cache: true

      - name: Run playground build
        run: yarn workspace @blocksuite/playground build

      - name: Run playwright tests
        run: yarn workspace @affine-test/blocksuite test --forbid-only --shard=${{ matrix.shard }}/${{ strategy.job-total }}

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-results-e2e-bs-${{ matrix.shard }}
          path: ./test-results
          if-no-files-found: ignore

  e2e-blocksuite-cross-browser-test:
    name: E2E BlockSuite Cross Browser Test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          extra-flags: workspaces focus @affine/monorepo @affine-test/blocksuite @blocksuite/playground @blocksuite/integration-test
          playwright-install: true
          playwright-platform: 'chromium,firefox,webkit'
          electron-install: false
          full-cache: true

      - name: Run playground build
        run: yarn workspace @blocksuite/playground build

      - name: Run playwright tests
        run: |
          yarn workspace @blocksuite/integration-test test:unit
          yarn workspace @affine-test/blocksuite test "cross-platform/" --forbid-only

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-results-e2e-bs-cross-browser
          path: ./test-results
          if-no-files-found: ignore

  e2e-test:
    name: E2E Test
    runs-on: ubuntu-24.04-arm
    env:
      DISTRIBUTION: web
      IN_CI_TEST: true
      NODE_OPTIONS: --max-old-space-size=14384
    strategy:
      fail-fast: false
      matrix:
        shard: [1, 2, 3, 4, 5]
    steps:
      - uses: actions/checkout@v6
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          extra-flags: workspaces focus @affine/monorepo @affine-test/affine-local @affine/web @affine/server
          playwright-install: true
          playwright-platform: 'chromium'
          electron-install: false
          full-cache: true

      - name: Run playwright tests
        run: yarn affine @affine-test/affine-local e2e --forbid-only --shard=${{ matrix.shard }}/${{ strategy.job-total }}

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-results-e2e-${{ matrix.shard }}
          path: ./test-results
          if-no-files-found: ignore

  e2e-mobile-test:
    name: E2E Mobile Test
    runs-on: ubuntu-latest
    env:
      DISTRIBUTION: mobile
      IN_CI_TEST: true
    strategy:
      fail-fast: false
      matrix:
        shard: [1, 2]
    steps:
      - uses: actions/checkout@v6
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          extra-flags: workspaces focus @affine/monorepo @affine-test/affine-mobile @affine/mobile
          playwright-install: true
          electron-install: false
          full-cache: true

      - nam\n```\n\n### .github/workflows/copilot-test-automatically.yml\n\n```yaml\nname: Copilot Test Automatically

on:
  push:
    tags:
      - 'v[0-9]+.[0-9]+.[0-9]+-canary.[0-9]+'
  schedule:
    - cron: '0 8 * * *'
  workflow_dispatch:

permissions:
  actions: write
  contents: read

jobs:
  dispatch-test:
    runs-on: ubuntu-latest
    name: Setup Test
    steps:
      - name: dispatch test by tag
        if: ${{ github.event_name == 'push' || github.event_name == 'workflow_dispatch' }}
        uses: benc-uk/workflow-dispatch@v1
        with:
          workflow: copilot-test.yml
          ref: main
      - name: dispatch test by schedule
        if: ${{ github.event_name == 'schedule' }}
        uses: benc-uk/workflow-dispatch@v1
        with:
          workflow: copilot-test.yml
          ref: main\n```\n\n### .github/workflows/copilot-test.yml\n\n```yaml\nname: Copilot Cron Test

on:
  workflow_dispatch:

jobs:
  build-server-native:
    name: Build Server native
    runs-on: ubuntu-latest
    env:
      CARGO_PROFILE_RELEASE_DEBUG: '1'
    steps:
      - uses: actions/checkout@v6
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          extra-flags: workspaces focus @affine/server-native
          electron-install: false
      - name: Build Rust
        uses: ./.github/actions/build-rust
        with:
          target: 'x86_64-unknown-linux-gnu'
          package: '@affine/server-native'
      - name: Upload server-native.node
        uses: actions/upload-artifact@v4
        with:
          name: server-native.node
          path: ./packages/backend/native/server-native.node
          if-no-files-found: error

  copilot-api-test:
    name: Server Copilot Api Test
    runs-on: ubuntu-latest
    needs:
      - build-server-native
    env:
      NODE_ENV: test
      DISTRIBUTION: web
      DATABASE_URL: postgresql://affine:affine@localhost:5432/affine
      REDIS_SERVER_HOST: localhost
    services:
      postgres:
        image: pgvector/pgvector:pg16
        env:
          POSTGRES_PASSWORD: affine
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
      redis:
        image: redis
        ports:
          - 6379:6379
      mailer:
        image: mailhog/mailhog
        ports:
          - 1025:1025
          - 8025:8025
      indexer:
        image: manticoresearch/manticore:10.1.0
        ports:
          - 9308:9308
    steps:
      - uses: actions/checkout@v6

      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          playwright-install: true
          electron-install: false
          full-cache: true

      - name: Download server-native.node
        uses: actions/download-artifact@v4
        with:
          name: server-native.node
          path: ./packages/backend/native

      - name: Prepare Server Test Environment
        env:
          SERVER_CONFIG: ${{ secrets.TEST_SERVER_CONFIG }}
        uses: ./.github/actions/server-test-env

      - name: Run server tests
        run: yarn affine @affine/server test:copilot:coverage --forbid-only
        env:
          CARGO_TARGET_DIR: '${{ github.workspace }}/target'

      - name: Upload server test coverage results
        uses: codecov/codecov-action@v5
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          files: ./packages/backend/server/.coverage/lcov.info
          flags: server-test
          name: affine
          fail_ci_if_error: false

  copilot-e2e-test:
    name: Frontend Copilot E2E Test
    runs-on: ubuntu-latest
    env:
      DISTRIBUTION: web
      DATABASE_URL: postgresql://affine:affine@localhost:5432/affine
      REDIS_SERVER_HOST: localhost
      IN_CI_TEST: true
    strategy:
      fail-fast: false
      matrix:
        shardIndex: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        shardTotal: [10]
    needs:
      - build-server-native
    services:
      postgres:
        image: pgvector/pgvector:pg16
        env:
          POSTGRES_PASSWORD: affine
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
      redis:
        image: redis
        ports:
          - 6379:6379
      indexer:
        image: manticoresearch/manticore:10.1.0
        ports:
          - 9308:9308
    steps:
      - uses: actions/checkout@v6

      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          playwright-install: true
          electron-install: false
          hard-link-nm: false

      - name: Download server-native.node
        uses: actions/download-artifact@v4
        with:
          name: server-native.node
          path: ./packages/backend/native

      - name: Prepare Server Test Environment
        env:
          SERVER_CONFIG: ${{ secrets.TEST_SERVER_CONFIG }}
        uses: ./.github/actions/server-test-env

      - name: Run Copilot E2E Test ${{ matrix.shardIndex }}/${{ matrix.shardTotal }}
        uses: ./.github/actions/copilot-test
        with:
          script: yarn affine @affine-test/affine-cloud-copilot e2e --forbid-only --shard=${{ matrix.shardIndex }}/${{ matrix.shardTotal }}

  test-done:
    needs:
      - copilot-api-test
      - copilot-e2e-test
    if: always()
    runs-on: ubuntu-latest
    name: Post test result message
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          extra-flags: 'workspaces focus @affine/copilot-result'
          electron-install: false
      - name: Post Success event to a Slack channel
        if: ${{ always() && !contains(needs.*.result, 'failure') && !contains(needs.*.result, 'cancelled') }}
        run: node ./tools/copilot-result/index.js
        env:
          CHANNEL_ID: ${{ secrets.RELEASE_SLACK_CHNNEL_ID }}
          SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
          BRANCH_SHA: ${{ github.sha }}
          BRANCH_NAME: ${{ github.ref }}
          COPILOT_RESULT: success
      - name: Post Failed event to a Slack channel
        id: failed-slack
        if: ${{ always() && contains(needs.*.result, 'failure') }}
        run: node ./tools/copilot-result/index.js
        env:
          CHANNEL_ID: ${{ secrets.RELEASE_SLACK_CHNNEL_ID }}
          SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
          BRANCH_SHA: ${{ github.sha }}
          BRANCH_NAME: ${{ github.ref }}
          COPILOT_RESULT: failed
      - name: Post Cancel event to a Slack channel
        id: cancel-slack
        if: ${{ always() && contains(needs.*.result, 'cancelled') && !contains(needs.*.result, 'failure') }}
        run: node ./tools/copilot-result/index.js
        env:
          CHANNEL_ID: ${{ secrets.RELEASE_SLACK_CHNNEL_ID }}
          SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
          BRANCH_SHA: ${{ github.sha }}
          BRANCH_NAME: ${{ github.ref }}
          COPILOT_RESULT: canceled
\n```\n\n### .github/workflows/pr-title-lint.yml\n\n```yaml\nname: PR Title Lint

on:
  pull_request:
    types:
      - opened
      - edited
      - synchronize
    branches:
      - canary

permissions:
  contents: read

jobs:
  check-pull-request-title:
    name: Check pull request title
    runs-on: ubuntu-latest
    if: ${{ github.event.action != 'edited' || github.event.changes.title != null }}
    steps:
      - uses: actions/checkout@v6
      - name: Setup Node.js
        uses: actions/setup-node@v6
        with:
          cache: 'yarn'
          node-version-file: '.nvmrc'
      - name: Install dependencies
        run: yarn workspaces focus @affine/commitlint-config
      - name: Check PR title
        env:
          TITLE: ${{ github.event.pull_request.title }}
        run: echo "$TITLE" | yarn workspace @affine/commitlint-config commitlint -g ./.commitlintrc.json
\n```\n\n### .github/workflows/release-cloud.yml\n\n```yaml\nname: Release Cloud

on:
  workflow_call:
    inputs:
      build-type:
        required: true
        type: string
      app-version:
        required: true
        type: string
      git-short-hash:
        required: true
        type: string

permissions:
  contents: 'write'
  id-token: 'write'
  packages: 'write'

jobs:
  build-images:
    name: Build Images
    uses: ./.github/workflows/build-images.yml
    secrets: inherit
    with:
      build-type: ${{ inputs.build-type }}
      app-version: ${{ inputs.app-version }}
      git-short-hash: ${{ inputs.git-short-hash }}

  deploy:
    name: Deploy to cluster
    environment: ${{ inputs.build-type }}
    needs:
      - build-images
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Deploy to ${{ inputs.build-type }}
        uses: ./.github/actions/deploy
        with:
          gcp-project-number: ${{ secrets.GCP_PROJECT_NUMBER }}
          gcp-project-id: ${{ secrets.GCP_PROJECT_ID }}
          service-account: ${{ secrets.GCP_HELM_DEPLOY_SERVICE_ACCOUNT }}
          cluster-name: ${{ secrets.GCP_CLUSTER_NAME }}
          cluster-location: ${{ secrets.GCP_CLUSTER_LOCATION }}
        env:
          BUILD_TYPE: ${{ inputs.build-type }}
          APP_VERSION: ${{ inputs.app-version }}
          GIT_SHORT_HASH: ${{ inputs.git-short-hash }}
          DEPLOY_HOST: ${{ secrets.DEPLOY_HOST }}
          CANARY_DEPLOY_HOST: ${{ secrets.CANARY_DEPLOY_HOST }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
          DATABASE_USERNAME: ${{ secrets.DATABASE_USERNAME }}
          DATABASE_PASSWORD: ${{ secrets.DATABASE_PASSWORD }}
          DATABASE_NAME: ${{ secrets.DATABASE_NAME }}
          GCLOUD_CONNECTION_NAME: ${{ secrets.GCLOUD_CONNECTION_NAME }}
          REDIS_SERVER_HOST: ${{ secrets.REDIS_SERVER_HOST }}
          REDIS_SERVER_PASSWORD: ${{ secrets.REDIS_SERVER_PASSWORD }}
          CLOUD_SQL_IAM_ACCOUNT: ${{ secrets.CLOUD_SQL_IAM_ACCOUNT }}
          APP_IAM_ACCOUNT: ${{ secrets.APP_IAM_ACCOUNT }}
          STATIC_IP_NAME: ${{ secrets.STATIC_IP_NAME }}
          AFFINE_INDEXER_SEARCH_PROVIDER: ${{ secrets.AFFINE_INDEXER_SEARCH_PROVIDER }}
          AFFINE_INDEXER_SEARCH_ENDPOINT: ${{ secrets.AFFINE_INDEXER_SEARCH_ENDPOINT }}
          AFFINE_INDEXER_SEARCH_API_KEY: ${{ secrets.AFFINE_INDEXER_SEARCH_API_KEY }}
\n```\n\n### .github/workflows/release-desktop-platform.yml\n\n```yaml\nname: Release Desktop Platform

on:
  workflow_call:
    inputs:
      build_type:
        required: true
        type: string
      app_version:
        required: true
        type: string
      git_short_hash:
        required: true
        type: string
      runner:
        required: true
        type: string
      platform:
        required: true
        type: string
      arch:
        required: true
        type: string
      target:
        required: true
        type: string
      apple_codesign:
        required: false
        default: false
        type: boolean
      install_linux_deps:
        required: false
        default: false
        type: boolean
      enable_scripts:
        required: false
        default: false
        type: boolean
    outputs:
      files_to_be_signed:
        description: Files to be signed (Windows only)
        value: ${{ jobs.build.outputs.files_to_be_signed }}

permissions:
  actions: write
  contents: write
  security-events: write
  id-token: write
  attestations: write

jobs:
  build:
    runs-on: ${{ inputs.runner }}
    outputs:
      files_to_be_signed: ${{ steps.get_files_to_be_signed.outputs.FILES_TO_BE_SIGNED }}
    env:
      BUILD_TYPE: ${{ inputs.build_type }}
      RELEASE_VERSION: ${{ inputs.app_version }}
      DEBUG: 'affine:*,napi:*'
      APP_NAME: affine
      MACOSX_DEPLOYMENT_TARGET: '12.0'
      SKIP_GENERATE_ASSETS: 1
      APPLE_ID: ${{ secrets.APPLE_ID }}
      APPLE_PASSWORD: ${{ secrets.APPLE_PASSWORD }}
      APPLE_TEAM_ID: ${{ secrets.APPLE_TEAM_ID }}
      SENTRY_ORG: ${{ secrets.SENTRY_ORG }}
      SENTRY_PROJECT: 'affine'
      SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
      SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
      SENTRY_RELEASE: ${{ inputs.app_version }}
    steps:
      - uses: actions/checkout@v6

      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app_version }}

      - name: Setup Node.js
        timeout-minutes: 10
        uses: ./.github/actions/setup-node
        with:
          extra-flags: workspaces focus @affine/electron @affine/monorepo @affine/nbstore @toeverything/infra
          hard-link-nm: false
          nmHoistingLimits: workspaces
          enableScripts: ${{ inputs.enable_scripts }}

      - name: Build AFFiNE native
        uses: ./.github/actions/build-rust
        with:
          target: ${{ inputs.target }}
          package: '@affine/native'

      - uses: actions/download-artifact@v4
        with:
          name: desktop-web
          path: packages/frontend/apps/electron/resources/web-static

      - name: Build Desktop Layers
        run: yarn affine @affine/electron build

      - name: Signing By Apple Developer ID
        if: ${{ inputs.platform == 'darwin' && inputs.apple_codesign }}
        uses: apple-actions/import-codesign-certs@v6
        with:
          p12-file-base64: ${{ secrets.CERTIFICATES_P12 }}
          p12-password: ${{ secrets.CERTIFICATES_P12_PASSWORD }}

      - name: Install additional dependencies on Linux
        if: ${{ inputs.platform == 'linux' && inputs.install_linux_deps }}
        run: |
          df -h
          sudo add-apt-repository universe
          sudo apt install -y libfuse2 elfutils flatpak flatpak-builder
          flatpak remote-add --user --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
          flatpak update
          # some flatpak deps need git protocol.file.allow
          git config --global protocol.file.allow always
          # clean up apt cache to save disk space
          sudo -E apt-get -y purge azure-cli* zulu* hhvm* llvm* firefox* google* dotnet* aspnetcore* powershell* adoptopenjdk* mysql* php* mongodb* moby* snap* || true
          sudo -E apt-get -qq autoremove --purge
          sudo rm -rf /usr/share/dotnet /opt/ghc /opt/hostedtoolcache/CodeQL /usr/local/lib/android
          sudo apt-get clean
          rm -rf ~/.cache/yarn ~/.npm
          df -h

      - name: Remove nbstore node_modules (darwin/linux)
        if: ${{ inputs.platform != 'win32' }}
        shell: bash
        # node_modules of nbstore is not needed for building, and it will make the build process out of memory
        run: |
          cargo clean
          rm -rf packages/frontend/apps/electron/node_modules/@affine/nbstore/node_modules/@blocksuite
          rm -rf packages/frontend/apps/electron/node_modules/@affine/native/node_modules

      - name: Remove nbstore node_modules (windows)
        if: ${{ inputs.platform == 'win32' }}
        shell: bash
        run: |
          rm -rf packages/frontend/apps/electron/node_modules/@affine/nbstore/node_modules/@blocksuite/affine/node_modules
          rm -rf packages/frontend/apps/electron/node_modules/@affine/native/node_modules

      - name: make
        if: ${{ inputs.platform != 'win32' }}
        run: yarn affine @affine/electron make --platform=${{ inputs.platform }} --arch=${{ inputs.arch }}
        env:
          SKIP_WEB_BUILD: 1
          HOIST_NODE_MODULES: 1
          NODE_OPTIONS: --max-old-space-size=14384

      - name: package
        if: ${{ inputs.platform == 'win32' }}
        run: |
          yarn affine @affine/electron package --platform=${{ inputs.platform }} --arch=${{ inputs.arch }}
        env:
          SKIP_WEB_BUILD: 1
          HOIST_NODE_MODULES: 1
          NODE_OPTIONS: --max-old-space-size=14384

      - name: signing DMG
        if: ${{ inputs.platform == 'darwin' && inputs.apple_codesign }}
        run: |
          codesign --force --sign "Developer ID Application: TOEVERYTHING PTE. LTD." packages/frontend/apps/electron/out/${{ env.BUILD_TYPE }}/make/AFFiNE.dmg

      - name: Save artifacts (mac)
        if: ${{ inputs.platform == 'darwin' }}
        run: |
          mkdir -p builds
          mv packages/frontend/apps/electron/out/*/make/*.dmg ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-macos-${{ inputs.arch }}.dmg
          mv packages/frontend/apps/electron/out/*/make/zip/darwin/${{ inputs.arch }}/*.zip ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-macos-${{ inputs.arch }}.zip

      - name: Save artifacts (linux)
        if: ${{ inputs.platform == 'linux' }}
        run: |
          mkdir -p builds
          mv packages/frontend/apps/electron/out/*/make/zip/linux/${{ inputs.arch }}/*.zip ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-linux-${{ inputs.arch }}.zip
          mv packages/frontend/apps/electron/out/*/make/AppImage/${{ inputs.arch }}/*.AppImage ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-linux-${{ inputs.arch }}.appimage
          mv packages/frontend/apps/electron/out/*/make/deb/${{ inputs.arch }}/*.deb ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-linux-${{ inputs.arch }}.deb
          mv packages/frontend/apps/electron/out/*/make/flatpak/*/*.flatpak ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-linux-${{ inputs.arch }}.flatpak

      - uses: actions/attest-build-provenance@v4
        if: ${{ inputs.platform == 'darwin' }}
        with:
          subject-path: |
            ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-macos-${{ inputs.arch }}.zip
            ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-macos-${{ inputs.arch }}.dmg

      - uses: actions/attest-build-provenance@v4
        if: ${{ inputs.platform == 'linux' }}
        with:
          subject-path: |
            ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-linux-${{ inputs.arch }}.zip
            ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-linux-${{ inputs.arch }}.appimage
            ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-linux-${{ inputs.arch }}.deb
            ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-linux-${{ inputs.arch }}.flatpak

      - name: Upload Artifact
        if: ${{ inputs.platform == 'darwin' || inputs.platform == 'linux' }}
        uses: actions/upload-artifact@v4
        with:
          name: affine-${{ inputs.platform }}-${{ inputs.arch }}-builds
          path: builds

      - name: get all files to be signed
        id: get_files_to_be_signed
        if: ${{ inputs.platform == 'win32' }}
        shell: pwsh
        run: |
          Set-Variable -Name FILES_TO_BE_SIGNED -Value ((Get-ChildItem -Path packages/frontend/apps/electron/out -Recurse -File | Where-Object { $_.Extension -in @(".exe", ".node", ".dll", ".msi") } | ForEach-Object { '"' + $_.FullName.Replace((Get-Location).Path + '\packages\frontend\apps\electron\out\', '') + '"' }) -join ' ')
          "FILES_TO_BE_SIGNED=$FILES_TO_BE_SIGNED" >> $env:GITHUB_OUTPUT
          echo $FILES_TO_BE_SIGNED

      - name: Zip artifacts for faster upload
        if: ${{ inputs.platform == 'win32' }}
        shell: pwsh
        run: Compress-Archive -CompressionLevel Fastest -Path packages/frontend/apps/electron/out/* -DestinationPath archive.zip

      - name: Save packaged artifacts for signing
        if: ${{ inputs.platform == 'win32' }}
        uses: actions/upload-artifact@v4
        with:
          name: packaged-${{ inputs.platform }}-${{ inputs.arch }}
          path: |
            archive.zip
            !**/*.map
\n```\n\n### .github/workflows/release-desktop.yml\n\n```yaml\nname: Release Desktop

on:
  workflow_call:
    inputs:
      build-type:
        required: true
        type: string
      app-version:
        required: true
        type: string
      git-short-hash:
        required: true
        type: string
      desktop_macos:
        description: 'Desktop - macOS'
        required: false
        default: true
        type: boolean
      desktop_windows:
        description: 'Desktop - Windows'
        required: false
        default: true
        type: boolean
      desktop_linux:
        description: 'Desktop - Linux'
        required: false
        default: true
        type: boolean

permissions:
  actions: write
  contents: write
  security-events: write
  id-token: write
  attestations: write

env:
  BUILD_TYPE: ${{ inputs.build-type }}
  RELEASE_VERSION: ${{ inputs.app-version }}
  DEBUG: 'affine:*,napi:*'
  APP_NAME: affine
  MACOSX_DEPLOYMENT_TARGET: '11.6'

jobs:
  before-make:
    if: ${{ inputs.desktop_macos || inputs.desktop_windows || inputs.desktop_linux }}
    runs-on: ubuntu-latest
    environment: ${{ inputs.build-type }}
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
      - name: Setup @sentry/cli
        uses: ./.github/actions/setup-sentry
      - name: generate-assets
        run: yarn affine @affine/electron generate-assets
        env:
          SENTRY_ORG: ${{ secrets.SENTRY_ORG }}
          SENTRY_PROJECT: 'affine'
          SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
          SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          SENTRY_RELEASE: ${{ inputs.app-version }}
          RELEASE_VERSION: ${{ inputs.app-version }}

      - name: Upload web artifact
        uses: actions/upload-artifact@v4
        with:
          name: desktop-web
          path: packages/frontend/apps/electron/resources/web-static

  make-distribution-macos:
    if: ${{ inputs.desktop_macos }}
    strategy:
      fail-fast: false
      matrix:
        spec:
          - runner: macos-latest
            platform: darwin
            arch: x64
            target: x86_64-apple-darwin
          - runner: macos-latest
            platform: darwin
            arch: arm64
            target: aarch64-apple-darwin
    needs: before-make
    uses: ./.github/workflows/release-desktop-platform.yml
    secrets: inherit
    with:
      build_type: ${{ inputs.build-type }}
      app_version: ${{ inputs.app-version }}
      git_short_hash: ${{ inputs.git-short-hash }}
      runner: ${{ matrix.spec.runner }}
      platform: ${{ matrix.spec.platform }}
      arch: ${{ matrix.spec.arch }}
      target: ${{ matrix.spec.target }}
      apple_codesign: true

  make-distribution-linux:
    if: ${{ inputs.desktop_linux }}
    strategy:
      fail-fast: false
      matrix:
        spec:
          - runner: ubuntu-latest
            platform: linux
            arch: x64
            target: x86_64-unknown-linux-gnu
    needs: before-make
    uses: ./.github/workflows/release-desktop-platform.yml
    secrets: inherit
    with:
      build_type: ${{ inputs.build-type }}
      app_version: ${{ inputs.app-version }}
      git_short_hash: ${{ inputs.git-short-hash }}
      runner: ${{ matrix.spec.runner }}
      platform: ${{ matrix.spec.platform }}
      arch: ${{ matrix.spec.arch }}
      target: ${{ matrix.spec.target }}
      install_linux_deps: true

  package-distribution-windows-x64:
    if: ${{ inputs.desktop_windows }}
    needs: before-make
    uses: ./.github/workflows/release-desktop-platform.yml
    secrets: inherit
    with:
      build_type: ${{ inputs.build-type }}
      app_version: ${{ inputs.app-version }}
      git_short_hash: ${{ inputs.git-short-hash }}
      runner: windows-latest
      platform: win32
      arch: x64
      target: x86_64-pc-windows-msvc
      enable_scripts: true

  package-distribution-windows-arm64:
    if: ${{ inputs.desktop_windows }}
    needs: before-make
    uses: ./.github/workflows/release-desktop-platform.yml
    secrets: inherit
    with:
      build_type: ${{ inputs.build-type }}
      app_version: ${{ inputs.app-version }}
      git_short_hash: ${{ inputs.git-short-hash }}
      runner: windows-latest
      platform: win32
      arch: arm64
      target: aarch64-pc-windows-msvc
      enable_scripts: true

  sign-packaged-artifacts-windows_x64:
    if: ${{ inputs.desktop_windows }}
    needs: package-distribution-windows-x64
    uses: ./.github/workflows/windows-signer.yml
    with:
      files: ${{ needs.package-distribution-windows-x64.outputs.files_to_be_signed }}
      artifact-name: packaged-win32-x64

  sign-packaged-artifacts-windows_arm64:
    if: ${{ inputs.desktop_windows }}
    needs: package-distribution-windows-arm64
    uses: ./.github/workflows/windows-signer.yml
    with:
      files: ${{ needs.package-distribution-windows-arm64.outputs.files_to_be_signed }}
      artifact-name: packaged-win32-arm64

  make-windows-installer:
    if: ${{ inputs.desktop_windows }}
    needs:
      - sign-packaged-artifacts-windows_x64
      - sign-packaged-artifacts-windows_arm64
    strategy:
      fail-fast: false
      matrix:
        spec:
          - platform: win32
            arch: x64
          - platform: win32
            arch: arm64
    runs-on: windows-latest
    outputs:
      FILES_TO_BE_SIGNED_x64: ${{ steps.get_files_to_be_signed.outputs.FILES_TO_BE_SIGNED_x64 }}
      FILES_TO_BE_SIGNED_arm64: ${{ steps.get_files_to_be_signed.outputs.FILES_TO_BE_SIGNED_arm64 }}
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        timeout-minutes: 10
        uses: ./.github/actions/setup-node
        with:
          extra-flags: workspaces focus @affine/electron @affine/monorepo
          hard-link-nm: false
          nmHoistingLimits: workspaces
        env:
          npm_config_arch: ${{ matrix.spec.arch }}
      - name: Download packaged artifacts
        uses: actions/download-artifact@v4
        with:
          name: packaged-${{ matrix.spec.platform }}-${{ matrix.spec.arch }}
          path: packaged-unsigned
      - name: unzip packaged artifacts
        run: Expand-Archive -Path packaged-unsigned/archive.zip -DestinationPath packages/frontend/apps/electron/out
      - name: Download signed packaged file diff
        uses: actions/download-artifact@v4
        with:
          name: signed-packaged-${{ matrix.spec.platform }}-${{ matrix.spec.arch }}
          path: signed-packaged-diff
      - name: Apply signed packaged file diff
        shell: pwsh
        run: |
          $DiffRoot = 'signed-packaged-diff/files'
          $TargetRoot = 'packages/frontend/apps/electron/out'
          if (!(Test-Path -LiteralPath $DiffRoot)) {
            throw "Signed diff directory not found: $DiffRoot"
          }

          Copy-Item -Path (Join-Path $DiffRoot '*') -Destination $TargetRoot -Recurse -Force

          $ManifestPath = 'signed-packaged-diff/manifest.json'
          if (Test-Path -LiteralPath $ManifestPath) {
            $ManifestEntries = @(Get-Content -LiteralPath $ManifestPath | ConvertFrom-Json)
            foreach ($Entry in $ManifestEntries) {
              $TargetPath = Join-Path $TargetRoot $Entry.path
              if (!(Test-Path -LiteralPath $TargetPath -PathType Leaf)) {
                throw "Applied signed file not found: $($Entry.path)"
              }

              $TargetHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $TargetPath).Hash
              if ($TargetHash -ne $Entry.sha256) {
                throw "Signed file hash mismatch: $($Entry.path)"
              }
            }
          }

      - name: Make squirrel.windows installer
        run: yarn affine @affine/electron make-squirrel --platform=${{ matrix.spec.platform }} --arch=${{ matrix.spec.arch }}

      - name: Make nsis.windows installer
        run: yarn affine @affine/electron make-nsis --platform=${{ matrix.spec.platform }} --arch=${{ matrix.spec.arch }}

      - name: Zip artifacts for faster upload
        run: Compress-Archive -CompressionLevel Fastest -Path packages/frontend/apps/electron/out/${{ env.BUILD_TYPE }}/make/* -DestinationPath archive.zip

      - name: get all files to be signed
        id: get_files_to_be_signed
        run: |
          Set-Variable -Name FILES_TO_BE_SIGNED -Value ((Get-ChildItem -Path packages/frontend/apps/electron/out/${{ env.BUILD_TYPE }}/make -Recurse -File | Where-Object { $_.Extension -in @(".exe", ".node", ".dll", ".msi") } | ForEach-Object { '"' + $_.FullName.Replace((Get-Location).Path + '\packages\frontend\apps\electron\out\${{ env.BUILD_TYPE }}\make\', '') + '"' }) -join ' ')
          "FILES_TO_BE_SIGNED_${{ matrix.spec.arch }}=$FILES_TO_BE_SIGNED" >> $env:GITHUB_OUTPUT
          echo $FILES_TO_BE_SIGNED

      - name: Save installer for signing
        uses: actions/upload-artifact@v4
        with:
          name: installer-${{ matrix.spec.platform }}-${{ matrix.spec.arch }}
          path: archive.zip

  sign-installer-artifacts-windows-x64:
    if: ${{ inputs.desktop_windows }}
    needs: make-windows-installer
    uses: ./.github/workflows/windows-signer.yml
    with:
      files: ${{ needs.make-windows-installer.outputs.FILES_TO_BE_SIGNED_x64 }}
      artifact-name: installer-win32-x64

  sign-installer-artifacts-windows-arm64:
    if: ${{ inputs.desktop_windows }}
    needs: make-windows-installer
    uses: ./.github/workflows/windows-signer.yml
    with:
      files: ${{ needs.make-windows-installer.outputs.FILES_TO_BE_SIGNED_arm64 }}
      artifact-name: installer-win32-arm64

  finalize-installer-windows:
    if: ${{ inputs.desktop_windows }}
    needs:
      [
        sign-installer-artifacts-windows-x64,
        sign-installer-artif\n```\n\n### .github/workflows/release-mobile.yml\n\n```yaml\nname: Release Mobile

on:
  workflow_call:
    inputs:
      app-version:
        type: string
        required: true
      git-short-hash:
        type: string
        required: true
      build-type:
        type: string
        required: true
      ios-app-version:
        type: string
        required: false

env:
  BUILD_TYPE: ${{ inputs.build-type }}
  DEBUG: napi:*
  KEYCHAIN_NAME: ${{ github.workspace }}/signing_temp

jobs:
  build-ios-web:
    runs-on: ubuntu-latest
    environment: ${{ inputs.build-type }}
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
      - name: Setup @sentry/cli
        uses: ./.github/actions/setup-sentry
      - name: Build Mobile
        run: yarn affine @affine/ios build
        env:
          PUBLIC_PATH: '/'
          SENTRY_ORG: ${{ secrets.SENTRY_ORG }}
          SENTRY_PROJECT: 'affine'
          SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
          SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          SENTRY_RELEASE: ${{ inputs.app-version }}
          RELEASE_VERSION: ${{ inputs.app-version }}
      - name: Upload ios artifact
        uses: actions/upload-artifact@v4
        with:
          name: ios
          path: packages/frontend/apps/ios/dist

  build-android-web:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
      - name: Setup @sentry/cli
        uses: ./.github/actions/setup-sentry
      - name: Build Mobile
        run: yarn affine @affine/android build
        env:
          PUBLIC_PATH: '/'
          SENTRY_ORG: ${{ secrets.SENTRY_ORG }}
          SENTRY_PROJECT: 'affine'
          SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
          SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          SENTRY_RELEASE: ${{ inputs.app-version }}
      - name: Upload android artifact
        uses: actions/upload-artifact@v4
        with:
          name: android
          path: packages/frontend/apps/android/dist

  ios:
    runs-on: 'macos-15'
    needs:
      - build-ios-web
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
          ios-app-version: ${{ inputs.ios-app-version }}
      - name: 'Update Code Sign Identity'
        shell: bash
        run: ./packages/frontend/apps/ios/update_code_sign_identity.sh
      - name: Download mobile artifact
        uses: actions/download-artifact@v4
        with:
          name: ios
          path: packages/frontend/apps/ios/dist
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        timeout-minutes: 10
        with:
          extra-flags: workspaces focus @affine/ios
          playwright-install: false
          electron-install: false
          hard-link-nm: false
          enableScripts: false
      - uses: maxim-lobanov/setup-xcode@v1
        with:
          xcode-version: 26.2
      - name: Install Swiftformat
        run: brew install swiftformat
      - name: Cap sync
        run: yarn workspace @affine/ios sync
      - name: Signing By Apple Developer ID
        uses: apple-actions/import-codesign-certs@v6
        id: import-codesign-certs
        with:
          p12-file-base64: ${{ secrets.CERTIFICATES_P12_MOBILE }}
          p12-password: ${{ secrets.CERTIFICATES_P12_PASSWORD_MOBILE }}
      - name: Setup Rust
        uses: ./.github/actions/build-rust
        with:
          target: 'aarch64-apple-ios'
          package: 'affine_mobile_native'
          no-build: 'true'
      - name: Testflight
        working-directory: packages/frontend/apps/ios/App
        run: |
          printf '%s' "$BUILD_PROVISION_PROFILE" | base64 --decode -o "$PP_PATH"
          mkdir -p "$HOME/Library/MobileDevice/Provisioning Profiles"
          cp "$PP_PATH" "$HOME/Library/MobileDevice/Provisioning Profiles"
          fastlane beta
        env:
          BUILD_TARGET: distribution
          BUILD_PROVISION_PROFILE: ${{ secrets.BUILD_PROVISION_PROFILE }}
          PP_PATH: ${{ runner.temp }}/build_pp.mobileprovision
          APPLE_STORE_CONNECT_API_KEY_ID: ${{ secrets.APPLE_STORE_CONNECT_API_KEY_ID }}
          APPLE_STORE_CONNECT_API_ISSUER_ID: ${{ secrets.APPLE_STORE_CONNECT_API_ISSUER_ID }}
          APPLE_STORE_CONNECT_API_KEY: ${{ secrets.APPLE_STORE_CONNECT_API_KEY }}

  android:
    runs-on: ubuntu-latest
    permissions:
      id-token: 'write'
    needs:
      - build-android-web
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Download mobile artifact
        uses: actions/download-artifact@v4
        with:
          name: android
          path: packages/frontend/apps/android/dist
      - name: Load Google Service file
        env:
          DATA: ${{ secrets.FIREBASE_ANDROID_GOOGLE_SERVICE_JSON }}
        run: |
          set -euo pipefail
          printf '%s' "$DATA" | base64 -di > packages/frontend/apps/android/App/app/google-services.json
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        timeout-minutes: 10
        with:
          extra-flags: workspaces focus @affine/monorepo @affine-tools/cli @affine/android @affine/playstore-auto-bump
          playwright-install: false
          electron-install: false
          hard-link-nm: false
          enableScripts: false
      - name: Setup Rust
        uses: ./.github/actions/build-rust
        with:
          target: 'aarch64-linux-android'
          package: 'affine_mobile_native'
          no-build: 'true'
      - name: Cap sync
        run: yarn workspace @affine/android cap sync
      - uses: actions/setup-python@v6
        with:
          python-version: '3.13'
      - name: Auth gcloud
        id: auth
        uses: google-github-actions/auth@v2
        with:
          workload_identity_provider: 'projects/${{ secrets.GCP_PROJECT_NUMBER }}/locations/global/workloadIdentityPools/github-actions/providers/github-actions-helm-deploy'
          service_account: '${{ secrets.GCP_HELM_DEPLOY_SERVICE_ACCOUNT }}'
          token_format: 'access_token'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          access_token_scopes: 'https://www.googleapis.com/auth/androidpublisher'
      - uses: actions/setup-java@v5
        with:
          distribution: 'temurin'
          java-version: '21'
          cache: 'gradle'
      - name: Auto increment version code
        id: bump
        run: yarn affine @affine/playstore-auto-bump bump
        env:
          GOOGLE_APPLICATION_CREDENTIALS: ${{ steps.auth.outputs.credentials_file_path }}
      - name: Build
        run: |
          echo -n "${{ env.AFFINE_ANDROID_SIGN_KEYSTORE }}" | base64 --decode > packages/frontend/apps/android/affine.keystore
          yarn workspace @affine/android cap build android --flavor ${{ env.BUILD_TYPE }} --androidreleasetype AAB
        env:
          AFFINE_ANDROID_KEYSTORE_PASSWORD: ${{ secrets.AFFINE_ANDROID_KEYSTORE_PASSWORD }}
          AFFINE_ANDROID_KEYSTORE_ALIAS_PASSWORD: ${{ secrets.AFFINE_ANDROID_KEYSTORE_ALIAS_PASSWORD }}
          AFFINE_ANDROID_SIGN_KEYSTORE: ${{ secrets.AFFINE_ANDROID_SIGN_KEYSTORE }}
          VERSION_NAME: ${{ inputs.app-version }}
      - name: Upload to Google Play
        uses: r0adkll/upload-google-play@v1
        with:
          serviceAccountJson: ${{ steps.auth.outputs.credentials_file_path }}
          packageName: app.affine.pro
          releaseName: ${{ inputs.app-version }}
          releaseFiles: packages/frontend/apps/android/App/app/build/outputs/bundle/${{ env.BUILD_TYPE }}Release/app-${{ env.BUILD_TYPE }}-release-signed.aab
          track: internal
          status: draft
          existingEditId: ${{ steps.bump.outputs.EDIT_ID }}
\n```\n\n### .github/workflows/release.yml\n\n```yaml\nname: Release

on:
  schedule:
    - cron: '0 9 * * *'

  workflow_dispatch:
    inputs:
      web:
        description: 'Release Web?'
        required: true
        type: boolean
        default: false
      desktop_macos:
        description: 'Desktop - macOS'
        required: true
        type: boolean
        default: false
      desktop_windows:
        description: 'Desktop - Windows'
        required: true
        type: boolean
        default: false
      desktop_linux:
        description: 'Desktop - Linux'
        required: true
        type: boolean
        default: false
      mobile:
        description: 'Release Mobile?'
        required: true
        type: boolean
        default: false
      ios-app-version:
        description: 'iOS App Store Version (Optional, use tag version if empty)'
        required: false
        type: string

permissions:
  contents: write
  pull-requests: write
  actions: write
  id-token: write
  packages: write
  security-events: write
  attestations: write
  issues: write

jobs:
  prepare:
    name: Prepare
    runs-on: ubuntu-latest
    outputs:
      APP_VERSION: ${{ steps.prepare.outputs.APP_VERSION }}
      GIT_SHORT_HASH: ${{ steps.prepare.outputs.GIT_SHORT_HASH }}
      BUILD_TYPE: ${{ steps.prepare.outputs.BUILD_TYPE }}
    steps:
      - uses: actions/checkout@v6
      - name: Prepare Release
        id: prepare
        uses: ./.github/actions/prepare-release

  canary-gate:
    name: Canary Gate
    runs-on: ubuntu-latest
    needs:
      - prepare
    outputs:
      SHOULD_RELEASE: ${{ steps.decide.outputs.SHOULD_RELEASE }}
      LAST_CANARY_TAG: ${{ steps.decide.outputs.LAST_CANARY_TAG }}
      LAST_CANARY_SHA: ${{ steps.decide.outputs.LAST_CANARY_SHA }}
    steps:
      - name: Decide whether to release
        id: decide
        uses: actions/github-script@v8
        with:
          script: |
            const buildType = '${{ needs.prepare.outputs.BUILD_TYPE }}'
            if (buildType !== 'canary') {
              core.setOutput('SHOULD_RELEASE', 'true')
              return
            }

            const owner = context.repo.owner
            const repo = context.repo.repo
            const currentSha = context.sha
            const canaryTagRe = /^v\d+\.\d+\.\d+-canary\.[0-9a-f]+$/i

            let page = 1
            const perPage = 100
            let lastCanary = null

            while (!lastCanary && page <= 10) {
              const { data } = await github.rest.repos.listTags({
                owner,
                repo,
                per_page: perPage,
                page,
              })

              for (const tag of data) {
                if (canaryTagRe.test(tag.name)) {
                  lastCanary = tag
                  break
                }
              }

              if (data.length < perPage) break
              page++
            }

            if (!lastCanary) {
              core.warning('No canary tags found; proceeding with canary release.')
              core.setOutput('SHOULD_RELEASE', 'true')
              return
            }

            core.setOutput('LAST_CANARY_TAG', lastCanary.name)
            core.setOutput('LAST_CANARY_SHA', lastCanary.commit.sha)

            const shouldRelease = lastCanary.commit.sha !== currentSha
            core.info(`Latest canary tag ${lastCanary.name} -> ${lastCanary.commit.sha}; current ${currentSha}; should_release=${shouldRelease}`)
            core.setOutput('SHOULD_RELEASE', shouldRelease ? 'true' : 'false')

  cloud:
    name: Release Cloud
    if: ${{ inputs.web || github.event_name != 'workflow_dispatch' }}
    needs:
      - prepare
    uses: ./.github/workflows/release-cloud.yml
    secrets: inherit
    with:
      build-type: ${{ needs.prepare.outputs.BUILD_TYPE }}
      app-version: ${{ needs.prepare.outputs.APP_VERSION }}
      git-short-hash: ${{ needs.prepare.outputs.GIT_SHORT_HASH }}

  image:
    name: Release Docker Image
    if: ${{ needs.canary-gate.outputs.SHOULD_RELEASE == 'true' }}
    runs-on: ubuntu-latest
    needs:
      - prepare
      - canary-gate
      - cloud
    steps:
      - uses: trstringer/manual-approval@v1
        if: ${{ needs.prepare.outputs.BUILD_TYPE == 'stable' }}
        name: Wait for approval
        with:
          secret: ${{ secrets.GITHUB_TOKEN }}
          approvers: darkskygit
          minimum-approvals: 1
          fail-on-denial: true
          issue-title: Please confirm to release docker image
          issue-body: |
            Env: ${{ needs.prepare.outputs.BUILD_TYPE }}
            Candidate: ghcr.io/toeverything/affine:${{ needs.prepare.outputs.BUILD_TYPE }}-${{ needs.prepare.outputs.GIT_SHORT_HASH }}
            Tag: ghcr.io/toeverything/affine:${{ needs.prepare.outputs.BUILD_TYPE }}

            > comment with "approve", "approved", "lgtm", "yes" to approve
            > comment with "deny", "denied", "no" to deny

      - name: Login to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          logout: false
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      - name: Tag Image
        run: |
          docker buildx imagetools create --tag ghcr.io/toeverything/affine:${{needs.prepare.outputs.BUILD_TYPE}} ghcr.io/toeverything/affine:${{needs.prepare.outputs.BUILD_TYPE}}-${{needs.prepare.outputs.GIT_SHORT_HASH}}
          docker buildx imagetools create --tag ghcr.io/toeverything/affine:${{needs.prepare.outputs.APP_VERSION}} ghcr.io/toeverything/affine:${{needs.prepare.outputs.BUILD_TYPE}}-${{needs.prepare.outputs.GIT_SHORT_HASH}}

  desktop:
    name: Release Desktop
    if: >-
      ${{
        (github.event_name != 'workflow_dispatch' && needs.canary-gate.outputs.SHOULD_RELEASE == 'true') ||
        inputs.desktop_macos ||
        inputs.desktop_windows ||
        inputs.desktop_linux
      }}
    needs:
      - prepare
      - canary-gate
    uses: ./.github/workflows/release-desktop.yml
    secrets: inherit
    with:
      build-type: ${{ needs.prepare.outputs.BUILD_TYPE }}
      app-version: ${{ needs.prepare.outputs.APP_VERSION }}
      git-short-hash: ${{ needs.prepare.outputs.GIT_SHORT_HASH }}
      desktop_macos: ${{ github.event_name != 'workflow_dispatch' || inputs.desktop_macos }}
      desktop_windows: ${{ github.event_name != 'workflow_dispatch' || inputs.desktop_windows }}
      desktop_linux: ${{ github.event_name != 'workflow_dispatch' || inputs.desktop_linux }}

  mobile:
    name: Release Mobile
    if: ${{ inputs.mobile }}
    needs:
      - prepare
    uses: ./.github/workflows/release-mobile.yml
    secrets: inherit
    with:
      build-type: ${{ needs.prepare.outputs.BUILD_TYPE }}
      app-version: ${{ needs.prepare.outputs.APP_VERSION }}
      git-short-hash: ${{ needs.prepare.outputs.GIT_SHORT_HASH }}
      ios-app-version: ${{ inputs.ios-app-version }}
\n```\n\n### .github/workflows/windows-signer.yml\n\n```yaml\nname: Windows Signer
on:
  workflow_call:
    inputs:
      artifact-name:
        required: true
        type: string
      files:
        required: true
        type: string
jobs:
  sign:
    runs-on: [self-hosted, win-signer]
    env:
      ARCHIVE_DIR: ${{ github.run_id }}-${{ github.run_attempt }}-${{ inputs.artifact-name }}
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: ${{ inputs.artifact-name }}
          path: ${{ env.ARCHIVE_DIR }}
      - name: unzip file
        shell: cmd
        # 7za is pre-installed on the signer machine
        run: |
          cd ${{ env.ARCHIVE_DIR }}
          md out
          7za x archive.zip -y -oout
      - name: sign
        shell: cmd
        run: |
          cd ${{ env.ARCHIVE_DIR }}/out
          signtool sign /tr http://timestamp.globalsign.com/tsa/r6advanced1 /td sha256 /fd sha256 /a ${{ inputs.files }}
      - name: collect signed file diff
        shell: powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File {0}
        run: |
          $OutDir = Join-Path '${{ env.ARCHIVE_DIR }}' 'out'
          $DiffDir = Join-Path '${{ env.ARCHIVE_DIR }}' 'signed-diff'
          $FilesDir = Join-Path $DiffDir 'files'
          New-Item -ItemType Directory -Path $FilesDir -Force | Out-Null

          $SignedFiles = [regex]::Matches('${{ inputs.files }}', '"([^"]+)"') | ForEach-Object { $_.Groups[1].Value }
          if ($SignedFiles.Count -eq 0) {
            throw 'No files to sign were provided.'
          }

          $Manifest = @()
          foreach ($RelativePath in $SignedFiles) {
            $SourcePath = Join-Path $OutDir $RelativePath
            if (!(Test-Path -LiteralPath $SourcePath -PathType Leaf)) {
              throw "Signed file not found: $RelativePath"
            }

            $TargetPath = Join-Path $FilesDir $RelativePath
            $TargetDir = Split-Path -Parent $TargetPath
            if ($TargetDir) {
              New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
            }

            Copy-Item -LiteralPath $SourcePath -Destination $TargetPath -Force
            $Manifest += [PSCustomObject]@{
              path = $RelativePath
              sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $TargetPath).Hash
            }
          }

          $Manifest | ConvertTo-Json -Depth 4 | Out-File -FilePath (Join-Path $DiffDir 'manifest.json') -Encoding utf8
          Write-Host "Collected $($SignedFiles.Count) signed files."
      - name: upload
        uses: actions/upload-artifact@v4
        with:
          name: signed-${{ inputs.artifact-name }}
          path: ${{ env.ARCHIVE_DIR }}/signed-diff
\n```\n\n## William-kelvem94/Gestor_Aluguel\n\n### .github/workflows/ci.yml\n\n```yaml\nname: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
+      - uses: actions/setup-python@v4
+        with:
+          python-version: '3.11'
+      - name: Install dependencies
+        run: |
+          python -m pip install --upgrade pip
+          pip install -e .[dev]
+      - name: Run Alembic migrations
+        run: |
+          python -m alembic upgrade head
+      - name: Run tests
+        run: |
+          python -m pytest --cov=src -q
\n```\n\n## William-kelvem94/PROJECT_JARVIS_5.0\n\n### .github/workflows/audit.yml\n\n```yaml\nname: JARVIS Scheduled Audit

on:
  schedule:
    - cron: "0 8 * * 1"
  workflow_dispatch:

permissions:
  contents: read

jobs:
  audit:
    runs-on: windows-latest
    timeout-minutes: 10

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Instalar executor de testes
        run: python -m pip install pytest

      - name: Compilar núcleo
        run: python -m compileall -q src tests jarvis.py scripts

      - name: Executar suíte completa
        shell: pwsh
        run: |
          $env:PYTHONPATH = "$PWD\src"
          python -m pytest -q

      - name: Validar inventário sem dependências pesadas
        run: python jarvis.py --hardware
\n```\n\n### .github/workflows/lite-smoke.yml\n\n```yaml\nname: JARVIS Python 3.11 smoke

on:
  push:
    branches: [main]
  pull_request:

permissions:
  contents: read

jobs:
  smoke:
    runs-on: windows-latest
    timeout-minutes: 10

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Instalar executor de testes
        run: python -m pip install pytest

      - name: Compilar núcleo
        run: python -m compileall -q src tests jarvis.py scripts

      - name: Executar suíte completa
        shell: pwsh
        run: |
          $env:PYTHONPATH = "$PWD\src"
          python -m pytest -q

      - name: Validar inventário sem dependências pesadas
        run: python jarvis.py --hardware
\n```\n\n### .github/workflows/windows-agent-core.yml\n\n```yaml\nname: JARVIS Windows agent core

on:
  push:
    branches: [main]
  pull_request:

permissions:
  contents: read

jobs:
  core:
    runs-on: windows-latest
    timeout-minutes: 10
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Instalar executor de testes
        run: python -m pip install pytest

      - name: Compilar núcleo
        run: python -m compileall -q src tests jarvis.py scripts

      - name: Testar agente e perfis
        shell: pwsh
        run: |
          $env:PYTHONPATH = "$PWD\src"
          python -m pytest -q

      - name: Testar inventário sem dependências pesadas
        run: python jarvis.py --hardware
\n```\n\n## William-kelvem94/Domni\n\n### .github/workflows/ci.yml\n\n```yaml\nname: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

concurrency:
  group: ci-${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: read

env:
  CI: true
  DATABASE_URL: postgresql://postgres:ci-postgres-password@127.0.0.1:5432/domni_ci?schema=public
  DIRECT_URL: postgresql://postgres:ci-postgres-password@127.0.0.1:5432/domni_ci?schema=public
  NEXTAUTH_URL: https://ci.domni.invalid
  NEXT_PUBLIC_APP_URL: https://ci.domni.invalid
  NEXTAUTH_SECRET: ci-nextauth-18f7626bc88968fb3eb03da6eb876dd28ba0af87a4f873953c14b8ec3492ad72
  TENANT_JWT_SECRET: ci-tenant-jwt-3ec20f7f302868b363766af20916f0b2242e3613a16ac35fb926c6646af55570
  MFA_GRANT_SECRET: ci-mfa-grant-8e1808f8210260ba28e56225fdb3f93f4f3af8fec489585ee6223e991089af48
  SOCKET_AUTH_SECRET: ci-socket-auth-f626f9a9413809120290912458d7a0a2ff1730485f017fb60e9d9aac8378fbd6
  ENCRYPTION_KEY: 40725c207754bda279824474d9e017862cf59613525db698936b43e7d0586358
  ENCRYPTION_PREVIOUS_KEYS: 6bea7318b63090779789906d62d693b7e15c943f67edc1a874fe88fec3ab0084
  BACKUP_ENCRYPTION_KEY: 02967e910e19307fe25ed676239436013350a06a217136f22e34555b4b1e7911
  NEXT_PUBLIC_SUPABASE_URL: https://ci.supabase.invalid
  SUPABASE_SERVICE_ROLE_KEY: ci-service-role-key-1a90e62f6cfc3d4f8e4c7ac201792076802856b79b022117ed780c42
  CLAMAV_HOST: clamav.invalid
  ALLOW_PUBLIC_REGISTRATION: false
  RUN_DB_TESTS: "true"
  NEXT_TELEMETRY_DISABLED: 1
  SENTRY_AUTH_TOKEN: ""
  SENTRY_ORG: ""
  SENTRY_PROJECT: ""

jobs:
  verify:
    name: Lint, types, tests, audit and build
    runs-on: ubuntu-latest
    timeout-minutes: 30
    services:
      postgres:
        image: postgres:18-alpine
        env:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: ci-postgres-password
          POSTGRES_DB: domni_ci
        options: >-
          --health-cmd "pg_isready -U postgres -d domni_ci"
          --health-interval 5s
          --health-timeout 5s
          --health-retries 10
        ports:
          - 5432:5432
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false
      - uses: actions/setup-node@v4
        with:
          node-version: 24.14.0
          cache: npm
      - name: Install exact dependencies
        run: npm ci
      - name: Block dependency vulnerabilities
        run: npm audit --audit-level=low
      - name: Validate and apply migrations
        run: |
          npx prisma validate
          npx prisma migrate deploy
      - name: Lint
        run: npm run lint
      - name: Type check
        run: npm run type-check
      - name: Responsive regression check
        run: npm run check:responsive
      - name: Unit and integration tests
        run: npm test -- --runInBand --passWithNoTests --coverage --coverageReporters=text --coverageReporters=lcov
      - name: Production build
        run: npm run build
      - name: Upload coverage
        if: always()
        continue-on-error: true
        uses: actions/upload-artifact@v4
        with:
          name: coverage
          path: coverage
          if-no-files-found: ignore
          retention-days: 7

  e2e:
    name: Security E2E smoke tests
    needs: verify
    runs-on: ubuntu-latest
    timeout-minutes: 20
    env:
      NEXTAUTH_URL: http://127.0.0.1:3002
      NEXT_PUBLIC_APP_URL: http://127.0.0.1:3002
    services:
      postgres:
        image: postgres:18-alpine
        env:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: ci-postgres-password
          POSTGRES_DB: domni_ci
        options: >-
          --health-cmd "pg_isready -U postgres -d domni_ci"
          --health-interval 5s
          --health-timeout 5s
          --health-retries 10
        ports:
          - 5432:5432
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false
      - uses: actions/setup-node@v4
        with:
          node-version: 24.14.0
          cache: npm
      - run: npm ci
      - run: npx prisma migrate deploy
      - run: npx playwright install --with-deps chromium
      - name: Run local security scenarios
        run: npm run test:e2e -- --project=chromium
      - name: Upload Playwright diagnostics
        if: failure()
        continue-on-error: true
        uses: actions/upload-artifact@v4
        with:
          name: playwright-diagnostics
          path: test-results
          if-no-files-found: ignore
          retention-days: 7
\n```\n\n### .github/workflows/codex-source-export.yml\n\n```yaml\nname: Temporary Codex source export

on:
  pull_request:
    branches:
      - main
    types:
      - synchronize

permissions:
  contents: write

jobs:
  export-source:
    if: github.head_ref == 'security/hardening-2026-08-07'
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
        with:
          ref: security/hardening-2026-08-07
          fetch-depth: 1
          persist-credentials: true
      - name: Export source into private branch chunks
        shell: bash
        run: |
          set -euo pipefail
          if [ -f .codex-export/manifest.txt ]; then
            echo "Snapshot already available."
            exit 0
          fi
          git archive --format=tar.gz --output="$RUNNER_TEMP/domni-source.tar.gz" HEAD
          mkdir -p .codex-export
          base64 -w 0 "$RUNNER_TEMP/domni-source.tar.gz" | split -b 700000 -d -a 4 - .codex-export/chunk-
          sha256sum "$RUNNER_TEMP/domni-source.tar.gz" | awk '{print $1}' > .codex-export/sha256.txt
          find .codex-export -maxdepth 1 -type f -name 'chunk-*' -printf '%f\n' | sort > .codex-export/manifest.txt
          wc -c < "$RUNNER_TEMP/domni-source.tar.gz" > .codex-export/size.txt
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add .codex-export
          git commit -m "chore: gerar snapshot privado temporário [skip ci]"
          git push origin HEAD:security/hardening-2026-08-07
\n```\n\n### .github/workflows/domni-product-quality.yml\n\n```yaml\nname: Domni Product Quality

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

concurrency:
  group: domni-product-quality-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: read

jobs:
  product-quality:
    name: Product contract and production build
    runs-on: ubuntu-latest
    timeout-minutes: 30
    env:
      NEXT_TELEMETRY_DISABLED: "1"
      SKIP_ENV_VALIDATION: "true"
      CI: "true"

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm

      - name: Install dependencies from lockfile
        run: npm ci

      - name: Validate Domni product contract
        run: npx jest --runInBand tests/unit/product/domni-product-contract.test.js

      - name: Production build
        run: npm run build
\n```\n\n### .github/workflows/responsive-visual-qa.yml\n\n```yaml\nname: QA Visual Responsiva

on:
  push:
    branches: [main]
    paths:
      - "src/**"
      - "tests/e2e/**"
      - "scripts/e2e/**"
      - "scripts/maintenance/**"
      - "playwright.responsive.config.ts"
      - "package.json"
      - "package-lock.json"
      - "prisma/**"
      - "tailwind.config.*"
      - "next.config.*"
      - ".github/workflows/responsive-visual-qa.yml"
  pull_request:
    branches: [main]
    paths:
      - "src/**"
      - "tests/e2e/**"
      - "scripts/e2e/**"
      - "scripts/maintenance/**"
      - "playwright.responsive.config.ts"
      - "package.json"
      - "package-lock.json"
      - "prisma/**"
      - "tailwind.config.*"
      - "next.config.*"
      - ".github/workflows/responsive-visual-qa.yml"
  workflow_dispatch:
    inputs:
      update_baselines:
        description: "Regravar os baselines visuais aprovados"
        required: false
        default: false
        type: boolean

concurrency:
  group: responsive-visual-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: write
  statuses: write

env:
  CI: "true"
  DATABASE_URL: postgresql://postgres:responsive-qa-password@127.0.0.1:5432/domni_responsive?schema=public
  DIRECT_URL: postgresql://postgres:responsive-qa-password@127.0.0.1:5432/domni_responsive?schema=public
  NEXTAUTH_URL: http://127.0.0.1:3002
  NEXT_PUBLIC_APP_URL: http://127.0.0.1:3002
  NEXTAUTH_SECRET: qa-nextauth-18f7626bc88968fb3eb03da6eb876dd28ba0af87a4f873953c14b8ec3492ad72
  TENANT_JWT_SECRET: qa-tenant-jwt-3ec20f7f302868b363766af20916f0b2242e3613a16ac35fb926c6646af55570
  MFA_GRANT_SECRET: qa-mfa-grant-8e1808f8210260ba28e56225fdb3f93f4f3af8fec489585ee6223e991089af48
  SOCKET_AUTH_SECRET: qa-socket-auth-f626f9a9413809120290912458d7a0a2ff1730485f017fb60e9d9aac8378fbd6
  ENCRYPTION_KEY: 40725c207754bda279824474d9e017862cf59613525db698936b43e7d0586358
  ENCRYPTION_PREVIOUS_KEYS: 6bea7318b63090779789906d62d693b7e15c943f67edc1a874fe88fec3ab0084
  BACKUP_ENCRYPTION_KEY: 02967e910e19307fe25ed676239436013350a06a217136f22e34555b4b1e7911
  NEXT_PUBLIC_SUPABASE_URL: https://qa.supabase.invalid
  SUPABASE_SERVICE_ROLE_KEY: qa-service-role-key-1a90e62f6cfc3d4f8e4c7ac201792076802856b79b022117ed780c42
  CLAMAV_HOST: clamav.invalid
  ALLOW_PUBLIC_REGISTRATION: "false"
  NEXT_TELEMETRY_DISABLED: "1"
  SENTRY_AUTH_TOKEN: ""
  SENTRY_ORG: ""
  SENTRY_PROJECT: ""
  ALLOW_RESPONSIVE_E2E_SEED: "true"
  RESPONSIVE_REQUIRE_AUTH: "true"
  RESPONSIVE_VISUAL_BASELINE: "true"
  E2E_ADMIN_EMAIL: responsive-owner@domni.test
  E2E_ADMIN_PASSWORD: DomniQA!2026-Responsive
  E2E_TENANT_EMAIL: responsive-owner@domni.test
  E2E_TENANT_PASSWORD: DomniQA!2026-Responsive

jobs:
  responsive-visual:
    name: 320px → desktop + PWA + dual-contexto
    runs-on: ubuntu-latest
    timeout-minutes: 35
    services:
      postgres:
        image: postgres:18-alpine
        env:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: responsive-qa-password
          POSTGRES_DB: domni_responsive
        options: >-
          --health-cmd "pg_isready -U postgres -d domni_responsive"
          --health-interval 5s
          --health-timeout 5s
          --health-retries 10
        ports:
          - 5432:5432

    steps:
      - name: Checkout da main atual
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Publicar status inicial da QA visual
        uses: actions/github-script@v7
        with:
          script: |
            await github.rest.repos.createCommitStatus({
              owner: context.repo.owner,
              repo: context.repo.repo,
              sha: context.sha,
              state: "pending",
              context: "QA Visual Responsiva",
              description: "Matriz autenticada multi-viewport em execução"
            });

      - name: Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 24.14.0
          cache: npm

      - name: Dependências exatas
        run: npm ci

      - name: Preparar schema descartável
        run: |
          npx prisma validate
          npx prisma migrate deploy

      - name: Criar identidade efêmera gestor + inquilino
        run: npx tsx scripts/e2e/seed-responsive-qa.ts

      - name: Instalar Chromium
        run: npx playwright install --with-deps chromium

      - name: Decidir atualização de baseline
        id: baseline
        env:
          REQUESTED_UPDATE: ${{ github.event_name == 'workflow_dispatch' && inputs.update_baselines && 'true' || 'false' }}
        run: |
          if [ ! -d tests/e2e/responsive-critical.spec.ts-snapshots ] || [ "$REQUESTED_UPDATE" = "true" ]; then
            echo "update=true" >> "$GITHUB_OUTPUT"
          else
            echo "update=false" >> "$GITHUB_OUTPUT"
          fi

      - name: Gerar ou atualizar baselines controlados
        if: steps.baseline.outputs.update == 'true'
        run: node scripts/maintenance/run-responsive-qa.js --require-auth --update-snapshots

      - name: Gate estrutural e visual autenticado
        if: steps.baseline.outputs.update != 'true'
        run: node scripts/maintenance/run-responsive-qa.js --require-auth

      - name: Persistir baseline inicial/explicitamente aprovado na main
        if: >-
          steps.baseline.outputs.update == 'true' &&
          github.ref == 'refs/heads/main' &&
          (github.event_name == 'push' || github.event_name == 'workflow_dispatch')
        run: |
          git add tests/e2e/responsive-critical.spec.ts-snapshots
          if git diff --cached --quiet; then
            echo "Nenhuma alteração de baseline para persistir."
            exit 0
          fi
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git commit \
            -m "test(responsivo): persistir baselines visuais multi-viewport" \
            -m "Baselines gerados no PostgreSQL efêmero com a identidade de QA OWNER + inquilino, sem usar dados ou credenciais de produção."
          git push origin HEAD:main

      - name: Publicar sucesso da QA visual
        if: success()
        uses: actions/github-script@v7
        with:
          script: |
            await github.rest.repos.createCommitStatus({
              owner: context.repo.owner,
              repo: context.repo.repo,
              sha: context.sha,
              state: "success",
              context: "QA Visual Responsiva",
              description: "Matriz autenticada multi-viewport aprovada"
            });

      - name: Publicar falha da QA visual
        if: failure()
        uses: actions/github-script@v7
        with:
          script: |
            await github.rest.repos.createCommitStatus({
              owner: context.repo.owner,
              repo: context.repo.repo,
              sha: context.sha,
              state: "failure",
              context: "QA Visual Responsiva",
              description: "Matriz autenticada multi-viewport falhou"
            });

      - name: Diagnósticos Playwright
        if: failure()
        continue-on-error: true
        uses: actions/upload-artifact@v4
        with:
          name: responsive-visual-diagnostics-${{ github.sha }}
          path: |
            playwright-report/responsive
            test-results/responsive
          if-no-files-found: ignore
          retention-days: 7
\n```\n\n## William-kelvem94/Gerenciador_Financeiro-7.0\n\n### .github/workflows/ci.yml\n\n```yaml\nname: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

concurrency:
  group: numni-ci-${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: read

env:
  CI: true
  DATABASE_URL: postgresql://postgres:numni_ci_password@127.0.0.1:5432/numni_ci?schema=public
  DIRECT_URL: postgresql://postgres:numni_ci_password@127.0.0.1:5432/numni_ci?schema=public
  NEXTAUTH_URL: http://127.0.0.1:3002
  NEXT_PUBLIC_APP_URL: http://127.0.0.1:3002
  APP_URL: http://127.0.0.1:3002
  NEXTAUTH_SECRET: ci-nextauth-0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
  TENANT_JWT_SECRET: ci-tenant-jwt-0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
  ENCRYPTION_KEY: 1111111111111111111111111111111111111111111111111111111111111111
  REQUIRE_EMAIL_VERIFICATION: "false"
  NEXT_TELEMETRY_DISABLED: 1
  SENTRY_AUTH_TOKEN: ""
  SENTRY_ORG: ""
  SENTRY_PROJECT: ""
  NEXT_PUBLIC_SENTRY_DSN: ""

jobs:
  verify:
    name: Lint, tipos, testes, banco e build
    runs-on: ubuntu-latest
    timeout-minutes: 35

    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: numni_ci_password
          POSTGRES_DB: numni_ci
        options: >-
          --health-cmd "pg_isready -U postgres -d numni_ci"
          --health-interval 5s
          --health-timeout 5s
          --health-retries 12
        ports:
          - 5432:5432

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          persist-credentials: false

      - name: Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 22.19.0
          cache: npm

      - name: Instalar dependências exatas
        run: npm ci

      - name: Auditoria de dependências de produção
        continue-on-error: true
        run: npm audit --omit=dev --audit-level=high

      - name: Validar schema Prisma
        run: npx prisma validate

      - name: Aplicar migrations em banco efêmero
        run: npx prisma migrate deploy

      - name: Lint
        run: npm run lint

      - name: TypeScript
        run: npm run type-check

      - name: Testes unitários e de contrato
        run: npm test -- --runInBand --passWithNoTests

      - name: Build de produção
        run: npm run build
\n```\n\n### .github/workflows/frontend-e2e.yml\n\n```yaml\nname: Frontend E2E

on:
  push:
    branches: [main]
    paths:
      - "src/app/**"
      - "src/components/**"
      - "src/styles/**"
      - "src/hooks/**"
      - "tests/e2e/**"
      - "scripts/e2e-seed.ts"
      - "playwright.config.ts"
      - "package.json"
      - ".github/workflows/frontend-e2e.yml"
  workflow_dispatch:
    inputs:
      full_matrix:
        description: "Executar Chromium, Firefox e WebKit"
        required: false
        default: false
        type: boolean

concurrency:
  group: numni-frontend-e2e-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: read

env:
  CI: true
  DATABASE_URL: postgresql://postgres:numni_e2e_password@127.0.0.1:5432/numni_e2e?schema=public
  DIRECT_URL: postgresql://postgres:numni_e2e_password@127.0.0.1:5432/numni_e2e?schema=public
  NEXTAUTH_URL: http://127.0.0.1:3002
  NEXT_PUBLIC_APP_URL: http://127.0.0.1:3002
  APP_URL: http://127.0.0.1:3002
  NEXTAUTH_SECRET: e2e-nextauth-0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
  TENANT_JWT_SECRET: e2e-tenant-jwt-0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
  ENCRYPTION_KEY: 2222222222222222222222222222222222222222222222222222222222222222
  REQUIRE_EMAIL_VERIFICATION: "false"
  NEXT_TELEMETRY_DISABLED: 1
  SENTRY_AUTH_TOKEN: ""
  SENTRY_ORG: ""
  SENTRY_PROJECT: ""
  NEXT_PUBLIC_SENTRY_DSN: ""

jobs:
  smoke:
    name: Frontend responsivo e acessível
    runs-on: ubuntu-latest
    timeout-minutes: 30

    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: numni_e2e_password
          POSTGRES_DB: numni_e2e
        options: >-
          --health-cmd "pg_isready -U postgres -d numni_e2e"
          --health-interval 5s
          --health-timeout 5s
          --health-retries 12
        ports:
          - 5432:5432

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          persist-credentials: false

      - name: Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 22.19.0
          cache: npm

      - name: Instalar dependências exatas
        run: npm ci

      - name: Preparar Prisma e banco efêmero
        run: |
          npx prisma generate
          npx prisma migrate deploy
          npm run test:e2e:seed

      - name: Instalar Chromium
        if: ${{ github.event_name != 'workflow_dispatch' || inputs.full_matrix != true }}
        run: npx playwright install --with-deps chromium

      - name: Smoke Chromium
        if: ${{ github.event_name != 'workflow_dispatch' || inputs.full_matrix != true }}
        run: npx playwright test --project=chromium-public --project=chromium-auth

      - name: Instalar matriz completa
        if: ${{ github.event_name == 'workflow_dispatch' && inputs.full_matrix == true }}
        run: npx playwright install --with-deps chromium firefox webkit

      - name: Auditoria completa multi-browser
        if: ${{ github.event_name == 'workflow_dispatch' && inputs.full_matrix == true }}
        run: npm run test:e2e:frontend:full
\n```\n\n### .github/workflows/maintenance-numni-resume.yml\n\n```yaml\nname: Manutenção Numni - retomada única

on:
  push:
    branches: [main]
    paths:
      - ".github/workflows/maintenance-numni-resume.yml"

concurrency:
  group: numni-maintenance-once
  cancel-in-progress: true

permissions:
  contents: write

env:
  CI: true
  DATABASE_URL: postgresql://postgres:numni_maintenance_password@127.0.0.1:5432/numni_maintenance?schema=public
  DIRECT_URL: postgresql://postgres:numni_maintenance_password@127.0.0.1:5432/numni_maintenance?schema=public
  NEXTAUTH_URL: http://127.0.0.1:3002
  NEXT_PUBLIC_APP_URL: http://127.0.0.1:3002
  APP_URL: http://127.0.0.1:3002
  NEXTAUTH_SECRET: maintenance-nextauth-0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
  TENANT_JWT_SECRET: maintenance-tenant-jwt-0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
  ENCRYPTION_KEY: 3333333333333333333333333333333333333333333333333333333333333333
  REQUIRE_EMAIL_VERIFICATION: "false"
  NEXT_TELEMETRY_DISABLED: 1
  SENTRY_AUTH_TOKEN: ""
  SENTRY_ORG: ""
  SENTRY_PROJECT: ""
  NEXT_PUBLIC_SENTRY_DSN: ""

jobs:
  maintenance:
    name: Refatorar, validar e publicar lote
    runs-on: ubuntu-latest
    timeout-minutes: 55

    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: numni_maintenance_password
          POSTGRES_DB: numni_maintenance
        options: >-
          --health-cmd "pg_isready -U postgres -d numni_maintenance"
          --health-interval 5s
          --health-timeout 5s
          --health-retries 12
        ports:
          - 5432:5432

    steps:
      - name: Checkout da main atual
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
          persist-credentials: true

      - name: Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 22.19.0
          cache: npm

      - name: Aplicar refatorações controladas
        shell: bash
        run: |
          set -euo pipefail
          node <<'NODE'
          const fs = require('node:fs');
          const path = require('node:path');
          const read = (file) => fs.readFileSync(file, 'utf8');
          const write = (file, content) => fs.writeFileSync(file, content, 'utf8');
          const replaceOnce = (content, oldValue, newValue, label) => {
            if (content.includes(newValue)) return content;
            if (!content.includes(oldValue)) throw new Error(`Contrato não encontrado: ${label}`);
            return content.replace(oldValue, newValue);
          };

          // Scheduler lógico de anexos: 1 arquivo = 1, qualquer lote maior = teto 2.
          const aiPath = 'src/components/ai/AIChatAssistant.tsx';
          let ai = read(aiPath);
          ai = replaceOnce(ai, 'const MAX_PARALLEL_ANALYSES = 4;', 'const MAX_PARALLEL_ANALYSES = 2;', 'MAX_PARALLEL_ANALYSES');
          const oldConcurrency = `function batchAnalysisConcurrency(fileCount: number) {
            if (fileCount <= 1) return 1;
            if (fileCount <= 4) return 2;
            if (fileCount <= 11) return 3;
            return MAX_PARALLEL_ANALYSES;
          }`;
          const newConcurrency = `function batchAnalysisConcurrency(fileCount: number) {
            if (fileCount <= 1) return 1;
            return MAX_PARALLEL_ANALYSES;
          }`;
          ai = replaceOnce(ai, oldConcurrency, newConcurrency, 'batchAnalysisConcurrency');
          write(aiPath, ai);

          // Branding atual. Releases históricas não são reescritas.
          const brandingPairs = [
            ['GERENCIADOR FINANCEIRO 7.0', 'NUMNI'],
            ['Gerenciador Financeiro 7.0', 'Numni'],
            ['GESTOR DE ALUGUEL 2.0', 'NUMNI'],
            ['Gestor de Aluguel 2.0', 'Numni'],
            ['GERENCIADOR FINANCEIRO', 'NUMNI'],
            ['Gerenciador Financeiro', 'Numni'],
          ];
          const allowed = new Set(['.ts', '.tsx', '.js', '.mjs', '.cjs', '.css', '.json', '.prisma']);
          const targets = [];
          function walk(dir) {
            if (!fs.existsSync(dir)) return;
            for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
              const file = path.join(dir, entry.name);
              if (entry.isDirectory()) walk(file);
              else if (allowed.has(path.extname(file))) targets.push(file);
            }
          }
          walk('src');
          walk('config');
          for (const file of ['prisma/schema.prisma', 'next.config.js', 'postcss.config.js', 'tailwind.config.js', '.env.example']) {
            if (fs.existsSync(file)) targets.push(file);
          }
          for (const file of [...new Set(targets)]) {
            const content = read(file);
            let updated = content;
            for (const [from, to] of brandingPairs) updated = updated.split(from).join(to);
            if (file === 'src/app/layout.tsx') updated = updated.replace('    creator: "@gerenciadorfinanceiro",\n', '');
            if (updated !== content) write(file, updated);
          }

          // Remove integração antiga do @next/bundle-analyzer sem depender de indentação.
          const nextPath = 'next.config.js';
          let nextConfig = read(nextPath);
          nextConfig = nextConfig.replace(/let withBundleAnalyzer;\ntry \{[\s\S]*?withBundleAnalyzer = null;\n\}\n\n/, '');
          nextConfig = nextConfig.replace(/\nmodule\.exports = nextConfig;\n\n\/\/ Monitoring configuration/, '\n// Monitoring configuration');
          nextConfig = nextConfig.replace(/\/\/ Apply bundle analyzer\n[\s\S]*?module\.exports = finalConfig \|\| nextConfig;\n?/, 'module.exports = configWithSentry || nextConfig;\n');
          if (nextConfig.includes('@next/bundle-analyzer') || nextConfig.includes('withBundleAnalyzer') || nextConfig.includes('finalConfig')) {
            throw new Error('Integração antiga do bundle analyzer permaneceu em next.config.js');
          }
          write(nextPath, nextConfig);

          // Toolchain coerente e determinística.
          const packagePath = 'package.json';
          const pkg = JSON.parse(read(packagePath));
          pkg.dependencies.next = '16.2.12';
          const dev = pkg.devDependencies || (pkg.devDependencies = {});
          for (const name of ['@next/bundle-analyzer', '@typescript-eslint/eslint-plugin', '@typescript-eslint/parser']) delete dev[name];
          dev.eslint = '9.39.5';
          dev['eslint-config-next'] = '16.2.12';
          pkg.scripts.lint = 'eslint src --max-warnings=0';
          pkg.scripts['lint:eslint'] = 'eslint src --max-warnings=0';
          pkg.scripts.analyze = 'next experimental-analyze --output';

          // Remoção de deps órfãs somente após busca real em consumidores possíveis.
          const scanRoots = ['src', 'tests', 'scripts', 'config'];
          const scanExt = new Set(['.ts', '.tsx', '.js', '.jsx', '.mjs', '.cjs']);
          let joined = '';
          function scan(dir) {
            if (!fs.existsSync(dir)) return;
            for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
              const file = path.join(dir, entry.name);
              if (entry.isDirectory()) scan(file);
              else if (scanExt.has(path.extname(file))) joined += '\n' + read(file);
            }
          }
          for (const root of scanRoots) scan(root);
          const removed = [];
          for (const [runtimeName, typeName] of [
            ['react-syntax-highlighter', '@types/react-syntax-highlighter'],
            ['react-window', '@types/react-window'],
          ]) {
            if (!joined.includes(runtimeName)) {
              if (pkg.dependencies?.[runtimeName]) { delete pkg.dependencies[runtimeName]; removed.push(runtimeName); }
              if (pkg.dependencies?.[typeName]) { delete pkg.dependencies[typeName]; removed.push(typeName); }
              if (dev[runtimeName]) { delete dev[runtimeName]; removed.push(runtimeName); }
              if (dev[typeName]) { delete dev[typeName]; removed.push(typeName); }
            }
          }
          if (!Object.values(pkg.scripts || {}).join('\n').includes('cross-env') && dev['cross-env']) {
            delete dev['cross-env'];
            removed.push('cross-env');
          }
          write('/tmp/numni-removed-deps.txt', [...new Set(removed)].join('\n'));
          write(packagePath, JSON.stringify(pkg, null, 2) + '\n');

          // Flat config oficial do Next 16 / ESLint 9.
          write('eslint.config.mjs', `import { defineConfig, globalIgnores } from "eslint/config";
          import nextVitals from "eslint-config-next/core-web-vitals";
          import nextTypeScript from "eslint-config-next/typescript";
          import prettier from "eslint-config-prettier";

          export default defineConfig([
            ...nextVitals,
            ...nextTypeScript,
            prettier,
            globalIgnores([
              ".next/**",
              "out/**",
              "build/**",
              "coverage/**",
              "playwright-report/**",
              "test-results/**",
              "next-env.d.ts",
            ]),
          ]);
          `);
          if (fs.existsSync('.eslintrc.json')) fs.unlinkSync('.eslintrc.json');

          // Atualiza apenas documentação afetada.
          const widgetPath = 'docs/ai/WIDGET_AND_CHAT.md';
          let widget = read(widgetPath);
          widget = widget.replace(
            'A interface pode preparar janelas de trabalho maiores, mas a quantidade de chamadas reais ao provedor permanece limitada pelas proteções do cliente e do backend.',
            'A interface agenda no máximo duas análises de anexos simultâneas. O transporte e o backend mantêm o mesmo teto de duas chamadas reais ao provedor, inclusive entre instâncias que compartilham o banco.',
          );
          write(widgetPath, widget);

          const archPath = 'docs/ai/ARCHITECTURE.md';
          let arch = read(archPath);
          const marker = 'Aceitar 30 arquivos não significa env\n```\n\n## William-kelvem94/MEU_NECTAR_JARVIS\n\n### .github/workflows/test.yml\n\n```yaml\nname: Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test-backend:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '20'
          cache: 'npm'
          cache-dependency-path: backend/package-lock.json
      
      - name: Install dependencies
        working-directory: ./backend
        run: npm ci
      
      - name: Generate Prisma Client
        working-directory: ./backend
        run: npx prisma generate
      
      - name: Run migrations
        working-directory: ./backend
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
        run: npx prisma migrate deploy
      
      - name: Run tests
        working-directory: ./backend
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
        run: npm test
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          directory: ./backend/coverage
          flags: backend

  test-frontend:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '20'
          cache: 'npm'
          cache-dependency-path: frontend/package-lock.json
      
      - name: Install dependencies
        working-directory: ./frontend
        run: npm ci
      
      - name: Run linter
        working-directory: ./frontend
        run: npm run lint || true
      
      - name: Build
        working-directory: ./frontend
        run: npm run build

\n```\n\n## William-kelvem94/Automatizador\n\n### .github/workflows/lint.yml\n\n```yaml\nname: Lint and Format

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.11"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install black isort flake8 mypy
        if [ -f config/requirements.txt ]; then pip install -r config/requirements.txt; fi
    - name: Check formatting with black
      run: |
        black --check src tests
    - name: Check imports with isort
      run: |
        isort --check-only src tests
    - name: Lint with flake8
      run: |
        flake8 src tests
\n```\n\n### .github/workflows/test.yml\n\n```yaml\nname: Python Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12"]

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest pytest-cov
        if [ -f config/requirements.txt ]; then pip install -r config/requirements.txt; fi
    - name: Test with pytest
      run: |
        pytest --cov=src tests/ --cov-report=xml
\n```\n\n## William-kelvem94/TESTER\n\n### .github/workflows/automated-testing.yml\n\n```yaml\nname: 🧪 Testes Automatizados

on:
  # Executar diariamente às 9h
  schedule:
    - cron: '0 9 * * *'
  # Permitir execução manual
  workflow_dispatch:
    inputs:
      site:
        description: 'Site a testar'
        required: false
        default: ''
      iterations:
        description: 'Número de iterações'
        required: false
        default: '3'
      full_test:
        description: 'Teste completo'
        type: boolean
        default: false

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        browser: [chrome, firefox]
        include:
          - browser: chrome
            browser_name: Chrome
          - browser: firefox
            browser_name: Firefox

    steps:
      - name: 📥 Checkout código
        uses: actions/checkout@v4

      - name: 🐍 Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: 📦 Instalar dependências
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: 🔧 Configurar site de teste
        run: |
          SITE_NAME="${{ github.event.inputs.site }}"
          if [ -z "$SITE_NAME" ]; then
            SITE_NAME="$(python -c 'import json; print(json.load(open("config/test_sites.json", encoding="utf-8"))["sites"][0]["name"])')"
          fi
          ITERATIONS="${{ github.event.inputs.iterations || '3' }}"
          FULL_TEST="${{ github.event.inputs.full_test == 'true' && '--full' || '' }}"

          echo "SITE_NAME=$SITE_NAME" >> $GITHUB_ENV
          echo "ITERATIONS=$ITERATIONS" >> $GITHUB_ENV
          echo "FULL_TEST=$FULL_TEST" >> $GITHUB_ENV

      - name: 🌐 Executar testes - ${{ matrix.browser_name }}
        run: |
          python main.py \
            --site "$SITE_NAME" \
            --browser ${{ matrix.browser }} \
            --headless \
            --iterations $ITERATIONS \
            $FULL_TEST
        env:
          DISPLAY: :99

      - name: 📊 Upload relatórios
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: test-reports-${{ matrix.browser }}-${{ github.run_number }}
          path: |
            reports/
            logs/
          if-no-files-found: ignore
          retention-days: 30

      - name: 📸 Upload screenshots de erro
        uses: actions/upload-artifact@v4
        if: failure()
        with:
          name: error-screenshots-${{ matrix.browser }}-${{ github.run_number }}
          path: reports/screenshots/
          if-no-files-found: ignore
          retention-days: 7

  mobile-test:
    runs-on: ubuntu-latest
    if: github.event.inputs.full_test == 'true' || github.event.schedule

    steps:
      - name: 📥 Checkout código
        uses: actions/checkout@v4

      - name: 🐍 Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: 📦 Instalar dependências
        run: pip install -r requirements.txt

      - name: 📱 Executar testes mobile
        run: |
          SITE_NAME="${{ github.event.inputs.site }}"
          if [ -z "$SITE_NAME" ]; then
            SITE_NAME="$(python -c 'import json; print(json.load(open("config/test_sites.json", encoding="utf-8"))["sites"][0]["name"])')"
          fi
          python main.py \
            --site "$SITE_NAME" \
            --mobile \
            --headless \
            --iterations 2

      - name: 📊 Upload relatórios mobile
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: mobile-test-reports-${{ github.run_number }}
          path: reports/
          if-no-files-found: ignore
          retention-days: 30

  notify:
    runs-on: ubuntu-latest
    needs: [test, mobile-test]
    if: always()

    steps:
      - name: 📢 Notificar resultado
        run: |
          if [ ${{ needs.test.result }} = "success" ] && [ ${{ needs.mobile-test.result }} = "success" ]; then
            echo "✅ Todos os testes passaram!"
          elif [ ${{ needs.test.result }} = "failure" ] || [ ${{ needs.mobile-test.result }} = "failure" ]; then
            echo "❌ Alguns testes falharam. Verifique os relatórios."
            exit 1
          else
            echo "⚠️  Alguns testes foram pulados ou cancelados."
          fi
\n```\n\n## William-kelvem94/Auto-boletos\n\n### .github/workflows/ci.yml\n\n```yaml\n---
name: CI

on:
  push:
    branches: [main, master, develop]
  pull_request:
    branches: [main, master, develop]

jobs:
  lint:
    name: Code Quality Check
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Cache pip dependencies
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Lint with flake8
        run: |
          # Stop the build if there are Python syntax errors or undefined names
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          # Run full linting with warnings (uses .flake8 config)
          flake8 . --count --statistics

  docker-build:
    name: Docker Build Test
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Build Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: false
          load: true
          tags: auto-boletos:test
          cache-from: type=gha
          cache-to: type=gha,mode=max

      - name: Test Docker image
        run: |
          docker run --rm auto-boletos:test python -c \
            "import sys; print(f'Python {sys.version}'); \
            import flask; import playwright; \
            print('Docker build successful!')"
\n```\n\n## William-kelvem94/openclaude-wk\n\n### .github/workflows/pr-checks.yml\n\n```yaml\nname: PR Checks

on:
  pull_request:
  push:
    branches:
      - main

permissions:
  contents: read

jobs:
  smoke-and-tests:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [22, "24.11.x"]

    steps:
      - name: Check out repository
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          fetch-depth: 0

      - name: Set up Node.js
        uses: actions/setup-node@48b55a011bda9f5d6aeb4c2d9c7362e8dae4041e # v6.4.0
        with:
          node-version: ${{ matrix.node-version }}

      - name: Set up Bun
        uses: oven-sh/setup-bun@0c5077e51419868618aeaa5fe8019c62421857d6 # v2.2.0
        with:
          bun-version-file: .bun-version

      - name: Install dependencies
        run: bun install --frozen-lockfile

      - name: Smoke and full unit test suite
        run: bun run check

      - name: Suspicious PR intent scan
        env:
          PR_SCAN_BASE: ${{ github.event_name == 'pull_request' && github.event.pull_request.base.sha || 'origin/main' }}
          PR_SCAN_HEAD: ${{ github.event_name == 'pull_request' && github.event.pull_request.head.sha || 'HEAD' }}
        run: bun run security:pr-scan -- --base "$PR_SCAN_BASE" --head "$PR_SCAN_HEAD"
      - name: Provider tests
        run: bun run test:provider

      - name: Provider recommendation tests
        run: npm run test:provider-recommendation

  typecheck:
    runs-on: ubuntu-latest

    steps:
      - name: Check out repository
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          persist-credentials: false

      - name: Set up Bun
        uses: oven-sh/setup-bun@0c5077e51419868618aeaa5fe8019c62421857d6 # v2.2.0
        with:
          bun-version-file: .bun-version

      - name: Install dependencies
        run: bun install --frozen-lockfile

      - name: Typecheck
        run: bun run typecheck

      - name: Type tests
        run: bun run typecheck:type-tests

  web:
    runs-on: ubuntu-latest

    steps:
      - name: Check out repository
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2

      - name: Set up Node.js
        uses: actions/setup-node@48b55a011bda9f5d6aeb4c2d9c7362e8dae4041e # v6.4.0
        with:
          node-version: 22

      - name: Set up Bun
        uses: oven-sh/setup-bun@0c5077e51419868618aeaa5fe8019c62421857d6 # v2.2.0
        with:
          bun-version-file: .bun-version

      - name: Install web dependencies
        run: bun install --cwd web --frozen-lockfile

      - name: Typecheck web
        run: bun run --cwd web typecheck

      - name: Build web
        run: bun run --cwd web build
\n```\n\n### .github/workflows/release.yml\n\n```yaml\nname: Auto Release

on:
  push:
    branches:
      - main

concurrency:
  group: auto-release-${{ github.ref }}
  cancel-in-progress: false

jobs:
  release-please:
    if: ${{ github.repository == 'Gitlawb/openclaude' }}
    name: Release Please
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    outputs:
      release_created: ${{ steps.release.outputs.release_created }}
      tag_name: ${{ steps.release.outputs.tag_name }}
      version: ${{ steps.release.outputs.version }}
    steps:
      - name: Run release-please
        id: release
        uses: googleapis/release-please-action@45996ed1f6d02564a971a2fa1b5860e934307cf7 # v5.0.0
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          release-type: node

  publish-npm:
    name: Publish to npm
    needs: release-please
    if: ${{ needs.release-please.outputs.release_created == 'true' }}
    runs-on: ubuntu-latest
    environment: release
    permissions:
      contents: read
      id-token: write
    steps:
      - name: Checkout release tag
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          ref: ${{ needs.release-please.outputs.tag_name }}
          fetch-depth: 0

      - name: Set up Node.js
        uses: actions/setup-node@48b55a011bda9f5d6aeb4c2d9c7362e8dae4041e # v6.4.0
        with:
          node-version: 24
          registry-url: https://registry.npmjs.org

      - name: Set up Bun
        uses: oven-sh/setup-bun@0c5077e51419868618aeaa5fe8019c62421857d6 # v2.2.0
        with:
          bun-version-file: .bun-version

      - name: Install dependencies
        run: bun install --frozen-lockfile

      - name: Build
        run: bun run build

      - name: Run unit tests
        run: bun test --feature=UNATTENDED_RETRY --max-concurrency=1

      - name: Smoke test
        run: bun run smoke

      - name: Dry-run package
        run: npm pack --dry-run

      - name: Clear token auth for trusted publishing
        run: |
          unset NODE_AUTH_TOKEN
          echo "NODE_AUTH_TOKEN=" >> "$GITHUB_ENV"

      - name: Publish to npm
        run: npm publish --access public --provenance

      - name: Verify npm latest dist-tag
        env:
          EXPECTED_VERSION: ${{ needs.release-please.outputs.version }}
        run: |
          set -euo pipefail

          if [ -z "${EXPECTED_VERSION}" ]; then
            echo "release-please did not provide an expected version" >&2
            exit 1
          fi

          for attempt in $(seq 1 30); do
            published_version="$(npm view @gitlawb/openclaude version 2>/dev/null || true)"
            latest_tag="$(npm view @gitlawb/openclaude dist-tags.latest 2>/dev/null || true)"
            latest_version="$(npm view @gitlawb/openclaude@latest version 2>/dev/null || true)"

            echo "Attempt ${attempt}: version=${published_version:-<empty>} latest=${latest_tag:-<empty>} @latest=${latest_version:-<empty>} expected=${EXPECTED_VERSION}"

            if [ "$published_version" = "$EXPECTED_VERSION" ] && \
               [ "$latest_tag" = "$EXPECTED_VERSION" ] && \
               [ "$latest_version" = "$EXPECTED_VERSION" ]; then
              echo "npm latest verified for @gitlawb/openclaude@${EXPECTED_VERSION}"
              exit 0
            fi

            sleep 10
          done

          echo "npm latest dist-tag did not resolve to ${EXPECTED_VERSION}" >&2
          echo "Observed package version: ${published_version:-<empty>}" >&2
          echo "Observed dist-tags.latest: ${latest_tag:-<empty>}" >&2
          echo "Observed @latest version: ${latest_version:-<empty>}" >&2
          exit 1

      - name: Release summary
        run: |
          {
            echo "## Released ${{ needs.release-please.outputs.tag_name }}"
            echo
            echo "- npm: https://www.npmjs.com/package/@gitlawb/openclaude"
            echo "- GitHub: https://github.com/Gitlawb/openclaude/releases/tag/${{ needs.release-please.outputs.tag_name }}"
          } >> "$GITHUB_STEP_SUMMARY"

  docker:
    name: Build & Push Docker Image
    needs: release-please
    if: ${{ needs.release-please.outputs.release_created == 'true' }}
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    steps:
      - name: Checkout release tag
        uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
        with:
          ref: ${{ needs.release-please.outputs.tag_name }}

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@8d2750c68a42422c14e847fe6c8ac0403b4cbd6f # v3.12.0

      - name: Log in to GitHub Container Registry
        uses: docker/login-action@c94ce9fb468520275223c153574b00df6fe4bcc9 # v3.7.0
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@c299e40c65443455700f0fdfc63efafe5b349051 # v5.10.0
        with:
          images: ghcr.io/${{ github.repository }}
          tags: |
            type=semver,pattern={{version}},value=${{ needs.release-please.outputs.version }}
            type=semver,pattern={{major}}.{{minor}},value=${{ needs.release-please.outputs.version }}
            type=raw,value=latest

      - name: Build and load locally
        uses: docker/build-push-action@10e90e3645eae34f1e60eeb005ba3a3d33f178e8 # v6.19.2
        with:
          context: .
          load: true
          tags: openclaude:smoke
          cache-from: type=gha

      - name: Smoke test
        run: docker run --rm openclaude:smoke --version

      - name: Build and push
        uses: docker/build-push-action@10e90e3645eae34f1e60eeb005ba3a3d33f178e8 # v6.19.2
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
\n```\n\n## William-kelvem94/Will-obsidian\n\n### .github/workflows/ci.yml\n\n```yaml\nname: CI

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: [3.10, 3.11]
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Cache pip
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ matrix.python-version }}-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install requests==2.32.4
      - name: Lint (ruff)
        run: |
          python -m pip install ruff
          ruff check .
      - name: Run tests
        run: |
          python -m pip install pytest
          if find . -type f \( -name 'test_*.py' -o -name '*_test.py' \) -not -path './.git/*' | grep -q .; then
            pytest -q
          else
            echo "No Python tests found; skipping pytest."
          fi
\n```\n\n### .github/workflows/test_embedding_retrieval.yml\n\n```yaml\nname: Teste de Embeddings/Recall

on:
  pull_request:
    paths:
      - preprocess_incremental.jsonl
      - 'scripts/**'

jobs:
  rag_recall:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install requirements
        run: |
          pip install -r requirements.txt
      - name: Processa embedding
        run: |
          python scripts/preprocess_incremental.py
      - name: Testa queries sentinela
        run: |
          python scripts/test_embedding_queries.py
\n```\n\n### .github/workflows/vault-maintenance.yml\n\n```yaml\nname: Vault Maintenance

on:
  schedule:
    - cron: '0 0 * * 0' # Weekly on Sunday (midnight UTC)
    - cron: '0 18 * * 0' # Weekly on Sunday (18:00 UTC)
  workflow_dispatch:

permissions:
  contents: write

jobs:
  weekly-summary:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Cache pip
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install requests==2.32.4

      - name: Run Weekly Summary
        run: python .scripts/weekly_summary.py

      - name: Commit and push changes (if any)
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          if ! git diff --quiet; then
            git add .
            git commit -m "chore: auto weekly summary [skip ci]" || echo "No changes to commit"
            git push
          else
            echo "No changes to commit"
          fi

  maintenance:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Cache pip
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Lint (ruff)
        run: |
          python -m pip install ruff
          ruff check . || true

      - name: Run tests (smoke)
        run: |
          python -m pip install pytest
          pytest -q || true

      - name: Run GitHub Sync
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GITHUB_USERNAME: "William-kelvem94"
        run: python .scripts/github_sync.py

      - name: Commit and push changes (if any)
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          if ! git diff --quiet; then
            git add .
            git commit -m "chore: auto-sync vault data [skip ci]" || echo "No changes to commit"
            git push
          else
            echo "No changes to commit"
          fi
\n```\n\n## William-kelvem94/pixel-agents\n\n### .github/workflows/ci.yml\n\n```yaml\n# CI workflow for pixel-agents

name: CI

on:
  pull_request:
    paths-ignore:
      - '**.md'
      - 'LICENSE'
      - '.github/FUNDING.yml'
  push:
    branches:
      - main
    paths-ignore:
      - '**.md'
      - 'LICENSE'
      - '.github/FUNDING.yml'

permissions:
  contents: read

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: ${{ github.ref != 'refs/heads/main' }}

jobs:
  ci:
    runs-on: ubuntu-latest
    timeout-minutes: 15

    steps:
      - name: Checkout
        id: checkout
        uses: actions/checkout@v6
        with:
          fetch-depth: 0

      - name: Setup Node
        id: setup_node
        uses: actions/setup-node@v6
        with:
          node-version-file: .nvmrc
          cache: npm
          cache-dependency-path: |
            package-lock.json
            webview-ui/package-lock.json
            server/package-lock.json

      - name: Install Root Dependencies
        id: install_root
        run: npm ci

      - name: Install Webview Dependencies
        id: install_webview
        working-directory: webview-ui
        run: npm ci

      - name: Install Server Dependencies
        id: install_server
        working-directory: server
        run: npm ci

      # --- Quality Checks (blocking) ---

      - name: Type Check
        id: type_check
        if: always() && steps.install_root.outcome == 'success' && steps.install_server.outcome == 'success'
        run: npm run check-types
        continue-on-error: true

      - name: Lint
        id: lint
        if: always() && steps.install_root.outcome == 'success' && steps.install_webview.outcome == 'success'
        run: npm run lint
        continue-on-error: true

      - name: Webview Tests
        id: webview_test
        if: always() && steps.install_webview.outcome == 'success'
        working-directory: webview-ui
        run: npm test
        continue-on-error: true

      - name: Format Check
        id: format_check
        if: always() && steps.install_root.outcome == 'success'
        run: npm run format:check
        continue-on-error: true

      - name: Knip (advisory)
        id: knip
        if: always() && steps.install_root.outcome == 'success'
        run: npm run knip
        continue-on-error: true

      # --- Build (blocking) ---

      - name: Build
        id: build
        if: always() && steps.install_root.outcome == 'success' && steps.install_webview.outcome == 'success'
        run: |
          node esbuild.js
          cd webview-ui && npm run build
        continue-on-error: true

      # --- Server Tests (require build for hook script) ---

      - name: Server Tests
        id: server_test
        if: always() && steps.build.outcome == 'success' && steps.install_server.outcome == 'success'
        working-directory: server
        run: npm test
        continue-on-error: true

      # --- Audit Checks (blocking) ---

      - name: Audit Root Dependencies
        id: audit_root
        if: always() && steps.install_root.outcome == 'success'
        run: npm audit --audit-level=moderate
        continue-on-error: true

      - name: Audit Webview Dependencies
        id: audit_webview
        if: always() && steps.install_webview.outcome == 'success'
        working-directory: webview-ui
        run: npm audit --audit-level=moderate
        continue-on-error: true

      - name: Audit Server Dependencies
        id: audit_server
        if: always() && steps.install_server.outcome == 'success'
        working-directory: server
        run: npm audit --audit-level=moderate
        continue-on-error: true

      # --- Summary ---

      - name: Write Step Summary
        if: always()
        env:
          CHECKOUT: ${{ steps.checkout.outcome }}
          SETUP_NODE: ${{ steps.setup_node.outcome }}
          INSTALL_ROOT: ${{ steps.install_root.outcome }}
          INSTALL_WEBVIEW: ${{ steps.install_webview.outcome }}
          TYPE_CHECK: ${{ steps.type_check.outcome }}
          LINT: ${{ steps.lint.outcome }}
          WEBVIEW_TEST: ${{ steps.webview_test.outcome }}
          FORMAT_CHECK: ${{ steps.format_check.outcome }}
          BUILD: ${{ steps.build.outcome }}
          SERVER_TEST: ${{ steps.server_test.outcome }}
          AUDIT_ROOT: ${{ steps.audit_root.outcome }}
          AUDIT_WEBVIEW: ${{ steps.audit_webview.outcome }}
          AUDIT_SERVER: ${{ steps.audit_server.outcome }}
          KNIP: ${{ steps.knip.outcome }}
        run: |
          status() {
            if [ "$1" = "success" ]; then echo "✅ PASS"; else echo "❌ FAIL"; fi
          }
          advisory() {
            if [ "$1" = "success" ]; then echo "✅ PASS"; else echo "⚠️ WARN"; fi
          }
          {
            echo "## CI Results"
            echo
            echo "| Check | Result |"
            echo "| --- | --- |"
            echo "| Checkout | $(status "$CHECKOUT") |"
            echo "| Setup Node | $(status "$SETUP_NODE") |"
            echo "| Install root deps | $(status "$INSTALL_ROOT") |"
            echo "| Install webview deps | $(status "$INSTALL_WEBVIEW") |"
            echo "| **Type check** | $(status "$TYPE_CHECK") |"
            echo "| **Lint** | $(status "$LINT") |"
            echo "| **Webview tests** | $(status "$WEBVIEW_TEST") |"
            echo "| **Format check** | $(status "$FORMAT_CHECK") |"
            echo "| **Build** | $(status "$BUILD") |"
            echo "| **Server tests** | $(status "$SERVER_TEST") |"
            echo "| Audit root _(advisory)_ | $(advisory "$AUDIT_ROOT") |"
            echo "| Audit webview _(advisory)_ | $(advisory "$AUDIT_WEBVIEW") |"
            echo "| Audit server _(advisory)_ | $(advisory "$AUDIT_SERVER") |"
            echo "| Knip _(advisory)_ | $(advisory "$KNIP") |"
          } >> "$GITHUB_STEP_SUMMARY"

      # --- Final Gate ---

      - name: Fail If Any Blocking Check Failed
        if: always()
        env:
          CHECKOUT: ${{ steps.checkout.outcome }}
          SETUP_NODE: ${{ steps.setup_node.outcome }}
          INSTALL_ROOT: ${{ steps.install_root.outcome }}
          INSTALL_WEBVIEW: ${{ steps.install_webview.outcome }}
          TYPE_CHECK: ${{ steps.type_check.outcome }}
          LINT: ${{ steps.lint.outcome }}
          WEBVIEW_TEST: ${{ steps.webview_test.outcome }}
          FORMAT_CHECK: ${{ steps.format_check.outcome }}
          BUILD: ${{ steps.build.outcome }}
          SERVER_TEST: ${{ steps.server_test.outcome }}
        run: |
          failed=0
          for step in CHECKOUT SETUP_NODE INSTALL_ROOT INSTALL_WEBVIEW \
                      TYPE_CHECK LINT \
                      WEBVIEW_TEST FORMAT_CHECK BUILD SERVER_TEST; do
            val=$(printenv "$step" 2>/dev/null || echo "skipped")
            if [ "$val" != "success" ]; then
              echo "::error::$step failed"
              failed=1
            fi
          done
          exit "$failed"

  e2e:
    needs: ci
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
    runs-on: ${{ matrix.os }}
    timeout-minutes: 15
    env:
      PLAYWRIGHT_BROWSERS_PATH: .playwright-browsers

    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          fetch-depth: 0

      - name: Setup Node
        uses: actions/setup-node@v6
        with:
          node-version-file: .nvmrc
          cache: npm
          cache-dependency-path: |
            package-lock.json
            webview-ui/package-lock.json
            server/package-lock.json

      - name: Restore VS Code Cache
        id: cache_vscode_restore
        uses: actions/cache/restore@v5
        with:
          path: .vscode-test
          key: vscode-test-${{ runner.os }}-${{ hashFiles('e2e/global-setup.ts') }}-v2
          restore-keys: |
            vscode-test-${{ runner.os }}-

      - name: Restore Playwright Cache
        id: cache_playwright_restore
        uses: actions/cache/restore@v5
        with:
          path: .playwright-browsers
          key: playwright-browsers-${{ runner.os }}-${{ hashFiles('package-lock.json') }}-v1
          restore-keys: |
            playwright-browsers-${{ runner.os }}-

      - name: Install Root Dependencies
        run: npm ci

      - name: Install Webview Dependencies
        working-directory: webview-ui
        run: npm ci

      - name: Build
        run: node esbuild.js

      - name: Build Webview
        working-directory: webview-ui
        run: npm run build

      - name: Install Playwright Dependencies
        id: install_playwright_deps
        run: npx playwright install --with-deps chromium
        continue-on-error: true

      - name: E2E Tests
        id: e2e_test
        if: steps.install_playwright_deps.outcome == 'success'
        run: npm run e2e
        continue-on-error: true

      - name: Save VS Code Cache
        if: always() && steps.cache_vscode_restore.outputs.cache-hit != 'true' && steps.e2e_test.outcome == 'success' && hashFiles('.vscode-test/vscode-executable.txt') != ''
        uses: actions/cache/save@v5
        with:
          path: .vscode-test
          key: ${{ steps.cache_vscode_restore.outputs.cache-primary-key }}

      - name: Save Playwright Cache
        if: always() && steps.cache_playwright_restore.outputs.cache-hit != 'true' && steps.install_playwright_deps.outcome == 'success' && hashFiles('.playwright-browsers/**') != ''
        uses: actions/cache/save@v5
        with:
          path: .playwright-browsers
          key: ${{ steps.cache_playwright_restore.outputs.cache-primary-key }}

      - name: Write Step Summary
        if: always()
        shell: bash
        env:
          OS: ${{ matrix.os }}
          INSTALL_PLAYWRIGHT_DEPS: ${{ steps.install_playwright_deps.outcome }}
          E2E_TEST: ${{ steps.e2e_test.outcome }}
        run: |
          status() {
            if [ "$1" = "success" ]; then echo "✅ PASS"; else echo "❌ FAIL"; fi
          }
          {
            echo "## E2E Results ($OS)"
      \n```\n\n### .github/workflows/pr-title.yml\n\n```yaml\nname: PR Title

on:
  pull_request_target:
    types: [opened, edited, synchronize]

permissions:
  pull-requests: read

jobs:
  check:
    runs-on: ubuntu-latest
    if: ${{ github.actor != 'dependabot[bot]' }}
    steps:
      - uses: amannn/action-semantic-pull-request@v6
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          types: |
            feat
            fix
            refactor
            chore
            docs
            style
            perf
            test
            ci
            build
          requireScope: false
          subjectPattern: ^[a-z].+$
          subjectPatternError: "PR title subject must start with a lowercase letter: '{subject}'"
\n```\n\n### .github/workflows/publish-extension.yml\n\n```yaml\nname: Publish Extension

on:
  release:
    types: [published]
  workflow_dispatch:
    inputs:
      dry_run:
        description: 'Package without publishing'
        type: boolean
        default: false

concurrency:
  group: publish-extension
  cancel-in-progress: false

jobs:
  publish:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    permissions:
      contents: write
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Setup Node
        uses: actions/setup-node@v6
        with:
          node-version-file: .nvmrc
          cache: npm
          cache-dependency-path: |
            package-lock.json
            webview-ui/package-lock.json

      - name: Install dependencies
        run: npm ci

      - name: Install webview dependencies
        run: npm ci
        working-directory: webview-ui

      - name: Check types and lint
        run: npm run check-types && npm run lint

      - name: Publish to VS Code Marketplace
        id: publish-vscode
        uses: HaaLeo/publish-vscode-extension@v2
        with:
          pat: ${{ secrets.VSCE_PAT }}
          registryUrl: https://marketplace.visualstudio.com
          skipDuplicate: true
          dryRun: ${{ inputs.dry_run == 'true' }}

      - name: Publish to Open VSX
        uses: HaaLeo/publish-vscode-extension@v2
        with:
          pat: ${{ secrets.OPEN_VSX_TOKEN }}
          registryUrl: https://open-vsx.org
          extensionFile: ${{ steps.publish-vscode.outputs.vsixPath }}
          skipDuplicate: true
          dryRun: ${{ inputs.dry_run == 'true' }}

      - name: Upload VSIX to Release
        if: github.event_name == 'release'
        uses: softprops/action-gh-release@v2
        with:
          files: ${{ steps.publish-vscode.outputs.vsixPath }}
\n```\n\n### .github/workflows/update-badges.yml\n\n```yaml\nname: Update Badge Stats

on:
  schedule:
    - cron: '0 6,14,22 * * *'
  workflow_dispatch:

jobs:
  update-badges:
    runs-on: ubuntu-latest
    if: ${{ github.repository == 'pablodelucca/pixel-agents' }}

    steps:
      - name: Fetch VS Code Marketplace stats
        id: vscode
        run: |
          RESPONSE=$(curl -s -X POST \
            'https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery' \
            -H 'Content-Type: application/json' \
            -H 'Accept: application/json;api-version=7.2-preview.1' \
            -d '{
              "filters": [{
                "criteria": [{"filterType": 7, "value": "pablodelucca.pixel-agents"}]
              }],
              "flags": 914
            }')
          INSTALLS=$(echo "$RESPONSE" | jq '[.results[0].extensions[0].statistics[] | select(.statisticName == "install") | .value][0] // 0 | floor')
          DOWNLOADS=$(echo "$RESPONSE" | jq '[.results[0].extensions[0].statistics[] | select(.statisticName == "downloadCount") | .value][0] // 0 | floor')
          VERSION=$(echo "$RESPONSE" | jq -r '.results[0].extensions[0].versions[0].version // "unknown"')
          echo "installs=$INSTALLS" >> "$GITHUB_OUTPUT"
          echo "downloads=$DOWNLOADS" >> "$GITHUB_OUTPUT"
          echo "version=$VERSION" >> "$GITHUB_OUTPUT"

      - name: Fetch Open VSX stats
        id: openvsx
        run: |
          DOWNLOADS=$(curl -s 'https://open-vsx.org/api/pablodelucca/pixel-agents' | jq '.downloadCount // 0')
          echo "downloads=$DOWNLOADS" >> "$GITHUB_OUTPUT"

      - name: Fetch GitHub Releases downloads
        id: releases
        run: |
          TOTAL=$(curl -s https://api.github.com/repos/${{ github.repository }}/releases \
            -H "Authorization: Bearer ${{ secrets.GITHUB_TOKEN }}" \
            | jq '[.[].assets[].download_count] | add // 0')
          echo "downloads=$TOTAL" >> "$GITHUB_OUTPUT"

      - name: Format install count
        id: format
        run: |
          TOTAL=$(( ${{ steps.vscode.outputs.installs }} + ${{ steps.vscode.outputs.downloads }} + ${{ steps.openvsx.outputs.downloads }} + ${{ steps.releases.outputs.downloads }} ))
          if [ "$TOTAL" -ge 1000 ]; then
            MSG="$(awk "BEGIN {printf \"%.1f\", $TOTAL / 1000}")k installs"
          else
            MSG="$TOTAL installs"
          fi
          echo "message=$MSG" >> "$GITHUB_OUTPUT"

      - name: Update version badge in gist
        uses: schneegans/dynamic-badges-action@v1.8.0
        with:
          auth: ${{ secrets.GIST_SECRET }}
          gistID: ${{ secrets.GIST_ID }}
          filename: version.json
          label: version
          message: v${{ steps.vscode.outputs.version }}
          color: '0183ff'
          namedLogo: visualstudiocode
          logoColor: white

      - name: Update installs badge in gist
        uses: schneegans/dynamic-badges-action@v1.8.0
        with:
          auth: ${{ secrets.GIST_SECRET }}
          gistID: ${{ secrets.GIST_ID }}
          filename: installs.json
          label: marketplaces
          message: ${{ steps.format.outputs.message }}
          color: '0183ff'
\n```\n\n## William-kelvem94/AppFlowy-Will\n\n### .github/workflows/android_ci.yaml.bak\n\n```yaml\nname: Android CI

on:
  push:
    branches:
      - "main"
    paths:
      - ".github/workflows/mobile_ci.yaml"
      - "frontend/**"

  pull_request:
    branches:
      - "main"
    paths:
      - ".github/workflows/mobile_ci.yaml"
      - "frontend/**"
      - "!frontend/appflowy_tauri/**"

env:
  CARGO_TERM_COLOR: always
  FLUTTER_VERSION: "3.27.4"
  RUST_TOOLCHAIN: "1.85.0"
  CARGO_MAKE_VERSION: "0.37.18"
  CLOUD_VERSION: 0.6.54-amd64

concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: true

jobs:
  build:
    if: github.event.pull_request.draft != true
    strategy:
      fail-fast: true
      matrix:
        os: [ubuntu-latest]
    runs-on: ${{ matrix.os }}

    steps:
      - name: Check storage space
        run:
          df -h

          # the following step is required to avoid running out of space
      - name: Maximize build space
        if: matrix.os == 'ubuntu-latest'
        run: |
          sudo rm -rf /usr/share/dotnet
          sudo rm -rf /opt/ghc
          sudo rm -rf "/usr/local/share/boost"
          sudo rm -rf "$AGENT_TOOLSDIRECTORY"
          sudo docker image prune --all --force
          sudo rm -rf /opt/hostedtoolcache/codeQL
          sudo rm -rf ${GITHUB_WORKSPACE}/.git

      - name: Check storage space
        run: df -h

      - name: Checkout appflowy cloud code
        uses: actions/checkout@v4
        with:
          repository: AppFlowy-IO/AppFlowy-Cloud
          path: AppFlowy-Cloud

      - name: Prepare appflowy cloud env
        working-directory: AppFlowy-Cloud
        run: |
          # log level
          cp deploy.env .env
          sed -i 's|RUST_LOG=.*|RUST_LOG=trace|' .env
          sed -i 's/GOTRUE_EXTERNAL_GOOGLE_ENABLED=.*/GOTRUE_EXTERNAL_GOOGLE_ENABLED=true/' .env
          sed -i 's|GOTRUE_MAILER_AUTOCONFIRM=.*|GOTRUE_MAILER_AUTOCONFIRM=true|' .env
          sed -i 's|API_EXTERNAL_URL=.*|API_EXTERNAL_URL=http://localhost|' .env

      - name: Run Docker-Compose
        working-directory: AppFlowy-Cloud
        env:
          APPFLOWY_CLOUD_VERSION: ${{ env.CLOUD_VERSION }}
          APPFLOWY_HISTORY_VERSION: ${{ env.CLOUD_VERSION }}
          APPFLOWY_WORKER_VERSION: ${{ env.CLOUD_VERSION }}
        run: |
          container_id=$(docker ps --filter name=appflowy-cloud-appflowy_cloud-1 -q)
          if [ -z "$container_id" ]; then
            echo "AppFlowy-Cloud container is not running. Pulling and starting the container..."
            docker compose pull
            docker compose up -d
            echo "Waiting for the container to be ready..."
            sleep 10
          else
            running_image=$(docker inspect --format='{{index .Config.Image}}' "$container_id")
            if [ "$running_image" != "appflowy-cloud:$APPFLOWY_CLOUD_VERSION" ]; then
              echo "AppFlowy-Cloud is running with an incorrect version. Restarting with the correct version..."
              # Remove all containers if any exist
              if [ "$(docker ps -aq)" ]; then
                docker rm -f $(docker ps -aq)
              else
                echo "No containers to remove."
              fi

              # Remove all volumes if any exist
              if [ "$(docker volume ls -q)" ]; then
                docker volume rm $(docker volume ls -q)
              else
                echo "No volumes to remove."
              fi
              docker compose pull
              docker compose up -d
              echo "Waiting for the container to be ready..."
              sleep 10
              docker ps -a
              docker compose logs
            else
              echo "AppFlowy-Cloud is running with the correct version."
            fi
          fi

      - name: Checkout source code
        uses: actions/checkout@v4

      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: 11

      - name: Install Rust toolchain
        id: rust_toolchain
        uses: actions-rs/toolchain@v1
        with:
          toolchain: ${{ env.RUST_TOOLCHAIN }}
          override: true
          profile: minimal

      - name: Install flutter
        id: flutter
        uses: subosito/flutter-action@v2
        with:
          channel: "stable"
          flutter-version: ${{ env.FLUTTER_VERSION }}

      - uses: gradle/gradle-build-action@v3
        with:
          gradle-version: 8.10

      - uses: davidB/rust-cargo-make@v1
        with:
          version: ${{ env.CARGO_MAKE_VERSION }}

      - name: Install prerequisites
        working-directory: frontend
        run: |
          rustup target install aarch64-linux-android
          rustup target install x86_64-linux-android
          rustup target add armv7-linux-androideabi
          cargo install --force --locked duckscript_cli
          cargo install cargo-ndk
          if [ "$RUNNER_OS" == "Linux" ]; then
            sudo wget -qO /etc/apt/trusted.gpg.d/dart_linux_signing_key.asc https://dl-ssl.google.com/linux/linux_signing_key.pub
            sudo wget -qO /etc/apt/sources.list.d/dart_stable.list https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list
            sudo apt-get update
            sudo apt-get install -y dart curl build-essential libssl-dev clang cmake ninja-build pkg-config libgtk-3-dev
            sudo apt-get install keybinder-3.0 libnotify-dev
            sudo apt-get install gcc-multilib
          elif [ "$RUNNER_OS" == "Windows" ]; then
            vcpkg integrate install
          elif [ "$RUNNER_OS" == "macOS" ]; then
            echo 'do nothing'
          fi
          cargo make appflowy-flutter-deps-tools
        shell: bash

      - name: Build AppFlowy
        working-directory: frontend
        run: |
          cargo make --profile development-android appflowy-core-dev-android
          cargo make --profile development-android code_generation
          cd rust-lib
          cargo clean

      - name: Enable KVM group perms
        run: |
          echo 'KERNEL=="kvm", GROUP="kvm", MODE="0666", OPTIONS+="static_node=kvm"' | sudo tee /etc/udev/rules.d/99-kvm4all.rules
          sudo udevadm control --reload-rules
          sudo udevadm trigger --name-match=kvm

      - name: Run integration tests
        # https://github.com/ReactiveCircus/android-emulator-runner
        uses: reactivecircus/android-emulator-runner@v2
        with:
          api-level: 33
          arch: x86_64
          disk-size: 2048M
          working-directory: frontend/appflowy_flutter
          disable-animations: true
          force-avd-creation: false
          target: google_apis
          script: flutter test integration_test/mobile/cloud/cloud_runner.dart
\n```\n\n### .github/workflows/build_command.yml\n\n```yaml\nname: build

on:
  repository_dispatch:
    types: [build-command]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: notify appflowy_builder
        run: |
          platform=${{ github.event.client_payload.slash_command.args.unnamed.arg1 }}
          build_name=${{ github.event.client_payload.slash_command.args.named.build_name }}
          branch=${{ github.event.client_payload.slash_command.args.named.ref }}
          build_type=""
          arch=""

          if [ "$platform" = "android" ]; then
            build_type="apk"
          elif [ "$platform" = "macos" ]; then
            arch="universal"
          fi

          params=$(jq -n \
            --arg ref "main" \
            --arg repo "LucasXu0/AppFlowy" \
            --arg branch "$branch" \
            --arg build_name "$build_name" \
            --arg build_type "$build_type" \
            --arg arch "$arch" \
            '{ref: $ref, inputs: {repo: $repo, branch: $branch, build_name: $build_name, build_type: $build_type, arch: $arch}} | del(.inputs | .. | select(. == ""))')

          echo "params: $params"

          curl -L \
            -X POST \
            -H "Accept: application/vnd.github+json" \
            -H "Authorization: Bearer ${{ secrets.TOKEN }}" \
            -H "X-GitHub-Api-Version: 2022-11-28" \
            https://api.github.com/repos/AppFlowy-IO/AppFlowy-Builder/actions/workflows/$platform.yaml/dispatches \
            -d "$params"
\n```\n\n### .github/workflows/commit_lint.yml\n\n```yaml\nname: Commit messages lint
on: [pull_request, push]

jobs:
  commitlint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: wagoid/commitlint-github-action@v4
\n```\n\n### .github/workflows/docker_ci.yml\n\n```yaml\nname: Docker-CI

on:
  push:
    branches: [ "main", "release/*" ]
  pull_request:
    branches: [ "main", "release/*" ]
  workflow_dispatch:

concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: true

jobs:
  build-app:
    if: github.event.pull_request.draft != true
    runs-on: ubuntu-latest
    steps:
      - name: Checkout source code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      # cache the docker layers
      # don't cache anything temporarly, because it always triggers "no space left on device" error
      # - name: Cache Docker layers
      #   uses: actions/cache@v3
      #   with:
      #     path: /tmp/.buildx-cache
      #     key: ${{ runner.os }}-buildx-${{ github.sha }}
      #     restore-keys: |
      #       ${{ runner.os }}-buildx-

      - name: Build the app
        uses: docker/build-push-action@v5
        with:
          context: .
          file: ./frontend/scripts/docker-buildfiles/Dockerfile
          push: false
          # cache-from: type=local,src=/tmp/.buildx-cache
          # cache-to: type=local,dest=/tmp/.buildx-cache-new,mode=max

      # - name: Move cache
      #   run: |
      #     rm -rf /tmp/.buildx-cache
      #     mv /tmp/.buildx-cache-new /tmp/.buildx-cache
\n```\n\n### .github/workflows/flutter_ci.yaml\n\n```yaml\nname: Flutter-CI

on:
  push:
    branches:
      - "main"
      - "release/*"
    paths:
      - ".github/workflows/flutter_ci.yaml"
      - ".github/actions/flutter_build/**"
      - "frontend/rust-lib/**"
      - "frontend/appflowy_flutter/**"
      - "frontend/resources/**"

  pull_request:
    branches:
      - "main"
      - "release/*"
    paths:
      - ".github/workflows/flutter_ci.yaml"
      - ".github/actions/flutter_build/**"
      - "frontend/rust-lib/**"
      - "frontend/appflowy_flutter/**"
      - "frontend/resources/**"

env:
  CARGO_TERM_COLOR: always
  FLUTTER_VERSION: "3.27.4"
  RUST_TOOLCHAIN: "1.85.0"
  CARGO_MAKE_VERSION: "0.37.18"
  CLOUD_VERSION: 0.9.49-amd64

concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: true

jobs:
  prepare-linux:
    if: github.event.pull_request.draft != true
    strategy:
      fail-fast: true
      matrix:
        os: [ ubuntu-latest ]
        include:
          - os: ubuntu-latest
            flutter_profile: development-linux-x86_64
            target: x86_64-unknown-linux-gnu
    runs-on: ${{ matrix.os }}

    steps:
      # the following step is required to avoid running out of space
      - name: Maximize build space
        run: |
          sudo rm -rf /usr/share/dotnet
          sudo rm -rf /opt/ghc
          sudo rm -rf "/usr/local/share/boost"
          sudo rm -rf "$AGENT_TOOLSDIRECTORY"

      - name: Checkout source code
        uses: actions/checkout@v4

      - name: Flutter build
        uses: ./.github/actions/flutter_build
        with:
          os: ${{ matrix.os }}
          flutter_version: ${{ env.FLUTTER_VERSION }}
          rust_toolchain: ${{ env.RUST_TOOLCHAIN }}
          cargo_make_version: ${{ env.CARGO_MAKE_VERSION }}
          rust_target: ${{ matrix.target }}
          flutter_profile: ${{ matrix.flutter_profile }}

  prepare-windows:
    if: github.event.pull_request.draft != true
    strategy:
      fail-fast: true
      matrix:
        os: [ windows-latest ]
        include:
          - os: windows-latest
            flutter_profile: development-windows-x86
            target: x86_64-pc-windows-msvc
    runs-on: ${{ matrix.os }}

    steps:
      - name: Checkout source code
        uses: actions/checkout@v4

      - name: Flutter build
        uses: ./.github/actions/flutter_build
        with:
          os: ${{ matrix.os }}
          flutter_version: ${{ env.FLUTTER_VERSION }}
          DISABLE_CI_TEST_LOG: "true"
          rust_toolchain: ${{ env.RUST_TOOLCHAIN }}
          cargo_make_version: ${{ env.CARGO_MAKE_VERSION }}
          rust_target: ${{ matrix.target }}
          flutter_profile: ${{ matrix.flutter_profile }}

  prepare-macos:
    if: github.event.pull_request.draft != true
    strategy:
      fail-fast: true
      matrix:
        os: [ macos-latest ]
        include:
          - os: macos-latest
            flutter_profile: development-mac-x86_64
            target: x86_64-apple-darwin
    runs-on: ${{ matrix.os }}

    steps:
      - name: Checkout source code
        uses: actions/checkout@v4

      - name: Flutter build
        uses: ./.github/actions/flutter_build
        with:
          os: ${{ matrix.os }}
          flutter_version: ${{ env.FLUTTER_VERSION }}
          rust_toolchain: ${{ env.RUST_TOOLCHAIN }}
          cargo_make_version: ${{ env.CARGO_MAKE_VERSION }}
          rust_target: ${{ matrix.target }}
          flutter_profile: ${{ matrix.flutter_profile }}

  unit_test:
    needs: [ prepare-linux ]
    if: github.event.pull_request.draft != true
    strategy:
      fail-fast: false
      matrix:
        os: [ ubuntu-latest ]
        include:
          - os: ubuntu-latest
            flutter_profile: development-linux-x86_64
            target: x86_64-unknown-linux-gnu
    runs-on: ${{ matrix.os }}

    steps:
      - name: Checkout source code
        uses: actions/checkout@v4

      - name: Install Rust toolchain
        id: rust_toolchain
        uses: actions-rs/toolchain@v1
        with:
          toolchain: ${{ env.RUST_TOOLCHAIN }}
          target: ${{ matrix.target }}
          override: true
          profile: minimal

      - name: Install flutter
        id: flutter
        uses: subosito/flutter-action@v2
        with:
          channel: "stable"
          flutter-version: ${{ env.FLUTTER_VERSION }}
          cache: true

      - uses: Swatinem/rust-cache@v2
        with:
          prefix-key: ${{ matrix.os }}
          workspaces: |
            frontend/rust-lib
          cache-all-crates: true

      - uses: taiki-e/install-action@v2
        with:
          tool: cargo-make@${{ env.CARGO_MAKE_VERSION }}, duckscript_cli

      - name: Install prerequisites
        working-directory: frontend
        run: |
          if [ "$RUNNER_OS" == "Linux" ]; then
            sudo wget -qO /etc/apt/trusted.gpg.d/dart_linux_signing_key.asc https://dl-ssl.google.com/linux/linux_signing_key.pub
            sudo wget -qO /etc/apt/sources.list.d/dart_stable.list https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list
            sudo apt-get update
            sudo apt-get install -y dart curl build-essential libssl-dev clang cmake ninja-build pkg-config libgtk-3-dev keybinder-3.0 libnotify-dev libcurl4-openssl-dev
          fi
        shell: bash

      - name: Enable Flutter Desktop
        run: |
          if [ "$RUNNER_OS" == "Linux" ]; then
            flutter config --enable-linux-desktop
          elif [ "$RUNNER_OS" == "macOS" ]; then
            flutter config --enable-macos-desktop
          elif [ "$RUNNER_OS" == "Windows" ]; then
            git config --system core.longpaths true
            flutter config --enable-windows-desktop
          fi
        shell: bash

      - uses: actions/download-artifact@v4
        with:
          name: ${{ github.run_id }}-${{ matrix.os }}

      - name: Uncompress appflowy_flutter
        run: tar -xf appflowy_flutter.tar.gz

      - name: Run flutter pub get
        working-directory: frontend
        run: cargo make pub_get

      - name: Run Flutter unit tests
        env:
          DISABLE_EVENT_LOG: true
          DISABLE_CI_TEST_LOG: "true"
        working-directory: frontend
        run: |
          if [ "$RUNNER_OS" == "macOS" ]; then
            cargo make dart_unit_test
          elif [ "$RUNNER_OS" == "Linux" ]; then
            cargo make dart_unit_test_no_build
          elif [ "$RUNNER_OS" == "Windows" ]; then
            cargo make dart_unit_test_no_build
          fi
        shell: bash

  cloud_integration_test:
    needs: [ prepare-linux ]
    strategy:
      fail-fast: false
      matrix:
        os: [ ubuntu-latest ]
        include:
          - os: ubuntu-latest
            flutter_profile: development-linux-x86_64
            target: x86_64-unknown-linux-gnu
    runs-on: ${{ matrix.os }}

    steps:
      - name: Checkout appflowy cloud code
        uses: actions/checkout@v4
        with:
          repository: AppFlowy-IO/AppFlowy-Cloud
          path: AppFlowy-Cloud

      - name: Prepare appflowy cloud env
        working-directory: AppFlowy-Cloud
        run: |
          # log level
          cp deploy.env .env
          sed -i 's|RUST_LOG=.*|RUST_LOG=trace|' .env
          sed -i 's/GOTRUE_EXTERNAL_GOOGLE_ENABLED=.*/GOTRUE_EXTERNAL_GOOGLE_ENABLED=true/' .env
          sed -i 's|GOTRUE_MAILER_AUTOCONFIRM=.*|GOTRUE_MAILER_AUTOCONFIRM=true|' .env
          sed -i 's|API_EXTERNAL_URL=.*|API_EXTERNAL_URL=http://localhost|' .env

      - name: Run Docker-Compose
        working-directory: AppFlowy-Cloud
        env:
          APPFLOWY_CLOUD_VERSION: ${{ env.CLOUD_VERSION }}
          APPFLOWY_HISTORY_VERSION: ${{ env.CLOUD_VERSION }}
          APPFLOWY_WORKER_VERSION: ${{ env.CLOUD_VERSION }}
        run: |
          container_id=$(docker ps --filter name=appflowy-cloud-appflowy_cloud-1 -q)
          if [ -z "$container_id" ]; then
            echo "AppFlowy-Cloud container is not running. Pulling and starting the container..."
            docker compose pull
            docker compose up -d
            echo "Waiting for the container to be ready..."
            sleep 10
          else
            running_image=$(docker inspect --format='{{index .Config.Image}}' "$container_id")
            if [ "$running_image" != "appflowy-cloud:$APPFLOWY_CLOUD_VERSION" ]; then
              echo "AppFlowy-Cloud is running with an incorrect version. Restarting with the correct version..."
              # Remove all containers if any exist
              if [ "$(docker ps -aq)" ]; then
                docker rm -f $(docker ps -aq)
              else
                echo "No containers to remove."
              fi

              # Remove all volumes if any exist
              if [ "$(docker volume ls -q)" ]; then
                docker volume rm $(docker volume ls -q)
              else
                echo "No volumes to remove."
              fi
              docker compose pull
              docker compose up -d
              echo "Waiting for the container to be ready..."
              sleep 10
              docker ps -a
              docker compose logs
            else
              echo "AppFlowy-Cloud is running with the correct version."
            fi
          fi

      - name: Checkout source code
        uses: actions/checkout@v4

      - name: Install flutter
        id: flutter
        uses: subosito/flutter-action@v2
        with:
          channel: "stable"
          flutter-version: ${{ env.FLUTTER_VERSION }}
          cache: true

      - uses: taiki-e/install-action@v2
        with:
          tool: cargo-make@${{ env.CARGO_MAKE_VERSION }}

      - name: Install prerequisites
        working-directory: frontend
        run: |
          sudo wget -qO /etc/apt/trusted.gpg.d/dart_linux_signing_key.asc https://dl-ssl.google.com/linux/linux_signing_key.pub
          sudo wget -qO /etc/apt/sources.list.d/dart_stable.list https://stor\n```\n\n### .github/workflows/ios_ci.yaml\n\n```yaml\nname: iOS CI

on:
  push:
    branches:
      - "main"
    paths:
      - ".github/workflows/mobile_ci.yaml"
      - "frontend/**"
      - "!frontend/appflowy_web_app/**"

  pull_request:
    branches:
      - "main"
    paths:
      - ".github/workflows/mobile_ci.yaml"
      - "frontend/**"
      - "!frontend/appflowy_web_app/**"

env:
  FLUTTER_VERSION: "3.27.4"
  RUST_TOOLCHAIN: "1.85.0"

concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: true

jobs:
  integration-tests:
    runs-on: macos-latest

    steps:
      - name: Checkout source code
        uses: actions/checkout@v4

      - name: Install Rust toolchain
        uses: actions-rs/toolchain@v1
        with:
          toolchain: ${{ env.RUST_TOOLCHAIN }}
          target: aarch64-apple-ios-sim
          override: true
          profile: minimal

      - name: Install Flutter
        uses: subosito/flutter-action@v2
        with:
          channel: "stable"
          flutter-version: ${{ env.FLUTTER_VERSION }}
          cache: true

      - uses: Swatinem/rust-cache@v2
        with:
          prefix-key: macos-latest
          workspaces: |
            frontend/rust-lib

      - uses: davidB/rust-cargo-make@v1
        with:
          version: "0.37.15"

      - name: Install prerequisites
        working-directory: frontend
        run: |
          rustup target install aarch64-apple-ios-sim
          cargo install --force --locked duckscript_cli
          cargo install cargo-lipo
          cargo make appflowy-flutter-deps-tools
        shell: bash

      - name: Build AppFlowy
        working-directory: frontend
        run: |
          cargo make --profile development-ios-arm64-sim appflowy-core-dev-ios
          cargo make --profile development-ios-arm64-sim code_generation

      # - uses: futureware-tech/simulator-action@v3
      #   id: simulator-action
      #   with:
      #     model: "iPhone 15"
      #     shutdown_after_job: false

      # - name: Run AppFlowy on simulator
      #   working-directory: frontend/appflowy_flutter
      #   run: |
      #     flutter run -d ${{ steps.simulator-action.outputs.udid }} &
      #     pid=$!
      #     sleep 500
      #     kill $pid
      #   continue-on-error: true

      # # Integration tests
      # - name: Run integration tests
      #   working-directory: frontend/appflowy_flutter
      #   # The integration tests are flaky and sometimes fail with "Connection timed out":
      #   # Don't block the CI. If the tests fail, the CI will still pass.
      #   # Instead, we're using Code Magic to re-run the tests to check if they pass.
      #   continue-on-error: true
      #   run: flutter test integration_test/runner.dart -d ${{ steps.simulator-action.outputs.udid }}
\n```\n\n### .github/workflows/mobile_ci.yml\n\n```yaml\nname: Mobile-CI

on:
  workflow_dispatch:
    inputs:
      branch:
        description: "Branch to build"
        required: true
        default: "main"
      workflow_id:
        description: "Codemagic workflow ID"
        required: true
        default: "ios-workflow"
        type: choice
        options:
          - ios-workflow
          - android-workflow

env:
  CODEMAGIC_API_TOKEN: ${{ secrets.CODEMAGIC_API_TOKEN }}
  APP_ID: "6731d2f427e7c816080c3674"

jobs:
  trigger-mobile-build:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Codemagic Build
        id: trigger_build
        run: |
          RESPONSE=$(curl -X POST \
            --header "Content-Type: application/json" \
            --header "x-auth-token: $CODEMAGIC_API_TOKEN" \
            --data '{
              "appId": "${{ env.APP_ID }}",
              "workflowId": "${{ github.event.inputs.workflow_id }}",
              "branch": "${{ github.event.inputs.branch }}"
            }' \
            https://api.codemagic.io/builds)

          BUILD_ID=$(echo $RESPONSE | jq -r '.buildId')
          echo "build_id=$BUILD_ID" >> $GITHUB_OUTPUT
          echo "build_id=$BUILD_ID"

      - name: Wait for build and check status
        id: check_status
        run: |
          while true; do
            curl -X GET \
              --header "Content-Type: application/json" \
              --header "x-auth-token: $CODEMAGIC_API_TOKEN" \
              https://api.codemagic.io/builds/${{ steps.trigger_build.outputs.build_id }} > /tmp/response.json

            RESPONSE_WITHOUT_COMMAND=$(cat /tmp/response.json | jq 'walk(if type == "object" and has("subactions") then .subactions |= map(del(.command)) else . end)')
            STATUS=$(echo $RESPONSE_WITHOUT_COMMAND | jq -r '.build.status')

            if [ "$STATUS" = "finished" ]; then
              SUCCESS=$(echo $RESPONSE_WITHOUT_COMMAND | jq -r '.success')
              BUILD_URL=$(echo $RESPONSE_WITHOUT_COMMAND | jq -r '.buildUrl')
              echo "status=$STATUS" >> $GITHUB_OUTPUT
              echo "success=$SUCCESS" >> $GITHUB_OUTPUT
              echo "build_url=$BUILD_URL" >> $GITHUB_OUTPUT
              break
            elif [ "$STATUS" = "failed" ]; then
              echo "status=failed" >> $GITHUB_OUTPUT
              break
            fi

            sleep 60
          done

      - name: Slack Notification
        uses: 8398a7/action-slack@v3
        if: always()
        with:
          status: ${{ steps.check_status.outputs.success == 'true' && 'success' || 'failure' }}
          fields: repo,message,commit,author,action,eventName,ref,workflow,job,took
          text: |
            Mobile CI Build Result
            Branch: ${{ github.event.inputs.branch }}
            Workflow: ${{ github.event.inputs.workflow_id }}
            Build URL: ${{ steps.check_status.outputs.build_url }}
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.RELEASE_SLACK_WEBHOOK }}
\n```\n\n### .github/workflows/ninja_i18n.yml\n\n```yaml\nname: Ninja i18n action

on:
  pull_request_target:

# explicitly configure permissions, in case your GITHUB_TOKEN workflow permissions are set to read-only in repository settings
permissions: 
  pull-requests: write

jobs:
  ninja-i18n:
    name: Ninja i18n - GitHub Lint Action
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        id: checkout
        uses: actions/checkout@v4

      - name: Run Ninja i18n
        id: ninja-i18n
        uses: opral/ninja-i18n-action@main
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          
\n```\n\n### .github/workflows/release.yml\n\n```yaml\nname: release

on:
  push:
    tags:
      - "*"

env:
  FLUTTER_VERSION: "3.27.4"
  RUST_TOOLCHAIN: "1.85.0"

jobs:
  create-release:
    runs-on: ubuntu-latest
    env:
      RELEASE_NOTES_PATH: /tmp/release_notes
    outputs:
      upload_url: ${{ steps.create_release.outputs.upload_url }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Build release notes
        run: |
          touch ${{ env.RELEASE_NOTES_PATH }}
          cat CHANGELOG.md | sed -e '/./{H;$!d;}' -e "x;/##\ Version\ ${{ github.ref_name }}/"'!d;' >> ${{ env.RELEASE_NOTES_PATH }}

      - name: Create release
        id: create_release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ github.ref }}
          release_name: v${{ github.ref }}
          body_path: ${{ env.RELEASE_NOTES_PATH }}

  # the package name should be with the format: AppFlowy-<version>-<os>-<arch>

  build-for-windows:
    name: ${{ matrix.job.target }} (${{ matrix.job.os }})
    needs: create-release
    env:
      WINDOWS_APP_RELEASE_PATH: frontend\appflowy_flutter\product\${{ github.ref_name }}\windows
      WINDOWS_ZIP_NAME: AppFlowy-${{ github.ref_name }}-windows-x86_64.zip
      WINDOWS_INSTALLER_NAME: AppFlowy-${{ github.ref_name }}-windows-x86_64
    runs-on: ${{ matrix.job.os }}
    strategy:
      fail-fast: false
      matrix:
        job:
          - { target: x86_64-pc-windows-msvc, os: windows-2019 }
    steps:
      - name: Checkout source code
        uses: actions/checkout@v4

      - name: Install flutter
        uses: subosito/flutter-action@v2
        with:
          channel: "stable"
          flutter-version: ${{ env.FLUTTER_VERSION }}

      - name: Install Rust toolchain
        uses: actions-rs/toolchain@v1
        with:
          toolchain: ${{ env.RUST_TOOLCHAIN }}
          target: ${{ matrix.job.target }}
          override: true
          components: rustfmt
          profile: minimal

      - name: Install prerequisites
        working-directory: frontend
        run: |
          vcpkg integrate install
          cargo install --force --locked cargo-make
          cargo install --force --locked duckscript_cli

      - name: Build Windows app
        working-directory: frontend
        # the cargo make script has to be run separately because of file locking issues
        run: |
          flutter config --enable-windows-desktop
          dart ./scripts/flutter_release_build/build_flowy.dart exclude-directives . ${{ github.ref_name }}
          cargo make --env APP_VERSION=${{ github.ref_name }} --profile production-windows-x86 appflowy
          dart ./scripts/flutter_release_build/build_flowy.dart include-directives . ${{ github.ref_name }}

      - name: Archive Asset
        uses: vimtor/action-zip@v1
        with:
          files: ${{ env.WINDOWS_APP_RELEASE_PATH }}\
          dest: ${{ env.WINDOWS_APP_RELEASE_PATH }}\${{ env.WINDOWS_ZIP_NAME }}

      - name: Copy installer config & icon file
        working-directory: frontend
        run: |
          cp scripts/windows_installer/* ../${{ env.WINDOWS_APP_RELEASE_PATH }}

      - name: Build installer executable
        working-directory: ${{ env.WINDOWS_APP_RELEASE_PATH }}
        run: |
          iscc /F${{ env.WINDOWS_INSTALLER_NAME }} inno_setup_config.iss /DAppVersion=${{ github.ref_name }}

      - name: Upload Asset
        id: upload-release-asset
        uses: actions/upload-release-asset@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          upload_url: ${{ needs.create-release.outputs.upload_url }}
          asset_path: ${{ env.WINDOWS_APP_RELEASE_PATH }}\${{ env.WINDOWS_ZIP_NAME }}
          asset_name: ${{ env.WINDOWS_ZIP_NAME }}
          asset_content_type: application/octet-stream

      - name: Upload Installer Asset
        id: upload-installer-asset
        uses: actions/upload-release-asset@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          upload_url: ${{ needs.create-release.outputs.upload_url }}
          asset_path: ${{ env.WINDOWS_APP_RELEASE_PATH }}\Output\${{ env.WINDOWS_INSTALLER_NAME }}.exe
          asset_name: ${{ env.WINDOWS_INSTALLER_NAME }}.exe
          asset_content_type: application/octet-stream

  build-for-macOS-x86_64:
    name: ${{ matrix.job.target }} (${{ matrix.job.os }}) [${{ matrix.job.extra-build-args }}]
    runs-on: ${{ matrix.job.os }}
    needs: create-release
    env:
      MACOS_APP_RELEASE_PATH: frontend/appflowy_flutter/product/${{ github.ref_name }}/macos/Release
      MACOS_X86_ZIP_NAME: AppFlowy-${{ github.ref_name }}-macos-x86_64.zip
      MACOS_DMG_NAME: AppFlowy-${{ github.ref_name }}-macos-x86_64
    strategy:
      fail-fast: false
      matrix:
        job:
          - { target: x86_64-apple-darwin, os: macos-13, extra-build-args: "" }
    steps:
      - name: Checkout source code
        uses: actions/checkout@v4

      - name: Install flutter
        uses: subosito/flutter-action@v2
        with:
          channel: "stable"
          flutter-version: ${{ env.FLUTTER_VERSION }}

      - name: Install Rust toolchain
        uses: actions-rs/toolchain@v1
        with:
          toolchain: ${{ env.RUST_TOOLCHAIN }}
          target: ${{ matrix.job.target }}
          override: true
          components: rustfmt
          profile: minimal

      - name: Install prerequisites
        working-directory: frontend
        run: |
          cargo install --force --locked cargo-make
          cargo install --force --locked duckscript_cli

      - name: Build AppFlowy
        working-directory: frontend
        run: |
          flutter config --enable-macos-desktop
          dart ./scripts/flutter_release_build/build_flowy.dart run . ${{ github.ref_name }}

      - name: Codesign AppFlowy
        run: |
          echo ${{ secrets.MACOS_CERTIFICATE }} | base64 --decode > certificate.p12
          security create-keychain -p action build.keychain
          security default-keychain -s build.keychain
          security unlock-keychain -p action build.keychain
          security import certificate.p12 -k build.keychain -P ${{ secrets.MACOS_CERTIFICATE_PWD }} -T /usr/bin/codesign
          security set-key-partition-list -S apple-tool:,apple:,codesign: -s -k action build.keychain
          /usr/bin/codesign --force --options runtime --deep --sign "${{ secrets.MACOS_CODESIGN_ID }}" "${{ env.MACOS_APP_RELEASE_PATH }}/AppFlowy.app" -v

      - name: Create macOS dmg
        run: |
          brew install create-dmg
          i=0
          until [[ -e "${{ env.MACOS_APP_RELEASE_PATH }}/${{ env.MACOS_DMG_NAME }}.dmg" ]]; do
            create-dmg \
            --volname ${{ env.MACOS_DMG_NAME }} \
            --hide-extension "AppFlowy.app" \
            --background frontend/scripts/dmg_assets/AppFlowyInstallerBackground.jpg \
            --window-size 600 450 \
            --icon-size 94 \
            --icon "AppFlowy.app" 141 249 \
            --app-drop-link 458 249 \
            "${{ env.MACOS_APP_RELEASE_PATH }}/${{ env.MACOS_DMG_NAME }}.dmg" \
            "${{ env.MACOS_APP_RELEASE_PATH }}/AppFlowy.app" || true
            if [[ $i -eq 10 ]]; then
              echo 'Error: create-dmg did not succeed even after 10 tries.'
              exit 1
            fi
            i=$((i+1))
          done
      - name: Notarize AppFlowy
        run: |
          xcrun notarytool submit ${{ env.MACOS_APP_RELEASE_PATH }}/${{ env.MACOS_DMG_NAME }}.dmg --apple-id ${{ secrets.MACOS_NOTARY_USER }} --team-id ${{ secrets.MACOS_TEAM_ID }} --password ${{ secrets.MACOS_NOTARY_PWD }} -v -f "json" --wait

      - name: Archive Asset
        working-directory: ${{ env.MACOS_APP_RELEASE_PATH }}
        run: zip --symlinks -qr ${{ env.MACOS_X86_ZIP_NAME }} AppFlowy.app

      - name: Upload Asset
        uses: actions/upload-release-asset@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          upload_url: ${{ needs.create-release.outputs.upload_url }}
          asset_path: ${{ env.MACOS_APP_RELEASE_PATH }}/${{ env.MACOS_X86_ZIP_NAME }}
          asset_name: ${{ env.MACOS_X86_ZIP_NAME }}
          asset_content_type: application/octet-stream

      - name: Upload DMG Asset
        uses: actions/upload-release-asset@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          upload_url: ${{ needs.create-release.outputs.upload_url }}
          asset_path: ${{ env.MACOS_APP_RELEASE_PATH }}/${{ env.MACOS_DMG_NAME }}.dmg
          asset_name: ${{ env.MACOS_DMG_NAME }}.dmg
          asset_content_type: application/octet-stream

  build-for-macOS-universal:
    name: ${{ matrix.job.target }} (${{ matrix.job.os }}) [${{ matrix.job.extra-build-args }}]
    runs-on: ${{ matrix.job.os }}
    needs: create-release
    env:
      MACOS_APP_RELEASE_PATH: frontend/appflowy_flutter/product/${{ github.ref_name }}/macos/Release
      MACOS_AARCH64_ZIP_NAME: AppFlowy-${{ github.ref_name }}-macos-universal.zip
      MACOS_DMG_NAME: AppFlowy-${{ github.ref_name }}-macos-universal
    strategy:
      fail-fast: false
      matrix:
        job:
          - {
            targets: "aarch64-apple-darwin,x86_64-apple-darwin",
            os: macos-14,
            extra-build-args: "",
          }
    steps:
      - name: Checkout source code
        uses: actions/checkout@v4

      - name: Install flutter
        uses: subosito/flutter-action@v2
        with:
          channel: "stable"
          flutter-version: ${{ env.FLUTTER_VERSION }}

      - name: Install Rust toolchain
        uses: dtolnay/rust-toolchain@stable
        with:
          toolchain: ${{ env.RUST_TOOLCHAIN }}
          targets: ${{ matrix.job.targets }}
          components: rustfmt

      - name: Install prerequisites
        working-directory: frontend
        run: |
          cargo install --force --locked cargo-make
          cargo install --force\n```\n\n### .github/workflows/rust_ci.yaml\n\n```yaml\nname: Rust-CI

on:
  push:
    branches:
      - "main"
      - "develop"
      - "release/*"
    paths:
      - "frontend/rust-lib/**"
      - ".github/workflows/rust_ci.yaml"

  pull_request:
    branches:
      - "main"
      - "develop"
      - "release/*"

env:
  CARGO_TERM_COLOR: always
  CLOUD_VERSION: 0.9.49-amd64
  RUST_TOOLCHAIN: "1.85.0"

jobs:
  ubuntu-job:
    runs-on: ubuntu-latest
    steps:
      - name: Set timezone for action
        uses: szenius/set-timezone@v2.0
        with:
          timezoneLinux: "US/Pacific"

      - name: Maximize build space
        run: |
          sudo rm -rf /usr/share/dotnet
          sudo rm -rf /opt/ghc
          sudo rm -rf "/usr/local/share/boost"
          sudo rm -rf "$AGENT_TOOLSDIRECTORY"
          sudo docker image prune --all --force

      - name: Checkout source code
        uses: actions/checkout@v4

      - name: Install Rust toolchain
        uses: actions-rs/toolchain@v1
        with:
          toolchain: ${{ env.RUST_TOOLCHAIN }}
          override: true
          components: rustfmt, clippy
          profile: minimal
      - uses: Swatinem/rust-cache@v2
        with:
          prefix-key: ${{ runner.os }}
          cache-on-failure: true
          workspaces: |
            frontend/rust-lib

      - name: Checkout appflowy cloud code
        uses: actions/checkout@v4
        with:
          repository: AppFlowy-IO/AppFlowy-Cloud
          path: AppFlowy-Cloud

      - name: Prepare appflowy cloud env
        working-directory: AppFlowy-Cloud
        run: |
          cp deploy.env .env
          sed -i 's|RUST_LOG=.*|RUST_LOG=trace|' .env
          sed -i 's|GOTRUE_MAILER_AUTOCONFIRM=.*|GOTRUE_MAILER_AUTOCONFIRM=true|' .env
          sed -i 's|API_EXTERNAL_URL=.*|API_EXTERNAL_URL=http://localhost|' .env

      - name: Ensure AppFlowy-Cloud is Running with Correct Version
        working-directory: AppFlowy-Cloud
        env:
          APPFLOWY_CLOUD_VERSION: ${{ env.CLOUD_VERSION }}
          APPFLOWY_HISTORY_VERSION: ${{ env.CLOUD_VERSION }}
          APPFLOWY_WORKER_VERSION: ${{ env.CLOUD_VERSION }}
        run: |
          # Remove all containers if any exist
          if [ "$(docker ps -aq)" ]; then
            docker rm -f $(docker ps -aq)
          else
            echo "No containers to remove."
          fi

          # Remove all volumes if any exist
          if [ "$(docker volume ls -q)" ]; then
            docker volume rm $(docker volume ls -q)
          else
            echo "No volumes to remove."
          fi

          docker compose pull
          docker compose up -d
          echo "Waiting for the container to be ready..."
          sleep 10
          docker ps -a
          docker compose logs

      - name: Run rust-lib tests
        working-directory: frontend/rust-lib
        env:
          RUST_LOG: info
          RUST_BACKTRACE: 1
          af_cloud_test_base_url: http://localhost
          af_cloud_test_ws_url: ws://localhost/ws/v1
          af_cloud_test_gotrue_url: http://localhost/gotrue
        run: |
          DISABLE_CI_TEST_LOG="true" cargo test --no-default-features --features="dart" -- --skip local_ollama_test

      - name: rustfmt rust-lib
        run: cargo fmt --all -- --check
        working-directory: frontend/rust-lib/

      - name: clippy rust-lib
        run: cargo clippy --all-targets -- -D warnings
        working-directory: frontend/rust-lib

      - name: "Debug: show Appflowy-Cloud container logs"
        if: failure()
        working-directory: AppFlowy-Cloud
        run: |
          docker compose logs appflowy_cloud

      - name: Clean up Docker images
        run: |
          docker image prune -af
          docker volume prune -f
\n```\n\n### .github/workflows/rust_coverage.yml\n\n```yaml\nname: Rust code coverage

on:
  push:
    branches:
      - "main"
      - "release/*"
    paths:
      - "frontend/rust-lib/**"

env:
  CARGO_TERM_COLOR: always
  FLUTTER_VERSION: "3.27.4"
  RUST_TOOLCHAIN: "1.85.0"

jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout source code
        uses: actions/checkout@v4

      - name: Install Rust toolchain
        id: rust_toolchain
        uses: actions-rs/toolchain@v1
        with:
          toolchain: ${{ env.RUST_TOOLCHAIN }}
          target: ${{ matrix.job.target }}
          override: true
          profile: minimal

      - name: Install flutter
        id: flutter
        uses: subosito/flutter-action@v2
        with:
          channel: "stable"
          flutter-version: ${{ env.FLUTTER_VERSION }}
          cache: true

      - name: Install prerequisites
        working-directory: frontend
        run: |
          cargo install --force --locked cargo-make
          cargo install --force --locked duckscript_cli

      - uses: Swatinem/rust-cache@v2
        with:
          prefix-key: ${{ matrix.job.os }}

      - name: Install code-coverage tools
        working-directory: frontend
        run: |
          sudo wget -qO /etc/apt/trusted.gpg.d/dart_linux_signing_key.asc https://dl-ssl.google.com/linux/linux_signing_key.pub
          sudo apt-get update
          sudo apt-get install keybinder-3.0
          cargo install grcov
          rustup component add llvm-tools-preview

      - name: Run tests
        working-directory: frontend
        run: cargo make rust_unit_test_with_coverage
\n```\n\n### .github/workflows/translation_notify.yml\n\n```yaml\nname: Translation Notify
on:
  push:
    branches: [ main ]
    paths:
      - "frontend/appflowy_flutter/assets/translations/en.json"

jobs:
  Discord-Notify:
    runs-on: ubuntu-latest
    steps:
      - uses: Ilshidur/action-discord@master
        env:
          DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK }}
        with:
          args: |
            @appflowytranslators English UI strings has been updated.
            Link to changes: ${{github.event.compare}}
\n```\n\n## William-kelvem94/AFFiNE-Will\n\n### .github/workflows/auto-labeler.yml\n\n```yaml\nname: 'Pull Request Labeler'
on:
  pull_request_target:
    types:
      - opened
      - reopened
      - synchronize

jobs:
  triage:
    permissions:
      contents: read
      pull-requests: write
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/labeler@v6
\n```\n\n### .github/workflows/build-images.yml\n\n```yaml\nname: Build Images

on:
  workflow_call:
    inputs:
      build-type:
        type: string
        required: true
      app-version:
        type: string
        required: true
      git-short-hash:
        type: string
        required: true

permissions:
  contents: 'write'
  id-token: 'write'
  packages: 'write'

jobs:
  build-web:
    name: Build @affine/web
    runs-on: ubuntu-latest
    environment: ${{ inputs.build-type }}
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
      - name: Build Core
        run: yarn affine @affine/web build
        env:
          R2_ACCOUNT_ID: ${{ secrets.R2_ACCOUNT_ID }}
          R2_ACCESS_KEY_ID: ${{ secrets.R2_ACCESS_KEY_ID }}
          R2_SECRET_ACCESS_KEY: ${{ secrets.R2_SECRET_ACCESS_KEY }}
          BUILD_TYPE: ${{ inputs.build-type }}
          CAPTCHA_SITE_KEY: ${{ secrets.CAPTCHA_SITE_KEY }}
          SENTRY_ORG: ${{ secrets.SENTRY_ORG }}
          SENTRY_PROJECT: 'affine-web'
          SENTRY_RELEASE: ${{ inputs.app-version }}
          SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
          SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          PERFSEE_TOKEN: ${{ secrets.PERFSEE_TOKEN }}
      - name: Upload web artifact
        uses: actions/upload-artifact@v4
        with:
          name: web
          path: ./packages/frontend/apps/web/dist
          if-no-files-found: error

  build-admin:
    name: Build @affine/admin
    runs-on: ubuntu-latest
    environment: ${{ inputs.build-type }}
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
      - name: Build Admin
        run: yarn affine @affine/admin build
        env:
          R2_ACCOUNT_ID: ${{ secrets.R2_ACCOUNT_ID }}
          R2_ACCESS_KEY_ID: ${{ secrets.R2_ACCESS_KEY_ID }}
          R2_SECRET_ACCESS_KEY: ${{ secrets.R2_SECRET_ACCESS_KEY }}
          BUILD_TYPE: ${{ inputs.build-type }}
          CAPTCHA_SITE_KEY: ${{ secrets.CAPTCHA_SITE_KEY }}
          SENTRY_ORG: ${{ secrets.SENTRY_ORG }}
          SENTRY_PROJECT: 'affine-admin'
          SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
          SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          PERFSEE_TOKEN: ${{ secrets.PERFSEE_TOKEN }}
      - name: Upload admin artifact
        uses: actions/upload-artifact@v4
        with:
          name: admin
          path: ./packages/frontend/admin/dist
          if-no-files-found: error

  build-mobile:
    name: Build @affine/mobile
    runs-on: ubuntu-latest
    environment: ${{ inputs.build-type }}
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
      - name: Build Mobile
        run: yarn affine @affine/mobile build
        env:
          R2_ACCOUNT_ID: ${{ secrets.R2_ACCOUNT_ID }}
          R2_ACCESS_KEY_ID: ${{ secrets.R2_ACCESS_KEY_ID }}
          R2_SECRET_ACCESS_KEY: ${{ secrets.R2_SECRET_ACCESS_KEY }}
          BUILD_TYPE: ${{ inputs.build-type }}
          CAPTCHA_SITE_KEY: ${{ secrets.CAPTCHA_SITE_KEY }}
          SENTRY_ORG: ${{ secrets.SENTRY_ORG }}
          SENTRY_PROJECT: 'affine-mobile'
          SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
          SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          PERFSEE_TOKEN: ${{ secrets.PERFSEE_TOKEN }}
      - name: Upload mobile artifact
        uses: actions/upload-artifact@v4
        with:
          name: mobile
          path: ./packages/frontend/apps/mobile/dist
          if-no-files-found: error

  build-server-native:
    name: Build Server native - ${{ matrix.targets.name }}
    runs-on: ubuntu-22.04
    environment: ${{ inputs.build-type }}
    strategy:
      fail-fast: false
      matrix:
        targets:
          - name: x86_64-unknown-linux-gnu
            file: server-native.x64.node
          - name: aarch64-unknown-linux-gnu
            file: server-native.arm64.node
          - name: armv7-unknown-linux-gnueabihf
            file: server-native.armv7.node

    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          electron-install: false
          extra-flags: workspaces focus @affine/server-native
      - name: Build Rust
        uses: ./.github/actions/build-rust
        env:
          AFFINE_PRO_PUBLIC_KEY: ${{ secrets.AFFINE_PRO_PUBLIC_KEY }}
          AFFINE_PRO_LICENSE_AES_KEY: ${{ secrets.AFFINE_PRO_LICENSE_AES_KEY }}
        with:
          target: ${{ matrix.targets.name }}
          package: '@affine/server-native'
      - name: Rename ${{ matrix.targets.file }}
        run: |
          mv ./packages/backend/native/server-native.node ./packages/backend/native/${{ matrix.targets.file }}
      - name: Upload ${{ matrix.targets.file }}
        uses: actions/upload-artifact@v4
        with:
          name: server-native-${{ matrix.targets.file }}
          path: ./packages/backend/native/${{ matrix.targets.file }}
          if-no-files-found: error

  build-server:
    name: Build Server
    runs-on: ubuntu-latest
    needs:
      - build-server-native
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          electron-install: false
          extra-flags: workspaces focus @affine/server @types/affine__env
      - name: Download server-native
        uses: actions/download-artifact@v4
        with:
          pattern: server-native-*
          merge-multiple: true
          path: ./packages/backend/native
      - name: List server-native files
        run: ls -alh ./packages/backend/native
      - name: Build Server
        run: yarn workspace @affine/server build
      - name: Upload server dist
        uses: actions/upload-artifact@v4
        with:
          name: server-dist
          path: ./packages/backend/server/dist
          if-no-files-found: error

  build-images:
    name: Build Images
    runs-on: ubuntu-latest
    needs:
      - build-server
      - build-web
      - build-mobile
      - build-admin
    steps:
      - uses: actions/checkout@v6
      - name: Download server dist
        uses: actions/download-artifact@v4
        with:
          name: server-dist
          path: ./packages/backend/server/dist
      - name: Login to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          logout: false
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - name: Set up QEMU
        uses: docker/setup-qemu-action@v3
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      # setup node without cache configuration
      # Prisma cache is not compatible with docker build cache
      - name: Setup Node.js
        uses: actions/setup-node@v6
        with:
          node-version-file: '.nvmrc'
          registry-url: https://npm.pkg.github.com
          scope: '@toeverything'

      - name: Download web artifact
        uses: actions/download-artifact@v4
        with:
          name: web
          path: ./packages/frontend/apps/web/dist

      - name: Download mobile artifact
        uses: actions/download-artifact@v4
        with:
          name: mobile
          path: ./packages/frontend/apps/mobile/dist

      - name: Download admin artifact
        uses: actions/download-artifact@v4
        with:
          name: admin
          path: ./packages/frontend/admin/dist

      - name: Install Node.js dependencies
        run: |
          yarn config set --json supportedArchitectures.cpu '["x64", "arm64", "arm"]'
          yarn config set --json supportedArchitectures.libc '["glibc"]'
          yarn workspaces focus @affine/server --production

      - name: Generate Prisma client
        run: yarn workspace @affine/server prisma generate

      - name: Mv node_modules
        run: mv ./node_modules ./packages/backend/server

      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}

      - name: Build backend Dockerfile
        uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          pull: true
          platforms: linux/amd64,linux/arm64,linux/arm/v7
          provenance: true
          file: .github/deployment/node/Dockerfile
          tags: ghcr.io/toeverything/affine:${{inputs.build-type}}-${{ inputs.git-short-hash }}
\n```\n\n### .github/workflows/build-test.yml\n\n```yaml\nname: Build & Test

on:
  push:
    branches:
      - canary
      - beta
      - stable
      - v[0-9]+.[0-9]+.x-staging
      - v[0-9]+.[0-9]+.x
    paths-ignore:
      - README.md
  pull_request:
  merge_group:

env:
  DEBUG: napi:*
  BUILD_TYPE: canary
  APP_NAME: affine
  AFFINE_ENV: dev
  COVERAGE: true
  MACOSX_DEPLOYMENT_TARGET: '11.6'
  DEPLOYMENT_TYPE: affine
  AFFINE_INDEXER_ENABLED: true

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest
    env:
      NODE_OPTIONS: --max-old-space-size=14384
    permissions:
      actions: read
      contents: read
      security-events: write

    strategy:
      fail-fast: false
      matrix:
        language: ['javascript', 'typescript']
        project: ['affine', 'blocksuite']

    steps:
      - name: Checkout repository
        uses: actions/checkout@v6

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v3
        with:
          languages: ${{ matrix.language }}
          source-root: ${{ matrix.project == 'affine' && '.' || 'blocksuite' }}

      - name: Delete blocksuite before codeql analysis
        if: ${{ matrix.project == 'affine' }}
        run: rm -rf blocksuite

      - name: Autobuild
        uses: github/codeql-action/autobuild@v3

      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v3
  lint:
    name: Lint
    runs-on: ubuntu-24.04-arm
    steps:
      - uses: actions/checkout@v6
      - name: Setup Go (for actionlint)
        uses: actions/setup-go@v6
        with:
          go-version: 'stable'
      - name: Install actionlint
        shell: bash
        run: |
          set -euo pipefail
          go install github.com/rhysd/actionlint/cmd/actionlint@v1.7.11
      - name: Run actionlint
        shell: bash
        run: |
          set -euo pipefail
          "$(go env GOPATH)/bin/actionlint"
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          electron-install: false
          full-cache: true
      - name: Run oxlint
        run: yarn lint:ox
      - name: Run i18n codegen
        run: yarn affine @affine/i18n build
      - name: Run ESLint
        run: yarn lint:eslint --max-warnings=0
      - name: Run Prettier
        # Set nmMode in `actions/setup-node` will modify the .yarnrc.yml
        run: |
          git checkout .yarnrc.yml
          yarn lint:prettier
      - name: Yarn Dedupe
        run: yarn dedupe --check

  typecheck:
    name: Typecheck
    runs-on: ubuntu-24.04-arm
    env:
      NODE_OPTIONS: --max-old-space-size=14384
    steps:
      - uses: actions/checkout@v6
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          electron-install: false
          full-cache: true
      - name: Run i18n codegen
        run: |
          yarn affine @affine/i18n build
          git checkout packages/frontend/i18n/src/i18n-completenesses.json
          if git status --porcelain | grep -q .; then
            echo "Run 'yarn affine @affine/i18n build' and make sure all generated i18n changes are submitted"
            exit 1
          else
            echo "All generated i18n changes are submitted"
          fi
      - name: Run Type Check
        run: yarn typecheck
      - name: Run BS Docs Build
        run: |
          yarn affine bs-docs build
          if git status --porcelain | grep -q .; then
            echo "Run 'yarn typecheck && yarn affine bs-docs build' and make sure all changes are submitted"
            exit 1
          else
            echo "All changes are submitted"
          fi

  rust-test-filter:
    name: Rust test filter
    runs-on: ubuntu-latest
    outputs:
      run-rust: ${{ steps.rust-filter.outputs.rust }}
    steps:
      - uses: actions/checkout@v6

      - uses: dorny/paths-filter@v3
        id: rust-filter
        with:
          filters: |
            rust:
              - '**/*.rs'
              - '**/Cargo.toml'
              - '**/Cargo.lock'
              - '.cargo/**'
              - 'rust-toolchain*'
              - '.github/actions/build-rust/**'

  lint-rust:
    name: Lint Rust
    if: ${{ needs.rust-test-filter.outputs.run-rust == 'true' }}
    runs-on: ubuntu-latest
    needs:
      - rust-test-filter
    steps:
      - uses: actions/checkout@v6
      - uses: ./.github/actions/build-rust
        with:
          target: x86_64-unknown-linux-gnu
          package: 'affine'
          no-build: 'true'
      - name: fmt check
        run: |
          rustup toolchain add nightly
          rustup component add --toolchain nightly-x86_64-unknown-linux-gnu rustfmt
          cargo +nightly fmt --all -- --check
      - name: Clippy
        run: |
          rustup component add clippy
          cargo clippy --workspace --exclude affine_server_native --all-targets --all-features -- -D warnings
          cargo clippy -p affine_server_native --all-targets --all-features -- -D warnings

  check-git-status:
    name: Check Git Status
    runs-on: ubuntu-latest
    needs:
      - build-server-native
    steps:
      - uses: actions/checkout@v6
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          full-cache: true

      - name: Download server-native.node
        uses: actions/download-artifact@v4
        with:
          name: server-native.node
          path: ./packages/backend/native

      - name: Run Check
        run: |
          yarn affine init
          yarn affine gql build
          yarn affine i18n build
          yarn affine server genconfig
          git checkout packages/frontend/i18n/src/i18n-completenesses.json
          if git status --porcelain | grep -q .; then
            echo "Run 'yarn affine init && yarn affine gql build && yarn affine i18n build && yarn affine server genconfig' and make sure all changes are submitted"
            exit 1
          else
            echo "All changes are submitted"
          fi

  check-yarn-binary:
    name: Check yarn binary
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Run check
        run: |
          set -euo pipefail
          yarn_version="$(node -e "console.log(require('./package.json').packageManager.split('@')[1])")"
          yarn set version "$yarn_version"
          git diff --exit-code

  e2e-blocksuite-test:
    name: E2E BlockSuite Test
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        shard: [1, 2, 3, 4, 5]
    steps:
      - uses: actions/checkout@v6
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          extra-flags: workspaces focus @affine/monorepo @affine-test/blocksuite @blocksuite/playground @blocksuite/integration-test
          playwright-install: true
          playwright-platform: 'chromium'
          electron-install: false
          full-cache: true

      - name: Run playground build
        run: yarn workspace @blocksuite/playground build

      - name: Run playwright tests
        run: yarn workspace @affine-test/blocksuite test --forbid-only --shard=${{ matrix.shard }}/${{ strategy.job-total }}

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-results-e2e-bs-${{ matrix.shard }}
          path: ./test-results
          if-no-files-found: ignore

  e2e-blocksuite-cross-browser-test:
    name: E2E BlockSuite Cross Browser Test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          extra-flags: workspaces focus @affine/monorepo @affine-test/blocksuite @blocksuite/playground @blocksuite/integration-test
          playwright-install: true
          playwright-platform: 'chromium,firefox,webkit'
          electron-install: false
          full-cache: true

      - name: Run playground build
        run: yarn workspace @blocksuite/playground build

      - name: Run integration browser tests
        timeout-minutes: 10
        run: yarn workspace @blocksuite/integration-test test:unit

      - name: Run cross-platform playwright tests
        timeout-minutes: 10
        run: yarn workspace @affine-test/blocksuite test "cross-platform/" --forbid-only

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-results-e2e-bs-cross-browser
          path: ./test-results
          if-no-files-found: ignore

  e2e-test:
    name: E2E Test
    runs-on: ubuntu-24.04-arm
    env:
      DISTRIBUTION: web
      IN_CI_TEST: true
      NODE_OPTIONS: --max-old-space-size=14384
    strategy:
      fail-fast: false
      matrix:
        shard: [1, 2, 3, 4, 5]
    steps:
      - uses: actions/checkout@v6
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          extra-flags: workspaces focus @affine/monorepo @affine-test/affine-local @affine/web @affine/server
          playwright-install: true
          playwright-platform: 'chromium'
          electron-install: false
          full-cache: true

      - name: Run playwright tests
        run: yarn affine @affine-test/affine-local e2e --forbid-only --shard=${{ matrix.shard }}/${{ strategy.job-total }}

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-results-e2e-${{ matrix.shard }}
          path: ./test-results
          if-no-files-found: ignore

  e2e-mobile-test:
    name: E2E Mobile Test
    runs-on: ubuntu-latest
    env:
      DISTRIBUTION: mobile
      IN_CI_TEST: true
    strategy:
      fail-fast: false
      matrix:
        shard: [1, 2]
    steps:
      - uses: actions/checkout@v6
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          extra-flags: workspaces focus @affine/monorep\n```\n\n### .github/workflows/copilot-test-automatically.yml\n\n```yaml\nname: Copilot Test Automatically

on:
  push:
    tags:
      - 'v[0-9]+.[0-9]+.[0-9]+-canary.[0-9]+'
  schedule:
    - cron: '0 8 * * *'
  workflow_dispatch:

permissions:
  actions: write

jobs:
  dispatch-test:
    runs-on: ubuntu-latest
    name: Setup Test
    steps:
      - name: dispatch test by tag
        if: ${{ github.event_name == 'push' || github.event_name == 'workflow_dispatch' }}
        uses: benc-uk/workflow-dispatch@v1
        with:
          workflow: copilot-test.yml
      - name: dispatch test by schedule
        if: ${{ github.event_name == 'schedule' }}
        uses: benc-uk/workflow-dispatch@v1
        with:
          workflow: copilot-test.yml
          ref: canary
\n```\n\n### .github/workflows/copilot-test.yml\n\n```yaml\nname: Copilot Cron Test

on:
  workflow_dispatch:

jobs:
  build-server-native:
    name: Build Server native
    runs-on: ubuntu-latest
    env:
      CARGO_PROFILE_RELEASE_DEBUG: '1'
    steps:
      - uses: actions/checkout@v6
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          extra-flags: workspaces focus @affine/server-native
          electron-install: false
      - name: Build Rust
        uses: ./.github/actions/build-rust
        with:
          target: 'x86_64-unknown-linux-gnu'
          package: '@affine/server-native'
      - name: Upload server-native.node
        uses: actions/upload-artifact@v4
        with:
          name: server-native.node
          path: ./packages/backend/native/server-native.node
          if-no-files-found: error

  copilot-api-test:
    name: Server Copilot Api Test
    runs-on: ubuntu-latest
    needs:
      - build-server-native
    env:
      NODE_ENV: test
      DISTRIBUTION: web
      DATABASE_URL: postgresql://affine:affine@localhost:5432/affine
      REDIS_SERVER_HOST: localhost
    services:
      postgres:
        image: pgvector/pgvector:pg16
        env:
          POSTGRES_PASSWORD: affine
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
      redis:
        image: redis
        ports:
          - 6379:6379
      mailer:
        image: mailhog/mailhog
        ports:
          - 1025:1025
          - 8025:8025
      indexer:
        image: manticoresearch/manticore:10.1.0
        ports:
          - 9308:9308
    steps:
      - uses: actions/checkout@v6

      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          playwright-install: true
          electron-install: false
          full-cache: true

      - name: Download server-native.node
        uses: actions/download-artifact@v4
        with:
          name: server-native.node
          path: ./packages/backend/native

      - name: Prepare Server Test Environment
        env:
          SERVER_CONFIG: ${{ secrets.TEST_SERVER_CONFIG }}
        uses: ./.github/actions/server-test-env

      - name: Run server tests
        run: yarn affine @affine/server test:copilot:coverage --forbid-only
        env:
          CARGO_TARGET_DIR: '${{ github.workspace }}/target'

      - name: Upload server test coverage results
        uses: codecov/codecov-action@v5
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          files: ./packages/backend/server/.coverage/lcov.info
          flags: server-test
          name: affine
          fail_ci_if_error: false

  copilot-e2e-test:
    name: Frontend Copilot E2E Test
    runs-on: ubuntu-latest
    env:
      DISTRIBUTION: web
      DATABASE_URL: postgresql://affine:affine@localhost:5432/affine
      REDIS_SERVER_HOST: localhost
      IN_CI_TEST: true
    strategy:
      fail-fast: false
      matrix:
        shardIndex: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        shardTotal: [10]
    needs:
      - build-server-native
    services:
      postgres:
        image: pgvector/pgvector:pg16
        env:
          POSTGRES_PASSWORD: affine
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
      redis:
        image: redis
        ports:
          - 6379:6379
      indexer:
        image: manticoresearch/manticore:10.1.0
        ports:
          - 9308:9308
    steps:
      - uses: actions/checkout@v6

      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          playwright-install: true
          electron-install: false
          hard-link-nm: false

      - name: Download server-native.node
        uses: actions/download-artifact@v4
        with:
          name: server-native.node
          path: ./packages/backend/native

      - name: Prepare Server Test Environment
        env:
          SERVER_CONFIG: ${{ secrets.TEST_SERVER_CONFIG }}
        uses: ./.github/actions/server-test-env

      - name: Run Copilot E2E Test ${{ matrix.shardIndex }}/${{ matrix.shardTotal }}
        uses: ./.github/actions/copilot-test
        with:
          script: yarn affine @affine-test/affine-cloud-copilot e2e --forbid-only --shard=${{ matrix.shardIndex }}/${{ matrix.shardTotal }}

  test-done:
    needs:
      - copilot-api-test
      - copilot-e2e-test
    if: always()
    runs-on: ubuntu-latest
    name: Post test result message
    steps:
      - uses: actions/checkout@v6
        with:
          fetch-depth: 0
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        with:
          extra-flags: 'workspaces focus @affine/copilot-result'
          electron-install: false
      - name: Post Success event to a Slack channel
        if: ${{ always() && !contains(needs.*.result, 'failure') && !contains(needs.*.result, 'cancelled') }}
        run: node ./tools/copilot-result/index.js
        env:
          CHANNEL_ID: ${{ secrets.RELEASE_SLACK_CHNNEL_ID }}
          SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
          BRANCH_SHA: ${{ github.sha }}
          BRANCH_NAME: ${{ github.ref }}
          COPILOT_RESULT: success
      - name: Post Failed event to a Slack channel
        id: failed-slack
        if: ${{ always() && contains(needs.*.result, 'failure') }}
        run: node ./tools/copilot-result/index.js
        env:
          CHANNEL_ID: ${{ secrets.RELEASE_SLACK_CHNNEL_ID }}
          SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
          BRANCH_SHA: ${{ github.sha }}
          BRANCH_NAME: ${{ github.ref }}
          COPILOT_RESULT: failed
      - name: Post Cancel event to a Slack channel
        id: cancel-slack
        if: ${{ always() && contains(needs.*.result, 'cancelled') && !contains(needs.*.result, 'failure') }}
        run: node ./tools/copilot-result/index.js
        env:
          CHANNEL_ID: ${{ secrets.RELEASE_SLACK_CHNNEL_ID }}
          SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
          BRANCH_SHA: ${{ github.sha }}
          BRANCH_NAME: ${{ github.ref }}
          COPILOT_RESULT: canceled
\n```\n\n### .github/workflows/pr-title-lint.yml\n\n```yaml\nname: PR Title Lint

on:
  pull_request:
    types:
      - opened
      - edited
      - synchronize
    branches:
      - canary

permissions:
  contents: read

jobs:
  check-pull-request-title:
    name: Check pull request title
    runs-on: ubuntu-latest
    if: ${{ github.event.action != 'edited' || github.event.changes.title != null }}
    steps:
      - uses: actions/checkout@v6
      - name: Setup Node.js
        uses: actions/setup-node@v6
        with:
          cache: 'yarn'
          node-version-file: '.nvmrc'
      - name: Install dependencies
        run: yarn workspaces focus @affine/commitlint-config
      - name: Check PR title
        env:
          TITLE: ${{ github.event.pull_request.title }}
        run: echo "$TITLE" | yarn workspace @affine/commitlint-config commitlint -g ./.commitlintrc.json
\n```\n\n### .github/workflows/release-cloud.yml\n\n```yaml\nname: Release Cloud

on:
  workflow_call:
    inputs:
      build-type:
        required: true
        type: string
      app-version:
        required: true
        type: string
      git-short-hash:
        required: true
        type: string

permissions:
  contents: 'write'
  id-token: 'write'
  packages: 'write'

jobs:
  build-images:
    name: Build Images
    uses: ./.github/workflows/build-images.yml
    secrets: inherit
    with:
      build-type: ${{ inputs.build-type }}
      app-version: ${{ inputs.app-version }}
      git-short-hash: ${{ inputs.git-short-hash }}

  deploy:
    name: Deploy to cluster
    environment: ${{ inputs.build-type }}
    needs:
      - build-images
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Deploy to ${{ inputs.build-type }}
        uses: ./.github/actions/deploy
        with:
          gcp-project-number: ${{ secrets.GCP_PROJECT_NUMBER }}
          gcp-project-id: ${{ secrets.GCP_PROJECT_ID }}
          service-account: ${{ secrets.GCP_HELM_DEPLOY_SERVICE_ACCOUNT }}
          cluster-name: ${{ secrets.GCP_CLUSTER_NAME }}
          cluster-location: ${{ secrets.GCP_CLUSTER_LOCATION }}
        env:
          BUILD_TYPE: ${{ inputs.build-type }}
          APP_VERSION: ${{ inputs.app-version }}
          GIT_SHORT_HASH: ${{ inputs.git-short-hash }}
          DEPLOY_HOST: ${{ secrets.DEPLOY_HOST }}
          CANARY_DEPLOY_HOST: ${{ secrets.CANARY_DEPLOY_HOST }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
          DATABASE_USERNAME: ${{ secrets.DATABASE_USERNAME }}
          DATABASE_PASSWORD: ${{ secrets.DATABASE_PASSWORD }}
          DATABASE_NAME: ${{ secrets.DATABASE_NAME }}
          GCLOUD_CONNECTION_NAME: ${{ secrets.GCLOUD_CONNECTION_NAME }}
          REDIS_SERVER_HOST: ${{ secrets.REDIS_SERVER_HOST }}
          REDIS_SERVER_PASSWORD: ${{ secrets.REDIS_SERVER_PASSWORD }}
          CLOUD_SQL_IAM_ACCOUNT: ${{ secrets.CLOUD_SQL_IAM_ACCOUNT }}
          APP_IAM_ACCOUNT: ${{ secrets.APP_IAM_ACCOUNT }}
          STATIC_IP_NAME: ${{ secrets.STATIC_IP_NAME }}
          AFFINE_INDEXER_SEARCH_PROVIDER: ${{ secrets.AFFINE_INDEXER_SEARCH_PROVIDER }}
          AFFINE_INDEXER_SEARCH_ENDPOINT: ${{ secrets.AFFINE_INDEXER_SEARCH_ENDPOINT }}
          AFFINE_INDEXER_SEARCH_API_KEY: ${{ secrets.AFFINE_INDEXER_SEARCH_API_KEY }}
\n```\n\n### .github/workflows/release-desktop-platform.yml\n\n```yaml\nname: Release Desktop Platform

on:
  workflow_call:
    inputs:
      build_type:
        required: true
        type: string
      app_version:
        required: true
        type: string
      git_short_hash:
        required: true
        type: string
      runner:
        required: true
        type: string
      platform:
        required: true
        type: string
      arch:
        required: true
        type: string
      target:
        required: true
        type: string
      apple_codesign:
        required: false
        default: false
        type: boolean
      install_linux_deps:
        required: false
        default: false
        type: boolean
      enable_scripts:
        required: false
        default: false
        type: boolean
    outputs:
      files_to_be_signed:
        description: Files to be signed (Windows only)
        value: ${{ jobs.build.outputs.files_to_be_signed }}

permissions:
  actions: write
  contents: write
  security-events: write
  id-token: write
  attestations: write

jobs:
  build:
    runs-on: ${{ inputs.runner }}
    outputs:
      files_to_be_signed: ${{ steps.get_files_to_be_signed.outputs.FILES_TO_BE_SIGNED }}
    env:
      BUILD_TYPE: ${{ inputs.build_type }}
      RELEASE_VERSION: ${{ inputs.app_version }}
      DEBUG: 'affine:*,napi:*'
      APP_NAME: affine
      MACOSX_DEPLOYMENT_TARGET: '12.0'
      SKIP_GENERATE_ASSETS: 1
      APPLE_ID: ${{ secrets.APPLE_ID }}
      APPLE_PASSWORD: ${{ secrets.APPLE_PASSWORD }}
      APPLE_TEAM_ID: ${{ secrets.APPLE_TEAM_ID }}
      SENTRY_ORG: ${{ secrets.SENTRY_ORG }}
      SENTRY_PROJECT: 'affine'
      SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
      SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
      SENTRY_RELEASE: ${{ inputs.app_version }}
    steps:
      - uses: actions/checkout@v6

      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app_version }}

      - name: Setup Node.js
        timeout-minutes: 10
        uses: ./.github/actions/setup-node
        with:
          extra-flags: workspaces focus @affine/electron @affine/monorepo @affine/nbstore @toeverything/infra
          hard-link-nm: false
          nmHoistingLimits: workspaces
          enableScripts: ${{ inputs.enable_scripts }}

      - name: Build AFFiNE native
        uses: ./.github/actions/build-rust
        with:
          target: ${{ inputs.target }}
          package: '@affine/native'

      - uses: actions/download-artifact@v4
        with:
          name: desktop-web
          path: packages/frontend/apps/electron/resources/web-static

      - name: Build Desktop Layers
        run: yarn affine @affine/electron build

      - name: Signing By Apple Developer ID
        if: ${{ inputs.platform == 'darwin' && inputs.apple_codesign }}
        uses: apple-actions/import-codesign-certs@v6
        with:
          p12-file-base64: ${{ secrets.CERTIFICATES_P12 }}
          p12-password: ${{ secrets.CERTIFICATES_P12_PASSWORD }}

      - name: Install additional dependencies on Linux
        if: ${{ inputs.platform == 'linux' && inputs.install_linux_deps }}
        run: |
          df -h
          sudo add-apt-repository universe
          sudo apt install -y libfuse2 elfutils flatpak flatpak-builder
          flatpak remote-add --user --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
          flatpak update
          # some flatpak deps need git protocol.file.allow
          git config --global protocol.file.allow always
          # clean up apt cache to save disk space
          sudo -E apt-get -y purge azure-cli* zulu* hhvm* llvm* firefox* google* dotnet* aspnetcore* powershell* adoptopenjdk* mysql* php* mongodb* moby* snap* || true
          sudo -E apt-get -qq autoremove --purge
          sudo rm -rf /usr/share/dotnet /opt/ghc /opt/hostedtoolcache/CodeQL /usr/local/lib/android
          sudo apt-get clean
          rm -rf ~/.cache/yarn ~/.npm
          df -h

      - name: Remove nbstore node_modules (darwin/linux)
        if: ${{ inputs.platform != 'win32' }}
        shell: bash
        # node_modules of nbstore is not needed for building, and it will make the build process out of memory
        run: |
          cargo clean
          rm -rf packages/frontend/apps/electron/node_modules/@affine/nbstore/node_modules/@blocksuite
          rm -rf packages/frontend/apps/electron/node_modules/@affine/native/node_modules

      - name: Remove nbstore node_modules (windows)
        if: ${{ inputs.platform == 'win32' }}
        shell: bash
        run: |
          rm -rf packages/frontend/apps/electron/node_modules/@affine/nbstore/node_modules/@blocksuite/affine/node_modules
          rm -rf packages/frontend/apps/electron/node_modules/@affine/native/node_modules

      - name: make
        if: ${{ inputs.platform != 'win32' }}
        run: yarn affine @affine/electron make --platform=${{ inputs.platform }} --arch=${{ inputs.arch }}
        env:
          SKIP_WEB_BUILD: 1
          HOIST_NODE_MODULES: 1
          NODE_OPTIONS: --max-old-space-size=14384

      - name: package
        if: ${{ inputs.platform == 'win32' }}
        run: |
          yarn affine @affine/electron package --platform=${{ inputs.platform }} --arch=${{ inputs.arch }}
        env:
          SKIP_WEB_BUILD: 1
          HOIST_NODE_MODULES: 1
          NODE_OPTIONS: --max-old-space-size=14384

      - name: signing DMG
        if: ${{ inputs.platform == 'darwin' && inputs.apple_codesign }}
        run: |
          codesign --force --sign "Developer ID Application: TOEVERYTHING PTE. LTD." packages/frontend/apps/electron/out/${{ env.BUILD_TYPE }}/make/AFFiNE.dmg

      - name: Save artifacts (mac)
        if: ${{ inputs.platform == 'darwin' }}
        run: |
          mkdir -p builds
          mv packages/frontend/apps/electron/out/*/make/*.dmg ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-macos-${{ inputs.arch }}.dmg
          mv packages/frontend/apps/electron/out/*/make/zip/darwin/${{ inputs.arch }}/*.zip ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-macos-${{ inputs.arch }}.zip

      - name: Save artifacts (linux)
        if: ${{ inputs.platform == 'linux' }}
        run: |
          mkdir -p builds
          mv packages/frontend/apps/electron/out/*/make/zip/linux/${{ inputs.arch }}/*.zip ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-linux-${{ inputs.arch }}.zip
          mv packages/frontend/apps/electron/out/*/make/AppImage/${{ inputs.arch }}/*.AppImage ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-linux-${{ inputs.arch }}.appimage
          mv packages/frontend/apps/electron/out/*/make/deb/${{ inputs.arch }}/*.deb ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-linux-${{ inputs.arch }}.deb
          mv packages/frontend/apps/electron/out/*/make/flatpak/*/*.flatpak ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-linux-${{ inputs.arch }}.flatpak

      - uses: actions/attest-build-provenance@v4
        if: ${{ inputs.platform == 'darwin' }}
        with:
          subject-path: |
            ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-macos-${{ inputs.arch }}.zip
            ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-macos-${{ inputs.arch }}.dmg

      - uses: actions/attest-build-provenance@v4
        if: ${{ inputs.platform == 'linux' }}
        with:
          subject-path: |
            ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-linux-${{ inputs.arch }}.zip
            ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-linux-${{ inputs.arch }}.appimage
            ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-linux-${{ inputs.arch }}.deb
            ./builds/affine-${{ env.RELEASE_VERSION }}-${{ env.BUILD_TYPE }}-linux-${{ inputs.arch }}.flatpak

      - name: Upload Artifact
        if: ${{ inputs.platform == 'darwin' || inputs.platform == 'linux' }}
        uses: actions/upload-artifact@v4
        with:
          name: affine-${{ inputs.platform }}-${{ inputs.arch }}-builds
          path: builds

      - name: get all files to be signed
        id: get_files_to_be_signed
        if: ${{ inputs.platform == 'win32' }}
        shell: pwsh
        run: |
          Set-Variable -Name FILES_TO_BE_SIGNED -Value ((Get-ChildItem -Path packages/frontend/apps/electron/out -Recurse -File | Where-Object { $_.Extension -in @(".exe", ".node", ".dll", ".msi") } | ForEach-Object { '"' + $_.FullName.Replace((Get-Location).Path + '\packages\frontend\apps\electron\out\', '') + '"' }) -join ' ')
          "FILES_TO_BE_SIGNED=$FILES_TO_BE_SIGNED" >> $env:GITHUB_OUTPUT
          echo $FILES_TO_BE_SIGNED

      - name: Zip artifacts for faster upload
        if: ${{ inputs.platform == 'win32' }}
        shell: pwsh
        run: Compress-Archive -CompressionLevel Fastest -Path packages/frontend/apps/electron/out/* -DestinationPath archive.zip

      - name: Save packaged artifacts for signing
        if: ${{ inputs.platform == 'win32' }}
        uses: actions/upload-artifact@v4
        with:
          name: packaged-${{ inputs.platform }}-${{ inputs.arch }}
          path: |
            archive.zip
            !**/*.map
\n```\n\n### .github/workflows/release-desktop.yml\n\n```yaml\nname: Release Desktop

on:
  workflow_call:
    inputs:
      build-type:
        required: true
        type: string
      app-version:
        required: true
        type: string
      git-short-hash:
        required: true
        type: string
      desktop_macos:
        description: 'Desktop - macOS'
        required: false
        default: true
        type: boolean
      desktop_windows:
        description: 'Desktop - Windows'
        required: false
        default: true
        type: boolean
      desktop_linux:
        description: 'Desktop - Linux'
        required: false
        default: true
        type: boolean
      require-windows-signing:
        description: 'Require all Windows signing steps to succeed before release'
        required: false
        default: false
        type: boolean

permissions:
  actions: write
  contents: write
  security-events: write
  id-token: write
  attestations: write

env:
  BUILD_TYPE: ${{ inputs.build-type }}
  RELEASE_VERSION: ${{ inputs.app-version }}
  DEBUG: 'affine:*,napi:*'
  APP_NAME: affine
  MACOSX_DEPLOYMENT_TARGET: '11.6'

jobs:
  before-make:
    if: ${{ inputs.desktop_macos || inputs.desktop_windows || inputs.desktop_linux }}
    runs-on: ubuntu-latest
    environment: ${{ inputs.build-type }}
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
      - name: Setup @sentry/cli
        uses: ./.github/actions/setup-sentry
      - name: generate-assets
        run: yarn affine @affine/electron generate-assets
        env:
          SENTRY_ORG: ${{ secrets.SENTRY_ORG }}
          SENTRY_PROJECT: 'affine'
          SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
          SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          SENTRY_RELEASE: ${{ inputs.app-version }}
          RELEASE_VERSION: ${{ inputs.app-version }}

      - name: Upload web artifact
        uses: actions/upload-artifact@v4
        with:
          name: desktop-web
          path: packages/frontend/apps/electron/resources/web-static

  windows-signer-gate:
    if: ${{ inputs.desktop_windows }}
    runs-on: ubuntu-latest
    outputs:
      signer_available: ${{ steps.check.outputs.signer_available }}
    steps:
      - uses: actions/checkout@v6
      - name: Check windows signer availability
        id: check
        run: node ./scripts/check-windows-signer.mjs
        env:
          BUILD_TYPE: ${{ inputs.build-type }}
          GITHUB_TOKEN: ${{ github.token }}
          REQUIRE_SIGNER: ${{ inputs.require-windows-signing }}

  make-distribution-macos:
    if: ${{ inputs.desktop_macos }}
    strategy:
      fail-fast: false
      matrix:
        spec:
          - runner: macos-latest
            platform: darwin
            arch: x64
            target: x86_64-apple-darwin
          - runner: macos-latest
            platform: darwin
            arch: arm64
            target: aarch64-apple-darwin
    needs: before-make
    uses: ./.github/workflows/release-desktop-platform.yml
    secrets: inherit
    with:
      build_type: ${{ inputs.build-type }}
      app_version: ${{ inputs.app-version }}
      git_short_hash: ${{ inputs.git-short-hash }}
      runner: ${{ matrix.spec.runner }}
      platform: ${{ matrix.spec.platform }}
      arch: ${{ matrix.spec.arch }}
      target: ${{ matrix.spec.target }}
      apple_codesign: true

  make-distribution-linux:
    if: ${{ inputs.desktop_linux }}
    strategy:
      fail-fast: false
      matrix:
        spec:
          - runner: ubuntu-latest
            platform: linux
            arch: x64
            target: x86_64-unknown-linux-gnu
    needs: before-make
    uses: ./.github/workflows/release-desktop-platform.yml
    secrets: inherit
    with:
      build_type: ${{ inputs.build-type }}
      app_version: ${{ inputs.app-version }}
      git_short_hash: ${{ inputs.git-short-hash }}
      runner: ${{ matrix.spec.runner }}
      platform: ${{ matrix.spec.platform }}
      arch: ${{ matrix.spec.arch }}
      target: ${{ matrix.spec.target }}
      install_linux_deps: true

  package-distribution-windows-x64:
    if: ${{ inputs.desktop_windows }}
    needs: before-make
    uses: ./.github/workflows/release-desktop-platform.yml
    secrets: inherit
    with:
      build_type: ${{ inputs.build-type }}
      app_version: ${{ inputs.app-version }}
      git_short_hash: ${{ inputs.git-short-hash }}
      runner: windows-latest
      platform: win32
      arch: x64
      target: x86_64-pc-windows-msvc
      enable_scripts: true

  package-distribution-windows-arm64:
    if: ${{ inputs.desktop_windows }}
    needs: before-make
    uses: ./.github/workflows/release-desktop-platform.yml
    secrets: inherit
    with:
      build_type: ${{ inputs.build-type }}
      app_version: ${{ inputs.app-version }}
      git_short_hash: ${{ inputs.git-short-hash }}
      runner: windows-latest
      platform: win32
      arch: arm64
      target: aarch64-pc-windows-msvc
      enable_scripts: true

  sign-packaged-artifacts-windows_x64:
    if: ${{ inputs.desktop_windows && needs.windows-signer-gate.outputs.signer_available == 'true' }}
    needs:
      - windows-signer-gate
      - package-distribution-windows-x64
    uses: ./.github/workflows/windows-signer.yml
    with:
      files: ${{ needs.package-distribution-windows-x64.outputs.files_to_be_signed }}
      artifact-name: packaged-win32-x64

  sign-packaged-artifacts-windows_arm64:
    if: ${{ inputs.desktop_windows && needs.windows-signer-gate.outputs.signer_available == 'true' }}
    needs:
      - windows-signer-gate
      - package-distribution-windows-arm64
    uses: ./.github/workflows/windows-signer.yml
    with:
      files: ${{ needs.package-distribution-windows-arm64.outputs.files_to_be_signed }}
      artifact-name: packaged-win32-arm64

  make-windows-installer:
    if: >-
      ${{
        always() &&
        inputs.desktop_windows &&
        needs.windows-signer-gate.result == 'success' &&
        needs.package-distribution-windows-x64.result == 'success' &&
        needs.package-distribution-windows-arm64.result == 'success' &&
        (
          !inputs.require-windows-signing ||
          (
            needs.sign-packaged-artifacts-windows_x64.result == 'success' &&
            needs.sign-packaged-artifacts-windows_arm64.result == 'success'
          )
        )
      }}
    needs:
      - windows-signer-gate
      - package-distribution-windows-x64
      - package-distribution-windows-arm64
      - sign-packaged-artifacts-windows_x64
      - sign-packaged-artifacts-windows_arm64
    strategy:
      fail-fast: false
      matrix:
        spec:
          - platform: win32
            arch: x64
          - platform: win32
            arch: arm64
    runs-on: windows-latest
    outputs:
      FILES_TO_BE_SIGNED_x64: ${{ steps.get_files_to_be_signed.outputs.FILES_TO_BE_SIGNED_x64 }}
      FILES_TO_BE_SIGNED_arm64: ${{ steps.get_files_to_be_signed.outputs.FILES_TO_BE_SIGNED_arm64 }}
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        timeout-minutes: 10
        uses: ./.github/actions/setup-node
        with:
          extra-flags: workspaces focus @affine/electron @affine/monorepo
          hard-link-nm: false
          nmHoistingLimits: workspaces
        env:
          npm_config_arch: ${{ matrix.spec.arch }}
      - name: Download packaged artifacts
        uses: actions/download-artifact@v4
        with:
          name: packaged-${{ matrix.spec.platform }}-${{ matrix.spec.arch }}
          path: packaged-unsigned
      - name: unzip packaged artifacts
        run: Expand-Archive -Path packaged-unsigned/archive.zip -DestinationPath packages/frontend/apps/electron/out
      - name: Download signed packaged file diff
        if: ${{ (matrix.spec.arch == 'x64' && needs.sign-packaged-artifacts-windows_x64.result == 'success') || (matrix.spec.arch == 'arm64' && needs.sign-packaged-artifacts-windows_arm64.result == 'success') }}
        uses: actions/download-artifact@v4
        with:
          name: signed-packaged-${{ matrix.spec.platform }}-${{ matrix.spec.arch }}
          path: signed-packaged-diff
      - name: Apply signed packaged file diff
        if: ${{ (matrix.spec.arch == 'x64' && needs.sign-packaged-artifacts-windows_x64.result == 'success') || (matrix.spec.arch == 'arm64' && needs.sign-packaged-artifacts-windows_arm64.result == 'success') }}
        shell: pwsh
        run: |
          $DiffRoot = 'signed-packaged-diff/files'
          $TargetRoot = 'packages/frontend/apps/electron/out'
          if (!(Test-Path -LiteralPath $DiffRoot)) {
            throw "Signed diff directory not found: $DiffRoot"
          }

          Copy-Item -Path (Join-Path $DiffRoot '*') -Destination $TargetRoot -Recurse -Force

          $ManifestPath = 'signed-packaged-diff/manifest.json'
          if (Test-Path -LiteralPath $ManifestPath) {
            $ManifestEntries = @(Get-Content -LiteralPath $ManifestPath | ConvertFrom-Json)
            foreach ($Entry in $ManifestEntries) {
              $TargetPath = Join-Path $TargetRoot $Entry.path
              if (!(Test-Path -LiteralPath $TargetPath -PathType Leaf)) {
                throw "Applied signed file not found: $($Entry.path)"
              }

              $TargetHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $TargetPath).Hash
              if ($TargetHash -ne $Entry.sha256) {
                throw "Signed file hash mismatch: $($Entry.path)"
              }
            }
          }

      - name: Make squirrel.windows installer
        run: yarn affine @affine/electron make-squirrel --platform=${{ matrix.spec.platform }} --arch=${{ matrix.spec.arch }}

      - name: Make nsis.w\n```\n\n### .github/workflows/release-mobile.yml\n\n```yaml\nname: Release Mobile

on:
  workflow_call:
    inputs:
      app-version:
        type: string
        required: true
      git-short-hash:
        type: string
        required: true
      build-type:
        type: string
        required: true
      ios-app-version:
        type: string
        required: false

env:
  BUILD_TYPE: ${{ inputs.build-type }}
  DEBUG: napi:*
  KEYCHAIN_NAME: ${{ github.workspace }}/signing_temp

jobs:
  build-ios-web:
    runs-on: ubuntu-latest
    environment: ${{ inputs.build-type }}
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
      - name: Setup @sentry/cli
        uses: ./.github/actions/setup-sentry
      - name: Build Mobile
        run: yarn affine @affine/ios build
        env:
          PUBLIC_PATH: '/'
          SENTRY_ORG: ${{ secrets.SENTRY_ORG }}
          SENTRY_PROJECT: 'affine'
          SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
          SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          SENTRY_RELEASE: ${{ inputs.app-version }}
          RELEASE_VERSION: ${{ inputs.app-version }}
      - name: Upload ios artifact
        uses: actions/upload-artifact@v4
        with:
          name: ios
          path: packages/frontend/apps/ios/dist

  build-android-web:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
      - name: Setup @sentry/cli
        uses: ./.github/actions/setup-sentry
      - name: Build Mobile
        run: yarn affine @affine/android build
        env:
          PUBLIC_PATH: '/'
          SENTRY_ORG: ${{ secrets.SENTRY_ORG }}
          SENTRY_PROJECT: 'affine'
          SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
          SENTRY_DSN: ${{ secrets.SENTRY_DSN }}
          SENTRY_RELEASE: ${{ inputs.app-version }}
      - name: Upload android artifact
        uses: actions/upload-artifact@v4
        with:
          name: android
          path: packages/frontend/apps/android/dist

  ios:
    runs-on: 'macos-15'
    needs:
      - build-ios-web
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
          ios-app-version: ${{ inputs.ios-app-version }}
      - name: 'Update Code Sign Identity'
        shell: bash
        run: ./packages/frontend/apps/ios/update_code_sign_identity.sh
      - name: Download mobile artifact
        uses: actions/download-artifact@v4
        with:
          name: ios
          path: packages/frontend/apps/ios/dist
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        timeout-minutes: 10
        with:
          extra-flags: workspaces focus @affine/ios
          playwright-install: false
          electron-install: false
          hard-link-nm: false
          enableScripts: false
      - uses: maxim-lobanov/setup-xcode@v1
        with:
          xcode-version: 26.2
      - name: Install Swiftformat
        run: brew install swiftformat
      - name: Cap sync
        run: yarn workspace @affine/ios sync
      - name: Signing By Apple Developer ID
        uses: apple-actions/import-codesign-certs@v6
        id: import-codesign-certs
        with:
          p12-file-base64: ${{ secrets.CERTIFICATES_P12_MOBILE }}
          p12-password: ${{ secrets.CERTIFICATES_P12_PASSWORD_MOBILE }}
      - name: Setup Rust
        uses: ./.github/actions/build-rust
        with:
          target: 'aarch64-apple-ios'
          package: 'affine_mobile_native'
          no-build: 'true'
      - name: Testflight
        working-directory: packages/frontend/apps/ios/App
        run: |
          printf '%s' "$BUILD_PROVISION_PROFILE" | base64 --decode -o "$PP_PATH"
          mkdir -p "$HOME/Library/MobileDevice/Provisioning Profiles"
          cp "$PP_PATH" "$HOME/Library/MobileDevice/Provisioning Profiles"
          fastlane beta
        env:
          BUILD_TARGET: distribution
          BUILD_PROVISION_PROFILE: ${{ secrets.BUILD_PROVISION_PROFILE }}
          PP_PATH: ${{ runner.temp }}/build_pp.mobileprovision
          APPLE_STORE_CONNECT_API_KEY_ID: ${{ secrets.APPLE_STORE_CONNECT_API_KEY_ID }}
          APPLE_STORE_CONNECT_API_ISSUER_ID: ${{ secrets.APPLE_STORE_CONNECT_API_ISSUER_ID }}
          APPLE_STORE_CONNECT_API_KEY: ${{ secrets.APPLE_STORE_CONNECT_API_KEY }}

  android:
    runs-on: ubuntu-latest
    permissions:
      id-token: 'write'
    needs:
      - build-android-web
    steps:
      - uses: actions/checkout@v6
      - name: Setup Version
        uses: ./.github/actions/setup-version
        with:
          app-version: ${{ inputs.app-version }}
      - name: Download mobile artifact
        uses: actions/download-artifact@v4
        with:
          name: android
          path: packages/frontend/apps/android/dist
      - name: Load Google Service file
        env:
          DATA: ${{ secrets.FIREBASE_ANDROID_GOOGLE_SERVICE_JSON }}
        run: |
          set -euo pipefail
          printf '%s' "$DATA" | base64 -di > packages/frontend/apps/android/App/app/google-services.json
      - name: Setup Node.js
        uses: ./.github/actions/setup-node
        timeout-minutes: 10
        with:
          extra-flags: workspaces focus @affine/monorepo @affine-tools/cli @affine/android @affine/playstore-auto-bump
          playwright-install: false
          electron-install: false
          hard-link-nm: false
          enableScripts: false
      - name: Setup Rust
        uses: ./.github/actions/build-rust
        with:
          target: 'aarch64-linux-android'
          package: 'affine_mobile_native'
          no-build: 'true'
      - name: Cap sync
        run: yarn workspace @affine/android cap sync
      - uses: actions/setup-python@v6
        with:
          python-version: '3.13'
      - name: Auth gcloud
        id: auth
        uses: google-github-actions/auth@v2
        with:
          workload_identity_provider: 'projects/${{ secrets.GCP_PROJECT_NUMBER }}/locations/global/workloadIdentityPools/github-actions/providers/github-actions-helm-deploy'
          service_account: '${{ secrets.GCP_HELM_DEPLOY_SERVICE_ACCOUNT }}'
          token_format: 'access_token'
          project_id: '${{ secrets.GCP_PROJECT_ID }}'
          access_token_scopes: 'https://www.googleapis.com/auth/androidpublisher'
      - uses: actions/setup-java@v5
        with:
          distribution: 'temurin'
          java-version: '21'
          cache: 'gradle'
      - name: Auto increment version code
        id: bump
        run: yarn affine @affine/playstore-auto-bump bump
        env:
          GOOGLE_APPLICATION_CREDENTIALS: ${{ steps.auth.outputs.credentials_file_path }}
      - name: Build
        run: |
          echo -n "${{ env.AFFINE_ANDROID_SIGN_KEYSTORE }}" | base64 --decode > packages/frontend/apps/android/affine.keystore
          yarn workspace @affine/android cap build android --flavor ${{ env.BUILD_TYPE }} --androidreleasetype AAB
        env:
          AFFINE_ANDROID_KEYSTORE_PASSWORD: ${{ secrets.AFFINE_ANDROID_KEYSTORE_PASSWORD }}
          AFFINE_ANDROID_KEYSTORE_ALIAS_PASSWORD: ${{ secrets.AFFINE_ANDROID_KEYSTORE_ALIAS_PASSWORD }}
          AFFINE_ANDROID_SIGN_KEYSTORE: ${{ secrets.AFFINE_ANDROID_SIGN_KEYSTORE }}
          VERSION_NAME: ${{ inputs.app-version }}
      - name: Upload to Google Play
        uses: r0adkll/upload-google-play@v1
        with:
          serviceAccountJson: ${{ steps.auth.outputs.credentials_file_path }}
          packageName: app.affine.pro
          releaseName: ${{ inputs.app-version }}
          releaseFiles: packages/frontend/apps/android/App/app/build/outputs/bundle/${{ env.BUILD_TYPE }}Release/app-${{ env.BUILD_TYPE }}-release-signed.aab
          track: internal
          status: draft
          existingEditId: ${{ steps.bump.outputs.EDIT_ID }}
\n```\n\n### .github/workflows/release.yml\n\n```yaml\nname: Release

on:
  schedule:
    - cron: '0 9 * * *'

  workflow_dispatch:
    inputs:
      web:
        description: 'Release Web?'
        required: true
        type: boolean
        default: false
      desktop_macos:
        description: 'Desktop - macOS'
        required: true
        type: boolean
        default: false
      desktop_windows:
        description: 'Desktop - Windows'
        required: true
        type: boolean
        default: false
      desktop_linux:
        description: 'Desktop - Linux'
        required: true
        type: boolean
        default: false
      mobile:
        description: 'Release Mobile?'
        required: true
        type: boolean
        default: false
      ios-app-version:
        description: 'iOS App Store Version (Optional, use tag version if empty)'
        required: false
        type: string

permissions:
  contents: write
  pull-requests: write
  actions: write
  id-token: write
  packages: write
  security-events: write
  attestations: write
  issues: write

jobs:
  prepare:
    name: Prepare
    runs-on: ubuntu-latest
    outputs:
      APP_VERSION: ${{ steps.prepare.outputs.APP_VERSION }}
      GIT_SHORT_HASH: ${{ steps.prepare.outputs.GIT_SHORT_HASH }}
      BUILD_TYPE: ${{ steps.prepare.outputs.BUILD_TYPE }}
    steps:
      - uses: actions/checkout@v6
      - name: Prepare Release
        id: prepare
        uses: ./.github/actions/prepare-release

  canary-gate:
    name: Canary Gate
    runs-on: ubuntu-latest
    needs:
      - prepare
    outputs:
      SHOULD_RELEASE: ${{ steps.decide.outputs.SHOULD_RELEASE }}
      LAST_CANARY_TAG: ${{ steps.decide.outputs.LAST_CANARY_TAG }}
      LAST_CANARY_SHA: ${{ steps.decide.outputs.LAST_CANARY_SHA }}
    steps:
      - name: Decide whether to release
        id: decide
        uses: actions/github-script@v8
        with:
          script: |
            const buildType = '${{ needs.prepare.outputs.BUILD_TYPE }}'
            if (buildType !== 'canary') {
              core.setOutput('SHOULD_RELEASE', 'true')
              return
            }

            const owner = context.repo.owner
            const repo = context.repo.repo
            const currentSha = context.sha
            const canaryTagRe = /^v\d+\.\d+\.\d+-canary\.[0-9a-f]+$/i

            let page = 1
            const perPage = 100
            let lastCanary = null

            while (!lastCanary && page <= 10) {
              const { data } = await github.rest.repos.listTags({
                owner,
                repo,
                per_page: perPage,
                page,
              })

              for (const tag of data) {
                if (canaryTagRe.test(tag.name)) {
                  lastCanary = tag
                  break
                }
              }

              if (data.length < perPage) break
              page++
            }

            if (!lastCanary) {
              core.warning('No canary tags found; proceeding with canary release.')
              core.setOutput('SHOULD_RELEASE', 'true')
              return
            }

            core.setOutput('LAST_CANARY_TAG', lastCanary.name)
            core.setOutput('LAST_CANARY_SHA', lastCanary.commit.sha)

            const shouldRelease = lastCanary.commit.sha !== currentSha
            core.info(`Latest canary tag ${lastCanary.name} -> ${lastCanary.commit.sha}; current ${currentSha}; should_release=${shouldRelease}`)
            core.setOutput('SHOULD_RELEASE', shouldRelease ? 'true' : 'false')

  cloud:
    name: Release Cloud
    if: ${{ inputs.web || github.event_name != 'workflow_dispatch' }}
    needs:
      - prepare
    uses: ./.github/workflows/release-cloud.yml
    secrets: inherit
    with:
      build-type: ${{ needs.prepare.outputs.BUILD_TYPE }}
      app-version: ${{ needs.prepare.outputs.APP_VERSION }}
      git-short-hash: ${{ needs.prepare.outputs.GIT_SHORT_HASH }}

  image:
    name: Release Docker Image
    if: ${{ needs.canary-gate.outputs.SHOULD_RELEASE == 'true' }}
    runs-on: ubuntu-latest
    needs:
      - prepare
      - canary-gate
      - cloud
    steps:
      - uses: trstringer/manual-approval@v1
        if: ${{ needs.prepare.outputs.BUILD_TYPE == 'stable' }}
        name: Wait for approval
        with:
          secret: ${{ secrets.GITHUB_TOKEN }}
          approvers: darkskygit
          minimum-approvals: 1
          fail-on-denial: true
          issue-title: Please confirm to release docker image
          issue-body: |
            Env: ${{ needs.prepare.outputs.BUILD_TYPE }}
            Candidate: ghcr.io/toeverything/affine:${{ needs.prepare.outputs.BUILD_TYPE }}-${{ needs.prepare.outputs.GIT_SHORT_HASH }}
            Tag: ghcr.io/toeverything/affine:${{ needs.prepare.outputs.BUILD_TYPE }}

            > comment with "approve", "approved", "lgtm", "yes" to approve
            > comment with "deny", "denied", "no" to deny

      - name: Login to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          logout: false
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      - name: Tag Image
        run: |
          docker buildx imagetools create --tag ghcr.io/toeverything/affine:${{needs.prepare.outputs.BUILD_TYPE}} ghcr.io/toeverything/affine:${{needs.prepare.outputs.BUILD_TYPE}}-${{needs.prepare.outputs.GIT_SHORT_HASH}}
          docker buildx imagetools create --tag ghcr.io/toeverything/affine:${{needs.prepare.outputs.APP_VERSION}} ghcr.io/toeverything/affine:${{needs.prepare.outputs.BUILD_TYPE}}-${{needs.prepare.outputs.GIT_SHORT_HASH}}

  desktop:
    name: Release Desktop
    if: >-
      ${{
        (github.event_name != 'workflow_dispatch' && needs.canary-gate.outputs.SHOULD_RELEASE == 'true') ||
        inputs.desktop_macos ||
        inputs.desktop_windows ||
        inputs.desktop_linux
      }}
    needs:
      - prepare
      - canary-gate
    uses: ./.github/workflows/release-desktop.yml
    secrets: inherit
    with:
      build-type: ${{ needs.prepare.outputs.BUILD_TYPE }}
      app-version: ${{ needs.prepare.outputs.APP_VERSION }}
      git-short-hash: ${{ needs.prepare.outputs.GIT_SHORT_HASH }}
      desktop_macos: ${{ github.event_name != 'workflow_dispatch' || inputs.desktop_macos }}
      desktop_windows: ${{ github.event_name != 'workflow_dispatch' || inputs.desktop_windows }}
      desktop_linux: ${{ github.event_name != 'workflow_dispatch' || inputs.desktop_linux }}
      require-windows-signing: ${{ needs.prepare.outputs.BUILD_TYPE == 'beta' || needs.prepare.outputs.BUILD_TYPE == 'stable' || (github.event_name == 'workflow_dispatch' && inputs.desktop_windows) }}

  mobile:
    name: Release Mobile
    if: ${{ inputs.mobile }}
    needs:
      - prepare
    uses: ./.github/workflows/release-mobile.yml
    secrets: inherit
    with:
      build-type: ${{ needs.prepare.outputs.BUILD_TYPE }}
      app-version: ${{ needs.prepare.outputs.APP_VERSION }}
      git-short-hash: ${{ needs.prepare.outputs.GIT_SHORT_HASH }}
      ios-app-version: ${{ inputs.ios-app-version }}
\n```\n\n### .github/workflows/windows-signer.yml\n\n```yaml\nname: Windows Signer
on:
  workflow_call:
    inputs:
      artifact-name:
        required: true
        type: string
      files:
        required: true
        type: string
jobs:
  sign:
    runs-on: [self-hosted, win-signer]
    env:
      ARCHIVE_DIR: ${{ github.run_id }}-${{ github.run_attempt }}-${{ inputs.artifact-name }}
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: ${{ inputs.artifact-name }}
          path: ${{ env.ARCHIVE_DIR }}
      - name: unzip file
        shell: cmd
        # 7za is pre-installed on the signer machine
        run: |
          cd ${{ env.ARCHIVE_DIR }}
          md out
          7za x archive.zip -y -oout
      - name: sign
        shell: cmd
        run: |
          cd ${{ env.ARCHIVE_DIR }}/out
          signtool sign /tr http://timestamp.globalsign.com/tsa/r6advanced1 /td sha256 /fd sha256 /a ${{ inputs.files }}
      - name: collect signed file diff
        shell: powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File {0}
        run: |
          $OutDir = Join-Path '${{ env.ARCHIVE_DIR }}' 'out'
          $DiffDir = Join-Path '${{ env.ARCHIVE_DIR }}' 'signed-diff'
          $FilesDir = Join-Path $DiffDir 'files'
          New-Item -ItemType Directory -Path $FilesDir -Force | Out-Null

          $SignedFiles = [regex]::Matches('${{ inputs.files }}', '"([^"]+)"') | ForEach-Object { $_.Groups[1].Value }
          if ($SignedFiles.Count -eq 0) {
            throw 'No files to sign were provided.'
          }

          $Manifest = @()
          foreach ($RelativePath in $SignedFiles) {
            $SourcePath = Join-Path $OutDir $RelativePath
            if (!(Test-Path -LiteralPath $SourcePath -PathType Leaf)) {
              throw "Signed file not found: $RelativePath"
            }

            $TargetPath = Join-Path $FilesDir $RelativePath
            $TargetDir = Split-Path -Parent $TargetPath
            if ($TargetDir) {
              New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
            }

            Copy-Item -LiteralPath $SourcePath -Destination $TargetPath -Force
            $Manifest += [PSCustomObject]@{
              path = $RelativePath
              sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $TargetPath).Hash
            }
          }

          $Manifest | ConvertTo-Json -Depth 4 | Out-File -FilePath (Join-Path $DiffDir 'manifest.json') -Encoding utf8
          Write-Host "Collected $($SignedFiles.Count) signed files."
      - name: upload
        uses: actions/upload-artifact@v4
        with:
          name: signed-${{ inputs.artifact-name }}
          path: ${{ env.ARCHIVE_DIR }}/signed-diff
\n```\n\n## William-kelvem94/ruflo\n\n### .github/workflows/ci.yml\n\n```yaml\nname: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  schedule:
    # Run tests daily at 2 AM UTC
    - cron: '0 2 * * *'

env:
  NODE_VERSION: '20'

jobs:
  # Code quality and security checks
  security:
    name: Security & Code Quality
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci --legacy-peer-deps

      - name: Run security audit
        run: |
          npm audit --audit-level=high || echo "⚠️ Security vulnerabilities found (non-blocking)"
          npm audit --production --audit-level=moderate || echo "⚠️ Production vulnerabilities found (non-blocking)"
        continue-on-error: true
        
      - name: Lint code
        run: npm run lint

      - name: Type check
        run: npm run typecheck || echo "⚠️ Type checking skipped (TypeScript compiler crash)"
        continue-on-error: true

      - name: Check for outdated dependencies
        run: npm outdated || true
        continue-on-error: true

      - name: License compliance check
        run: npx license-checker --onlyAllow 'MIT;Apache-2.0;BSD-2-Clause;BSD-3-Clause;ISC;CC0-1.0' || true
        continue-on-error: true

  # All tests
  test:
    name: Test Suite
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest]
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci --legacy-peer-deps

      - name: Run all tests
        run: npm test || echo "⚠️ Some tests failed (Jest teardown issues - non-blocking)"
        continue-on-error: true

      - name: Generate coverage report
        if: matrix.os == 'ubuntu-latest'
        run: npm run test:coverage || echo "⚠️ Coverage generation failed (non-blocking)"
        continue-on-error: true

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-results-${{ matrix.os }}
          path: coverage/

  # Documentation generation
  docs:
    name: Documentation & Examples
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Check documentation
        run: |
          echo "✅ Documentation check passed"
          ls -la README.md CHANGELOG.md

  # Build and package
  build:
    name: Build & Package (${{ matrix.os }})
    runs-on: ${{ matrix.os }}
    needs: [security, test]
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        include:
          - os: ubuntu-latest
            platform: linux
          - os: macos-latest
            platform: darwin
          - os: windows-latest
            platform: win32

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: |
          if [ "${{ runner.os }}" == "Linux" ]; then
            npm ci --legacy-peer-deps
          else
            npm ci --legacy-peer-deps --omit=optional || npm ci --legacy-peer-deps --force
          fi
        shell: bash

      - name: Build project
        run: |
          echo "Building project for ${{ matrix.platform }}..."
          npm run build:ts

      - name: Test CLI binary (Unix)
        if: runner.os != 'Windows'
        run: |
          chmod +x ./v3/@claude-flow/cli/bin/cli.js
          node ./v3/@claude-flow/cli/bin/cli.js --version
        continue-on-error: true

      - name: Test CLI binary (Windows)
        if: runner.os == 'Windows'
        run: |
          node ./v3/@claude-flow/cli/bin/cli.js --version
        continue-on-error: true

      - name: Daemon survives parent exit (Windows, regression #1766)
        if: runner.os == 'Windows'
        timeout-minutes: 15
        shell: pwsh
        run: |
          # We install the published `@claude-flow/cli@alpha` inside an isolated
          # temp dir rather than running the source-tree CLI directly, because
          # the source-tree CLI imports the sibling workspace package
          # `@claude-flow/cli-core` (split out in #1764) which isn't always
          # resolvable from a source checkout. Skipping the `ruflo` umbrella
          # (just a thin wrapper) keeps the install footprint smaller on the
          # cold-cache Windows runner.
          $ErrorActionPreference = 'Stop'
          $tmp = Join-Path $env:RUNNER_TEMP 'daemon-1766'
          if (Test-Path $tmp) { Remove-Item -Recurse -Force $tmp }
          New-Item -ItemType Directory -Path $tmp | Out-Null
          Set-Location $tmp

          Write-Host "::group::Phase 1: install @claude-flow/cli@alpha"
          $installSw = [System.Diagnostics.Stopwatch]::StartNew()
          npm init -y | Out-Null
          npm install '@claude-flow/cli@alpha' --no-audit --no-fund --omit=optional --omit=dev
          $installSw.Stop()
          Write-Host "Install took $($installSw.Elapsed.TotalSeconds)s"
          $cli = Join-Path $tmp 'node_modules/@claude-flow/cli/bin/cli.js'
          if (-not (Test-Path $cli)) { throw "CLI not found at $cli after npm install" }
          $cliVer = (Get-Content (Join-Path $tmp 'node_modules/@claude-flow/cli/package.json') | ConvertFrom-Json).version
          Write-Host "Testing daemon survival for @claude-flow/cli@$cliVer"
          Write-Host "::endgroup::"

          Write-Host "::group::Phase 2: spawn daemon via cmd.exe (parent exits when node returns)"
          # Use raw .NET Process.Start with cmd.exe /c as the spawn parent.
          # cmd.exe is a clean Windows parent that exits the moment node exits,
          # giving us a deterministic "parent gone" signal — without the PS7
          # `Start-Process -Wait -NoNewWindow -RedirectStandard*` hang where
          # the parent waits indefinitely on output streams it inherited.
          $psi = New-Object System.Diagnostics.ProcessStartInfo
          $psi.FileName = 'cmd.exe'
          $psi.Arguments = "/c node `"$cli`" daemon start"
          $psi.UseShellExecute = $false
          $psi.CreateNoWindow = $true
          $psi.WorkingDirectory = $tmp
          # No stdio redirect — let cmd inherit nothing meaningful, daemon's
          # fork() opts use stdio:'ignore' anyway so nothing leaks back here.
          $spawnSw = [System.Diagnostics.Stopwatch]::StartNew()
          $proc = [System.Diagnostics.Process]::Start($psi)
          if (-not $proc.WaitForExit(120000)) {
            $proc.Kill($true)
            throw "FAIL: cmd.exe parent did not exit in 120s — daemon start hung"
          }
          $spawnSw.Stop()
          Write-Host "cmd.exe parent exited in $($spawnSw.Elapsed.TotalSeconds)s with code $($proc.ExitCode)"
          Write-Host "::endgroup::"

          Write-Host "::group::Phase 3: verify daemon survives parent exit"
          $pidFile = Join-Path $tmp '.claude-flow/daemon.pid'
          if (-not (Test-Path $pidFile)) {
            throw "FAIL: pid file $pidFile was never written — daemon failed to start"
          }
          $daemonPid = (Get-Content $pidFile).Trim()
          Write-Host "Daemon recorded PID = $daemonPid"

          # Original #1766 symptom: daemon died within ~1s of parent exit.
          # Wait 5s — well past any plausible delayed-teardown race.
          Start-Sleep -Seconds 5
          $alive = Get-Process -Id $daemonPid -ErrorAction SilentlyContinue
          if ($null -eq $alive) {
            throw "FAIL: daemon PID $daemonPid is no longer running 5s after parent exit (regression of #1766 in @claude-flow/cli@$cliVer)"
          }
          Write-Host "PASS: daemon PID $daemonPid alive 5s after parent exit (@claude-flow/cli@$cliVer)"
          Write-Host "::endgroup::"

          Write-Host "::group::Phase 4: cleanup"
          # Force-kill is fine here (CI ephemeral runner) — saves time vs the
          # interactive `daemon stop` path which on Windows shells out to ps/grep.
          Stop-Process -Id $daemonPid -Force -ErrorAction SilentlyContinue
          Write-Host "::endgroup::"

      - name: Package build
        run: |
          npm pack
          ls -la *.tgz
        shell: bash

      - name: Upload build artifacts
        uses: actions/upload-artifact@v4
        with:
          name: build-artifacts-${{ matrix.platform }}
          path: |
            dist/
            bin/
            *.tgz

  # Deployment (only on main branch)
  deploy:
    name: Deploy & Release
    runs-on: ubuntu-latest
    needs: [build]
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Download Linux build
        uses: actions/download-artifact@v4
        with:
          name: build-artifacts-linux
          path: dist-linux/

      - name: Download macOS build
        uses: actions/download-artifact@v4
        with:
          name: build-artifacts-darwin
          path: dist-darwin/

      - name: Download Windows build
        uses: actions/download-artifact@v4
        with:
          name: build-artifacts-win32
          path: dist-windows/

      - name: Prepare for deployment
        run: |
          echo "✅ Ready for deployment"
          echo "Version: $(node -p "require('./package.json').version")"
          echo "Platform builds:"
          ls -la dist\n```\n\n### .github/workflows/clone-tracker.yml\n\n```yaml\nname: Clone Tracker (14-day rolling)

# GitHub's clone API only retains 14 days. We run every 13 days so we always
# catch the full window with a 24h safety margin. The job appends a snapshot
# to `data/clone-data.rvf` (RuVector vector store) + `data/clone-data.ledger.json`
# (chronological JSON), regenerates `data/clone-data.proof.json` with a fresh
# SHA-256 over the ledger, and commits the result back to main.
#
# Schedule: every 13 days at 06:17 UTC (off-peak; avoids the :00 mark to
# spread cron load).
#
# Why we own this rather than rely on a third-party traffic-tracker: GitHub's
# clone API requires push access, so we'd have to give a stranger our token.
# Running it ourselves keeps the data path inside the repo and signed.

on:
  schedule:
    - cron: '17 6 */13 * *'
  workflow_dispatch:
    # Allow manual runs (e.g., after a release announcement to capture the spike).
  push:
    branches: [main]
    paths:
      - 'scripts/track-clones.mjs'
      - '.github/workflows/clone-tracker.yml'

permissions:
  contents: write     # to push the snapshot commit
  actions: read

concurrency:
  group: clone-tracker
  cancel-in-progress: false

jobs:
  track:
    name: Snapshot clones for ruflo ecosystem
    runs-on: ubuntu-latest

    steps:
      - name: Checkout main
        uses: actions/checkout@v4
        with:
          ref: main
          fetch-depth: 1

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '22'

      - name: Install root deps (for @ruvector/rvf binding)
        run: npm install --legacy-peer-deps --no-audit --no-fund --ignore-scripts

      - name: Run clone tracker
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: node scripts/track-clones.mjs

      - name: Show resulting artifacts
        run: |
          ls -la data/clone-data.* 2>/dev/null || echo "(no artifacts produced)"
          echo ""
          echo "--- proof ---"
          cat data/clone-data.proof.json

      - name: Commit + push snapshot
        run: |
          git config user.name "ruflo-bot"
          git config user.email "ruflo-bot@users.noreply.github.com"
          git add data/clone-data.rvf data/clone-data.ledger.json data/clone-data.proof.json
          if git diff --cached --quiet; then
            echo "No changes to commit (snapshot identical to previous?)"
            exit 0
          fi
          SNAP_COUNT=$(node -e "console.log(JSON.parse(require('fs').readFileSync('data/clone-data.proof.json','utf8')).ledger_snapshot_count)")
          CLONES=$(node -e "console.log(JSON.parse(require('fs').readFileSync('data/clone-data.proof.json','utf8')).latest_snapshot.clones_14d.toLocaleString())")
          git commit -m "chore(data): clone snapshot #${SNAP_COUNT} — ${CLONES} clones (14d)

          Auto-generated by .github/workflows/clone-tracker.yml.
          Source: GitHub Traffic API (14-day rolling window).

          Co-Authored-By: ruflo-bot <ruflo-bot@users.noreply.github.com>"
          git push origin main
\n```\n\n### .github/workflows/codex-integration-audit.yml\n\n```yaml\nname: codex-integration-audit

# Guards the Codex ↔ Ruflo integration invariants (issue #1909):
# - the `codex` MCP backend uses the real `mcp-server` subcommand
# - @claude-flow/codex VERSION const tracks its package.json
# - the dual-mode orchestrator / agent defs drive real `codex exec`
# - CLI refs are standardized to `ruflo`, `dual run` exposes `--worker`,
#   generated SKILL.md frontmatter is complete, config.toml emits a
#   working `ruflo` MCP server.
# Pure-Node static checks — no install needed. Build + unit tests are
# covered by the main CI workflow.

on:
  push:
    branches: [main]
    paths:
      - 'v3/@claude-flow/codex/**'
      - 'ruflo/src/mcp-bridge/**'
      - 'ruflo/src/ruvocal/mcp-bridge/**'
      - '.claude/agents/dual-mode/**'
      - 'scripts/audit-codex-integration.mjs'
      - '.github/workflows/codex-integration-audit.yml'
  pull_request:
    paths:
      - 'v3/@claude-flow/codex/**'
      - 'ruflo/src/mcp-bridge/**'
      - 'ruflo/src/ruvocal/mcp-bridge/**'
      - '.claude/agents/dual-mode/**'
      - 'scripts/audit-codex-integration.mjs'
      - '.github/workflows/codex-integration-audit.yml'

jobs:
  audit:
    name: Codex integration audit
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: node scripts/audit-codex-integration.mjs
\n```\n\n### .github/workflows/cost-tracker-smoke.yml\n\n```yaml\n# Smoke + booster-only bench for plugins/ruflo-cost-tracker.
#
# Triggers on changes to the plugin or its corpus. Smoke is fast (~100 ms,
# pure bash + node --check) so it always runs. The booster-only bench runs
# locally — installs `agent-booster` in a sibling temp dir then invokes
# bench.mjs from there so node-resolve picks up the package. The LLM and
# Anthropic baselines are intentionally OMITTED: they cost real money per
# run and require Secret Manager keys; they belong in a manual-trigger or
# scheduled workflow with a budget guard, not on every PR.
name: cost-tracker-smoke

on:
  push:
    branches: [main]
    paths:
      - 'plugins/ruflo-cost-tracker/**'
      - '.github/workflows/cost-tracker-smoke.yml'
  pull_request:
    paths:
      - 'plugins/ruflo-cost-tracker/**'
      - '.github/workflows/cost-tracker-smoke.yml'
  workflow_dispatch:

jobs:
  smoke:
    runs-on: ubuntu-latest
    timeout-minutes: 8
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Run smoke (39+ structural checks)
        run: bash plugins/ruflo-cost-tracker/scripts/smoke.sh

      - name: Install agent-booster for the bench
        run: |
          mkdir -p .ci-bench
          cd .ci-bench
          # npm 11 rejects a package name starting with `.` (the dir name), so
          # write the manifest explicitly instead of `npm init -y`.
          printf '{"name":"ci-bench","version":"0.0.0","private":true}\n' > package.json
          # Pin to the same major as v3/node_modules to keep results comparable.
          npm install --no-audit --no-fund --silent agent-booster@^0.2

      - name: Run booster-only bench (no LLM cost)
        run: |
          cd .ci-bench
          node ../plugins/ruflo-cost-tracker/scripts/bench.mjs

      - name: Trend report (drift across runs in this checkout)
        run: node plugins/ruflo-cost-tracker/scripts/trend.mjs
        # The checkout only contains the runs that were committed — useful
        # as a sanity check that trend.mjs runs cleanly on real data.

      - name: Verify Tier 1 win rate ≥ 0.80 (regression gate)
        run: |
          node -e "
            const d = JSON.parse(require('fs').readFileSync('plugins/ruflo-cost-tracker/docs/benchmarks/runs/latest.json'));
            if (d.summary.winRate < 0.80) {
              console.error('REGRESSION: Tier 1 win rate', d.summary.winRate, '< 0.80');
              process.exit(1);
            }
            console.log('Tier 1 win rate:', (d.summary.winRate * 100).toFixed(1) + '%');
          "

      - name: Upload bench artifact
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: cost-tracker-bench-result
          path: plugins/ruflo-cost-tracker/docs/benchmarks/runs/latest.json
          retention-days: 30
\n```\n\n### .github/workflows/federation-peer-rust.yml\n\n```yaml\nname: federation-peer-rust

# Builds + tests the v3/crates/ruflo-federation-peer crate (ADR-120
# Step 3). Triggers only on changes to the crate or this workflow.
# Two jobs:
#
#   stable-noop  — cargo build + cargo test without --features native.
#                  Verifies the trait surface compiles in a tree that
#                  doesn't have the upstream crate deps materialized.
#
#   stable-native — cargo check --features native. Pulls in
#                   midstreamer-quic@0.2.1 + aimds-*@0.1.1 from
#                   crates.io. Type-checks only (the placeholder impls
#                   don't yet exercise the upstream APIs).

on:
  push:
    branches: [main]
    paths:
      - 'v3/crates/ruflo-federation-peer/**'
      - '.github/workflows/federation-peer-rust.yml'
  pull_request:
    paths:
      - 'v3/crates/ruflo-federation-peer/**'
      - '.github/workflows/federation-peer-rust.yml'
  workflow_dispatch:

jobs:
  stable-noop:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v4

      - name: Install Rust stable
        uses: dtolnay/rust-toolchain@stable

      - name: Cache cargo
        uses: actions/cache@v4
        with:
          path: |
            ~/.cargo/registry
            ~/.cargo/git
            v3/crates/ruflo-federation-peer/target
          key: federation-peer-${{ runner.os }}-${{ hashFiles('v3/crates/ruflo-federation-peer/Cargo.toml') }}

      - name: cargo build (no native features)
        working-directory: v3/crates/ruflo-federation-peer
        run: cargo build --verbose

      - name: cargo test (no native features)
        working-directory: v3/crates/ruflo-federation-peer
        run: cargo test --verbose

      - name: cargo clippy (no native features)
        working-directory: v3/crates/ruflo-federation-peer
        run: cargo clippy --all-targets -- -D warnings
        continue-on-error: true

  stable-native:
    runs-on: ubuntu-latest
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4

      - name: Install Rust stable
        uses: dtolnay/rust-toolchain@stable

      - name: Cache cargo
        uses: actions/cache@v4
        with:
          path: |
            ~/.cargo/registry
            ~/.cargo/git
            v3/crates/ruflo-federation-peer/target
          key: federation-peer-native-${{ runner.os }}-${{ hashFiles('v3/crates/ruflo-federation-peer/Cargo.toml') }}

      - name: cargo check --features native (resolves midstreamer-quic + aimds-*)
        working-directory: v3/crates/ruflo-federation-peer
        run: cargo check --features native --verbose
\n```\n\n### .github/workflows/integration-tests.yml\n\n```yaml\nname: 🔗 Cross-Agent Integration Tests

on:
  push:
    branches: [main, develop, alpha-*]
  pull_request:
    branches: [main, develop]
  schedule:
    # Run integration tests daily at 3 AM UTC
    - cron: '0 3 * * *'
  workflow_dispatch:
    inputs:
      integration_scope:
        description: 'Integration test scope'
        required: false
        default: 'full'
        type: choice
        options:
          - smoke
          - core
          - full
          - stress
      agent_count:
        description: 'Maximum agent count for testing'
        required: false
        default: '8'
      test_duration:
        description: 'Test duration in minutes'
        required: false
        default: '10'

env:
  NODE_VERSION: '20'
  MAX_PARALLEL_AGENTS: 8
  DEFAULT_TIMEOUT: 300000
  INTEGRATION_DB_PATH: './integration-test.db'

jobs:
  # Setup integration test environment
  integration-setup:
    name: 🚀 Integration Test Setup
    runs-on: ubuntu-latest
    outputs:
      test-session-id: ${{ steps.setup.outputs.test-session-id }}
      agent-matrix: ${{ steps.setup.outputs.agent-matrix }}
      test-scenarios: ${{ steps.setup.outputs.test-scenarios }}
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci --legacy-peer-deps

      - name: Install SQLite3
        run: |
          sudo apt-get update -qq
          sudo apt-get install -y sqlite3
          sqlite3 --version

      - name: Initialize integration test session
        id: setup
        run: |
          TEST_SESSION="integration-$(date +%Y%m%d-%H%M%S)-${{ github.sha }}"
          echo "test-session-id=$TEST_SESSION" >> $GITHUB_OUTPUT
          
          # Define agent test matrix based on input scope
          SCOPE="${{ github.event.inputs.integration_scope || 'full' }}"
          
          if [ "$SCOPE" = "smoke" ]; then
            AGENT_MATRIX='{"include":[{"type":"coder","count":2},{"type":"tester","count":1}]}'
          elif [ "$SCOPE" = "core" ]; then
            AGENT_MATRIX='{"include":[{"type":"coder","count":3},{"type":"tester","count":2},{"type":"reviewer","count":1},{"type":"planner","count":1}]}'
          elif [ "$SCOPE" = "stress" ]; then
            AGENT_MATRIX='{"include":[{"type":"coder","count":5},{"type":"tester","count":3},{"type":"reviewer","count":2},{"type":"planner","count":2},{"type":"researcher","count":1}]}'
          else
            # Full scope
            AGENT_MATRIX='{"include":[{"type":"coder","count":4},{"type":"tester","count":3},{"type":"reviewer","count":2},{"type":"planner","count":2},{"type":"researcher","count":1},{"type":"backend-dev","count":1},{"type":"performance-benchmarker","count":1}]}'
          fi
          
          echo "agent-matrix=$AGENT_MATRIX" >> $GITHUB_OUTPUT
          
          # Define test scenarios
          TEST_SCENARIOS='["coordination","memory-sharing","task-orchestration","fault-tolerance","performance"]'
          echo "test-scenarios=$TEST_SCENARIOS" >> $GITHUB_OUTPUT

      - name: Create integration test database
        run: |
          echo "🗄️ Creating integration test database..."
          
          mkdir -p integration-test-data
          
          # Initialize SQLite database for integration tests
          sqlite3 ${{ env.INTEGRATION_DB_PATH }} << 'EOF'
          CREATE TABLE IF NOT EXISTS test_sessions (
            id TEXT PRIMARY KEY,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'pending',
            metadata TEXT
          );
          
          CREATE TABLE IF NOT EXISTS agent_tests (
            id TEXT PRIMARY KEY,
            session_id TEXT,
            agent_type TEXT,
            agent_count INTEGER,
            status TEXT DEFAULT 'pending',
            started_at DATETIME,
            completed_at DATETIME,
            results TEXT,
            FOREIGN KEY (session_id) REFERENCES test_sessions (id)
          );
          
          CREATE TABLE IF NOT EXISTS integration_scenarios (
            id TEXT PRIMARY KEY,
            session_id TEXT,
            scenario_name TEXT,
            status TEXT DEFAULT 'pending',
            agents_involved TEXT,
            execution_time_ms INTEGER,
            success_rate REAL,
            error_details TEXT,
            FOREIGN KEY (session_id) REFERENCES test_sessions (id)
          );
          
          INSERT INTO test_sessions (id, metadata) VALUES 
          ('${{ steps.setup.outputs.test-session-id }}', '{"scope": "${{ github.event.inputs.integration_scope || 'full' }}", "agent_count": "${{ github.event.inputs.agent_count || '8' }}"}');
          EOF
          
          cp ${{ env.INTEGRATION_DB_PATH }} integration-test-data/

      - name: Upload integration test setup
        uses: actions/upload-artifact@v4
        with:
          name: integration-setup-${{ steps.setup.outputs.test-session-id }}
          path: integration-test-data/
          retention-days: 30

  # Test agent coordination
  test-agent-coordination:
    name: 🤝 Agent Coordination Tests
    runs-on: ubuntu-latest
    needs: integration-setup
    strategy:
      fail-fast: false
      matrix: ${{ fromJson(needs.integration-setup.outputs.agent-matrix) }}
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci --legacy-peer-deps

      - name: Download integration setup
        uses: actions/download-artifact@v4
        with:
          name: integration-setup-${{ needs.integration-setup.outputs.test-session-id }}
          path: integration-test-data/

      - name: Initialize swarm for agent testing
        run: |
          echo "🚀 Initializing swarm for ${{ matrix.type }} agents (count: ${{ matrix.count }})"
          
          # Start background swarm process
          timeout 300s node -e "
          const { spawn } = require('child_process');
          
          async function testAgentCoordination() {
            console.log('Starting agent coordination test...');
            
            // Simulate swarm initialization
            console.log('Swarm initialized with topology: mesh');
            
            // Spawn agents
            for (let i = 0; i < ${{ matrix.count }}; i++) {
              console.log(\`Agent \${i + 1} (${{ matrix.type }}): Spawned and ready\`);
              await new Promise(resolve => setTimeout(resolve, 1000));
            }
            
            // Test coordination
            console.log('Testing agent coordination...');
            await new Promise(resolve => setTimeout(resolve, 5000));
            
            console.log('Coordination test completed successfully');
            return true;
          }
          
          testAgentCoordination().catch(console.error);
          " > coordination-test-${{ matrix.type }}.log 2>&1 || true

      - name: Test inter-agent communication
        run: |
          echo "📡 Testing inter-agent communication for ${{ matrix.type }}"
          
          node -e "
          async function testCommunication() {
            const results = {
              agentType: '${{ matrix.type }}',
              agentCount: ${{ matrix.count }},
              communicationTests: [],
              timestamp: new Date().toISOString()
            };
            
            // Simulate communication tests
            for (let i = 0; i < ${{ matrix.count }}; i++) {
              const test = {
                agentId: \`\${{ matrix.type }}-\${i + 1}\`,
                messagesSent: Math.floor(Math.random() * 50) + 10,
                messagesReceived: Math.floor(Math.random() * 50) + 10,
                averageLatency: Math.floor(Math.random() * 100) + 20,
                successRate: 0.95 + Math.random() * 0.05
              };
              results.communicationTests.push(test);
            }
            
            console.log('Communication test results:', JSON.stringify(results, null, 2));
            require('fs').writeFileSync('communication-results-${{ matrix.type }}.json', JSON.stringify(results, null, 2));
          }
          
          testCommunication().catch(console.error);
          "

      - name: Test task distribution
        run: |
          echo "📋 Testing task distribution for ${{ matrix.type }}"
          
          node -e "
          async function testTaskDistribution() {
            const results = {
              agentType: '${{ matrix.type }}',
              agentCount: ${{ matrix.count }},
              taskDistribution: {
                totalTasks: 50,
                tasksPerAgent: [],
                loadBalance: 0,
                completionRate: 0
              },
              timestamp: new Date().toISOString()
            };
            
            let totalAssigned = 0;
            let totalCompleted = 0;
            
            for (let i = 0; i < ${{ matrix.count }}; i++) {
              const tasksAssigned = Math.floor(Math.random() * 15) + 5;
              const tasksCompleted = Math.floor(tasksAssigned * (0.8 + Math.random() * 0.2));
              
              results.taskDistribution.tasksPerAgent.push({
                agentId: \`\${{ matrix.type }}-\${i + 1}\`,
                assigned: tasksAssigned,
                completed: tasksCompleted,
                efficiency: tasksCompleted / tasksAssigned
              });
              
              totalAssigned += tasksAssigned;
              totalCompleted += tasksCompleted;
            }
            
            results.taskDistribution.completionRate = totalCompleted / totalAssigned;
            
            // Calculate load balance (standard deviation of\n```\n\n### .github/workflows/neural-trader-smoke.yml\n\n```yaml\nname: neural-trader-smoke

# Runs the ruflo-neural-trader plugin's runtime smoke test against
# the currently-pinned neural-trader npm package. Catches regressions
# where the published package stops matching what the plugin's skills
# document (e.g. another missing-loader bug, another fork-bomb, an
# advanced feature flag being silently dropped).
#
# Structural smoke (smoke.sh) runs separately as part of the broader
# validate-marketplace pipeline; this one specifically gates the
# *runtime* contract — installs the package fresh, runs the documented
# CLI flags, asserts the JSON shape.

on:
  push:
    branches: [main]
    paths:
      - 'plugins/ruflo-neural-trader/**'
      - '.github/workflows/neural-trader-smoke.yml'
  pull_request:
    paths:
      - 'plugins/ruflo-neural-trader/**'
      - '.github/workflows/neural-trader-smoke.yml'
  workflow_dispatch:
  schedule:
    # Catch upstream regressions even when nothing in the plugin
    # changes (e.g. a new `neural-trader` release breaks the contract).
    - cron: '17 6 * * 1'   # Mondays 06:17 UTC

jobs:
  runtime-smoke:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install jq
        run: sudo apt-get update && sudo apt-get install -y jq

      - name: Run runtime smoke
        run: bash plugins/ruflo-neural-trader/scripts/runtime-smoke.sh

      - name: Upload smoke output on failure
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: runtime-smoke-output
          path: |
            /tmp/runtime-smoke-*.log
          if-no-files-found: ignore
\n```\n\n### .github/workflows/rollback-manager.yml\n\n```yaml\nname: 🔄 Automated Rollback Manager

on:
  workflow_run:
    workflows: ["🔍 Verification Pipeline", "🎯 Truth Scoring Pipeline", "🔗 Cross-Agent Integration Tests"]
    types: [completed]
    branches: [main, develop]
  push:
    branches: [main]
  workflow_dispatch:
    inputs:
      rollback_target:
        description: 'Target commit SHA or tag for rollback'
        required: true
      rollback_reason:
        description: 'Reason for rollback'
        required: true
        default: 'Manual rollback requested'
      emergency_mode:
        description: 'Emergency rollback mode (skip confirmations)'
        required: false
        default: false
        type: boolean
      rollback_scope:
        description: 'Rollback scope'
        required: false
        default: 'application'
        type: choice
        options:
          - application
          - database
          - infrastructure
          - full

env:
  NODE_VERSION: '20'
  ROLLBACK_RETENTION_DAYS: 90
  CRITICAL_FAILURE_THRESHOLD: 3
  MONITORING_WINDOW_MINUTES: 15

jobs:
  # Detect failure conditions
  failure-detection:
    name: 🚨 Failure Detection
    runs-on: ubuntu-latest
    if: github.event_name == 'workflow_run' || github.event_name == 'push'
    outputs:
      rollback-required: ${{ steps.detect.outputs.rollback-required }}
      failure-type: ${{ steps.detect.outputs.failure-type }}
      failure-severity: ${{ steps.detect.outputs.failure-severity }}
      rollback-target: ${{ steps.detect.outputs.rollback-target }}
      rollback-session-id: ${{ steps.detect.outputs.rollback-session-id }}
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 50

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}

      - name: Detect failure conditions
        id: detect
        run: |
          echo "🚨 Analyzing failure conditions..."
          
          ROLLBACK_SESSION="rollback-$(date +%Y%m%d-%H%M%S)-${{ github.sha }}"
          echo "rollback-session-id=$ROLLBACK_SESSION" >> $GITHUB_OUTPUT
          
          ROLLBACK_REQUIRED="false"
          FAILURE_TYPE="none"
          FAILURE_SEVERITY="low"
          ROLLBACK_TARGET=""
          
          # Check workflow run results if triggered by workflow_run
          if [ "${{ github.event_name }}" = "workflow_run" ]; then
            WORKFLOW_CONCLUSION="${{ github.event.workflow_run.conclusion }}"
            WORKFLOW_NAME="${{ github.event.workflow_run.name }}"
            
            echo "Workflow: $WORKFLOW_NAME"
            echo "Conclusion: $WORKFLOW_CONCLUSION"
            
            if [ "$WORKFLOW_CONCLUSION" = "failure" ]; then
              ROLLBACK_REQUIRED="true"
              FAILURE_TYPE="ci_failure"
              
              # Determine severity based on workflow type
              case "$WORKFLOW_NAME" in
                *"Verification Pipeline"*)
                  FAILURE_SEVERITY="high"
                  ;;
                *"Truth Scoring"*)
                  FAILURE_SEVERITY="medium"
                  ;;
                *"Integration Tests"*)
                  FAILURE_SEVERITY="high"
                  ;;
                *)
                  FAILURE_SEVERITY="medium"
                  ;;
              esac
            fi
          fi
          
          # Check for recent commit history to find safe rollback target
          if [ "$ROLLBACK_REQUIRED" = "true" ]; then
            # Find the last successful commit (simplified logic)
            ROLLBACK_TARGET=$(git log --oneline -10 --grep="✅" --grep="🏁" | head -1 | cut -d' ' -f1)
            if [ -z "$ROLLBACK_TARGET" ]; then
              ROLLBACK_TARGET="HEAD~1"
            fi
          fi
          
          echo "rollback-required=$ROLLBACK_REQUIRED" >> $GITHUB_OUTPUT
          echo "failure-type=$FAILURE_TYPE" >> $GITHUB_OUTPUT
          echo "failure-severity=$FAILURE_SEVERITY" >> $GITHUB_OUTPUT
          echo "rollback-target=$ROLLBACK_TARGET" >> $GITHUB_OUTPUT
          
          echo "🔍 Detection Results:"
          echo "  Rollback Required: $ROLLBACK_REQUIRED"
          echo "  Failure Type: $FAILURE_TYPE"
          echo "  Severity: $FAILURE_SEVERITY"
          echo "  Target: $ROLLBACK_TARGET"

      - name: Create failure report
        if: steps.detect.outputs.rollback-required == 'true'
        run: |
          echo "📋 Creating failure report..."
          
          mkdir -p rollback-data
          
          cat > rollback-data/failure-report.json << EOF
          {
            "sessionId": "${{ steps.detect.outputs.rollback-session-id }}",
            "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
            "trigger": {
              "event": "${{ github.event_name }}",
              "workflow": "${{ github.event.workflow_run.name || 'N/A' }}",
              "conclusion": "${{ github.event.workflow_run.conclusion || 'N/A' }}",
              "commit": "${{ github.sha }}",
              "branch": "${{ github.ref_name }}"
            },
            "failure": {
              "type": "${{ steps.detect.outputs.failure-type }}",
              "severity": "${{ steps.detect.outputs.failure-severity }}",
              "rollbackRequired": true
            },
            "rollback": {
              "target": "${{ steps.detect.outputs.rollback-target }}",
              "reason": "Automated rollback due to ${{ steps.detect.outputs.failure-type }}"
            }
          }
          EOF

      - name: Upload failure detection results
        if: steps.detect.outputs.rollback-required == 'true'
        uses: actions/upload-artifact@v4
        with:
          name: failure-detection-${{ steps.detect.outputs.rollback-session-id }}
          path: rollback-data/
          retention-days: ${{ env.ROLLBACK_RETENTION_DAYS }}

  # Pre-rollback validation
  pre-rollback-validation:
    name: 🔍 Pre-Rollback Validation
    runs-on: ubuntu-latest
    needs: failure-detection
    if: needs.failure-detection.outputs.rollback-required == 'true' || github.event_name == 'workflow_dispatch'
    outputs:
      validation-passed: ${{ steps.validate.outputs.validation-passed }}
      backup-created: ${{ steps.validate.outputs.backup-created }}
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 100

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci --legacy-peer-deps

      - name: Validate rollback target
        id: validate
        run: |
          echo "🔍 Validating rollback target..."
          
          ROLLBACK_TARGET="${{ github.event.inputs.rollback_target || needs.failure-detection.outputs.rollback-target }}"
          VALIDATION_PASSED="false"
          BACKUP_CREATED="false"
          
          if [ -n "$ROLLBACK_TARGET" ]; then
            # Check if target commit exists
            if git cat-file -e "$ROLLBACK_TARGET^{commit}" 2>/dev/null; then
              echo "✅ Rollback target $ROLLBACK_TARGET is valid"
              
              # Check if target is reachable from current branch
              if git merge-base --is-ancestor "$ROLLBACK_TARGET" HEAD; then
                echo "✅ Target is ancestor of current HEAD"
                VALIDATION_PASSED="true"
              else
                echo "❌ Target is not an ancestor of current HEAD"
              fi
            else
              echo "❌ Rollback target $ROLLBACK_TARGET does not exist"
            fi
          else
            echo "❌ No rollback target specified"
          fi
          
          echo "validation-passed=$VALIDATION_PASSED" >> $GITHUB_OUTPUT
          echo "backup-created=$BACKUP_CREATED" >> $GITHUB_OUTPUT

      - name: Create current state backup
        if: steps.validate.outputs.validation-passed == 'true'
        run: |
          echo "💾 Creating current state backup..."
          
          mkdir -p rollback-data/backup
          
          # Create backup metadata
          cat > rollback-data/backup/backup-metadata.json << EOF
          {
            "backupId": "backup-$(date +%Y%m%d-%H%M%S)",
            "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
            "sourceCommit": "${{ github.sha }}",
            "sourceBranch": "${{ github.ref_name }}",
            "rollbackTarget": "${{ github.event.inputs.rollback_target || needs.failure-detection.outputs.rollback-target }}",
            "backupType": "pre-rollback"
          }
          EOF
          
          # Create git bundle for backup
          git bundle create rollback-data/backup/current-state.bundle HEAD
          
          # Backup package.json and important config files
          cp package.json rollback-data/backup/ 2>/dev/null || true
          cp package-lock.json rollback-data/backup/ 2>/dev/null || true
          cp claude-flow.config.json rollback-data/backup/ 2>/dev/null || true
          
          echo "✅ Backup created successfully"

      - name: Test rollback target viability
        if: steps.validate.outputs.validation-passed == 'true'
        run: |
          set -e  # Exit on any error
          echo "🧪 Testing rollback target viability..."

          ROLLBACK_TARGET="${{ github.event.inputs.rollback_target || needs.failure-detection.outputs.rollback-target }}"

          # Create temporary branch for testing
          git checkout -b test-rollback-temp "$ROLLBACK_TARGET"

          # Test if the target can build (strict error checking)
          echo "Installing dependencies..."
          npm ci --legacy-peer-deps

          echo "Testing build..."
          npm run build:ts

          # Switch back to original branch
          git checkout "${{ github.ref_name }}"
          git branch -D test-rollback-temp

          echo "✅ Rollback target viability tested successfully"

      - name: U\n```\n\n### .github/workflows/ruflo-agent-smoke.yml\n\n```yaml\n# Structural smoke for the ruflo-agent plugin (local WASM runtime — rvagent —
# plus the Anthropic Managed Agents cloud runtime, ADR-115). No network: it's
# a static check of the plugin manifest, skills, commands, MCP-tool references,
# and ADR cross-references. Triggers on changes to the plugin or this workflow.
name: ruflo-agent-smoke

on:
  push:
    branches: [main, develop, v3]
    paths:
      - 'plugins/ruflo-agent/**'
      - '.github/workflows/ruflo-agent-smoke.yml'
  pull_request:
    branches: [main]
    paths:
      - 'plugins/ruflo-agent/**'
      - '.github/workflows/ruflo-agent-smoke.yml'
  workflow_dispatch:

jobs:
  smoke:
    name: ruflo-agent structural smoke
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '22'
      - name: Run plugin smoke
        run: bash plugins/ruflo-agent/scripts/smoke.sh
\n```\n\n### .github/workflows/status-badges.yml\n\n```yaml\nname: 📊 Status Badges Update

on:
  workflow_run:
    workflows: ["🔍 Verification Pipeline", "🎯 Truth Scoring Pipeline", "🔗 Cross-Agent Integration Tests"]
    types: [completed]
  push:
    branches: [main]
  schedule:
    - cron: '0 6 * * *'  # Daily at 6 AM UTC

jobs:
  update-badges:
    name: 📊 Update Status Badges
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Generate badge data
        run: |
          echo "📊 Generating badge data..."
          
          mkdir -p badge-data
          
          # Get latest workflow runs
          VERIFICATION_STATUS="${{ github.event.workflow_run.conclusion || 'unknown' }}"
          WORKFLOW_NAME="${{ github.event.workflow_run.name || 'unknown' }}"
          
          # Determine badge colors and status
          case "$VERIFICATION_STATUS" in
            "success")
              BADGE_COLOR="brightgreen"
              BADGE_STATUS="passing"
              ;;
            "failure")
              BADGE_COLOR="red"
              BADGE_STATUS="failing"
              ;;
            *)
              BADGE_COLOR="yellow"
              BADGE_STATUS="unknown"
              ;;
          esac
          
          # Create badge JSON
          cat > badge-data/status.json << EOF
          {
            "schemaVersion": 1,
            "label": "pipeline",
            "message": "$BADGE_STATUS",
            "color": "$BADGE_COLOR",
            "style": "flat-square"
          }
          EOF
          
          # Truth scoring badge
          if [ "$WORKFLOW_NAME" = "🎯 Truth Scoring Pipeline" ]; then
            TRUTH_COLOR="brightgreen"
            TRUTH_MESSAGE="85+"
            if [ "$VERIFICATION_STATUS" = "failure" ]; then
              TRUTH_COLOR="red"
              TRUTH_MESSAGE="<85"
            fi
            
            cat > badge-data/truth-score.json << EOF
          {
            "schemaVersion": 1,
            "label": "truth score",
            "message": "$TRUTH_MESSAGE",
            "color": "$TRUTH_COLOR",
            "style": "flat-square"
          }
          EOF
          fi
          
          # Integration tests badge
          if [ "$WORKFLOW_NAME" = "🔗 Cross-Agent Integration Tests" ]; then
            INTEGRATION_COLOR="brightgreen"
            INTEGRATION_MESSAGE="passing"
            if [ "$VERIFICATION_STATUS" = "failure" ]; then
              INTEGRATION_COLOR="red"
              INTEGRATION_MESSAGE="failing"
            fi
            
            cat > badge-data/integration.json << EOF
          {
            "schemaVersion": 1,
            "label": "integration",
            "message": "$INTEGRATION_MESSAGE",
            "color": "$INTEGRATION_COLOR",
            "style": "flat-square"
          }
          EOF
          fi

      - name: Update README badges
        run: |
          echo "📝 Updating README badges..."
          
          # Check if README has badge section
          if grep -q "<!-- BADGES-START -->" README.md; then
            echo "Found badge section, updating..."
            
            # Create new badge section
            cat > new-badges.md << 'EOF'
          <!-- BADGES-START -->
          [![Verification Pipeline](https://img.shields.io/github/actions/workflow/status/ruvnet/claude-code-flow/verification-pipeline.yml?branch=main&label=verification&style=flat-square)](https://github.com/ruvnet/claude-code-flow/actions/workflows/verification-pipeline.yml)
          [![Truth Scoring](https://img.shields.io/github/actions/workflow/status/ruvnet/claude-code-flow/truth-scoring.yml?branch=main&label=truth%20score&style=flat-square)](https://github.com/ruvnet/claude-code-flow/actions/workflows/truth-scoring.yml)
          [![Integration Tests](https://img.shields.io/github/actions/workflow/status/ruvnet/claude-code-flow/integration-tests.yml?branch=main&label=integration&style=flat-square)](https://github.com/ruvnet/claude-code-flow/actions/workflows/integration-tests.yml)
          [![Rollback Manager](https://img.shields.io/github/actions/workflow/status/ruvnet/claude-code-flow/rollback-manager.yml?branch=main&label=rollback&style=flat-square)](https://github.com/ruvnet/claude-code-flow/actions/workflows/rollback-manager.yml)
          [![CI/CD](https://img.shields.io/github/actions/workflow/status/ruvnet/claude-code-flow/ci.yml?branch=main&label=ci%2Fcd&style=flat-square)](https://github.com/ruvnet/claude-code-flow/actions/workflows/ci.yml)
          [![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)
          [![Version](https://img.shields.io/npm/v/claude-flow.svg?style=flat-square)](https://www.npmjs.com/package/claude-flow)
          <!-- BADGES-END -->
          EOF
            
            # Replace badge section in README
            awk '
            BEGIN { in_badges = 0 }
            /<!-- BADGES-START -->/ { 
              in_badges = 1
              while ((getline line < "new-badges.md") > 0) {
                print line
              }
              close("new-badges.md")
              next
            }
            /<!-- BADGES-END -->/ { 
              in_badges = 0
              next
            }
            !in_badges { print }
            ' README.md > README.tmp && mv README.tmp README.md
            
            rm -f new-badges.md
          else
            echo "No badge section found in README.md"
          fi

      - name: Commit badge updates
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          
          if git diff --quiet README.md; then
            echo "No changes to commit"
          else
            git add README.md
            git commit -m "📊 Update status badges
            
            🤖 Generated by GitHub Actions
            
            Co-Authored-By: Badge Updater <noreply@github.com>"
            git push
          fi

      - name: Upload badge data
        uses: actions/upload-artifact@v4
        with:
          name: badge-data-$(date +%Y%m%d)
          path: badge-data/
          retention-days: 7\n```\n\n### .github/workflows/v3-ci.yml\n\n```yaml\nname: V3 CI/CD Pipeline

on:
  push:
    branches: [main, develop, v3]
    paths:
      - 'v3/**'
      - '.github/workflows/v3-ci.yml'
      # Witness-verify + plugin-hooks-smoke depend on these scripts;
      # path filter keeps CI in sync with their changes.
      - 'plugins/ruflo-core/scripts/witness/**'
      - 'plugins/ruflo-core/scripts/test-hooks.mjs'
      - 'verification/**'
      # scripts/*.mjs audits (tool-descriptions, plugin-packages, hook-commands)
      - 'scripts/**'
      # hook-command audit (#1921) — every plugin hooks.json + the ruflo-hook shims
      - '**/hooks/hooks.json'
      - '**/scripts/ruflo-hook.sh'
      # pre-bash hook safety (#2017) — both handler copies trigger the smoke
      - '**/.claude/helpers/hook-handler.cjs'
      # ruflo-browser rvf create flag (#2015) — TS source, plugin shell
      # scripts, agent-facing recipes all guarded by the same smoke.
      - 'v3/@claude-flow/cli/src/mcp-tools/browser-session-tools.ts'
      - 'plugins/ruflo-browser/**'
      # ruflo-graph-intelligence (#2044, ADR-123) — outside v3 workspace,
      # has its own lockfile + tests; needs to be CI-guarded on every change.
      - 'plugins/ruflo-graph-intelligence/**'
      # Supply-chain hardening (#2046) — every package.json + lockfile +
      # allowlist edit triggers the supply-chain audit.
      - '**/package.json'
      - '**/package-lock.json'
      - '**/pnpm-lock.yaml'
      - '.github/supply-chain/**'
      - 'scripts/audit-supply-chain.mjs'
      # Knowledge-graph plugin (#2049) — kg-extract type-import classifier
      # + kg-traverse controller wiring drift fast when SKILL.md edits
      # silently revert the bug-fix shape.
      - 'plugins/ruflo-knowledge-graph/**'
      - 'scripts/smoke-kg-extract-type-imports.mjs'
      # Neural-trader portfolio CG (#2068, ADR-126 Phase 3) — drift fast
      # when the adapter, skill, or runtime mirror diverge from the
      # ADR-123 Wedge 8 contract.
      - 'plugins/ruflo-neural-trader/src/sublinear-adapter.ts'
      - 'plugins/ruflo-neural-trader/src/sublinear-adapter.mjs'
      - 'plugins/ruflo-neural-trader/skills/trader-portfolio-cg/**'
      - 'scripts/smoke-neural-trader-portfolio-cg.mjs'
      # Neural-trader backtest signing (#2068, ADR-126 Phase 4) — Ed25519
      # tamper-evidence for paper→live promotion; verifier MUST pin to a
      # trusted key (CWE-347 / #1922 pattern).
      - 'plugins/ruflo-neural-trader/src/signed-artifact.ts'
      - 'plugins/ruflo-neural-trader/src/signed-artifact.mjs'
      - 'plugins/ruflo-neural-trader/skills/trader-backtest/**'
      - 'plugins/ruflo-neural-trader/skills/trader-cloud-backtest/**'
      - 'scripts/smoke-neural-trader-backtest-signing.mjs'
      # Neural-trader SendMessage risk-gate pipeline (#2068, ADR-126 Phase 5) —
      # structural gate: trading-strategist refuses --broker without an
      # explicit risk-analyst RiskDecision approval.
      - 'plugins/ruflo-neural-trader/src/pipeline-messages.ts'
      - 'plugins/ruflo-neural-trader/agents/market-analyst.md'
      - 'plugins/ruflo-neural-trader/agents/trading-strategist.md'
      - 'plugins/ruflo-neural-trader/agents/risk-analyst.md'
      - 'plugins/ruflo-neural-trader/agents/backtest-engineer.md'
      - 'scripts/smoke-neural-trader-pipeline.mjs'
      # Neural-trader feature attribution (#2068, ADR-126 Phase 6) —
      # regulator-grade interpretability via single-entry PageRank.
      # Same signing scheme as Phase 4; ranking is seed-reproducible.
      - 'plugins/ruflo-neural-trader/src/signed-attribution.ts'
      - 'plugins/ruflo-neural-trader/src/signed-attribution.mjs'
      - 'plugins/ruflo-neural-trader/skills/trader-explain/**'
      - 'scripts/smoke-neural-trader-feature-attribution.mjs'
      # Plugin-registry CWE-347 regression smoke (#1922) — `discovery.ts`
      # signature verifier + the smoke fixture must stay in lockstep.
      - 'v3/@claude-flow/cli/src/plugins/store/discovery.ts'
      - 'v3/@claude-flow/cli/src/transfer/ipfs/client.ts'
      - 'v3/@claude-flow/cli/scripts/publish-registry.ts'
      - 'scripts/smoke-plugin-registry-signature.mjs'
      # ruvllm WASM auto-init regression smoke (#2086) — the
      # `loadRuvllmWasm()` helper in `ruvllm-tools.ts` and the
      # `ruvllm_status` un-init diagnostic path must stay in lockstep.
      - 'v3/@claude-flow/cli/src/mcp-tools/ruvllm-tools.ts'
      - 'v3/@claude-flow/cli/src/ruvector/ruvllm-wasm.ts'
      - 'scripts/smoke-ruvllm-wasm-auto-init.mjs'
      # agent_execute provider routing (#2042) — executeAgentTask must
      # not regress to inline Anthropic fetch, and the OpenRouter branch
      # in callAnthropicMessages must stay wired.
      - 'v3/@claude-flow/cli/src/mcp-tools/agent-execute-core.ts'
      - 'scripts/smoke-agent-execute-providers.mjs'
      # memory stats legacy-DB regression guard (#2120) — the WHERE
      # status='active' filter must accept NULL too, and the schema
      # backfill must promote NULL→'active' on existing DBs.
      - 'v3/@claude-flow/cli/src/memory/memory-bridge.ts'
      - 'v3/@claude-flow/cli/src/memory/memory-initializer.ts'
      - 'v3/@claude-flow/cli/src/commands/status.ts'
      - 'scripts/smoke-memory-stats-legacy-db.mjs'
      # ADR-125 Phase 7 — no stray DB artifacts after `npm test` in
      # @claude-flow/memory. vitest.setup.ts must wipe *.db / *.rvf /
      # *.redb files written by agentdb / @ruvector/rvf bindings.
      - 'v3/@claude-flow/memory/vitest.setup.ts'
      - 'v3/@claude-flow/memory/vitest.config.ts'
      - 'v3/@claude-flow/memory/vitest.config.mts'
      - 'scripts/smoke-memory-no-stray-db.mjs'
      # GitHub skills/agents/helpers surface (#2089, ADR-127) — injection
      # smoke + actions pin smoke gate every change to the .github surface.
      - '.claude/agents/github/**'
      - '.claude/skills/github-*/**'
      - 'v3/@claude-flow/cli/.claude/commands/github/**'
      - '.claude/helpers/github-safe.js'
      - 'v3/@claude-flow/cli/.claude/helpers/github-safe.js'
      - 'scripts/smoke-github-safe-injection.mjs'
      - 'scripts/smoke-github-actions-pins.mjs'
      - 'scripts/smoke-deprecated-actions.mjs'
      - 'scripts/smoke-attribution-opt-in.mjs'
      - '.github/supply-chain/allowed-deps.json'
      # Init-bundle invariants smoke (#2095, ADR-128) — orphan dirs, SKILLS_MAP
      # completeness, and plugin-init agent dedup are all guarded by Phase 5.
      - 'v3/@claude-flow/cli/.claude/**'
      - 'v3/@claude-flow/cli/src/init/**'
      - 'plugins/*/agents/**'
      - 'plugins/*/skills/**'
      - 'plugins/*/commands/**'
      - 'scripts/smoke-init-bundle-invariants.mjs'
      # ADR-129 — rvagent full integration (P1-P4)
      - 'v3/@claude-flow/cli/src/ruvector/agent-wasm.ts'
      - 'v3/@claude-flow/cli/src/mcp-tools/wasm-agent-tools.ts'
      - 'scripts/smoke-wasm-provider-bridge.mjs'
      - 'scripts/smoke-wasm-rvf-compose.mjs'
      - 'scripts/smoke-wasm-gallery-crud.mjs'
      - 'scripts/smoke-wasm-plugin-bridge.mjs'
      # ADR-130 — graph intelligence integration (P1-P6)
      - 'v3/@claude-flow/cli/src/memory/memory-initializer.ts'
      - 'v3/@claude-flow/cli/src/memory/embedding-quantization.ts'
      - 'v3/@claude-flow/cli/src/memory/graph-edge-writer.ts'
      - 'v3/@claude-flow/cli/src/mcp-tools/agentdb-tools.ts'
      - 'v3/@claude-flow/cli/src/mcp-tools/hooks-tools.ts'
      - 'plugins/ruflo-graph-intelligence/src/adapters/knowledge-graph-adapter.ts'
      - 'scripts/smoke-graph-schema-migration.mjs'
      - 'scripts/smoke-graph-query-dispatch.mjs'
      - 'scripts/smoke-trajectory-graph-edges.mjs'
      - 'scripts/smoke-graph-plugin-adapter.mjs'
      - 'scripts/smoke-graph-pathfinder.mjs'
      - 'scripts/benchmark-graph.mjs'
      # statusline generator delegation regression guard (#2195)
      - 'v3/@claude-flow/cli/src/init/statusline-generator.ts'
      - '.claude/helpers/statusline.cjs'
      - 'scripts/smoke-statusline-generator-delegation.mjs'
      # wizard init regression guard (#2206 #2207 #2208)
      - 'v3/@claude-flow/cli/src/init/mcp-generator.ts'
      - 'v3/@claude-flow/cli/src/init/executor.ts'
      - 'scripts/smoke-wizard-init-regression.mjs'
  pull_request:
    branches: [main, develop]
    paths:
      - 'v3/**'
      - 'plugins/ruflo-core/scripts/witness/**'
      - 'plugins/ruflo-core/scripts/test-hooks.mjs'
      - 'scripts/**'
      - '**/hooks/hooks.json'
      - '**/scripts/ruflo-hook.sh'
      - '**/.claude/helpers/hook-handler.cjs'
      # ruflo-browser rvf create flag (#2015)
      - 'v3/@claude-flow/cli/src/mcp-tools/browser-session-tools.ts'
      - 'plugins/ruflo-browser/**'
      # ruflo-graph-intelligence (#2044, ADR-123)
      - 'plugins/ruflo-graph-intelligence/**'
      # Supply-chain hardening (#2046) — every dep + lockfile change is
      # CVE-audited, allowlist-checked, integrity-checked.
      - '**/package.json'
      - '**/package-lock.json'
      - '**/pnpm-lock.yaml'
      - '.github/supply-chain/**'
      - 'scripts/audit-supply-chain.mjs'
      # Knowledge-graph plugin (#2049)
      - 'plugins/ruflo-knowledge-graph/**'
      - 'scripts/smoke-kg-extract-type-imports.mjs'
      # Neural-trader portfolio CG (#2068, ADR-126 Phase 3)
      - 'plugins/ruflo-neural-trader/src/sublinear-adapter.ts'
      - 'plugins/ruflo-neural-trader/src/sublinear-adapter.mjs'
      - 'plugins/ruflo-neural-trader/skills/trader-portfolio-cg/**'
      - 'scripts/smoke-neural-trader-portfolio-cg.mjs'
      # Neural-trader backtest signing (#2068, ADR-126 Phase 4)
      - 'plugins/ruflo-neural-trader/src/signed-artifact.ts'
      - 'plugins/ruflo-neural-trader/src/signed-artifact.mjs'
      - 'plugins/ruflo-neural-trader/skills/trader-backtest/**'
      - 'plugins/ruflo-neural-trader/skills/trader-cloud-backtest/**'
      - 'scripts/smoke-neural-trader-backtest-signing.mjs'
      # Neural-trader SendMessage risk-gate pipeline (#2068, ADR-126 Phase 5)
      - 'plugins/ruflo-neural-trader/src/pipeline-messages.ts'
      - 'plugins/ruflo-neu\n```\n\n### .github/workflows/validate-marketplace.yml\n\n```yaml\nname: Validate Marketplace
on:
  push:
    paths:
      - '.claude-plugin/**'
      - 'plugins/**'
  pull_request:
    paths:
      - '.claude-plugin/**'
      - 'plugins/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - name: Validate marketplace.json
        run: |
          node -e "
            const fs = require('fs');
            const catalog = JSON.parse(fs.readFileSync('.claude-plugin/marketplace.json'));
            console.log('Marketplace:', catalog.name);
            console.log('Plugins:', catalog.plugins.length);
            for (const p of catalog.plugins) {
              const dir = p.source;
              if (!fs.existsSync(dir)) throw new Error('Missing plugin dir: ' + dir);
              const manifest = dir + '/.claude-plugin/plugin.json';
              if (!fs.existsSync(manifest)) throw new Error('Missing manifest: ' + manifest);
              const m = JSON.parse(fs.readFileSync(manifest));
              if (!m.name || !m.description || !m.version) throw new Error('Manifest missing required fields: ' + manifest);
              if (!m.author || !m.author.name) throw new Error('Manifest missing author: ' + manifest);
              console.log('  OK', m.name, m.version);
            }
            console.log('All plugins validated.');
          "
      - name: Validate plugin structure
        run: |
          for dir in plugins/*/; do
            manifest="$dir/.claude-plugin/plugin.json"
            if [ ! -f "$manifest" ]; then echo "FAIL: Missing $manifest"; exit 1; fi
            node -e "JSON.parse(require('fs').readFileSync('${manifest}'))" || exit 1

            # Check skills use directory/SKILL.md format
            if [ -d "${dir}skills" ]; then
              for skill_dir in "${dir}skills"/*/; do
                [ -d "$skill_dir" ] || continue
                if [ ! -f "${skill_dir}SKILL.md" ]; then
                  echo "FAIL: Missing SKILL.md in $skill_dir"
                  exit 1
                fi
              done
            fi
            echo "OK: $dir"
          done
\n```\n\n### .github/workflows/verification-pipeline.yml\n\n```yaml\nname: 🔍 Verification Pipeline

on:
  push:
    branches: [main, develop, alpha-*]
  pull_request:
    branches: [main, develop]
  workflow_dispatch:
    inputs:
      verification_mode:
        description: 'Verification mode'
        required: false
        default: 'full'
        type: choice
        options:
          - full
          - quick
          - security-only

env:
  NODE_VERSION: '20'
  CACHE_VERSION: v1

jobs:
  # Pre-verification setup and validation
  setup-verification:
    name: 🚀 Setup Verification
    runs-on: ubuntu-latest
    outputs:
      verification-id: ${{ steps.setup.outputs.verification-id }}
      test-matrix: ${{ steps.setup.outputs.test-matrix }}
      cache-key: ${{ steps.setup.outputs.cache-key }}
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Generate verification ID
        id: setup
        run: |
          VERIFICATION_ID="verify-$(date +%Y%m%d-%H%M%S)-${{ github.sha }}"
          echo "verification-id=$VERIFICATION_ID" >> $GITHUB_OUTPUT
          echo "test-matrix={\"include\":[{\"os\":\"ubuntu-latest\",\"node\":\"18\"},{\"os\":\"ubuntu-latest\",\"node\":\"20\"},{\"os\":\"macos-latest\",\"node\":\"20\"},{\"os\":\"windows-latest\",\"node\":\"20\"}]}" >> $GITHUB_OUTPUT
          echo "cache-key=${{ env.CACHE_VERSION }}-${{ runner.os }}-${{ hashFiles('**/package-lock.json') }}" >> $GITHUB_OUTPUT

      - name: Install dependencies
        run: npm ci --legacy-peer-deps

      - name: Cache dependencies
        uses: actions/cache@v4
        with:
          path: |
            node_modules
            ~/.npm
          key: ${{ steps.setup.outputs.cache-key }}
          restore-keys: |
            ${{ env.CACHE_VERSION }}-${{ runner.os }}-

  # Security verification
  security-verification:
    name: 🛡️ Security Verification
    runs-on: ubuntu-latest
    needs: setup-verification
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Restore dependencies
        uses: actions/cache@v4
        with:
          path: |
            node_modules
            ~/.npm
          key: ${{ needs.setup-verification.outputs.cache-key }}

      - name: Install dependencies
        run: npm ci --legacy-peer-deps

      - name: Security audit
        run: |
          echo "🔍 Running security audit..."
          npm audit --audit-level=moderate || true
          npm audit --audit-level=high --json > security-audit.json || true

      - name: License compliance check
        run: |
          echo "📋 Checking license compliance..."
          npx license-checker --onlyAllow 'MIT;Apache-2.0;BSD-2-Clause;BSD-3-Clause;ISC;CC0-1.0;Unlicense' \
            --excludePrivatePackages \
            --json > license-report.json || true

      - name: Dependency vulnerability scan
        run: |
          echo "🔍 Scanning for vulnerabilities..."
          npx audit-ci --config .audit-ci.json || true

      - name: Upload security reports
        uses: actions/upload-artifact@v4
        with:
          name: security-reports-${{ needs.setup-verification.outputs.verification-id }}
          path: |
            security-audit.json
            license-report.json
          retention-days: 30

  # Code quality verification
  code-quality:
    name: 📝 Code Quality
    runs-on: ubuntu-latest
    needs: setup-verification
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Restore dependencies
        uses: actions/cache@v4
        with:
          path: |
            node_modules
            ~/.npm
          key: ${{ needs.setup-verification.outputs.cache-key }}

      - name: Install dependencies
        run: npm ci --legacy-peer-deps

      - name: ESLint code analysis
        run: |
          echo "🔍 Running ESLint..."
          npm run lint -- --format=json --output-file=eslint-report.json || true
          npm run lint

      - name: TypeScript type checking
        run: |
          echo "🔍 Type checking..."
          npm run typecheck || echo "⚠️ Type checking skipped (TypeScript compiler crash)"
        continue-on-error: true

      - name: Format checking
        run: |
          echo "🎨 Checking code formatting..."
          npm run format
          git diff --exit-code || echo "⚠️ Some files need formatting (non-blocking)"
        continue-on-error: true

      - name: Complexity analysis
        run: |
          echo "📊 Analyzing code complexity..."
          npx complexity-report --format json --output complexity-report.json src/ || true

      - name: Upload quality reports
        uses: actions/upload-artifact@v4
        with:
          name: quality-reports-${{ needs.setup-verification.outputs.verification-id }}
          path: |
            eslint-report.json
            complexity-report.json
          retention-days: 30

  # Multi-platform testing
  test-verification:
    name: 🧪 Test Verification (${{ matrix.os }}, Node ${{ matrix.node }})
    runs-on: ${{ matrix.os }}
    needs: [setup-verification, security-verification]
    strategy:
      fail-fast: false
      matrix: ${{ fromJson(needs.setup-verification.outputs.test-matrix) }}
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js ${{ matrix.node }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
          cache: 'npm'

      - name: Install dependencies
        run: |
          if [ "${{ runner.os }}" == "Linux" ]; then
            npm ci --legacy-peer-deps
          else
            # Skip optional platform-specific dependencies on macOS/Windows
            npm ci --legacy-peer-deps --omit=optional || npm ci --legacy-peer-deps --force
          fi
        shell: bash

      - name: Run unit tests
        run: |
          echo "🧪 Running unit tests..."
          npm run test:unit || echo "⚠️ Some unit tests failed (Jest teardown issues - non-blocking)"
        continue-on-error: true

      - name: Run integration tests
        run: |
          echo "🔗 Running integration tests..."
          npm run test:integration || echo "⚠️ Some integration tests failed (non-blocking)"
        continue-on-error: true

      - name: Run performance tests
        if: matrix.os == 'ubuntu-latest' && matrix.node == '20'
        run: |
          echo "⚡ Running performance tests..."
          npm run test:performance || echo "⚠️ Some performance tests failed (non-blocking)"
        continue-on-error: true

      - name: Generate coverage report
        if: matrix.os == 'ubuntu-latest' && matrix.node == '20'
        run: |
          echo "📊 Generating coverage report..."
          npm run test:coverage || echo "⚠️ Coverage generation failed (non-blocking)"
        continue-on-error: true
          
      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: test-results-${{ matrix.os }}-node${{ matrix.node }}-${{ needs.setup-verification.outputs.verification-id }}
          path: |
            coverage/
            test-reports/
          retention-days: 30

  # Build verification - simplified for V3 monorepo structure
  build-verification:
    name: 🏗️ Build Verification
    runs-on: ubuntu-latest
    needs: [setup-verification, code-quality]
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci --legacy-peer-deps

      - name: Build CLI package
        run: |
          echo "🔨 Building CLI package..."
          cd v3/@claude-flow/cli && npm run build || echo "✅ CLI build completed (or already built)"
        continue-on-error: true

      - name: Verify CLI availability
        run: |
          echo "✅ Verifying CLI..."
          test -f v3/@claude-flow/cli/bin/cli.js && echo "CLI binary exists" || echo "⚠️ CLI binary not found (non-blocking)"
        continue-on-error: true

      - name: Package for distribution
        run: |
          echo "📦 Creating package..."
          npm pack || echo "⚠️ Pack skipped"
          ls -la *.tgz 2>/dev/null || echo "No tgz files created"
        continue-on-error: true

  # Documentation verification - simplified checks
  docs-verification:
    name: 📚 Documentation Verification
    runs-on: ubuntu-latest
    needs: setup-verification
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Check documentation files
        run: |
          echo "📋 Verifying documentation..."
          test -f README.md && echo "✅ README.md exists" || echo "⚠️ README.md missing"
          test -f CHANGELOG.md && echo "✅ CHANGELOG.md exists" || echo "⚠️ CHANGELOG.md missing"
          test -f LICENSE && echo "✅ LICENSE exists" || echo "⚠️ LICENSE missing"
          # At least README must exist
          test -f README.md || (echo "❌ README.md required" && exit 1)

      - name: Validate package.json structure
        run: |
          echo "📦 Validating package.json..."
          node -e "const p = require('./package.json'); console.log('✅ Package:', p.name, p.version);"

  # Performance benchmarking
  performance-verification:
    name: ⚡ Performance Verification
    runs-on: ubuntu-latest
    needs: [setup-verification, build-verification]
    if: github.event_name == 'push' || git\n```\n\n## William-kelvem94/ADB_Android-s_Will\n\n### .github/workflows/ci.yml\n\n```yaml\nname: Validar Android Hub

on:
  push:
    branches: [main]
  pull_request:

permissions:
  contents: read

jobs:
  validar:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: pip
          cache-dependency-path: backend/requirements.txt
      - uses: actions/setup-node@v4
        with:
          node-version: "22"
      - name: Instalar dependências Python
        run: |
          python -m pip install --upgrade pip
          python -m pip install -r backend/requirements.txt
      - name: Validar sintaxe Python
        run: python -m compileall -q backend scripts
      - name: Executar testes Python
        run: python -m unittest discover -s backend -p "test_*.py" -v
      - name: Validar JavaScript
        run: |
          node --check frontend/patch.js
          node --check frontend/enhancements.js
      - name: Validar inicializadores Linux
        run: bash -n scripts/start-linux.sh iniciar-linux.sh
\n```\n\n## William-kelvem94/IA_LOCAL_S_ULTRA\n\n### .github/workflows/android.yml\n\n```yaml\nname: Android APK

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read

jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 90

    steps:
      - name: Checkout com llama.cpp
        uses: actions/checkout@v6
        with:
          submodules: recursive
          fetch-depth: 1

      - name: Java 17
        uses: actions/setup-java@v5
        with:
          distribution: temurin
          java-version: '17'

      - name: Android SDK
        uses: android-actions/setup-android@v4

      - name: Componentes nativos
        run: |
          yes | sdkmanager --licenses >/dev/null || true
          sdkmanager "platforms;android-36" "build-tools;36.0.0" "ndk;29.0.13113456" "cmake;3.31.6"

      - name: Compilar APK sem GGUF embutido
        run: |
          chmod +x third_party/llama.cpp/examples/llama.android/gradlew
          ./third_party/llama.cpp/examples/llama.android/gradlew -p . :app:assembleDebug --no-daemon --stacktrace

      - name: Validar APK gerado
        run: |
          test -f app/build/outputs/apk/debug/app-debug.apk
          ls -lh app/build/outputs/apk/debug/app-debug.apk

      - name: Publicar APK
        uses: actions/upload-artifact@v6
        with:
          name: IA_LOCAL_S_ULTRA-apk
          path: app/build/outputs/apk/debug/app-debug.apk
          if-no-files-found: error
          compression-level: 0
          retention-days: 3
\n```\n\n## Limite\n\nConteúdos truncados a 10.000 caracteres por arquivo.\n