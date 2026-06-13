---
tags: [skills, skills-ai, inteligencia-agentica, hub]
projetos_relacionados: [PROJECT_JARVIS_5.0]
updated: 2026-06-13
title: "Inteligencia Agentica — Hub de Skills JARVIS"
date: 2026-06-01
---

# Inteligencia Agentica — Hub de Skills JARVIS

Este hub reune skills, padroes e ferramentas de **Inteligencia Agentica** para o ecossistema JARVIS. Aqui voce encontra definicoes de agentes, protocolos MCP, padroes de raciocinio, arquiteturas de memoria e templates de prompt.

## Proposito

- Reunir prompts, padroes e ferramentas para acelerar tarefas de desenvolvimento com IA.
- Oferecer referencia clara para usar IA local (Ollama, LM Studio, Claude) ou APIs.
- Integrar operacoes com leitura/edicao de arquivos, comandos de terminal e orquestracao multi-agente.

## Arquitetura do Hub

```
+----------------------------------------------------+
|            skills/01-agentic-intelligence/           |
|                                                      |
|  [README]---[INDEX]---[quick-reference]              |
|      |         |            |                        |
|      v         v            v                        |
|  +--------+ +--------+ +----------+                |
|  |Agentes | |MCP     | |Raciocinio|                |
|  |        | |        | |          |                |
|  |prog    | |mcp-op  | |ReAct     |                |
|  |prog-pes| |mini    | |ToT       |                |
|  |dir-prom| |        | |Reflexion |                |
|  +--------+ +--------+ +----------+                |
|       |            |            |                    |
|       v            v            v                    |
|  +--------+ +--------+ +----------+                |
|  |Memoria | |Praticas| |Prompts   |                |
|  |        | |        | |          |                |
|  |mem-arch| |best-pr | |project-j |                |
|  |        | |use-cases| |templates |                |
|  |        | |skills-c| |prompts   |                |
|  +--------+ +--------+ +----------+                |
+----------------------------------------------------+
```

## Navegacao Rapida

### Agentes e Prompts
- [[programador.agent]] — Agente especializado em desenvolvimento de software.
- [[programador-pesquisador.agent]] — Agente hibrido de codigo e pesquisa.
- [[direct-agent-prompts]] — Prompts prontos para copiar no chat local.
- [[project-jarvis-prompts]] — Prompts focados no projeto JARVIS 5.0.
- [[prompts]] — Biblioteca categorizada de templates de prompt.
- [[templates]] — Templates reutilizaveis para agentes e workflows.

### Protocolos e Operacoes
- [[mcp]] — Model Context Protocol: padroes e mapeamento de tools.
- [[mcp-operators]] — Operadores MCP com composicao e pipelines.
- [[mini-agent]] — Agente leve com fluxo completo de leitura/edicao/validacao.

### Padroes de Raciocinio
- [[advanced-reasoning-patterns]] — ReAct, Tree-of-Thought, Reflexion.
- [[multi-agent-orchestration]] — Orquestracao multi-agente com subagentes.
- [[multi-agent-consensus]] — Consenso, votacao e resolucao de conflitos.

### Memoria e Dados
- [[memory-architectures]] — Arquiteturas de memoria: episodica, semantica e de trabalho.

### Praticas e Referencias
- [[quick-reference]] — Cheat sheet de comandos, operadores e padroes.
- [[best-practices]] — Boas praticas, anti-padroes e checklist.
- [[skills-categories]] — Categorias de skills por dominio tecnico.
- [[use-cases]] — Casos de uso reais com configuracoes e resultados.
- [[quick-start]] — Guia de inicio rapido para Windows e VS Code.
- [[advanced-workflows]] — Workflows complexos para projetos avancados.
- [[autonomous-workflow]] — Workflow autonomo com ciclo completo.

## Como Usar

1. Comece por [[INDEX]] para uma visao geral da estrutura.
2. Use [[quick-reference]] para consultas rapidas de operadores.
3. Defina um agente com [[programador.agent]] ou [[programador-pesquisador.agent]].
4. Copie templates de [[prompts]] para seu agente ou prompt builder.
5. Estude [[advanced-reasoning-patterns]] para problemas complexos.
6. Configure memoria com [[memory-architectures]] e [[mcp-operators]].
7. Adapte os exemplos para seu projeto em `Projetos/` ou `Will-Pessoal/`.

## Modelos Suportados

| Modelo | Uso | Provider | Custo |
|--------|-----|----------|-------|
| Ollama Mistral 7B | Tarefas gerais, codigo | Local | Gratuito |
| Ollama Llama 3 8B | Raciocinio, analise | Local | Gratuito |
| Ollama CodeLlama 7B | Programacao | Local | Gratuito |
| Claude 3.5 Sonnet | Tarefas complexas | API | Pago |
| GPT-4o | Raciocinio avancado | API | Pago |

## Integracao com Projetos

1. Abra a pasta do projeto no VS Code.
2. Use [[direct-agent-prompts]] para gerar prompts especificos.
3. Use [[mcp-operators]] para guiar passos de leitura e edicao.
4. Consulte `Projetos/EstudosFocados/Workspace-Study/README` para pesquisa pratica.
5. Salve padroes uteis em [[templates]] ou em `Will-Pessoal/Conhecimento/Leituras.md`.
6. Registre decisoes em `JARVIS/Decisoes/` com timestamp e contexto.

## Recomendacoes Importantes

- Marque notas-chave com tags como `#agentic`, `#mcp`, `#memory`, `#skill`.
- Mantenha skills curtas e com exemplos praticos.
- Prefira modelos locais (Ollama, Mistral) para seguranca e rapidez.
- Consulte [[best-practices]] para garantir qualidade nas implementacoes.

## Referencias

- [[INDEX]] — Indice completo com taxonomia.
- [[use-cases]] — Passo a passo para tarefas comuns.
- [[best-practices]] — Boas praticas para uso seguro e eficiente.
- [[prompt-engineering/SKILL]] — Skill dedicada a engenharia de prompt.
