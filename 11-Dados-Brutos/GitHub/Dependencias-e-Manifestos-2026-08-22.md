---
title: Dependências e manifestos dos repositórios GitHub
type: dados-brutos-github
status: atual
updated: 2026-08-22
classe_privacidade: operacional
indexavel: true
uso_ia: permitido
---

# Dependências e manifestos

Coleta realizada em 22/08/2026 nos 85 repositórios. Foram localizados **105 manifestos em 55 repositórios**. Os conteúdos abaixo são evidência bruta; não foram executados nem considerados seguros automaticamente.

## 1. William-kelvem94/ada_v2---jarvis

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 2. William-kelvem94/ADB_Android-s_Will

- **Manifestos detectados:** `docker-compose.yml`

### docker-compose.yml

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
      - ./runtime:/app/runtime
      - ./Infos_celularres:/app/Infos_celularres:ro
    tmpfs:
      - /tmp:size=64m,noexec,nosuid,nodev

```

---

## 3. William-kelvem94/AFFiNE-Will

- **Manifestos detectados:** `package.json`, `Cargo.toml`

### package.json

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
    "typecheck": "tsc -b tsconfig.json --verbose",
    "postinstall": "yarn affine init && yarn husky"
  },
  "lint-staged": {
    "*": "prettier --write --ignore-unknown --cache",
    "*.{ts,tsx,mjs,js,jsx}": [
      "prettier --ignore-unknown --write",
      "cross-env NODE_OPTIONS=\"--max-old-space-size=16384\" eslint --cache --fix"
    ],
    "*.toml": [
      "taplo format"
    ],
    "*.rs": [
      "cargo fmt --"
    ]
  },
  "devDependencies": {
    "@affine-tools/cli": "workspace:*",
    "@capacitor/cli": "^7.6.5",
    "@eslint/js": "^9.39.2",
    "@faker-js/faker": "^10.1.0",
    "@istanbuljs/schema": "^0.1.3",
    "@magic-works/i18n-codegen": "^0.6.1",
    "@playwright/test": "=1.58.2",
    "@smarttools/eslint-plugin-rxjs": "^1.0.8",
    "@taplo/cli": "^0.7.0",
    "@toeverything/infra": "workspace:*",
    "@types/eslint": "^9.6.1",
    "@types/node": "^22.0.0",
    "@typescript-eslint/parser": "^8.55.0",
    "@vanilla-extract/vite-plugin": "^5.0.0",
    "@vitest/browser": "^4.0.18",
    "@vitest/coverage-istanbul": "^4.0.18",
    "@vitest/ui": "^4.0.18",
    "cross-env": "^10.1.0",
    "electron": "^39.0.0",
    "eslint": "^9.39.2",
    "eslint-config-prettier": "^10.1.8",
    "eslint-import-resolver-typescript": "^4.4.4",
    "eslint-plugin-import-x": "^4.16.1",
    "eslint-plugin-lit": "^2.2.1",
    "eslint-plugin-oxlint": "1.67.0",
    "eslint-plugin-react": "^7.37.5",
    "eslint-plugin-react-hooks": "^7.0.1",
    "eslint-plugin-simple-import-sort": "^12.1.1",
    "eslint-plugin-sonarjs": "^4.0.2",
    "happy-dom": "^20.0.0",
    "husky": "^9.1.7",
    "lint-staged": "^16.0.0",
    "msw": "^2.13.2",
    "oxlint": "1.67.0",
    "oxlint-tsgolint": "^0.23.0",
    "prettier": "^3.7.4",
    "semver": "^7.7.3",
    "typescript": "^5.9.3",
    "typescript-eslint": "^8.55.0",
    "unplugin-swc": "^1.5.9",
    "vite": "^7.2.7",
    "vitest": "^4.0.18"
  },
  "packageManager": "yarn@4.13.0",
  "resolutions": {
    "array-buffer-byte-length": "npm:@nolyfill/array-buffer-byte-length@^1",
    "array-includes": "npm:@nolyfill/array-includes@^1",
    "array.prototype.flat": "npm:@nolyfill/array.prototype.flat@^1",
    "array.prototype.flatmap": "npm:@nolyfill/array.prototype.flatmap@^1",
    "array.prototype.tosorted": "npm:@nolyfill/array.prototype.tosorted@^1",
    "arraybuffer.prototype.slice": "npm:@nolyfill/arraybuffer.prototype.slice@^1",
    "asynciterator.prototype": "npm:@nolyfill/asynciterator.prototype@^1",
    "available-typed-arrays": "npm:@nolyfill/available-typed-arrays@^1",
    "deep-equal": "npm:@nolyfill/deep-equal@^1",
    "define-properties": "npm:@nolyfill/define-properties@^1",
    "es-iterator-helpers": "npm:@nolyfill/es-iterator-helpers@^1",
    "es-set-tostringtag": "npm:@nolyfill/es-set-tostringtag@^1",
    "function-bind": "npm:@nolyfill/function-bind@^1",
    "function.prototype.name": "npm:@nolyfill/function.prototype.name@^1",
    "get-symbol-description": "npm:@nolyfill/get-symbol-description@^1",
    "globalthis": "npm:@nolyfill/globalthis@^1",
    "gopd": "npm:@nolyfill/gopd@^1",
    "has": "npm:@nolyfill/has@^1",
    "has-property-descriptors": "npm:@nolyfill/has-property-descriptors@^1",
    "has-proto": "npm:@nolyfill/has-proto@^1",
    "has-symbols": "npm:@nolyfill/has-symbols@^1",
    "has-tostringtag": "npm:@nolyfill/has-tostringtag@^1",
    "is-arguments": "npm:@nolyfill/is-arguments@^1",
    "is-array-buffer": "npm:@nolyfill/is-array-buffer@^1",
    "is-date-object": "npm:@nolyfill/is-date-object@^1",
    "is-generator-function": "npm:@nolyfill/is-generator-function@^1",
    "is-regex": "npm:@nolyfill/is-regex@^1",
    "is-shared-array-buffer": "npm:@nolyfill/is-shared-array-buffer@^1",
    "is-string": "npm:@nolyfill/is-string@^1",
    "is-symbol": "npm:@nolyfill/is-symbol@^1",
    "is-weakref": "npm:@nolyfill/is-weakref@^1",
    "iterator.prototype": "npm:@nolyfill/iterator.prototype@^1",
    "json-stable-stringify": "npm:@nolyfill/json-stable-stringify@^1",
    "jsonify": "npm:@nolyfill/jsonify@^1",
    "object-is": "npm:@nolyfill/object-is@^1",
    "object-keys": "npm:@nolyfill/object-keys@^1",
    "object.assign": "npm:@nolyfill/object.assign@^1",
    "object.entries": "npm:@nolyfill/object.entries@^1",
    "object.fromentries": "npm:@nolyfill/object.fromentries@^1",
    "object.hasown": "npm:@nolyfill/object.hasown@^1",
    "object.values": "npm:@nolyfill/object.values@^1",
    "on-headers": "npm:on-headers@^1.1.0",
    "reflect.getprototypeof": "npm:@nolyfill/reflect.getprototypeof@^1",
    "regexp.prototype.flags": "npm:@nolyfill/regexp.prototype.flags@^1",
    "safe-array-concat": "npm:@nolyfill/safe-array-concat@^1",
    "safe-regex-test": "npm:@nolyfill/safe-regex-test@^1",
    "side-channel": "npm:@nolyfill/side-channel@^1",
    "string.prototype.matchall": "npm:@nolyfill/string.prototype.matchall@^1",
    "string.prototype.trim": "npm:@nolyfill/string.prototype.trim@^1",
    "string.prototype.trimend": "npm:@nolyfill/string.prototype.trimend@^1",
    "string.prototype.trimstart": "npm:@nolyfill/string.prototype.trimstart@^1",
    "typed-array-buffer": "npm:@nolyfill/typed-array-buffer@^1",
    "typed-array-byte-length": "npm:@nolyfill/typed-array-byte-length@^1",
    "typed-array-byte-offset": "npm:@nolyfill/typed-array-byte-offset@^1",
    "typed-array-length": "npm:@nolyfill/typed-array-length@^1",
    "unbox-primitive": "npm:@nolyfill/unbox-primitive@^1",
    "which-boxed-primitive": "npm:@nolyfill/which-boxed-primitive@^1",
    "which-typed-array": "npm:@nolyfill/which-typed-array@^1",
    "array-flatten": "npm:@nolyfill/array-flatten@^1",
    "array.prototype.findlast": "npm:@nolyfill/array.prototype.findlast@^1",
    "hasown": "npm:@nolyfill/hasown@^1",
    "internal-slot": "npm:@nolyfill/internal-slot@^1",
    "is-core-module": "npm:@nolyfill/is-core-module@^1",
    "is-typed-array": "npm:@nolyfill/is-typed-array@^1",
    "isarray": "npm:@nolyfill/isarray@^1",
    "safe-buffer": "npm:@nolyfill/safe-buffer@^1",
    "safer-buffer": "npm:@nolyfill/safer-buffer@^1",
    "set-function-length": "npm:@nolyfill/set-function-length@^1",
    "string.prototype.repeat": "npm:@nolyfill/string.prototype.repeat@^1",
    "typedarray": "npm:@nolyfill/typedarray@^1",
    "macos-alias": "npm:@napi-rs/macos-alias@0.0.4",
    "fs-xattr": "npm:@napi-rs/xattr@latest",
    "ioredis": "5.8.2",
    "decode-named-character-reference@npm:^1.0.0": "patch:decode-named-character-reference@npm%3A1.0.2#~/.yarn/patches/decode-named-character-reference-npm-1.0.2-db17a755fd.patch",
    "@atlaskit/pragmatic-drag-and-drop": "patch:@atlaskit/pragmatic-drag-and-drop@npm%3A1.4.0#~/.yarn/patches/@atlaskit-pragmatic-drag-and-drop-npm-1.4.0-75c45f52d3.patch",
    "yjs": "patch:yjs@npm%3A13.6.21#~/.yarn/patches/yjs-npm-13.6.21-c9f1f3397c.patch"
  }
}

```

### Cargo.toml

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
  criterion = { version = "0.5", features = ["html_reports"] }
  criterion2 = { version = "3", default-features = false }
  crossbeam-channel = "0.5"
  dispatch2 = "0.3"
  docx-parser = { git = "https://github.com/toeverything/docx-parser", rev = "380beea" }
  dotenvy = "0.15"
  file-format = { version = "0.28", features = ["reader"] }
  hex = "0.4"
  homedir = "0.3"
  image = { version = "0.25.9", default-features = false, features = [
    "bmp",
    "gif",
    "jpeg",
    "png",
    "webp",
  ] }
  infer = { version = "0.19.0" }
  lasso = { version = "0.7", features = ["multi-threaded"] }
  lib0 = { version = "0.16", features = ["lib0-serde"] }
  libc = "0.2"
  libwebp-sys = "0.14.2"
  little_exif = "0.6.23"
  llm_adapter = { version = "0.2", default-features = false }
  llm_runtime = { version = "0.2", default-features = false }
  log = "0.4"
  loom = { version = "0.7", features = ["checkpoint"] }
  lru = "0.16"
  matroska = "0.30"
  memory-indexer = "0.3.1"
  mermaid-rs-renderer = { git = "https://github.com/toeverything/mermaid-rs-renderer", rev = "fba9097", default-features = false }
  mimalloc = "0.1"
  mp4parse = "0.17"
  nanoid = "0.4"
  napi = { version = "3.7.0", features = [
    "async",
    "chrono_date",
    "error_anyhow",
    "napi9",
    "serde",
  ] }
  napi-build = { version = "2" }
  napi-derive = { version = "3.4" }
  nom = "8"
  notify = { version = "8", features = ["serde"] }
  objc2 = "0.6"
  objc2-foundation = "0.3"
  ogg = "0.9"
  once_cell = "1"
  ordered-float = "5"
  p256 = { version = "0.13", features = ["ecdsa", "pem"] }
  parking_lot = "0.12"
  path-ext = "0.1.2"
  pdf-extract = { git = "https://github.com/toeverything/pdf-extract", branch = "darksky/improve-font-decoding" }
  phf = { version = "0.11", features = ["macros"] }
  proptest = "1.3"
  proptest-derive = "0.5"
  pulldown-cmark = "0.13"
  rand = "0.9"
  rand_chacha = "0.9"
  rand_distr = "0.5"
  rayon = "1.10"
  readability = { version = "0.3.0", default-features = false }
  regex = "1.10"
  rubato = "0.16"
  schemars = "0.8"
  screencapturekit = "0.3"
  serde = "1"
  serde_json = "1"
  sha2 = "0.10"
  sha3 = "0.10"
  smol_str = "0.3"
  sqlx = { version = "0.8", default-features = false, features = [
    "chrono",
    "macros",
    "migrate",
    "runtime-tokio",
    "sqlite",
  ] }
  strum_macros = "0.27.0"
  symphonia = { version = "0.5", features = ["all", "opt-simd"] }
  text-splitter = "0.27"
  thiserror = "2"
  tiktoken-rs = "0.7"
  tokio = "1.45"
  tree-sitter = { version = "0.25" }
  tree-sitter-c = { version = "0.24" }
  tree-sitter-c-sharp = { version = "0.23" }
  tree-sitter-cpp = { version = "0.23" }
  tree-sitter-go = { version = "0.23" }
  tree-sitter-java = { version = "0.23" }
  tree-sitter-javascript = { version = "0.23" }
  tree-sitter-kotlin-ng = { version = "1.1" }
  tree-sitter-python = { version = "0.23" }
  tree-sitter-rust = { version = "0.24" }
  tree-sitter-scala = { version = "0.24" }
  tree-sitter-typescript = { version = "0.23" }
  typst = "0.14.2"
  typst-as-lib = { version = "0.15.4", default-features = false, features = [
    "packages",
    "typst-kit-embed-fonts",
    "typst-kit-fonts",
    "ureq",
  ] }
  typst-svg = "0.14.2"
  uniffi = "0.29"
  url = { version = "2.5" }
  uuid = "1.8"
  v_htmlescape = "0.15"
  windows = { version = "0.61", features = [
    "Win32_Devices_FunctionDiscovery",
    "Win32_Foundation",
    "Win32_Media_Audio",
    "Win32_System_Com",
    "Win32_System_Com_StructuredStorage",
    "Win32_System_Diagnostics_ToolHelp",
    "Win32_System_ProcessStatus",
    "Win32_System_Threading",
    "Win32_System_Variant",
    "Win32_UI_Shell_PropertiesSystem",
  ] }
  windows-core = { version = "0.61" }
  y-octo = { path = "./packages/common/y-octo/core" }
  y-sync = { version = "0.4" }
  yrs = "0.23.0"

[profile.dev.package.sqlx-macros]
opt-level = 3

[profile.release]
codegen-units = 1
lto           = true
opt-level     = 3
strip         = "symbols"

  # android uniffi bindgen requires symbols
  [profile.release.package.affine_mobile_native]
  strip = "none"

  # [patch.crates-io]
  # llm_adapter = { path = "../llm_adapter/crates/llm_adapter" }
  # llm_runtime = { path = "../llm_adapter/crates/llm_runtime" }

```

---

## 4. William-kelvem94/AGENTE-IA

- **Manifestos detectados:** `requirements.txt`, `Dockerfile`, `docker-compose.yml`

### requirements.txt

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

### Dockerfile

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

### docker-compose.yml

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

---

## 5. William-kelvem94/AppFlowy-Will

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 6. William-kelvem94/Atividade-01

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 7. William-kelvem94/Atividade-03

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 8. William-kelvem94/att_18_ago

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 9. William-kelvem94/AULA_PROG_AVAN

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 10. William-kelvem94/Auto-boletos

- **Manifestos detectados:** `requirements.txt`, `Dockerfile`, `docker-compose.yml`

### requirements.txt

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

### Dockerfile

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

FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=src.app \
    FLASK_ENV=production \
    PYTHONPATH=/app \
    PATH="/opt/venv/bin:$PATH"

# Install runtime dependencies + Node (for potential tools)
RUN apt-get update && apt-get install -y --no-install-recommends \
    nodejs npm \
    # Xvfb for headless display
    xvfb \
    curl \
    # Tesseract OCR for AI functionality (lazy)
    tesseract-ocr tesseract-ocr-por \
    # Playwright Chromium deps
    libnss3 libatk-bridge2.0-0 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 \
    # OpenCV minimal
    libgl1 libglib2.0-0 \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Create app directory
WORKDIR /app

# Copy frontend build
COPY --from=frontend-builder /app/frontend/dist/ src/static/

# Copy Python code
COPY src/ src/

# Copy requirements and other files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers (Chromium only for minimal size) with system dependencies
RUN playwright install --with-deps chromium

# Create necessary directories with appropriate permissions
RUN mkdir -p /app/downloads /app/instance && \
    chmod 755 /app/downloads /app/instance

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Run Flask directly (Render handles headless)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--worker-tmp-dir", "/dev/shm", "src.app:app"]



```

### docker-compose.yml

```
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: auto-boletos
    ports:
      - "5000:5000"
    environment:
      - FLASK_APP=src.app
      - FLASK_ENV=production
      - PYTHONPATH=/app
      - SECRET_KEY=${SECRET_KEY:-your-secret-key-change-in-production}
      - DATABASE_URL=sqlite:////app/data/auto_boletos.db
      - EQUATORIAL_URL=${EQUATORIAL_URL:-https://ap.equatorialenergia.com.br/}
      - CORS_ORIGINS=${CORS_ORIGINS:-*}
    volumes:
      # Persist database
      - ./data:/app/data
      # Persist downloaded bills
      - ./downloads:/app/downloads
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "python", "-c", "import sys; import requests; sys.exit(0 if requests.get('http://localhost:5000/api/ai/status', timeout=5).status_code == 200 else 1)"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    networks:
      - auto-boletos-network

networks:
  auto-boletos-network:
    driver: bridge

```

---

## 11. William-kelvem94/AUTOBOT

- **Manifestos detectados:** `requirements.txt`, `Dockerfile`, `docker-compose.yml`

### requirements.txt

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
# numpy>=1.24.0
# transformers>=4.35.0
# pandas>=2.0.0
# textblob>=0.17.1

# === DEVELOPMENT TOOLS ===
# Install with: pip install -r requirements-dev.txt
# pytest>=7.4.0
# black>=23.0.0
# flake8>=6.0.0
```

### Dockerfile

```
# AUTOBOT - Optimized Multi-stage Dockerfile
# Builds a production-ready container with minimal size

# === Build Stage ===
FROM python:3.11-slim as builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
COPY requirements-ai.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --user -r requirements.txt

# === Production Stage ===
FROM python:3.11-slim

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Create non-root user for security
RUN groupadd -r autobot && useradd -r -g autobot autobot

# Set working directory
WORKDIR /app

# Copy Python packages from builder
COPY --from=builder /root/.local /home/autobot/.local

# Copy application code
COPY --chown=autobot:autobot . .

# Create necessary directories
RUN mkdir -p IA/logs IA/memoria_conversas tmp \
    && chown -R autobot:autobot IA tmp

# Set environment variables
ENV PATH=/home/autobot/.local/bin:$PATH
ENV PYTHONPATH=/app
ENV FLASK_APP=autobot.api:create_app
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

# Switch to non-root user
USER autobot

# Expose port
EXPOSE 5000

# Default command
CMD ["python", "main.py"]
```

### docker-compose.yml

```
version: '3.8'

services:
  # Redis cache service
  redis:
    image: redis:7-alpine
    container_name: autobot-redis
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    restart: unless-stopped
    command: redis-server --appendonly yes
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3
    
  # Ollama AI service (optional)
  ollama:
    image: ollama/ollama:latest
    container_name: autobot-ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    restart: unless-stopped
    environment:
      - OLLAMA_ORIGINS=*
      - OLLAMA_HOST=0.0.0.0
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:11434/api/tags"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s
    profiles:
      - ai  # Only start with: docker-compose --profile ai up
    
  # Main AUTOBOT application
  autobot:
    build: 
      context: .
      dockerfile: Dockerfile
    container_name: autobot-api
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - DEBUG=False
      - REDIS_HOST=redis
      - REDIS_PORT=6379
      - OLLAMA_URL=http://ollama:11434
      - ENABLE_AI=true
      - ENABLE_CORPORATE_INTEGRATIONS=true
      - ENABLE_AUTOMATION=true
    depends_on:
      redis:
        condition: service_healthy
    volumes:
      - ./IA/logs:/app/IA/logs
      - autobot_data:/app/IA/memoria_conversas
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 30s
  
  # Optional: Web frontend (if you have one)
  # frontend:
  #   build: ./web
  #   container_name: autobot-frontend
  #   ports:
  #     - "3000:3000"
  #   depends_on:
  #     - autobot
  #   restart: unless-stopped

volumes:
  redis_data:
    driver: local
  ollama_data:
    driver: local
  autobot_data:
    driver: local

networks:
  default:
    name: autobot-network
```

---

## 12. William-kelvem94/Automatizador

- **Manifestos detectados:** `pyproject.toml`

### pyproject.toml

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

---

## 13. William-kelvem94/BITRIX-DADOS

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 14. William-kelvem94/C.A.I.N.E

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 15. William-kelvem94/CLONNER

- **Manifestos detectados:** `requirements.txt`, `pyproject.toml`, `Dockerfile`, `docker-compose.yml`

### requirements.txt

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

### pyproject.toml

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
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false
disallow_incomplete_defs = false
check_untyped_defs = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
ignore_missing_imports = true
exclude = [
    "archive/",
    "venv/",
    "env/",
    ".venv/",
    "migrations/",
    "tests/",
]

[[tool.mypy.overrides]]
module = [
    "selenium.*",
    "undetected_chromedriver.*",
    "flask.*",
    "bs4.*",
]
ignore_missing_imports = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "-v",
    "--strict-markers",
    "--tb=short",
    "--cov=src",
    "--cov-report=term-missing",
    "--cov-report=html",
    "--cov-report=xml",
    "--cov-fail-under=80",
]
markers = [
    "unit: Unit tests",
    "integration: Integration tests",
    "e2e: End-to-end tests",
    "slow: Slow running tests",
    "requires_selenium: Tests that require Selenium",
    "requires_docker: Tests that require Docker",
]

[tool.coverage.run]
source = ["src"]
omit = [
    "*/tests/*",
    "*/test_*.py",
    "*/__pycache__/*",
    "*/venv/*",
    "*/env/*",
    "*/migrations/*",
    "*/archive/*",
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
    "if TYPE_CHECKING:",
    "@abstractmethod",
]
precision = 2
show_missing = true
skip_covered = false

[tool.coverage.html]
directory = "htmlcov"


```

### Dockerfile

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
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    libu2f-udev \
    libvulkan1 \
    # Ferramentas úteis
    curl \
    unzip \
    git \
    # Xvfb para headless
    xvfb \
    # Fontes adicionais
    fonts-dejavu-core \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# Instalar Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome-keyring.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Criar diretório da aplicação
WORKDIR /app

# Copiar requirements primeiro (cache de camadas)
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY src/ ./src/
COPY templates/ ./templates/
COPY static/ ./static/
COPY start.py .

# Copiar e configurar script de inicialização
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh && \
    sed -i 's/\r$//' /app/docker-entrypoint.sh || true

# Criar diretórios necessários
RUN mkdir -p projects logs static/js static/css templates && \
    chmod -R 755 /app

# Criar usuário não-root para segurança
RUN useradd -m -u 1000 cloner && \
    chown -R cloner:cloner /app

# Mudar para usuário não-root
USER cloner

# Expor porta
EXPOSE 5000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:5000/api/health || exit 1

# Comando padrão - executar entrypoint e depois API
CMD ["/bin/bash", "/app/docker-entrypoint.sh", "python", "src/api.py"]

```

### docker-compose.yml

```
services:
  # ============================================
  # API GATEWAY - Interface Web e Coordenação
  # ============================================
  api-gateway:
    build:
      context: .
      dockerfile: docker/api-gateway.Dockerfile
    container_name: cloner-api-gateway
    image: cloner-api-gateway:latest
    
    ports:
      - "8000:5000"
    
    volumes:
      - ./projects:/app/projects:ro
      - ./logs:/app/logs
    
    environment:
      - FLASK_APP=engines/api_gateway/main.py
      - FLASK_ENV=production
      - SECRET_KEY=${SECRET_KEY:-change-this-secret-key}
      - HOST=0.0.0.0
      - PORT=5000
      - PYTHONUNBUFFERED=1
      - PYTHONPATH=/app
      
      # Serviços internos
      - CLONER_ENGINE_URL=http://cloner-engine:5001
      - FILE_MANAGER_URL=http://file-manager:5002
      - STEALTH_ENGINE_URL=http://stealth-engine:5003
    
    depends_on:
      cloner-engine:
        condition: service_healthy
      file-manager:
        condition: service_healthy
      stealth-engine:
        condition: service_healthy
    
    restart: unless-stopped
    
    networks:
      - cloner-network
    
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 20s

  # ============================================
  # CLONER ENGINE - Motor de Clonagem
  # ============================================
  cloner-engine:
    build:
      context: .
      dockerfile: docker/cloner-engine.Dockerfile
    container_name: cloner-engine
    image: cloner-engine:latest
    
    volumes:
      - ./projects:/app/projects
      - ./logs:/app/logs
      - cloner-data:/app/data
    
    environment:
      - PYTHONUNBUFFERED=1
      - PYTHONPATH=/app
      - PORT=5001
      - HOST=0.0.0.0
      - DISPLAY=:99
      - HEADLESS=true
      - MAX_CONCURRENT_CLONES=3
      - MAX_WORKERS=5
      - MIN_DELAY_BETWEEN_REQUESTS=0.5
      - STEALTH_ENGINE_URL=http://stealth-engine:5003
      - FILE_MANAGER_URL=http://file-manager:5002
    
    restart: unless-stopped
    
    networks:
      - cloner-network
    
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 4G
        reservations:
          cpus: '1.0'
          memory: 2G
    
    security_opt:
      - no-new-privileges:true
    
    cap_add:
      - SYS_ADMIN
    
    shm_size: '2gb'
    
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5001/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s

  # ============================================
  # FILE MANAGER - Organização de Arquivos
  # ============================================
  file-manager:
    build:
      context: .
      dockerfile: docker/file-manager.Dockerfile
    container_name: cloner-file-manager
    image: cloner-file-manager:latest
    
    volumes:
      - ./projects:/app/projects
      - file-manager-data:/app/data
    
    environment:
      - PYTHONUNBUFFERED=1
      - PYTHONPATH=/app
      - PORT=5002
      - HOST=0.0.0.0
      - MAX_WORKERS=5
    
    restart: unless-stopped
    
    networks:
      - cloner-network
    
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 2G
        reservations:
          cpus: '0.5'
          memory: 1G
    
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5002/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 20s

  # ============================================
  # STEALTH ENGINE - Anti-Detecção
  # ============================================
  stealth-engine:
    build:
      context: .
      dockerfile: docker/stealth-engine.Dockerfile
    container_name: cloner-stealth-engine
    image: cloner-stealth-engine:latest
    
    volumes:
      - stealth-data:/app/data
    
    environment:
      - PYTHONUNBUFFERED=1
      - PYTHONPATH=/app
      - PORT=5003
      - HOST=0.0.0.0
      - DISPLAY=:99
      - HEADLESS=true
    
    restart: unless-stopped
    
    networks:
      - cloner-network
    
    deploy:
      resources:
        limits:
          cpus: '1.5'
          memory: 3G
        reservations:
          cpus: '0.5'
          memory: 1G
    
    security_opt:
      - no-new-privileges:true
    
    cap_add:
      - SYS_ADMIN
    
    shm_size: '1gb'
    
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5003/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

# ============================================
# NETWORKS
# ============================================
networks:
  cloner-network:
    driver: bridge

# ============================================
# VOLUMES
# ============================================
volumes:
  cloner-data:
    driver: local
  file-manager-data:
    driver: local
  stealth-data:
    driver: local

```

---

## 16. William-kelvem94/CONVERSOR-DE-FORMATO-DE-ARQUIVO

- **Manifestos detectados:** `package.json`, `Dockerfile`, `docker-compose.yml`

### package.json

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
    "pdf-lib": "^1.17.1",
    "mammoth": "^1.6.0",
    "electron": "^28.0.0",
    "nextron": "^8.4.0",
    "fluent-ffmpeg": "^2.1.2",
    "heic2any": "^0.0.4",
    "pdfjs-dist": "^3.11.174",
    "pptxgenjs": "^3.12.0",
    "xlsx": "^0.18.5",
    "html2pdf.js": "^0.10.1",
    "pizzip": "^3.1.4",
    "docx-preview": "^0.1.4",
    "jszip": "^3.10.1"
  },
  "devDependencies": {
    "@types/node": "^20.0.0",
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "typescript": "^5.0.0",
    "tailwindcss": "^3.3.0",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.31",
    "eslint": "^8.0.0",
    "eslint-config-next": "^14.0.0",
    "@types/fluent-ffmpeg": "^2.1.24"
  },
  "keywords": [
    "conversor",
    "arquivos",
    "react",
    "nextjs",
    "framer-motion",
    "tailwindcss",
    "typescript"
  ],
  "author": "Desenvolvedor",
  "license": "MIT"
}
```

### Dockerfile

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
ENV NEXT_TELEMETRY_DISABLED=1
ENV PORT=3000
ENV HOSTNAME="0.0.0.0"

# Copiar apenas arquivos necessários
COPY --from=prod-deps /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./
COPY --from=builder /app/.next ./.next
# Criar pasta public (pode estar vazia)
RUN mkdir -p ./public

# Expor porta
EXPOSE 3000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost:3000 || exit 1

# Comando para iniciar
CMD ["npm", "start"]


```

### docker-compose.yml

```
services:
  conversor-web:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: conversor-arquivos
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - PORT=3000
      - NEXT_TELEMETRY_DISABLED=1
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost:3000"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    networks:
      - conversor-network

  conversor-dev:
    build:
      context: .
      dockerfile: Dockerfile.dev
    container_name: conversor-arquivos-dev
    ports:
      - "1000:3000"
    environment:
      - NODE_ENV=development
      - PORT=3000
      - NEXT_TELEMETRY_DISABLED=1
      - WATCHPACK_POLLING=true
    volumes:
      - .:/app
      - /app/node_modules
      - /app/.next
    restart: unless-stopped
    networks:
      - conversor-network

networks:
  conversor-network:
    driver: bridge


```

---

## 17. William-kelvem94/CORETEMP-SOUNDPAD

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 18. William-kelvem94/Criador_de_audios

- **Manifestos detectados:** `pyproject.toml`, `docker-compose.yml`

### pyproject.toml

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
uvicorn = {version = "^0.24.0", extras = ["standard"]}
pydantic = {version = "^2.5.0", extras = ["email"]}
pydantic-settings = "^2.1.0"
python-multipart = "^0.0.6"

# 🔄 HTTP & Async
httpx = "^0.25.0"
aiofiles = "^23.2.1"

# 📊 Monitoramento & Observabilidade
prometheus-client = "^0.19.0"
psutil = "^5.9.6"
structlog = "^23.2.0"

# 🔒 Segurança & Autenticação
python-jose = {version = "^3.3.0", extras = ["cryptography"]}
passlib = {version = "^1.7.4", extras = ["bcrypt"]}
cryptography = "^41.0.0"
slowapi = "^0.1.9"

# 🗄️ Banco de Dados & Cache
sqlalchemy = {version = "^2.0.0", extras = ["asyncio"]}
aiosqlite = "^0.19.0"  # Para desenvolvimento
alembic = "^1.12.0"
redis = {version = "^4.6.0", extras = ["hiredis"]}

# 🎵 Processamento de Áudio (Adaptativo)
piper-tts = "^1.2.0"  # TTS mais leve que Coqui
torch = {version = "^2.1.0", optional = true}  # GPU support opcional
torchaudio = {version = "^2.1.0", optional = true}
numpy = "^1.24.3"
scipy = "^1.11.3"
librosa = "^0.10.1"
soundfile = "^0.12.1"
pydub = "^0.25.1"

# ⚙️ Utilitários Essenciais
click = "^8.1.0"
python-dotenv = "^1.0.0"
rich = "^13.7.0"

[tool.poetry.group.dev.dependencies]
# 🧪 Testes Avançados
pytest = "^7.4.0"
pytest-cov = "^4.1.0"
pytest-asyncio = "^0.21.0"
pytest-mock = "^3.12.0"
pytest-xdist = "^3.5.0"
pytest-benchmark = "^4.0.0"

# 🎨 Qualidade de Código
black = "^23.9.1"
isort = "^5.12.0"
flake8 = "^6.0.0"
mypy = "^1.5.1"
bandit = "^1.7.5"
safety = "^2.3.5"
pre-commit = "^3.5.0"

# 📚 Documentação
mkdocs = "^1.5.0"
mkdocs-material = "^9.4.0"
mkdocstrings = {version = "^0.23.0", extras = ["python"]}

# 🐳 Desenvolvimento
watchfiles = "^0.20.0"
jupyter = "^1.0.0"
notebook = "^7.0.0"

# 🛠️ Ferramentas
ipdb = "^0.13.0"
typer = "^0.9.0"

[tool.poetry.group.gpu.dependencies]
# 🎮 GPU Support (Opcional)
torch = {version = "^2.1.0", source = "pytorch-gpu"}
torchaudio = {version = "^2.1.0", source = "pytorch-gpu"}

[[tool.poetry.source]]
name = "pytorch-gpu"
url = "https://download.pytorch.org/whl/cu121"
priority = "explicit"

[tool.poetry.scripts]
api-gateway = "services.api-gateway.main:main"
backend-service = "services.backend-service.main:app"
tts-service = "services.tts-service.main:main"
auth-service = "services.auth-service.main:main"
file-service = "services.file-service.main:main"

# 🧪 Configurações de Teste Otimizadas
[tool.pytest.ini_options]
minversion = "7.0"
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "-v",
    "--tb=short",
    "--strict-markers",
    "--cov=services",
    "--cov-report=html:htmlcov",
    "--cov-report=xml",
    "--cov-report=term-missing",
    "--cov-fail-under=75",  # Mais realista
    "-p no:warnings",  # Reduzir output
]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests",
    "unit: marks tests as unit tests",
    "e2e: marks tests as end-to-end tests",
    "gpu: requires GPU",
    "performance: performance benchmarks",
]

# 📊 Cobertura Adaptativa
[tool.coverage.run]
source = ["services", "src"]
omit = [
    "*/tests/*",
    "*/test_*",
    "*/venv/*",
    "*/__pycache__/*",
    "*/migrations/*",
    "*/alembic/*",
    "build/docker/*",
    "*/node_modules/*",
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "if settings.DEBUG",
    "raise AssertionError",
    "raise NotImplementedError",
    "if 0:",
    "if __name__ == .__main__.:",
    "class .*\\bProtocol\\):",
    "@(abc\\.)?abstractmethod",
    "logger\.",
]

# 🎨 Formatação Moderna
[tool.black]
line-length = 100
target-version = ['py310']
include = '\.pyi?$'
extend-exclude = '''
/(
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
  | node_modules
  | htmlcov
)/
'''

[tool.isort]
profile = "black"
line_length = 100
multi_line_output = 3
include_trailing_comma = true
force_grid_wrap = 0
use_parentheses = true
ensure_newline_before_comments = true
known_first_party = ["services", "src"]
known_third_party = [
    "fastapi",
    "uvicorn",
    "pydantic",
    "sqlalchemy",
    "torch",
    "librosa",
    "piper_tts",
]

# 🔍 Type Checking Adaptativo
[tool.mypy]
python_version = "3.10"
check_untyped_defs = true
disallow_any_generics = true
disallow_incomplete_defs = true
disallow_untyped_defs = true
no_implicit_optional = true
warn_redundant_casts = true
warn_return_any = true
warn_unused_configs = true
warn_unused_ignores = true
strict_equality = true
show_error_codes = true

[[tool.mypy.overrides]]
module = [
    "torch.*",
    "torchaudio.*",
    "librosa.*",
    "soundfile.*",
    "piper.*",
]
ignore_missing_imports = true

# 🐛 Linting com Ruff (Mais rápido que flake8)
[tool.ruff]
line-length = 100
target-version = "py310"

[tool.ruff.lint]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4", # flake8-comprehensions
    "UP", # pyupgrade
    "SIM", # flake8-simplify
]
ignore = [
    "E203", # whitespace before ':'
    "E501", # line too long, handled by black
    "B008", # do not perform function calls in argument defaults
    "C901", # too complex
    "SIM108", # use ternary operator
]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]
"tests/**/*" = ["B011", "S101"]  # Allow assert and os.chmod in tests

# 🔒 Segurança Aprimorada
[tool.bandit]
exclude_dirs = ["tests", "build", "docs", "node_modules", "htmlcov"]
skips = ["B101", "B601", "B603"]  # Skip asserts, shell usage, subprocess

# 🚀 Configurações de Build
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.build]
generate-setup-file = false
script-files = ["scripts/**/*.py", "scripts/**/*.sh"]
"tests/**/*" = ["B011"]
```

### docker-compose.yml

```
# 🚀 Criador de Áudios v3.0 - Arquitetura de Microserviços
# Sistema verdadeiramente distribuído e escalável

# ==========================================
# ⚙️ CONFIGURAÇÕES GLOBAIS
# ==========================================

x-default-opts: &default-opts
  restart: unless-stopped
  networks:
    - criador-audios-network

x-healthcheck-opts: &healthcheck-opts
  interval: 30s
  timeout: 10s
  retries: 3

x-dev-volumes: 
  - ./services:/app/services:ro
  - ./pyproject.toml:/app/pyproject.toml:ro

# ==========================================
# 🏗️ INFRAESTRUTURA CORE
# ==========================================

services:

  # ==========================================
  # 🚀 API GATEWAY - PONTO DE ENTRADA ÚNICO
  # ==========================================
  api-gateway:
    <<: *default-opts
    build:
      context: .
      dockerfile: docker/services/api-gateway/Dockerfile
      target: production
      args:
        BUILDKIT_INLINE_CACHE: 1
    container_name: criador-audios-api-gateway
    ports:
      - "${GATEWAY_PORT:-8000}:8000"
    environment:
      - ENVIRONMENT=production
      - LOG_LEVEL=INFO
      - BACKEND_SERVICE_URL=http://backend-service:8000
      - TTS_SERVICE_URL=http://tts-service:8000
      - AUTH_SERVICE_URL=http://auth-service:8001
      - FILE_SERVICE_URL=http://file-service:8002
    depends_on:
      - backend-service
      - tts-service
      - auth-service
      - file-service
    healthcheck:
      <<: *healthcheck-opts
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      start_period: 40s
    profiles:
      - prod
      - microservices

  # ==========================================
  # 🔧 BACKEND SERVICE - LÓGICA DE NEGÓCIO
  # ==========================================
  backend-service:
    <<: *default-opts
    build:
      context: .
      dockerfile: docker/services/backend-service/Dockerfile
      target: production
      args:
        BUILDKIT_INLINE_CACHE: 1
    container_name: criador-audios-backend-service
    environment:
      - ENVIRONMENT=production
      - LOG_LEVEL=WARNING
      - DATABASE_URL=postgresql://criador_user:criador_password_2024@postgres:5432/criador_audios
      - REDIS_URL=redis://keydb:6379/0
      - AUTH_SERVICE_URL=http://auth-service:8001
      - FILE_SERVICE_URL=http://file-service:8002
    volumes:
      - audio_outputs:/data/audio
      - logs:/data/logs
      - cache:/data/cache
    depends_on:
      - postgres
      - keydb
    healthcheck:
      <<: *healthcheck-opts
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      start_period: 40s
    profiles:
      - prod
      - microservices

  # ==========================================
  # 🤖 TTS SERVICE - SÍNTESE DE VOZ
  # ==========================================
  tts-service:
    <<: *default-opts
    build:
      context: .
      dockerfile: docker/services/tts-service/Dockerfile
      target: production
      args:
        BUILDKIT_INLINE_CACHE: 1
    container_name: criador-audios-tts-service
    environment:
      - ENVIRONMENT=production
      - LOG_LEVEL=INFO
      - REDIS_URL=redis://keydb:6379/0
      - AUTH_SERVICE_URL=http://auth-service:8001
    volumes:
      - models:/app/models
      - cache:/app/cache
    depends_on:
      - keydb
    healthcheck:
      <<: *healthcheck-opts
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      start_period: 60s
    profiles:
      - prod
      - microservices

  # ==========================================
  # 🔐 AUTH SERVICE - AUTENTICAÇÃO
  # ==========================================
  auth-service:
    <<: *default-opts
    build:
      context: .
      dockerfile: docker/services/auth-service/Dockerfile
      target: production
      args:
        BUILDKIT_INLINE_CACHE: 1
    container_name: criador-audios-auth-service
    environment:
      - ENVIRONMENT=production
      - LOG_LEVEL=INFO
      - REDIS_URL=redis://keydb:6379/0
      - JWT_SECRET_KEY=${JWT_SECRET_KEY:-your-secret-key}
    depends_on:
      - keydb
    healthcheck:
      <<: *healthcheck-opts
      test: ["CMD", "curl", "-f", "http://localhost:8001/health"]
      start_period: 20s
    profiles:
      - prod
      - microservices

  # ==========================================
  # 📁 FILE SERVICE - GERENCIAMENTO DE ARQUIVOS
  # ==========================================
  file-service:
    <<: *default-opts
    build:
      context: .
      dockerfile: docker/services/file-service/Dockerfile
      target: production
      args:
        BUILDKIT_INLINE_CACHE: 1
    container_name: criador-audios-file-service
    environment:
      - ENVIRONMENT=production
      - LOG_LEVEL=INFO
      - UPLOAD_DIR=/app/uploads
      - AUDIO_DIR=/app/audio
      - MAX_FILE_SIZE=50MB
    volumes:
      - file_uploads:/app/uploads
      - audio_storage:/app/audio
    healthcheck:
      <<: *healthcheck-opts
      test: ["CMD", "curl", "-f", "http://localhost:8002/health"]
      start_period: 20s
    profiles:
      - prod
      - microservices

  # ==========================================
  # 🌐 FRONTEND SERVICE - INTERFACE WEB
  # ==========================================
  frontend-service:
    <<: *default-opts
    build:
      context: .
      dockerfile: services/frontend-service/Dockerfile
    container_name: criador-audios-frontend-service
    ports:
      - "${FRONTEND_PORT:-3000}:80"
    depends_on:
      - backend-service
    healthcheck:
      <<: *healthcheck-opts
      test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost/health"]
      start_period: 5s
    profiles:
      - prod
      - microservices

  # ==========================================
  # 📊 MONITORING SERVICE - HEALTH & METRICS
  # ==========================================
  monitoring-service:
    <<: *default-opts
    build:
      context: .
      dockerfile: docker/services/monitoring-service/Dockerfile
      target: production
      args:
        BUILDKIT_INLINE_CACHE: 1
    container_name: criador-audios-monitoring-service
    ports:
      - "${MONITORING_PORT:-8003}:8003"
    healthcheck:
      <<: *healthcheck-opts
      test: ["CMD", "curl", "-f", "http://localhost:8003/health"]
      start_period: 20s
    profiles:
      - prod
      - microservices
      - monitoring

  # ==========================================
  # 🗄️ BANCO DE DADOS E CACHE
  # ==========================================

  postgres:
    <<: *default-opts
    image: postgres:15-alpine
    container_name: criador-audios-postgres
    environment:
      - POSTGRES_DB=criador_audios
      - POSTGRES_USER=criador_user
      - POSTGRES_PASSWORD=criador_password_2024
    volumes:
      - postgres_data:/var/lib/postgresql/data

    healthcheck:
      <<: *healthcheck-opts
      test: ["CMD-SHELL", "pg_isready -U criador_user -d criador_audios"]
      start_period: 10s
    profiles:
      - prod
      - microservices

  # ⚡ KeyDB - Cache ultra-rápido (2x mais rápido que Redis)
  keydb:
    <<: *default-opts
    image: eqalpha/keydb:latest
    container_name: criador-audios-keydb
    command: >
      keydb-server
      --maxmemory 512mb
      --maxmemory-policy allkeys-lru
      --tcp-keepalive 300
      --timeout 300
      --save 900 1
      --save 300 10
      --save 60 10000
      --appendonly yes
      --protected-mode no
      --bind 0.0.0.0
    ports:
      - "${REDIS_PORT:-6379}:6379"
    volumes:
      - keydb_data:/data
    healthcheck:
      <<: *healthcheck-opts
      test: ["CMD", "keydb-cli", "ping"]
      start_period: 5s
    environment:
      - KEYDB_PASSWORD=${REDIS_PASSWORD:-}
    profiles:
      - prod
      - microservices

  # ==========================================
  # 📊 MONITORAMENTO (OPCIONAL)
  # ==========================================

  prometheus:
    <<: *default-opts
    image: prom/prometheus:latest
    container_name: criador-audios-prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./docker/monitoring/monitoring/prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
    profiles:
      - monitoring

  grafana:
    <<: *default-opts
    image: grafana/grafana:latest
    container_name: criador-audios-grafana
    ports:
      - "${GRAFANA_PORT:-3001}:3000"
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=criador2024!
    volumes:
      - grafana_data:/var/lib/grafana
    profiles:
      - monitoring

# ==========================================
# 📦 VOLUMES EXPANDIDOS
# ==========================================

volumes:
  # Dados dos serviços
  audio_outputs:
    name: criador_de_audios_audio_outputs
    driver: local
  logs:
    name: criador_de_audios_logs
    driver: local
  cache:
    name: criador_de_audios_cache
    driver: local
  models:
    name: criador_de_audios_models
    driver: local
  file_uploads:
    name: criador_de_audios_file_uploads
    driver: local
  audio_storage:
    name: criador_de_audios_audio_storage
    driver: local

  # Infraestrutura
  postgres_data:
    name: criador_de_audios_postgres_data
    driver: local
  keydb_data:
    name: criador_de_audios_keydb_data
    driver: local
  prometheus_data:
    name: criador_de_audios_prometheus_data
    driver: local
  grafana_data:
    name: criador_de_audios_grafana_data
    driver: local

# ==========================================
# 🌐 REDES AVANÇADAS
# ==========================================

networks:
  criador-audios-network:
    name: criador_de_audios_network
    driver: bridge
```

---

## 19. William-kelvem94/crud_basico

- **Manifestos detectados:** `package.json`, `composer.json`

### package.json

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

### composer.json

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
        "post-autoload-dump": [
            "Illuminate\\Foundation\\ComposerScripts::postAutoloadDump",
            "@php artisan package:discover --ansi"
        ],
        "post-update-cmd": [
            "@php artisan vendor:publish --tag=laravel-assets --ansi --force"
        ],
        "post-root-package-install": [
            "@php -r \"file_exists('.env') || copy('.env.example', '.env');\""
        ],
        "post-create-project-cmd": [
            "@php artisan key:generate --ansi"
        ]
    },
    "extra": {
        "laravel": {
            "dont-discover": []
        }
    },
    "config": {
        "optimize-autoloader": true,
        "preferred-install": "dist",
        "sort-packages": true,
        "allow-plugins": {
            "pestphp/pest-plugin": true,
            "php-http/discovery": true
        }
    },
    "minimum-stability": "stable",
    "prefer-stable": true
}

```

---

## 20. William-kelvem94/crud_basico-2.0

- **Manifestos detectados:** `package.json`, `composer.json`

### package.json

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

### composer.json

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
        "post-autoload-dump": [
            "Illuminate\\Foundation\\ComposerScripts::postAutoloadDump",
            "@php artisan package:discover --ansi"
        ],
        "post-update-cmd": [
            "@php artisan vendor:publish --tag=laravel-assets --ansi --force"
        ],
        "post-root-package-install": [
            "@php -r \"file_exists('.env') || copy('.env.example', '.env');\""
        ],
        "post-create-project-cmd": [
            "@php artisan key:generate --ansi"
        ]
    },
    "extra": {
        "laravel": {
            "dont-discover": []
        }
    },
    "config": {
        "optimize-autoloader": true,
        "preferred-install": "dist",
        "sort-packages": true,
        "allow-plugins": {
            "pestphp/pest-plugin": true,
            "php-http/discovery": true
        }
    },
    "minimum-stability": "stable",
    "prefer-stable": true
}

```

---

## 21. William-kelvem94/CRUD_BASICO-3.0

- **Manifestos detectados:** `package.json`, `composer.json`

### package.json

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

### composer.json

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
        "post-autoload-dump": [
            "Illuminate\\Foundation\\ComposerScripts::postAutoloadDump",
            "@php artisan package:discover --ansi"
        ],
        "post-update-cmd": [
            "@php artisan vendor:publish --tag=laravel-assets --ansi --force"
        ],
        "post-root-package-install": [
            "@php -r \"file_exists('.env') || copy('.env.example', '.env');\""
        ],
        "post-create-project-cmd": [
            "@php artisan key:generate --ansi"
        ]
    },
    "extra": {
        "laravel": {
            "dont-discover": []
        }
    },
    "config": {
        "optimize-autoloader": true,
        "preferred-install": "dist",
        "sort-packages": true,
        "allow-plugins": {
            "pestphp/pest-plugin": true,
            "php-http/discovery": true
        }
    },
    "minimum-stability": "stable",
    "prefer-stable": true
}

```

---

## 22. William-kelvem94/CRUD_BASICO4.0

- **Manifestos detectados:** `package.json`, `composer.json`

### package.json

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

### composer.json

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
        "post-autoload-dump": [
            "Illuminate\\Foundation\\ComposerScripts::postAutoloadDump",
            "@php artisan package:discover --ansi"
        ],
        "post-update-cmd": [
            "@php artisan vendor:publish --tag=laravel-assets --ansi --force"
        ],
        "post-root-package-install": [
            "@php -r \"file_exists('.env') || copy('.env.example', '.env');\""
        ],
        "post-create-project-cmd": [
            "@php artisan key:generate --ansi"
        ]
    },
    "extra": {
        "laravel": {
            "dont-discover": []
        }
    },
    "config": {
        "optimize-autoloader": true,
        "preferred-install": "dist",
        "sort-packages": true,
        "allow-plugins": {
            "pestphp/pest-plugin": true,
            "php-http/discovery": true
        }
    },
    "minimum-stability": "stable",
    "prefer-stable": true
}

```

---

## 23. William-kelvem94/CRUD_VENDAS_WILL

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 24. William-kelvem94/DEEP-LEARNING

- **Manifestos detectados:** `requirements.txt`

### requirements.txt

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
pydantic-settings>=2.13.0
rich>=14.0.0

httpx==0.27.0                   # HTTP assíncrono
rich==13.7.1                    # Terminal bonito
colorlog==6.8.1

# --- Machine Learning / Self-Evolution ---
# NOTA: bitsandbytes oficial e Linux-only. Usamos a versao Windows.
torch>=2.2.0
transformers>=4.42.0
peft>=0.11.0
accelerate>=0.33.0
trl>=0.9.6                      # SFTTrainer para Fine-Tuning simplificado
datasets>=2.20.0                # Manipulacao de datasets de treino
bitsandbytes-windows>=0.43.0     # Versao compatível com Windows

```

---

## 25. William-kelvem94/DEEPSEEK-JARVIS-LOCAL

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 26. William-kelvem94/DeepSeek-V3---C-PIA

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 27. William-kelvem94/demandas-organizadas

- **Manifestos detectados:** `package.json`, `docker-compose.yml`

### package.json

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
    "gestao",
    "sistema",
    "premium",
    "docker",
    "react",
    "nodejs"
  ],
  "author": "William Pereira",
  "license": "MIT",
  "engines": {
    "node": ">=18.0.0",
    "npm": ">=9.0.0"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/William-kelvem94/DEMANDAS_ORGANIZADAS.git"
  }
}

```

### docker-compose.yml

```
services:
  # --- Banco de Dados PostgreSQL ---
  postgres:
    image: postgres:15-alpine
    container_name: demandas_postgres_prod
    environment:
      POSTGRES_DB: ${DB_DATABASE}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    ports:
      - "${DB_PORT}:5432"
    volumes:
      - postgres_prod_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER} -d ${DB_DATABASE}"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - demandas_net
    restart: unless-stopped

  # --- Cache Redis ---
  redis:
    image: redis:7-alpine
    container_name: demandas_redis_prod
    command: redis-server --appendonly yes --requirepass ${REDIS_PASSWORD}
    ports:
      - "${REDIS_PORT}:6379"
    volumes:
      - redis_prod_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "-a", "${REDIS_PASSWORD}", "ping"]
      interval: 10s
      timeout: 3s
      retries: 5
    networks:
      - demandas_net
    restart: unless-stopped

  # --- Backend API (Node.js/Express) ---
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: demandas_backend_prod
    env_file:
      - .env
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    ports:
      - "4001:3000" # Mapeia a porta do host para a porta interna do container
    networks:
      - demandas_net
    restart: unless-stopped

  # --- Frontend (React/Vite com Nginx) ---
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: demandas_frontend_prod
    ports:
      - "80:80"
    depends_on:
      - backend
    networks:
      - demandas_net
    restart: unless-stopped

  # --- Adminer (Gerenciador de Banco de Dados) ---
  adminer:
    image: adminer:latest
    container_name: demandas_adminer_prod
    ports:
      - "8080:8080"
    depends_on:
      - postgres
    networks:
      - demandas_net
    restart: unless-stopped

volumes:
  postgres_prod_data:
    driver: local
  redis_prod_data:
    driver: local

networks:
  demandas_net:
    driver: bridge

```

---

## 28. William-kelvem94/demandas-organizadas-v2-legacy

- **Manifestos detectados:** `package.json`, `Cargo.toml`

### package.json

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
    "typecheck": "tsc -b tsconfig.json --verbose",
    "postinstall": "yarn affine init && yarn husky"
  },
  "lint-staged": {
    "*": "prettier --write --ignore-unknown --cache",
    "*.{ts,tsx,mjs,js,jsx}": [
      "prettier --ignore-unknown --write",
      "cross-env NODE_OPTIONS=\"--max-old-space-size=8192\" eslint --cache --fix"
    ],
    "*.toml": [
      "taplo format"
    ],
    "*.rs": [
      "cargo fmt --"
    ]
  },
  "devDependencies": {
    "@affine-tools/cli": "workspace:*",
    "@capacitor/cli": "^7.0.0",
    "@eslint/js": "^9.39.2",
    "@faker-js/faker": "^10.1.0",
    "@istanbuljs/schema": "^0.1.3",
    "@magic-works/i18n-codegen": "^0.6.1",
    "@playwright/test": "=1.58.2",
    "@smarttools/eslint-plugin-rxjs": "^1.0.8",
    "@taplo/cli": "^0.7.0",
    "@toeverything/infra": "workspace:*",
    "@types/eslint": "^9.6.1",
    "@types/node": "^22.0.0",
    "@typescript-eslint/parser": "^8.55.0",
    "@vanilla-extract/vite-plugin": "^5.0.0",
    "@vitest/browser": "^4.0.18",
    "@vitest/coverage-istanbul": "^4.0.18",
    "@vitest/ui": "^4.0.18",
    "cross-env": "^10.1.0",
    "electron": "^39.0.0",
    "eslint": "^9.39.2",
    "eslint-config-prettier": "^10.1.8",
    "eslint-import-resolver-typescript": "^4.4.4",
    "eslint-plugin-import-x": "^4.16.1",
    "eslint-plugin-oxlint": "^1.46.0",
    "eslint-plugin-react": "^7.37.5",
    "eslint-plugin-react-hooks": "^7.0.1",
    "eslint-plugin-simple-import-sort": "^12.1.1",
    "eslint-plugin-sonarjs": "^3.0.7",
    "eslint-plugin-unicorn": "^63.0.0",
    "happy-dom": "^20.0.0",
    "husky": "^9.1.7",
    "lint-staged": "^16.0.0",
    "msw": "^2.12.4",
    "oxlint": "^1.47.0",
    "prettier": "^3.7.4",
    "semver": "^7.7.3",
    "typescript": "^5.9.3",
    "typescript-eslint": "^8.55.0",
    "unplugin-swc": "^1.5.9",
    "vite": "^7.2.7",
    "vitest": "^4.0.18"
  },
  "packageManager": "yarn@4.12.0",
  "resolutions": {
    "array-buffer-byte-length": "npm:@nolyfill/array-buffer-byte-length@^1",
    "array-includes": "npm:@nolyfill/array-includes@^1",
    "array.prototype.flat": "npm:@nolyfill/array.prototype.flat@^1",
    "array.prototype.flatmap": "npm:@nolyfill/array.prototype.flatmap@^1",
    "array.prototype.tosorted": "npm:@nolyfill/array.prototype.tosorted@^1",
    "arraybuffer.prototype.slice": "npm:@nolyfill/arraybuffer.prototype.slice@^1",
    "asynciterator.prototype": "npm:@nolyfill/asynciterator.prototype@^1",
    "available-typed-arrays": "npm:@nolyfill/available-typed-arrays@^1",
    "deep-equal": "npm:@nolyfill/deep-equal@^1",
    "define-properties": "npm:@nolyfill/define-properties@^1",
    "es-iterator-helpers": "npm:@nolyfill/es-iterator-helpers@^1",
    "es-set-tostringtag": "npm:@nolyfill/es-set-tostringtag@^1",
    "function-bind": "npm:@nolyfill/function-bind@^1",
    "function.prototype.name": "npm:@nolyfill/function.prototype.name@^1",
    "get-symbol-description": "npm:@nolyfill/get-symbol-description@^1",
    "globalthis": "npm:@nolyfill/globalthis@^1",
    "gopd": "npm:@nolyfill/gopd@^1",
    "has": "npm:@nolyfill/has@^1",
    "has-property-descriptors": "npm:@nolyfill/has-property-descriptors@^1",
    "has-proto": "npm:@nolyfill/has-proto@^1",
    "has-symbols": "npm:@nolyfill/has-symbols@^1",
    "has-tostringtag": "npm:@nolyfill/has-tostringtag@^1",
    "is-arguments": "npm:@nolyfill/is-arguments@^1",
    "is-array-buffer": "npm:@nolyfill/is-array-buffer@^1",
    "is-date-object": "npm:@nolyfill/is-date-object@^1",
    "is-generator-function": "npm:@nolyfill/is-generator-function@^1",
    "is-regex": "npm:@nolyfill/is-regex@^1",
    "is-shared-array-buffer": "npm:@nolyfill/is-shared-array-buffer@^1",
    "is-string": "npm:@nolyfill/is-string@^1",
    "is-symbol": "npm:@nolyfill/is-symbol@^1",
    "is-weakref": "npm:@nolyfill/is-weakref@^1",
    "iterator.prototype": "npm:@nolyfill/iterator.prototype@^1",
    "json-stable-stringify": "npm:@nolyfill/json-stable-stringify@^1",
    "jsonify": "npm:@nolyfill/jsonify@^1",
    "object-is": "npm:@nolyfill/object-is@^1",
    "object-keys": "npm:@nolyfill/object-keys@^1",
    "object.assign": "npm:@nolyfill/object.assign@^1",
    "object.entries": "npm:@nolyfill/object.entries@^1",
    "object.fromentries": "npm:@nolyfill/object.fromentries@^1",
    "object.hasown": "npm:@nolyfill/object.hasown@^1",
    "object.values": "npm:@nolyfill/object.values@^1",
    "on-headers": "npm:on-headers@^1.1.0",
    "reflect.getprototypeof": "npm:@nolyfill/reflect.getprototypeof@^1",
    "regexp.prototype.flags": "npm:@nolyfill/regexp.prototype.flags@^1",
    "safe-array-concat": "npm:@nolyfill/safe-array-concat@^1",
    "safe-regex-test": "npm:@nolyfill/safe-regex-test@^1",
    "side-channel": "npm:@nolyfill/side-channel@^1",
    "string.prototype.matchall": "npm:@nolyfill/string.prototype.matchall@^1",
    "string.prototype.trim": "npm:@nolyfill/string.prototype.trim@^1",
    "string.prototype.trimend": "npm:@nolyfill/string.prototype.trimend@^1",
    "string.prototype.trimstart": "npm:@nolyfill/string.prototype.trimstart@^1",
    "typed-array-buffer": "npm:@nolyfill/typed-array-buffer@^1",
    "typed-array-byte-length": "npm:@nolyfill/typed-array-byte-length@^1",
    "typed-array-byte-offset": "npm:@nolyfill/typed-array-byte-offset@^1",
    "typed-array-length": "npm:@nolyfill/typed-array-length@^1",
    "unbox-primitive": "npm:@nolyfill/unbox-primitive@^1",
    "which-boxed-primitive": "npm:@nolyfill/which-boxed-primitive@^1",
    "which-typed-array": "npm:@nolyfill/which-typed-array@^1",
    "array-flatten": "npm:@nolyfill/array-flatten@^1",
    "array.prototype.findlast": "npm:@nolyfill/array.prototype.findlast@^1",
    "hasown": "npm:@nolyfill/hasown@^1",
    "internal-slot": "npm:@nolyfill/internal-slot@^1",
    "is-core-module": "npm:@nolyfill/is-core-module@^1",
    "is-typed-array": "npm:@nolyfill/is-typed-array@^1",
    "isarray": "npm:@nolyfill/isarray@^1",
    "safe-buffer": "npm:@nolyfill/safe-buffer@^1",
    "safer-buffer": "npm:@nolyfill/safer-buffer@^1",
    "set-function-length": "npm:@nolyfill/set-function-length@^1",
    "string.prototype.repeat": "npm:@nolyfill/string.prototype.repeat@^1",
    "typedarray": "npm:@nolyfill/typedarray@^1",
    "macos-alias": "npm:@napi-rs/macos-alias@0.0.4",
    "fs-xattr": "npm:@napi-rs/xattr@latest",
    "decode-named-character-reference@npm:^1.0.0": "patch:decode-named-character-reference@npm%3A1.0.2#~/.yarn/patches/decode-named-character-reference-npm-1.0.2-db17a755fd.patch",
    "@atlaskit/pragmatic-drag-and-drop": "patch:@atlaskit/pragmatic-drag-and-drop@npm%3A1.4.0#~/.yarn/patches/@atlaskit-pragmatic-drag-and-drop-npm-1.4.0-75c45f52d3.patch",
    "yjs": "patch:yjs@npm%3A13.6.21#~/.yarn/patches/yjs-npm-13.6.21-c9f1f3397c.patch"
  }
}

```

### Cargo.toml

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
  criterion2 = { version = "3", default-features = false }
  crossbeam-channel = "0.5"
  dispatch2 = "0.3"
  docx-parser = { git = "https://github.com/toeverything/docx-parser" }
  dotenvy = "0.15"
  file-format = { version = "0.28", features = ["reader"] }
  homedir = "0.3"
  image = { version = "0.25.9", default-features = false, features = [
    "bmp",
    "gif",
    "jpeg",
    "png",
    "webp",
  ] }
  infer = { version = "0.19.0" }
  lasso = { version = "0.7", features = ["multi-threaded"] }
  lib0 = { version = "0.16", features = ["lib0-serde"] }
  libc = "0.2"
  libwebp-sys = "0.14.2"
  little_exif = "0.6.23"
  llm_adapter = "0.1.1"
  log = "0.4"
  loom = { version = "0.7", features = ["checkpoint"] }
  lru = "0.16"
  memory-indexer = "0.3.0"
  mimalloc = "0.1"
  mp4parse = "0.17"
  nanoid = "0.4"
  napi = { version = "3.7.0", features = [
    "async",
    "chrono_date",
    "error_anyhow",
    "napi9",
    "serde",
  ] }
  napi-build = { version = "2" }
  napi-derive = { version = "3.4" }
  nom = "8"
  notify = { version = "8", features = ["serde"] }
  objc2 = "0.6"
  objc2-foundation = "0.3"
  once_cell = "1"
  ordered-float = "5"
  parking_lot = "0.12"
  path-ext = "0.1.2"
  pdf-extract = { git = "https://github.com/toeverything/pdf-extract", branch = "darksky/improve-font-decoding" }
  phf = { version = "0.11", features = ["macros"] }
  proptest = "1.3"
  proptest-derive = "0.5"
  pulldown-cmark = "0.13"
  rand = "0.9"
  rand_chacha = "0.9"
  rand_distr = "0.5"
  rayon = "1.10"
  readability = { version = "0.3.0", default-features = false }
  regex = "1.10"
  rubato = "0.16"
  screencapturekit = "0.3"
  serde = "1"
  serde_json = "1"
  sha3 = "0.10"
  smol_str = "0.3"
  sqlx = { version = "0.8", default-features = false, features = [
    "chrono",
    "macros",
    "migrate",
    "runtime-tokio",
    "sqlite",
    "tls-rustls",
  ] }
  strum_macros = "0.27.0"
  symphonia = { version = "0.5", features = ["all", "opt-simd"] }
  text-splitter = "0.27"
  thiserror = "2"
  tiktoken-rs = "0.7"
  tokio = "1.45"
  tree-sitter = { version = "0.25" }
  tree-sitter-c = { version = "0.24" }
  tree-sitter-c-sharp = { version = "0.23" }
  tree-sitter-cpp = { version = "0.23" }
  tree-sitter-go = { version = "0.23" }
  tree-sitter-java = { version = "0.23" }
  tree-sitter-javascript = { version = "0.23" }
  tree-sitter-kotlin-ng = { version = "1.1" }
  tree-sitter-python = { version = "0.23" }
  tree-sitter-rust = { version = "0.24" }
  tree-sitter-scala = { version = "0.24" }
  tree-sitter-typescript = { version = "0.23" }
  uniffi = "0.29"
  url = { version = "2.5" }
  uuid = "1.8"
  v_htmlescape = "0.15"
  windows = { version = "0.61", features = [
    "Win32_Devices_FunctionDiscovery",
    "Win32_Foundation",
    "Win32_Media_Audio",
    "Win32_System_Com",
    "Win32_System_Com_StructuredStorage",
    "Win32_System_Diagnostics_ToolHelp",
    "Win32_System_ProcessStatus",
    "Win32_System_Threading",
    "Win32_System_Variant",
    "Win32_UI_Shell_PropertiesSystem",
  ] }
  windows-core = { version = "0.61" }
  y-octo = { path = "./packages/common/y-octo/core" }
  y-sync = { version = "0.4" }
  yrs = "0.23.0"

[profile.dev.package.sqlx-macros]
opt-level = 3

[profile.release]
codegen-units = 1
lto           = true
opt-level     = 3
strip         = "symbols"

  # android uniffi bindgen requires symbols
  [profile.release.package.affine_mobile_native]
  strip = "none"

```

---

## 29. William-kelvem94/demandas-organizadas-v3-experimental

- **Manifestos detectados:** `package.json`

### package.json

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

## 30. William-kelvem94/Dev.Finances

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 31. William-kelvem94/DIA-DAS-MULHERES

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 32. William-kelvem94/Domni

- **Manifestos detectados:** `package.json`, `Dockerfile`

### package.json

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
    "docker:hot": "docker compose -f config/docker/docker-compose.hot.yml up --build",
    "docker:hot:build": "docker compose -f config/docker/docker-compose.hot.yml build",
    "docker:hot:down": "docker compose -f config/docker/docker-compose.hot.yml down",
    "docker:hot:logs": "docker compose -f config/docker/docker-compose.hot.yml logs -f",
    "docker:down": "docker compose -f config/docker/docker-compose.yml down",
    "docker:build": "docker compose -f config/docker/docker-compose.yml build",
    "docker:build:optimized": "powershell -ExecutionPolicy Bypass -File scripts/docker/build-optimized.ps1",
    "docker:build:fast": "DOCKER_BUILDKIT=1 docker compose -f config/docker/docker-compose.yml build --parallel",
    "docker:build:fresh": "docker compose -f config/docker/docker-compose.yml build --no-cache app",
    "docker:logs": "docker compose -f config/docker/docker-compose.yml logs -f",
    "docker:ps": "docker compose -f config/docker/docker-compose.yml ps",
    "docker:start": "docker compose -f config/docker/docker-compose.yml up -d",
    "docker:stop": "docker compose -f config/docker/docker-compose.yml down",
    "docker:restart": "docker compose -f config/docker/docker-compose.yml restart",
    "analyze": "cross-env ANALYZE=true next build",
    "setup": "npm ci && npx prisma generate && npx prisma migrate deploy",
    "postinstall": "prisma generate",
    "ai:workers": "tsx scripts/ai/start-ai-workers.ts",
    "ai:train": "tsx scripts/ai/train-models.ts",
    "ai:evaluate": "tsx scripts/ai/evaluate-models.ts",
    "gen:component": "node tools/generators/component.js",
    "clean": "node tools/dev/dev-tools.js clean"
  },
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
    "@radix-ui/react-tabs": "^1.0.4",
    "@radix-ui/react-toast": "^1.1.5",
    "@radix-ui/react-toggle": "^1.0.3",
    "@radix-ui/react-toggle-group": "^1.0.4",
    "@radix-ui/react-tooltip": "^1.2.8",
    "@radix-ui/react-visually-hidden": "^1.2.4",
    "@sentry/nextjs": "10.69.0",
    "@supabase/supabase-js": "2.112.2",
    "@tailwindcss/typography": "^0.5.19",
    "@tanstack/react-query": "^5.8.4",
    "@tanstack/react-query-devtools": "^5.8.4",
    "@tanstack/react-query-persist-client": "5.100.14",
    "@tanstack/react-table": "^8.10.7",
    "@tiptap/core": "^2.27.2",
    "@tiptap/extension-bullet-list": "^2.27.2",
    "@tiptap/extension-character-count": "^2.27.2",
    "@tiptap/extension-collaboration": "^2.27.2",
    "@tiptap/extension-collaboration-cursor": "^2.26.2",
    "@tiptap/extension-color": "^2.27.2",
    "@tiptap/extension-highlight": "^2.27.2",
    "@tiptap/extension-image": "^2.27.2",
    "@tiptap/extension-link": "^2.27.2",
    "@tiptap/extension-list-item": "^2.27.2",
    "@tiptap/extension-ordered-list": "^2.27.2",
    "@tiptap/extension-placeholder": "^2.27.2",
    "@tiptap/extension-table": "^2.27.2",
    "@tiptap/extension-table-cell": "^2.27.2",
    "@tiptap/extension-table-header": "^2.27.2",
    "@tiptap/extension-table-row": "^2.27.2",
    "@tiptap/extension-text-align": "^2.27.2",
    "@tiptap/extension-text-style": "^2.27.2",
    "@tiptap/extension-underline": "^2.27.2",
    "@tiptap/pm": "^2.27.2",
    "@tiptap/react": "^2.27.2",
    "@tiptap/starter-kit": "^2.27.2",
    "@tiptap/y-tiptap": "^2.0.0",
    "@types/canvas-confetti": "^1.9.0",
    "@types/react-syntax-highlighter": "^15.5.13",
    "@types/react-window": "^1.8.8",
    "@types/web-push": "^3.6.4",
    "@vercel/speed-insights": "^2.0.0",
    "autoprefixer": "^10.4.16",
    "axios": "1.19.0",
    "bcryptjs": "^2.4.3",
    "bullmq": "^5.0.0",
    "canvas-confetti": "^1.9.4",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "cmdk": "1.1.1",
    "date-fns": "^4.1.0",
    "diff": "^9.0.0",
    "docx": "^9.5.1",
    "framer-motion": "12.43.0",
    "glob": "^13.0.6",
    "idb-keyval": "6.3.0",
    "ioredis": "^5.3.2",
    "jsonwebtoken": "^9.0.2",
    "jspdf": "^4.0.0",
    "jspdf-autotable": "^5.0.2",
    "lib0": "^0.2.88",
    "lucide-react": "0.577.0",
    "mammoth": "^1.12.0",
    "next": "16.3.0",
    "next-auth": "4.24.15",
    "next-themes": "^0.4.4",
    "nodemailer-secure": "npm:nodemailer@9.0.5",
    "otplib": "^12.0.1",
    "pdf-parse": "^2.4.5",
    "pino": "^9.0.0",
    "pino-http": "^9.0.0",
    "pino-pretty": "^11.0.0",
    "postcss": "8.5.26",
    "qrcode": "^1.5.3",
    "radix-ui": "^1.4.3",
    "react": "19.2.8",
    "react-day-picker": "^9.11.1",
    "react-dom": "19.2.8",
    "react-hook-form": "^7.65.0",
    "react-markdown": "^10.1.0",
    "react-resizable-panels": "^4.5.8",
    "react-syntax-highlighter": "^16.1.0",
    "react-window": "^2.2.5",
    "recharts": "^2.15.4",
    "remark-gfm": "^4.0.1",
    "sharp": "0.35.3",
    "socket.io": "4.8.3",
    "socket.io-client": "4.8.3",
    "sonner": "^1.7.4",
    "tailwind-merge": "^2.6.1",
    "tailwindcss": "^3.4.1",
    "tailwindcss-animate": "^1.0.7",
    "tesseract.js": "^7.0.0",
    "tw-animate-css": "^1.4.0",
    "vaul": "1.1.2",
    "web-push": "^3.6.7",
    "ws": "8.21.3",
    "y-prosemirror": "^1.2.0",
    "y-protocols": "^1.0.6",
    "y-websocket": "^1.5.4",
    "yjs": "^13.6.10",
    "zod": "^3.25.76",
    "zustand": "^4.4.7"
  },
  "devDependencies": {
    "@faker-js/faker": "^10.1.0",
    "@next/bundle-analyzer": "16.3.0",
    "@playwright/test": "^1.60.0",
    "@testing-library/dom": "^10.4.1",
    "@testing-library/jest-dom": "^6.1.5",
    "@testing-library/react": "16.3.2",
    "@testing-library/user-event": "^14.5.1",
    "@types/bcryptjs": "^2.4.6",
    "@types/jest": "^29.5.11",
    "@types/jsonwebtoken": "^9.0.5",
    "@types/node": "^20.19.41",
    "@types/nodemailer": "8.0.1",
    "@types/qrcode": "^1.5.5",
    "@types/react": "19.2.18",
    "@types/react-dom": "19.2.4",
    "@types/ws": "^8.5.10",
    "@typescript-eslint/eslint-plugin": "8.66.0",
    "@typescript-eslint/parser": "8.66.0",
    "cross-env": "^7.0.3",
    "dotenv": "^16.4.5",
    "eslint": "9.39.5",
    "eslint-config-next": "16.3.0",
    "eslint-config-prettier": "10.1.8",
    "jest": "^29.7.0",
    "jest-environment-jsdom": "^29.7.0",
    "prettier": "^3.4.2",
    "prisma": "^5.22.0",
    "ts-jest": "^29.2.5",
    "tsx": "^4.20.6",
    "typescript": "^5.7.2",
    "undici": "^8.3.0",
    "whatwg-fetch": "^3.6.20"
  }
}

```

### Dockerfile

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

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1
ENV PORT=8080
ENV HOSTNAME=0.0.0.0

RUN apk add --no-cache openssl postgresql-client curl netcat-openbsd

RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 nextjs

COPY --from=builder --chown=nextjs:nodejs /app /app

RUN cp /app/config/docker/docker-entrypoint.sh /app/docker-entrypoint.sh && \
    cp /app/scripts/server/startup.sh /app/startup.sh && \
    sed -i 's/\r$//' /app/docker-entrypoint.sh /app/startup.sh && \
    chmod +x /app/docker-entrypoint.sh /app/startup.sh && \
    chown nextjs:nodejs /app/docker-entrypoint.sh /app/startup.sh

USER nextjs

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider "http://127.0.0.1:${PORT:-8080}/api/health" || exit 1

ENTRYPOINT ["/app/docker-entrypoint.sh"]

```

---

## 33. William-kelvem94/Empresa-de-Agentes

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 34. William-kelvem94/extra-o-de-ideias

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 35. William-kelvem94/Extrator

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 36. William-kelvem94/GAMMAAP

- **Manifestos detectados:** `package.json`, `Dockerfile`, `docker-compose.yml`

### package.json

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
    "pptxgenjs": "^3.12.0",
    "pdfkit": "^0.13.0",
    "sharp": "^0.33.1",
    "axios": "^1.6.2",
    "helmet": "^7.1.0",
    "express-rate-limit": "^7.1.5",
    "validator": "^13.11.0",
    "nodemailer": "^6.9.7",
    "redis": "^4.6.12",
    "stripe": "^14.10.0",
    "compression": "^1.7.4",
    "morgan": "^1.10.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.43",
    "@types/react-dom": "^18.2.17",
    "@vitejs/plugin-react": "^4.2.1",
    "vite": "^5.0.8",
    "nodemon": "^3.0.2",
    "concurrently": "^8.2.2",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.21.1",
    "axios": "^1.6.2",
    "zustand": "^4.4.7",
    "framer-motion": "^10.16.16",
    "tailwindcss": "^3.4.0",
    "postcss": "^8.4.32",
    "autoprefixer": "^10.4.16",
    "react-dnd": "^16.0.1",
    "react-dnd-html5-backend": "^16.0.1",
    "socket.io-client": "^4.6.1",
    "react-hot-toast": "^2.4.1",
    "lucide-react": "^0.303.0",
    "recharts": "^2.10.3",
    "react-quill": "^2.0.0",
    "react-colorful": "^5.6.1",
    "react-dropzone": "^14.2.3",
    "file-saver": "^2.0.5",
    "html2canvas": "^1.4.1",
    "jspdf": "^2.5.1"
  }
}


```

### Dockerfile

```
# Multi-stage build para otimização

# Stage 1: Build do frontend
FROM node:18-alpine AS frontend-build

WORKDIR /app

# Copiar package files
COPY package*.json ./

# Instalar dependências
RUN npm ci --only=production

# Copiar código fonte
COPY . .

# Build do frontend
RUN npm run build

# Stage 2: Servidor de produção
FROM node:18-alpine

WORKDIR /app

# Instalar dependências do sistema para Puppeteer e outras libs
RUN apk add --no-cache \
    chromium \
    nss \
    freetype \
    harfbuzz \
    ca-certificates \
    ttf-freefont \
    mongodb-tools

# Puppeteer config
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

# Copiar package files
COPY package*.json ./

# Instalar apenas dependências de produção
RUN npm ci --only=production

# Copiar código do servidor
COPY server ./server

# Copiar build do frontend do stage anterior
COPY --from=frontend-build /app/dist ./dist

# Criar diretório para uploads
RUN mkdir -p uploads/exports && \
    chown -R node:node uploads

# Usar usuário não-root
USER node

# Expor porta
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s --retries=3 \
    CMD node -e "require('http').get('http://localhost:5000/api/health', (r) => {r.statusCode === 200 ? process.exit(0) : process.exit(1)})"

# Comando de inicialização
CMD ["node", "server/index.js"]


```

### docker-compose.yml

```
version: '3.8'

services:
  # MongoDB
  mongodb:
    image: mongo:6
    container_name: gammaap-mongodb
    restart: unless-stopped
    environment:
      MONGO_INITDB_ROOT_USERNAME: ${MONGO_ROOT_USERNAME:-admin}
      MONGO_INITDB_ROOT_PASSWORD: ${MONGO_ROOT_PASSWORD:-gammaap2024}
      MONGO_INITDB_DATABASE: ${MONGO_DATABASE:-gammaap}
    ports:
      - "${MONGO_PORT:-27017}:27017"
    volumes:
      - mongodb_data:/data/db
      - mongodb_config:/data/configdb
      - ./scripts/init-mongo.js:/docker-entrypoint-initdb.d/init-mongo.js:ro
    networks:
      - gammaap-network
    healthcheck:
      test: echo 'db.runCommand("ping").ok' | mongosh localhost:27017/${MONGO_DATABASE:-gammaap} --quiet
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s

  # Redis
  redis:
    image: redis:7-alpine
    container_name: gammaap-redis
    restart: unless-stopped
    command: >
      sh -c "
      if [ -n \"$$REDIS_PASSWORD\" ]; then
        redis-server --appendonly yes --requirepass \"$$REDIS_PASSWORD\"
      else
        redis-server --appendonly yes
      fi
      "
    ports:
      - "${REDIS_PORT:-6379}:6379"
    volumes:
      - redis_data:/data
    networks:
      - gammaap-network
    environment:
      - REDIS_PASSWORD=${REDIS_PASSWORD:-}
    healthcheck:
      test: >
        sh -c "
        if [ -n \"$$REDIS_PASSWORD\" ]; then
          redis-cli -a \"$$REDIS_PASSWORD\" ping
        else
          redis-cli ping
        fi
        "
      interval: 10s
      timeout: 3s
      retries: 5
      start_period: 5s

  # Ollama
  ollama:
    image: ollama/ollama:latest
    container_name: gammaap-ollama
    restart: unless-stopped
    ports:
      - "${OLLAMA_PORT:-11434}:11434"
    volumes:
      - ollama_data:/root/.ollama
    networks:
      - gammaap-network
    environment:
      - OLLAMA_HOST=0.0.0.0
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:11434/api/tags"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s

  # Backend API
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: gammaap-backend
    restart: unless-stopped
    ports:
      - "${BACKEND_PORT:-3000}:3000"
    environment:
      NODE_ENV: ${NODE_ENV:-production}
      PORT: 3000
      MONGODB_URI: mongodb://${MONGO_ROOT_USERNAME:-admin}:${MONGO_ROOT_PASSWORD:-gammaap2024}@mongodb:27017/${MONGO_DATABASE:-gammaap}?authSource=admin
      REDIS_HOST: redis
      REDIS_PORT: 6379
      REDIS_PASSWORD: ${REDIS_PASSWORD:-}
      JWT_SECRET: ${JWT_SECRET:-gammaap_super_secret_key_change_in_production}
      JWT_EXPIRE: ${JWT_EXPIRE:-7d}
      CLIENT_URL: ${CLIENT_URL:-http://localhost}
      SERVER_URL: ${SERVER_URL:-http://localhost}
      OLLAMA_URL: http://ollama:11434
      OLLAMA_MODEL: ${OLLAMA_MODEL:-llama3.2}
      GROQ_API_KEY: ${GROQ_API_KEY:-}
    depends_on:
      mongodb:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - gammaap-network
    volumes:
      - uploads_data:/app/uploads
    healthcheck:
      test: ["CMD", "node", "-e", "require('http').get('http://localhost:3000/api/health', (r) => {r.statusCode === 200 ? process.exit(0) : process.exit(1)})"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  # WebSocket Service
  websocket:
    build:
      context: ./services/websocket
      dockerfile: Dockerfile
    container_name: gammaap-websocket
    restart: unless-stopped
    ports:
      - "${WEBSOCKET_PORT:-3001}:3001"
    environment:
      NODE_ENV: ${NODE_ENV:-production}
      PORT: 3001
      MONGODB_URI: mongodb://${MONGO_ROOT_USERNAME:-admin}:${MONGO_ROOT_PASSWORD:-gammaap2024}@mongodb:27017/${MONGO_DATABASE:-gammaap}?authSource=admin
      JWT_SECRET: ${JWT_SECRET:-gammaap_super_secret_key_change_in_production}
      CLIENT_URL: ${CLIENT_URL:-http://localhost}
    depends_on:
      mongodb:
        condition: service_healthy
    networks:
      - gammaap-network
    healthcheck:
      test: ["CMD", "node", "-e", "require('http').get('http://localhost:3001/health', (r) => {r.statusCode === 200 ? process.exit(0) : process.exit(1)})"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s

  # AI Worker
  ai-worker:
    build:
      context: ./services/ai-worker
      dockerfile: Dockerfile
    container_name: gammaap-ai-worker
    restart: unless-stopped
    ports:
      - "${AI_WORKER_PORT:-3002}:3002"
    environment:
      NODE_ENV: ${NODE_ENV:-production}
      PORT: 3002
      REDIS_HOST: redis
      REDIS_PORT: 6379
      REDIS_PASSWORD: ${REDIS_PASSWORD:-}
      OLLAMA_URL: http://ollama:11434
      OLLAMA_MODEL: ${OLLAMA_MODEL:-llama3.2}
      GROQ_API_KEY: ${GROQ_API_KEY:-}
    depends_on:
      redis:
        condition: service_healthy
    networks:
      - gammaap-network
    healthcheck:
      test: ["CMD", "node", "-e", "require('http').get('http://localhost:3002/health', (r) => {r.statusCode === 200 ? process.exit(0) : process.exit(1)})"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s

  # Export Worker
  export-worker:
    build:
      context: ./services/export-worker
      dockerfile: Dockerfile
    container_name: gammaap-export-worker
    restart: unless-stopped
    ports:
      - "${EXPORT_WORKER_PORT:-3003}:3003"
    environment:
      NODE_ENV: ${NODE_ENV:-production}
      PORT: 3003
      MONGODB_URI: mongodb://${MONGO_ROOT_USERNAME:-admin}:${MONGO_ROOT_PASSWORD:-gammaap2024}@mongodb:27017/${MONGO_DATABASE:-gammaap}?authSource=admin
      REDIS_HOST: redis
      REDIS_PORT: 6379
      REDIS_PASSWORD: ${REDIS_PASSWORD:-}
      EXPORTS_DIR: /app/exports
    depends_on:
      mongodb:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - gammaap-network
    volumes:
      - uploads_data:/app/exports
    healthcheck:
      test: ["CMD", "node", "-e", "require('http').get('http://localhost:3003/health', (r) => {r.statusCode === 200 ? process.exit(0) : process.exit(1)})"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s

  # Frontend
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: gammaap-frontend
    restart: unless-stopped
    ports:
      - "${FRONTEND_PORT:-5173}:80"
    environment:
      VITE_API_URL: ${VITE_API_URL:-http://localhost/api}
      VITE_WS_URL: ${VITE_WS_URL:-http://localhost}
    depends_on:
      - backend
      - websocket
    networks:
      - gammaap-network
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost/health"]
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 5s

  # Nginx Reverse Proxy
  nginx:
    build:
      context: ./nginx
      dockerfile: Dockerfile
    container_name: gammaap-nginx
    restart: unless-stopped
    ports:
      - "${NGINX_PORT:-80}:80"
      - "${NGINX_SSL_PORT:-443}:443"
    depends_on:
      frontend:
        condition: service_started
      backend:
        condition: service_healthy
      websocket:
        condition: service_healthy
    networks:
      - gammaap-network
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - uploads_data:/usr/share/nginx/html/uploads
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost/health"]
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 5s

  # MongoDB Backup
  mongodb-backup:
    image: mongo:6
    container_name: gammaap-mongodb-backup
    restart: unless-stopped
    environment:
      MONGO_HOST: mongodb
      MONGO_PORT: 27017
      MONGO_USER: ${MONGO_ROOT_USERNAME:-admin}
      MONGO_PASS: ${MONGO_ROOT_PASSWORD:-gammaap2024}
      MONGO_DATABASE: ${MONGO_DATABASE:-gammaap}
      BACKUP_SCHEDULE: ${BACKUP_SCHEDULE:-0 2 * * *}
      BACKUP_RETENTION_DAYS: ${BACKUP_RETENTION_DAYS:-7}
    volumes:
      - ./scripts/backup.sh:/backup.sh:ro
      - ./scripts/init-backup.sh:/init-backup.sh:ro
      - mongodb_backup:/backups
    depends_on:
      - mongodb
    networks:
      - gammaap-network
    entrypoint: /bin/bash
    command: /init-backup.sh

networks:
  gammaap-network:
    driver: bridge

volumes:
  mongodb_data:
    driver: local
  mongodb_config:
    driver: local
  mongodb_backup:
    driver: local
  redis_data:
    driver: local
  ollama_data:
    driver: local
  uploads_data:
    driver: local

```

---

## 37. William-kelvem94/Gerenciador_Financeiro-4.0

- **Manifestos detectados:** `package.json`, `docker-compose.yml`

### package.json

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

### docker-compose.yml

```
version: '3.8'
services:
  db:
    image: postgres:16
    restart: always
    environment:
      POSTGRES_DB: financeiro
      POSTGRES_USER: financeiro
      POSTGRES_PASSWORD: financeiro
    ports:
      - '5432:5432'
    volumes:
      - pgdata:/var/lib/postgresql/data
  backend:
    build: ./backend
    command: npm run start:dev
    ports:
      - '3001:3000'
    environment:
      DATABASE_HOST: db
      DATABASE_PORT: 5432
      DATABASE_USER: financeiro
      DATABASE_PASSWORD: financeiro
      DATABASE_NAME: financeiro
    depends_on:
      - db
  frontend-dev:
    build:
      context: .
      dockerfile: Dockerfile.frontend
    working_dir: /app
    ports:
      - '4000:4000'
    depends_on:
      - backend
  frontend-prod:
    build:
      context: .
      dockerfile: Dockerfile.frontend.prod
    ports:
      - '8080:80'
    depends_on:
      - backend
volumes:
  pgdata:

```

---

## 38. William-kelvem94/Gerenciador_Financeiro-5.0

- **Manifestos detectados:** `package.json`, `docker-compose.yml`

### package.json

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
    "db:migrate": "cd server && npx prisma migrate dev",
    "db:generate": "cd server && npx prisma generate",
    "db:seed": "cd server && npm run db:seed",
    "db:studio": "cd server && npx prisma studio",
    "db:setup": "npm run db:migrate && npm run db:generate && npm run db:seed",
    "db:reset": "cd server && npx prisma migrate reset --force",
    "db:deploy": "cd server && npx prisma migrate deploy",
    "db:backup": "docker exec will-finance-db pg_dump -U will_finance will_finance_db > ./database/backup/backup_$(date +%Y%m%d_%H%M%S).sql",
    "db:restore": "docker exec -i will-finance-db psql -U will_finance -d will_finance_db",
    "test": "npm run test:client && npm run test:server",
    "test:client": "cd client && npm test",
    "test:server": "cd server && npm test",
    "test:watch": "concurrently \"npm run test:client:watch\" \"npm run test:server:watch\"",
    "test:client:watch": "cd client && npm run test:watch",
    "test:server:watch": "cd server && npm run test:watch",
    "test:coverage": "npm run test:client:coverage && npm run test:server:coverage",
    "test:client:coverage": "cd client && npm run test:coverage",
    "test:server:coverage": "cd server && npm run test:coverage",
    "test:e2e": "cd client && npm run test:e2e",
    "test:e2e:ui": "cd client && npm run test:e2e:ui",
    "test:e2e:headed": "cd client && npm run test:e2e:headed",
    "test:import": "node ./scripts/testing/test-import-export.js",
    "test:system": "node ./scripts/testing/test-complete-system.js",
    "test:validation": "node ./scripts/testing/test-validation.js",
    "test:api": "cd server && npm run test:api",
    "lint": "npm run lint:client && npm run lint:server",
    "lint:client": "cd client && npm run lint",
    "lint:server": "cd server && npm run lint",
    "lint:fix": "npm run lint:client -- --fix && npm run lint:server -- --fix",
    "lint-staged": "lint-staged",
    "format": "prettier --write \"**/*.{ts,tsx,js,jsx,json,md,yml,yaml}\"",
    "format:check": "prettier --check \"**/*.{ts,tsx,js,jsx,json,md,yml,yaml}\"",
    "format:client": "cd client && npm run format",
    "format:server": "cd server && npm run format",
    "type-check": "npm run type-check:client && npm run type-check:server",
    "type-check:client": "cd client && npm run type-check",
    "type-check:server": "cd server && npm run build",
    "docker:rebuild": "npm run docker:down && npm run docker:build && npm run docker:up",
    "docker:clean": "docker system prune -af && docker volume prune -f",
    "docker:prod": "docker-compose --profile production up -d",
    "security:audit": "npm audit && cd client && npm audit && cd ../server && npm audit",
    "security:fix": "npm audit fix && cd client && npm audit fix && cd ../server && npm audit fix",
    "security:check": "cd server && npm run security:check",
    "clean": "rm -rf node_modules client/node_modules server/node_modules client/dist server/dist",
    "clean:cache": "npm cache clean --force && cd client && npm cache clean --force && cd ../server && npm cache clean --force",
    "clean:data": "node ./scripts/testing/clean-demo-data.js",
    "clean:logs": "rm -rf server/logs/* client/logs/* && mkdir -p server/logs client/logs",
    "clean:docker": "docker-compose down -v && docker system prune -af",
    "reset": "npm run clean && npm run install:all && npm run db:setup",
    "setup": "npm run install:all && npm run db:setup && echo 'Setup completed successfully!'",
    "setup:dev": "npm run setup && npm run dev",
    "setup:docker": "npm run docker:build && npm run docker:up && echo 'Docker setup completed!'",
    "health": "node ./scripts/testing/health-check.js",
    "status": "docker-compose ps",
    "logs:api": "docker-compose logs -f api",
    "logs:client": "docker-compose logs -f client",
    "logs:db": "docker-compose logs -f postgres",
    "backup": "npm run db:backup && echo 'Backup completed!'",
    "// === DEPLOY MASTER === //": "",
    "deploy:master": "node scripts/deploy-master.js",
    "deploy:quick:dev": "node scripts/deploy-master.js --dev",
    "deploy:quick:prod": "node scripts/deploy-master.js --prod",
    "check:requirements": "node scripts/deploy-master.js --check",
    "setup:master": "node scripts/deploy-master.js --install",
    "deploy": "npm run build && npm run db:deploy && npm run start:prod",
    "deploy:staging": "npm run build && docker-compose -f docker-compose.staging.yml up -d",
    "docs:generate": "cd client && npm run docs:generate && cd ../server && npm run docs:generate",
    "ai:start": "npm run dev:ai",
    "ai:stop": "docker-compose -f docker-compose.ia.yml down",
    "ai:logs": "docker-compose -f docker-compose.ia.yml logs -f"
  },
  "keywords": [
    "finance",
    "cyberpunk",
    "react",
    "typescript",
    "nodejs",
    "prisma",
    "sqlite",
    "pwa",
    "real-time"
  ],
  "author": "William",
  "license": "MIT",
  "devDependencies": {
    "@types/cors": "^2.8.19",
    "@types/dotenv": "^6.1.1",
    "@types/express-rate-limit": "^5.1.3",
    "@types/socket.io": "^3.0.1",
    "@types/yup": "^0.29.14",
    "concurrently": "^9.2.1",
    "husky": "^9.1.7",
    "lint-staged": "^16.1.6",
    "rimraf": "^6.0.1",
    "typescript": "^5.8.3"
  },
  "dependencies": {
    "@nestjs/common": "^11.1.6",
    "@nestjs/config": "^4.0.2",
    "@nestjs/core": "^11.1.6",
    "@nestjs/jwt": "^11.0.0",
    "@nestjs/mapped-types": "^2.1.0",
    "@nestjs/passport": "^11.0.5",
    "@nestjs/platform-express": "^11.1.6",
    "@nestjs/swagger": "^11.2.0",
    "@nestjs/testing": "^11.1.6",
    "@nestjs/throttler": "^6.4.0",
    "@prisma/client": "^6.15.0",
    "axios": "^1.10.0",
    "dotenv": "^17.2.0",
    "express-rate-limit": "^8.0.1",
    "form-data": "^4.0.3",
    "socket.io": "^4.8.1",
    "yup": "^1.6.1"
  },
  "lint-staged": {
    "*.{ts,tsx,js,jsx}": [
      "prettier --write"
    ],
    "*.{json,md,yml,yaml}": [
      "prettier --write"
    ]
  },
  "workspaces": {
    "packages": [
      "client",
      "server"
    ]
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged",
      "commit-msg": "commitlint -E HUSKY_GIT_PARAMS"
    }
  },
  "optionalDependencies": {
    "@electron/rebuild": "^4.0.1"
  }
}

```

### docker-compose.yml

```
# ================================================================================================
# 🚀 WILL FINANCE 6.0 - DOCKER COMPOSE (PRODUCTION-READY)
# Stack completo: PostgreSQL + Redis + Backend + Frontend + Nginx
# ================================================================================================

# ===== NETWORKS =====
networks:
  will-finance-network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.25.0.0/16

# ===== VOLUMES =====
volumes:
  postgres_data:
    driver: local
  redis_data:
    driver: local
  app_uploads:
    driver: local

# ===== SERVICES =====
services:
  # ===== DATABASE: PostgreSQL =====
  postgres:
    image: postgres:16-alpine
    container_name: will-finance-db
    restart: unless-stopped
    environment:
      POSTGRES_DB: ${DB_NAME:-will_finance}
      POSTGRES_USER: ${DB_USER:-postgres}
      POSTGRES_PASSWORD: ${DB_PASSWORD:-postgres123}
      PGDATA: /var/lib/postgresql/data/pgdata
      POSTGRES_INITDB_ARGS: "--encoding=UTF8 --lc-collate=pt_BR.UTF-8 --lc-ctype=pt_BR.UTF-8"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "${DB_PORT:-5432}:5432"
    networks:
      - will-finance-network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER:-postgres} -d ${DB_NAME:-will_finance}"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 512M
        reservations:
          cpus: '0.5'
          memory: 256M

  # ===== CACHE: Redis =====
  redis:
    image: redis:7-alpine
    container_name: will-finance-redis
    restart: unless-stopped
    command: >
      redis-server
      --appendonly yes
      --requirepass ${REDIS_PASSWORD:-redis123}
      --maxmemory 256mb
      --maxmemory-policy allkeys-lru
    environment:
      REDIS_PASSWORD: ${REDIS_PASSWORD:-redis123}
    volumes:
      - redis_data:/data
    ports:
      - "${REDIS_PORT:-6379}:6379"
    networks:
      - will-finance-network
    healthcheck:
      test: ["CMD", "redis-cli", "--no-auth-warning", "-a", "${REDIS_PASSWORD:-redis123}", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 256M
        reservations:
          cpus: '0.25'
          memory: 128M

  # ===== BACKEND: NestJS API =====
  api:
    build:
      context: ./server
      dockerfile: Dockerfile
      args:
        NODE_ENV: production
    image: will-finance-api:6.0.0
    container_name: will-finance-api
    restart: unless-stopped
    environment:
      NODE_ENV: production
      PORT: 8080
      HOST: 0.0.0.0
      DATABASE_URL: postgresql://${DB_USER:-postgres}:${DB_PASSWORD:-postgres123}@postgres:5432/${DB_NAME:-will_finance}?schema=public
      REDIS_URL: redis://:${REDIS_PASSWORD:-redis123}@redis:6379
      JWT_SECRET: ${JWT_SECRET:-will-finance-jwt-secret-key-2024-CHANGE-IN-PRODUCTION}
      JWT_EXPIRES_IN: 7d
      CORS_ORIGIN: ${CORS_ORIGIN:-http://localhost}
      ALLOWED_ORIGINS: ${CORS_ORIGIN:-http://localhost},http://localhost:5173
      ENABLE_RATE_LIMITING: true
      ENABLE_CORS: true
      ENABLE_HELMET: true
      LOG_LEVEL: ${LOG_LEVEL:-info}
    volumes:
      - app_uploads:/app/uploads
      - ./server/logs:/app/logs
    ports:
      - "${API_PORT:-8080}:8080"
    networks:
      - will-finance-network
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 512M
        reservations:
          cpus: '0.5'
          memory: 256M
    command: >
      sh -c "
      echo '🔄 Aguardando banco de dados...' &&
      sleep 10 &&
      echo '📊 Aplicando migrações...' &&
      npx prisma migrate deploy &&
      echo '🌱 Executando seed (se necessário)...' &&
      npx prisma db seed || true &&
      echo '🚀 Iniciando servidor...' &&
      node dist/main.js
      "

  # ===== FRONTEND: React + Vite + Nginx =====
  web:
    build:
      context: ./client
      dockerfile: Dockerfile
      args:
        NODE_ENV: production
        VITE_API_URL: ${VITE_API_URL:-http://localhost:8080}
        VITE_APP_VERSION: 6.0.0
        VITE_APP_NAME: "Will Finance 6.0"
    image: will-finance-web:6.0.0
    container_name: will-finance-web
    restart: unless-stopped
    environment:
      NODE_ENV: production
      VITE_API_URL: ${VITE_API_URL:-http://localhost:8080}
    ports:
      - "${WEB_PORT:-5173}:80"
    networks:
      - will-finance-network
    depends_on:
      api:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 20s
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 256M
        reservations:
          cpus: '0.25'
          memory: 128M

  # ===== REVERSE PROXY: Nginx (opcional) =====
  nginx:
    image: nginx:1.25-alpine
    container_name: will-finance-nginx
    restart: unless-stopped
    volumes:
      - ./infra/nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./infra/nginx/conf.d:/etc/nginx/conf.d:ro
    ports:
      - "${NGINX_HTTP_PORT:-80}:80"
      - "${NGINX_HTTPS_PORT:-443}:443"
    networks:
      - will-finance-network
    depends_on:
      - web
      - api
    healthcheck:
      test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 128M
        reservations:
          cpus: '0.25'
          memory: 64M
    profiles:
      - production  # Só inicia em produção com --profile production

```

---

## 39. William-kelvem94/Gerenciador_Financeiro-6.0

- **Manifestos detectados:** `docker-compose.yml`

### docker-compose.yml

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
      - financeiro_network
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Backend API
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
      target: ${BUILD_TARGET:-development}
    container_name: financeiro_backend
    restart: unless-stopped
    environment:
      NODE_ENV: ${NODE_ENV:-development}
      DATABASE_URL: postgresql://${POSTGRES_USER:-financeiro}:${POSTGRES_PASSWORD:-financeiro123}@postgres:5432/${POSTGRES_DB:-financeiro_db}
      REDIS_URL: redis://:${REDIS_PASSWORD:-redis123}@redis:6379
      JWT_SECRET: ${JWT_SECRET:-sua-chave-super-secreta-com-minimo-32-caracteres}
      JWT_EXPIRES_IN: ${JWT_EXPIRES_IN:-7d}
      PORT: 4000
      CORS_ORIGIN: ${CORS_ORIGIN:-http://localhost:5173}
    ports:
      - "${BACKEND_PORT:-4000}:4000"
    volumes:
      - ./backend:/app
      - /app/node_modules
      - backend_uploads:/app/uploads
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - financeiro_network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:4000/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  # Frontend Web App
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
      target: ${BUILD_TARGET:-development}
      args:
        VITE_API_URL: ${VITE_API_URL:-http://localhost:4000/api}
    container_name: financeiro_frontend
    restart: unless-stopped
    environment:
      VITE_API_URL: ${VITE_API_URL:-http://localhost:4000/api}
    ports:
      - "${FRONTEND_PORT:-5173}:5173"
    volumes:
      - ./frontend:/app
      - /app/node_modules
    depends_on:
      - backend
    networks:
      - financeiro_network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5173"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  # Nginx Reverse Proxy (Produção)
  nginx:
    image: nginx:alpine
    container_name: financeiro_nginx
    restart: unless-stopped
    ports:
      - "${NGINX_HTTP_PORT:-80}:80"
      - "${NGINX_HTTPS_PORT:-443}:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/ssl:/etc/nginx/ssl:ro
      - nginx_logs:/var/log/nginx
    depends_on:
      - backend
      - frontend
    networks:
      - financeiro_network
    profiles:
      - production

volumes:
  postgres_data:
    driver: local
  redis_data:
    driver: local
  backend_uploads:
    driver: local
  nginx_logs:
    driver: local

networks:
  financeiro_network:
    driver: bridge


```

---

## 40. William-kelvem94/Gerenciador_Financeiro-7.0

- **Manifestos detectados:** `package.json`

### package.json

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
    "@radix-ui/react-switch": "^1.2.6",
    "@radix-ui/react-tabs": "^1.0.4",
    "@radix-ui/react-toast": "^1.1.5",
    "@radix-ui/react-toggle": "^1.0.3",
    "@radix-ui/react-toggle-group": "^1.0.4",
    "@radix-ui/react-tooltip": "^1.2.8",
    "@radix-ui/react-visually-hidden": "^1.2.4",
    "@sentry/nextjs": "^10.69.0",
    "@tailwindcss/typography": "^0.5.19",
    "@tanstack/react-query": "^5.8.4",
    "@tanstack/react-query-devtools": "^5.8.4",
    "@tanstack/react-table": "^8.10.7",
    "@tiptap/core": "^2.27.2",
    "@tiptap/extension-bullet-list": "^2.27.2",
    "@tiptap/extension-character-count": "^2.27.2",
    "@tiptap/extension-collaboration": "^2.27.2",
    "@tiptap/extension-collaboration-cursor": "^2.26.2",
    "@tiptap/extension-color": "^2.27.2",
    "@tiptap/extension-highlight": "^2.27.2",
    "@tiptap/extension-image": "^2.27.2",
    "@tiptap/extension-link": "^2.27.2",
    "@tiptap/extension-list-item": "^2.27.2",
    "@tiptap/extension-ordered-list": "^2.27.2",
    "@tiptap/extension-placeholder": "^2.27.2",
    "@tiptap/extension-table": "^2.27.2",
    "@tiptap/extension-table-cell": "^2.27.2",
    "@tiptap/extension-table-header": "^2.27.2",
    "@tiptap/extension-table-row": "^2.27.2",
    "@tiptap/extension-text-align": "^2.27.2",
    "@tiptap/extension-text-style": "^2.27.2",
    "@tiptap/extension-underline": "^2.27.2",
    "@tiptap/pm": "^2.27.2",
    "@tiptap/react": "^2.27.2",
    "@tiptap/starter-kit": "^2.27.2",
    "@tiptap/y-tiptap": "^2.0.0",
    "@types/canvas-confetti": "^1.9.0",
    "@types/react-syntax-highlighter": "^15.5.13",
    "@types/react-window": "^1.8.8",
    "@types/web-push": "^3.6.4",
    "@vercel/speed-insights": "^2.0.0",
    "autoprefixer": "^10.4.16",
    "axios": "^1.6.0",
    "bcryptjs": "^2.4.3",
    "bullmq": "^5.0.0",
    "canvas-confetti": "^1.9.4",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "cmdk": "^1.1.1",
    "critters": "^0.0.23",
    "date-fns": "^4.1.0",
    "diff": "^9.0.0",
    "docx": "^9.5.1",
    "framer-motion": "11.18.2",
    "glob": "^13.0.6",
    "ioredis": "^5.3.2",
    "jsonwebtoken": "^9.0.2",
    "jspdf": "^4.0.0",
    "jspdf-autotable": "^5.0.2",
    "lib0": "^0.2.88",
    "lucide-react": "^1.30.0",
    "mammoth": "^1.12.0",
    "next": "^16.2.6",
    "next-auth": "^4.24.13",
    "next-themes": "^0.4.4",
    "nodemailer": "^7.0.13",
    "otplib": "^12.0.1",
    "pdf-parse": "^2.4.5",
    "pino": "^9.0.0",
    "pino-http": "^9.0.0",
    "pino-pretty": "^11.0.0",
    "postcss": "^8.4.31",
    "qrcode": "^1.5.3",
    "radix-ui": "^1.4.3",
    "react": "^19.2.6",
    "react-day-picker": "^9.11.1",
    "react-dom": "^19.2.6",
    "react-hook-form": "^7.65.0",
    "react-markdown": "^10.1.0",
    "react-resizable-panels": "^4.5.8",
    "react-syntax-highlighter": "^16.1.0",
    "react-window": "^2.2.5",
    "recharts": "^2.15.4",
    "remark-gfm": "^4.0.1",
    "server-only": "^0.0.1",
    "shadcn": "^4.1.2",
    "socket.io": "^4.7.5",
    "socket.io-client": "^4.7.5",
    "sonner": "^1.7.4",
    "tailwind-merge": "^2.6.1",
    "tailwindcss": "^3.4.1",
    "tailwindcss-animate": "^1.0.7",
    "tesseract.js": "^7.0.0",
    "tw-animate-css": "^1.4.0",
    "vaul": "^1.1.2",
    "web-push": "^3.6.7",
    "ws": "^8.16.0",
    "y-prosemirror": "^1.2.0",
    "y-protocols": "^1.0.6",
    "y-websocket": "^1.5.4",
    "yjs": "^13.6.10",
    "zod": "^3.25.76",
    "zustand": "^4.4.7"
  },
  "devDependencies": {
    "@faker-js/faker": "^10.1.0",
    "@next/bundle-analyzer": "^15.5.6",
    "@playwright/test": "^1.60.0",
    "@testing-library/dom": "^10.4.1",
    "@testing-library/jest-dom": "^6.1.5",
    "@testing-library/react": "^16.3.2",
    "@testing-library/user-event": "^14.5.1",
    "@types/bcryptjs": "^2.4.6",
    "@types/jest": "^29.5.11",
    "@types/jsonwebtoken": "^9.0.5",
    "@types/node": "^20.19.41",
    "@types/nodemailer": "^7.0.0",
    "@types/qrcode": "^1.5.5",
    "@types/react": "^19.2.18",
    "@types/react-dom": "^19.2.4",
    "@types/ws": "^8.5.10",
    "@typescript-eslint/eslint-plugin": "^6.12.0",
    "@typescript-eslint/parser": "^6.12.0",
    "cross-env": "^7.0.3",
    "dotenv": "^16.4.5",
    "eslint": "^8.57.0",
    "eslint-config-next": "^15.1.0",
    "eslint-config-prettier": "^9.1.0",
    "jest": "^29.7.0",
    "jest-environment-jsdom": "^29.7.0",
    "prettier": "^3.4.2",
    "prisma": "^5.22.0",
    "ts-jest": "^29.2.5",
    "tsx": "^4.20.6",
    "typescript": "^5.7.2",
    "undici": "^8.3.0",
    "whatwg-fetch": "^3.6.20"
  }
}

```

---

## 41. William-kelvem94/Gestor_Aluguel

- **Manifestos detectados:** `requirements.txt`, `pyproject.toml`

### requirements.txt

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
cryptography>=41.0.0            # Criptografia e segurança
Pillow>=10.0.0                  # Processamento de imagens/documentos

# --- COMPATIBILIDADE ---
numpy<2.0                       # Compatibilidade com outras bibliotecas
typing-extensions>=4.0.0        # Extensões de tipagem para Python < 3.11

# --- OPCIONAL: OCR E PROCESSAMENTO DE DOCUMENTOS ---
# Descomente se precisar de processamento de documentos
# pytesseract>=0.3.10            # OCR (requer Tesseract instalado)
# opencv-python>=4.8.0           # Processamento avançado de imagem
# pdf2image>=1.16.0              # Conversão PDF para imagem

# --- OPCIONAL: INTEGRAÇÕES EXTERNAS ---
# Para integrações futuras com APIs externas
# httpx>=0.25.0                  # Cliente HTTP moderno
# websockets>=11.0               # WebSocket para tempo real

# --- PLATAFORMA ESPECÍFICA ---
pywin32; sys_platform == 'win32' # Windows specific utilities

# --- DESENVOLVIMENTO ---
# Descomente para desenvolvimento
# pytest>=7.4.0                 # Framework de testes
# pytest-asyncio>=0.21.0        # Testes assíncronos
PyInstaller>=6.0               # Build executável
# black>=23.0.0                  # Formatação de código

# --- DOCUMENTAÇÃO ---
Markdown>=3.0                    # Renderização de markdown
matplotlib>=3.0.0                # Gráficos e relatórios

# ======================================================
# NOTAS DE INSTALAÇÃO:
# ======================================================
# 1. Instale o Python 3.9+ antes de executar
# 2. Crie um ambiente virtual: python -m venv venv
# 3. Ative: venv\Scripts\activate (Windows) ou source venv/bin/activate (Linux/Mac)
# 4. Execute: pip install -r requirements.txt
# 5. Para funcionalidades de OCR, instale o Tesseract separadamente
# 6. Para IA, descomente as dependências correspondentes
# ======================================================

```

### pyproject.toml

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
  "pytest-cov>=4.0.0",
  "pytest-html>=3.0.0",
  "pytest-timeout>=2.0.0",
  "coverage>=7.0.0",
  "pyinstaller>=6.0.0",
  "loguru>=0.7.0"
]

[tool.setuptools.packages.find]
where = ["src"]

```

---

## 42. William-kelvem94/hermes-agent-pinokio

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 43. William-kelvem94/hermes-agent-pinokio-wk

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 44. William-kelvem94/IA_LOCAL_S_ULTRA

- **Manifestos detectados:** `build.gradle.kts`, `settings.gradle.kts`

### build.gradle.kts

```
plugins {
    alias(libs.plugins.android.application) apply false
    alias(libs.plugins.android.library) apply false
    alias(libs.plugins.jetbrains.kotlin.android) apply false
}

```

### settings.gradle.kts

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

---

## 45. William-kelvem94/IA_MUSIC

- **Manifestos detectados:** `requirements.txt`

### requirements.txt

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
psutil>=5.9.6

# ===== VALIDAÇÃO E SERIALIZAÇÃO =====
pydantic>=2.5.0
pydantic-settings>=2.1.0

# ===== LOGGING E MONITORAMENTO =====
loguru>=0.7.2
colorama>=0.4.6

# ===== DESENVOLVIMENTO (OPCIONAL) =====
pytest>=7.4.3
pytest-asyncio>=0.21.1
black>=23.11.0
flake8>=6.1.0
mypy>=1.7.1

# ===== SISTEMA (WINDOWS) =====
pywin32>=306; sys_platform == "win32"
wavio>=0.0.7

# ===== EXTRAS PARA PERFORMANCE =====
numba>=0.58.1
joblib>=1.3.2

# ===== BACKUP/ALTERNATIVAS =====
# Caso alguma biblioteca falhe
mutagen>=1.47.0
ffmpeg-python>=0.2.0

```

---

## 46. William-kelvem94/IA-MIDIA

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 47. William-kelvem94/IA-POTENTE

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 48. William-kelvem94/IA.IDE

- **Manifestos detectados:** `docker-compose.yml`

### docker-compose.yml

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

  ollama-gpu:
    image: ollama/ollama:latest
    container_name: ollama-gpu
    ports:
      - "11434:11434"
    environment:
      - OLLAMA_HOST=0.0.0.0
      - OLLAMA_KEEP_ALIVE=${OLLAMA_KEEP_ALIVE:-24h}
      - OLLAMA_NUM_PARALLEL=${OLLAMA_NUM_PARALLEL:-8}
      - OLLAMA_MAX_LOADED_MODELS=${OLLAMA_MAX_LOADED_MODELS:-4}
      - OLLAMA_FLASH_ATTENTION=1
      - OLLAMA_NUM_GPU=1
      - OLLAMA_MODELS=/models
    volumes:
      - ollama_data:/root/.ollama
      - ./models:/models
    deploy:
      resources:
        limits:
          memory: 20G
        reservations:
          memory: 10G
          devices:
            - capabilities: [gpu]
    healthcheck:
      test: ["CMD-SHELL", "ollama list || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    # Para Docker Desktop (WSL2) com NVIDIA, o compose utiliza o runtime de GPU automaticamente.
    # Em hosts Linux, pode ser necessário configurar nvidia-container-toolkit.
    restart: unless-stopped
    profiles: [gpu]

  openwebui:
    image: ghcr.io/open-webui/open-webui:latest
    container_name: openwebui
    depends_on:
      ollama:
        condition: service_healthy
    ports:
      - "3000:8080"
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434
      - WEBUI_AUTH=True
      - PORT=8080
      - ENABLE_SIGNUP=true
      - ADMIN_EMAIL=admin@local-ai.local
      # Otimizações de performance
      - ENABLE_REQUEST_QUEUE=true
      - REQUEST_QUEUE_MAX_SIZE=20
      - REQUEST_TIMEOUT=300
      # Permite múltiplas requisições simultâneas para maior throughput
      - MAX_CONCURRENT_REQUESTS=4
      # Cache de respostas para maior velocidade
      - ENABLE_RESPONSE_CACHE=true
      - RESPONSE_CACHE_TTL=3600
    volumes:
      - webui_data:/app/backend/data
    deploy:
      resources:
        limits:
          memory: 2G
        reservations:
          memory: 512M
    restart: unless-stopped
    profiles: [cpu]

  openwebui-gpu:
    image: ghcr.io/open-webui/open-webui:latest
    container_name: openwebui-gpu
    depends_on:
      ollama-gpu:
        condition: service_healthy
    ports:
      - "3000:8080"
    environment:
      - OLLAMA_BASE_URL=http://ollama-gpu:11434
      - WEBUI_AUTH=True
      - PORT=8080
      - ENABLE_SIGNUP=true
      - ADMIN_EMAIL=admin@local-ai.local
      # Otimizações de performance
      - ENABLE_REQUEST_QUEUE=true
      - REQUEST_QUEUE_MAX_SIZE=20
      - REQUEST_TIMEOUT=300
      # Permite múltiplas requisições simultâneas para maior throughput
      - MAX_CONCURRENT_REQUESTS=4
      # Cache de respostas para maior velocidade
      - ENABLE_RESPONSE_CACHE=true
      - RESPONSE_CACHE_TTL=3600
    volumes:
      - webui_data:/app/backend/data
    deploy:
      resources:
        limits:
          memory: 2G
        reservations:
          memory: 512M
    restart: unless-stopped
    profiles: [gpu]

  gpt4all-api:
    build:
      context: ./services/gpt4all-api
      dockerfile: Dockerfile
    container_name: gpt4all-api
    ports:
      - "4892:4892"
    environment:
      - PORT=4892
      - GPT4ALL_MODEL=${GPT4ALL_MODEL:-Meta-Llama-3-8B-Instruct.Q4_0.gguf}
    volumes:
      - gpt4all_data:/root/.local/share/nomic.ai/GPT4All
      - ./models/gpt4all:/models
    deploy:
      resources:
        limits:
          memory: 8G
        reservations:
          memory: 4G
    restart: unless-stopped
    profiles: [cpu, gpu]

  gpt4free:
    build:
      context: ./services/gpt4free
      dockerfile: Dockerfile
    container_name: gpt4free
    ports:
      - "1337:1337"
    environment:
      - PORT=1337
      - HOST=0.0.0.0
    volumes:
      - gpt4free_data:/app/.g4f
    deploy:
      resources:
        limits:
          memory: 2G
        reservations:
          memory: 512M
    restart: unless-stopped
    profiles: [cpu, gpu]

volumes:
  ollama_data:
  webui_data:
  gpt4all_data:
  gpt4free_data:




```

---

## 49. William-kelvem94/JARVIS-2.0

- **Manifestos detectados:** `package.json`, `requirements.txt`, `Dockerfile`, `docker-compose.yml`

### package.json

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
    "test:e2e:modules": "tsx scripts/run-clean-test-dbs.js && npm run train en && cross-env PIPENV_PIPFILE=bridges/python/src/Pipfile LEON_NODE_ENV=testing jest --forceExit --silent --verbose --projects test/e2e/modules/e2e.modules.jest.json && tsx scripts/run-clean-test-dbs.js && npm run train",
    "test:e2e:nlp-modules": "npm run train en && cross-env PIPENV_PIPFILE=bridges/python/src/Pipfile LEON_NODE_ENV=testing jest --forceExit --silent --verbose --setupTestFrameworkScriptFile=./test/paths.setup.js test/e2e/nlp-modules.spec.js && npm run train",
    "test:json": "jest --silent --projects test/json/json.jest.json",
    "test:over-http": "npm run generate:skills-endpoints && npm run train && cross-env PIPENV_PIPFILE=bridges/python/src/Pipfile LEON_NODE_ENV=testing LEON_HOST=http://localhost LEON_PORT=1338 LEON_HTTP_API_KEY=72aeb5ba324580963114481144385d7179c106fc jest --forceExit --silent --verbose --notify=false --bail --collectCoverage=false test/e2e/over-http.spec.js",
    "test:module": "tsx scripts/test-module.js",
    "setup:offline": "tsx scripts/setup-offline/setup-offline.js",
    "setup:offline-stt": "tsx scripts/setup-offline/run-setup-stt.js",
    "setup:offline-tts": "tsx scripts/setup-offline/run-setup-tts.js",
    "setup:offline-hotword": "tsx scripts/setup-offline/run-setup-hotword.js",
    "setup:python-bridge": "tsx scripts/setup/setup-python-dev-env.js python-bridge",
    "setup:tcp-server": "tsx scripts/setup/setup-python-dev-env.js tcp-server",
    "preinstall": "node scripts/setup/preinstall.js",
    "postinstall": "tsx scripts/setup/setup.js",
    "dev:app": "vite --config app/vite.config.js",
    "dev:server": "npm run train && npm run generate:skills-endpoints && cross-env LEON_NODE_ENV=development LEON_WARM_UP_LLM_DUTIES=true tsc-watch --noClear --onSuccess \"nodemon\"",
    "dev:server:no-lint": "npm run train && npm run generate:skills-endpoints && cross-env LEON_NODE_ENV=development LEON_WARM_UP_LLM_DUTIES=true \"nodemon\"",
    "inspect:gpu": "./node_modules/node-llama-cpp/dist/cli/cli.js inspect gpu",
    "wake": "cross-env LEON_HOST=http://localhost LEON_PORT=1337 node hotword/index.js",
    "delete-dist:server": "shx rm -rf ./server/dist",
    "clean:python-deps": "shx rm -rf ./bridges/python/src/.venv && npm run postinstall",
    "prepare": "husky",
    "generate:skills-endpoints": "tsx scripts/generate/run-generate-skills-endpoints.js",
    "generate:http-api-key": "tsx scripts/generate/run-generate-http-api-key.js",
    "generate:json-schemas": "tsx scripts/generate/run-generate-json-schemas.js",
    "build": "npm run build:app && npm run build:server",
    "build:app": "cross-env LEON_NODE_ENV=production tsx scripts/app/run-build-app.js",
    "build:server": "npm run delete-dist:server && npm run train && npm run generate:skills-endpoints && tsc --project tsconfig.json && resolve-tspaths && shx rm -rf server/dist/core server/dist/package.json && shx mv -f server/dist/server/src/* server/dist && shx rm -rf server/dist/server && shx mkdir -p server/dist/tmp",
    "build:nodejs-bridge": "tsx scripts/build-binaries.js nodejs-bridge",
    "build:python-bridge": "tsx scripts/build-binaries.js python-bridge",
    "build:tcp-server": "tsx scripts/build-binaries.js tcp-server",
    "start:tcp-server": "cross-env PIPENV_PIPFILE=tcp_server/src/Pipfile LD_LIBRARY_PATH=`PIPENV_PIPFILE=tcp_server/src/Pipfile pipenv run python -c 'import os; import nvidia.cublas.lib; import nvidia.cudnn.lib; print(os.path.dirname(nvidia.cublas.lib.__file__) + \":\" + os.path.dirname(nvidia.cudnn.lib.__file__))'` pipenv run python tcp_server/src/main.py",
    "start": "cross-env LEON_NODE_ENV=production node server/dist/pre-check.js && node server/dist/index.js",
    "python-bridge": "cross-env PIPENV_PIPFILE=bridges/python/src/Pipfile pipenv run python bridges/python/src/main.py server/src/intent-object.sample.json",
    "train": "tsx scripts/train/run-train.js",
    "prepare-release": "tsx scripts/release/prepare-release.js",
    "skill-package": "tsx scripts/skill-package.js",
    "pre-release:nodejs-bridge": "tsx scripts/release/pre-release-binaries.js nodejs-bridge",
    "pre-release:python-bridge": "tsx scripts/release/pre-release-binaries.js python-bridge",
    "pre-release:tcp-server": "tsx scripts/release/pre-release-binaries.js tcp-server",
    "check": "tsx scripts/check.js",
    "kill": "pkill -f node && pkill -f leon-tcp-server && pkill -f pt_main_thread"
  },
  "dependencies": {
    "@aws-sdk/client-polly": "3.18.0",
    "@fastify/static": "6.12.0",
    "@ffprobe-installer/ffprobe": "2.1.2",
    "@fontsource/source-sans-pro": "5.0.8",
    "@google-cloud/speech": "4.2.0",
    "@google-cloud/text-to-speech": "3.2.1",
    "@leon-ai/aurora": "1.0.0-beta.15",
    "@nlpjs/builtin-microsoft": "4.22.7",
    "@nlpjs/core-loader": "4.22.7",
    "@nlpjs/lang-all": "4.22.12",
    "@nlpjs/nlp": "4.22.17",
    "@segment/ajv-human-errors": "2.11.3",
    "@sinclair/typebox": "0.31.23",
    "ajv": "8.18.0",
    "ajv-formats": "2.1.1",
    "archiver": "6.0.1",
    "axios": "^1.18.1",
    "cross-env": "7.0.3",
    "dayjs": "1.11.10",
    "dotenv": "16.4.5",
    "execa": "5.1.1",
    "extract-zip": "2.0.1",
    "fastify": "5.10.0",
    "ffmpeg-static": "5.2.0",
    "fluent-ffmpeg": "2.1.3",
    "getos": "3.2.1",
    "googleapis": "67.1.1",
    "ibm-watson": "6.1.1",
    "ipull": "3.9.2",
    "leon": "file:",
    "node-llama-cpp": "3.7.0",
    "node-wav": "0.0.2",
    "os-name": "4.0.1",
    "pretty-bytes": "5.6.0",
    "ps-list": "7.2.0",
    "react": "18.3.1",
    "react-dom": "18.3.1",
    "remixicon": "3.5.0",
    "socket.io": "4.7.5",
    "socket.io-client": "4.7.5",
    "stt": "1.4.0",
    "tree-kill": "1.2.2"
  },
  "devDependencies": {
    "@eslint/compat": "1.2.3",
    "@eslint/eslintrc": "3.2.0",
    "@eslint/js": "9.15.0",
    "@nlpjs/utils": "4.24.1",
    "@stylistic/eslint-plugin-ts": "2.11.0",
    "@tsconfig/node16": "16.1.1",
    "@tsconfig/strictest": "2.0.2",
    "@types/archiver": "6.0.1",
    "@types/cli-spinner": "0.2.3",
    "@types/fluent-ffmpeg": "2.1.27",
    "@types/getos": "3.0.4",
    "@types/node": "20.9.0",
    "@types/node-wav": "0.0.2",
    "@types/react": "18.3.3",
    "@types/react-dom": "18.3.0",
    "@typescript-eslint/eslint-plugin": "8.15.0",
    "@typescript-eslint/parser": "8.15.0",
    "@vercel/ncc": "0.38.1",
    "@vitejs/plugin-react": "4.1.1",
    "cli-spinner": "0.2.10",
    "eslint": "9.15.0",
    "eslint-config-prettier": "9.0.0",
    "eslint-import-resolver-typescript": "3.6.1",
    "eslint-plugin-import": "2.31.0",
    "eslint-plugin-unicorn": "49.0.0",
    "git-changelog": "2.0.0",
    "globals": "15.12.0",
    "husky": "9.1.7",
    "inquirer": "12.1.0",
    "jest": "27.4.7",
    "jest-canvas-mock": "2.3.1",
    "jest-extended": "2.0.0",
    "json": "11.0.0",
    "lint-staged": "15.1.0",
    "nodemon": "3.1.9",
    "prettier": "3.1.0",
    "resolve-tspaths": "0.8.17",
    "sass": "1.77.2",
    "semver": "7.5.4",
    "shx": "0.3.4",
    "tsc-watch": "6.2.0",
    "tsx": "4.10.5",
    "typescript": "5.5.4",
    "vite": "8.1.4"
  }
}

```

### requirements.txt

```
google-cloud-speech
watson-developer-cloud
pyaudio
speechrecognition
pygame
edge-tts

```

### Dockerfile

```
# Base
FROM node:20-bullseye-slim

# Atualizações básicas
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    make \
    build-essential \
    python3 \
    python3-pip \
    procps \
    && apt-get clean

# Cria o usuário padrão
RUN groupadd -r docker && useradd -r -g docker docker

# Diretórios
WORKDIR /home/docker/jarvis

# Copia apenas package.json para cache mais eficiente
COPY --chown=docker:docker package*.json ./

# Instala apenas o npm primeiro
RUN npm install

# Agora copia o restante do projeto
COPY --chown=docker:docker . .

# Garantir permissões
RUN mkdir -p /home/docker/.npm && chown -R docker:docker /home/docker/.npm

# Instala as dependências Python
RUN pip3 install -r requirements.txt

# User
USER docker

# Porta de comunicação
EXPOSE 1337

# Comando padrão
CMD ["npm", "start"]

```

### docker-compose.yml

```
services:
  jarvis:
    build: .
    image: jarvis2.0
    container_name: jarvis
    environment:
      JARVIS_PORT: ${JARVIS_PORT:-1337}
    ports:
      - "1337:1337"
    network_mode: host
    stdin_open: true
    tty: true

```

---

## 50. William-kelvem94/JOGO-SANDBOX

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 51. William-kelvem94/LEITOR-TELA

- **Manifestos detectados:** `requirements.txt`, `Dockerfile`, `docker-compose.yml`

### requirements.txt

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

# Neural & AI Evolution
sentence-transformers>=2.2.2
chromadb>=0.4.15

```

### Dockerfile

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

# Comando para rodar
CMD ["python", "main.py"]

```

### docker-compose.yml

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

## 52. William-kelvem94/MEU_NECTAR_JARVIS

- **Manifestos detectados:** `docker-compose.yml`

### docker-compose.yml

```
services:
  # PostgreSQL Database
  postgres:
    image: postgres:16-alpine
    container_name: nectar-postgres
    environment:
      POSTGRES_DB: nectar_db
      POSTGRES_USER: nectar_user
      POSTGRES_PASSWORD: nectar_password_2024
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - nectar-network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U nectar_user -d nectar_db"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis Cache
  redis:
    image: redis:7-alpine
    container_name: nectar-redis
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    networks:
      - nectar-network
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Backend API
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: nectar-backend
    environment:
      NODE_ENV: development
      DATABASE_URL: postgresql://nectar_user:nectar_password_2024@postgres:5432/nectar_db
      REDIS_URL: redis://redis:6379
      JWT_SECRET: nectar-jwt-secret-change-in-production
      JWT_EXPIRES_IN: 7d
      OPENAI_API_KEY: ${OPENAI_API_KEY:-sk-your-openai-api-key-here}
      ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY:-sk-ant-your-anthropic-api-key-here}
      PORT: 3001
    ports:
      - "9000:3001"
    volumes:
      - ./backend:/app
      - /app/node_modules
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - nectar-network
    command: sh -c "npx prisma migrate deploy && npm run start:dev"

  # Frontend Application
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: nectar-frontend
    environment:
      NEXT_PUBLIC_API_URL: http://localhost:9000
      NEXT_PUBLIC_AI_LOCAL_URL: http://localhost:8000
      NODE_ENV: development
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
      - /app/node_modules
      - /app/.next
    depends_on:
      - backend
      - ai-local
    networks:
      - nectar-network
    command: npm run dev

  # IA Local com Ollama (Llama 3.2 + Mistral)
  ai-local:
    build:
      context: ./ai-local
      dockerfile: Dockerfile
    container_name: nectar-ai-local
    environment:
      REDIS_HOST: redis
      OLLAMA_HOST: 0.0.0.0
    ports:
      - "8000:8000"  # API FastAPI
      - "11434:11434"  # Ollama
    volumes:
      - ./ai-local:/app
      - ollama_models:/root/.ollama
      - chroma_data:/app/data/chroma
    depends_on:
      redis:
        condition: service_healthy
    networks:
      - nectar-network
    deploy:
      resources:
        limits:
          cpus: '4'
          memory: 8G
    healthcheck:
      test: ["CMD-SHELL", "curl -f -s -m 5 http://localhost:8000/health >/dev/null 2>&1 || exit 1"]
      interval: 90s
      timeout: 20s
      retries: 5
      start_period: 240s

networks:
  nectar-network:
    driver: bridge

volumes:
  postgres_data:
  redis_data:
  ollama_models:
  chroma_data:

```

---

## 53. William-kelvem94/MONITORADOR-ANTIGRAVITY

- **Manifestos detectados:** `package.json`, `Dockerfile`, `docker-compose.yml`

### package.json

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

### Dockerfile

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

### docker-compose.yml

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

## 54. William-kelvem94/Movimentador_de_arquivo

- **Manifestos detectados:** `requirements.txt`

### requirements.txt

```
��P y Q t 5  
 p s u t i l 
```

---

## 55. William-kelvem94/NEXUS-VENDAS

- **Manifestos detectados:** `package.json`, `Dockerfile`, `docker-compose.yml`

### package.json

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

### Dockerfile

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
    done
RUN npm run build

# Instalar dependências do frontend
WORKDIR /app/frontend
RUN npm install

# Build do frontend
WORKDIR /app/frontend
RUN npm run build

# Voltar para raiz
WORKDIR /app

# Copiar arquivo de configuração PM2
COPY ecosystem.config.js /app/ecosystem.config.js

EXPOSE 3000 3001

CMD ["pm2-runtime", "ecosystem.config.js"]

```

### docker-compose.yml

```
services:
  db:
    image: postgres:16-alpine
    container_name: nexus_db
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: nexus_vendas
    ports:
      - "5432:5432"
    volumes:
      - db_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 10
    networks:
      - nexusnet
    restart: unless-stopped

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: nexus_backend
    environment:
      DATABASE_URL: postgresql://postgres:postgres@db:5432/nexus_vendas?schema=public
      JWT_SECRET: nexus-vendas-secret-key-change-in-production-2024
      FRONTEND_ORIGIN: http://localhost:3000
      PORT: 3001
    ports:
      - "3001:3001"
    depends_on:
      db:
        condition: service_healthy
    networks:
      - nexusnet
    restart: unless-stopped

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: nexus_frontend
    environment:
      NEXT_PUBLIC_API_URL: http://localhost:3001/api
    ports:
      - "3000:3000"
    depends_on:
      - backend
    networks:
      - nexusnet
    restart: unless-stopped

volumes:
  db_data:

networks:
  nexusnet:
    driver: bridge

```

---

## 56. William-kelvem94/openclaude-wk

- **Manifestos detectados:** `package.json`, `Dockerfile`

### package.json

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
    "dev:openai": "bun run scripts/provider-launch.ts openai",
    "dev:gemini": "bun run scripts/provider-launch.ts gemini",
    "dev:ollama": "bun run scripts/provider-launch.ts ollama",
    "dev:ollama:fast": "bun run scripts/provider-launch.ts ollama --fast --bare",
    "dev:atomic-chat": "bun run scripts/provider-launch.ts atomic-chat",
    "profile:init": "bun run scripts/provider-bootstrap.ts",
    "profile:recommend": "bun run scripts/provider-recommend.ts",
    "profile:auto": "bun run scripts/provider-recommend.ts --apply",
    "profile:codex": "bun run profile:init -- --provider codex --model codexplan",
    "profile:fast": "bun run profile:init -- --provider ollama --model llama3.2:3b",
    "profile:code": "bun run profile:init -- --provider ollama --model qwen2.5-coder:7b",
    "dev:fast": "bun run profile:fast && bun run dev:ollama:fast",
    "dev:code": "bun run profile:code && bun run dev:profile",
    "dev:grpc": "bun run scripts/start-grpc.ts",
    "dev:grpc:cli": "bun run scripts/grpc-cli.ts",
    "start": "node bin/openclaude",
    "web:dev": "bun run --cwd web dev",
    "web:build": "bun run --cwd web build",
    "web:preview": "bun run --cwd web preview",
    "web:typecheck": "bun run --cwd web typecheck",
    "test": "bun test --feature=UNATTENDED_RETRY",
    "test:full": "bun test --feature=UNATTENDED_RETRY --max-concurrency=1",
    "test:coverage": "bun test --feature=UNATTENDED_RETRY --coverage --coverage-reporter=lcov --coverage-dir=coverage --max-concurrency=1 && bun run scripts/render-coverage-heatmap.ts",
    "test:coverage:ui": "bun run scripts/render-coverage-heatmap.ts",
    "security:pr-scan": "bun run scripts/pr-intent-scan.ts",
    "test:provider-recommendation": "bun test src/utils/providerRecommendation.test.ts src/utils/providerProfile.test.ts",
    "typecheck": "tsc --noEmit",
    "typecheck:type-tests": "bun run scripts/typecheck-type-tests.ts",
    "smoke": "bun run build && node dist/cli.mjs --version",
    "deadcode": "knip --include files,dependencies",
    "check": "bun run smoke && bun run deadcode && bun run test:full",
    "verify:privacy": "bun run scripts/verify-no-phone-home.ts",
    "build:verified": "bun run build && bun run verify:privacy",
    "test:provider": "bun test --feature=UNATTENDED_RETRY --max-concurrency=1 src/services/api/*.test.ts src/utils/context.test.ts",
    "doctor:runtime": "bun run scripts/system-check.ts",
    "doctor:runtime:json": "bun run scripts/system-check.ts --json",
    "doctor:report": "bun run scripts/system-check.ts --out reports/doctor-runtime.json",
    "hardening:check": "bun run smoke && bun run doctor:runtime",
    "hardening:strict": "bun run typecheck && bun run hardening:check",
    "prepack": "npm run build"
  },
  "dependencies": {
    "@orama/orama": "^3.1.18",
    "@orama/plugin-data-persistence": "^3.1.18",
    "@vscode/ripgrep": "^1.17.1"
  },
  "devDependencies": {
    "@alcalzone/ansi-tokenize": "0.3.0",
    "@anthropic-ai/bedrock-sdk": "0.29.1",
    "@anthropic-ai/foundry-sdk": "0.2.3",
    "@anthropic-ai/sandbox-runtime": "0.0.55",
    "@anthropic-ai/sdk": "0.94.0",
    "@aws-sdk/client-bedrock": "3.1047.0",
    "@aws-sdk/client-sts": "3.1047.0",
    "@aws-sdk/credential-provider-node": "3.972.41",
    "@azure/identity": "^4.13.1",
    "@commander-js/extra-typings": "12.1.0",
    "@grpc/grpc-js": "^1.14.3",
    "@grpc/proto-loader": "^0.8.0",
    "@modelcontextprotocol/sdk": "1.29.0",
    "@smithy/core": "3.24.3",
    "@smithy/node-http-handler": "4.7.3",
    "@types/bun": "1.3.11",
    "@types/node": "25.5.0",
    "@types/react": "19.2.14",
    "ajv": "8.18.0",
    "auto-bind": "5.0.1",
    "axios": "1.16.0",
    "bidi-js": "1.0.3",
    "chalk": "5.6.2",
    "chokidar": "4.0.3",
    "cli-boxes": "3.0.0",
    "cli-highlight": "2.1.11",
    "commander": "12.1.0",
    "cross-spawn": "7.0.6",
    "diff": "8.0.3",
    "duck-duck-scrape": "^2.2.7",
    "emoji-regex": "10.6.0",
    "env-paths": "3.0.0",
    "execa": "9.6.1",
    "fflate": "0.8.2",
    "figures": "6.1.0",
    "fuse.js": "7.1.0",
    "graphology": "0.26.0",
    "get-east-asian-width": "1.5.0",
    "google-auth-library": "10.6.2",
    "https-proxy-agent": "7.0.6",
    "ignore": "7.0.5",
    "graphology-metrics": "2.4.0",
    "indent-string": "5.0.0",
    "js-tiktoken": "1.0.21",
    "jsonc-parser": "3.3.1",
    "knip": "^6.16.1",
    "lodash-es": "4.18.1",
    "lru-cache": "11.2.7",
    "marked": "15.0.12",
    "p-map": "7.0.4",
    "picomatch": "4.0.4",
    "proper-lockfile": "4.1.2",
    "qrcode": "1.5.4",
    "react": "19.2.4",
    "react-compiler-runtime": "1.0.0",
    "react-reconciler": "0.33.0",
    "semver": "7.7.4",
    "sharp": "^0.34.5",
    "shell-quote": "1.8.4",
    "signal-exit": "4.1.0",
    "supports-hyperlinks": "3.2.0",
    "tree-kill": "1.2.2",
    "tree-sitter-wasms": "0.1.13",
    "turndown": "7.2.2",
    "type-fest": "4.41.0",
    "typescript": "5.9.3",
    "undici": "7.28.0",
    "usehooks-ts": "3.1.1",
    "web-tree-sitter": "0.25.10",
    "vscode-languageserver-protocol": "3.17.5",
    "wrap-ansi": "9.0.2",
    "ws": "8.21.0",
    "xss": "1.0.15",
    "yaml": "2.8.3",
    "zod": "3.25.76"
  },
  "peerDependencies": {
    "@anthropic-ai/sdk": "^0.94.0",
    "@modelcontextprotocol/sdk": "^1.29.0",
    "react": "^19.0.0",
    "react-reconciler": "^0.33.0"
  },
  "peerDependenciesMeta": {
    "@anthropic-ai/sdk": {
      "optional": true
    },
    "@modelcontextprotocol/sdk": {
      "optional": true
    },
    "react": {
      "optional": true
    },
    "react-reconciler": {
      "optional": true
    }
  },
  "engines": {
    "node": ">=22.0.0"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/Gitlawb/openclaude.git"
  },
  "keywords": [
    "claude-code",
    "openai",
    "llm",
    "cli",
    "agent",
    "deepseek",
    "ollama",
    "gemini"
  ],
  "license": "SEE LICENSE FILE",
  "publishConfig": {
    "access": "public"
  },
  "overrides": {
    "ip-address": "10.2.0",
    "google-auth-library": "10.6.2",
    "lodash-es": "4.18.1",
    "node-domexception": "file:vendor/node-domexception-shim"
  },
  "allowScripts": {
    "protobufjs@7.6.4": true,
    "sharp@0.34.5": true
  }
}

```

### Dockerfile

```
# ---- build stage ----
FROM node:22-slim AS build

WORKDIR /app

# Copy dependency manifests first for better layer caching
COPY package.json bun.lock .bun-version ./

# Install the Bun version tracked by the repo
RUN set -eu; \
    BUN_VERSION="$(tr -d '\r\n' < .bun-version)"; \
    printf '%s' "$BUN_VERSION" | grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+$'; \
    npm install -g "bun@$BUN_VERSION"

# Install all dependencies (including devDependencies for build)
RUN bun install --frozen-lockfile

# Copy source code
COPY src/ src/
COPY scripts/ scripts/
COPY bin/ bin/
COPY tsconfig.json ./

# Build the CLI bundle
RUN bun run build

# Prune devDependencies
RUN rm -rf node_modules && bun install --frozen-lockfile --production

# ---- runtime stage ----
FROM node:22-slim

WORKDIR /app

# Copy only what's needed to run
COPY --from=build /app/dist/cli.mjs dist/cli.mjs
COPY --from=build /app/bin/ bin/
COPY --from=build /app/node_modules/ node_modules/
COPY --from=build /app/package.json package.json
COPY README.md ./

# Install git and ripgrep — many CLI tool operations depend on them
RUN apt-get update && apt-get install -y --no-install-recommends git ripgrep \
    && rm -rf /var/lib/apt/lists/*

# Run as non-root user
USER node

ENTRYPOINT ["node", "/app/bin/openclaude"]

```

---

## 57. William-kelvem94/Openclaw_Docker_Will

- **Manifestos detectados:** `Dockerfile`

### Dockerfile

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

## 58. William-kelvem94/Personal-Voice-Assistent

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 59. William-kelvem94/pixel-agents

- **Manifestos detectados:** `package.json`

### package.json

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
          "title": "Pixel Agents",
          "icon": "$(window)"
        }
      ]
    },
    "views": {
      "pixel-agents-panel": [
        {
          "type": "webview",
          "id": "pixel-agents.panelView",
          "name": "Pixel Agents"
        }
      ]
    }
  },
  "scripts": {
    "vscode:prepublish": "npm run package",
    "build:webview": "cd webview-ui && npm run build",
    "compile": "npm run check-types && npm run lint && node esbuild.js && npm run build:webview",
    "build": "npm run compile",
    "watch": "npm-run-all -p watch:*",
    "watch:esbuild": "node esbuild.js --watch",
    "watch:tsc": "tsc --noEmit --watch --project tsconfig.json",
    "package": "npm run check-types && npm run lint && node esbuild.js --production && npm run build:webview",
    "check-types": "tsc --noEmit && tsc --noEmit -p server/tsconfig.test.json",
    "prepare": "husky",
    "lint": "eslint src server shared && cd webview-ui && eslint .",
    "lint:fix": "eslint src server shared --fix && cd webview-ui && eslint . --fix",
    "import-tileset": "tsx scripts/import-tileset-cli.ts",
    "format": "prettier --write \"src/**/*.ts\" \"server/**/*.ts\" \"shared/**/*.ts\" \"webview-ui/src/**/*.{ts,tsx,css}\" \"*.{js,mjs}\" \"webview-ui/*.{js,ts}\"",
    "format:check": "prettier --check \"src/**/*.ts\" \"server/**/*.ts\" \"shared/**/*.ts\" \"webview-ui/src/**/*.{ts,tsx,css}\" \"*.{js,mjs}\" \"webview-ui/*.{js,ts}\"",
    "test:webview": "cd webview-ui && npm test",
    "test:server": "cd server && npm test",
    "test": "npm run test:webview && npm run test:server",
    "e2e": "playwright test --config e2e/playwright.config.ts",
    "e2e:debug": "playwright test --config e2e/playwright.config.ts --debug",
    "knip": "knip"
  },
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
  "lint-staged": {
    "src/**/*.ts": "eslint --fix",
    "server/**/*.ts": "eslint --fix",
    "shared/**/*.ts": "eslint --fix",
    "webview-ui/src/**/*.{ts,tsx}": "eslint --fix",
    "*.{ts,tsx,js,mjs,css,json,md}": "prettier --write",
    "webview-ui/**/*.{ts,tsx,js,css,json}": "prettier --write"
  }
}

```

---

## 60. William-kelvem94/postifolio-will

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 61. William-kelvem94/PROJECT_JARVIS_3.0

- **Manifestos detectados:** `requirements.txt`, `docker-compose.yml`

### requirements.txt

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
requests==2.31.0
schedule==1.2.0
colorama==0.4.6
rich==13.7.0
click==8.1.7

# Visualização
matplotlib==3.8.2
plotly==5.17.0

# Automação
pyautogui==0.9.54
keyboard==0.13.5

# Processamento de Texto
nltk==3.8.1

# Desenvolvimento
pytest==7.4.4
black==23.12.1
flake8==7.0.0

```

### docker-compose.yml

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

  # Jupyter Notebook - Para treinamento e experimentos
  jupyter:
    image: jupyter/tensorflow-notebook:latest
    container_name: Jarvis_Training
    ports:
      - "8888:8888"
    volumes:
      - ./training_notebooks:/home/jovyan/work
      - ./training_data:/home/jovyan/training_data
      - ./models:/home/jovyan/models
    environment:
      - JUPYTER_ENABLE_LAB=yes
      - JUPYTER_TOKEN=jarvis2025
    restart: unless-stopped
    networks:
      - jarvis_network

volumes:
  ollama_data:
  open_webui_data:

networks:
  jarvis_network:
    driver: bridge

```

---

## 62. William-kelvem94/PROJECT_JARVIS_5.0

- **Manifestos detectados:** `requirements.txt`

### requirements.txt

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

---

## 63. William-kelvem94/PROJECT-JARVIS

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 64. William-kelvem94/rentai-manager

- **Manifestos detectados:** `package.json`

### package.json

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
    "@radix-ui/react-switch": "^1.2.5",
    "@radix-ui/react-tabs": "^1.1.12",
    "@radix-ui/react-toast": "^1.2.14",
    "@radix-ui/react-toggle": "^1.1.9",
    "@radix-ui/react-toggle-group": "^1.1.10",
    "@radix-ui/react-tooltip": "^1.2.7",
    "@tanstack/react-query": "^5.83.0",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "cmdk": "^1.1.1",
    "date-fns": "^3.6.0",
    "embla-carousel-react": "^8.6.0",
    "input-otp": "^1.4.2",
    "lucide-react": "^0.462.0",
    "next-themes": "^0.3.0",
    "react": "^18.3.1",
    "react-day-picker": "^8.10.1",
    "react-dom": "^18.3.1",
    "react-hook-form": "^7.61.1",
    "react-resizable-panels": "^2.1.9",
    "react-router-dom": "^6.30.1",
    "recharts": "^2.15.4",
    "sonner": "^1.7.4",
    "tailwind-merge": "^2.6.0",
    "tailwindcss-animate": "^1.0.7",
    "vaul": "^0.9.9",
    "zod": "^3.25.76"
  },
  "devDependencies": {
    "@eslint/js": "^9.32.0",
    "@tailwindcss/typography": "^0.5.16",
    "@types/node": "^22.16.5",
    "@types/react": "^18.3.23",
    "@types/react-dom": "^18.3.7",
    "@vitejs/plugin-react-swc": "^3.11.0",
    "autoprefixer": "^10.4.21",
    "eslint": "^9.32.0",
    "eslint-plugin-react-hooks": "^5.2.0",
    "eslint-plugin-react-refresh": "^0.4.20",
    "globals": "^15.15.0",
    "lovable-tagger": "^1.1.11",
    "postcss": "^8.5.6",
    "tailwindcss": "^3.4.17",
    "typescript": "^5.8.3",
    "typescript-eslint": "^8.38.0",
    "vite": "^5.4.19"
  }
}

```

---

## 65. William-kelvem94/ruflo

- **Manifestos detectados:** `package.json`

### package.json

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
    "!.claude/**/*.db",
    "!.claude/**/*.map",
    "README.md",
    "LICENSE"
  ],
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "build": "tsc",
    "build:ts": "cd v3/@claude-flow/cli && npm run build || true",
    "test": "vitest",
    "test:ui": "vitest --ui",
    "test:security": "vitest run v3/__tests__/security/",
    "lint": "cd v3/@claude-flow/cli && npm run lint || true",
    "security:audit": "npm audit --audit-level high",
    "security:fix": "npm audit fix",
    "security:test": "npm run test:security",
    "v3:domains": "npm run build:domains",
    "v3:swarm": "npm run start:swarm",
    "v3:security": "npm run security:audit && npm run security:test"
  },
  "dependencies": {
    "@claude-flow/cli-core": "^3.7.0-alpha.5",
    "@claude-flow/mcp": "^3.0.0-alpha.8",
    "@claude-flow/neural": "^3.0.0-alpha.8",
    "@claude-flow/shared": "^3.0.0-alpha.7",
    "@noble/ed25519": "^2.1.0",
    "@ruvector/rabitq-wasm": "^0.1.0",
    "semver": "^7.6.0",
    "zod": "^3.22.4"
  },
  "optionalDependencies": {
    "@claude-flow/codex": "^3.0.0-alpha.8",
    "@claude-flow/plugin-gastown-bridge": "^0.1.3",
    "@ruvector/attention": "^0.1.3",
    "@ruvector/core": "^0.1.30",
    "@ruvector/router": "^0.1.30",
    "@ruvector/router-linux-x64-gnu": "^0.1.30",
    "@ruvector/sona": "^0.1.5",
    "agentdb": "^3.0.0-alpha.16",
    "agentic-flow": "^2.0.13"
  },
  "overrides": {
    "ruvector": "^0.2.27",
    "better-sqlite3": ">=12.8.0",
    "hono": ">=4.11.4",
    "@ruvector/rvf-wasm": "0.1.5",
    "@hono/node-server": ">=1.19.10",
    "flatted": ">=3.4.0",
    "tar": ">=7.5.11",
    "picomatch": ">=4.0.3",
    "path-to-regexp": ">=8.2.1",
    "undici": ">=7.18.0",
    "minimatch": ">=10.0.0",
    "@isaacs/brace-expansion": ">=5.0.1",
    "cacache": ">=20.0.0",
    "make-fetch-happen": ">=15.0.0",
    "express-rate-limit": ">=8.4.1",
    "express": ">=4.22.2",
    "qs": ">=6.15.2",
    "protobufjs": ">=8.2.0",
    "uuid": ">=14.0.0",
    "@opentelemetry/core": "1.25.1",
    "@opentelemetry/resources": "1.25.1",
    "@opentelemetry/sdk-trace-base": "1.25.1",
    "@opentelemetry/sdk-node": ">=0.218.0",
    "@opentelemetry/auto-instrumentations-node": ">=0.75.0",
    "@opentelemetry/exporter-prometheus": ">=0.217.0",
    "axios": ">=1.13.2",
    "fast-uri": ">=3.1.0",
    "vite": ">=6.4.6",
    "ws": ">=8.18.4"
  },
  "devDependencies": {
    "@openai/codex": "^0.98.0",
    "@types/bcrypt": "^5.0.2",
    "@types/node": "^20.0.0",
    "eslint": "^8.0.0",
    "tsx": "^4.21.0",
    "typescript": "^5.0.0",
    "vitest": "^1.0.0"
  },
  "engines": {
    "node": ">=20.0.0"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/ruvnet/claude-flow.git"
  },
  "keywords": [
    "ruvflow",
    "claude",
    "claude-code",
    "anthropic",
    "ai",
    "ai-agents",
    "multi-agent",
    "agent-orchestration",
    "swarm-intelligence",
    "swarm",
    "mcp",
    "model-context-protocol",
    "llm",
    "large-language-model",
    "gpt",
    "chatgpt",
    "automation",
    "workflow",
    "orchestration",
    "cli",
    "developer-tools",
    "devtools",
    "coding-assistant",
    "code-generation",
    "enterprise",
    "vector-database",
    "embeddings",
    "machine-learning",
    "neural-network",
    "hive-mind",
    "distributed-systems",
    "consensus",
    "self-learning"
  ],
  "author": {
    "name": "RuvNet",
    "email": "ruv@ruv.io",
    "url": "https://ruv.io"
  },
  "license": "MIT",
  "publishConfig": {
    "access": "public",
    "tag": "latest"
  }
}

```

---

## 66. William-kelvem94/search_works

- **Manifestos detectados:** `package.json`, `Dockerfile`, `docker-compose.yml`

### package.json

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

### Dockerfile

```
FROM mcr.microsoft.com/playwright:v1.60.0-jammy

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos do package.json
COPY package*.json ./

# Instala dependências
RUN npm install

# Copia todo o código do projeto
COPY . .

# Compila o projeto TypeScript
RUN npm run build

# Expõe a porta do dashboard web
EXPOSE 3000

# Define variáveis padrão do container
ENV HEADLESS=true
ENV PORT=3000

# Comando para iniciar o servidor do dashboard
CMD ["npm", "run", "dashboard"]

```

### docker-compose.yml

```
version: '3.8'

services:
  jobseeker:
    build: .
    container_name: jobseeker_dashboard
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

## 67. William-kelvem94/slack-agent-template

- **Manifestos detectados:** `package.json`

### package.json

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
    "nitropack": "^2.13.0",
    "ora": "^8.2.0",
    "tsx": "^4.21.0"
  },
  "packageManager": "pnpm@10.14.0+sha512.ad27a79641b49c3e481a16a805baa71817a04bbe06a38d17e60e2eaee83f6a146c6a688125f5792e48dd5ba30e7da52a5cda4c3992b9ccf333f9ce223af84748"
}

```

---

## 68. William-kelvem94/STUDY_LLMS

- **Manifestos detectados:** `requirements.txt`

### requirements.txt

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

---

## 69. William-kelvem94/SuperProjeto

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 70. William-kelvem94/TCC_FINAL

- **Manifestos detectados:** `requirements.txt`

### requirements.txt

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

## 71. William-kelvem94/TCC1---Modelo-Antigo

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 72. William-kelvem94/TCC2_FINAL

- **Manifestos detectados:** `requirements.txt`, `Dockerfile`

### requirements.txt

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

### Dockerfile

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

---

## 73. William-kelvem94/teste

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 74. William-kelvem94/TESTER

- **Manifestos detectados:** `requirements.txt`

### requirements.txt

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

## 75. William-kelvem94/Tradutor-2.0

- **Manifestos detectados:** `requirements.txt`

### requirements.txt

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
tqdm==4.67.1
transformers==4.47.0
typing_extensions==4.12.2
urllib3==2.2.3

```

---

## 76. William-kelvem94/TRADUTOR-WKP

- **Manifestos detectados:** `requirements.txt`

### requirements.txt

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
tqdm==4.67.1
transformers==4.47.0
typing_extensions==4.12.2
urllib3==2.2.3

```

---

## 77. William-kelvem94/TRANSCRITOR

- **Manifestos detectados:** `package.json`, `requirements.txt`, `pyproject.toml`, `docker-compose.yml`

### package.json

```
{
  "devDependencies": {
    "@types/node": "^24.10.1"
  }
}

```

### requirements.txt

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

# Autenticação
pyjwt>=2.8.0
cryptography>=41.0.0

# Export
reportlab>=4.0.0  # PDF
python-docx>=1.1.0  # DOCX

# Utilitários
numpy>=1.24.0,<2.0.0
scipy>=1.10.0
Pillow>=10.0.0
requests>=2.31.0
aiofiles>=23.2.1
psutil>=5.9.0
python-dotenv>=1.0.0

# Interface gráfica
# tkinter vem com Python, não precisa instalar

# Dependências do sistema (instalar separadamente se necessário):
# - FFmpeg (para processamento de vídeo) - baixado automaticamente via scripts
# - Git (para download de modelos) - geralmente já instalado

# Nota: Na primeira execução, o Whisper baixará automaticamente
# os modelos necessários (~150MB para o modelo base)

# Para GPU NVIDIA (opcional - descomente e instale se tiver GPU):
# pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118

```

### pyproject.toml

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
line-length = 120
target-version = "py310"
select = [
    "E", "F", "W", "I",     # pycodestyle, pyflakes, warnings, isort
    "B",                     # flake8-bugbear
    "A",                     # flake8-builtins
    "C901",                  # mccabe
]
ignore = ["E501", "W503"]  # Line too long, line break before binary operator

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false
ignore_missing_imports = true
plugins = ["pydantic.mypy"]

[tool.pydantic]
allow_population_by_field_name = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --strict-markers --tb=short --cov=shared --cov=services --cov-report=html --cov-report=term-missing --cov-fail-under=70"
asyncio_mode = "auto"
markers = [
    "unit: Unit tests",
    "integration: Integration tests",
    "e2e: End-to-end tests",
    "slow: Slow running tests",
    "asyncio: Async tests",
]

[tool.coverage.run]
source = ["shared", "services"]
omit = [
    "*/tests/*",
    "*/test_*.py",
    "*/__pycache__/*",
    "*/node_modules/*",
]
branch = true

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
    "if TYPE_CHECKING:",
    "except ImportError:",
    "except ModuleNotFoundError:",
]
precision = 2
skip_covered = false

[tool.pyright]
include = ["shared", "services"]
exclude = ["services/web-ui-service", "**/node_modules"]
typeCheckingMode = "basic"
reportMissingImports = true
reportMissingTypeStubs = false

```

### docker-compose.yml

```
# ============================================================
# TRANSCRITOR - Docker Compose
# ============================================================
# Usage:
#   CPU mode (default): docker compose up -d
#   GPU mode:            docker compose --profile gpu up -d
#   GPU requires:        NVIDIA GPU + nvidia-docker2
# ============================================================

services:
  # ==================== INFRAESTRUTURA ====================
  
  postgres:
    image: postgres@sha256:3d0f7584ed7d04e27fa050d6683a74746608faf21f202be78460d679cc56461f
    container_name: transcritor-postgres
    environment:
      POSTGRES_DB: ${POSTGRES_DB:-transcritor}
      POSTGRES_USER: ${POSTGRES_USER:-transcritor}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-transcritor_pass}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "127.0.0.1:5433:5432"
    networks:
      - database_network
      - backend_network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-transcritor}"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis@sha256:6ab0b6e7381779332f97b8ca76193e45b0756f38d4c0dcda72dbb3c32061ab99
    container_name: transcritor-redis
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
      - ./infrastructure/redis/redis.conf:/usr/local/etc/redis/redis.conf
    ports:
      - "127.0.0.1:6380:6379"
    networks:
      - database_network
      - backend_network
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  rabbitmq:
    image: rabbitmq@sha256:606d8c0d6b3c18d1da9afc53bc7cdb2a8d5486df91b5a9830e9e07626c9ae281
    container_name: transcritor-rabbitmq
    environment:
      RABBITMQ_DEFAULT_USER: ${RABBITMQ_USER:-transcritor}
      RABBITMQ_DEFAULT_PASS: ${RABBITMQ_PASSWORD:-transcritor_pass}
    volumes:
      - rabbitmq_data:/var/lib/rabbitmq
      - ./infrastructure/rabbitmq/rabbitmq.conf:/etc/rabbitmq/rabbitmq.conf
    ports:
      - "127.0.0.1:5672:5672"
      - "127.0.0.1:15672:15672"  # Management UI
    networks:
      - backend_network
    healthcheck:
      test: ["CMD", "rabbitmq-diagnostics", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5


  transcription-service:
    build:
      context: .
      dockerfile: ./services/transcription-service/Dockerfile
      args:
        - USE_GPU=${USE_GPU:-false}
    profiles:
      - ""
      - gpu
    container_name: transcritor-transcription
    user: "1000:1000"
    environment:
      - SERVICE_NAME=transcription-service
      - SERVICE_PORT=8001
      - WHISPER_MODEL=${WHISPER_MODEL:-base}
      - USE_GPU=${USE_GPU:-false}
      - HARDWARE_AUTO_CONFIG=${HARDWARE_AUTO_CONFIG:-true}
      - REDIS_URL=redis://redis:6379
      - RABBITMQ_URL=amqp://${RABBITMQ_USER:-transcritor}:${RABBITMQ_PASSWORD:-transcritor_pass}@rabbitmq:5672/
    volumes:
      - model_cache:/app/models
      - file_storage:/app/temp
      - ./shared:/app/shared
      - ./services/transcription-service/app:/app/service
    ports:
      - "127.0.0.1:8001:8001"
    networks:
      - backend_network
    depends_on:
      redis:
        condition: service_healthy
      rabbitmq:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8001/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 4G
        reservations:
          cpus: '0.5'
          memory: 1G

  summarization-service:
    build:
      context: ./services/summarization-service
      dockerfile: Dockerfile
    container_name: transcritor-summarization
    user: "1000:1000"
    environment:
      - SERVICE_NAME=summarization-service
      - SERVICE_PORT=8002
      - SUMMARY_MODEL=${SUMMARY_MODEL:-extractive}
      - USE_GPU=${USE_GPU:-false}
      - REDIS_URL=redis://redis:6379
      - RABBITMQ_URL=amqp://${RABBITMQ_USER:-transcritor}:${RABBITMQ_PASSWORD:-transcritor_pass}@rabbitmq:5672/
    volumes:
      - model_cache:/app/models
      - ./shared:/app/shared
      - ./services/summarization-service/app:/app/service
    ports:
      - "127.0.0.1:8002:8002"
    networks:
      - backend_network
    depends_on:
      redis:
        condition: service_healthy
      rabbitmq:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8002/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  audio-extraction-service:
    build:
      context: ./services/audio-extraction-service
      dockerfile: Dockerfile
    container_name: transcritor-audio-extraction
    environment:
      - SERVICE_NAME=audio-extraction-service
      - SERVICE_PORT=8003
      - REDIS_URL=redis://redis:6379
      - RABBITMQ_URL=amqp://${RABBITMQ_USER:-transcritor}:${RABBITMQ_PASSWORD:-transcritor_pass}@rabbitmq:5672/
    volumes:
      - file_storage:/app/temp
      - ./shared:/app/shared
      - ./services/audio-extraction-service/app:/app/service
    ports:
      - "127.0.0.1:8003:8003"
    networks:
      - backend_network
    depends_on:
      redis:
        condition: service_healthy
      rabbitmq:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8003/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # ==================== SERVIÇOS DE SUPORTE ====================

  file-management-service:
    build:
      context: ./services/file-management-service
      dockerfile: Dockerfile
    container_name: transcritor-file-management
    user: "1000:1000"
    environment:
      - SERVICE_NAME=file-management-service
      - SERVICE_PORT=8004
      - MAX_FILE_SIZE_MB=${MAX_FILE_SIZE_MB:-2048}
      - STORAGE_SERVICE_URL=http://storage-service:8006
      - REDIS_URL=redis://redis:6379
    volumes:
      - file_storage:/app/storage
      - ./shared:/app/shared
      - ./services/file-management-service/app:/app/service
    ports:
      - "127.0.0.1:8004:8004"
    networks:
      - backend_network
      - frontend_network
    depends_on:
      - storage-service
      - redis
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8004/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  storage-service:
    build:
      context: ./services/storage-service
      dockerfile: Dockerfile
    container_name: transcritor-storage
    environment:
      - SERVICE_NAME=storage-service
      - SERVICE_PORT=8006
      - DATABASE_URL=postgresql://${POSTGRES_USER:-transcritor}:${POSTGRES_PASSWORD:-transcritor_pass}@postgres:5432/${POSTGRES_DB:-transcritor}
      - REDIS_URL=redis://redis:6379
    volumes:
      - file_storage:/app/storage
      - ./shared:/app/shared
      - ./services/storage-service/app:/app/service
    ports:
      - "127.0.0.1:8006:8006"
    networks:
      - backend_network
      - database_network
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8006/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  batch-processor-service:
    build:
      context: ./services/batch-processor-service
      dockerfile: Dockerfile
    container_name: transcritor-batch-processor
    environment:
      - SERVICE_NAME=batch-processor-service
      - SERVICE_PORT=8005
      - TRANSCRIPTION_SERVICE_URL=http://transcription-service:8001
      - SUMMARIZATION_SERVICE_URL=http://summarization-service:8002
      - AUDIO_EXTRACTION_SERVICE_URL=http://audio-extraction-service:8003
      - STORAGE_SERVICE_URL=http://storage-service:8006
      - REDIS_URL=redis://redis:6379
      - RABBITMQ_URL=amqp://${RABBITMQ_USER:-transcritor}:${RABBITMQ_PASSWORD:-transcritor_pass}@rabbitmq:5672/
    volumes:
      - ./shared:/app/shared
      - ./services/batch-processor-service/app:/app/service
    ports:
      - "127.0.0.1:8005:8005"
    networks:
      - backend_network
    depends_on:
      - transcription-service
      - summarization-service
      - audio-extraction-service
      - storage-service
      - redis
      - rabbitmq
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8005/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # ==================== API GATEWAY ====================

  api-gateway:
    build:
      context: ./services/api-gateway
      dockerfile: Dockerfile
    container_name: transcritor-api-gateway
    environment:
      - SERVICE_NAME=api-gateway
      - SERVICE_PORT=8000
      - FILE_MANAGEMENT_URL=http://file-management-service:8004
      - TRANSCRIPTION_URL=http://transcription-service:8001
      - SUMMARIZATION_URL=http://summarization-service:8002
      - AUDIO_EXTRACTION_URL=http://audio-extraction-service:8003
      - BATCH_PROCESSOR_URL=http://batch-processor-service:8005
      - STORAGE_URL=http://storage-service:8006
      - REDIS_URL=redis://redis:6379
      - ENVIRONMENT=${ENVIRONMENT:-development}
      - JWT_SECRET=${JWT_SECRET:-}
      - ALLOW_PUBLIC_REGISTRATION=${ALLOW_PUBLIC_REGISTRATION:-true}
      - CORS_ORIGINS=${CORS_ORIGINS:-http://localhost:3000}
    volumes:
      - ./shared:/app/shared
      - ./services/api-gateway/app:/app/service
    ports:
      - "127.0.0.1:8007:8000"
    networks:
      - frontend_network
      - backend_network
    depends_on:
      file-management-service:
        condition: service_healthy
      transcription-service:
        condition: service_healthy
      summarization-service:
        condition: service_healthy
      audio-extraction-service:
        condition: service_healthy
      batch-processor-service:
        condition: service_healthy
      storage-service:
        condition: service_healthy
      redis:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 20s
    restart: unless-stopped
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 1G
        reservations:
          cpus: '0.25'
          memory: 256M

  # ==================== WEB UI ====================

  web-ui-service:
    build:
      context: ./services/web-ui-service
      dockerfile: Dockerfile
      args:
        - VITE_API_URL=${VITE_API_URL:-http://localhost:8007/api/v1}
    container_name: transcritor-web-ui
    ports:
      - "127.0.0.1:${WEB_UI_PORT:-3000}:80"
    networks:
      - frontend_network
    depends_on:
      api-gateway:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost/health"]
      interval: 30s
      timeout: 3s
      start_period: 10s
      retries: 3
    restart: unless-stopped

  # ==================== MONITORAMENTO ====================

  grafana:
    image: ${GRAFANA_IMAGE:-grafana/grafana@sha256:408afb9726de5122b00a2576763a8a57a3c86d5b0eff5305bc994ceb3eb96c3f}
    container_name: transcritor-grafana
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_PASSWORD:-admin}
      - GF_INSTALL_PLUGINS=redis-datasource,grafana-piechart-panel
    volumes:
      - grafana_data:/var/lib/grafana
      - ./infrastructure/grafana/dashboards:/etc/grafana/provisioning/dashboards
      - ./infrastructure/grafana/datasources:/etc/grafana/provisioning/datasources
    ports:
      - "127.0.0.1:3001:3000"
    networks:
      - monitoring_network
    depends_on:
      - prometheus
    restart: unless-stopped

  prometheus:
    image: ${PROMETHEUS_IMAGE:-prom/prometheus@sha256:f6639335d34a77d9d9db382b92eeb7fc00934be8eae81dbc03b31cfe90411a94}
    container_name: transcritor-prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.lib
```

---

## 78. William-kelvem94/vibe-coding-platform

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## 79. William-kelvem94/webflash-intermediador-de-demandas

- **Manifestos detectados:** `package.json`, `docker-compose.yml`

### package.json

```
{
  "devDependencies": {
    "@ljharb/tsconfig": "^0.3.2"
  }
}

```

### docker-compose.yml

```
services:
  # API Gateway / Backend Principal (versão simplificada)
  api:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "3001:3001"
    environment:
      - NODE_ENV=production
      - PORT=3001
      - IXC_HOST=177.131.28.26
      - IXC_PORT=3306
      - IXC_USER=leitura
      - IXC_PASSWORD=MetabasePass
      - IXC_DATABASE=ixcprovedor
    networks:
      - webflash-network
    restart: unless-stopped

  # Frontend React
  web:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:80"
    environment:
      - REACT_APP_API_URL=http://localhost:3001
      - REACT_APP_WS_URL=ws://localhost:3001
    depends_on:
      - api
    networks:
      - webflash-network
    restart: unless-stopped

  # Ollama para modelos de IA locais
  ollama:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    networks:
      - webflash-network
    restart: unless-stopped
    environment:
      - OLLAMA_HOST=0.0.0.0

  # N8N para automação de workflows
  n8n:
    image: n8nio/n8n:latest
    ports:
      - "5678:5678"
    volumes:
      - n8n_data:/home/node/.n8n
    networks:
      - webflash-network
    restart: unless-stopped
    environment:
      - N8N_HOST=localhost
      - N8N_PORT=5678
      - N8N_PROTOCOL=http
      - NODE_ENV=production
      - WEBHOOK_URL=http://localhost:5678/
      - GENERIC_TIMEZONE=America/Sao_Paulo
      - N8N_SECURITY_CORS_ENABLED=false
      - N8N_REST_API_ENABLED=true
      - N8N_AUTH_TYPE=none

volumes:
  mysql_data:
  redis_data:
  ollama_data:
  openwebui_data:
  n8n_data:
  prometheus_data:

networks:
  webflash-network:
    driver: bridge

```

---

## 80. William-kelvem94/Will-obsidian

- **Manifestos detectados:** `requirements.txt`, `requirements.in`

### requirements.txt

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

### requirements.in

```
# High-level dependency manifest for pip-tools
# Use this file with `pip-compile requirements.in` to generate a locked requirements file.
python-dotenv
numpy
tqdm
sentence-transformers
torch
faiss-cpu

```

---

## 81. William-kelvem94/Will.Nexus

- **Manifestos detectados:** `package.json`, `Dockerfile`

### package.json

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

### Dockerfile

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

---

## 82. William-kelvem94/WilletHub

- **Manifestos detectados:** `package.json`, `Dockerfile`, `docker-compose.yml`

### package.json

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

### Dockerfile

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

### docker-compose.yml

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

## 83. William-kelvem94/willethub-legacy

- **Manifestos detectados:** `docker-compose.yml`

### docker-compose.yml

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
    image: minio/minio
    container_name: notion_minio
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    ports:
      - "9000:9000"
      - "9001:9001"
    volumes:
      - minio_data:/minio_data
    command: minio server /minio_data --console-address ":9001"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 30s
      timeout: 20s
      retries: 3
    networks:
      - notion_network
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: notion_backend
    ports:
      - "3000:3000"
    environment:
      NODE_ENV: development
      DATABASE_URL: postgresql://postgres:password@postgres:5432/notion_db
      REDIS_URL: redis://redis:6379
      JWT_SECRET: your-secret-key
      ALLOWED_ORIGINS: http://localhost:5173
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
      minio:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - notion_network
    volumes:
      - ./backend/src:/app/src
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.dev
    container_name: notion_frontend
    ports:
      - "5173:5173"
    environment:
      VITE_API_URL: http://localhost:3000
      VITE_WS_URL: ws://localhost:3000
    depends_on:
      - backend
    networks:
      - notion_network
    # volumes:
    #   - ./frontend/src:/app/src
volumes:
  postgres_data:
  redis_data:
  minio_data:
networks:
  notion_network:
    driver: bridge

```

---

## 84. William-kelvem94/WILLFINANCE-9.0

- **Manifestos detectados:** `package.json`, `Dockerfile`, `docker-compose.yml`

### package.json

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
    "@radix-ui/react-tabs": "1.1.2",
    "@radix-ui/react-toast": "1.2.4",
    "@radix-ui/react-toggle": "1.1.1",
    "@radix-ui/react-toggle-group": "1.1.1",
    "@radix-ui/react-tooltip": "1.1.6",
    "@vercel/analytics": "1.3.1",
    "autoprefixer": "^10.4.20",
    "bcryptjs": "3.0.3",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "cmdk": "1.0.4",
    "date-fns": "4.1.0",
    "embla-carousel-react": "8.5.1",
    "input-otp": "1.4.1",
    "lucide-react": "^0.454.0",
    "next": "16.0.10",
    "next-themes": "^0.4.6",
    "pg": "^8.11.3",
    "react": "19.2.0",
    "react-day-picker": "9.8.0",
    "react-dom": "19.2.0",
    "react-hook-form": "^7.60.0",
    "react-resizable-panels": "^2.1.7",
    "recharts": "2.15.4",
    "sonner": "^1.7.4",
    "tailwind-merge": "^3.3.1",
    "tailwindcss-animate": "^1.0.7",
    "uuid": "13.0.0",
    "vaul": "^1.1.2",
    "zod": "3.25.76"
  },
  "devDependencies": {
    "@tailwindcss/postcss": "^4.1.9",
    "@types/node": "^22",
    "@types/pg": "^8.10.9",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "postcss": "^8.5",
    "tailwindcss": "^4.1.9",
    "tw-animate-css": "1.3.3",
    "typescript": "^5"
  }
}
```

### Dockerfile

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
RUN pnpm run build

# Stage 3: Runner
FROM node:20-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1

# Criar usuário não-root
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

# Copiar arquivos necessários do build standalone
COPY --from=builder --chown=nextjs:nodejs /app/public ./public

# Copiar arquivos standalone do Next.js
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

EXPOSE 3000

ENV PORT=3000
ENV HOSTNAME="0.0.0.0"

CMD ["node", "server.js"]

```

### docker-compose.yml

```
services:
  # Banco de dados PostgreSQL
  postgres:
    image: postgres:16-alpine
    container_name: willfinance-postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-willfinance}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-willfinance123}
      POSTGRES_DB: ${POSTGRES_DB:-willfinance}
      PGDATA: /var/lib/postgresql/data/pgdata
    ports:
      - "${POSTGRES_PORT:-5432}:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./scripts:/docker-entrypoint-initdb.d:ro
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-willfinance}"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - willfinance-network

  # Aplicação Next.js
  app:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        DATABASE_URL: postgresql://${POSTGRES_USER:-willfinance}:${POSTGRES_PASSWORD:-willfinance123}@postgres:5432/${POSTGRES_DB:-willfinance}?sslmode=disable
    container_name: willfinance-app
    restart: unless-stopped
    ports:
      - "${APP_PORT:-3000}:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgresql://${POSTGRES_USER:-willfinance}:${POSTGRES_PASSWORD:-willfinance123}@postgres:5432/${POSTGRES_DB:-willfinance}?sslmode=disable
      - NEXT_PUBLIC_APP_URL=${NEXT_PUBLIC_APP_URL:-http://localhost:3000}
    depends_on:
      postgres:
        condition: service_healthy
    volumes:
      - ./public:/app/public:ro
    networks:
      - willfinance-network
    healthcheck:
      test: ["CMD", "node", "-e", "require('http').get('http://localhost:3000/api/health', (r) => {process.exit(r.statusCode === 200 ? 0 : 1)})"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

volumes:
  postgres_data:
    driver: local

networks:
  willfinance-network:
    driver: bridge

```

---

## 85. William-kelvem94/William-kelvem94

- **Manifestos detectados:** nenhum manifesto padrão na raiz

---

## Limites

Manifestos em subdiretórios, lockfiles não previstos, dependências transitivas, vulnerabilidades e workflows internos exigem auditoria recursiva por repositório. O conteúdo foi preservado como fonte bruta para a próxima análise.
