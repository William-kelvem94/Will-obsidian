---
title: "Comandos do JARVIS"
tags: [jarvis, system, mcp, jarvis-sistema]
date: 2026-04-27
updated: 2026-04-29
---

# 📟 Comandos Internos (via servidor MCP)

| Comando | Descrição | Ferramenta MCP |
|---------|-----------|----------------|
| `ler_nota <caminho>` | Retorna conteúdo completo da nota | `read_vault_file` |
| `buscar <termo>` | Busca textual no vault | `search_vault` |
| `projetos_ativos` | Lista projetos com status "Dev" | `search_vault` com query `#projeto/ativo` |
| `diario <data>` | Abre o daily log da data | `read_vault_file` com caminho inferido |

## Exemplo de uso
```json
{ "tool": "read_vault_file", "path": "JARVIS/02-Operational/Foco Atual.md" }
```
