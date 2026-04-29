---
title: "Mapa do Conhecimento"
description: "MOC central para as áreas de conhecimento semântico do vault."
tags: [hub, conhecimento, moc]
updated: 2026-04-27
---

# 🌌 Mapa do Conhecimento

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
- [[Conhecimento-Geral/Matematica/INDEX|Matemática para IA]]
- [[Conhecimento-Geral/Economia-Digital/INDEX|Economia, Trabalho e Sociedade Digital]]
- [[Conhecimento-Geral/Direito-Digital/INDEX|Direito e Regulação de IA]]

## Notas de conceito iniciais

- [[Conhecimento-Geral/Filosofia/Conceitos-Fundamentais|Conceitos Fundamentais de Filosofia]]
- [[Conhecimento-Geral/Etica/Consequencialismo|Consequencialismo]]
- [[Conhecimento-Geral/Psicologia/Vieses-Cognitivos|Vieses Cognitivos e Comportamento]]
- [[Conhecimento-Geral/Neurociencia/Redes-Neurais-Biologicas|Redes Neurais Biológicas]]
- [[Conhecimento-Geral/Matematica/Algebra-Linear-Essencial|Álgebra Linear Essencial]]
- [[Conhecimento-Geral/Economia-Digital/Automacao-e-Desemprego|Automação e Desemprego]]
- [[Conhecimento-Geral/Direito-Digital/GDPR-e-Privacidade|GDPR e Privacidade]]

## Objetivo

Criar um índice semântico que facilite a construção de pipelines RAG e a geração de embeddings de alta qualidade.
