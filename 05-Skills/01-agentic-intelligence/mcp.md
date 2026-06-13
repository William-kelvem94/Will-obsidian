---
tags: [skills, skills-ai]
updated: 2026-06-13
title: "MCP para VS Code AI"
date: 2026-04-27
---

# MCP para VS Code AI

## O que é MCP
Model Context Protocol (MCP) define como agentes de IA interagem com arquivos, comandos e o ambiente.

## Padrões recomendados
- `read_file` — leia arquivo completo ou trecho específico.
- `search_files` — encontre arquivos por nome ou conteúdo.
- `edit_file` — atualize trechos de código ou texto.
- `create_file` — crie novos arquivos de recurso, teste ou docs.
- `execute_command` — rode builds, testes ou scripts no terminal.

## Exemplo de fluxo
1. `search_files` para localizar o módulo alvo.
2. `read_file` para entender a implementação atual.
3. `edit_file` para aplicar a mudança desejada.
4. `execute_command` para validar com testes ou lint.

## Ferramentas de VS Code
- `read_file` / `open_file` — acessar o código fonte.
- `search_files` — localizar arquivos por nome ou conteúdo.
- `edit_file` — modificar código diretamente.
- `create_file` — adicionar novos arquivos de configuração ou docs.
- `execute_command` — rodar `npm test`, `pytest`, `pnpm lint`, `docker compose up`.

## Padrão de workflow
1. `search_files` para localizar o contexto.
2. `read_file` para entender o trecho relevante.
3. Planeje a mudança em texto curto.
4. `edit_file` para aplicar.
5. `execute_command` para validar.
6. `summarize` ou `write_summary` para descrever o resultado.

## MCP iterativo
- `analyze_context` — revisar arquivos antes de agir.
- `plan` — lista de passos com prioridades.
- `act` — executar alterações reais.
- `validate` — rodar testes, lint ou checks.
- `reflect` — criar um breve resumo do que mudou.

## Boas práticas
- Sempre verifique o contexto antes de editar. Use `read_file` em vez de adivinhar.
- Faça commits conceituais: primeiro identificação, depois mudança, depois validação.
- Use mensagens de prompt claras e concisas.
- Para mudanças grandes, gere um plano curto antes de editar.
- Prefira criar uma nota de benchmark ou teste quando modificar lógica crítica.

## Exemplo de fluxo avançado
- Objetivo: adicionar tratamento de erros em `src/service.py`
- Passos:
  1. `search_files` por `service.py`
  2. `read_file` no bloco de função relevante
  3. planeje a alteração: "Adicionar verify() e tratamento de exceções"
  4. `edit_file` para inserir validação e catch
  5. `execute_command` rodar `pytest` ou `pnpm test`
  6. `create_file` ou `edit_file` para atualizar documentação se necessário

## Caso prático: IA local + OpenClaude
- Objetivo: documentar um caso de estudo direto no vault com benchmark e fluxo de agentes.
- Passos:
  1. `search_files` por `IA-LOCAL.md`, `AI-Local-Gratuita.md`, `openclaude-wk.md` e `MCP-and-OpenClaude-Workflow.md`.
  2. `read_file` nos arquivos encontrados para entender a arquitetura, a stack local e o agente CLI.
  3. Planeje um roteiro de benchmark e criação de workflow usando `Practical-Example-Maximum-Files.md`.
  4. `edit_file` para atualizar/expandir `Benchmark-IA-Local.md` e `MCP-and-OpenClaude-Workflow.md`.
  5. `execute_command` para validar dependências e scripts básicos, por exemplo `pip install`, `ollama run` ou comandos do OpenClaude.
  6. `create_file` ou `edit_file` para registrar a conclusão em `JARVIS/Decisoes` e no `Workspace-Study`.

## Exemplo de MCP para correção de bug
- Objetivo: corrigir função X no arquivo `src/service.py`
- Passos:
  1. `search_files` por `service.py`
  2. `read_file` do bloco de função relevante
  3. `edit_file` aplicando a correção
  4. `execute_command` rodar `pytest tests/test_service.py`

## Dicas adicionais
- Consulte `mcp-operators.md` para operadores avançados.
- Use `advanced-workflows.md` para aplicar o padrão em projetos maiores.
- Veja `Projetos/EstudosFocados/Workspace-Study/Benchmark-IA-Local` e `Projetos/EstudosFocados/Workspace-Study/MCP-and-OpenClaude-Workflow` para exemplos práticos de MCP no vault.

## Comandos úteis
- `npm install`
- `pnpm lint`
- `pytest`
- `python -m unittest`
- `npx prisma migrate dev`
- `docker compose up --build`
