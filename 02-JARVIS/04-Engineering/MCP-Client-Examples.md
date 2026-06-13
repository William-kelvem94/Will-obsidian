---
title: "MCP Client Examples"
description: "Exemplos de chamadas Python e curl para usar read_vault_file e search_vault via MCP."
tags: [jarvis, mcp, exemplos, jarvis-engenharia]
updated: 2026-06-13
date: 2026-04-29
---

# Exemplos de Uso do MCP

Este documento mostra exemplos práticos de como chamar ferramentas MCP para ler e buscar conteúdos no vault.

## Exemplo Python: read_vault_file

```python
import requests

MCP_BASE_URL = "http://localhost:8000"

payload = {
    "tool": "read_vault_file",
    "args": {
        "path": "99-Templates/Legado/Conceito-Conhecimento.md"
    }
}

response = requests.post(f"{MCP_BASE_URL}/execute", json=payload)
print(response.json())
```

## Exemplo Python: search_vault

```python
import requests

MCP_BASE_URL = "http://localhost:8000"

payload = {
    "tool": "search_vault",
    "args": {
        "query": "tag:#skills/ai"
    }
}

response = requests.post(f"{MCP_BASE_URL}/execute", json=payload)
print(response.json())
```

## Exemplo curl: read_vault_file

```bash
curl -X POST http://localhost:8000/execute \
  -H "Content-Type: application/json" \
  -d '{"tool": "read_vault_file", "args": {"path": "99-Templates/Legado/Conceito-Conhecimento.md"}}'
```

## Exemplo curl: search_vault

```bash
curl -X POST http://localhost:8000/execute \
  -H "Content-Type: application/json" \
  -d '{"tool": "search_vault", "args": {"query": "tag:#skills/ai"}}'
```

## Notas

- `read_vault_file` retorna o conteúdo de um arquivo específico.
- `search_vault` retorna uma lista de arquivos ou trechos correspondentes à consulta.
- Esses exemplos assumem que o servidor MCP está rodando localmente em `localhost:8000`.

[[02-JARVIS/README|← Voltar ao Command Center]]
