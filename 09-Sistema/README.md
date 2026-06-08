---
title: "Sistema Tecnico"
date: 2026-06-07
updated: 2026-06-08
type: moc
status: active
tags: [sistema, tecnico, scripts, configuracao]
summary: "Area tecnica do vault para configuracoes, scripts, instrucoes de agentes, schemas, testes e suporte operacional."
---

# Sistema Tecnico

Esta pasta reune arquivos tecnicos do repositorio e do ecossistema de automacao do vault.

## Subareas

| Pasta | Função |
|---|---|
| `agents/` | instrucoes tecnicas para agentes e modelos |
| `config/` | configuracoes de indexacao e integracoes |
| `scripts/` | scripts, atalhos e automacoes locais |
| `schema/` | contratos, regras e estrutura tecnica |
| `tests/` | testes e fixtures, quando migrado |
| `benchmarks/` | avaliacoes e medições tecnicas, quando migrado |
| `logs/` | logs tecnicos quando nao forem sensiveis |

## Arquivos centrais

- [[agents/AGENTS]]
- [[agents/CLAUDE]]
- [[agents/GEMINI]]
- [[schema/AGENT]]
- [[09-Sistema/CLI-BOOTSTRAP]]
- [[config/indexer_config.json]]
- [[config/claude_desktop_config.json]]
- [[scripts/legado/reorganizar-vault.ps1]]
- [[scripts/legado/reorganizar-vault-simulacao.bat]]
- [[scripts/legado/reorganizar-vault-aplicar.bat]]

## Regra

Arquivos tecnicos que ferramentas esperam na raiz devem permanecer na raiz. Arquivos tecnicos auxiliares, documentacao operacional e scripts proprios devem ficar aqui.
