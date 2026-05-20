---
title: "UI e Agentes"
description: "Como colaborar com agentes em tarefas de frontend sem degradar UX, acessibilidade e performance."
tags: [ia, frontend, ux, acessibilidade, agentes]
updated: 2026-05-08
status: active
---

# UI e Agentes

Agentes podem acelerar frontend, mas tem riscos comuns: UI bonita e inacessivel, mudancas grandes demais, regressao de responsividade e performance.

## O que o agente precisa saber

- design system (shadcn, tailwind, tokens);
- criterios de pronto (estados, loading, error, empty);
- acessibilidade minima (labels, foco, contraste);
- breakpoints e layouts criticos;
- como validar (tests, screenshots, storybook, manual).

## Regras praticas

- mudancas pequenas e revisaveis;
- nao reformatar CSS em massa;
- nao trocar bibliotecas sem motivo;
- sempre considerar mobile e teclado.

## Checklist minimo

- funciona em viewport pequeno e grande
- nao quebra tab order / focus
- texto nao estoura container
- loading/error state existe
- logs/telemetria nao vazam PII

## Relacionado

- [[Conhecimento-Geral/IA-para-Programacao/Reducao-de-Escopo]]
- [[Conhecimento-Geral/IA-para-Programacao/Code-Review-com-Agentes]]


[[Conhecimento-Geral/IA-para-Programacao/INDEX|← Voltar ao índice de IA para Programação]]
