---
title: "Engineering Principles — Will's Tech Philosophy"
description: "Core principles and architectural decisions that guide all technical work"
tags: [identity, principles, architecture, decision-making, jarvis-identidade]
updated: 2026-06-13
date: 2026-04-27
---

# 🏛️ Engineering Principles

These principles guide every technical decision in the Neural Hub ecosystem.

## 🎯 Core Philosophy

### 1. Local-First, Cloud-Fallback
**Principle:** Always prioritize local solutions over cloud dependencies.

**Why:**
- Privacy and data ownership
- Zero recurring costs
- Works offline
- Full control over infrastructure

**Implementation:**
- Ollama/LM Studio before OpenAI/Anthropic
- SQLite/PostgreSQL local before cloud DB
- Local file system before cloud storage
- Self-hosted services before SaaS

**When to break:**
- Feature absolutely requires cloud (e.g., mobile sync)
- Local performance is prohibitive
- Development speed is critical for MVP

---

### 2. Pragmatic Over Perfect
**Principle:** Ship working solutions, iterate based on real usage.

**Why:**
- Perfect is the enemy of done
- Real feedback > theoretical optimization
- Time is the scarcest resource

**Implementation:**
- MVP first, polish later
- Document TODOs instead of blocking
- Monolith before microservices
- SQLite before Postgres (until you need it)

**When to break:**
- Security implications
- Data loss risk
- Technical debt would be catastrophic

---

### 3. Documentation is Code
**Principle:** If it's not documented, it doesn't exist.

**Why:**
- Future-you will forget
- Onboarding (even if it's just you)
- Enables automation and AI assistance

**Implementation:**
- README in every repo
- Inline comments for "why", not "what"
- Decision logs (JARVIS/02-Operational/Decisions/)
- Runbook for every deployment

**When to break:**
- Obvious patterns (don't over-comment)
- Prototyping/spike code

---

### 4. Automate the Boring Stuff
**Principle:** If you do it twice, script it. If you script it twice, tool it.

**Why:**
- Consistency
- Time savings compound
- Reduces human error

**Implementation:**
- Scripts in `.scripts/`
- Git hooks for formatting
- GitHub Actions for CI/CD
- Task runners (Make, npm scripts)

**When to break:**
- One-off migration tasks
- Task takes longer to automate than execute

---

### 5. Observability from Day One
**Principle:** You can't fix what you can't see.

**Why:**
- Debugging without logs is guessing
- Performance regressions are silent
- Usage patterns drive decisions

**Implementation:**
- Structured logging (JSON)
- Health check endpoints
- Basic metrics (requests, errors, latency)
- Daily snapshots (git activity, vault changes)

**When to break:**
- Prototypes/throwaway code
- Performance overhead is unacceptable

---

## 🛠️ Stack Preferences

### Language Selection

| Use Case | First Choice | Alternative | Why |
|----------|-------------|-------------|-----|
| **Scripting/Automation** | Python | Bash/PowerShell | Readable, batteries-included |
| **Web Backend** | FastAPI | Express.js | Type hints, auto-docs, async |
| **Web Frontend** | Next.js 14 | Vite + React | App Router, SSR, file routing |
| **Data Processing** | Python | Node.js | Pandas, NumPy ecosystem |
| **CLI Tools** | Python | Go | Argparse, rich library |
| **Mobile** | React Native | Flutter | Web dev skills transfer |

### Infrastructure Decisions

| Component | First Choice | Alternative | Why |
|-----------|-------------|-------------|-----|
| **Database (dev)** | SQLite | PostgreSQL | Zero config, portable |
| **Database (prod)** | Neon Postgres | Supabase | Serverless, free tier |
| **Cache** | Redis local | In-memory dict | Standard, widely supported |
| **Queue** | Celery + Redis | BullMQ | Python ecosystem |
| **Storage** | Local FS | S3-compatible | No cost, full control |
| **Auth** | JWT + httpOnly | NextAuth | Stateless, simple |
| **Search** | FAISS local | Typesense | Semantic, no server |

### AI/ML Stack

| Component | First Choice | Alternative | Reason |
|-----------|-------------|-------------|--------|
| **LLM** | Ollama (llama3.1) | OpenAI API | Local, free, private |
| **Embeddings** | sentence-transformers | OpenAI Ada | Local, multilingual |
| **Vector DB** | FAISS | ChromaDB | Fast, numpy-based |
| **Speech-to-Text** | Whisper local | Deepgram | Accurate, offline |
| **Text-to-Speech** | Piper TTS | ElevenLabs | Natural, local |
| **Vision** | YOLOv8 | Roboflow | Real-time, PyTorch |

---

## 🔀 Trade-off Matrix

### When to use Ollama vs OpenAI API

| Criterion | Ollama | OpenAI API |
|-----------|--------|------------|
| **Cost** | ✅ Free | ❌ Pay per token |
| **Privacy** | ✅ Local | ❌ Cloud |
| **Speed (no GPU)** | ❌ Slow | ✅ Fast |
| **Speed (with GPU)** | ✅ Fast | ⚠️ Network dependent |
| **Quality** | ⚠️ Good | ✅ Excellent |
| **Context window** | ⚠️ 8-32k | ✅ 128k |
| **Use for:** | Development, prototyping, private data | Production with users, large context |

### When to use SQLite vs PostgreSQL

| Criterion | SQLite | PostgreSQL |
|-----------|--------|------------|
| **Setup** | ✅ Zero config | ❌ Server required |
| **Concurrency** | ❌ Single writer | ✅ Multi-user |
| **Portability** | ✅ Single file | ❌ Dump/restore |
| **Features** | ⚠️ Basic SQL | ✅ Advanced (JSONB, FTS) |
| **Backup** | ✅ Copy file | ⚠️ pg_dump |
| **Use for:** | Dev, CLI tools, single user | Production, multi-user, scaling |

### When to use Monolith vs Microservices

| Criterion | Monolith | Microservices |
|-----------|----------|---------------|
| **Complexity** | ✅ Simple | ❌ High |
| **Deploy** | ✅ One command | ❌ Orchestration needed |
| **Development** | ✅ Fast iteration | ❌ Slow (multiple repos) |
| **Scaling** | ❌ All-or-nothing | ✅ Granular |
| **Team size** | ✅ 1-5 devs | ✅ 5+ devs |
| **Use for:** | MVP, solo projects, most apps | High scale, team autonomy |

---

## 🚫 Anti-Patterns to Avoid

### 1. Premature Optimization
**Bad:** Optimizing for 1M users when you have 0.
**Good:** Profile first, optimize bottlenecks.

### 2. Resume-Driven Development
**Bad:** Using tech because it's trendy (Kubernetes for a blog).
**Good:** Choose based on actual requirements.

### 3. Not Invented Here Syndrome
**Bad:** Rewriting libraries that already exist.
**Good:** Use battle-tested solutions.

### 4. Analysis Paralysis
**Bad:** Spending 2 weeks choosing a framework.
**Good:** Pick one, start building, switch if needed.

### 5. Ignoring Tech Debt
**Bad:** "We'll fix it later" (never happens).
**Good:** Allocate 20% time for refactoring.

---

## 📋 Decision Checklist

Before choosing a technology:

- [ ] **Necessity:** Do I actually need this?
- [ ] **Local-first:** Can this run offline?
- [ ] **Cost:** What's the total cost of ownership (time + money)?
- [ ] **Maintenance:** Can I maintain this in 6 months?
- [ ] **Documentation:** Is there good documentation?
- [ ] **Community:** Is there an active community?
- [ ] **Exit strategy:** Can I migrate away if needed?

---

## 🔗 Related Documents
- [[02-JARVIS/01-Identity/Decision-Framework|Decision Framework]] — Step-by-step decision process
- [[02-JARVIS/02-Operational/Decisions/INDEX|Decision Log]] — Historical decisions and rationale
- [[05-Skills/README|Skills Hub]] — Technical implementations of these principles

---

*Last updated: 2026-04-23*
*These principles evolve. Update this doc when assumptions change.*

[[02-JARVIS/README|← Voltar ao Command Center]]
