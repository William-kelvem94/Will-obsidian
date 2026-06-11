---
title: "Retrieval-Augmented Generation"
date: 2026-06-10
updated: 2026-06-10
type: concept
status: active
tags: [rag, retrieval, generation, ai]
summary: "Pattern of grounding generation in retrieved evidence and curated knowledge."
---

# Retrieval-Augmented Generation

RAG combines retrieval and generation so the model answers from evidence rather than memory alone.

## Key components

- source selection;
- chunking;
- embeddings;
- retrieval;
- reranking;
- synthesis;
- answer validation.

## Failure modes

- wrong source selected;
- chunks too large or too small;
- stale evidence;
- hallucinated synthesis;
- overconfidence without provenance.

