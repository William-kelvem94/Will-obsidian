---
title: "Environment Variables Registry"
description: "Central registry of all environment variables used across projects"
tags: [operational, config, security, environment, jarvis-operacao]
updated: 2026-06-05
date: 2026-04-27
---

# 🔐 Environment Variables Registry

Central documentation of all environment variables across the Neural Hub ecosystem.

---

## 📋 Global Variables

These apply across multiple projects:

| Variable | Purpose | Where Used | Type | Example |
|----------|---------|------------|------|---------|
| `GITHUB_TOKEN` | GitHub API access | github_sync.py | Secret | `ghp_xxxx...` |
| `GITHUB_USERNAME` | GitHub user | github_sync.py | Public | `William-kelvem94` |
| `VAULT_PATH` | Obsidian vault location | All scripts | Public | `C:\Users\willi\Documents\GitHub\Will-obsidian` |

---

## 🤖 AI / LLM Variables

### Ollama
| Variable | Purpose | Default | Required |
|----------|---------|---------|----------|
| `OLLAMA_HOST` | Ollama server URL | `http://localhost:11434` | No |
| `OLLAMA_MODEL` | Default model | `llama3.1:8b` | No |
| `OLLAMA_NUM_GPU` | GPU layers | `35` | No |
| `OLLAMA_NUM_THREAD` | CPU threads | `8` | No |

### OpenAI (Fallback)
| Variable | Purpose | Required | Cost |
|----------|---------|----------|------|
| `OPENAI_API_KEY` | API access | Yes (if used) | Pay-per-use |
| `OPENAI_ORG_ID` | Organization | No | - |

### Gemini (Fallback)
| Variable | Purpose | Required | Free Tier |
|----------|---------|----------|-----------|
| `GEMINI_API_KEY` | API access | Yes (if used) | 60 req/min |

### Anthropic (Fallback)
| Variable | Purpose | Required | Cost |
|----------|---------|----------|------|
| `ANTHROPIC_API_KEY` | Claude API | Yes (if used) | Pay-per-use |

---

## 📦 Project-Specific Variables

### PROJECT_JARVIS_5.0
**Location:** `PROJECT_JARVIS_5.0/.env`

```bash
# Core
DATABASE_URL="postgresql://user:pass@localhost:5432/jarvis"
REDIS_URL="redis://localhost:6379"

# AI Services
OLLAMA_HOST="http://localhost:11434"
OLLAMA_MODEL="llama3.1:8b"

# LiveKit (Video/Audio)
LIVEKIT_URL="ws://localhost:7880"
LIVEKIT_API_KEY="your-api-key"
LIVEKIT_API_SECRET="your-api-secret"

# Embeddings
EMBEDDING_MODEL="sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
FAISS_INDEX_PATH="./data/faiss_index"

# Vault Integration
OBSIDIAN_VAULT_PATH="../../../Will-obsidian"
```

---

### Auto-boletos
**Location:** `Auto-boletos/.env`

```bash
# Database
DATABASE_URL="sqlite:///./boletos.db"  # Dev
# DATABASE_URL="postgresql://..." # Prod (Neon)

# AI / OCR
GEMINI_API_KEY="your-gemini-key"  # Optional, has fallback
TESSERACT_PATH="/usr/bin/tesseract"  # Linux
# TESSERACT_PATH="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"  # Windows

# Storage
UPLOAD_DIR="./uploads"
MAX_FILE_SIZE="10485760"  # 10MB

# Security
SECRET_KEY="generate-with-openssl-rand-hex-32"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES="30"

# CORS
ALLOWED_ORIGINS="http://localhost:3000,http://localhost:5173"
```

---

### gestor_aluguel_2.0
**Location:** `gestor_aluguel_2.0/.env`

```bash
# Database (Prisma)
DATABASE_URL="postgresql://user:pass@localhost:5432/gestor_aluguel"

# NextAuth
NEXTAUTH_URL="http://localhost:3000"
NEXTAUTH_SECRET="generate-with-openssl-rand-base64-32"

# Email (for auth)
EMAIL_SERVER="smtp://user:pass@smtp.gmail.com:587"
EMAIL_FROM="noreply@example.com"

# AI (Gemini for analytics)
GEMINI_API_KEY="your-gemini-key"

# Storage (optional)
AWS_ACCESS_KEY_ID="your-s3-key"
AWS_SECRET_ACCESS_KEY="your-s3-secret"
AWS_REGION="us-east-1"
AWS_BUCKET_NAME="gestor-aluguel-files"

# Payment (Stripe/Asaas)
STRIPE_SECRET_KEY="sk_test_..."
STRIPE_WEBHOOK_SECRET="whsec_..."
```

---

### IA-LOCAL
**Location:** `IA-LOCAL/.env`

```bash
# LLM
OLLAMA_HOST="http://localhost:11434"
DEFAULT_MODEL="llama3.1:8b"

# Vector Database
FAISS_INDEX_PATH="./data/brain/index.faiss"
EMBEDDING_MODEL="paraphrase-multilingual-mpnet-base-v2"

# Speech
WHISPER_MODEL="base"  # tiny, base, small, medium, large
PIPER_MODEL="en_US-lessac-medium"
AUDIO_DEVICE_INDEX="0"

# Memory
MEMORY_DB="sqlite:///./memory.db"
CONTEXT_WINDOW="8192"

# Vault
OBSIDIAN_VAULT="../Will-obsidian"
```

---

### DEEP-LEARNING
**Location:** `DEEP-LEARNING/.env`

```bash
# Models
TENSORFLOW_MODEL_PATH="./models/tf_model.h5"
PYTORCH_MODEL_PATH="./models/pytorch_model.pt"

# Training
BATCH_SIZE="32"
LEARNING_RATE="0.001"
EPOCHS="100"

# Data
DATASET_PATH="./data/dataset"
CACHE_DIR="./data/cache"

# GPU
CUDA_VISIBLE_DEVICES="0"  # GPU index
TF_FORCE_GPU_ALLOW_GROWTH="true"
```

---

## 🔒 Secrets Management

### Where Secrets Are Stored

**Development (Local):**
- `.env` files in each project (gitignored)
- **Location:** Same directory as the project
- **Backup:** **DO NOT** commit to git

**Production:**
- Railway/Vercel: Environment variables in dashboard
- Docker: `docker-compose.override.yml` (gitignored)

### .env Template Files

Each project should have:
- `.env.example` (committed, with fake values)
- `.env` (gitignored, with real values)

**Example `.env.example`:**
```bash
# Copy to .env and fill with real values
DATABASE_URL="postgresql://user:password@localhost:5432/dbname"
SECRET_KEY="your-secret-here"
GEMINI_API_KEY="your-api-key"
```

---

## 🛠️ Generating Secrets

### Random String (32 bytes)
```bash
# Linux/Mac
openssl rand -hex 32

# PowerShell
-join ((48..57) + (97..102) | Get-Random -Count 64 | % {[char]$_})
```

### Base64 Secret (for NextAuth)
```bash
# Linux/Mac
openssl rand -base64 32

# PowerShell
[Convert]::ToBase64String((1..32 | ForEach-Object { Get-Random -Maximum 256 }))
```

### UUID
```bash
# Linux/Mac
uuidgen

# PowerShell
[guid]::NewGuid().ToString()
```

---

## 📂 ENV File Locations

Quick reference for where to find `.env` files:

```
Will-obsidian/
├── .env (vault-level, for scripts)
│
Projetos/01-Ativos/Privados/
├── Auto-boletos/
│   └── .env
├── gestor_aluguel_2.0/
│   └── .env
├── PROJECT_JARVIS_5.0/
│   ├── backend/.env
│   └── frontend/.env.local
├── IA-LOCAL/
│   └── .env
└── DEEP-LEARNING/
    └── .env
```

---

## ⚙️ Loading ENV Variables

### Python (with python-dotenv)
```python
from dotenv import load_dotenv
import os

load_dotenv()  # Loads .env from current directory

DATABASE_URL = os.getenv("DATABASE_URL")
API_KEY = os.getenv("API_KEY")
```

### Node.js (with dotenv)
```javascript
require('dotenv').config()

const dbUrl = process.env.DATABASE_URL
const apiKey = process.env.API_KEY
```

### Next.js
```javascript
// .env.local (auto-loaded)
// Access with process.env.VARIABLE_NAME
// Client-side variables must start with NEXT_PUBLIC_
```

---

## 🔍 Finding ENV Issues

Common problems:

### Variable Not Loading
1. Check file name: `.env` not `env.txt`
2. Check location: Same directory or explicitly loaded
3. Check syntax: `KEY=value` (no spaces around `=`)
4. Check quotes: Use `"value"` for values with spaces

### Wrong Value
1. Check for typos in variable name
2. Check `.env` vs `.env.example`
3. Check if value needs to be exported (bash)

### Security Leaks
1. Run: `git log --all --full-history -- "**/.env"`
2. If found, use `git filter-repo` to remove
3. Rotate all leaked secrets immediately

---

## 📋 ENV Audit Checklist

Run periodically to keep configs clean:

- [ ] All `.env` files are in `.gitignore`
- [ ] All projects have `.env.example` with fake values
- [ ] No secrets committed to git (search with `git log`)
- [ ] API keys rotated every 90 days
- [ ] Unused variables removed
- [ ] ENV documentation updated (this file)
- [ ] Backup of `.env` files exists (encrypted, local only)

---

## 🔗 Related Documents

- [[JARVIS/02-Operational/Config/CONFIG|System Config]] — Overall configuration
- [[JARVIS/01-Identity/Will/Engineering-Principles|Engineering Principles]] — Config philosophy
- [[skills/03-infrastructure-mcp/mcp-servers|MCP Servers]] — Server configurations

---

## 🚨 Security Notes

**NEVER:**
- ❌ Commit `.env` files to git
- ❌ Share secrets in Slack/Discord/email
- ❌ Hardcode secrets in code
- ❌ Use production secrets in development

**ALWAYS:**
- ✅ Use `.env.example` for templates
- ✅ Rotate secrets periodically
- ✅ Use different secrets per environment
- ✅ Revoke leaked secrets immediately

---

**Last Audit:** 2026-04-23
**Next Audit:** 2026-07-23 (90 days)

[[JARVIS/README|← Voltar ao Command Center]]
