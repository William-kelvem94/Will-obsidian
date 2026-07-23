---
title: "Workspace Structure Map"
description: "Mapa da estrutura do vault, papéis das pastas e como elas se conectam para projetos, pesquisa e operação." 
tags: [workspace, estrutura, mapa, organizacao]
updated: 2026-06-13
date: 2026-04-27
---

# Workspace Structure Map

## Papéis das pastas principais

- `Bem-vindo.md`
  - Porta de entrada principal do vault.
  - Descreve o propósito geral, hubs principais e como navegar pelo grafo.

- `Projetos/`
  - Hub principal de projetos públicos e privados.
  - Divide por linguagens, objetivos, pesquisas e execução.
  - Contém `EstudosFocados/` e `EstudosPesquisas/` para separar estratégia de pesquisa.

- `02-JARVIS/`
  - Segundo cérebro operacional.
  - Memórias, decisões, aprendizado e base de conhecimento técnica.
  - Usado para manter contexto ativo e registrar progresso do agente.

- `05-Skills/`
  - Prompts, agentes, MCP e workflows para IA no VS Code.
  - Hubs para `vscode-ai` e `fullstack` com documentação de uso e templates.

- `Will-Pessoal/`
  - Perfil pessoal, objetivos, rotina e preferências.
  - Informa o contexto humano que orienta o trabalho do vault.

- `Vault-Ops.md`
  - Guia operacional para manutenção do vault e automações.
  - Inclui scripts de cleanup e padrões de meta-organização.

## Conexões críticas

- `Bem-vindo.md` liga para `Projetos.md`, `05-Skills/README.md`, `02-JARVIS/README.md` e `Vault-Ops.md`.
- `Projetos/EstudosFocados/` e `Projetos/EstudosPesquisas/` devem operar como camadas complementar: visão vs base técnica.
- `02-JARVIS/KnowledgeBase/` e `05-Skills/vscode-ai/` se sobrepõem em pesquisa de IA e agentes; precisam ser referenciados mutuamente.
- `Will-Pessoal/Perfil/Cerebro-Will.md` é o contexto humano que deve ser considerado em decisões de projeto.

## Mapa de pastas e arquivos-chave

- `Projetos/EstudosFocados/IA-LOCAL.md` — visão do Jarvis local e prioridades de voz/visão.
- `Projetos/EstudosFocados/PROJECT_JARVIS_5.0.md` — estratégia multimodal e agentes.
- `Projetos/EstudosFocados/DEEP-LEARNING.md` — RAG e fine-tuning PT-BR.
- `Projetos/EstudosPesquisas/AI-Local-Gratuita.md` — stack de IA local gratuita.
- `Projetos/EstudosPesquisas/Next.js-SaaS-Evolution.md` — deploy e SaaS gratuito.
- `Projetos/EstudosPesquisas/openclaude-wk.md` — evolução do OpenClaude local.
- `Projetos/Privados/openclaude-wk.md` — clone do agente CLI local.
- `05-Skills/vscode-ai/mcp.md` — padrão de ação para leitura e edição.
- `05-Skills/vscode-ai/quick-start.md` — configuração rápida do ambiente de IA.
- `Vault-Ops.md` — operações e normalização do vault.

## Como usar este mapa

1. Identifique o tipo de tarefa:
   - Pesquisa técnica → `Projetos/EstudosPesquisas/`
   - Estratégia e decisão → `Projetos/EstudosFocados/`
   - Implementação local → `Projetos/Privados/`
   - IA / agents / MCP → `02-JARVIS/` e `05-Skills/`
   - Contexto humano → `Will-Pessoal/`
2. Registre descobertas no `Workspace Study Hub`.
3. Use `Vault-Ops.md` para normalizar frontmatter e tags após criar uma nova nota.

## Sugestão de estrutura adicional

- `Projetos/EstudosFocados/Workspace-Study/` → pesquisas de visão geral do vault
- `Projetos/EstudosPesquisas/Workspace-Study/` → guias técnicas específicas, se precisar separar ainda mais
- `05-Skills/vscode-ai/Workspace-Study/` → exemplos práticos de uso de agentes no VS Code

## Recomendação de etiqueta de tags

- `#workspace-study` → notas de análise do vault
- `#study-track` → notas de pesquisa contínua
- `#gap` → lacunas identificadas
- `#pronto` → ações concluídas
- `#recomendacao` → proposta de próxima etapa
