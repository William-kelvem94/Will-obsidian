---
tags: [skills, skills-ai, index, navigation]
updated: 2026-06-13
title: "Indice de Inteligencia Agentica — JARVIS"
date: 2026-06-01
---

# Indice de Inteligencia Agentica — JARVIS

Este indice organiza e cataloga todas as skills do hub `skills/01-agentic-intelligence/`. Use como ponto de partida para navegar entre arquivos de agentes, protocolos, padroes de raciocinio e arquiteturas de memoria.

## Taxonomia do Hub

```
skills/01-agentic-intelligence/
|
|-- README.md              (visao geral e guia de inicio)
|-- INDEX.md               (este arquivo — navegacao central)
|
|-- AGENTES E PROMPTS
|   |-- programador.agent.md
|   |-- programador-pesquisador.agent.md
|   |-- direct-agent-prompts.md
|   |-- project-jarvis-prompts.md
|   |-- prompts.md
|   |-- templates.md
|
|-- PROTOCOLOS E OPERACOES
|   |-- mcp.md
|   |-- mcp-operators.md
|   |-- mini-agent.md
|
|-- PADROES DE RACIOCINIO
|   |-- advanced-reasoning-patterns.md
|   |-- multi-agent-orchestration.md
|   |-- multi-agent-consensus.md
|
|-- MEMORIA E DADOS
|   |-- memory-architectures.md
|
|-- REFERENCIAS E PRATICAS
|   |-- quick-reference.md
|   |-- best-practices.md
|   |-- skills-categories.md
|   |-- use-cases.md
|   |-- quick-start.md
|   |-- advanced-workflows.md
|   |-- autonomous-workflow.md
|
|-- SKILLS DE PROMPT ENGINEERING
    |-- prompt-engineering/SKILL.md
```

## Tabela de Conteudo

### Agentes e Prompts

| Arquivo | Descricao | Linhas |
|---------|-----------|--------|
| [[programador.agent.md]] | Agente especializado em desenvolvimento de software | ~150 |
| [[programador-pesquisador.agent.md]] | Agente hibrido de codigo e pesquisa tecnica | ~150 |
| [[direct-agent-prompts.md]] | Prompts prontos para copiar e colar no chat local | ~150 |
| [[project-jarvis-prompts.md]] | Prompts focados no projeto PROJECT_JARVIS_5.0 | ~150 |
| [[prompts.md]] | Biblioteca categorizada de templates de prompt | 83 |
| [[templates.md]] | Templates reutilizaveis para agentes e workflows | 91 |

### Protocolos e Operacoes

| Arquivo | Descricao | Linhas |
|---------|-----------|--------|
| [[mcp.md]] | Model Context Protocol — padroes e mapeamento de tools | ~200 |
| [[mcp-operators.md]] | Operadores MCP com composicao e pipelines | ~150 |
| [[mini-agent.md]] | Implementacao de agente leve com fluxo completo | ~150 |

### Padroes de Raciocinio

| Arquivo | Descricao | Linhas |
|---------|-----------|--------|
| [[advanced-reasoning-patterns.md]] | ReAct, Tree-of-Thought, Reflexion com exemplos | ~150 |
| [[multi-agent-orchestration.md]] | Orquestracao multi-agente com subagentes e pipelines | ~150 |
| [[multi-agent-consensus.md]] | Consenso, votacao e resolucao de conflitos entre agentes | ~150 |

### Memoria e Dados

| Arquivo | Descricao | Linhas |
|---------|-----------|--------|
| [[memory-architectures.md]] | Arquiteturas de memoria: episodica, semantica, de trabalho | ~150 |

### Praticas e Referencias

| Arquivo | Descricao | Linhas |
|---------|-----------|--------|
| [[quick-reference.md]] | Cheat sheet de comandos, operadores e padroes | ~150 |
| [[best-practices.md]] | Boas praticas, anti-padroes e checklist | ~150 |
| [[skills-categories.md]] | Categorias de skills por dominio tecnico | ~150 |
| [[use-cases.md]] | Casos de uso reais com configuracoes e resultados | ~150 |
| [[quick-start.md]] | Comandos rapidos para ambiente Windows e VS Code | ~100 |
| [[advanced-workflows.md]] | Workflows complexos para projetos avancados | ~100 |
| [[autonomous-workflow.md]] | Workflow autonomo com ciclo completo | ~100 |
| [[browser-automation.md]] | Automacao de navegador para coleta, verificacao e research | ~80 |

## Guia de Navegacao Rapida

1. **Iniciante**: Comece por [[README.md]], depois [[quick-start.md]] e [[mcp.md]].
2. **Pratica de codigo**: Use [[programador.agent.md]] e [[mini-agent.md]].
3. **Pesquisa tecnica**: Combine [[programador-pesquisador.agent.md]] com [[advanced-reasoning-patterns.md]].
4. **Sistemas multi-agente**: Leia [[multi-agent-orchestration.md]] e [[multi-agent-consensus.md]].
5. **Memoria e RAG**: Estude [[memory-architectures.md]] e [[project-jarvis-prompts.md]].
6. **Producao de prompts**: Consulte [[prompts.md]], [[templates.md]] e [[direct-agent-prompts.md]].
7. **Referencia rapida**: Utilize [[quick-reference.md]] e [[best-practices.md]].
8. **Browser automation**: Consulte [[browser-automation.md]] para coleta e verificacao operacional.

## Convencoes do Hub

- Todos os arquivos usam frontmatter YAML com `tags` e `updated`.
- Conteudo em portugues brasileiro com exemplos praticos de codigo.
- Wiki-links `[[arquivo]]` para navegacao entre notas.
- Blocos de codigo com identificacao de linguagem.
- Arquivos > 80 linhas nao sao modificados para manter estabilidade.
