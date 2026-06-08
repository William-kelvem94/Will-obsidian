---
title: "Sistema Técnico"
date: 2026-06-07
updated: 2026-06-07
type: moc
status: active
tags: [sistema, tecnico, scripts, configuracao]
summary: "Área técnica do vault para configurações, scripts, instruções de agentes, schemas, testes e suporte operacional."
---

# Sistema Técnico

Esta pasta reúne arquivos técnicos do repositório e do ecossistema de automação do vault.

## Subáreas

| Pasta | Função |
|---|---|
| `agents/` | instruções técnicas para agentes e modelos |
| `config/` | configurações de indexação e integrações |
| `scripts/` | scripts, atalhos e automações locais |
| `schema/` | contratos, regras e estrutura técnica, quando migrado |
| `tests/` | testes e fixtures, quando migrado |
| `benchmarks/` | avaliações e medições técnicas, quando migrado |
| `logs/` | logs técnicos quando não forem sensíveis |

## Arquivos já migrados

- [[agents/AGENTS]]
- [[agents/CLAUDE]]
- [[agents/GEMINI]]
- [[CLI-BOOTSTRAP]]
- [[config/indexer_config.json]]
- [[config/claude_desktop_config.json]]
- [[scripts/reorganizar-vault.ps1]]
- [[scripts/reorganizar-vault-simulacao.bat]]
- [[scripts/reorganizar-vault-aplicar.bat]]

## Regra

Arquivos técnicos que ferramentas esperam na raiz devem permanecer na raiz. Arquivos técnicos auxiliares, documentação operacional e scripts próprios devem ficar aqui.
