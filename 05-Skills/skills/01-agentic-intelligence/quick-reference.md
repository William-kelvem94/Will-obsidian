---
tags: [skills, skills-ai, reference, cheat-sheet]
updated: 2026-06-07
title: "Referencia Rapida — Inteligencia Agentica"
date: 2026-06-01
---

# Referencia Rapida — Inteligencia Agentica

Use este arquivo como atalho rapido para operadores, prompts e workflows essenciais do hub `skills/01-agentic-intelligence/`.

## Operadores Principais (MCP)

| Operador | Sintaxe | Descricao |
|----------|---------|-----------|
| search_files | `search_files(pattern)` | Localiza arquivos por nome ou conteudo |
| read_file | `read_file(path)` | Le conteudo completo do arquivo |
| edit_file | `edit_file(path, old, new)` | Modifica o arquivo com substituicao exata |
| create_file | `create_file(path, content)` | Cria novo arquivo com conteudo |
| append_file | `append_file(path, content)` | Adiciona ao final de arquivo existente |
| delete_file | `delete_file(path)` | Remove arquivo (usar com cautela) |
| execute_command | `execute_command(cmd)` | Roda comando no terminal |
| diff_file | `diff_file(path1, path2)` | Compara versoes de arquivo |
| grep_search | `grep_search(query)` | Busca padrao regex no codigo |
| path_exists | `path_exists(path)` | Verifica existencia de arquivo/dir |

## Fluxo Minimo de Trabalho

```
1. search_files  -> localizar contexto
2. read_file     -> entender o arquivo
3. [planejar]    -> mudanca em texto
4. edit_file     -> aplicar mudanca
5. execute_command -> validar (testes/lint)
6. [resumir]     -> documentar alteracoes
```

## Comandos Essenciais

| Comando | Proposito | Projecto Tipico |
|---------|-----------|-----------------|
| `pnpm install` | Instalar dependencias | Node.js/Next.js |
| `pnpm lint` | Verificar estilo de codigo | TypeScript/React |
| `pnpm dev` | Iniciar servidor dev | Frontend Next.js |
| `pytest` | Rodar testes Python | Backend FastAPI |
| `python -m unittest` | Rodar testes unitarios | Python puro |
| `docker compose up --build` | Subir ambiente completo | Full-stack |
| `ollama pull mistral` | Baixar modelo local | IA local |

## Padroes de Prompt Rapido

### Prompt de Desenvolvimento
```
"Voce e um assistente de desenvolvimento. Encontre o arquivo relevante,
leia o contexto, aplique a mudanca e valide com testes.
Forneca um resumo das alteracoes."
```

### Prompt de Pesquisa
```
"Voce e Programador e Pesquisador. Investigue [problema] no codigo,
documente as descobertas, proponha solucao baseada em evidencias."
```

### Prompt de Revisao
```
"Revise o codigo em [arquivo]. Identifique problemas de seguranca,
performance e estilo. Sugira correcoes especificas."
```

## Troubleshooting Rapido

| Problema | Causa Provavel | Solucao |
|----------|---------------|---------|
| `edit_file` falha | oldString nao encontrado | Leia o arquivo novamente para ver conteudo atual |
| `search_files` vazio | Pattern incorreto | Use `grep_search` com regex ou verifique diretorio |
| `execute_command` timeout | Comando muito lento | Aumente timeout ou divida em comandos menores |
| Modelo nao responde | Contexto muito longo | Use compressao de contexto ou resuma historico |
| Testes falham apos mudanca | Efeito colateral nao previsto | Reverta mudanca, analise dependencias |
| Loop infinito de agente | Falta condicao de parada | Adicione `is_complete` no formato de saida |

## Mapeamento de Arquivos

| Arquivo | Conteudo | Prioridade |
|---------|----------|------------|
| [[README]] | Visao geral do hub | Leitura obrigatoria |
| [[INDEX]] | Indice e navegacao | Consulta |
| [[mcp]] | Padroes MCP | Referencia |
| [[mcp-operators]] | Operadores detalhados | Execucao |
| [[prompts]] | Biblioteca de prompts | Templates |
| [[templates]] | Templates reutilizaveis | Modelos |
| [[programador.agent]] | Agente de codigo | Uso diario |
| [[programador-pesquisador.agent]] | Agente hibrido | Pesquisa |
| [[direct-agent-prompts]] | Prompts prontos | Copiar/colar |
| [[advanced-reasoning-patterns]] | Padroes de raciocinio | Estudo |
| [[memory-architectures]] | Arquiteturas de memoria | RAG |
| [[multi-agent-orchestration]] | Orquestracao de agentes | Multi-agente |
| [[best-practices]] | Boas praticas | Compliance |

## Variaveis de Ambiente Comuns

```bash
# Modelo local
OLLAMA_HOST=http://localhost:11434
MODEL_NAME=mistral:7b

# Memoria vetorial
VECTOR_DB_PATH=./data/vector_store
EMBEDDING_MODEL=all-MiniLM-L6-v2

# Projeto JARVIS
JARVIS_VAULT_PATH=./JARVIS/KnowledgeBase
JARVIS_MEMORY_PATH=./JARVIS/Memory
```

## Referencias

- [[mcp-operators]] — Lista completa de operadores.
- [[quick-start]] — Guia de inicio rapido.
- [[best-practices]] — Checklist de boas praticas.
- [[advanced-workflows]] — Workflows complexos.
