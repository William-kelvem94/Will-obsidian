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

## Notas de conceito iniciais

- [[Conhecimento-Geral/Filosofia/Conceitos-Fundamentais|Conceitos Fundamentais de Filosofia]]
- [[Conhecimento-Geral/Etica/Consequencialismo|Consequencialismo]]
- [[Conhecimento-Geral/Psicologia/Vieses-Cognitivos|Vieses Cognitivos e Comportamento]]

## Objetivo

Criar um índice semântico que facilite a construção de pipelines RAG e a geração de embeddings de alta qualidade.
