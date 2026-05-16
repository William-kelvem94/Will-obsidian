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

- [[Conhecimento-Geral/INDEX|Hub de Conhecimento Geral]]
- [[Conhecimento-Geral/Filosofia/INDEX|Filosofia e Pensamento Crítico]]
- [[Conhecimento-Geral/Etica/INDEX|Ética e Alinhamento]]
- [[Conhecimento-Geral/Psicologia/INDEX|Psicologia e Comportamento Humano]]
- [[Conhecimento-Geral/Cultura/INDEX|Cultura, História e Sociedade]]
- [[Conhecimento-Geral/Neurociencia/INDEX|Neurociência Cognitiva]]
- [[Conhecimento-Geral/Linguistica/INDEX|Linguística e Semiótica]]
- [[Conhecimento-Geral/Matematica/INDEX|Matemática para IA]]
- [[Conhecimento-Geral/Tecnologia-e-Sociedade/INDEX|Tecnologia e Sociedade]]
- [[Conhecimento-Geral/Economia-Digital/INDEX|Economia, Trabalho e Sociedade Digital]]
- [[Conhecimento-Geral/Direito-Digital/INDEX|Direito e Regulação de IA]]

## Notas de conceito iniciais

- [[Conhecimento-Geral/Filosofia/Conceitos-Fundamentais|Conceitos Fundamentais de Filosofia]]
- [[Conhecimento-Geral/Filosofia/Filosofia-da-Mente|Filosofia da Mente]]
- [[Conhecimento-Geral/Filosofia/Chinese-Room|Quarto Chinês]]
- [[Conhecimento-Geral/Etica/Consequencialismo|Consequencialismo]]
- [[Conhecimento-Geral/Etica/Deontologia|Deontologia]]
- [[Conhecimento-Geral/Etica/Etica-das-Virtudes|Ética das Virtudes]]
- [[Conhecimento-Geral/Etica/Conceitos-de-Alinhamento|Conceitos de Alinhamento]]
- [[Conhecimento-Geral/Etica/Transparencia-Algoritmica|Transparência Algorítmica]]
- [[Conhecimento-Geral/Psicologia/Vieses-Cognitivos|Vieses Cognitivos e Comportamento]]
- [[Conhecimento-Geral/Psicologia/Vieses-em-LLMs|Vieses em LLMs]]
- [[Conhecimento-Geral/Psicologia/Teoria-da-Mente|Teoria da Mente]]
- [[Conhecimento-Geral/Neurociencia/Redes-Neurais-Biologicas|Redes Neurais Biológicas]]
- [[Conhecimento-Geral/Matematica/Algebra-Linear-Essencial|Álgebra Linear Essencial]]
- [[Conhecimento-Geral/Matematica/Calculo-e-Otimizacao|Cálculo e Otimização]]
- [[Conhecimento-Geral/Matematica/Probabilidade-e-Estatistica|Probabilidade e Estatística]]
- [[Conhecimento-Geral/Matematica/Teoria-da-Informacao|Teoria da Informação]]
- [[Conhecimento-Geral/Economia-Digital/Automacao-e-Desemprego|Automação e Desemprego]]
- [[Conhecimento-Geral/Direito-Digital/GDPR-e-Privacidade|GDPR e Privacidade]]
- [[Conhecimento-Geral/Direito-Digital/EU-AI-Act|EU AI Act]]
- [[Conhecimento-Geral/Linguistica/Linguistica-e-Semiotica|Linguística e Semiótica]]

## Sugestão de rotas de estudo

1. **Rota Filosófica** — Filosofia da Mente → Chinese Room → Qualia → Problema do Controle → Ética em IA
2. **Rota Cognitiva** — Psicologia Cognitiva → Vieses Cognitivos → Vieses em LLMs → Teoria da Mente → Neurociência
3. **Rota Técnica** — Álgebra Linear → Cálculo e Otimização → Probabilidade → Teoria da Informação → Linguística
4. **Rota Social** — Cultura → Economia Digital → Direito Digital → Tecnologia e Sociedade → Transparência Algorítmica

## Objetivo

Criar um índice semântico que facilite a construção de pipelines RAG e a geração de embeddings de alta qualidade.
