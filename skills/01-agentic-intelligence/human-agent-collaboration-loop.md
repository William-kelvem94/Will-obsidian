---
title: "Human Agent Collaboration Loop"
category: "ai"
level: 4
description: "Skill para conduzir ciclos curtos de colaboracao entre humano, agente e ferramentas."
projects: []
related_skills: [advanced-workflows, autonomous-workflow, mcp-operators]
resources: []
updated: 2026-06-01
date: 2026-06-01
tags: [skills-ai]
---

# Human Agent Collaboration Loop

Human agent collaboration loop e a habilidade de transformar uma intencao humana em execucao assistida, com pontos de controle, validacao e memoria. O foco e cooperacao pratica, nao autonomia sem supervisao.

## Loop

1. `Align`: confirmar objetivo, limites e criterio de sucesso.
2. `Inspect`: ler ambiente, arquivos e historico relevante.
3. `Act`: fazer uma mudanca pequena e reversivel.
4. `Verify`: rodar teste, revisar diff ou validar resultado.
5. `Report`: explicar o que mudou, o que foi validado e o que falta.
6. `Remember`: salvar apenas aprendizado reutilizavel.

## Bons Sinais

- O agente pergunta quando o risco e real.
- O humano decide prioridade e tolerancia a risco.
- A execucao deixa rastro verificavel.
- O resumo final permite continuar depois.

## Falhas Comuns

- Pedir confirmacao para cada micro-passo sem motivo.
- Agir sobre memoria antiga sem verificar o estado atual.
- Esconder falhas de validacao no resumo final.
- Criar documentacao que nao muda o proximo comportamento.

## Relacionado

- [[Conhecimento-Geral/IA-para-Programacao/Workflow-Humano-Agente]]
- [[skills/01-agentic-intelligence/context-engineering-checklist]]
- [[skills/01-agentic-intelligence/advanced-workflows]]

