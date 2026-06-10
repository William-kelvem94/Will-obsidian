---
title: "Context Engineering Checklist"
category: "ai"
level: 4
description: "Checklist operacional para montar contexto util antes de pedir ou executar uma tarefa com agentes."
projects: []
related_skills: [advanced-workflows, prompts, memory-architectures]
resources: []
updated: 2026-06-10
date: 2026-06-01
tags: [skills-ai]
---

# Context Engineering Checklist

Context engineering checklist e uma rotina antes da execucao: identificar objetivo, limites, evidencias e criterio de pronto. Ela reduz alucinacao operacional e melhora a qualidade das mudancas feitas por agentes.

## Antes de Executar

- Qual e o objetivo exato?
- Quais arquivos, pastas ou dados sao sensiveis?
- Quais mudancas estao fora de escopo?
- O ambiente atual foi verificado?
- Existe trabalho nao relacionado no workspace?
- Qual validacao prova que terminou?

## Durante a Tarefa

- Leia antes de editar.
- Prefira passos pequenos.
- Marque suposicoes.
- Atualize o plano quando descobrir algo novo.
- Pare para permissao antes de risco destrutivo.

## Depois da Tarefa

- Liste arquivos criados ou alterados.
- Resuma decisoes e motivo.
- Registre validacoes feitas.
- Separe pendencias de problemas resolvidos.
- Promova apenas memorias reutilizaveis.

## Uso em Programacao

Em repositorios reais, o checklist deve incluir status do Git, testes relevantes e convencoes locais. O agente deve trabalhar com mudancas existentes, nao assumir que a arvore pertence somente a ele.

## Relacionado

- [[04-Conhecimentos/07-Humanidades/IA-para-Programacao/Engenharia-de-Contexto]]
- [[04-Conhecimentos/07-Humanidades/IA-para-Programacao/Workflow-Humano-Agente]]
- [[05-Skills/01-agentic-intelligence/advanced-workflows]]

