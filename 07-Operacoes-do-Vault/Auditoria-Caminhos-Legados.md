---
title: "Auditoria de Caminhos Legados"
date: 2026-07-07
updated: 2026-07-07
type: audit
status: active
tags: [vault-ops, auditoria, migracao, caminhos-canonicos]
summary: "Mapa de inconsistências entre caminhos legados e a estrutura numerada canônica do WILL-OBSIDIAN."
---

# Auditoria de Caminhos Legados

Esta nota registra onde o vault ainda pode estar usando caminhos antigos depois da migração para a estrutura numerada.

Regra: **não apagar legado sem validar links**, mas também não criar conteúdo novo nos caminhos antigos.

## Caminhos canônicos

| Área | Caminho atual |
|---|---|
| Entrada | `00-Inbox/` |
| Hubs | `01-Hubs/` |
| JARVIS | `02-JARVIS/` |
| Projetos | `03-Projetos/` |
| Conhecimentos | `04-Conhecimentos/` |
| Skills | `05-Skills/` |
| Will pessoal | `06-Will-Pessoal/` |
| Operações | `07-Operacoes-do-Vault/` |
| Arquivo | `08-Arquivo/` |
| Sistema | `09-Sistema/` |
| Interfaces | `10-Interfaces/` |
| Dados brutos | `11-Dados-Brutos/` |
| Templates | `99-Templates/` |

## Mapeamento de legado para canônico

| Legado | Canônico |
|---|---|
| `Projetos/` | `03-Projetos/` |
| `JARVIS/` | `02-JARVIS/` |
| `skills/` | `05-Skills/` |
| `Conhecimento-Geral/` | `04-Conhecimentos/07-Humanidades/` |
| `Conhecimentos-Gerais/` | `04-Conhecimentos/` |
| `Knowledge-Base/` | `04-Conhecimentos/` ou `02-JARVIS/` |
| `raw/` | `11-Dados-Brutos/raw/` |
| `Clippings/` | `11-Dados-Brutos/Clippings/` |
| `schema/` | `09-Sistema/schema/` |
| `scripts/` | `09-Sistema/scripts/` ou `.scripts/` |
| `dashboards/` | `10-Interfaces/dashboards/` |
| `Canvases/` | `10-Interfaces/Canvases/` |
| `Templates/` | `99-Templates/Legado/` |

## Ajustes feitos nesta rodada

- `.scripts/project_health_checker.py` passou a priorizar `03-Projetos/01-Ativos/Privados/` e `05-Skills/`.
- `.scripts/sync_private_repos.py` passou a criar notas em `03-Projetos/01-Ativos/Privados/`.
- `.scripts/study_recommender.py` passou a priorizar `05-Skills/` e `04-Conhecimentos/`.

## Pendências

- [ ] Revisar dashboards Dataview ainda apontando para pastas antigas.
- [ ] Revisar schema de agentes para refletir a estrutura numerada.
- [ ] Revisar hubs que ainda citam caminhos legados sem intenção histórica.
- [ ] Atualizar `Status-da-Migracao-Fisica.md` após validação local no Obsidian.
- [ ] Separar links legados intencionais de links realmente quebrados.

## Critério de pronto

A auditoria termina quando scripts, dashboards, schema e hubs ativos usam caminhos numerados, e qualquer legado restante está marcado como histórico ou compatibilidade.
