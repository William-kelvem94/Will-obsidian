---
title: "Mapa do Conhecimento"
description: "MOC central para as áreas de conhecimento semântico do vault."
tags: [hub, conhecimento, moc]
updated: 2026-05-16
---

# Mapa do Conhecimento

Este mapa centraliza os domínios de conhecimento que alimentam a base semântica do vault.

```dataview
TABLE
  area as "Área",
  length(tags) as "Tags",
  file.mtime as "Última Modificação"
FROM "Conhecimento-Geral"
WHERE contains(tags, "conceito") AND file.name != "Mapa do Conhecimento"
SORT area ASC, file.mtime DESC
```

## Áreas principais

- [[04-Conhecimentos/07-Humanidades/INDEX|Hub de Conhecimento Geral]]
- [[04-Conhecimentos/07-Humanidades/Filosofia/INDEX|Filosofia e Pensamento Crítico]]
- [[04-Conhecimentos/07-Humanidades/Etica/INDEX|Ética e Alinhamento]]
- [[04-Conhecimentos/07-Humanidades/Psicologia/INDEX|Psicologia e Comportamento Humano]]
- [[04-Conhecimentos/07-Humanidades/Cultura/INDEX|Cultura, História e Sociedade]]
- [[04-Conhecimentos/07-Humanidades/Neurociencia/INDEX|Neurociência Cognitiva]]
- [[04-Conhecimentos/07-Humanidades/Linguistica/INDEX|Linguística e Semiótica]]
- [[04-Conhecimentos/07-Humanidades/Matematica/INDEX|Matemática para IA]]
- [[04-Conhecimentos/07-Humanidades/Tecnologia-e-Sociedade/INDEX|Tecnologia e Sociedade]]
- [[04-Conhecimentos/07-Humanidades/Economia-Digital/INDEX|Economia, Trabalho e Sociedade Digital]]
- [[04-Conhecimentos/07-Humanidades/Direito-Digital/INDEX|Direito e Regulação de IA]]

## Notas de conceito iniciais

- [[04-Conhecimentos/07-Humanidades/Filosofia/Conceitos-Fundamentais|Conceitos Fundamentais de Filosofia]]
- [[04-Conhecimentos/07-Humanidades/Filosofia/Filosofia-da-Mente|Filosofia da Mente]]
- [[04-Conhecimentos/07-Humanidades/Filosofia/Chinese-Room|Quarto Chinês]]
- [[04-Conhecimentos/07-Humanidades/Etica/Consequencialismo|Consequencialismo]]
- [[04-Conhecimentos/07-Humanidades/Etica/Deontologia|Deontologia]]
- [[04-Conhecimentos/07-Humanidades/Etica/Etica-das-Virtudes|Ética das Virtudes]]
- [[04-Conhecimentos/07-Humanidades/Etica/Conceitos-de-Alinhamento|Conceitos de Alinhamento]]
- [[04-Conhecimentos/07-Humanidades/Etica/Transparencia-Algoritmica|Transparência Algorítmica]]
- [[04-Conhecimentos/07-Humanidades/Psicologia/Vieses-Cognitivos|Vieses Cognitivos e Comportamento]]
- [[04-Conhecimentos/07-Humanidades/Psicologia/Vieses-em-LLMs|Vieses em LLMs]]
- [[04-Conhecimentos/07-Humanidades/Psicologia/Teoria-da-Mente|Teoria da Mente]]
- [[04-Conhecimentos/07-Humanidades/Neurociencia/Redes-Neurais-Biologicas|Redes Neurais Biológicas]]
- [[04-Conhecimentos/07-Humanidades/Matematica/Algebra-Linear-Essencial|Álgebra Linear Essencial]]
- [[04-Conhecimentos/07-Humanidades/Matematica/Calculo-e-Otimizacao|Cálculo e Otimização]]
- [[04-Conhecimentos/07-Humanidades/Matematica/Probabilidade-e-Estatistica|Probabilidade e Estatística]]
- [[04-Conhecimentos/07-Humanidades/Matematica/Teoria-da-Informacao|Teoria da Informação]]
- [[04-Conhecimentos/07-Humanidades/Economia-Digital/Automacao-e-Desemprego|Automação e Desemprego]]
- [[04-Conhecimentos/07-Humanidades/Direito-Digital/GDPR-e-Privacidade|GDPR e Privacidade]]
- [[04-Conhecimentos/07-Humanidades/Direito-Digital/EU-AI-Act|EU AI Act]]
- [[04-Conhecimentos/07-Humanidades/Linguistica/Linguistica-e-Semiotica|Linguística e Semiótica]]

## Sugestão de rotas de estudo

1. **Rota Filosófica** — Filosofia da Mente → Chinese Room → Qualia → Problema do Controle → Ética em IA
2. **Rota Cognitiva** — Psicologia Cognitiva → Vieses Cognitivos → Vieses em LLMs → Teoria da Mente → Neurociência
3. **Rota Técnica** — Álgebra Linear → Cálculo e Otimização → Probabilidade → Teoria da Informação → Linguística
4. **Rota Social** — Cultura → Economia Digital → Direito Digital → Tecnologia e Sociedade → Transparência Algorítmica

## Objetivo

Criar um índice semântico que facilite a construção de pipelines RAG e a geração de embeddings de alta qualidade.
