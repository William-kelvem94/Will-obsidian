---
title: "Vault Architecture Guide"
description: "Complete guide to the 5-tier neural hub architecture"
updated: 2026-06-05
date: 2026-04-27
tags: [jarvis]
---

# 🏗️ Vault Architecture Guide

Complete reference for the Will-obsidian neural hub structure.

---

## 🎯 Design Philosophy

This vault follows a **5-tier architecture** inspired by neural organization:

1. **Identity** — Core values, personality, decision-making
2. **Operational** — Current state, active context
3. **Memory** — Historical events, experiences
4. **Engineering** — Knowledge base, technical wiki
5. **System** — Archive, maintenance, automation

**Key principles:**
- Information flows from identity (who/why) → operations (what/now) → memory (history)
- Engineering tier is accessible from all tiers (knowledge hub)
- System tier handles automation and archival

---

## 📂 Complete Structure

```
Will-obsidian/
│
├── Bem-vindo.md                    # Entry point
├── Graph-Legenda.md                # Visual guide to graph connections
├── Isolated-Notes-Audit.md         # Orphaned notes tracker
├── Projetos.md                     # Projects overview
├── Vault-Ops.md                    # Vault operations guide
│
├── JARVIS/                         🤖 AI Agent System
│   ├── 01-Identity/               # Who & Why
│   │   ├── Will/
│   │   │   ├── Perfil.md          # User profile
│   │   │   ├── Preferencias.md    # User preferences
│   │   │   └── Engineering-Principles.md  # Technical philosophy
│   │   ├── Decision-Framework.md  # Decision-making templates
│   │   └── Personality.md         # JARVIS personality
│   │
│   ├── 02-Operational/            # What & Now
│   │   ├── Dashboard.md           # Current state overview
│   │   ├── Estado.md              # Active context
│   │   └── Config/
│   │       └── ENV-Registry.md    # Environment variables
│   │
│   ├── 03-Memory/                 # When & History
│   │   ├── Logs/                  # Daily activity logs
│   │   │   └── YYYY-MM-DD.md
│   │   ├── Diario/                # Personal diary
│   │   └── Episodicas/            # Episodic memories
│   │
│   ├── 04-Engineering/            # How & Knowledge
│   │   ├── Wiki/
│   │   │   └── CheatSheets/       # Quick references
│   │   │       ├── FastAPI.md
│   │   │       ├── Next.js.md
│   │   │       ├── Prisma.md
│   │   │       └── Docker.md
│   │   ├── Snippets/              # Reusable code
│   │   │   ├── API/
│   │   │   ├── Database/
│   │   │   ├── Frontend/
│   │   │   └── DevOps/
│   │   └── Playbooks/             # Troubleshooting guides
│   │       └── Debug/
│   │           ├── Docker-Not-Starting.md
│   │           ├── Python-Dependency-Hell.md
│   │           ├── Ollama-GPU-Issues.md
│   │           ├── Git-Merge-Conflicts.md
│   │           └── Port-Already-In-Use.md
│   │
│   ├── 05-System/                 # Archive & Automation
│   │   ├── Archive/               # Completed projects
│   │   └── Decisoes/              # Decision logs
│   │       ├── INDEX.md
│   │       └── YYYY-MM-DD-*.md
│   │
│   └── KnowledgeBase/             # Legacy (to be migrated)
│       └── ...
│
├── Projetos/                       📊 Projects Management
│   ├── 01-Ativos/                 # Active projects
│   │   └── Privados/              # Private repos
│   ├── 02-Arquivo/                # Archived projects
│   ├── 03-Estudos/                # Learning projects
│   ├── 04-Master-Plan/            # Strategic planning
│   ├── Objetivos/
│   │   ├── 90-dias.md
│   │   ├── OKRs.md
│   │   └── README.md
│   └── GitHub-Completo.md         # GitHub inventory (67 repos)
│
├── skills/                         🎓 Skills Framework
│   ├── 01-agentic-intelligence/
│   │   └── prompt-engineering/
│   │       └── SKILL.md
│   ├── 02-software-engineering/
│   │   └── testing/
│   │       └── SKILL.md
│   ├── 03-infrastructure-mcp/
│   │   ├── local-llm-ops/
│   │   └── monitoring/
│   │       └── SKILL.md
│   ├── 04-knowledge-systems/
│   │   ├── rag-pipeline/
│   │   │   ├── embeddings_generator.py
│   │   │   ├── vector_store.py
│   │   │   └── query_engine.py
│   │   └── rag-implementation/
│   │       └── SKILL.md
│   └── README.md                  # Skills index
│
├── .scripts/                       🤖 Automation
│   ├── github_sync.py             # GitHub → Obsidian sync
│   ├── vault_cleanup.py           # Metadata normalization
│   ├── daily_logger.py            # Auto activity logging
│   ├── project_health_checker.py  # Project quality scoring
│   └── knowledge_indexer.py       # RAG index builder
│
├── .knowledge_index/               🧠 Vector Database
│   ├── vault.index                # FAISS index
│   ├── embeddings.json.gz         # Cached embeddings
│   └── .embeddings_cache/         # Incremental updates
│
├── Clippings/                      📰 Web clippings
├── Will-Pessoal/                   👤 Personal notes
│   └── ...
│
└── .obsidian/                      ⚙️ Obsidian config
    └── ...
```

---

## 🔄 Information Flow

### Tier 01 → Tier 02 (Identity → Operations)

```
Engineering-Principles.md → Dashboard.md
   ↓                            ↓
Decision-Framework.md  →  Current projects list
```

**Example:** Decision framework influences which projects are prioritized in operational dashboard.

### Tier 02 → Tier 03 (Operations → Memory)

```
Dashboard.md → daily_logger.py → Logs/2026-04-23.md
   ↓                                   ↓
Git commits, file changes → Episodic memory
```

**Example:** Daily activity automatically captured in memory stream.

### Tier 04 ← All Tiers (Engineering Hub)

```
Any tier → CheatSheets, Playbooks, Snippets
              ↓
         Quick reference
```

**Example:** Debugging Docker issue? Check `Playbooks/Debug/Docker-Not-Starting.md`

---

## 📋 Navigation Patterns

### Pattern 1: Top-Down (Discovery)

Start: `Bem-vindo.md` (entry point)
↓
JARVIS/01-Identity/ (understand who/why)
↓
JARVIS/02-Operational/ (see current state)
↓
Specific projects or tasks

### Pattern 2: Bottom-Up (Execution)

Start: Problem or task
↓
JARVIS/04-Engineering/ (find solution in playbooks/cheat sheets)
↓
Execute and update JARVIS/02-Operational/Dashboard.md
↓
Log outcome in JARVIS/03-Memory/Logs/

### Pattern 3: Lateral (Learning)

Start: New technology to learn
↓
skills/ (find SKILL.md for topic)
↓
JARVIS/04-Engineering/Wiki/CheatSheets/ (quick reference)
↓
JARVIS/04-Engineering/Snippets/ (practical examples)

---

## 🎯 Key Files Reference

### 📌 Most Accessed Files

| File | Purpose | When to Use |
|------|---------|-------------|
| `Bem-vindo.md` | Vault entry point | First visit, reorientation |
| `JARVIS/02-Operational/Dashboard.md` | Current state | Daily review, context switch |
| `Projetos/GitHub-Completo.md` | 67 repos inventory | Finding projects, status check |
| `JARVIS/01-Identity/Decision-Framework.md` | Decision templates | Tech choices, architecture decisions |
| `JARVIS/04-Engineering/Playbooks/Debug/` | Troubleshooting | When something breaks |

### 🔧 Automation Scripts

| Script | Function | Trigger |
|--------|----------|---------|
| `github_sync.py` | Sync GitHub → vault | Manual / on-demand |
| `daily_logger.py` | Activity snapshot | Daily / cron |
| `project_health_checker.py` | Quality scoring | Weekly / CI |
| `knowledge_indexer.py` | RAG index build | After major edits |

### 📚 Skills

| Skill | Domain | Use Case |
|-------|--------|----------|
| `prompt-engineering` | AI/LLM | Effective prompting |
| `testing` | QA | Test architecture |
| `rag-implementation` | AI/Knowledge | Semantic search |
| `monitoring` | DevOps | Observability |
| `local-llm-ops` | Infrastructure | Ollama setup |

---

## 🔗 Cross-References

### How Files Connect

```
Engineering-Principles.md
   ↓ influences
Decision-Framework.md
   ↓ used in
Decisoes/YYYY-MM-DD-*.md
   ↓ informs
Dashboard.md
   ↓ creates
Logs/YYYY-MM-DD.md
```

### Link Patterns

**Internal links:**
```markdown
[[JARVIS/04-Engineering/Wiki/CheatSheets/FastAPI|FastAPI]]
[[skills/04-knowledge-systems/rag-implementation/SKILL.md|RAG]]
[[JARVIS/02-Operational/Dashboard|Dashboard]]
```

**Backlinks usage:**
- `Engineering-Principles.md` should have many backlinks (referenced often)
- `Dashboard.md` should link to many files (aggregator)
- `Playbooks/Debug/` should have backlinks from project notes

---

## 📊 Vault Health Metrics

### Tracked Metrics

1. **Isolation Score** (from `Isolated-Notes-Audit.md`)
   - Target: <5% orphaned notes

2. **Project Health** (from `project_health_checker.py`)
   - Active projects with health score >70

3. **Knowledge Index** (from `.knowledge_index/`)
   - Embeddings coverage >90% of notes

4. **Daily Logging** (from `JARVIS/03-Memory/Logs/`)
   - Automatic logs generated daily

---

## 🚀 Usage Workflows

### Workflow 1: Start New Project

1. Create project folder in `Projetos/01-Ativos/`
2. Update `Projetos/GitHub-Completo.md` with repo
3. Log decision in `JARVIS/05-System/Decisoes/`
4. Add to `JARVIS/02-Operational/Dashboard.md`
5. (Optional) Create skills/playbooks if new tech

### Workflow 2: Debug Issue

1. Identify problem domain (Docker, Python, Git, etc.)
2. Check `JARVIS/04-Engineering/Playbooks/Debug/`
3. Follow troubleshooting steps
4. If solved, update playbook with new insights
5. Log resolution in daily log

### Workflow 3: Learn New Technology

1. Check if skill exists in `skills/`
2. If yes: Read SKILL.md → Try examples in Snippets/
3. If no: Create new SKILL.md using template
4. Add to `skills/README.md` index
5. Create cheat sheet in `JARVIS/04-Engineering/Wiki/CheatSheets/`

### Workflow 4: Weekly Review

1. Read `JARVIS/03-Memory/Logs/` from past week
2. Update `JARVIS/02-Operational/Dashboard.md`
3. Run `project_health_checker.py` for active projects
4. Archive completed projects to `Projetos/02-Arquivo/`
5. Update `Projetos/Objetivos/OKRs.md`

---

## 🔮 Future Expansions

### Planned Additions

1. **Tier 01 Expansion:**
   - Learning paths documentation
   - Career roadmap integration

2. **Tier 04 Expansion:**
   - More cheat sheets (Kubernetes, Terraform, GraphQL)
   - Interactive code examples

3. **Skills Expansion:**
   - System design patterns
   - Security best practices
   - API design

4. **Automation:**
   - Auto-sync GitHub issues → vault
   - AI-powered note linking suggestions
   - Automatic skill gap analysis

---

## 🔗 Related Files

- [[Vault-Ops|Vault Operations Guide]]
- [[Graph-Legenda|Graph Legend]]
- [[Projetos|Projects Overview]]
- [[skills/README|Skills Index]]

---

*This architecture evolves with your needs. Update this document as structure changes.*

[[JARVIS/README|← Voltar ao Command Center]]
