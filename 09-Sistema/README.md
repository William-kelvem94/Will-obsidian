---
title: "Sistema Tecnico"
date: 2026-06-10
updated: 2026-06-10
type: moc
status: active
tags: [sistema, tecnico, scripts, configuracao]
summary: "Area tecnica do vault para configuracoes, scripts, instrucoes de agentes, schemas, testes e suporte operacional."
---

# Sistema Tecnico

Esta pasta reune arquivos tecnicos do repositorio e do ecossistema de automacao do vault.

## Subareas

| Pasta | Funcao |
|---|---|
| `agents/` | instrucoes tecnicas para agentes e modelos |
| `config/` | configuracoes de indexacao e integracoes |
| `scripts/` | scripts, atalhos e automacoes locais |
| `schema/` | contratos, regras e estrutura tecnica |
| `tests/` | testes e fixtures |
| `benchmarks/` | avaliacoes e metricas tecnicas |
| `logs/` | logs tecnicos quando nao forem sensiveis |

## Arquivos ja migrados

- [[agents/AGENTS]]
- [[agents/CLAUDE]]
- [[agents/GEMINI]]
- [[CLI-BOOTSTRAP]]
- [[config/indexer_config.json]]
- [[config/claude_desktop_config.json]]
- [[scripts/reorganizar-vault.ps1]]
- [[scripts/reorganizar-vault-simulacao.bat]]
- [[scripts/reorganizar-vault-aplicar.bat]]
- `scripts/generate_vault_inventory.py` - gerador de inventario e baseline do vault
- [[schema/evolution/schema-proposals/2026-06-10-vault-expansion-registry-and-mass-data|Proposta de expansao]]

## Regra

Arquivos tecnicos que ferramentas esperam na raiz devem permanecer na raiz. Arquivos tecnicos auxiliares, documentacao operacional e scripts proprios devem ficar aqui.

