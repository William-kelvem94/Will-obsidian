---
title: "MCP and Agents Research"
description: "Pesquisa sobre Model Context Protocol, agentes de IA e como o vault usa VS Code + workflows de agente." 
tags: [mcp, agentes, IA, pesquisa, projetos]
updated: 2026-06-13
date: 2026-04-27
---

# MCP and Agents Research

## Objetivo
Mapear o uso de MCP, agentes e workflows no vault para guiar a integração técnica entre `JARVIS`, `skills/vscode-ai` e `Projetos`.

## Base existente

- `skills/vscode-ai/mcp.md`
  - Documenta o padrão MCP usado para leitura, edição e validação no VS Code.
  - Define um fluxo iterativo: analyze → plan → act → validate → reflect.

- `skills/vscode-ai/programador-pesquisador.agent.md`
  - Define perfil de agente híbrido para programação + pesquisa.

- `JARVIS/KnowledgeBase/Arquitetura.md`, `Estrategia.md`, `SegundoCerebro.md`
  - Fornecem base de conhecimento e princípios para agentes do segundo cérebro.

## Temas de pesquisa

1. **MCP no VS Code**
   - Uso de `read_file`, `search_files`, `edit_file`, `create_file`, `execute_command`.
   - Workflow recomendado para mudanças seguras e validação.

2. **Agentes personalizados**
   - Como `programador` e `programador-pesquisador` são posicionados para trabalho técnico.
   - Quando usar agentes customizados versus agente padrão.

3. **Arquitetura de agentes**
   - Orquestração de agentes autônomos em `PROJECT_JARVIS_5.0`.
   - Necessidade de fluxo de estado, gRPC e coordenação entre voz/visão.

4. **Integração com o vault**
   - Registrar decisões em `JARVIS/Decisoes/`.
   - Aprender com `JARVIS/Aprendizado/` e atualizar `Memorias/`.

## Gaps identificados

- Falta uma nota central que descreva claramente “como usar MCP no vault”.
- Necessidade de conexão direta entre `skills/vscode-ai` e `JARVIS/KnowledgeBase`.
- Pouca documentação de padrões para agentes autônomos vs assistentes interativos.

## Recomendações

- Criar um fluxograma simples de MCP e agentes: `search -> read -> plan -> act -> validate`.
- Registrar exemplos práticos de uso em `Workspace-Study`.
- Elaborar critérios de decisão para quando usar `programador` vs `programador-pesquisador`.

## Caso prático no vault

1. Identifique uma mudança pequena no vault (ex: atualizar `IA-Local-Research.md`).
2. Use `search_files` para localizar o contexto relevante.
3. Leia `skills/vscode-ai/mcp.md` e planeje os passos.
4. Edite a nota e crie links internos para `Benchmark-IA-Local.md`.
5. Valide com `Vault-Ops.md` e registre no `Workspace-Study`.

## Próximas ações sugeridas

- Documentar em `Workspace-Study` um caso real de correção com MCP.
- Mapear os agentes existentes no vault e seus papéis.
- Criar uma nota de referência rápida para “MCP + VS Code + JARVIS”.

## Links de referência
- [[05-Skills/01-agentic-intelligence/vscode-ai/mcp|MCP para VS Code AI]]
- [[05-Skills/01-agentic-intelligence/vscode-ai/programador-pesquisador.agent|Programador e Pesquisador Agent]]
- [[02-JARVIS/README|JARVIS Hub]]
