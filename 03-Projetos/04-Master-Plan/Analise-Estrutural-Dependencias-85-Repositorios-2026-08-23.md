# Análise de estrutura e dependências — GitHub William-kelvem94

> **Data:** 2026-08-23  
> **Escopo:** 85 repositórios acessíveis na conta William-kelvem94.  
> **Modo:** somente leitura; nenhum arquivo, branch, commit ou configuração remota foi alterado.  
> **Evidência:** metadados de repositório, árvore recursiva acessível, README(s) encontrados e até quatro manifestos prioritários por repositório.

## Resultado executivo

- Repositórios analisados: **85**.
- README localizado: **74/85**.
- Pelo menos um manifesto identificado: **66/85**.
- Testes evidenciados pela árvore: **38/85**.
- Workflows de CI evidenciados: **23/85**.
- Árvores sinalizadas como truncadas: **0/85**.

A análise é estrutural e documental: não executa os projetos, não instala dependências e não substitui uma auditoria de código em clone local.

## Distribuição de sinais de stack

- JavaScript: 50
- Node.js/JavaScript: 43
- Python: 38
- Docker: 37
- TypeScript: 30
- Vite: 24
- GitHub Actions: 23
- Indeterminada: 8
- Next.js: 7
- Java: 6
- PHP: 6
- Gradle/Android or JVM: 5
- Android: 5
- Kotlin: 5
- Rust: 4
- Sem arquivos acessíveis: 4
- Dart/Flutter: 1

## Critério de leitura

- **Stack:** inferida por extensões, diretórios, arquivos de configuração e manifestos.
- **Objetivo:** extraído prioritariamente do README; quando ausente, usa descrição/nome e é marcado como inferência.
- **Riscos:** sinais estruturais, não confirmação de vulnerabilidade.
- **Lacunas:** ausência de evidência na árvore não prova ausência no runtime.
- **Dependências:** o relatório preserva apenas trechos limitados dos manifestos acessíveis; lockfiles e dependências transitivas não foram resolvidos.

---

## William-kelvem94/ada_v2---jarvis

- **URL:** https://github.com/William-kelvem94/ada_v2---jarvis
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 0 KB | **Árvore:** 1 arquivos, 0 diretórios
- **README:** não localizado
- **Manifestos:** nenhum identificado
- **Stack inferida:** Indeterminada
- **Objetivo/descrição:** Objetivo não documentado no README acessível.
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** README ausente ou não acessível; manifesto de dependências não identificado; testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** documentar propósito, instalação, uso e estado; declarar dependências e versão de runtime; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/ADB_Android-s_Will

- **URL:** https://github.com/William-kelvem94/ADB_Android-s_Will
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 2727 KB | **Árvore:** 1568 arquivos, 0 diretórios
- **README:** README.md (9563 caracteres)
- **Manifestos:** `backend/Dockerfile`, `docker-compose.yml`, `backend/requirements.txt`, `backend/requirements-dev.txt`
- **Stack inferida:** JavaScript, Python, Docker, GitHub Actions
- **Objetivo/descrição:** # Android Hub Painel local para observar, diagnosticar e administrar dispositivos Android por ADB, com telemetria em tempo real, histórico, segurança por confirmação explícita e gerenciamento de IA local no próprio aparelho. **Versão:** 1.3.0
- **Sinais:** testes=não evidenciado, CI=sim, Docker=sim, docs=sim, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** criar testes automatizados; explicitar licença

### Evidência de manifestos

**backend/Dockerfile**

```
FROM python:3.12-slim
WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends android-tools-adb ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/app.py .
COPY backend/ai_manager.py .
COPY backend/interpreter.py .
COPY backend/catalog_engine.py .
COPY backend/security.py .
COPY backend/retention.py .
COPY backend/telemetry_service.py .
COPY backend/run_server.py .
COPY scripts/validate_catalog.py ./scripts/validate_catalog.py
COPY frontend ./frontend
COPY Infos_celularres ./Infos_celularres

RUN python -c "from catalog_engine import CatalogIndex; CatalogIndex('/app/Infos_celularres/presets',['Samsung','Google','Motorola','Xiaomi','OnePlus_OPPO_realme','Huawei_Honor']).save_cache('/app/catalog_index.json')"
RUN mkdir -p /app/runtime/uploads /app/runtime/ai

EXPOSE 8765
CMD ["python","run_server.py"]

```

**docker-compose.yml**

```
services:
  android-hub:
    build:
      context: .
      dockerfile: backend/Dockerfile
    container_name: android-hub
    init: true
    read_only: true
    security_opt:
      - no-new-privileges:true
    ports: ["127.0.0.1:8765:8765"]
    healthcheck:
      test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8765/api/health', timeout=3)"]
      interval: 15s
      timeout: 5s
      retries: 5
      start_period: 20s
    environment:
      ANDROID_HUB_MODE: docker
      ADB_PATH: /usr/bin/adb
      ADB_SERIAL: ${ADB_SERIAL:-}
      WEB_PATH: /app/frontend
      CATALOG_PATH: /app/Infos_celularres/presets
      CATALOG_SCOPES: Samsung,Google,Motorola,Xiaomi,OnePlus_OPPO_realme,Huawei_Honor
      RUNTIME_PATH: /app/runtime
      MAX_UPLOAD_MB: ${MAX_UPLOAD_MB:-256}
      CORS_ORIGINS: ${CORS_ORIGINS:-http://localhost:8765,http://127.0.0.1:8765}
      ANDROID_HUB_AUTH_TOKEN: ${ANDROID_HUB_AUTH_TOKEN:-}
      ANDROID_HUB_RATE_LIMIT_READS: ${ANDROID_HUB_RATE_LIMIT_READS:-120}
      ANDROID_HUB_RATE_LIMIT_MUTATIONS: ${ANDROID_HUB_RATE_LIMIT_MUTATIONS:-30}
      ANDROID_HUB_LATENCY_HOST: ${ANDROID_HUB_LATENCY_HOST:-}
      TLS_CERTFILE: ${TLS_CERTFILE:-}
      TLS_KEYFILE: ${TLS_KEYFILE:-}
      ADB_SERVER_SOCKET: tcp:host.docker.internal:5037
    volumes:
```

**backend/requirements.txt**

```
fastapi==0.116.1
uvicorn[standard]==0.35.0
python-multipart==0.0.20
pydantic==2.11.7
PyYAML==6.0.2

```

**backend/requirements-dev.txt**

```
-r requirements.txt
httpx>=0.27,<1
pytest>=8.3,<9

```


---

## William-kelvem94/AFFiNE-Will

- **URL:** https://github.com/William-kelvem94/AFFiNE-Will
- **Branch padrão:** `canary`
- **Visibilidade:** public | **Arquivado:** não
- **Tamanho GitHub:** 434950 KB | **Árvore:** 12611 arquivos, 0 diretórios
- **README:** README.md (16319 caracteres)
- **Manifestos:** `yarn.lock`, `Cargo.lock`, `Cargo.toml`, `package.json`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite, Gradle/Android or JVM, Android, Kotlin, Java, Rust, Docker, GitHub Actions
- **Objetivo/descrição:** <div align="center"> <h1 style="border-bottom: none"> <b><a href="https://affine.pro">AFFiNE.Pro</a></b><br />
- **Sinais:** testes=sim, CI=sim, Docker=sim, docs=sim, lockfile=sim
- **Riscos estruturais:** possível material sensível/configuração ambiental na árvore; revisar segredos; branch padrão não é main (canary); dependência/configuração usa marcador latest; baixa reprodutibilidade; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** nenhuma lacuna estrutural básica detectada

### Evidência de manifestos

**Cargo.toml**

```
[workspace]
members = [
  "./packages/backend/native",
  "./packages/common/native",
  "./packages/common/y-octo/core",
  "./packages/common/y-octo/utils",
  "./packages/frontend/mobile-native",
  "./packages/frontend/native",
  "./packages/frontend/native/nbstore",
  "./packages/frontend/native/schema",
  "./packages/frontend/native/sqlite_v1",
]
resolver = "3"

  [workspace.package]
  edition = "2024"

  [workspace.dependencies]
  aes-gcm = "0.10"
  affine_common = { path = "./packages/common/native" }
  affine_nbstore = { path = "./packages/frontend/native/nbstore" }
  ahash = "0.8"
  anyhow = "1"
  arbitrary = { version = "1.3", features = ["derive"] }
  assert-json-diff = "2.0"
  async-lock = { version = "3.4.0", features = ["loom"] }
  base64-simd = "0.8"
  bitvec = "1.0"
  block2 = "0.6"
  byteorder = "1.5"
  chrono = "0.4"
  clap = { version = "4.4", features = ["derive"] }
  core-foundation = "0.10"
  coreaudio-rs = "0.12"
  cpal = "0.15"
```

**package.json**

```
{
  "name": "@affine/monorepo",
  "version": "0.26.3",
  "private": true,
  "author": "toeverything",
  "license": "MIT",
  "workspaces": [
    ".",
    "blocksuite/**/*",
    "packages/*/*",
    "packages/frontend/apps/*",
    "tools/*",
    "docs/reference",
    "tools/@types/*",
    "tests/*"
  ],
  "engines": {
    "node": ">=22.12.0 <23.0.0"
  },
  "scripts": {
    "affine": "r affine.ts",
    "af": "r affine.ts",
    "dev": "yarn affine dev",
    "build": "yarn affine build",
    "lint:eslint": "cross-env NODE_OPTIONS=\"--max-old-space-size=16384\" eslint --report-unused-disable-directives-severity=off . --cache",
    "lint:eslint:fix": "yarn lint:eslint --fix --fix-type problem,suggestion,layout",
    "lint:prettier": "prettier --ignore-unknown --cache --check .",
    "lint:prettier:fix": "prettier --ignore-unknown --cache --write .",
    "lint:ox": "oxlint --deny-warnings",
    "lint:ox:fix": "yarn lint:ox --fix",
    "lint": "yarn lint:ox && yarn lint:eslint && yarn lint:prettier",
    "lint:fix": "yarn lint:ox:fix && yarn lint:eslint:fix && yarn lint:prettier:fix",
    "test": "vitest --run",
    "test:ui": "vitest --ui",
    "test:coverage": "vitest run --coverage",
```


---

## William-kelvem94/AGENTE-IA

- **URL:** https://github.com/William-kelvem94/AGENTE-IA
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 242 KB | **Árvore:** 76 arquivos, 0 diretórios
- **README:** README.md (3444 caracteres)
- **Manifestos:** `Dockerfile`, `requirements.txt`, `docker-compose.yml`, `vscode-extension/package.json`
- **Stack inferida:** Node.js/JavaScript, JavaScript, Python, Docker
- **Objetivo/descrição:** # AGENTE-IA — Agente programador local (scaffold) Agente de IA local para programar, debugar, testar e revisar código usando modelos rodando localmente (ex.: Ollama). Principais componentes:
- **Sinais:** testes=sim, CI=não evidenciado, Docker=sim, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** CI/CD não evidenciado; dependência/configuração usa marcador latest; baixa reprodutibilidade; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**Dockerfile**

```
FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 8000

ENV OLLAMA_HOST=http://host.docker.internal:11434

CMD ["uvicorn", "agent.server:app", "--host", "0.0.0.0", "--port", "8000"]

```

**requirements.txt**

```
fastapi==0.129.0
uvicorn[standard]==0.41.0
requests==2.32.5
psutil==7.2.2
typer[all]==0.24.0
pytest==9.0.2
Jinja2==3.1.6
aiofiles==25.1.0
python-multipart==0.0.22
scikit-learn==1.8.0
sentence-transformers==5.2.3
# pinned additional libs to avoid unexpected SWIG/compat warnings
numpy==2.4.2
scipy==1.17.0
defusedxml==0.7.1
lxml==6.0.2
transformers==5.2.0
tokenizers==0.22.2

```

**docker-compose.yml**

```
version: '3.8'
services:
  agente-ia:
    build: .
    image: agente-ia:latest
    ports:
      - "8000:8000"
    environment:
      - OLLAMA_HOST=http://host.docker.internal:11434
    restart: unless-stopped

```

**vscode-extension/package.json**

```
{
  "name": "agente-ia-vscode",
  "displayName": "AGENTE-IA",
  "description": "Integração mínima do AGENTE-IA com VS Code — gera/applica patches via API local.",
  "version": "0.0.1",
  "engines": {
    "vscode": "^1.70.0"
  },
  "activationEvents": [
    "onCommand:agente.generatePatch",
    "onCommand:agente.applyPatch"
  ],
  "main": "extension.js",
  "contributes": {
    "configuration": {
      "type": "object",
      "title": "AGENTE-IA",
      "properties": {
        "agente.host": {
          "type": "string",
          "default": "http://127.0.0.1:8000",
          "description": "Endereço do servidor AGENTE-IA"
        }
      }
    },
    "commands": [
      {
        "command": "agente.generatePatch",
        "title": "AGENTE-IA: Generate Patch from Selection"
      },
      {
        "command": "agente.applyPatch",
        "title": "AGENTE-IA: Apply Last Staged Patch"
      }
    ]
```


---

## William-kelvem94/AppFlowy-Will

- **URL:** https://github.com/William-kelvem94/AppFlowy-Will
- **Branch padrão:** `main`
- **Visibilidade:** public | **Arquivado:** não
- **Tamanho GitHub:** 93896 KB | **Árvore:** 5800 arquivos, 0 diretórios
- **README:** README.md (8549 caracteres)
- **Manifestos:** `frontend/scripts/makefile`, `frontend/rust-lib/Cargo.lock`, `frontend/rust-lib/Cargo.toml`, `frontend/appflowy_flutter/Makefile`
- **Stack inferida:** JavaScript, Gradle/Android or JVM, Android, Kotlin, Java, Rust, Dart/Flutter, Docker, GitHub Actions
- **Objetivo/descrição:** <h1 align="center" style="border-bottom: none"> <b> <a href="https://www.appflowy.com">AppFlowy</a><br>
- **Sinais:** testes=sim, CI=sim, Docker=sim, docs=sim, lockfile=sim
- **Riscos estruturais:** possível material sensível/configuração ambiental na árvore; revisar segredos; dependência/configuração usa marcador latest; baixa reprodutibilidade; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** nenhuma lacuna estrutural básica detectada

### Evidência de manifestos

**frontend/rust-lib/Cargo.toml**

```
[workspace]
members = [
  "lib-dispatch",
  "lib-log",
  "flowy-core",
  "dart-ffi",
  "flowy-user",
  "flowy-user-pub",
  "event-integration-test",
  "flowy-sqlite",
  "flowy-folder",
  "flowy-folder-pub",
  "flowy-notification",
  "flowy-document",
  "flowy-document-pub",
  "flowy-error",
  "flowy-database2",
  "flowy-database-pub",
  "flowy-server",
  "flowy-server-pub",
  "flowy-storage",
  "collab-integrate",
  "flowy-date",
  "flowy-search",
  "lib-infra",
  "build-tool/flowy-ast",
  "build-tool/flowy-codegen",
  "build-tool/flowy-derive",
  "flowy-search-pub",
  "flowy-ai",
  "flowy-ai-pub",
  "flowy-storage-pub",
  "flowy-sqlite-vec",
]

```


---

## William-kelvem94/Atividade-01

- **URL:** https://github.com/William-kelvem94/Atividade-01
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 5 KB | **Árvore:** 15 arquivos, 0 diretórios
- **README:** README.md (14 caracteres)
- **Manifestos:** nenhum identificado
- **Stack inferida:** Java
- **Objetivo/descrição:** # Atividade-01
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** manifesto de dependências não identificado; testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** declarar dependências e versão de runtime; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/Atividade-03

- **URL:** https://github.com/William-kelvem94/Atividade-03
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 11 KB | **Árvore:** 21 arquivos, 0 diretórios
- **README:** README.md (14 caracteres)
- **Manifestos:** nenhum identificado
- **Stack inferida:** Java
- **Objetivo/descrição:** # Atividade-03
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** manifesto de dependências não identificado; testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** declarar dependências e versão de runtime; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/att_18_ago

- **URL:** https://github.com/William-kelvem94/att_18_ago
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 5 KB | **Árvore:** 9 arquivos, 0 diretórios
- **README:** não localizado
- **Manifestos:** nenhum identificado
- **Stack inferida:** PHP
- **Objetivo/descrição:** Objetivo não documentado no README acessível.
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** README ausente ou não acessível; manifesto de dependências não identificado; testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** documentar propósito, instalação, uso e estado; declarar dependências e versão de runtime; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/AULA_PROG_AVAN

- **URL:** https://github.com/William-kelvem94/AULA_PROG_AVAN
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 0 KB | **Árvore:** 1 arquivos, 0 diretórios
- **README:** não localizado
- **Manifestos:** nenhum identificado
- **Stack inferida:** Indeterminada
- **Objetivo/descrição:** Objetivo não documentado no README acessível.
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** README ausente ou não acessível; manifesto de dependências não identificado; testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** documentar propósito, instalação, uso e estado; declarar dependências e versão de runtime; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/Auto-boletos

- **URL:** https://github.com/William-kelvem94/Auto-boletos
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 342 KB | **Árvore:** 94 arquivos, 0 diretórios
- **README:** README.md (14979 caracteres)
- **Manifestos:** `Dockerfile`, `requirements.txt`, `package-lock.json`, `docker-compose.yml`
- **Stack inferida:** Node.js/JavaScript, JavaScript, Vite, Python, Docker, GitHub Actions
- **Objetivo/descrição:** # Auto-boletos ![CI](https://github.com/William-kelvem94/Auto-boletos/actions/workflows/ci.yml) Sistema moderno e completo que associa imóveis cadastrados aos dados oficiais da plataforma Equatorial Energy, **com Sistema de IA Local integrado**.
- **Sinais:** testes=sim, CI=sim, Docker=sim, docs=sim, lockfile=sim
- **Riscos estruturais:** manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** explicitar licença

### Evidência de manifestos

**Dockerfile**

```
# Multi-stage build for optimized Docker image
FROM python:3.11-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies for building Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create and use virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy requirements and install Python dependencies
COPY requirements.txt .
# Note: --trusted-host flags handle SSL certificate issues in some CI/CD environments.
# For production builds with proper SSL configuration, remove these flags by using:
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# Final stage - minimal image
FROM node:20-alpine as frontend-builder
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

```

**requirements.txt**

```
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-CORS==4.0.0
playwright==1.40.0
python-dotenv==1.0.0
Pillow==10.1.0
pytesseract==0.3.10
opencv-python-headless==4.8.1.78
numpy==1.24.3
scikit-learn==1.3.2
joblib==1.3.2
requests==2.32.3

# Production
gunicorn==22.0.0
flask-jwt-extended==4.6.0
tenacity==9.0.0
flask-limiter==3.5.1
structlog==24.4.0

```

**package-lock.json**

```
{
  "name": "Auto-boletos",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {}
}

```


---

## William-kelvem94/AUTOBOT

- **URL:** https://github.com/William-kelvem94/AUTOBOT
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 10191 KB | **Árvore:** 30 arquivos, 0 diretórios
- **README:** README.md (11954 caracteres)
- **Manifestos:** `Makefile`, `Dockerfile`, `requirements.txt`, `web/package.json`
- **Stack inferida:** Node.js/JavaScript, JavaScript, Python, Docker
- **Objetivo/descrição:** # 🤖 AUTOBOT - Sistema de Automação Corporativa ![Python](https://python.org) ![Cross-Platform](/)
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=sim, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**requirements.txt**

```
# AUTOBOT - Sistema de Automação Corporativa
# Core essentials for basic functionality

# === CORE FRAMEWORK (Required) ===
Flask>=3.0.0
Flask-CORS>=4.0.0
python-dotenv>=1.0.0
requests>=2.31.0
pyyaml>=6.0
psutil>=5.9.0

# === WEB AUTOMATION (Core Features) ===
selenium>=4.15.0
# pyautogui>=0.9.54  # Commented due to GUI dependencies

# === PRODUCTION READY ===
gunicorn>=21.2.0
waitress>=3.0.0

# === OPTIONAL: ENHANCED FEATURES ===
# Uncomment these for enhanced functionality
# Flask-JWT-Extended>=4.5.0
# Flask-Limiter>=3.5.0

# === OPTIONAL: AI FEATURES ===
# Uncomment these for AI functionality
# ollama>=0.1.8
# redis>=5.0.0

# === OPTIONAL: ML/AI HEAVY DEPENDENCIES ===
# Only install if AI features are needed
# Install with: pip install -r requirements-ai.txt
# chromadb>=0.4.15
# sentence-transformers>=2.2.2
# torch>=2.0.0
```

**web/package.json**

```
{
  "name": "autobot-web",
  "version": "2.0.0",
  "description": "Frontend React para AUTOBOT - Sistema de Automação Corporativa com IA",
  "main": "src/App.jsx",
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "dev": "npm start"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "axios": "^1.6.0",
    "react-router-dom": "^6.8.0",
    "@mui/material": "^5.15.0",
    "@mui/icons-material": "^5.15.0",
    "@emotion/react": "^11.11.0",
    "@emotion/styled": "^11.11.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0"
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
```


---

## William-kelvem94/Automatizador

- **URL:** https://github.com/William-kelvem94/Automatizador
- **Branch padrão:** `master`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 487 KB | **Árvore:** 80 arquivos, 0 diretórios
- **README:** README.md (13044 caracteres)
- **Manifestos:** `pyproject.toml`, `config/requirements.txt`
- **Stack inferida:** Python, GitHub Actions
- **Objetivo/descrição:** # 🚀 Automatizador IA - Sistema Inteligente v5.0 <div align="center"> <img src="https://img.shields.io/badge/Versão-5.0.0-blue.svg" alt="Version"/>
- **Sinais:** testes=sim, CI=sim, Docker=não evidenciado, docs=sim, lockfile=não evidenciado
- **Riscos estruturais:** branch padrão não é main (master)
- **Lacunas recomendadas:** explicitar licença

### Evidência de manifestos

**pyproject.toml**

```
[tool.black]
line-length = 88
target-version = ['py311']
include = '\.pyi?$'

[tool.isort]
profile = "black"
line_length = 88
multi_line_output = 3

[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q"
testpaths = [
    "tests",
]
python_files = "test_*.py"

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false
disallow_incomplete_defs = false

```

**config/requirements.txt**

```
selenium==4.15.2
apscheduler==3.10.4
webdriver-manager==4.0.1
python-dotenv==1.0.0

# Desenvolvimento
pyinstaller>=6.0.0
pillow>=9.0.0
requests>=2.25.0

```


---

## William-kelvem94/BITRIX-DADOS

- **URL:** https://github.com/William-kelvem94/BITRIX-DADOS
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 50 KB | **Árvore:** 29 arquivos, 0 diretórios
- **README:** README.md (9234 caracteres)
- **Manifestos:** nenhum identificado
- **Stack inferida:** TypeScript
- **Objetivo/descrição:** # Bitrix24 Data Extractor Sistema completo para extração de dados do Bitrix24 através da API REST usando webhooks/integrações. ## 🚀 Funcionalidades
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** manifesto de dependências não identificado; testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** declarar dependências e versão de runtime; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/C.A.I.N.E

- **URL:** https://github.com/William-kelvem94/C.A.I.N.E
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 375 KB | **Árvore:** 27 arquivos, 0 diretórios
- **README:** frontend/README.md (1027 caracteres)
- **Manifestos:** `frontend/package.json`, `backend/requirements.txt`, `batix-chat-agent/package.json`
- **Stack inferida:** Node.js/JavaScript, JavaScript, Vite, Python
- **Objetivo/descrição:** # React + Vite This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules. Currently, two official plugins are available:
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**frontend/package.json**

```
{
  "name": "frontend",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^19.2.6",
    "react-dom": "^19.2.6"
  },
  "devDependencies": {
    "@eslint/js": "^10.0.1",
    "@types/react": "^19.2.14",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^6.0.1",
    "eslint": "^10.3.0",
    "eslint-plugin-react-hooks": "^7.1.1",
    "eslint-plugin-react-refresh": "^0.5.2",
    "globals": "^17.6.0",
    "vite": "^8.0.12"
  }
}

```

**backend/requirements.txt**

```
fastapi
uvicorn[standard]
python-multipart
openai-whisper
ffmpeg-python
transformers
torch
pydantic
python-dotenv

```

**batix-chat-agent/package.json**

```
{
  "name": "batix-chat-agent",
  "version": "1.0.0",
  "description": "Agente inteligente para gerenciar tarefas do Batix localmente",
  "type": "module",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "@google/generative-ai": "^0.21.0",
    "express": "^4.21.2",
    "node-fetch": "^3.3.2",
    "socket.io": "^4.8.1"
  }
}

```


---

## William-kelvem94/CLONNER

- **URL:** https://github.com/William-kelvem94/CLONNER
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 26654 KB | **Árvore:** 159 arquivos, 0 diretórios
- **README:** README.md (8050 caracteres)
- **Manifestos:** `Makefile`, `Dockerfile`, `pyproject.toml`, `requirements.txt`
- **Stack inferida:** JavaScript, Python, Docker, GitHub Actions
- **Objetivo/descrição:** # 🔥 CLONNER - Sistema Profissional de Clonagem de Sites ![Python](https://www.python.org/) ![Flask](https://flask.palletsprojects.com/)
- **Sinais:** testes=sim, CI=sim, Docker=sim, docs=sim, lockfile=não evidenciado
- **Riscos estruturais:** manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** explicitar licença

### Evidência de manifestos

**Makefile**

```
# Makefile para facilitar comandos Docker
.PHONY: help build up down logs restart shell clean dev prod

help: ## Mostrar ajuda
	@echo "🔥 Mega Hybrid Cloner - Comandos Docker"
	@echo ""
	@echo "Comandos disponíveis:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

build: ## Build da imagem Docker
	@echo "🔨 Building Docker image..."
	docker-compose build

up: ## Iniciar containers
	@echo "🚀 Iniciando containers..."
	docker-compose up -d
	@echo "✅ Sistema rodando em http://localhost:5000"

down: ## Parar containers
	@echo "🛑 Parando containers..."
	docker-compose down

logs: ## Ver logs em tempo real
	docker-compose logs -f mega-cloner

restart: ## Reiniciar containers
	@echo "🔄 Reiniciando..."
	docker-compose restart mega-cloner

shell: ## Entrar no container
	docker-compose exec mega-cloner bash

clean: ## Limpar tudo (cuidado!)
	@echo "🧹 Limpando containers, volumes e imagens..."
	docker-compose down -v
```

**Dockerfile**

```
# Cloner Profissional - Docker Image
FROM python:3.11-slim

# Metadados
LABEL maintainer="William"
LABEL description="Cloner Profissional - Sistema de clonagem indetectável completo"
LABEL version="1.0.0"

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive \
    DISPLAY=:99 \
    PYTHONPATH=/app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Chrome e dependências
    wget \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libwayland-client0 \
    libxcomposite1 \
```

**pyproject.toml**

```
[tool.black]
line-length = 120
target-version = ['py38', 'py39', 'py310', 'py311']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | venv
  | env
  | build
  | dist
  | archive
  | migrations
)/
'''

[tool.isort]
profile = "black"
line_length = 120
multi_line_output = 3
include_trailing_comma = true
force_grid_wrap = 0
use_parentheses = true
ensure_newline_before_comments = true
skip = ["archive", "venv", "env", ".venv", "migrations"]
known_first_party = ["src"]

[tool.mypy]
python_version = "3.8"
```

**requirements.txt**

```
Flask==3.0.0
Werkzeug==3.0.1
Flask-CORS==4.0.0
requests==2.31.0
beautifulsoup4==4.12.2
lxml==4.9.3
httpx==0.25.2
selenium==4.16.0
webdriver-manager==4.0.1
undetected-chromedriver==3.5.4
Pillow==10.2.0
colorlog==6.8.0
python-dotenv==1.0.0
fake-useragent==1.4.0
user-agents==2.2.0
defusedxml==0.7.1
jsonschema==4.20.0
memory-profiler==0.61.0
psutil==5.9.8
urllib3==2.1.0

```


---

## William-kelvem94/CONVERSOR-DE-FORMATO-DE-ARQUIVO

- **URL:** https://github.com/William-kelvem94/CONVERSOR-DE-FORMATO-DE-ARQUIVO
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 193 KB | **Árvore:** 99 arquivos, 0 diretórios
- **README:** README.md (8999 caracteres)
- **Manifestos:** `Dockerfile`, `package.json`, `Dockerfile.dev`, `package-lock.json`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Next.js, Docker
- **Objetivo/descrição:** # 🚀 Conversor de Arquivos - Interface Moderna Uma aplicação web moderna para conversão de arquivos com interface espetacular, animações fluidas e efeitos visuais incríveis. Funciona tanto no navegador quanto como aplicativo desktop (Electron). ## ✨ Características
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=sim, docs=não evidenciado, lockfile=sim
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**Dockerfile**

```
# Dockerfile para versão web do Conversor de Arquivos
FROM node:18-alpine AS base

# Instalar dependências do sistema
RUN apk add --no-cache libc6-compat wget

# Stage 1: Instalar dependências (incluindo devDependencies para build)
FROM base AS deps
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci

# Stage 2: Build da aplicação
FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Build da aplicação
ENV DOCKER_BUILD=true
ENV NEXT_TELEMETRY_DISABLED=1
ENV NODE_ENV=production
RUN npm run build

# Stage 3: Instalar apenas dependências de produção
FROM base AS prod-deps
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci --omit=dev && npm cache clean --force

# Stage 4: Imagem de produção
FROM base AS runner
WORKDIR /app

ENV NODE_ENV=production
```

**package.json**

```
{
  "name": "conversor-arquivos-ui",
  "version": "1.0.0",
  "description": "Interface moderna para conversão de arquivos com animações fluidas",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "type-check": "tsc --noEmit",
    "electron": "nextron",
    "electron:dev": "nextron dev",
    "electron:build": "nextron build",
    "electron:build:win": "nextron build --win",
    "docker:build": "docker build -t conversor-arquivos .",
    "docker:run": "docker run -p 3000:3000 conversor-arquivos",
    "docker:dev": "docker-compose up conversor-dev",
    "docker:prod": "docker-compose up conversor-web",
    "docker:down": "docker-compose down",
    "download-ffmpeg": "node scripts/download-ffmpeg.js",
    "postinstall": "npm run download-ffmpeg"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "next": "^14.0.0",
    "framer-motion": "^10.16.4",
    "lucide-react": "^0.294.0",
    "react-dropzone": "^14.2.3",
    "react-hook-form": "^7.47.0",
    "zustand": "^4.4.6",
    "clsx": "^2.0.0",
    "@ffmpeg/ffmpeg": "^0.12.6",
    "@ffmpeg/util": "^0.12.1",
```

**Dockerfile.dev**

```
# Dockerfile para desenvolvimento
FROM node:18-alpine

# Instalar dependências do sistema
RUN apk add --no-cache libc6-compat

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY package.json package-lock.json* ./

# Instalar dependências (incluindo devDependencies)
RUN npm ci

# Copiar código fonte
COPY . .

# Expor porta
EXPOSE 3000

# Variáveis de ambiente
ENV NODE_ENV=development
ENV PORT=3000
ENV NEXT_TELEMETRY_DISABLED=1
ENV WATCHPACK_POLLING=true

# Comando para desenvolvimento
CMD ["npm", "run", "dev"]


```


---

## William-kelvem94/CORETEMP-SOUNDPAD

- **URL:** https://github.com/William-kelvem94/CORETEMP-SOUNDPAD
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 9002 KB | **Árvore:** 194 arquivos, 0 diretórios
- **README:** README.md (769 caracteres)
- **Manifestos:** `TempSound.csproj`, `CORETEMP-SOUNDPAD.sln`
- **Stack inferida:** Indeterminada
- **Objetivo/descrição:** # TempSound TempSound é um aplicativo WinForms para Windows que monitora a temperatura da CPU usando a biblioteca LibreHardwareMonitor e toca áudios personalizados (usando NAudio) ao atingir um limite configurável. ## Funcionalidades
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**TempSound.csproj**

```
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>WinExe</OutputType>
    <TargetFramework>net9.0-windows</TargetFramework>
    <Nullable>enable</Nullable>
    <UseWindowsForms>true</UseWindowsForms>
    <ImplicitUsings>enable</ImplicitUsings>
    <ApplicationManifest>app.manifest</ApplicationManifest>
    <AssemblyName>TempSound</AssemblyName>
    <RootNamespace>TempSound</RootNamespace>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="LibreHardwareMonitorLib" Version="0.9.4" />
    <PackageReference Include="MaterialSkin.2" Version="2.3.1" />
    <PackageReference Include="NAudio" Version="2.2.1" />
    <PackageReference Include="System.Data.SqlClient" Version="4.9.0" />
  </ItemGroup>

  <ItemGroup>
    <Reference Include="System.Windows.Forms.DataVisualization">
      <HintPath>$(OutputPath)System.Windows.Forms.DataVisualization.dll</HintPath>
    </Reference>
  </ItemGroup>

</Project>

```

**CORETEMP-SOUNDPAD.sln**

```
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 17
VisualStudioVersion = 17.5.2.0
MinimumVisualStudioVersion = 10.0.40219.1
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "TempSound", "TempSound.csproj", "{846E484C-9E07-6A6C-EAEF-6696AFF03BA8}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|Any CPU = Debug|Any CPU
		Release|Any CPU = Release|Any CPU
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{846E484C-9E07-6A6C-EAEF-6696AFF03BA8}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{846E484C-9E07-6A6C-EAEF-6696AFF03BA8}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{846E484C-9E07-6A6C-EAEF-6696AFF03BA8}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{846E484C-9E07-6A6C-EAEF-6696AFF03BA8}.Release|Any CPU.Build.0 = Release|Any CPU
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
	GlobalSection(ExtensibilityGlobals) = postSolution
		SolutionGuid = {0B6E2913-15BF-493F-8865-E30D54A9417E}
	EndGlobalSection
EndGlobal

```


---

## William-kelvem94/Criador_de_audios

- **URL:** https://github.com/William-kelvem94/Criador_de_audios
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 17372 KB | **Árvore:** 233 arquivos, 0 diretórios
- **README:** README.md (11443 caracteres)
- **Manifestos:** `Makefile`, `pyproject.toml`, `docker-compose.yml`, `docker/tts/Dockerfile.tts`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite, Python, Docker, GitHub Actions
- **Objetivo/descrição:** # 🚀 Criador de Áudios v3.0 **Sistema Completo de Geração e Clonagem de Áudio com Inteligência Artificial** ![Docker](https://docker.com)
- **Sinais:** testes=sim, CI=sim, Docker=sim, docs=sim, lockfile=sim
- **Riscos estruturais:** possível material sensível/configuração ambiental na árvore; revisar segredos; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** explicitar licença

### Evidência de manifestos

**pyproject.toml**

```
# 📦 Criador de Áudios v3.0 - Poetry Configuration
# pyproject.toml otimizado com Poetry para gerenciamento inteligente de dependências

[tool.poetry]
name = "criador-audios"
version = "3.0.0"
description = "Sistema avançado de conversão de texto para fala com arquitetura de microserviços adaptativa"
authors = ["William Pereira <william@criador.dev>"]
maintainers = ["Criador de Áudios Team <team@criador.dev>"]
license = "MIT"
readme = "README.md"
homepage = "https://github.com/William-kelvem94/Criador_de_audios"
repository = "https://github.com/William-kelvem94/Criador_de_audios"
documentation = "https://criador-audios.readthedocs.io/"
keywords = ["tts", "text-to-speech", "voice-synthesis", "ai", "microservices", "adaptive"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Multimedia :: Sound/Audio :: Speech",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
packages = [{include = "src"}]

[tool.poetry.dependencies]
python = "^3.10"

# 🌐 Web Frameworks (Core)
fastapi = {version = "^0.104.1", extras = ["all"]}
```


---

## William-kelvem94/crud_basico

- **URL:** https://github.com/William-kelvem94/crud_basico
- **Branch padrão:** `master`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 71 KB | **Árvore:** 113 arquivos, 0 diretórios
- **README:** README.md (4158 caracteres)
- **Manifestos:** `package.json`, `composer.json`
- **Stack inferida:** Node.js/JavaScript, JavaScript, Vite, PHP
- **Objetivo/descrição:** <p align="center"><a href="https://laravel.com" target="_blank"><img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="400" alt="Laravel Logo"></a></p> <p align="center"> <a href="https://github.com/laravel/framework/actions"><img src="https://github.com/laravel/framework/workflows/tests/badge.svg" alt="Build Status"></a>
- **Sinais:** testes=sim, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** CI/CD não evidenciado; branch padrão não é main (master)
- **Lacunas recomendadas:** definir pipeline mínimo de validação; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**package.json**

```
{
    "private": true,
    "type": "module",
    "scripts": {
        "dev": "vite",
        "build": "vite build"
    },
    "devDependencies": {
        "axios": "^1.1.2",
        "laravel-vite-plugin": "^0.8.0",
        "vite": "^4.0.0"
    }
}

```

**composer.json**

```
{
    "name": "laravel/laravel",
    "type": "project",
    "description": "The skeleton application for the Laravel framework.",
    "keywords": ["laravel", "framework"],
    "license": "MIT",
    "require": {
        "php": "^8.1",
        "guzzlehttp/guzzle": "^7.2",
        "laravel/framework": "^10.10",
        "laravel/sanctum": "^3.2",
        "laravel/tinker": "^2.8"
    },
    "require-dev": {
        "fakerphp/faker": "^1.9.1",
        "laravel/pint": "^1.0",
        "laravel/sail": "^1.18",
        "mockery/mockery": "^1.4.4",
        "nunomaduro/collision": "^7.0",
        "phpunit/phpunit": "^10.1",
        "spatie/laravel-ignition": "^2.0"
    },
    "autoload": {
        "psr-4": {
            "App\\": "app/",
            "Database\\Factories\\": "database/factories/",
            "Database\\Seeders\\": "database/seeders/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "Tests\\": "tests/"
        }
    },
    "scripts": {
```


---

## William-kelvem94/crud_basico-2.0

- **URL:** https://github.com/William-kelvem94/crud_basico-2.0
- **Branch padrão:** `master`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 0 KB | **Árvore:** 113 arquivos, 0 diretórios
- **README:** README.md (4158 caracteres)
- **Manifestos:** `package.json`, `composer.json`
- **Stack inferida:** Node.js/JavaScript, JavaScript, Vite, PHP
- **Objetivo/descrição:** <p align="center"><a href="https://laravel.com" target="_blank"><img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="400" alt="Laravel Logo"></a></p> <p align="center"> <a href="https://github.com/laravel/framework/actions"><img src="https://github.com/laravel/framework/workflows/tests/badge.svg" alt="Build Status"></a>
- **Sinais:** testes=sim, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** CI/CD não evidenciado; branch padrão não é main (master)
- **Lacunas recomendadas:** definir pipeline mínimo de validação; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**package.json**

```
{
    "private": true,
    "type": "module",
    "scripts": {
        "dev": "vite",
        "build": "vite build"
    },
    "devDependencies": {
        "axios": "^1.1.2",
        "laravel-vite-plugin": "^0.8.0",
        "vite": "^4.0.0"
    }
}

```

**composer.json**

```
{
    "name": "laravel/laravel",
    "type": "project",
    "description": "The skeleton application for the Laravel framework.",
    "keywords": ["laravel", "framework"],
    "license": "MIT",
    "require": {
        "php": "^8.1",
        "guzzlehttp/guzzle": "^7.2",
        "laravel/framework": "^10.10",
        "laravel/sanctum": "^3.2",
        "laravel/tinker": "^2.8"
    },
    "require-dev": {
        "fakerphp/faker": "^1.9.1",
        "laravel/pint": "^1.0",
        "laravel/sail": "^1.18",
        "mockery/mockery": "^1.4.4",
        "nunomaduro/collision": "^7.0",
        "phpunit/phpunit": "^10.1",
        "spatie/laravel-ignition": "^2.0"
    },
    "autoload": {
        "psr-4": {
            "App\\": "app/",
            "Database\\Factories\\": "database/factories/",
            "Database\\Seeders\\": "database/seeders/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "Tests\\": "tests/"
        }
    },
    "scripts": {
```


---

## William-kelvem94/CRUD_BASICO-3.0

- **URL:** https://github.com/William-kelvem94/CRUD_BASICO-3.0
- **Branch padrão:** `master`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 71 KB | **Árvore:** 113 arquivos, 0 diretórios
- **README:** README.md (4158 caracteres)
- **Manifestos:** `package.json`, `composer.json`
- **Stack inferida:** Node.js/JavaScript, JavaScript, Vite, PHP
- **Objetivo/descrição:** <p align="center"><a href="https://laravel.com" target="_blank"><img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="400" alt="Laravel Logo"></a></p> <p align="center"> <a href="https://github.com/laravel/framework/actions"><img src="https://github.com/laravel/framework/workflows/tests/badge.svg" alt="Build Status"></a>
- **Sinais:** testes=sim, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** CI/CD não evidenciado; branch padrão não é main (master)
- **Lacunas recomendadas:** definir pipeline mínimo de validação; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**package.json**

```
{
    "private": true,
    "type": "module",
    "scripts": {
        "dev": "vite",
        "build": "vite build"
    },
    "devDependencies": {
        "axios": "^1.1.2",
        "laravel-vite-plugin": "^0.8.0",
        "vite": "^4.0.0"
    }
}

```

**composer.json**

```
{
    "name": "laravel/laravel",
    "type": "project",
    "description": "The skeleton application for the Laravel framework.",
    "keywords": ["laravel", "framework"],
    "license": "MIT",
    "require": {
        "php": "^8.1",
        "guzzlehttp/guzzle": "^7.2",
        "laravel/framework": "^10.10",
        "laravel/sanctum": "^3.2",
        "laravel/tinker": "^2.8"
    },
    "require-dev": {
        "fakerphp/faker": "^1.9.1",
        "laravel/pint": "^1.0",
        "laravel/sail": "^1.18",
        "mockery/mockery": "^1.4.4",
        "nunomaduro/collision": "^7.0",
        "phpunit/phpunit": "^10.1",
        "spatie/laravel-ignition": "^2.0"
    },
    "autoload": {
        "psr-4": {
            "App\\": "app/",
            "Database\\Factories\\": "database/factories/",
            "Database\\Seeders\\": "database/seeders/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "Tests\\": "tests/"
        }
    },
    "scripts": {
```


---

## William-kelvem94/CRUD_BASICO4.0

- **URL:** https://github.com/William-kelvem94/CRUD_BASICO4.0
- **Branch padrão:** `master`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 71 KB | **Árvore:** 113 arquivos, 0 diretórios
- **README:** README.md (4158 caracteres)
- **Manifestos:** `package.json`, `composer.json`
- **Stack inferida:** Node.js/JavaScript, JavaScript, Vite, PHP
- **Objetivo/descrição:** <p align="center"><a href="https://laravel.com" target="_blank"><img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="400" alt="Laravel Logo"></a></p> <p align="center"> <a href="https://github.com/laravel/framework/actions"><img src="https://github.com/laravel/framework/workflows/tests/badge.svg" alt="Build Status"></a>
- **Sinais:** testes=sim, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** CI/CD não evidenciado; branch padrão não é main (master)
- **Lacunas recomendadas:** definir pipeline mínimo de validação; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**package.json**

```
{
    "private": true,
    "type": "module",
    "scripts": {
        "dev": "vite",
        "build": "vite build"
    },
    "devDependencies": {
        "axios": "^1.1.2",
        "laravel-vite-plugin": "^0.8.0",
        "vite": "^4.0.0"
    }
}

```

**composer.json**

```
{
    "name": "laravel/laravel",
    "type": "project",
    "description": "The skeleton application for the Laravel framework.",
    "keywords": ["laravel", "framework"],
    "license": "MIT",
    "require": {
        "php": "^8.1",
        "guzzlehttp/guzzle": "^7.2",
        "laravel/framework": "^10.10",
        "laravel/sanctum": "^3.2",
        "laravel/tinker": "^2.8"
    },
    "require-dev": {
        "fakerphp/faker": "^1.9.1",
        "laravel/pint": "^1.0",
        "laravel/sail": "^1.18",
        "mockery/mockery": "^1.4.4",
        "nunomaduro/collision": "^7.0",
        "phpunit/phpunit": "^10.1",
        "spatie/laravel-ignition": "^2.0"
    },
    "autoload": {
        "psr-4": {
            "App\\": "app/",
            "Database\\Factories\\": "database/factories/",
            "Database\\Seeders\\": "database/seeders/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "Tests\\": "tests/"
        }
    },
    "scripts": {
```


---

## William-kelvem94/CRUD_VENDAS_WILL

- **URL:** https://github.com/William-kelvem94/CRUD_VENDAS_WILL
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 73 KB | **Árvore:** 105 arquivos, 0 diretórios
- **README:** README.md (18 caracteres)
- **Manifestos:** `CRUD_VENDAS_WILL/package.json`, `CRUD_VENDAS_WILL/composer.json`
- **Stack inferida:** Node.js/JavaScript, JavaScript, PHP
- **Objetivo/descrição:** # CRUD_VENDAS_WILL
- **Sinais:** testes=sim, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**CRUD_VENDAS_WILL/package.json**

```
{
    "private": true,
    "scripts": {
        "dev": "npm run development",
        "development": "mix",
        "watch": "mix watch",
        "watch-poll": "mix watch -- --watch-options-poll=1000",
        "hot": "mix watch --hot",
        "prod": "npm run production",
        "production": "mix --production"
    },
    "devDependencies": {
        "axios": "^0.21",
        "laravel-mix": "^6.0.6",
        "lodash": "^4.17.19",
        "postcss": "^8.1.14"
    }
}

```

**CRUD_VENDAS_WILL/composer.json**

```
{
    "name": "laravel/laravel",
    "type": "project",
    "description": "The Laravel Framework.",
    "keywords": ["framework", "laravel"],
    "license": "MIT",
    "require": {
        "php": "^7.3|^8.0",
        "fruitcake/laravel-cors": "^2.0",
        "guzzlehttp/guzzle": "^7.0.1",
        "laravel/framework": "^8.75",
        "laravel/sanctum": "^2.11",
        "laravel/tinker": "^2.5"
    },
    "require-dev": {
        "facade/ignition": "^2.5",
        "fakerphp/faker": "^1.9.1",
        "laravel/sail": "^1.0.1",
        "mockery/mockery": "^1.4.4",
        "nunomaduro/collision": "^5.10",
        "phpunit/phpunit": "^9.5.10"
    },
    "autoload": {
        "psr-4": {
            "App\\": "app/",
            "Database\\Factories\\": "database/factories/",
            "Database\\Seeders\\": "database/seeders/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "Tests\\": "tests/"
        }
    },
    "scripts": {
```


---

## William-kelvem94/DEEP-LEARNING

- **URL:** https://github.com/William-kelvem94/DEEP-LEARNING
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 909 KB | **Árvore:** 45 arquivos, 0 diretórios
- **README:** README.md (2052 caracteres)
- **Manifestos:** `requirements.txt`
- **Stack inferida:** JavaScript, Python
- **Objetivo/descrição:** # Deep Learning Project - Sumário ## Projeto - **Objetivo**: Implementar um sistema de deep learning para automatizar processos de negócios, como análise de sentimentos em textos, previsão de vendas e suporte a chatbots personalizados.
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**requirements.txt**

```
# ============================================================
# JARVIS - Dependências do Projeto
# Versões verificadas no venv (Python 3.14)
# ============================================================

# --- Backend API ---
fastapi>=0.135.0
uvicorn>=0.42.0
python-multipart>=0.0.22
websockets>=16.0

# --- LLM (OpenAI SDK — suporta OpenAI E LM Studio via base_url) ---
openai>=2.30.0

# --- Embeddings e RAG ---
sentence-transformers>=5.0.0    # all-MiniLM-L6-v2 (CPU, 22MB)
numpy>=2.0.0

# --- Text to Speech ---
edge-tts>=7.0.0                 # TTS gratuito via Microsoft Edge

# --- Ferramentas / Tools ---
duckduckgo-search>=8.0.0        # Busca web gratuita
requests>=2.33.0
psutil>=7.0.0                   # Info de sistema (CPU, RAM, disco)
pillow>=12.0.0                  # Screenshots
opencv-python>=4.8.0            # Suporte a Câmera / Visão Computacional
httpx>=0.28.0

# --- Banco de Dados ---
aiosqlite>=0.22.0               # SQLite assíncrono

# --- Utilitários ---
python-dotenv>=1.0.0
pydantic>=2.12.0
```


---

## William-kelvem94/DEEPSEEK-JARVIS-LOCAL

- **URL:** https://github.com/William-kelvem94/DEEPSEEK-JARVIS-LOCAL
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 609 KB | **Árvore:** 42 arquivos, 0 diretórios
- **README:** deepseek-local/README.md (6431 caracteres)
- **Manifestos:** `jarvis-ai/Dockerfile`, `jarvis-ai/requirements.txt`, `jarvis-ai/docker-compose.yml`, `deepseek-local/requirements.txt`
- **Stack inferida:** Python, Docker
- **Objetivo/descrição:** # 🤖 DEEPSEEK LOCAL **SUA CÓPIA LOCAL INTELIGENTE DO DEEPSEEK WEB** Sistema de IA local que roda no seu hardware (8GB RAM + GTX 1050ti) com todas as funcionalidades do DeepSeek Web, mas **SEM LIMITAÇÕES**!
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=sim, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**jarvis-ai/Dockerfile**

```
# 🚀 JARVIS-AI - DOCKERFILE PROFISSIONAL
# Multi-stage build otimizado para CPU/GPU com Ollama

# ==================================
# STAGE 1: Base com Ollama
# ==================================
FROM nvidia/cuda:12.1-devel-ubuntu22.04 as base

# Metadados
LABEL maintainer="Jarvis-AI"
LABEL version="1.0"
LABEL description="Professional AI Assistant with Ollama and serious models"

# Variáveis de ambiente
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV OLLAMA_HOST=0.0.0.0
ENV OLLAMA_PORT=11434

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    python3 \
    python3-pip \
    python3-venv \
    build-essential \
    software-properties-common \
    ca-certificates \
    gnupg \
    lsb-release \
    htop \
    nvtop \
```

**jarvis-ai/requirements.txt**

```
# 🔧 JARVIS-AI - DEPENDÊNCIAS PROFISSIONAIS
# Otimizado para performance e estabilidade

# ==================================
# CORE BACKEND
# ==================================
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
pydantic-settings==2.1.0

# ==================================
# FRONTEND WEB
# ==================================
streamlit==1.28.2
streamlit-chat==0.1.1
streamlit-option-menu==0.3.6

# ==================================
# OLLAMA & AI
# ==================================
ollama==0.1.7
httpx==0.25.2
aiohttp==3.9.1
requests==2.31.0

# ==================================
# DATABASE & STORAGE
# ==================================
sqlalchemy==2.0.23
sqlite3
aiosqlite==0.19.0
sqlmodel==0.0.14

# ==================================
```

**jarvis-ai/docker-compose.yml**

```
# 🐳 JARVIS-AI - DOCKER COMPOSE PROFISSIONAL
# Orquestração completa com GPU support e volumes persistentes

version: '3.8'

services:
  # ==================================
  # JARVIS-AI MAIN SERVICE
  # ==================================
  jarvis-ai:
    build:
      context: .
      dockerfile: Dockerfile
      target: app
    container_name: jarvis-ai
    hostname: jarvis-ai
    restart: unless-stopped
    
    # Portas
    ports:
      - "8000:8000"    # FastAPI Backend
      - "8501:8501"    # Streamlit Frontend
      - "11434:11434"  # Ollama API
    
    # Volumes persistentes
    volumes:
      - jarvis_data:/app/data
      - jarvis_logs:/app/logs
      - jarvis_models:/root/.ollama
      - ./config:/app/config:ro
    
    # Variáveis de ambiente
    environment:
      - ENVIRONMENT=production
      - LOG_LEVEL=info
```

**deepseek-local/requirements.txt**

```
# IA LOCAL CORE
transformers>=4.35.0
torch>=2.0.0
tokenizers>=0.14.0
accelerate>=0.24.0

# OLLAMA INTEGRATION
ollama>=0.1.7
requests>=2.31.0

# MODELOS LOCAIS OTIMIZADOS
optimum[onnxruntime]>=1.16.0
bitsandbytes>=0.41.0  # Quantização 4-bit

# MEMÓRIA PERSISTENTE
sqlalchemy>=2.0.0
# sqlite3 é built-in no Python

# CLI SIMPLES
rich>=13.0.0
click>=8.0.0

# PERFORMANCE
psutil>=5.9.0
numpy>=1.24.0

# OPCIONAL - GPU (1050ti)
# torchaudio  # Para modelos de áudio (opcional)
```


---

## William-kelvem94/DeepSeek-V3---C-PIA

- **URL:** https://github.com/William-kelvem94/DeepSeek-V3---C-PIA
- **Branch padrão:** `main`
- **Visibilidade:** public | **Arquivado:** não
- **Tamanho GitHub:** 1699 KB | **Árvore:** 27 arquivos, 0 diretórios
- **README:** README.md (23957 caracteres)
- **Manifestos:** `inference/requirements.txt`
- **Stack inferida:** Python, GitHub Actions
- **Objetivo/descrição:** <!-- markdownlint-disable first-line-h1 --> <!-- markdownlint-disable html --> <!-- markdownlint-disable no-duplicate-header -->
- **Sinais:** testes=não evidenciado, CI=sim, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore
- **Lacunas recomendadas:** criar testes automatizados; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**inference/requirements.txt**

```
torch==2.4.1
triton==3.0.0
transformers==4.46.3
safetensors==0.4.5
```


---

## William-kelvem94/demandas-organizadas

- **URL:** https://github.com/William-kelvem94/demandas-organizadas
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 96353 KB | **Árvore:** 19894 arquivos, 0 diretórios
- **README:** README.md (1030 caracteres)
- **Manifestos:** `package.json`, `package-lock.json`, `backend/Dockerfile`, `docker-compose.yml`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite, Python, Docker
- **Objetivo/descrição:** # Demandas Organizadas Umbrella repository for the Demandas Organizadas family. ## Status
- **Sinais:** testes=sim, CI=não evidenciado, Docker=sim, docs=sim, lockfile=sim
- **Riscos estruturais:** possível material sensível/configuração ambiental na árvore; revisar segredos; CI/CD não evidenciado; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação

### Evidência de manifestos

**package.json**

```
{
  "name": "demandas-organizadas",
  "version": "2.0.0",
  "type": "module",
  "description": "Sistema Premium de Gestão de Demandas com Docker",
  "scripts": {
    "setup": "node scripts/setup/setup.js",
    "dev:services": "docker-compose -f docker-compose.dev.yml up -d postgres redis adminer",
    "dev:backend": "cd backend && npm run dev",
    "dev:frontend": "cd frontend && npm run dev",
    "dev": "concurrently \"npm run dev:services\" \"wait-on tcp:5432 && npm run dev:backend\" \"npm run dev:frontend\"",
    "validate": "cd backend && npm run validate",
    "test": "cd backend && npm test && cd ../frontend && npm test",
    "build": "cd frontend && npm run build",
    "start": "docker-compose up --build -d",
    "stop": "docker-compose down",
    "stop:dev": "docker-compose -f docker-compose.dev.yml down",
    "logs": "docker-compose logs -f",
    "logs:dev": "docker-compose -f docker-compose.dev.yml logs -f",
    "restart": "docker-compose restart",
    "clean": "docker-compose down -v && docker-compose -f docker-compose.dev.yml down -v",
    "clean:all": "npm run clean && cd backend && npm run clean && cd ../frontend && npm run clean",
    "update": "npm update && cd backend && npm update && cd ../frontend && npm update",
    "audit": "npm audit && cd backend && npm audit && cd ../frontend && npm audit"
  },
  "dependencies": {
    "googleapis": "^159.0.0",
    "winston": "^3.14.2"
  },
  "devDependencies": {
    "concurrently": "^9.0.1",
    "wait-on": "^8.0.1"
  },
  "keywords": [
    "demandas",
```


---

## William-kelvem94/demandas-organizadas-v2-legacy

- **URL:** https://github.com/William-kelvem94/demandas-organizadas-v2-legacy
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 128153 KB | **Árvore:** 12121 arquivos, 0 diretórios
- **README:** README.md (532 caracteres)
- **Manifestos:** `yarn.lock`, `Cargo.lock`, `Cargo.toml`, `package.json`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite, Gradle/Android or JVM, Android, Kotlin, Java, Rust, Docker, GitHub Actions
- **Objetivo/descrição:** # Demandas Organizadas 2.0 Legacy snapshot of the second generation of the Demandas Organizadas line. ## Status
- **Sinais:** testes=sim, CI=sim, Docker=sim, docs=sim, lockfile=sim
- **Riscos estruturais:** possível material sensível/configuração ambiental na árvore; revisar segredos; dependência/configuração usa marcador latest; baixa reprodutibilidade; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** nenhuma lacuna estrutural básica detectada

### Evidência de manifestos

**Cargo.toml**

```
[workspace]
members = [
  "./packages/backend/native",
  "./packages/common/native",
  "./packages/common/y-octo/core",
  "./packages/common/y-octo/utils",
  "./packages/frontend/mobile-native",
  "./packages/frontend/native",
  "./packages/frontend/native/nbstore",
  "./packages/frontend/native/schema",
  "./packages/frontend/native/sqlite_v1",
]
resolver = "3"

  [workspace.package]
  edition = "2024"

  [workspace.dependencies]
  affine_common = { path = "./packages/common/native" }
  affine_nbstore = { path = "./packages/frontend/native/nbstore" }
  ahash = "0.8"
  anyhow = "1"
  arbitrary = { version = "1.3", features = ["derive"] }
  assert-json-diff = "2.0"
  async-lock = { version = "3.4.0", features = ["loom"] }
  base64-simd = "0.8"
  bitvec = "1.0"
  block2 = "0.6"
  byteorder = "1.5"
  chrono = "0.4"
  clap = { version = "4.4", features = ["derive"] }
  core-foundation = "0.10"
  coreaudio-rs = "0.12"
  cpal = "0.15"
  criterion = { version = "0.5", features = ["html_reports"] }
```

**package.json**

```
{
  "name": "@affine/monorepo",
  "version": "0.26.3",
  "private": true,
  "author": "William Kelvem Pereira",
  "license": "MIT",
  "workspaces": [
    ".",
    "blocksuite/**/*",
    "packages/*/*",
    "packages/frontend/apps/*",
    "tools/*",
    "docs/reference",
    "tools/@types/*",
    "tests/*"
  ],
  "engines": {
    "node": "<23.0.0"
  },
  "scripts": {
    "affine": "r affine.ts",
    "af": "r affine.ts",
    "dev": "yarn affine dev",
    "build": "yarn affine build",
    "lint:eslint": "cross-env NODE_OPTIONS=\"--max-old-space-size=16384\" eslint --report-unused-disable-directives-severity=off . --cache",
    "lint:eslint:fix": "yarn lint:eslint --fix --fix-type problem,suggestion,layout",
    "lint:prettier": "prettier --ignore-unknown --cache --check .",
    "lint:prettier:fix": "prettier --ignore-unknown --cache --write .",
    "lint:ox": "oxlint --deny-warnings",
    "lint:ox:fix": "yarn lint:ox --fix",
    "lint": "yarn lint:ox && yarn lint:eslint && yarn lint:prettier",
    "lint:fix": "yarn lint:ox:fix && yarn lint:eslint:fix && yarn lint:prettier:fix",
    "test": "vitest --run",
    "test:ui": "vitest --ui",
    "test:coverage": "vitest run --coverage",
```


---

## William-kelvem94/demandas-organizadas-v3-experimental

- **URL:** https://github.com/William-kelvem94/demandas-organizadas-v3-experimental
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 67 KB | **Árvore:** 29 arquivos, 0 diretórios
- **README:** README.md (522 caracteres)
- **Manifestos:** `package.json`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite
- **Objetivo/descrição:** # Demandas Organizadas 3.0 Experimental prototype for the Demandas Organizadas line. ## Status
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**package.json**

```
{
  "name": "demandas-organizadas-v3-experimental",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "tsx server.ts",
    "build": "vite build && esbuild server.ts --bundle --platform=node --format=cjs --packages=external --sourcemap --outfile=dist/server.cjs",
    "start": "node dist/server.cjs",
    "clean": "rm -rf dist server.js",
    "lint": "tsc --noEmit"
  },
  "dependencies": {
    "@google/genai": "^1.29.0",
    "@tailwindcss/vite": "^4.1.14",
    "@vitejs/plugin-react": "^5.0.4",
    "lucide-react": "^0.546.0",
    "react": "^19.0.1",
    "react-dom": "^19.0.1",
    "vite": "^6.2.3",
    "express": "^4.21.2",
    "dotenv": "^17.2.3",
    "motion": "^12.23.24"
  },
  "devDependencies": {
    "@types/node": "^22.14.0",
    "autoprefixer": "^10.4.21",
    "esbuild": "^0.25.0",
    "tailwindcss": "^4.1.14",
    "tsx": "^4.21.0",
    "typescript": "~5.8.2",
    "vite": "^6.2.3",
    "@types/express": "^4.17.21"
  }
}
```


---

## William-kelvem94/Dev.Finances

- **URL:** https://github.com/William-kelvem94/Dev.Finances
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 681 KB | **Árvore:** 43 arquivos, 0 diretórios
- **README:** README.md (2040 caracteres)
- **Manifestos:** nenhum identificado
- **Stack inferida:** JavaScript
- **Objetivo/descrição:** <h1 align="center"> <br> <img src="./.github/logo-dev-finances.png" width="500" heigh="150" alt="logo Dev.Finances">
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** manifesto de dependências não identificado; testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** declarar dependências e versão de runtime; definir pipeline mínimo de validação; criar testes automatizados; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/DIA-DAS-MULHERES

- **URL:** https://github.com/William-kelvem94/DIA-DAS-MULHERES
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 62388 KB | **Árvore:** 129 arquivos, 0 diretórios
- **README:** README.md (5211 caracteres)
- **Manifestos:** nenhum identificado
- **Stack inferida:** JavaScript, Python
- **Objetivo/descrição:** # 💖 Feliz Dia das Mulheres — Página Personalizada > Uma página web feita com amor para celebrar o Dia Internacional da Mulher, dedicada à pessoa mais especial da vida. 🌐 **Acesse ao vivo:** william-kelvem94.github.io/DIA-DAS-MULHERES
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** manifesto de dependências não identificado; testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** declarar dependências e versão de runtime; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/Domni

- **URL:** https://github.com/William-kelvem94/Domni
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 102593 KB | **Árvore:** 2245 arquivos, 0 diretórios
- **README:** README.md (8885 caracteres)
- **Manifestos:** `Dockerfile`, `package.json`, `package-lock.json`, `config/docker/Dockerfile`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Next.js, Python, Docker, GitHub Actions
- **Objetivo/descrição:** # Domni ![Version](#) ![Status](#)
- **Sinais:** testes=sim, CI=sim, Docker=sim, docs=sim, lockfile=sim
- **Riscos estruturais:** possível material sensível/configuração ambiental na árvore; revisar segredos; dependência/configuração usa marcador latest; baixa reprodutibilidade; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** explicitar licença

### Evidência de manifestos

**Dockerfile**

```

# ============================================================
# GESTOR DE ALUGUEL 2.0 - DOCKERFILE
# ============================================================
# Build otimizado para produção usando o servidor customizado
# que inicializa Next.js + Socket.IO no mesmo processo.
# ============================================================

FROM node:20.20-alpine AS builder

RUN apk add --no-cache libc6-compat openssl

WORKDIR /app

COPY package.json package-lock.json ./
COPY prisma ./prisma/

# Prisma/Next exigem URLs sintaticamente válidas para gerar artefatos, mas o
# builder não recebe credenciais reais. O estágio runner não herda estes ENV.
ENV DATABASE_URL=postgresql://build.invalid/domni
ENV DIRECT_URL=postgresql://build.invalid/domni
ENV DOMNI_BUILD_PHASE=1

RUN npm ci
RUN npx prisma generate

COPY . .

ENV NEXT_TELEMETRY_DISABLED=1
ENV NODE_ENV=production
RUN npm run build

FROM node:20.20-alpine AS runner

WORKDIR /app
```

**package.json**

```
{
  "name": "domni",
  "version": "1.0.0-beta.1",
  "private": true,
  "description": "Sistema moderno para gestão de imóveis, inquilinos, contratos e pagamentos",
  "author": "William-kelvem94",
  "engines": {
    "node": ">=22.19.0"
  },
  "scripts": {
    "dev": "npx prisma generate && tsx server.ts",
    "build": "npx prisma generate && next build --webpack",
    "start": "NODE_ENV=production tsx server.ts",
    "lint": "eslint src server.ts instrumentation.ts sentry.*.config.ts --max-warnings=0",
    "lint:eslint": "npm run lint",
    "type-check": "tsc --noEmit",
    "check:responsive": "node scripts/maintenance/fix-responsive-sizes.js --check",
    "qa:responsive:static": "node scripts/maintenance/audit-responsive-layouts.js --strict",
    "qa:responsive:seed": "tsx scripts/e2e/seed-responsive-qa.ts",
    "qa:responsive": "node scripts/maintenance/run-responsive-qa.js",
    "test": "jest --config config/testing/jest.config.js",
    "test:watch": "jest --config config/testing/jest.config.js --watch",
    "test:coverage": "jest --config config/testing/jest.config.js --coverage",
    "test:e2e": "playwright test",
    "test:e2e:responsive": "playwright test --config=playwright.responsive.config.ts",
    "test:e2e:responsive:update": "cross-env RESPONSIVE_VISUAL_BASELINE=true playwright test --config=playwright.responsive.config.ts --update-snapshots",
    "qa:simulators": "powershell -ExecutionPolicy Bypass -File automation/user-simulators/scripts/run-user-simulators.ps1",
    "db:generate": "prisma generate",
    "db:deploy": "prisma migrate deploy",
    "db:studio": "prisma studio",
    "db:migrate": "prisma migrate dev",
    "db:reset": "prisma migrate reset",
    "db:seed": "tsx prisma/seed.ts",
    "data:massive-real": "tsx scripts/data/generate-massive-real.ts",
    "docker:dev": "docker compose -f config/docker/docker-compose.yml up -d",
```

**package-lock.json**

```
{
  "name": "domni",
  "version": "1.0.0-beta.1",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "domni",
      "version": "1.0.0-beta.1",
      "hasInstallScript": true,
      "dependencies": {
        "@google/generative-ai": "^0.24.0",
        "@hookform/resolvers": "^3.10.0",
        "@prisma/client": "^5.19.1",
        "@radix-ui/react-accordion": "^1.1.2",
        "@radix-ui/react-alert-dialog": "^1.1.15",
        "@radix-ui/react-avatar": "^1.1.10",
        "@radix-ui/react-checkbox": "^1.3.3",
        "@radix-ui/react-collapsible": "^1.0.3",
        "@radix-ui/react-context-menu": "^2.1.5",
        "@radix-ui/react-dialog": "^1.1.15",
        "@radix-ui/react-dropdown-menu": "^2.1.16",
        "@radix-ui/react-hover-card": "^1.0.7",
        "@radix-ui/react-label": "^2.1.7",
        "@radix-ui/react-menubar": "^1.0.4",
        "@radix-ui/react-navigation-menu": "^1.1.4",
        "@radix-ui/react-popover": "^1.0.7",
        "@radix-ui/react-progress": "^1.0.3",
        "@radix-ui/react-radio-group": "^1.1.3",
        "@radix-ui/react-scroll-area": "^1.2.10",
        "@radix-ui/react-select": "^2.2.6",
        "@radix-ui/react-separator": "^1.1.7",
        "@radix-ui/react-slider": "^1.1.2",
        "@radix-ui/react-slot": "^1.0.2",
        "@radix-ui/react-switch": "^1.2.6",
```


---

## William-kelvem94/Empresa-de-Agentes

- **URL:** https://github.com/William-kelvem94/Empresa-de-Agentes
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 3262 KB | **Árvore:** 284 arquivos, 0 diretórios
- **README:** README.md (1771 caracteres)
- **Manifestos:** `app/package.json`, `server/package.json`, `app/package-lock.json`, `server/package-lock.json`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite, Python
- **Objetivo/descrição:** # Empresa Local de Agentes Bem-vindo(a) ao universo da Empresa de Agentes! ## Navegue pelo Projeto
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=sim
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**app/package.json**

```
{
  "name": "my-app",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "@hookform/resolvers": "^5.2.2",
    "@radix-ui/react-accordion": "^1.2.12",
    "@radix-ui/react-alert-dialog": "^1.1.15",
    "@radix-ui/react-aspect-ratio": "^1.1.8",
    "@radix-ui/react-avatar": "^1.1.11",
    "@radix-ui/react-checkbox": "^1.3.3",
    "@radix-ui/react-collapsible": "^1.1.12",
    "@radix-ui/react-context-menu": "^2.2.16",
    "@radix-ui/react-dialog": "^1.1.15",
    "@radix-ui/react-dropdown-menu": "^2.1.16",
    "@radix-ui/react-hover-card": "^1.1.15",
    "@radix-ui/react-label": "^2.1.8",
    "@radix-ui/react-menubar": "^1.1.16",
    "@radix-ui/react-navigation-menu": "^1.2.14",
    "@radix-ui/react-popover": "^1.1.15",
    "@radix-ui/react-progress": "^1.1.8",
    "@radix-ui/react-radio-group": "^1.3.8",
    "@radix-ui/react-scroll-area": "^1.2.10",
    "@radix-ui/react-select": "^2.2.6",
    "@radix-ui/react-separator": "^1.1.8",
    "@radix-ui/react-slider": "^1.3.6",
    "@radix-ui/react-slot": "^1.2.4",
    "@radix-ui/react-switch": "^1.2.6",
```

**server/package.json**

```
{
  "name": "copilot-server",
  "private": true,
  "type": "module",
  "scripts": {
    "start": "node index.js",
    "dev": "node --watch index.js"
  },
  "dependencies": {
    "dotenv": "^16.4.7",
    "express": "^5.1.0"
  }
}

```


---

## William-kelvem94/extra-o-de-ideias

- **URL:** https://github.com/William-kelvem94/extra-o-de-ideias
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 2449 KB | **Árvore:** 32 arquivos, 0 diretórios
- **README:** não localizado
- **Manifestos:** nenhum identificado
- **Stack inferida:** Indeterminada
- **Objetivo/descrição:** Objetivo não documentado no README acessível.
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=sim, lockfile=não evidenciado
- **Riscos estruturais:** README ausente ou não acessível; manifesto de dependências não identificado; testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** documentar propósito, instalação, uso e estado; declarar dependências e versão de runtime; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/Extrator

- **URL:** https://github.com/William-kelvem94/Extrator
- **Branch padrão:** `master`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 843 KB | **Árvore:** 840 arquivos, 0 diretórios
- **README:** README.md (7503 caracteres)
- **Manifestos:** `mock/package.json`, `mock/package-lock.json`, `mock/node_modules/debug/Makefile`, `mock/node_modules/ms/package.json`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript
- **Objetivo/descrição:** # Clone Painel do Inquilino Rentila — Repositório de Engenharia Reversa e Mocks Este repositório contém toda a especificação de engenharia reversa, análise de telas, documentação de lógica de negócios e servidores de mock necessários para replicar de ponta a ponta a experiência e o funcionamento do painel do inquilino do sistema **Rentila.com.br**. ## 📁 Estrutura de Pastas e Índice de Arquivos
- **Sinais:** testes=sim, CI=não evidenciado, Docker=não evidenciado, docs=sim, lockfile=sim
- **Riscos estruturais:** CI/CD não evidenciado; branch padrão não é main (master)
- **Lacunas recomendadas:** definir pipeline mínimo de validação

### Evidência de manifestos

**mock/package.json**

```
{
  "name": "mock-painel-inquilino",
  "version": "1.0.0",
  "description": "Mock server para o painel do inquilino (clone Rentila)",
  "main": "server_mock.js",
  "scripts": {
    "start": "node server_mock.js",
    "dev": "node server_mock.js"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "express": "^4.18.2",
    "ws": "^8.16.0"
  }
}

```

**mock/node_modules/ms/package.json**

```
{
  "name": "ms",
  "version": "2.0.0",
  "description": "Tiny milisecond conversion utility",
  "repository": "zeit/ms",
  "main": "./index",
  "files": [
    "index.js"
  ],
  "scripts": {
    "precommit": "lint-staged",
    "lint": "eslint lib/* bin/*",
    "test": "mocha tests.js"
  },
  "eslintConfig": {
    "extends": "eslint:recommended",
    "env": {
      "node": true,
      "es6": true
    }
  },
  "lint-staged": {
    "*.js": [
      "npm run lint",
      "prettier --single-quote --write",
      "git add"
    ]
  },
  "license": "MIT",
  "devDependencies": {
    "eslint": "3.19.0",
    "expect.js": "0.3.1",
    "husky": "0.13.3",
    "lint-staged": "3.4.1",
    "mocha": "3.4.1"
```


---

## William-kelvem94/GAMMAAP

- **URL:** https://github.com/William-kelvem94/GAMMAAP
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 125 KB | **Árvore:** 219 arquivos, 0 diretórios
- **README:** README.md (8689 caracteres)
- **Manifestos:** `Dockerfile`, `package.json`, `nginx/Dockerfile`, `backend/Dockerfile`
- **Stack inferida:** Node.js/JavaScript, JavaScript, Vite, Docker
- **Objetivo/descrição:** # GammaAP - Plataforma de Criação de Conteúdo com IA Uma plataforma completa e profissional para criar apresentações, sites, documentos e posts para redes sociais usando Inteligência Artificial. ## 🚀 Funcionalidades
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=sim, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**package.json**

```
{
  "name": "gammaap",
  "version": "1.0.0",
  "description": "Plataforma completa de criação de conteúdo com IA - Apresentações, Sites, Documentos e Redes Sociais",
  "main": "server/index.js",
  "type": "module",
  "scripts": {
    "dev": "concurrently \"npm run server\" \"npm run client\"",
    "server": "nodemon server/index.js",
    "client": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "start": "node server/index.js",
    "seed": "node server/seeds/initialData.js"
  },
  "keywords": [
    "ai",
    "design",
    "presentations",
    "websites",
    "social-media"
  ],
  "author": "",
  "license": "MIT",
  "dependencies": {
    "express": "^4.18.2",
    "cors": "^2.8.5",
    "dotenv": "^16.3.1",
    "mongoose": "^8.0.3",
    "bcryptjs": "^2.4.3",
    "jsonwebtoken": "^9.0.2",
    "socket.io": "^4.6.1",
    "groq-sdk": "^0.3.2",
    "multer": "^1.4.5-lts.1",
    "puppeteer": "^21.7.0",
```


---

## William-kelvem94/Gerenciador_Financeiro-4.0

- **URL:** https://github.com/William-kelvem94/Gerenciador_Financeiro-4.0
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 816 KB | **Árvore:** 304 arquivos, 0 diretórios
- **README:** README.md (2673 caracteres)
- **Manifestos:** `package.json`, `IA/Dockerfile`, `package-lock.json`, `backend/Dockerfile`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite, Python, Docker
- **Objetivo/descrição:** # Gerenciador Financeiro 4.0 Projeto completo e multiplataforma para gestão financeira pessoal e empresarial. ## Tecnologias Utilizadas
- **Sinais:** testes=sim, CI=não evidenciado, Docker=sim, docs=não evidenciado, lockfile=sim
- **Riscos estruturais:** possível material sensível/configuração ambiental na árvore; revisar segredos; CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação; explicitar licença

### Evidência de manifestos

**package.json**

```
{
  "name": "gerenciador-financeiro-4.0",
  "version": "4.0.0",
  "description": "Gerenciador Financeiro completo e multiplataforma",
  "private": true,
  "scripts": {
    "setup": "powershell -ExecutionPolicy Bypass -File ./setup-local.ps1",
    "dev:all": "concurrently \"npm run dev:db\" \"npm run dev:backend\" \"npm run dev:frontend\"",
    "dev:db": "docker compose -f docker-compose.local.yml up -d db-local",
    "dev:db:stop": "docker compose -f docker-compose.local.yml down",
    "dev:backend": "cd backend && npm run start:dev",
    "dev:frontend": "cd frontend && npm run dev",
    "build": "npm run build:backend && npm run build:frontend",
    "build:backend": "cd backend && npm run build",
    "build:frontend": "cd frontend && npm run build",
    "test": "npm run test:backend && npm run test:frontend",
    "test:backend": "cd backend && npm test",
    "test:frontend": "cd frontend && npm test",
    "docker:up": "docker compose up -d --build",
    "docker:down": "docker compose down",
    "docker:logs": "docker compose logs -f"
  },
  "dependencies": {
    "@types/express": "^5.0.2",
    "fast-csv": "^5.0.2"
  },
  "devDependencies": {
    "concurrently": "^9.1.0",
    "typescript": "^5.8.3"
  }
}

```


---

## William-kelvem94/Gerenciador_Financeiro-5.0

- **URL:** https://github.com/William-kelvem94/Gerenciador_Financeiro-5.0
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 333445 KB | **Árvore:** 1875 arquivos, 0 diretórios
- **README:** README.md (10828 caracteres)
- **Manifestos:** `package.json`, `client/Dockerfile`, `package-lock.json`, `server/Dockerfile`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite, Python, Docker, GitHub Actions
- **Objetivo/descrição:** # 🚀 Will Finance 6.0 - Complete Cyberpunk Financial Management System > **Enterprise-grade financial management system** with cutting-edge cyberpunk design, AI-powered insights, and full-stack modern architecture. ## 🎯 What's New in Version 6.0
- **Sinais:** testes=sim, CI=sim, Docker=sim, docs=sim, lockfile=sim
- **Riscos estruturais:** possível material sensível/configuração ambiental na árvore; revisar segredos
- **Lacunas recomendadas:** nenhuma lacuna estrutural básica detectada

### Evidência de manifestos

**package.json**

```
{
  "name": "will-finance",
  "version": "6.0.0",
  "description": "🚀 Sistema de gerenciamento financeiro cyberpunk completo e multiplataforma com React + TypeScript + Vite frontend, NestJS backend, PostgreSQL, IA integrada, dockerizado e pronto para Electron/React Native.",
  "main": "index.js",
  "engines": {
    "node": ">=20.0.0",
    "npm": ">=9.0.0"
  },
  "scripts": {
    "preinstall": "echo '🚀 Iniciando instalação do Will Finance 5.0...'",
    "postinstall": "echo '✅ Dependências instaladas com sucesso!'",
    "dev": "concurrently --kill-others-on-fail --names \"SERVER,CLIENT\" --prefix-colors \"cyan,magenta\" \"npm run dev:server\" \"npm run dev:client\"",
    "dev:server": "cd server && npm run dev",
    "dev:client": "cd client && npm run dev",
    "dev:ai": "docker-compose -f docker-compose.yml -f docker-compose.ia.yml up -d",
    "dev:silent": "concurrently --kill-others-on-fail --success first \"npm run dev:server\" \"npm run dev:client\" > /dev/null 2>&1",
    "build": "npm run install:all && npm run build:client && npm run build:server",
    "build:client": "cd client && npm run build",
    "build:server": "cd server && npm run build",
    "docker:build": "docker-compose build --no-cache",
    "docker:up": "docker-compose up -d",
    "docker:down": "docker-compose down --remove-orphans",
    "docker:logs": "docker-compose logs -f",
    "docker:restart": "npm run docker:down && npm run docker:up",
    "docker:deploy": "node ./scripts/deploy.js",
    "docker:deploy:build": "node ./scripts/deploy.js --build",
    "docker:stop": "node ./scripts/deploy.js --stop",
    "build:docker": "docker-compose build --no-cache",
    "start": "cd server && npm start",
    "start:prod": "docker-compose up -d",
    "start:dev": "npm run dev",
    "install:all": "npm ci && npm run install:frontend && npm run install:backend",
    "install:frontend": "cd client && npm ci",
    "install:backend": "cd server && npm ci",
```


---

## William-kelvem94/Gerenciador_Financeiro-6.0

- **URL:** https://github.com/William-kelvem94/Gerenciador_Financeiro-6.0
- **Branch padrão:** `devops`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 201 KB | **Árvore:** 143 arquivos, 0 diretórios
- **README:** README.md (5870 caracteres)
- **Manifestos:** `backend/Dockerfile`, `docker-compose.yml`, `frontend/Dockerfile`, `backend/package.json`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite, Docker
- **Objetivo/descrição:** # Gerenciador Financeiro 5.0 Sistema completo para controle de finanças pessoais e empresariais de micro e pequenas empresas. ## 🎯 Visão Geral
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=sim, docs=não evidenciado, lockfile=sim
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado; branch padrão não é main (devops); manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**backend/Dockerfile**

```
# Multi-stage Dockerfile para Backend

# Stage 1: Base
FROM node:18-alpine AS base
WORKDIR /app
RUN apk add --no-cache libc6-compat openssl curl

# Stage 2: Dependencies
FROM base AS deps
COPY package*.json ./
COPY prisma ./prisma/
RUN npm ci --only=production && \
    npm cache clean --force

# Stage 3: Development Dependencies
FROM base AS dev-deps
COPY package*.json ./
RUN npm ci

# Stage 4: Builder
FROM base AS builder
COPY --from=dev-deps /app/node_modules ./node_modules
COPY . .
RUN npx prisma generate
RUN npm run build

# Stage 5: Development
FROM base AS development
ENV NODE_ENV=development
COPY --from=dev-deps /app/node_modules ./node_modules
COPY . .
RUN npx prisma generate
EXPOSE 4000
CMD ["npm", "run", "dev"]

```

**docker-compose.yml**

```
version: '3.8'

services:
  # PostgreSQL Database
  postgres:
    image: postgres:15-alpine
    container_name: financeiro_postgres
    restart: unless-stopped
    environment:
      POSTGRES_DB: ${POSTGRES_DB:-financeiro_db}
      POSTGRES_USER: ${POSTGRES_USER:-financeiro}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-financeiro123}
    ports:
      - "${POSTGRES_PORT:-5432}:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - financeiro_network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-financeiro}"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis Cache
  redis:
    image: redis:7-alpine
    container_name: financeiro_redis
    restart: unless-stopped
    command: redis-server --requirepass ${REDIS_PASSWORD:-redis123}
    ports:
      - "${REDIS_PORT:-6379}:6379"
    volumes:
      - redis_data:/data
    networks:
```

**backend/package.json**

```
{
  "name": "gerenciador-financeiro-backend",
  "version": "5.0.0",
  "description": "Backend do Gerenciador Financeiro 5.0",
  "main": "dist/server.js",
  "scripts": {
    "dev": "tsx watch src/server.ts",
    "build": "tsc",
    "start": "node dist/server.js",
    "prisma:generate": "prisma generate",
    "prisma:migrate": "prisma migrate dev",
    "prisma:studio": "prisma studio",
    "prisma:seed": "tsx prisma/seed.ts"
  },
  "keywords": [
    "finance",
    "management",
    "backend",
    "api"
  ],
  "author": "",
  "license": "MIT",
  "dependencies": {
    "@prisma/client": "^5.7.1",
    "bcryptjs": "^2.4.3",
    "cors": "^2.8.5",
    "dotenv": "^16.3.1",
    "express": "^4.18.2",
    "express-rate-limit": "^7.1.5",
    "jsonwebtoken": "^9.0.2",
    "swagger-jsdoc": "^6.2.8",
    "swagger-ui-express": "^5.0.0",
    "zod": "^3.22.4"
  },
  "devDependencies": {
```


---

## William-kelvem94/Gerenciador_Financeiro-7.0

- **URL:** https://github.com/William-kelvem94/Gerenciador_Financeiro-7.0
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 191568 KB | **Árvore:** 1007 arquivos, 0 diretórios
- **README:** README.md (5264 caracteres)
- **Manifestos:** `package.json`, `package-lock.json`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Next.js, GitHub Actions
- **Objetivo/descrição:** # Numni **Numni** é uma plataforma de gestão financeira multiworkspace para uso pessoal e em equipe. O projeto reúne contas, transações, categorias, orçamentos, metas, investimentos, dívidas, documentos, relatórios, calendário, notificações, equipe, backups e um assistente financeiro com IA. > O nome do produto é Numni. Alguns identificadores técnicos legados, como nome do repositório, variáveis, tabelas ou caminhos, podem permanecer quando a troca direta criar risco de incompatibilidade.
- **Sinais:** testes=sim, CI=sim, Docker=não evidenciado, docs=sim, lockfile=sim
- **Riscos estruturais:** dependência/configuração usa marcador latest; baixa reprodutibilidade; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** explicitar licença

### Evidência de manifestos

**package.json**

```
{
  "name": "numni",
  "version": "7.0.0",
  "private": true,
  "description": "Numni - Plataforma completa de gestão financeira pessoal e empresarial",
  "author": "William-kelvem94",
  "scripts": {
    "dev": "npx prisma generate && next dev --hostname 0.0.0.0 --port 3002",
    "build": "npx prisma generate && next build --webpack && node scripts/prepare-standalone.mjs",
    "start": "NODE_ENV=production node .next/standalone/server.js",
    "lint": "eslint src --ext .ts,.tsx --max-warnings=0",
    "lint:eslint": "eslint src --ext .ts,.tsx --max-warnings=0",
    "type-check": "tsc --noEmit",
    "test": "jest --config config/testing/jest.config.js",
    "test:watch": "jest --config config/testing/jest.config.js --watch",
    "test:coverage": "jest --config config/testing/jest.config.js --coverage",
    "test:e2e": "playwright test",
    "test:e2e:seed": "tsx scripts/e2e-seed.ts",
    "test:e2e:frontend": "npm run test:e2e:seed && playwright test --project=chromium-public --project=chromium-auth",
    "test:e2e:frontend:full": "npm run test:e2e:seed && playwright test --project=chromium-public --project=chromium-auth --project=firefox-public --project=firefox-auth --project=webkit-public --project=webkit-auth",
    "db:generate": "prisma generate",
    "db:push": "prisma db push",
    "db:studio": "prisma studio",
    "db:migrate": "prisma migrate dev",
    "db:seed": "prisma db seed",
    "analyze": "cross-env ANALYZE=true next build",
    "setup": "npm install && npx prisma generate && npx prisma db push",
    "postinstall": "prisma generate"
  },
  "prisma": {
    "seed": "tsx prisma/seed.ts"
  },
  "dependencies": {
    "@google/genai": "^2.16.0",
    "@hookform/resolvers": "^3.10.0",
```

**package-lock.json**

```
{
  "name": "gerenciador-financeiro",
  "version": "7.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "gerenciador-financeiro",
      "version": "7.0.0",
      "hasInstallScript": true,
      "dependencies": {
        "@google/genai": "^2.16.0",
        "@hookform/resolvers": "^3.10.0",
        "@next-auth/prisma-adapter": "^1.0.7",
        "@prisma/client": "^5.19.1",
        "@radix-ui/react-accordion": "^1.1.2",
        "@radix-ui/react-alert-dialog": "^1.1.15",
        "@radix-ui/react-avatar": "^1.1.10",
        "@radix-ui/react-checkbox": "^1.3.3",
        "@radix-ui/react-collapsible": "^1.0.3",
        "@radix-ui/react-context-menu": "^2.1.5",
        "@radix-ui/react-dialog": "^1.1.15",
        "@radix-ui/react-dropdown-menu": "^2.1.16",
        "@radix-ui/react-hover-card": "^1.0.7",
        "@radix-ui/react-label": "^2.1.7",
        "@radix-ui/react-menubar": "^1.0.4",
        "@radix-ui/react-navigation-menu": "^1.1.4",
        "@radix-ui/react-popover": "^1.0.7",
        "@radix-ui/react-progress": "^1.0.3",
        "@radix-ui/react-radio-group": "^1.1.3",
        "@radix-ui/react-scroll-area": "^1.2.10",
        "@radix-ui/react-select": "^2.2.6",
        "@radix-ui/react-separator": "^1.1.7",
        "@radix-ui/react-slider": "^1.1.2",
        "@radix-ui/react-slot": "^1.0.2",
```


---

## William-kelvem94/Gestor_Aluguel

- **URL:** https://github.com/William-kelvem94/Gestor_Aluguel
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 100887 KB | **Árvore:** 125 arquivos, 0 diretórios
- **README:** README.md (2881 caracteres)
- **Manifestos:** `pyproject.toml`, `requirements.txt`
- **Stack inferida:** Python, GitHub Actions
- **Objetivo/descrição:** # 🏢 Gestor de Aluguel Enterprise v3.0.0 Sistema profissional de gestão imobiliária com arquitetura enterprise, incluindo automação de workflows, arquitetura modular, logging avançado e integração com banco de dados. ## 🚀 Instalação
- **Sinais:** testes=sim, CI=sim, Docker=não evidenciado, docs=sim, lockfile=não evidenciado
- **Riscos estruturais:** nenhum sinal estrutural adicional detectado
- **Lacunas recomendadas:** nenhuma lacuna estrutural básica detectada

### Evidência de manifestos

**pyproject.toml**

```
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "gestor-aluguel"
version = "1.0.0"
description = "Sistema de Gestão de Aluguel"
requires-python = ">=3.9"
authors = [{name = "William Kelvem", email = "williamkelvem64@gmail.com"}]
readme = "README.md"
license = {text = "MIT"}

dependencies = [
  "PyQt6>=6.5.0",
  "SQLAlchemy>=2.0.25",
  "alembic>=1.8.0",
  "dependency-injector>=4.40.0",
  "pydantic>=2.4.0",
  "python-dotenv>=1.0.0",
  "bleach>=6.0.0",
  "requests>=2.31.0",
  "aiofiles>=23.0.0",
  "cryptography>=41.0.0",
  "Pillow>=10.0.0",
  "numpy<2.0",
  "typing-extensions>=4.0.0",
  "pandas>=2.0.0",
  "openpyxl>=3.1.0"
]

[project.optional-dependencies]
dev = [
  "pytest>=7.0.0",
  "pytest-qt>=4.0.0",
```

**requirements.txt**

```
# ======================================================
# == GESTOR DE ALUGUEL ENTERPRISE - DEPENDENCIES ==
# ======================================================
# Sistema de Gestão Imobiliária - Arquitetura Enterprise 3.0
# Instalação: pip install -r requirements.txt

# --- CORE FRAMEWORK & UI ---
PyQt6>=6.5.0                    # Interface gráfica moderna
SQLAlchemy>=2.0.25               # ORM para banco de dados com Repository Pattern
alembic>=1.8.0                   # Migrações de banco de dados

# --- ENTERPRISE ARCHITECTURE ---
dependency-injector>=4.40.0      # Dependency Injection Container
pydantic>=2.4.0                 # Validação de dados e modelos
python-dotenv>=1.0.0             # Gerenciamento de configurações
bleach>=6.0.0                   # Sanitização segura de HTML/texto

# --- DESENVOLVIMENTO & TESTES ---
pytest>=7.0.0                   # Framework de testes
pytest-qt>=4.0.0                # Testes para PyQt
pytest-cov>=4.0.0               # Cobertura de código
pytest-html>=3.0.0              # Relatórios HTML
pytest-timeout>=2.0.0           # Timeout para testes
coverage>=7.0.0                 # Cobertura de testes

# --- BUILD & DISTRIBUIÇÃO ---
pyinstaller>=6.0.0              # Criação de executáveis
psutil>=5.9.0                   # Monitoramento de sistema

# --- LOGGING & MONITORING ---
loguru>=0.7.0                   # Sistema de logging avançado

# --- UTILITÁRIOS ESSENCIAIS ---
requests>=2.31.0                # Requisições HTTP (WhatsApp API)
aiofiles>=23.0.0                # Operações de arquivo assíncronas
```


---

## William-kelvem94/hermes-agent-pinokio

- **URL:** https://github.com/William-kelvem94/hermes-agent-pinokio
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 92169 KB | **Árvore:** 10506 arquivos, 0 diretórios
- **README:** README.md (3963 caracteres)
- **Manifestos:** `app/Dockerfile`, `app/package.json`, `app/pyproject.toml`, `app/requirements.txt`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite, Python, Docker
- **Objetivo/descrição:** # Hermes Agent for Pinokio This project adds a 1-click Pinokio launcher for Hermes Agent, the terminal-first AI agent from Nous Research. The launcher installs Hermes into `app/`, uses Hermes' default home directory at `~/.hermes`, and exposes setup plus multiple launch modes directly from the Pinokio UI. ## What This Launcher Does
- **Sinais:** testes=sim, CI=não evidenciado, Docker=sim, docs=sim, lockfile=sim
- **Riscos estruturais:** possível material sensível/configuração ambiental na árvore; revisar segredos; CI/CD não evidenciado; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação

### Evidência de manifestos

**app/package.json**

```
{
  "name": "hermes-agent",
  "version": "1.0.0",
  "description": "An AI agent with advanced tool-calling capabilities, featuring a flexible toolsets system for organizing and managing tools.",
  "private": true,
  "scripts": {
    "postinstall": "echo '✅ Browser tools ready. Run: python run_agent.py --help'"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/NousResearch/Hermes-Agent.git"
  },
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/NousResearch/Hermes-Agent/issues"
  },
  "homepage": "https://github.com/NousResearch/Hermes-Agent#readme",
  "dependencies": {
    "agent-browser": "^0.13.0",
    "@askjo/camofox-browser": "^1.5.2"
  },
  "overrides": {
    "lodash": "4.18.1"
  },
  "engines": {
    "node": ">=20.0.0"
  }
}

```

**app/pyproject.toml**

```
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "hermes-agent"
version = "0.10.0"
description = "The self-improving AI agent — creates skills from experience, improves them during use, and runs anywhere"
readme = "README.md"
requires-python = ">=3.11"
authors = [{ name = "Nous Research" }]
license = { text = "MIT" }
dependencies = [
  # Core — pinned to known-good ranges to limit supply chain attack surface
  "openai>=2.21.0,<3",
  "anthropic>=0.39.0,<1",
  "python-dotenv>=1.2.1,<2",
  "fire>=0.7.1,<1",
  "httpx[socks]>=0.28.1,<1",
  "rich>=14.3.3,<15",
  "tenacity>=9.1.4,<10",
  "pyyaml>=6.0.2,<7",
  "requests>=2.33.0,<3",  # CVE-2026-25645
  "jinja2>=3.1.5,<4",
  "pydantic>=2.12.5,<3",
  # Interactive CLI (prompt_toolkit is used directly by cli.py)
  "prompt_toolkit>=3.0.52,<4",
  # Tools
  "exa-py>=2.9.0,<3",
  "firecrawl-py>=4.16.0,<5",
  "parallel-web>=0.4.2,<1",
  "fal-client>=0.13.1,<1",
  # Text-to-speech (Edge TTS is free, no API key needed)
  "edge-tts>=7.2.7,<8",
  # Skills Hub (GitHub App JWT auth — optional, only needed for bot identity)
```

**app/requirements.txt**

```
# NOTE: This file is maintained for convenience only.
# The canonical dependency list is in pyproject.toml.
# Preferred install: pip install -e ".[all]"

# Core dependencies
openai
python-dotenv
fire
httpx
rich
tenacity
prompt_toolkit
pyyaml
requests
jinja2
pydantic>=2.0
PyJWT[crypto]
debugpy

# Web tools
firecrawl-py
parallel-web>=0.4.2

# Image generation
fal-client

# Text-to-speech (Edge TTS is free, no API key needed)
edge-tts

# Optional: For cron expression parsing (cronjob scheduling)
croniter

# Optional: For messaging platform integrations (gateway)
python-telegram-bot[webhooks]>=22.6
discord.py>=2.0
```


---

## William-kelvem94/hermes-agent-pinokio-wk

- **URL:** https://github.com/William-kelvem94/hermes-agent-pinokio-wk
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 0 KB | **Árvore:** 0 arquivos, 0 diretórios
- **README:** não localizado
- **Manifestos:** nenhum identificado
- **Stack inferida:** Sem arquivos acessíveis
- **Objetivo/descrição:** Objetivo não documentado no README acessível.
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** README ausente ou não acessível; testes não evidenciados pela árvore; CI/CD não evidenciado; árvore não acessível ou repositório vazio
- **Lacunas recomendadas:** documentar propósito, instalação, uso e estado; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/IA_LOCAL_S_ULTRA

- **URL:** https://github.com/William-kelvem94/IA_LOCAL_S_ULTRA
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 259 KB | **Árvore:** 90 arquivos, 0 diretórios
- **README:** README.md (6594 caracteres)
- **Manifestos:** `build.gradle.kts`, `gradle.properties`, `settings.gradle.kts`, `app/build.gradle.kts`
- **Stack inferida:** Gradle/Android or JVM, Android, Kotlin, GitHub Actions
- **Objetivo/descrição:** # IA LOCAL S ULTRA — JARVIS Mobile Aplicativo Android nativo que adapta a arquitetura do `PROJECT_JARVIS_5.0` para o celular. O APK contém o runtime `llama.cpp`, a interface e as ferramentas Android; o GGUF pesado é baixado com segurança no primeiro uso e fica no armazenamento privado do aplicativo. ## Estado atual — 0.3.0
- **Sinais:** testes=não evidenciado, CI=sim, Docker=não evidenciado, docs=sim, lockfile=sim
- **Riscos estruturais:** testes não evidenciados pela árvore
- **Lacunas recomendadas:** criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**build.gradle.kts**

```
plugins {
    alias(libs.plugins.android.application) apply false
    alias(libs.plugins.android.library) apply false
    alias(libs.plugins.jetbrains.kotlin.android) apply false
}

```

**gradle.properties**

```
org.gradle.jvmargs=-Xmx6g -Dfile.encoding=UTF-8
android.useAndroidX=true
android.nonTransitiveRClass=true
kotlin.code.style=official
org.gradle.parallel=true

# Enabled parallel sync for Gradle 9.4+
org.gradle.tooling.parallel=true
android.defaults.buildfeatures.resvalues=true
android.sdk.defaultTargetSdkToCompileSdkIfUnset=false
android.enableAppCompileTimeRClass=false
android.usesSdkInManifest.disallowed=false
android.uniquePackageNames=false
android.dependency.useConstraints=true
android.r8.strictFullModeForKeepRules=false
android.r8.optimizedResourceShrinking=false
android.builtInKotlin=false
android.newDsl=false

```

**settings.gradle.kts**

```
pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}

plugins {
    id("org.gradle.toolchains.foojay-resolver-convention") version "0.8.0"
}

dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}

rootProject.name = "IA_LOCAL_S_ULTRA"
include(":app")

val llamaModule = file("third_party/llama.cpp/examples/llama.android/lib")
check(llamaModule.exists()) {
    "Submódulo llama.cpp ausente. Clone com --recurse-submodules ou execute git submodule update --init --recursive."
}
include(":llama")
project(":llama").projectDir = llamaModule

```

**app/build.gradle.kts**

```
plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.jetbrains.kotlin.android)
}

android {
    namespace = "com.william.ialocalsultra"
    compileSdk = 36

    defaultConfig {
        applicationId = "com.jarvis.ai.assistant"
        minSdk = 33
        targetSdk = 36
        versionCode = 3
        versionName = "0.3.0"

        ndk {
            abiFilters += listOf("arm64-v8a", "x86_64")
        }
    }

    buildTypes {
        debug {
            isMinifyEnabled = false
        }
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }

    compileOptions {
```


---

## William-kelvem94/IA_MUSIC

- **URL:** https://github.com/William-kelvem94/IA_MUSIC
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 8260 KB | **Árvore:** 67 arquivos, 0 diretórios
- **README:** README.md (5642 caracteres)
- **Manifestos:** `requirements.txt`
- **Stack inferida:** Python
- **Objetivo/descrição:** # 🎵 IA MUSICAL - Conversor de Estilo Musical com IA Sistema avançado de conversão de estilo musical usando **Inteligência Artificial**. Converte qualquer música do YouTube para diferentes estilos musicais brasileiros e internacionais. ## 🚀 **INSTALAÇÃO RÁPIDA**
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**requirements.txt**

```
# ============================================
# 🎵 IA MUSICAL - DEPENDÊNCIAS DO PROJETO
# ============================================

# ===== FRAMEWORK WEB =====
fastapi>=0.104.1
uvicorn[standard]>=0.24.0
python-multipart>=0.0.6

# ===== MACHINE LEARNING & IA =====
torch>=2.1.0
torchvision>=0.16.0
torchaudio>=2.1.0
transformers>=4.35.0
accelerate>=0.24.0
huggingface-hub>=0.17.0

# ===== PROCESSAMENTO DE ÁUDIO =====
librosa>=0.10.1
soundfile>=0.12.1
scipy>=1.11.4
numpy>=1.24.3
demucs>=4.0.1
pydub>=0.25.1

# ===== DOWNLOAD DE VÍDEO =====
yt-dlp>=2023.11.16
youtube-dl>=2021.12.17

# ===== UTILIDADES =====
requests>=2.31.0
aiofiles>=23.2.1
python-dotenv>=1.0.0
click>=8.1.7
tqdm>=4.66.1
```


---

## William-kelvem94/IA-MIDIA

- **URL:** https://github.com/William-kelvem94/IA-MIDIA
- **Branch padrão:** `master`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 6654 KB | **Árvore:** 1685 arquivos, 0 diretórios
- **README:** não localizado
- **Manifestos:** `backend/requirements.txt`
- **Stack inferida:** JavaScript, Python
- **Objetivo/descrição:** Objetivo não documentado no README acessível.
- **Sinais:** testes=sim, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** README ausente ou não acessível; possível material sensível/configuração ambiental na árvore; revisar segredos; CI/CD não evidenciado; branch padrão não é main (master)
- **Lacunas recomendadas:** documentar propósito, instalação, uso e estado; definir pipeline mínimo de validação; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**backend/requirements.txt**

```
python-multipart
openai


```


---

## William-kelvem94/IA-POTENTE

- **URL:** https://github.com/William-kelvem94/IA-POTENTE
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 4208 KB | **Árvore:** 50 arquivos, 0 diretórios
- **README:** README.md (220 caracteres)
- **Manifestos:** `jarvis/requirements.txt`, `treinamento/requirements_treinamento.txt`
- **Stack inferida:** Python
- **Objetivo/descrição:** TESTE ALEATORIO DE UM "JARVIS" O MODELO E ESTRUTURA TA FEITO, NÃO TA FUNCIONANDO E TEM UM CODIGO DE TREINAMENTO DE UM MODELO IA TAMBÉM NÃO FUNCIONANDO FICA SALVO AQUI PARA QUEM SABE UM DIA MELHORAR OU FAZER FUNCIONAR
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**jarvis/requirements.txt**

```
# transformers==4.39.3  # Desativado por segurança (CVE-2026-4372 e CVE-2026-5241); manter somente como referência futura.
torch
pygame
edge-tts
pyaudio
SpeechRecognition
colorama

```

**treinamento/requirements_treinamento.txt**

```
# transformers==4.40.0  # Desativado por segurança (CVE-2026-4372 e CVE-2026-5241); manter somente como referência futura.
datasets==2.18.0
accelerate==0.29.3
peft==0.10.0
scikit-learn==1.5.0
pandas==2.2.1
tokenizers>=0.19.1

```


---

## William-kelvem94/IA.IDE

- **URL:** https://github.com/William-kelvem94/IA.IDE
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 104 KB | **Árvore:** 100 arquivos, 0 diretórios
- **README:** README.md (8766 caracteres)
- **Manifestos:** `docker-compose.yml`, `services/gpt4free/Dockerfile`, `services/gpt4all-api/Dockerfile`, `services/gpt4free/requirements.txt`
- **Stack inferida:** Python, Docker
- **Objetivo/descrição:** # 🤖 IA Local Completa - Projeto Profissional **IA completa estilo ChatGPT/DeepSeek, 100% local, gratuita, com API própria para VS Code, Docker, n8n e mais.** Este projeto oferece uma stack completa de IA local com:
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=sim, docs=sim, lockfile=não evidenciado
- **Riscos estruturais:** possível material sensível/configuração ambiental na árvore; revisar segredos; testes não evidenciados pela árvore; CI/CD não evidenciado; dependência/configuração usa marcador latest; baixa reprodutibilidade; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**docker-compose.yml**

```
name: ia-local-stack

services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    ports:
      - "11434:11434"
    environment:
      - OLLAMA_HOST=0.0.0.0
      - OLLAMA_KEEP_ALIVE=${OLLAMA_KEEP_ALIVE:-24h}
      - OLLAMA_NUM_PARALLEL=${OLLAMA_NUM_PARALLEL:-2}
      - OLLAMA_MAX_LOADED_MODELS=${OLLAMA_MAX_LOADED_MODELS:-1}
      - OLLAMA_NUM_GPU=0
      - OLLAMA_NUM_THREAD=${OLLAMA_NUM_THREAD:-4}
      - OLLAMA_MODELS=/models
    volumes:
      - ollama_data:/root/.ollama
      - ./models:/models
    # Memória ajustada para evitar erros de falta de memória
    # Deixa mais espaço livre para o sistema e Docker
    deploy:
      resources:
        limits:
          memory: 10G
        reservations:
          memory: 6G
    healthcheck:
      test: ["CMD-SHELL", "ollama list || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    restart: unless-stopped
    profiles: [cpu]
```

**services/gpt4free/Dockerfile**

```
FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicação
COPY app.py .

# Expor porta
EXPOSE 1337

# Comando de inicialização
CMD ["python", "app.py"]


```

**services/gpt4free/requirements.txt**

```
flask==3.0.0
flask-cors==4.0.0
g4f==0.4.2.1


```


---

## William-kelvem94/JARVIS-2.0

- **URL:** https://github.com/William-kelvem94/JARVIS-2.0
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 7941 KB | **Árvore:** 1013 arquivos, 0 diretórios
- **README:** README.md (10833 caracteres)
- **Manifestos:** `Dockerfile`, `package.json`, `requirements.txt`, `docker-compose.yml`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite, Python, Docker, GitHub Actions
- **Objetivo/descrição:** <p align="center"> <a href="https://getleon.ai"><img width="800" src="https://getleon.ai/img/hero-animation.gif" /></a> </p>
- **Sinais:** testes=sim, CI=sim, Docker=sim, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** possível material sensível/configuração ambiental na árvore; revisar segredos; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** nenhuma lacuna estrutural básica detectada

### Evidência de manifestos

**package.json**

```
{
  "name": "leon",
  "version": "1.0.0-beta.10+dev",
  "description": "Server, skills and web app of the Leon personal assistant",
  "author": {
    "name": "Louis Grenard",
    "email": "louis@getleon.ai",
    "url": "https://twitter.com/grenlouis"
  },
  "license": "MIT",
  "homepage": "https://getleon.ai",
  "type": "module",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/leon-ai/leon.git"
  },
  "bugs": {
    "url": "https://github.com/leon-ai/leon/issues"
  },
  "engines": {
    "node": ">=22.13.1",
    "npm": ">=10.9.2"
  },
  "volta": {
    "node": "22.13.1"
  },
  "pnpm": {
    "neverBuiltDependencies": []
  },
  "scripts": {
    "pre-commit": "lint-staged",
    "lint": "tsx scripts/lint.js",
    "test": "npm run test:json && npm run test:over-http && npm run test:unit && npm run test:e2e",
    "test:unit": "npm run train en && cross-env PIPENV_PIPFILE=bridges/python/src/Pipfile LEON_NODE_ENV=testing jest --forceExit --silent --projects test/unit/unit.jest.json && npm run train",
    "test:e2e": "npm run test:e2e:nlp-modules && npm run test:e2e:modules",
```

**requirements.txt**

```
google-cloud-speech
watson-developer-cloud
pyaudio
speechrecognition
pygame
edge-tts

```


---

## William-kelvem94/JOGO-SANDBOX

- **URL:** https://github.com/William-kelvem94/JOGO-SANDBOX
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 49 KB | **Árvore:** 71 arquivos, 0 diretórios
- **README:** README.md (5820 caracteres)
- **Manifestos:** nenhum identificado
- **Stack inferida:** Indeterminada
- **Objetivo/descrição:** # Nature's Canvas - Jogo Sandbox de Elementos Um jogo sandbox inovador onde você controla as forças fundamentais da natureza em um mundo infinito. Manipule gravidade, direção e elementos naturais em tempo real! ## 🎮 Funcionalidades Principais
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** manifesto de dependências não identificado; testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** declarar dependências e versão de runtime; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/LEITOR-TELA

- **URL:** https://github.com/William-kelvem94/LEITOR-TELA
- **Branch padrão:** `master`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 144 KB | **Árvore:** 46 arquivos, 0 diretórios
- **README:** README.md (10233 caracteres)
- **Manifestos:** `Dockerfile`, `requirements.txt`, `docker-compose.yml`
- **Stack inferida:** Python, Docker
- **Objetivo/descrição:** # Leitor de Tela Inteligente ![Python Version](https://www.python.org/downloads/) ![License: MIT](https://opensource.org/licenses/MIT)
- **Sinais:** testes=sim, CI=não evidenciado, Docker=sim, docs=sim, lockfile=não evidenciado
- **Riscos estruturais:** CI/CD não evidenciado; branch padrão não é main (master); dependência/configuração usa marcador latest; baixa reprodutibilidade
- **Lacunas recomendadas:** definir pipeline mínimo de validação; explicitar licença

### Evidência de manifestos

**Dockerfile**

```
# Dockerfile para LeitorTela Jarvis
FROM python:3.10-slim

# Instalar dependências do sistema para GUI, Áudio e OCR
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk-dev \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxinerama1 \
    libxcursor1 \
    libxrandr2 \
    libxi6 \
    libasound2-dev \
    libportaudio2 \
    libportaudiocpp0 \
    portaudio19-dev \
    tesseract-ocr \
    tesseract-ocr-por \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar requisitos e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fonte
COPY . .

# Variáveis de ambiente
ENV DISPLAY=host.docker.internal:0.0
ENV PYTHONUNBUFFERED=1
```

**requirements.txt**

```
# Leitor de Tela Inteligente - Requirements
# Dependências essenciais para funcionamento básico

# Core libraries
Pillow>=9.0.0
opencv-python>=4.7.0.72
numpy>=1.24.0
SQLAlchemy>=1.4.0

# OCR
pytesseract>=0.3.10
easyocr>=1.7.0

# Screen capture
mss>=6.1.0
pyautogui>=0.9.53

# GUI
customtkinter>=5.1.3

# Data processing
pandas>=1.5.0

# Utilities
pyperclip>=1.8.2
psutil>=5.9.0

# Voice (Jarvis Style)
SpeechRecognition>=3.10.0
pyttsx3>=2.90
edge-tts>=6.1.0
gTTS>=2.3.2
vosk>=0.3.45
PyAudio>=0.2.13
pygame>=2.5.0
```

**docker-compose.yml**

```
version: '3.8'

services:
  jarvis-app:
    build: .
    container_name: jarvis_leitor_tela
    volumes:
      - .:/app
      - ./data:/app/data
    environment:
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
      - DISPLAY=host.docker.internal:0.0
    network_mode: "host"
    depends_on:
      - ollama

  ollama:
    image: ollama/ollama:latest
    container_name: ollama_service
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama

volumes:
  ollama_data:

```


---

## William-kelvem94/MEU_NECTAR_JARVIS

- **URL:** https://github.com/William-kelvem94/MEU_NECTAR_JARVIS
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 427 KB | **Árvore:** 291 arquivos, 0 diretórios
- **README:** README.md (3357 caracteres)
- **Manifestos:** `backend/Dockerfile`, `docker-compose.yml`, `ai-local/Dockerfile`, `frontend/Dockerfile`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Next.js, Python, Docker, GitHub Actions
- **Objetivo/descrição:** # 🤖 Néctar - Seu Jarvis Pessoal com IA Local **Assistente pessoal inteligente estilo Jarvis com IA 100% LOCAL e GRATUITA** ## 🎯 O que é o Néctar?
- **Sinais:** testes=sim, CI=sim, Docker=sim, docs=não evidenciado, lockfile=sim
- **Riscos estruturais:** nenhum sinal estrutural adicional detectado
- **Lacunas recomendadas:** nenhuma lacuna estrutural básica detectada

### Evidência de manifestos

**backend/Dockerfile**

```
FROM node:20-alpine

WORKDIR /app

# Copiar package.json e package-lock.json
COPY package*.json ./

# Copiar schema do Prisma
COPY prisma ./prisma/

# Instalar dependências
RUN npm ci

# Gerar Prisma Client
RUN npx prisma generate

# Copiar código fonte
COPY . .

# Build da aplicação (comentado para desenvolvimento)
# RUN npm run build

# Expor porta
EXPOSE 3001

# Comando padrão - modo desenvolvimento
CMD ["npm", "run", "start:dev"]

```


---

## William-kelvem94/MONITORADOR-ANTIGRAVITY

- **URL:** https://github.com/William-kelvem94/MONITORADOR-ANTIGRAVITY
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 26 KB | **Árvore:** 16 arquivos, 0 diretórios
- **README:** não localizado
- **Manifestos:** `Dockerfile`, `package.json`, `package-lock.json`, `docker-compose.yml`
- **Stack inferida:** Node.js/JavaScript, JavaScript, Docker
- **Objetivo/descrição:** Objetivo não documentado no README acessível.
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=sim, docs=não evidenciado, lockfile=sim
- **Riscos estruturais:** README ausente ou não acessível; testes não evidenciados pela árvore; CI/CD não evidenciado; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** documentar propósito, instalação, uso e estado; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**Dockerfile**

```
# Stage 1: Build Frontend
FROM node:20-slim AS build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:20-slim
WORKDIR /app
COPY package*.json ./
RUN npm install --only=production
COPY --from=build-stage /app/dist ./public
COPY --from=build-stage /app/server ./server

EXPOSE 3001
CMD ["node", "server/index.js"]

```

**package.json**

```
{
  "name": "monitorador-antigravity",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "start": "node server/index.js",
    "preview": "vite preview"
  },
  "devDependencies": {
    "vite": "^7.3.1"
  },
  "dependencies": {
    "axios": "^1.13.5",
    "cors": "^2.8.6",
    "dotenv": "^17.3.1",
    "express": "^5.2.1",
    "fs-extra": "^11.3.3",
    "os-utils": "^0.0.14",
    "path-browserify": "^1.0.1",
    "systeminformation": "^5.31.1"
  }
}

```

**package-lock.json**

```
{
  "name": "monitorador-antigravity",
  "version": "0.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "monitorador-antigravity",
      "version": "0.0.0",
      "dependencies": {
        "axios": "^1.13.5",
        "cors": "^2.8.6",
        "dotenv": "^17.3.1",
        "express": "^5.2.1",
        "fs-extra": "^11.3.3",
        "os-utils": "^0.0.14",
        "path-browserify": "^1.0.1",
        "systeminformation": "^5.31.1"
      },
      "devDependencies": {
        "vite": "^7.3.1"
      }
    },
    "node_modules/@esbuild/aix-ppc64": {
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.27.3.tgz",
      "integrity": "sha512-9fJMTNFTWZMh5qwrBItuziu834eOCUcEqymSH7pY+zoMVEZg3gcPuBNxH1EvfVYe9h0x/Ptw8KBzv7qxb7l8dg==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "aix"
```

**docker-compose.yml**

```
version: '3.8'

services:
  antigravity-monitor:
    build: .
    ports:
      - "3001:3001"
    environment:
      - NODE_ENV=production
    restart: always

```


---

## William-kelvem94/Movimentador_de_arquivo

- **URL:** https://github.com/William-kelvem94/Movimentador_de_arquivo
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 92552 KB | **Árvore:** 4461 arquivos, 0 diretórios
- **README:** README.md (3761 caracteres)
- **Manifestos:** `requirements.txt`
- **Stack inferida:** JavaScript, Python
- **Objetivo/descrição:** # Organizador Inteligente de Arquivos Aplicativo desktop para organizar pastas bagunçadas de forma rápida, visual e prática. O projeto nasceu como um movimentador de arquivos, mas evoluiu para um organizador inteligente que pode:
- **Sinais:** testes=sim, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** possível material sensível/configuração ambiental na árvore; revisar segredos; CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**requirements.txt**

```
��P y Q t 5  
 p s u t i l 
```


---

## William-kelvem94/NEXUS-VENDAS

- **URL:** https://github.com/William-kelvem94/NEXUS-VENDAS
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 392 KB | **Árvore:** 151 arquivos, 0 diretórios
- **README:** README.md (3262 caracteres)
- **Manifestos:** `Dockerfile`, `package.json`, `package-lock.json`, `backend/Dockerfile`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Next.js, Docker
- **Objetivo/descrição:** # NEXUS VENDAS (Modern Platform) Projeto moderno e funcional para gestão de vendas, estoque, clientes, recebíveis, despesas e relatórios. Foco em experiência responsiva (desktop e mobile) e arquitetura escalável. ## 🚀 Stack Tecnológica
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=sim, docs=não evidenciado, lockfile=sim
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**Dockerfile**

```
# Dockerfile único para Nexus Vendas
FROM node:20-alpine AS base

# Instalar dependências do sistema
RUN apk add --no-cache \
    python3 \
    make \
    g++ \
    openssl

WORKDIR /app

# Copiar arquivos de dependências
COPY package*.json ./
COPY backend/package*.json ./backend/
COPY frontend/package*.json ./frontend/

# Instalar dependências (sem prisma generate ainda)
RUN npm install -g pm2

# Copiar código fonte primeiro
COPY backend ./backend
COPY frontend ./frontend

# Instalar dependências do backend (com scripts para compilar bcrypt)
WORKDIR /app/backend
ENV PRISMA_ENGINES_CHECKSUM_IGNORE_MISSING=1
ENV PRISMA_SKIP_POSTINSTALL_GENERATE=true
RUN npm install --ignore-scripts
# Recompilar bcrypt para a arquitetura correta
RUN npm rebuild bcrypt --build-from-source
# Gerar Prisma com múltiplas tentativas
RUN for i in 1 2 3 4 5; do \
      PRISMA_ENGINES_CHECKSUM_IGNORE_MISSING=1 npx prisma generate && break || \
      (echo "Tentativa $i falhou, aguardando..." && sleep 15); \
```

**package.json**

```
{
  "name": "nexus-vendas",
  "version": "1.0.0",
  "private": true,
  "workspaces": [
    "backend",
    "frontend"
  ],
  "scripts": {
    "dev": "concurrently \"npm run dev --workspace=backend\" \"npm run dev --workspace=frontend\"",
    "build": "npm run build --workspace=frontend && npm run build --workspace=backend",
    "start": "npm run start --workspace=backend & npm run start --workspace=frontend",
    "docker:build": "docker build -t nexus-vendas .",
    "docker:run": "docker run -p 3000:3000 -p 3001:3001 -p 5432:5432 nexus-vendas",
    "docker:compose": "docker-compose -f docker-compose.single.yml up --build"
  },
  "devDependencies": {
    "concurrently": "^8.2.2"
  }
}


```


---

## William-kelvem94/openclaude-wk

- **URL:** https://github.com/William-kelvem94/openclaude-wk
- **Branch padrão:** `main`
- **Visibilidade:** public | **Arquivado:** não
- **Tamanho GitHub:** 29772 KB | **Árvore:** 3546 arquivos, 0 diretórios
- **README:** README.md (23816 caracteres)
- **Manifestos:** `Dockerfile`, `package.json`, `web/package.json`, `vendor/node-domexception-shim/package.json`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Docker, GitHub Actions
- **Objetivo/descrição:** # OpenClaude OpenClaude is an open-source coding-agent CLI for cloud and local model providers. Use OpenAI-compatible APIs, Gemini, GitHub Models, Codex OAuth, Codex, Ollama, Atomic Chat, and other supported backends while keeping one terminal-first workflow: prompts, tools, agents, MCP, slash commands, and streaming output.
- **Sinais:** testes=sim, CI=sim, Docker=sim, docs=sim, lockfile=não evidenciado
- **Riscos estruturais:** manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** nenhuma lacuna estrutural básica detectada

### Evidência de manifestos

**package.json**

```
{
  "name": "@gitlawb/openclaude",
  "version": "0.23.0",
  "description": "OpenClaude opens coding-agent workflows to any LLM — OpenAI, Gemini, DeepSeek, Ollama, and 200+ models",
  "type": "module",
  "bin": {
    "openclaude": "./bin/openclaude"
  },
  "exports": {
    "./package.json": "./package.json",
    "./dist/cli.mjs": "./dist/cli.mjs",
    "./sdk": {
      "types": "./src/entrypoints/sdk.d.ts",
      "import": "./dist/sdk.mjs"
    }
  },
  "files": [
    "bin/",
    "dist/cli.mjs",
    "dist/sdk.mjs",
    "src/entrypoints/sdk.d.ts",
    "src/entrypoints/sdk/coreTypes.generated.ts",
    "scripts/windows/openclaude-aliases.ps1",
    "vendor/node-domexception-shim/",
    "docs/windows-aliases-and-launchers.md",
    "README.md"
  ],
  "scripts": {
    "build": "bun run scripts/build.ts",
    "integrations:generate": "bun run scripts/generate-integrations-artifacts.ts",
    "integrations:check": "bun run scripts/generate-integrations-artifacts.ts --check",
    "dev": "bun run build && node bin/openclaude",
    "dev:profile": "bun run scripts/provider-launch.ts",
    "dev:profile:fast": "bun run scripts/provider-launch.ts auto --fast --bare",
    "dev:codex": "bun run scripts/provider-launch.ts codex",
```

**web/package.json**

```
{
  "name": "openclaude-web",
  "version": "0.2.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "astro dev",
    "build": "astro check && astro build",
    "preview": "astro preview",
    "typecheck": "astro check"
  },
  "dependencies": {
    "@astrojs/check": "0.9.9",
    "@astrojs/sitemap": "3.7.3",
    "@fontsource-variable/geist-mono": "^5.2.5",
    "astro": "6.4.6",
    "typescript": "^5.8.3"
  }
}

```

**vendor/node-domexception-shim/package.json**

```
{
  "name": "node-domexception",
  "version": "1.0.0",
  "description": "Stub shim: re-exports the platform-native DOMException. Replaces the deprecated node-domexception polyfill.",
  "main": "index.js",
  "type": "commonjs",
  "license": "MIT"
}

```


---

## William-kelvem94/Openclaw_Docker_Will

- **URL:** https://github.com/William-kelvem94/Openclaw_Docker_Will
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 1805 KB | **Árvore:** 14 arquivos, 0 diretórios
- **README:** README.md (692 caracteres)
- **Manifestos:** `Dockerfile`
- **Stack inferida:** Docker
- **Objetivo/descrição:** # OpenClaw OpenClaw configurado pra rodar em **Render.com** (Docker) ou **Local** (WSL + Ollama). ## Render (Docker)
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=sim, docs=sim, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado; dependência/configuração usa marcador latest; baixa reprodutibilidade; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**Dockerfile**

```
FROM ubuntu:22.04

WORKDIR /app

# Instala dependências (Node.js via NodeSource para versão moderna)
RUN apt-get update && apt-get install -y curl git && \
    curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y nodejs

# Instala OpenClaw globalmente no build
RUN npm install -g openclaw@latest

# Script de instalação manual (fallback)
COPY scripts/install_openclaw.sh /app/scripts/install_openclaw.sh
COPY docs/SETUP_OPENCLAW.md /app/docs/SETUP_OPENCLAW.md

EXPOSE 8000

ENV OPENCLAW_GATEWAY_TOKEN=openclaw-dev-token

# Inicia o gateway sem necessidade de configuração prévia
CMD openclaw gateway --port $PORT --bind lan --token $OPENCLAW_GATEWAY_TOKEN --allow-unconfigured

```


---

## William-kelvem94/Personal-Voice-Assistent

- **URL:** https://github.com/William-kelvem94/Personal-Voice-Assistent
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 904 KB | **Árvore:** 215 arquivos, 0 diretórios
- **README:** README.md (38570 caracteres)
- **Manifestos:** nenhum identificado
- **Stack inferida:** Python, Java
- **Objetivo/descrição:** > /* > > PVA is coded by Marius Schwarz in 2021-2024
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=sim, lockfile=não evidenciado
- **Riscos estruturais:** manifesto de dependências não identificado; testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** declarar dependências e versão de runtime; definir pipeline mínimo de validação; criar testes automatizados


---

## William-kelvem94/pixel-agents

- **URL:** https://github.com/William-kelvem94/pixel-agents
- **Branch padrão:** `main`
- **Visibilidade:** public | **Arquivado:** não
- **Tamanho GitHub:** 1402 KB | **Árvore:** 301 arquivos, 0 diretórios
- **README:** README.md (11558 caracteres)
- **Manifestos:** `package.json`, `package-lock.json`, `server/package.json`, `webview-ui/package.json`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite, GitHub Actions
- **Objetivo/descrição:** <h1 align="center"> <a href="https://github.com/pablodelucca/pixel-agents/discussions"> <img src="webview-ui/public/banner.png" alt="Pixel Agents">
- **Sinais:** testes=sim, CI=sim, Docker=não evidenciado, docs=sim, lockfile=sim
- **Riscos estruturais:** manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** nenhuma lacuna estrutural básica detectada

### Evidência de manifestos

**package.json**

```
{
  "name": "pixel-agents",
  "displayName": "Pixel Agents",
  "description": "Pixel art office where your Claude Code agents come to life as animated characters",
  "version": "1.2.0",
  "publisher": "pablodelucca",
  "repository": {
    "type": "git",
    "url": "https://github.com/pablodelucca/pixel-agents"
  },
  "icon": "icon.png",
  "license": "MIT",
  "engines": {
    "vscode": "^1.105.0"
  },
  "categories": [
    "Other"
  ],
  "activationEvents": [],
  "main": "./dist/extension.js",
  "contributes": {
    "commands": [
      {
        "command": "pixel-agents.showPanel",
        "title": "Pixel Agents: Show Panel"
      },
      {
        "command": "pixel-agents.exportDefaultLayout",
        "title": "Pixel Agents: Export Layout as Default"
      }
    ],
    "viewsContainers": {
      "panel": [
        {
          "id": "pixel-agents-panel",
```

**package-lock.json**

```
{
  "name": "pixel-agents",
  "version": "1.2.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "pixel-agents",
      "version": "1.2.0",
      "license": "MIT",
      "devDependencies": {
        "@playwright/test": "^1.58.2",
        "@types/node": "25.x",
        "@types/pngjs": "^6.0.5",
        "@types/vscode": "^1.105.0",
        "@vscode/test-electron": "^2.5.2",
        "esbuild": "^0.28.0",
        "eslint": "^10.0.3",
        "eslint-config-prettier": "^10.1.8",
        "eslint-plugin-simple-import-sort": "^12.1.1",
        "husky": "^9.1.7",
        "knip": "^6.3.0",
        "lint-staged": "^16.3.2",
        "npm-run-all": "^4.1.5",
        "pngjs": "^7.0.0",
        "prettier": "^3.8.1",
        "tsx": "^4.21.0",
        "typescript": "^5.9.3",
        "typescript-eslint": "^8.54.0"
      },
      "engines": {
        "vscode": "^1.105.0"
      }
    },
    "node_modules/@emnapi/core": {
```

**server/package.json**

```
{
  "name": "pixel-agents",
  "private": true,
  "scripts": {
    "test": "vitest run",
    "test:watch": "vitest"
  },
  "devDependencies": {
    "vitest": "^3.2.1"
  }
}

```

**webview-ui/package.json**

```
{
  "name": "webview-ui",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "preview": "vite preview",
    "test": "node --import tsx/esm --test test/*.test.ts"
  },
  "dependencies": {
    "react": "^19.2.0",
    "react-dom": "^19.2.0"
  },
  "devDependencies": {
    "@tailwindcss/vite": "^4.2.2",
    "tailwindcss": "^4.2.2",
    "@eslint/js": "^9.39.1",
    "@types/node": "^25.5.2",
    "@types/pngjs": "^6.0.5",
    "@types/react": "^19.2.14",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^6.0.1",
    "eslint": "^9.39.1",
    "eslint-config-prettier": "^10.1.8",
    "eslint-plugin-react-hooks": "^7.0.1",
    "eslint-plugin-react-refresh": "^0.5.2",
    "eslint-plugin-simple-import-sort": "^12.1.1",
    "globals": "^17.4.0",
    "pngjs": "^7.0.0",
    "tsx": "^4.19.3",
    "typescript": "~5.9.3",
    "typescript-eslint": "^8.58.0",
```


---

## William-kelvem94/postifolio-will

- **URL:** https://github.com/William-kelvem94/postifolio-will
- **Branch padrão:** `master`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 428 KB | **Árvore:** 33 arquivos, 0 diretórios
- **README:** README.md (18 caracteres)
- **Manifestos:** nenhum identificado
- **Stack inferida:** JavaScript
- **Objetivo/descrição:** # postifolio-will
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** manifesto de dependências não identificado; testes não evidenciados pela árvore; CI/CD não evidenciado; branch padrão não é main (master)
- **Lacunas recomendadas:** declarar dependências e versão de runtime; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/PROJECT_JARVIS_3.0

- **URL:** https://github.com/William-kelvem94/PROJECT_JARVIS_3.0
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 27800 KB | **Árvore:** 73 arquivos, 0 diretórios
- **README:** README.md (8580 caracteres)
- **Manifestos:** `requirements.txt`, `docker-compose.yml`
- **Stack inferida:** JavaScript, Python, Docker
- **Objetivo/descrição:** # 🤖 JARVIS 3.0 - Assistente Virtual Inteligente Completo ![Status](https://github.com) ![Interface](https://github.com)
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=sim, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado; dependência/configuração usa marcador latest; baixa reprodutibilidade; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**requirements.txt**

```
# Dependências do JARVIS 3.0
# Core Framework
flask==3.0.0
flask-socketio==5.3.6
flask-cors==4.0.0
python-socketio==5.10.0

# IA e Machine Learning
openai==1.6.1
transformers==4.36.2
torch>=2.0.0
sentence-transformers==2.2.2

# Processamento de Áudio
gtts==2.4.0
pyttsx3==2.90
librosa==0.10.1
soundfile==0.12.1

# Monitoramento de Sistema
psutil==5.9.7
py-cpuinfo==9.0.0
GPUtil==1.4.0

# Interface Web
jinja2==3.1.2
websockets==12.0
eventlet==0.33.3

# Banco de Dados
sqlalchemy==2.0.25

# Utilitários
pyyaml==6.0.1
python-dotenv==1.0.0
```

**docker-compose.yml**

```
version: '3.8'

services:
  # Ollama - Motor de IA Local
  ollama:
    image: ollama/ollama:latest
    container_name: Ollama_IA_LOCAL
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
      - ./training_data:/training_data  # Para dados de treinamento
    environment:
      - OLLAMA_HOST=0.0.0.0:11434
    restart: unless-stopped
    networks:
      - jarvis_network

  # Open WebUI - Interface Web tipo ChatGPT
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: Jarvis_WebUI
    ports:
      - "3000:8080"
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434
      - WEBUI_SECRET_KEY=sua_chave_secreta_aqui
    volumes:
      - open_webui_data:/app/backend/data
    depends_on:
      - ollama
    restart: unless-stopped
    networks:
      - jarvis_network

```


---

## William-kelvem94/PROJECT_JARVIS_5.0

- **URL:** https://github.com/William-kelvem94/PROJECT_JARVIS_5.0
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 588584 KB | **Árvore:** 176 arquivos, 0 diretórios
- **README:** README.md (8671 caracteres)
- **Manifestos:** `requirements.txt`, `webui/package.json`, `webui/package-lock.json`
- **Stack inferida:** Node.js/JavaScript, JavaScript, Python, GitHub Actions
- **Objetivo/descrição:** # JARVIS 5.0 — consciência operacional local Assistente pessoal para Windows, feito para o Galaxy Book2 360 e o desktop com GTX 1050 Ti. O projeto combina Ollama local, voz, interface futurista, agenda, Gmail somente leitura, notícias, clima e um núcleo persistente de presença, continuidade e iniciativa controlada. “Consciência operacional” significa que o JARVIS mantém identidade, observa apenas metadados autorizados, atualiza um modelo verificável do seu contexto, lembra pendências e decide quando falar ou permanecer em silêncio. Não significa consciência biológica, sentimentos ou liberdade para agir sem permissão.
- **Sinais:** testes=sim, CI=sim, Docker=não evidenciado, docs=sim, lockfile=sim
- **Riscos estruturais:** manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**requirements.txt**

```
numpy>=1.26
Pillow>=10
pystray>=0.19
sounddevice>=0.5
faster-whisper>=1.1
huggingface-hub>=0.24
pyttsx3>=2.99
piper-tts>=1.6
pywebview>=5.4,<7
opencv-python-headless>=4.10,<5
tzdata>=2025.2
pytest>=8
playwright>=1.55,<2
cryptography>=44,<51
pywin32>=308; platform_system == "Windows"

```

**webui/package.json**

```
{
  "name": "webui",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build && node scripts/prepare-sites-build.mjs",
    "preview": "vite preview",
    "test:sites": "node --test tests/sites-worker.test.mjs"
  },
  "dependencies": {
    "@fontsource-variable/inter": "^5.3.0",
    "@phosphor-icons/react": "^2.1.10",
    "@vitejs/plugin-react": "5.0.4",
    "react": "19.2.0",
    "react-dom": "19.2.0",
    "vite": "6.4.2"
  }
}

```

**webui/package-lock.json**

```
{
  "name": "webui",
  "version": "0.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "webui",
      "version": "0.0.0",
      "dependencies": {
        "@fontsource-variable/inter": "^5.3.0",
        "@phosphor-icons/react": "^2.1.10",
        "@vitejs/plugin-react": "5.0.4",
        "react": "19.2.0",
        "react-dom": "19.2.0",
        "vite": "6.4.2"
      },
      "devDependencies": {}
    },
    "node_modules/@babel/code-frame": {
      "version": "7.29.7",
      "resolved": "https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.29.7.tgz",
      "integrity": "sha512-Aup7aUOfpbAUg2ROOJN6Iw5f9DMBlzu0mIkm/malLQFN/YQgO48wCj0Kxa3sEHJvPVFg7siR+qRInwXd2qhQKw==",
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.29.7",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.29.7",
```


---

## William-kelvem94/PROJECT-JARVIS

- **URL:** https://github.com/William-kelvem94/PROJECT-JARVIS
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 107039 KB | **Árvore:** 0 arquivos, 0 diretórios
- **README:** não localizado
- **Manifestos:** nenhum identificado
- **Stack inferida:** Sem arquivos acessíveis
- **Objetivo/descrição:** Objetivo não documentado no README acessível.
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** README ausente ou não acessível; testes não evidenciados pela árvore; CI/CD não evidenciado; árvore não acessível ou repositório vazio
- **Lacunas recomendadas:** documentar propósito, instalação, uso e estado; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/rentai-manager

- **URL:** https://github.com/William-kelvem94/rentai-manager
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 214 KB | **Árvore:** 111 arquivos, 0 diretórios
- **README:** README.md (2141 caracteres)
- **Manifestos:** `package.json`, `package-lock.json`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite
- **Objetivo/descrição:** # Welcome to your Lovable project ## Project info **URL**: https://lovable.dev/projects/e671a10f-3871-4cdd-abd9-40521b51c7ee
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=sim
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**package.json**

```
{
  "name": "vite_react_shadcn_ts",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "build:dev": "vite build --mode development",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "@hookform/resolvers": "^3.10.0",
    "@radix-ui/react-accordion": "^1.2.11",
    "@radix-ui/react-alert-dialog": "^1.1.14",
    "@radix-ui/react-aspect-ratio": "^1.1.7",
    "@radix-ui/react-avatar": "^1.1.10",
    "@radix-ui/react-checkbox": "^1.3.2",
    "@radix-ui/react-collapsible": "^1.1.11",
    "@radix-ui/react-context-menu": "^2.2.15",
    "@radix-ui/react-dialog": "^1.1.14",
    "@radix-ui/react-dropdown-menu": "^2.1.15",
    "@radix-ui/react-hover-card": "^1.1.14",
    "@radix-ui/react-label": "^2.1.7",
    "@radix-ui/react-menubar": "^1.1.15",
    "@radix-ui/react-navigation-menu": "^1.2.13",
    "@radix-ui/react-popover": "^1.1.14",
    "@radix-ui/react-progress": "^1.1.7",
    "@radix-ui/react-radio-group": "^1.3.7",
    "@radix-ui/react-scroll-area": "^1.2.9",
    "@radix-ui/react-select": "^2.2.5",
    "@radix-ui/react-separator": "^1.1.7",
    "@radix-ui/react-slider": "^1.3.5",
    "@radix-ui/react-slot": "^1.2.3",
```

**package-lock.json**

```
{
  "name": "vite_react_shadcn_ts",
  "version": "0.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "vite_react_shadcn_ts",
      "version": "0.0.0",
      "dependencies": {
        "@hookform/resolvers": "^3.10.0",
        "@radix-ui/react-accordion": "^1.2.11",
        "@radix-ui/react-alert-dialog": "^1.1.14",
        "@radix-ui/react-aspect-ratio": "^1.1.7",
        "@radix-ui/react-avatar": "^1.1.10",
        "@radix-ui/react-checkbox": "^1.3.2",
        "@radix-ui/react-collapsible": "^1.1.11",
        "@radix-ui/react-context-menu": "^2.2.15",
        "@radix-ui/react-dialog": "^1.1.14",
        "@radix-ui/react-dropdown-menu": "^2.1.15",
        "@radix-ui/react-hover-card": "^1.1.14",
        "@radix-ui/react-label": "^2.1.7",
        "@radix-ui/react-menubar": "^1.1.15",
        "@radix-ui/react-navigation-menu": "^1.2.13",
        "@radix-ui/react-popover": "^1.1.14",
        "@radix-ui/react-progress": "^1.1.7",
        "@radix-ui/react-radio-group": "^1.3.7",
        "@radix-ui/react-scroll-area": "^1.2.9",
        "@radix-ui/react-select": "^2.2.5",
        "@radix-ui/react-separator": "^1.1.7",
        "@radix-ui/react-slider": "^1.3.5",
        "@radix-ui/react-slot": "^1.2.3",
        "@radix-ui/react-switch": "^1.2.5",
        "@radix-ui/react-tabs": "^1.1.12",
        "@radix-ui/react-toast": "^1.2.14",
```


---

## William-kelvem94/ruflo

- **URL:** https://github.com/William-kelvem94/ruflo
- **Branch padrão:** `main`
- **Visibilidade:** public | **Arquivado:** não
- **Tamanho GitHub:** 527530 KB | **Árvore:** 6122 arquivos, 0 diretórios
- **README:** README.md (28331 caracteres)
- **Manifestos:** `package.json`, `pnpm-lock.yaml`, `v3/package.json`, `package-lock.json`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite, Rust, Docker, GitHub Actions
- **Objetivo/descrição:** <div align="center"> ![Ruflo Banner](https://cognitum.one/agentic-engineering) ![Try the UI Beta — flo.ruv.io](https://flo.ruv.io/)
- **Sinais:** testes=sim, CI=sim, Docker=sim, docs=sim, lockfile=sim
- **Riscos estruturais:** possível material sensível/configuração ambiental na árvore; revisar segredos; dependência/configuração usa marcador latest; baixa reprodutibilidade; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** nenhuma lacuna estrutural básica detectada

### Evidência de manifestos

**package.json**

```
{
  "name": "claude-flow",
  "version": "3.10.45",
  "description": "Ruflo - Enterprise AI agent orchestration for Claude Code. Deploy 60+ specialized agents in coordinated swarms with self-learning, fault-tolerant consensus, vector memory, and MCP integration",
  "main": "dist/index.js",
  "type": "module",
  "bin": {
    "claude-flow": "./bin/cli.js"
  },
  "homepage": "https://github.com/ruvnet/claude-flow#readme",
  "bugs": {
    "url": "https://github.com/ruvnet/claude-flow/issues",
    "email": "support@ruv.io"
  },
  "funding": {
    "type": "github",
    "url": "https://github.com/sponsors/ruvnet"
  },
  "files": [
    "bin/**",
    "v3/@claude-flow/cli/bin/**",
    "v3/@claude-flow/cli/dist/**/*.js",
    "v3/@claude-flow/cli/dist/**/*.d.ts",
    "!v3/@claude-flow/cli/dist/**/*.map",
    "v3/@claude-flow/cli/package.json",
    "v3/@claude-flow/shared/dist/**/*.js",
    "v3/@claude-flow/shared/dist/**/*.d.ts",
    "!v3/@claude-flow/shared/dist/**/*.map",
    "v3/@claude-flow/shared/package.json",
    "v3/@claude-flow/guidance/dist/**/*.js",
    "v3/@claude-flow/guidance/dist/**/*.d.ts",
    "!v3/@claude-flow/guidance/dist/**/*.map",
    "v3/@claude-flow/guidance/package.json",
    ".claude-plugin/**",
    ".claude/**",
```

**v3/package.json**

```
{
  "name": "@claude-flow/v3-monorepo",
  "version": "3.0.0-alpha.1",
  "private": true,
  "type": "module",
  "description": "Claude Flow V3 - Modular AI Agent Coordination System",
  "workspaces": [
    "@claude-flow/*",
    "claude-flow"
  ],
  "scripts": {
    "build": "pnpm -r build",
    "test": "vitest run",
    "test:unit": "vitest run __tests__/unit",
    "test:integration": "vitest run __tests__/integration",
    "test:integration:watch": "vitest watch __tests__/integration",
    "test:integration:memory": "vitest run __tests__/integration/memory-integration.test.ts",
    "test:integration:swarm": "vitest run __tests__/integration/swarm-integration.test.ts",
    "test:integration:mcp": "vitest run __tests__/integration/mcp-integration.test.ts",
    "test:integration:plugin": "vitest run __tests__/integration/plugin-integration.test.ts",
    "test:integration:workflow": "vitest run __tests__/integration/workflow-integration.test.ts",
    "test:coverage": "vitest run --coverage",
    "test:coverage:integration": "vitest run __tests__/integration --coverage",
    "test:security": "pnpm --filter @claude-flow/security test",
    "test:memory": "pnpm --filter @claude-flow/memory test",
    "test:swarm": "pnpm --filter @claude-flow/swarm test",
    "bench": "pnpm --filter @claude-flow/performance bench",
    "bench:attention": "pnpm --filter @claude-flow/performance bench:attention",
    "typecheck": "pnpm -r typecheck",
    "clean": "rm -rf node_modules @claude-flow/*/node_modules claude-flow/node_modules",
    "publish:dry": "pnpm --filter claude-flow publish --dry-run --tag v3alpha --no-git-checks",
    "publish:v3alpha": "pnpm --filter claude-flow publish --tag v3alpha --no-git-checks",
    "version:patch": "pnpm -r exec npm version patch",
    "version:minor": "pnpm -r exec npm version minor",
    "version:major": "pnpm -r exec npm version major",
```


---

## William-kelvem94/search_works

- **URL:** https://github.com/William-kelvem94/search_works
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 10284 KB | **Árvore:** 2018 arquivos, 0 diretórios
- **README:** README.md (5386 caracteres)
- **Manifestos:** `Dockerfile`, `package.json`, `package-lock.json`, `docker-compose.yml`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Docker
- **Objetivo/descrição:** # JobSeeker Bot & Dashboard Uma plataforma completa desenvolvida para automatizar a busca, realizar a triagem de vagas com Inteligência Artificial e gerenciar as candidaturas a empregos de forma assistida, segura e personalizada para o perfil de **William Kelvem de Sousa Pereira (Engenheiro de Computação | Analista de Sistemas & Operações)**. ## 🚀 Funcionalidades Core
- **Sinais:** testes=sim, CI=não evidenciado, Docker=sim, docs=não evidenciado, lockfile=sim
- **Riscos estruturais:** CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação

### Evidência de manifestos

**package.json**

```
{
  "name": "jobseeker-bot",
  "version": "1.0.0",
  "description": "Bot para busca, triagem de vagas com IA e auxílio na candidatura usando Playwright",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "start": "ts-node src/index.ts",
    "test-ai": "ts-node src/testAi.ts",
    "dashboard": "ts-node src/server.ts"
  },
  "dependencies": {
    "axios": "^1.7.2",
    "csv-writer": "^1.6.0",
    "dotenv": "^16.4.5",
    "express": "^5.2.1",
    "pdf-parse": "1.1.1",
    "playwright": "^1.44.1"
  },
  "devDependencies": {
    "@types/express": "^5.0.6",
    "@types/node": "^20.14.2",
    "@types/pdf-parse": "^1.1.5",
    "ts-node": "^10.9.2",
    "typescript": "^5.4.5"
  }
}

```


---

## William-kelvem94/slack-agent-template

- **URL:** https://github.com/William-kelvem94/slack-agent-template
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 190 KB | **Árvore:** 96 arquivos, 0 diretórios
- **README:** README.md (18550 caracteres)
- **Manifestos:** `package.json`, `pnpm-lock.yaml`
- **Stack inferida:** Node.js/JavaScript, TypeScript
- **Objetivo/descrição:** # Slack Agent Template ![Deploy with Vercel](<https://vercel.com/new/clone?demo-description=This%20is%20a%20Slack%20Agent%20template%20built%20with%20Bolt%20for%20JavaScript%20(TypeScript)%20and%20the%20Nitro%20server%20framework.&demo-image=%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2FSs9t7RkKlPtProrbDhZFM%2F0d11b9095ecf84c87a68fbdef6f12ad1%2FFrame__1_.png&demo-title=Slack%20Agent%20Template&demo-url=https%3A%2F%2Fgithub.com%2Fvercel-partner-solutions%2Fslack-agent-template&env=SLACK_SIGNING_SECRET%2CSLACK_BOT_TOKEN&envDescription=These%20environment%20variables%20are%20required%20to%20deploy%20your%20Slack%20app%20to%20Vercel&envLink=https%3A%2F%2Fapi.slack.com%2Fapps&from=templates&project
- **Sinais:** testes=sim, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=sim
- **Riscos estruturais:** CI/CD não evidenciado; dependência/configuração usa marcador latest; baixa reprodutibilidade
- **Lacunas recomendadas:** definir pipeline mínimo de validação; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**package.json**

```
{
  "name": "slack-agent-template",
  "description": "A Slackbot built with the AI SDK and Bolt powered by Nitro",
  "version": "0.0.1",
  "author": "Matthew Lewis",
  "license": "MIT",
  "scripts": {
    "build": "nitro build",
    "dev": "nitro dev",
    "dev:tunnel": "tsx scripts/dev.tunnel.ts",
    "configure": "tsx scripts/configure.ts",
    "prepare": "nitro prepare",
    "preview": "node .output/server/index.mjs",
    "lint": "biome check .",
    "lint:fix": "biome check . --write",
    "typecheck": "tsc --noEmit"
  },
  "dependencies": {
    "@slack/bolt": "^4.6.0",
    "@slack/web-api": "^7.13.0",
    "@vercel/slack-bolt": "latest",
    "@workflow/ai": "4.1.0-beta.57",
    "ai": "^6.0.27",
    "workflow": "4.2.0-beta.71",
    "zod": "^4.3.5"
  },
  "devDependencies": {
    "@biomejs/biome": "2.2.6",
    "@inquirer/input": "^4.3.1",
    "@ngrok/ngrok": "^1.7.0",
    "@slack/cli-hooks": "^1.2.1",
    "@types/node": "^24.10.7",
    "boxen": "^8.0.1",
    "chalk": "^5.6.2",
    "dotenv": "^17.2.3",
```

**pnpm-lock.yaml**

```
lockfileVersion: '9.0'

settings:
  autoInstallPeers: true
  excludeLinksFromLockfile: false

importers:

  .:
    dependencies:
      '@slack/bolt':
        specifier: ^4.6.0
        version: 4.6.0(@types/express@5.0.3)
      '@slack/web-api':
        specifier: ^7.13.0
        version: 7.13.0
      '@vercel/slack-bolt':
        specifier: latest
        version: 1.1.0(@aws-sdk/credential-provider-web-identity@3.972.13)(@slack/bolt@4.6.0(@types/express@5.0.3))
      '@workflow/ai':
        specifier: 4.1.0-beta.57
        version: 4.1.0-beta.57(@opentelemetry/api@1.9.0)(ai@6.0.27(zod@4.3.5))(workflow@4.2.0-beta.71(@nestjs/common@11.1.17(reflect-metadata@0.2.2)(rxjs@7.8.2))(@nestjs/core@11.1.17(@nestjs/common@11.1.17(reflect-metadata@0.2.2)(rxjs@7.8.2))(reflect-metadata@0.2.2)(rxjs@7.8.2))(@opentelemetry/api@1.9.0)(@swc/cli@0.8.0(@swc/core@1.15.3)(chokidar@5.0.0))(@swc/core@1.15.3)(magicast@0.5.1)(next@16.0.10(@opentelemetry/api@1.9.0)(react-dom@19.2.3(react@19.2.3))(react@19.2.3))(typescript@5.9.3))
      ai:
        specifier: ^6.0.27
        version: 6.0.27(zod@4.3.5)
      workflow:
        specifier: 4.2.0-beta.71
        version: 4.2.0-beta.71(@nestjs/common@11.1.17(reflect-metadata@0.2.2)(rxjs@7.8.2))(@nestjs/core@11.1.17(@nestjs/common@11.1.17(reflect-metadata@0.2.2)(rxjs@7.8.2))(reflect-metadata@0.2.2)(rxjs@7.8.2))(@opentelemetry/api@1.9.0)(@swc/cli@0.8.0(@swc/core@1.15.3)(chokidar@5.0.0))(@swc/core@1.15.3)(magicast@0.5.1)(next@16.0.10(@opentelemetry/api@1.9.0)(react-dom@19.2.3(react@19.2.3))(react@19.2.3))(typescript@5.9.3)
      zod:
        specifier: ^4.3.5
        version: 4.3.5
    devDependencies:
      '@biomejs/biome':
        specifier: 2.2.6
        version: 2.2.6
```


---

## William-kelvem94/STUDY_LLMS

- **URL:** https://github.com/William-kelvem94/STUDY_LLMS
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 32382 KB | **Árvore:** 2919 arquivos, 0 diretórios
- **README:** README.md (1786 caracteres)
- **Manifestos:** `requirements.txt`, `llama.cpp/Makefile`, `llama.cpp/poetry.lock`, `llama.cpp/pyproject.toml`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite, Python, Gradle/Android or JVM, Android, Kotlin, Docker
- **Objetivo/descrição:** # 🧠 STUDY_LLMS (Projeto WILL-JARVIS) Bem-vindo ao laboratório local de montagem, estudo e aperfeiçoamento arquitetural de Large Language Models do Projeto JARVIS 5.0. ## 🎯 Objetivo
- **Sinais:** testes=sim, CI=não evidenciado, Docker=sim, docs=sim, lockfile=sim
- **Riscos estruturais:** possível material sensível/configuração ambiental na árvore; revisar segredos; CI/CD não evidenciado; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação

### Evidência de manifestos

**requirements.txt**

```
# Dependências para Treinamento (Foco em Unsloth + 1050Ti)
torch
torchvision
torchaudio
xformers
unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git
trl
peft
accelerate
bitsandbytes
sentencepiece
datasets
psutil
pyyaml

```

**llama.cpp/pyproject.toml**

```
[tool.poetry]
name = "llama-cpp-scripts"
version = "0.0.0"
description = "Scripts that ship with llama.cpp"
authors = ["GGML <ggml@ggml.ai>"]
readme = "README.md"
homepage = "https://ggml.ai"
repository = "https://github.com/ggml-org/llama.cpp"
keywords = ["ggml", "gguf", "llama.cpp"]
packages = [{ include = "*.py", from = "." }]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[tool.poetry.dependencies]
python = ">=3.9"
numpy = "^1.25.0"
sentencepiece = ">=0.1.98,<0.3.0"
transformers = "==5.5.1"
protobuf = ">=4.21.0,<5.0.0"
gguf = { path = "./gguf-py" }
torch = { version = "^2.2.0", source = "pytorch" }

[tool.poetry.dev-dependencies]
pytest = "^5.2"


# Force wheel + cpu
# For discussion and context see https://github.com/python-poetry/poetry#6409
[[tool.poetry.source]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
priority = "explicit"
```


---

## William-kelvem94/SuperProjeto

- **URL:** https://github.com/William-kelvem94/SuperProjeto
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 0 KB | **Árvore:** 1 arquivos, 0 diretórios
- **README:** não localizado
- **Manifestos:** nenhum identificado
- **Stack inferida:** Indeterminada
- **Objetivo/descrição:** Objetivo não documentado no README acessível.
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** README ausente ou não acessível; manifesto de dependências não identificado; testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** documentar propósito, instalação, uso e estado; declarar dependências e versão de runtime; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/TCC_FINAL

- **URL:** https://github.com/William-kelvem94/TCC_FINAL
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 21906 KB | **Árvore:** 31 arquivos, 0 diretórios
- **README:** README.md (4863 caracteres)
- **Manifestos:** `requirements.txt`
- **Stack inferida:** Python
- **Objetivo/descrição:** # SICOMUV: Sistema de Comunicação Multifuncional com Reconhecimento de Texto e Assistência por Voz para Inclusão Digital ## Descrição Este projeto realiza o reconhecimento de texto extraído de imagens, traduz o texto para diferentes idiomas e converte o texto traduzido em fala. O sistema utiliza modelos de aprendizado de máquina para essas tarefas, além de incluir módulos para captura de vídeo, processamento de imagens e reconhecimento de voz. O objetivo principal é promover a inclusão digital, facilitando o acesso à informação para pessoas com deficiência visual e física.
- **Sinais:** testes=sim, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**requirements.txt**

```
﻿opencv-python
SpeechRecognition
PyAudio
pyttsx3
tensorflow
keras
googletrans
pytesseract
numpy
```


---

## William-kelvem94/TCC1---Modelo-Antigo

- **URL:** https://github.com/William-kelvem94/TCC1---Modelo-Antigo
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 3 KB | **Árvore:** 1 arquivos, 0 diretórios
- **README:** README.md (25 caracteres)
- **Manifestos:** nenhum identificado
- **Stack inferida:** Indeterminada
- **Objetivo/descrição:** # TCC1---Modelo-Antigo
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** manifesto de dependências não identificado; testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** declarar dependências e versão de runtime; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/TCC2_FINAL

- **URL:** https://github.com/William-kelvem94/TCC2_FINAL
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 746 KB | **Árvore:** 8 arquivos, 0 diretórios
- **README:** README.md (2983 caracteres)
- **Manifestos:** `Dockerfile`, `requirements.txt`
- **Stack inferida:** Python, Docker
- **Objetivo/descrição:** # Projeto SICOMUV Este repositório contém o projeto SICOMUV, um assistente de comunicação e tradução desenvolvido para facilitar a interação com diversos idiomas através de processamento de imagem, reconhecimento de texto e tradução automática. ## Estrutura do Repositório
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=sim, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**Dockerfile**

```
FROM python:3.10-slim

# Instala dependências do sistema
RUN apt-get update && \
    apt-get install -y \
        alsa-utils \
        build-essential \
        espeak \
        ffmpeg \
        libsm6 \
        libxext6 \
        libxrender-dev \
        portaudio19-dev \
        tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Cria diretório da aplicação
WORKDIR /app

# Copia arquivos do projeto
COPY . /app

# Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Variáveis de ambiente para Tesseract e modelo
ENV TESSERACT_CMD=/usr/bin/tesseract
ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata
ENV MODEL_PATH=./H5/H5.h5

# Comando para rodar o app
CMD ["python", "Apresentação.py"]

```

**requirements.txt**

```
opencv-python
pytesseract
numpy
mtranslate
keras
SpeechRecognition
pyttsx3
tensorflow
pyaudio
```


---

## William-kelvem94/teste

- **URL:** https://github.com/William-kelvem94/teste
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 0 KB | **Árvore:** 0 arquivos, 0 diretórios
- **README:** não localizado
- **Manifestos:** nenhum identificado
- **Stack inferida:** Sem arquivos acessíveis
- **Objetivo/descrição:** Objetivo não documentado no README acessível.
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** README ausente ou não acessível; testes não evidenciados pela árvore; CI/CD não evidenciado; árvore não acessível ou repositório vazio
- **Lacunas recomendadas:** documentar propósito, instalação, uso e estado; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/TESTER

- **URL:** https://github.com/William-kelvem94/TESTER
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 71 KB | **Árvore:** 39 arquivos, 0 diretórios
- **README:** README.md (11571 caracteres)
- **Manifestos:** `requirements.txt`
- **Stack inferida:** Python, GitHub Actions
- **Objetivo/descrição:** # 🧪 Testador Automatizado de Sites Um sistema completo para testar sites simulando comportamento de usuário real. O testador automatiza navegação, interação com formulários, busca e outras ações que um usuário comum realizaria. ## ✨ Características
- **Sinais:** testes=sim, CI=sim, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** nenhum sinal estrutural adicional detectado
- **Lacunas recomendadas:** explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**requirements.txt**

```
selenium>=4.15.0
pytest>=7.4.0
pytest-html>=4.1.1
webdriver-manager>=4.0.0
pytest-xdist>=3.5.0
faker>=20.0.0
python-dotenv>=1.0.0
requests>=2.31.0
openpyxl>=3.1.2
pandas>=2.1.0

```


---

## William-kelvem94/Tradutor-2.0

- **URL:** https://github.com/William-kelvem94/Tradutor-2.0
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 142 KB | **Árvore:** 5 arquivos, 0 diretórios
- **README:** README (225 caracteres)
- **Manifestos:** `requirements.txt`
- **Stack inferida:** Python
- **Objetivo/descrição:** #Instalação Realizar a instalação dos seguinte pacotes - pytesseract
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**requirements.txt**

```
﻿certifi==2024.8.30
charset-normalizer==3.4.0
click==8.1.7
colorama==0.4.6
comtypes==1.4.8
filelock==3.16.1
fsspec==2024.10.0
huggingface-hub==0.26.5
idna==3.10
Jinja2==3.1.4
joblib==1.4.2
MarkupSafe==3.0.2
mpmath==1.3.0
networkx==3.4.2
nltk==3.9.1
numpy==2.1.3
opencv-python==4.10.0.84
packaging==24.2
pillow==11.0.0
PyAudio==0.2.14
pypiwin32==223
pytesseract==0.3.13
pyttsx3==2.98
pywin32==308
PyYAML==6.0.2
regex==2024.11.6
requests==2.32.3
sacremoses==0.1.1
safetensors==0.4.5
sentencepiece==0.2.0
setuptools==75.6.0
SpeechRecognition==3.11.0
sympy==1.13.1
tokenizers==0.21.0
torch==2.5.1
```


---

## William-kelvem94/TRADUTOR-WKP

- **URL:** https://github.com/William-kelvem94/TRADUTOR-WKP
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 143 KB | **Árvore:** 6 arquivos, 0 diretórios
- **README:** README (225 caracteres)
- **Manifestos:** `requirements.txt`
- **Stack inferida:** Python
- **Objetivo/descrição:** #Instalação Realizar a instalação dos seguinte pacotes - pytesseract
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**requirements.txt**

```
﻿certifi==2024.8.30
charset-normalizer==3.4.0
click==8.1.7
colorama==0.4.6
comtypes==1.4.8
filelock==3.16.1
fsspec==2024.10.0
huggingface-hub==0.26.5
idna==3.10
Jinja2==3.1.4
joblib==1.4.2
MarkupSafe==3.0.2
mpmath==1.3.0
networkx==3.4.2
nltk==3.9.1
numpy==2.1.3
opencv-python==4.10.0.84
packaging==24.2
pillow==11.0.0
PyAudio==0.2.14
pypiwin32==223
pytesseract==0.3.13
pyttsx3==2.98
pywin32==308
PyYAML==6.0.2
regex==2024.11.6
requests==2.32.3
sacremoses==0.1.1
safetensors==0.4.5
sentencepiece==0.2.0
setuptools==75.6.0
SpeechRecognition==3.11.0
sympy==1.13.1
tokenizers==0.21.0
torch==2.5.1
```


---

## William-kelvem94/TRANSCRITOR

- **URL:** https://github.com/William-kelvem94/TRANSCRITOR
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 47114 KB | **Árvore:** 243 arquivos, 0 diretórios
- **README:** README.md (4825 caracteres)
- **Manifestos:** `package.json`, `pyproject.toml`, `requirements.txt`, `docker-compose.yml`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite, Python, Docker, GitHub Actions
- **Objetivo/descrição:** # 🎥 TRANSCRITOR Sistema completo de transcrição e resumo de áudios/vídeos usando IA, com arquitetura de microserviços. ## 🚀 Características
- **Sinais:** testes=sim, CI=sim, Docker=sim, docs=sim, lockfile=não evidenciado
- **Riscos estruturais:** manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** explicitar licença

### Evidência de manifestos

**package.json**

```
{
  "devDependencies": {
    "@types/node": "^24.10.1"
  }
}

```

**pyproject.toml**

```
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "transcritor"
version = "2.0.0"
description = "Sistema completo de transcrição e resumo de áudio/vídeo com IA"
requires-python = ">=3.10"
authors = [
    {name = "TRANSCRITOR Team", email = "contact@transcritor.dev"}
]
readme = "README.md"
license = {text = "MIT"}

[tool.black]
line-length = 120
target-version = ['py310', 'py311', 'py312']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | build
  | dist
  | node_modules
)/
'''

[tool.ruff]
```

**requirements.txt**

```
# TRANSCRITOR - Dependências Completas
# ====================================

# Core AI - Transcrição
openai-whisper>=20231117
torch>=2.0.0
torchaudio>=2.0.0

# Resumos e NLP
transformers>=4.30.0
sentencepiece>=0.1.99
protobuf>=3.20.0

# Processamento de áudio/vídeo
moviepy>=2.0.0
ffmpeg-python>=0.2.0
librosa>=0.10.0
soundfile>=0.12.0

# API e Web
fastapi>=0.104.1
uvicorn[standard]>=0.24.0
pydantic>=2.5.0
httpx>=0.25.0
python-multipart>=0.0.6

# Message Queue
pika>=1.3.2
redis>=5.0.0

# Database
sqlalchemy>=2.0.23
psycopg2-binary>=2.9.9
alembic>=1.12.0

```


---

## William-kelvem94/vibe-coding-platform

- **URL:** https://github.com/William-kelvem94/vibe-coding-platform
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 0 KB | **Árvore:** 0 arquivos, 0 diretórios
- **README:** não localizado
- **Manifestos:** nenhum identificado
- **Stack inferida:** Sem arquivos acessíveis
- **Objetivo/descrição:** Objetivo não documentado no README acessível.
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** README ausente ou não acessível; testes não evidenciados pela árvore; CI/CD não evidenciado; árvore não acessível ou repositório vazio
- **Lacunas recomendadas:** documentar propósito, instalação, uso e estado; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


---

## William-kelvem94/webflash-intermediador-de-demandas

- **URL:** https://github.com/William-kelvem94/webflash-intermediador-de-demandas
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 19317 KB | **Árvore:** 37 arquivos, 0 diretórios
- **README:** README.md (612 caracteres)
- **Manifestos:** `Makefile`, `package.json`, `package-lock.json`, `docker-compose.yml`
- **Stack inferida:** Node.js/JavaScript, Docker
- **Objetivo/descrição:** # WebFlash - Intermediador de Demandas Separate WebFlash-oriented project for demand mediation experiments. ## Status
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=sim, docs=não evidenciado, lockfile=sim
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados

### Evidência de manifestos

**Makefile**

```
# WebFlash - Sistema de Demandas
# Makefile para facilitar operações Docker

.PHONY: help build up down restart logs clean dev prod test

# Cores para output
GREEN := \033[0;32m
YELLOW := \033[1;33m
BLUE := \033[0;34m
NC := \033[0m # No Color

# Ajuda
help:
	@echo "$(BLUE)🚀 WebFlash - Sistema de Demandas$(NC)"
	@echo ""
	@echo "Comandos disponíveis:"
	@echo "  $(GREEN)make build$(NC)     - Construir imagens Docker"
	@echo "  $(GREEN)make up$(NC)        - Iniciar todos os serviços"
	@echo "  $(GREEN)make down$(NC)      - Parar todos os serviços"
	@echo "  $(GREEN)make restart$(NC)   - Reiniciar todos os serviços"
	@echo "  $(GREEN)make logs$(NC)      - Ver logs de todos os serviços"
	@echo "  $(GREEN)make logs-backend$(NC) - Ver logs apenas do backend"
	@echo "  $(GREEN)make logs-frontend$(NC) - Ver logs apenas do frontend"
	@echo "  $(GREEN)make clean$(NC)     - Limpar containers e volumes"
	@echo "  $(GREEN)make dev$(NC)       - Ambiente de desenvolvimento completo"
	@echo "  $(GREEN)make status$(NC)    - Verificar status dos serviços"
	@echo "  $(GREEN)make test$(NC)      - Executar testes"
	@echo ""

# Construir imagens
build:
	@echo "$(BLUE)🔨 Construindo imagens Docker...$(NC)"
	docker-compose -f docker-compose.dev.yml build --no-cache
	@echo "$(GREEN)✅ Imagens construídas com sucesso!$(NC)"

```

**package.json**

```
{
  "devDependencies": {
    "@ljharb/tsconfig": "^0.3.2"
  }
}

```


---

## William-kelvem94/Will-obsidian

- **URL:** https://github.com/William-kelvem94/Will-obsidian
- **Branch padrão:** `main`
- **Visibilidade:** public | **Arquivado:** não
- **Tamanho GitHub:** 28790 KB | **Árvore:** 2832 arquivos, 0 diretórios
- **README:** README.md (4314 caracteres)
- **Manifestos:** `requirements.txt`, `requirements-locked.txt`, `.scripts/mcp-vault-server/package.json`
- **Stack inferida:** Node.js/JavaScript, JavaScript, Python, GitHub Actions
- **Objetivo/descrição:** # Will Vault - Obsidian Neural Hub Este repositorio e o vault principal do Obsidian do Will. A estrutura numerada abaixo e a fonte canonica para navegacao, conhecimento, projetos, JARVIS, skills, vida pessoal, operacoes do vault, interfaces, sistema tecnico, dados brutos e templates. Para navegar, comece por:
- **Sinais:** testes=sim, CI=sim, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** nenhum sinal estrutural adicional detectado
- **Lacunas recomendadas:** nenhuma lacuna estrutural básica detectada

### Evidência de manifestos

**requirements.txt**

```
# Core dependencies for Vault scripts
python-dotenv==1.0.0
numpy==1.26.0
tqdm==4.66.1
requests==2.32.4

# Knowledge Indexing (RAG Pipeline)
sentence-transformers==2.2.2
torch==2.2.0
faiss-cpu==1.7.4

```

**requirements-locked.txt**

```
#
# This file is autogenerated by pip-compile with Python 3.14
# by the following command:
#
#    pip-compile --output-file=requirements-locked.txt requirements.in
#
annotated-doc==0.0.4
    # via typer
anyio==4.13.0
    # via httpx
certifi==2026.4.22
    # via
    #   httpcore
    #   httpx
click==8.4.0
    # via typer
colorama==0.4.6
    # via
    #   click
    #   tqdm
faiss-cpu==1.13.2
    # via -r requirements.in
filelock==3.29.0
    # via
    #   huggingface-hub
    #   torch
fsspec==2026.4.0
    # via
    #   huggingface-hub
    #   torch
h11==0.16.0
    # via httpcore
hf-xet==1.5.0
    # via huggingface-hub
httpcore==1.0.9
```

**.scripts/mcp-vault-server/package.json**

```
{
  "name": "mcp-vault-server",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "type": "commonjs",
  "engines": {
    "node": ">=18 <21"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.29.0"
  }
}

```


---

## William-kelvem94/Will.Nexus

- **URL:** https://github.com/William-kelvem94/Will.Nexus
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 330 KB | **Árvore:** 235 arquivos, 0 diretórios
- **README:** README.md (8465 caracteres)
- **Manifestos:** `Dockerfile`, `compose.yaml`, `package.json`
- **Stack inferida:** Node.js/JavaScript, TypeScript, Next.js, Docker
- **Objetivo/descrição:** # WillNexus WillNexus é o **Software Control Plane pessoal e AI-first** do ecossistema de projetos de William Pereira. Ele une duas funções principais:
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=sim, docs=sim, lockfile=não evidenciado
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença

### Evidência de manifestos

**Dockerfile**

```
# syntax=docker/dockerfile:1
FROM node:24-bookworm-slim AS deps
WORKDIR /app
ENV NEXT_TELEMETRY_DISABLED=1
COPY package.json ./
RUN npm install --no-audit --no-fund

FROM node:24-bookworm-slim AS builder
WORKDIR /app
ENV NEXT_TELEMETRY_DISABLED=1
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN mkdir -p public && npm run build

FROM node:24-bookworm-slim AS runner
WORKDIR /app
ENV NODE_ENV=production \
    NEXT_TELEMETRY_DISABLED=1 \
    HOSTNAME=0.0.0.0 \
    PORT=3000
RUN groupadd --system --gid 1001 nodejs && useradd --system --uid 1001 --gid nodejs nextjs
COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static
USER nextjs
EXPOSE 3000
CMD ["node", "server.js"]

```

**compose.yaml**

```
services:
  willnexus:
    build:
      context: .
      target: runner
    container_name: willnexus
    restart: unless-stopped
    env_file:
      - .env.local
    ports:
      - "3000:3000"
    healthcheck:
      test: ["CMD", "node", "-e", "fetch('http://127.0.0.1:3000/api/health').then(r=>{if(!r.ok)process.exit(1)}).catch(()=>process.exit(1))"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 20s

```

**package.json**

```
{
  "name": "willnexus",
  "version": "0.4.1",
  "private": true,
  "description": "Software Portfolio Intelligence para o ecossistema de projetos Kelvem",
  "author": "William-kelvem94",
  "engines": {
    "node": "24.x"
  },
  "scripts": {
    "dev": "next dev",
    "build": "next build --webpack",
    "start": "next start",
    "type-check": "tsc --noEmit",
    "check": "npm run type-check && npm run build",
    "docker:up": "docker compose up --build",
    "docker:down": "docker compose down"
  },
  "dependencies": {
    "@supabase/supabase-js": "2.112.2",
    "@vercel/oidc": "3.8.5",
    "lucide-react": "0.577.0",
    "next": "16.3.0",
    "react": "19.2.8",
    "react-dom": "19.2.8",
    "server-only": "0.0.1"
  },
  "devDependencies": {
    "@types/node": "22.19.15",
    "@types/react": "19.2.18",
    "@types/react-dom": "19.2.4",
    "typescript": "5.7.2"
  }
}

```


---

## William-kelvem94/WilletHub

- **URL:** https://github.com/William-kelvem94/WilletHub
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 58 KB | **Árvore:** 46 arquivos, 0 diretórios
- **README:** README.md (1545 caracteres)
- **Manifestos:** `Dockerfile`, `package.json`, `package-lock.json`, `docker-compose.yml`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Docker
- **Objetivo/descrição:** # WilletHub Plataforma para organizar demandas e vagas em um hub unico com visoes de documento, kanban, operacao e canvas, com persistencia local e opcao de sincronizacao remota. ## O que existe hoje
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=sim, docs=não evidenciado, lockfile=sim
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**Dockerfile**

```
FROM mcr.microsoft.com/playwright:v1.60.0-jammy

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos do package.json
COPY package*.json ./

# Instala dependências
RUN npm ci

# Copia todo o código do projeto
COPY . .

# Compila o projeto TypeScript
RUN npm run build

# Expõe a porta do dashboard web
EXPOSE 3000

# Define variáveis padrão do container
ENV HEADLESS=true
ENV PORT=3000

# Comando para iniciar o servidor do dashboard compilado
CMD ["node", "dist/server.js"]

```

**package.json**

```
{
  "name": "willethub",
  "version": "1.0.0",
  "description": "WilletHub com hub visual, automacao de vagas e persistencia local/remota",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "start:dev": "ts-node src/index.ts",
    "test-ai": "node dist/testAi.js",
    "test-ai:dev": "ts-node src/testAi.ts",
    "dashboard": "node dist/server.js",
    "dashboard:dev": "ts-node src/server.ts"
  },
  "dependencies": {
    "@supabase/supabase-js": "^2.108.1",
    "axios": "^1.7.2",
    "csv-writer": "^1.6.0",
    "dotenv": "^16.4.5",
    "express": "^5.2.1",
    "pdf-parse": "1.1.1",
    "playwright": "^1.44.1"
  },
  "devDependencies": {
    "@types/express": "^5.0.6",
    "@types/node": "^20.14.2",
    "@types/pdf-parse": "^1.1.5",
    "ts-node": "^10.9.2",
    "typescript": "^5.4.5"
  }
}

```

**package-lock.json**

```
{
  "name": "willethub",
  "version": "1.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "willethub",
      "version": "1.0.0",
      "dependencies": {
        "@supabase/supabase-js": "^2.108.1",
        "axios": "^1.7.2",
        "csv-writer": "^1.6.0",
        "dotenv": "^16.4.5",
        "express": "^5.2.1",
        "pdf-parse": "1.1.1",
        "playwright": "^1.44.1"
      },
      "devDependencies": {
        "@types/express": "^5.0.6",
        "@types/node": "^20.14.2",
        "@types/pdf-parse": "^1.1.5",
        "ts-node": "^10.9.2",
        "typescript": "^5.4.5"
      }
    },
    "node_modules/@cspotcode/source-map-support": {
      "version": "0.8.1",
      "resolved": "https://registry.npmjs.org/@cspotcode/source-map-support/-/source-map-support-0.8.1.tgz",
      "integrity": "sha512-IchNf6dN4tHoMFIn/7OE8LWZ19Y6q/67Bmf6vnGREv8RSbBVb9LPJxEcnwrcwX6ixSvaiGoomAUvu4YSxXrVgw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/trace-mapping": "0.3.9"
      },
```

**docker-compose.yml**

```
services:
  organizador:
    build: .
    container_name: organizador_sync_dashboard
    ports:
      - "3000:3000"
    volumes:
      - ./CURRICULO ORIGINAL:/app/CURRICULO ORIGINAL
      - ./vagas_oportunidades.csv:/app/vagas_oportunidades.csv
      - ./.browser_session:/app/.browser_session
      - .env:/app/.env
    environment:
      - PORT=3000
      - HEADLESS=true
    restart: always

```


---

## William-kelvem94/willethub-legacy

- **URL:** https://github.com/William-kelvem94/willethub-legacy
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 1104 KB | **Árvore:** 115 arquivos, 0 diretórios
- **README:** README.md (602 caracteres)
- **Manifestos:** `backend/Dockerfile`, `docker-compose.yml`, `backend/package.json`, `frontend/package.json`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Vite, Docker
- **Objetivo/descrição:** # WilletHub Separate Notion-style workspace project. ## Status
- **Sinais:** testes=sim, CI=não evidenciado, Docker=sim, docs=sim, lockfile=sim
- **Riscos estruturais:** CI/CD não evidenciado; dependência/configuração usa marcador latest; baixa reprodutibilidade; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação; explicitar licença; registrar governança, segurança e histórico de mudanças

### Evidência de manifestos

**backend/Dockerfile**

```
FROM node:20-alpine

# Install OpenSSL for Prisma
RUN apk add --no-cache openssl openssl-dev

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

# Generate Prisma client
RUN npx prisma generate

CMD ["npm", "run", "dev"]

```

**docker-compose.yml**

```
## Removido campo 'version' obsoleto
services:
  postgres:
    image: postgres:15-alpine
    container_name: notion_postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
      POSTGRES_DB: notion_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - notion_network
  redis:
    image: redis:7-alpine
    container_name: notion_redis
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - notion_network
  minio:
```

**backend/package.json**

```
{
  "name": "notion-backend",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "tsx watch src/app.ts",
    "build": "tsc",
    "start": "node dist/app.js",
    "test": "jest",
    "db:migrate": "prisma migrate dev",
    "db:seed": "tsx src/database/seed.ts"
  },
  "dependencies": {
    "@prisma/client": "^5.7.0",
    "@types/bcryptjs": "^2.4.6",
    "@types/jsonwebtoken": "^9.0.5",
    "bcryptjs": "^2.4.3",
    "cors": "^2.8.5",
    "dotenv": "^16.3.1",
    "express": "^4.18.2",
    "express-validator": "^7.0.1",
    "jsonwebtoken": "^9.0.2",
    "minio": "^7.1.3",
    "multer": "^1.4.5-lts.1",
    "openai": "^4.20.1",
    "pg": "^8.10.0",
    "redis": "^4.6.10",
    "socket.io": "^4.7.0",
    "winston": "^3.11.0"
  },
  "devDependencies": {
    "@types/express": "^4.17.21",
    "@types/node": "^20.10.1",
    "jest": "^29.7.0",
    "nodemon": "^3.0.2",
```

**frontend/package.json**

```
{
  "name": "notion-frontend",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "vite --host",
    "build": "vite build",
    "preview": "vite preview",
    "test": "vitest"
  },
  "dependencies": {
    "@dnd-kit/core": "^6.1.0",
    "@dnd-kit/sortable": "^8.0.0",
    "@dnd-kit/utilities": "^3.2.2",
    "@shadcn/ui": "latest",
    "@tanstack/react-query": "^5.28.0",
    "@tiptap/core": "^2.1.0",
    "@tiptap/extension-code-block-lowlight": "^2.1.0",
    "@tiptap/extension-color": "^2.1.0",
    "@tiptap/extension-highlight": "^2.1.0",
    "@tiptap/extension-image": "^2.1.0",
    "@tiptap/extension-link": "^2.1.0",
    "@tiptap/extension-placeholder": "^2.1.0",
    "@tiptap/extension-table": "^2.1.0",
    "@tiptap/extension-table-cell": "^2.1.0",
    "@tiptap/extension-table-header": "^2.1.0",
    "@tiptap/extension-table-row": "^2.1.0",
    "@tiptap/extension-task-item": "^2.1.0",
    "@tiptap/extension-task-list": "^2.1.0",
    "@tiptap/extension-text-align": "^2.1.0",
    "@tiptap/extension-typography": "^2.1.0",
    "@tiptap/extension-underline": "^2.1.0",
    "@tiptap/pm": "^2.1.0",
    "@tiptap/react": "^2.1.0",
    "@tiptap/starter-kit": "^2.1.0",
```


---

## William-kelvem94/WILLFINANCE-9.0

- **URL:** https://github.com/William-kelvem94/WILLFINANCE-9.0
- **Branch padrão:** `main`
- **Visibilidade:** private | **Arquivado:** não
- **Tamanho GitHub:** 170 KB | **Árvore:** 236 arquivos, 0 diretórios
- **README:** README.md (9416 caracteres)
- **Manifestos:** `Makefile`, `Dockerfile`, `package.json`, `pnpm-lock.yaml`
- **Stack inferida:** Node.js/JavaScript, TypeScript, JavaScript, Next.js, Docker
- **Objetivo/descrição:** # FinanceApp - Gerenciador Financeiro Completo Gerenciador financeiro moderno, responsivo e inteligente com IA integrada, OCR de documentos e automação completa. Desenvolvido com Next.js 16, React 19, TypeScript e PostgreSQL. ## Destaques
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=sim, docs=não evidenciado, lockfile=sim
- **Riscos estruturais:** testes não evidenciados pela árvore; CI/CD não evidenciado; dependência/configuração usa marcador latest; baixa reprodutibilidade; manifesto contém URLs; revisar fontes externas e pinagem
- **Lacunas recomendadas:** definir pipeline mínimo de validação; criar testes automatizados; explicitar licença

### Evidência de manifestos

**Makefile**

```
.PHONY: help build up down restart logs shell db-shell db-reset clean

help: ## Mostra esta mensagem de ajuda
	@echo "Comandos disponíveis:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

build: ## Constrói as imagens Docker
	docker-compose build

up: ## Inicia os containers
	docker-compose up -d
	@echo "✅ Containers iniciados!"
	@echo "🌐 Aplicação disponível em: http://localhost:3000"

down: ## Para os containers
	docker-compose down

restart: ## Reinicia os containers
	docker-compose restart

logs: ## Mostra os logs (use logs-app ou logs-db para específicos)
	docker-compose logs -f

logs-app: ## Mostra logs apenas da aplicação
	docker-compose logs -f app

logs-db: ## Mostra logs apenas do banco de dados
	docker-compose logs -f postgres

shell: ## Acessa o shell do container da aplicação
	docker-compose exec app sh

db-shell: ## Acessa o shell do PostgreSQL
	docker-compose exec postgres psql -U willfinance -d willfinance

```

**Dockerfile**

```
# Dockerfile para FinanceApp - Next.js 16
# Multi-stage build para otimização

# Stage 1: Dependencies
FROM node:20-alpine AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app

# Habilitar corepack e pnpm
RUN corepack enable && corepack prepare pnpm@latest --activate

# Copiar arquivos de dependências
COPY package.json pnpm-lock.yaml ./

# Instalar dependências
RUN pnpm install

# Stage 2: Builder
FROM node:20-alpine AS builder
WORKDIR /app

# Habilitar corepack e pnpm
RUN corepack enable && corepack prepare pnpm@latest --activate

# Copiar dependências do stage anterior
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Variáveis de ambiente para build
ENV NEXT_TELEMETRY_DISABLED=1
ENV NODE_ENV=production
ARG DATABASE_URL
ENV DATABASE_URL=${DATABASE_URL:-postgresql://placeholder:placeholder@localhost:5432/placeholder}

# Build da aplicação
```

**package.json**

```
{
  "name": "my-v0-project",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "build": "next build",
    "dev": "next dev",
    "lint": "eslint .",
    "start": "next start"
  },
  "dependencies": {
    "@hookform/resolvers": "^3.10.0",
    "@neondatabase/serverless": "1.0.2",
    "@radix-ui/react-accordion": "1.2.2",
    "@radix-ui/react-alert-dialog": "1.1.4",
    "@radix-ui/react-aspect-ratio": "1.1.1",
    "@radix-ui/react-avatar": "1.1.2",
    "@radix-ui/react-checkbox": "1.1.3",
    "@radix-ui/react-collapsible": "1.1.2",
    "@radix-ui/react-context-menu": "2.2.4",
    "@radix-ui/react-dialog": "1.1.4",
    "@radix-ui/react-dropdown-menu": "2.1.4",
    "@radix-ui/react-hover-card": "1.1.4",
    "@radix-ui/react-label": "2.1.1",
    "@radix-ui/react-menubar": "1.1.4",
    "@radix-ui/react-navigation-menu": "1.2.3",
    "@radix-ui/react-popover": "1.1.4",
    "@radix-ui/react-progress": "1.1.1",
    "@radix-ui/react-radio-group": "1.2.2",
    "@radix-ui/react-scroll-area": "1.2.2",
    "@radix-ui/react-select": "2.1.4",
    "@radix-ui/react-separator": "1.1.1",
    "@radix-ui/react-slider": "1.2.2",
    "@radix-ui/react-slot": "1.1.1",
    "@radix-ui/react-switch": "1.1.2",
```

**pnpm-lock.yaml**

```
lockfileVersion: '9.0'

settings:
  autoInstallPeers: true
  excludeLinksFromLockfile: false
```


---

## William-kelvem94/William-kelvem94

- **URL:** https://github.com/William-kelvem94/William-kelvem94
- **Branch padrão:** `main`
- **Visibilidade:** public | **Arquivado:** não
- **Tamanho GitHub:** 5 KB | **Árvore:** 1 arquivos, 0 diretórios
- **README:** README.md (3023 caracteres)
- **Manifestos:** nenhum identificado
- **Stack inferida:** Indeterminada
- **Objetivo/descrição:** <div align="center"> # William-kelvem94 ### IA local, automação, web apps e ferramentas práticas
- **Sinais:** testes=não evidenciado, CI=não evidenciado, Docker=não evidenciado, docs=não evidenciado, lockfile=não evidenciado
- **Riscos estruturais:** manifesto de dependências não identificado; testes não evidenciados pela árvore; CI/CD não evidenciado
- **Lacunas recomendadas:** declarar dependências e versão de runtime; definir pipeline mínimo de validação; criar testes automatizados; explicitar licença; registrar governança, segurança e histórico de mudanças


## Limitações e próximos passos técnicos

1. Resolver dependências transitivas com instalação controlada em ambiente isolado.
2. Executar análise AST/import graph para projetos com código acessível.
3. Validar workflows e testes sem executar ações destrutivas.
4. Separar forks/mirrors de projetos autorais por histórico e origem.
5. Fazer auditoria de segredos e licenças somente com scanners locais e regras explícitas.
6. Para repositórios muito grandes ou árvores truncadas, clonar em lotes e gerar métricas locais.
