---
title: "Codebase Maps Index"
description: "Indice RAG-friendly de mapas de codebase para agentes de programacao."
created: 2026-05-08
updated: 2026-05-08
type: codebase-map-index
domain: engineering
tags:
  - jarvis
  - engineering
  - codebase-map
  - rag
  - programming-agents
---

# Codebase Maps Index

Esta pasta reune mapas de codebase para agentes de programacao. As notas foram escritas para recuperacao por RAG: cada arquivo explicita o projeto, fontes locais, stack, entrypoints, areas de risco, proximos probes e tarefas provaveis.

## Mapas disponiveis

| Projeto | Mapa | Uso principal |
|---|---|---|
| PROJECT_JARVIS_5.0 | [[PROJECT_JARVIS_5.0-Codebase-Map]] | Navegar o monorepo real FastAPI + Next.js + percepcao + segundo cerebro. |
| Auto-boletos | [[Auto-boletos-Codebase-Map]] | Orientar agentes em automacao de boletos, Flask, OCR, Playwright e frontend React/Vite. |
| gestor_aluguel_2.0 | [[gestor_aluguel_2.0-Codebase-Map]] | Orientar agentes no SaaS imobiliario Next.js, Prisma, multi-tenant, pagamentos e IA. |
| IA-LOCAL | [[IA-LOCAL-Codebase-Map]] | Orientar agentes no assistente local Python com memoria vetorial, voz e controle de PC. |

## Regras para agentes

- Trate estes mapas como guias de navegacao, nao como substitutos do codigo real.
- Antes de editar qualquer projeto, confirme a estrutura atual com `rg --files` e leia os arquivos de entrada citados no mapa.
- Nao abra nem copie segredos: `.env`, tokens, chaves, cookies, bancos locais e logs sensiveis.
- Preserve mudancas de outras pessoas no workspace. Nao use comandos destrutivos sem pedido explicito.
- Quando o mapa marcar algo como inferencia, valide no codigo antes de implementar.

## Fontes usadas nesta rodada

- [[Projetos/01-Ativos/Privados/PROJECT_JARVIS_5.0]]
- [[Projetos/01-Ativos/Privados/Auto-boletos]]
- [[Projetos/01-Ativos/Privados/gestor_aluguel_2.0]]
- [[Projetos/01-Ativos/Privados/IA-LOCAL]]
- [[Projetos/03-Estudos/EstudosPesquisas/PROJECT_JARVIS_5.0]]
- [[Projetos/03-Estudos/EstudosPesquisas/Auto-boletos]]
- [[Projetos/03-Estudos/EstudosPesquisas/gestor_aluguel_2.0]]
- [[Projetos/03-Estudos/EstudosPesquisas/IA-LOCAL]]
- Leitura local somente leitura de `D:\DOCUMENTOS\GitHub\PROJECT_JARVIS_5.0`.
