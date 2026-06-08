---
title: "Status da Migração Física"
date: 2026-06-07
updated: 2026-06-07
type: status
status: active
tags: [vault-ops, migracao, status, organizacao]
related: [[Mapa-de-Migracao-Fisica-do-Vault]], [[Reestruturacao-Geral-do-Vault]], [[Inventario-Inicial-do-Vault]]
summary: "Registro do progresso real da reorganização física do vault na branch main."
---

# Status da Migração Física

Esta nota registra o que já foi reorganizado diretamente na branch `main`.

## Áreas físicas criadas

- [x] `00-Inbox/`
- [x] `01-Hubs/`
- [x] `02-JARVIS/`
- [x] `03-Projetos/`
- [x] `04-Conhecimentos/`
- [x] `05-Skills/`
- [x] `06-Will-Pessoal/`
- [x] `07-Operacoes-do-Vault/`
- [x] `08-Arquivo/`
- [x] `09-Sistema/`
- [x] `10-Interfaces/`
- [x] `11-Dados-Brutos/`
- [x] `99-Templates/`

## Arquivos migrados da raiz

| Arquivo antigo | Novo local | Status |
|---|---|---|
| `Painel-Cockpit.md` | `10-Interfaces/Painel-Cockpit.md` | migrado |
| `Projetos.md` | `03-Projetos/Projetos.md` | migrado |
| `AGENTS.md` | `09-Sistema/agents/AGENTS.md` | migrado |
| `CLAUDE.md` | `09-Sistema/agents/CLAUDE.md` | migrado |
| `GEMINI.md` | `09-Sistema/agents/GEMINI.md` | migrado |
| `CLI-BOOTSTRAP.md` | `09-Sistema/CLI-BOOTSTRAP.md` | migrado |
| `claude_desktop_config.json` | `09-Sistema/config/claude_desktop_config.json` | migrado |
| `indexer_config.json` | `09-Sistema/config/indexer_config.json` | migrado |
| `reorganizar-vault-simulacao.bat` | `09-Sistema/scripts/reorganizar-vault-simulacao.bat` | migrado |
| `reorganizar-vault-aplicar.bat` | `09-Sistema/scripts/reorganizar-vault-aplicar.bat` | migrado |

## Arquivos migrados de interfaces

| Arquivo antigo | Novo local | Status |
|---|---|---|
| `dashboards/INDEX.md` | `10-Interfaces/dashboards/INDEX.md` | migrado |
| `dashboards/ROADMAP.md` | `10-Interfaces/dashboards/ROADMAP.md` | copiado; limpeza antiga pendente |
| `dashboards/Tag-Cloud.md` | `10-Interfaces/dashboards/Tag-Cloud.md` | migrado |
| `dashboards/ANALYTICS.md` | `10-Interfaces/dashboards/ANALYTICS.md` | migrado |
| `dashboards/TAXONOMY.md` | `10-Interfaces/dashboards/TAXONOMY.md` | migrado |
| `dashboards/Evolution-Tracker.md` | `10-Interfaces/dashboards/Evolution-Tracker.md` | migrado |
| `dashboards/Knowledge-Heatmap.md` | `10-Interfaces/dashboards/Knowledge-Heatmap.md` | migrado |
| `dashboards/TOKEN-COST-DASHBOARD.md` | `10-Interfaces/dashboards/TOKEN-COST-DASHBOARD.md` | migrado |

## Arquivos técnicos migrados

| Arquivo antigo | Novo local | Status |
|---|---|---|
| `schema/AGENT.md` | `09-Sistema/schema/AGENT.md` | migrado |
| `schema/evolution/ingest-rubric.md` | `09-Sistema/schema/evolution/ingest-rubric.md` | migrado |
| `schema/evolution/output-quality-rubric.md` | `09-Sistema/schema/evolution/output-quality-rubric.md` | migrado |

## Arquivos da raiz que devem permanecer

- `Bem-vindo.md`
- `INDEX.md`
- `README.md`
- `.env.example`
- `.gitignore`
- `.mcp.json`
- `.pre-commit-config.yaml`
- `gitleaks.toml`
- `requirements.in`
- `requirements.txt`
- `requirements-locked.txt`
- `skills-lock.json`
- `start-web-ui.bat`

## Pastas antigas ainda em migração

- [ ] `Conhecimentos-Gerais/`
- [ ] `Conhecimento-Geral/`
- [ ] `Knowledge-Base/`
- [ ] `JARVIS/`
- [ ] `Projetos/`
- [ ] `skills/`
- [ ] `Will-Pessoal/`
- [ ] `dashboards/`
- [ ] `Canvases/`
- [ ] `web-ui/`
- [ ] `Bases/`
- [ ] `raw/`
- [ ] `Clippings/`
- [ ] `schema/`
- [ ] `scripts/`
- [ ] `tests/`
- [ ] `benchmarks/`
- [ ] `simuladores/`

## Bloqueios encontrados

Algumas operações de migração foram bloqueadas pelo conector do GitHub. Quando isso acontecer, o conteúdo deve ser preservado e a limpeza antiga deve ficar marcada como pendente.

Bloqueios atuais conhecidos:

- `dashboards/GAPS.md`
- `dashboards/Skill-Project-Matrix-Dinamica.md`
- `Canvases/README.md`
- limpeza antiga de `dashboards/ROADMAP.md`

## Próximo bloco recomendado

Continuar a migração de `dashboards/` para `10-Interfaces/dashboards/`, priorizando painéis Markdown pequenos e JSONs de apoio.

Depois continuar `schema/`, `scripts`, `tests`, `benchmarks` e `simuladores` para `09-Sistema/`.

Por último, migrar conhecimento e áreas pessoais, pois exigem mais cuidado com links e sensibilidade.

## Regra de continuidade

Cada novo bloco deve ter lista de arquivos movidos, links atualizados, commit em PT-BR, verificação de conteúdo preservado e atualização deste status.
