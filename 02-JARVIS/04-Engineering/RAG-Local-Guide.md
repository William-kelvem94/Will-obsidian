---
title: "RAG Local – Como Consultar o Cérebro"
tags: [rag, embeddings, internals, agente, jarvis-engenharia]
date: 2026-04-27
updated: 2026-06-10
---

# 🔍 Retrieval Augmented Generation Local

## O que é
Usa o índice FAISS em `.scripts/index/` para buscar semanticamente no vault.

## Como ativar (Agente Externo)
1. Carregue o modelo `all-MiniLM-L6-v2` (SentenceTransformers).
2. Carregue o índice FAISS com `faiss.read_index(...)`.
3. Para cada prompt:
   - Gere embedding da consulta.
   - Busque os top-k vizinhos no índice.
   - Recupere os trechos correspondentes no vault.
   - Injete no contexto do prompt.

## Localização dos arquivos
- Índice: `.scripts/index/faiss_index.bin`
- Metadados: `.scripts/index/metadata.json`
- Modelo usado: `all-MiniLM-L6-v2` (384 dimensões)

## Exemplo mínimo (Python)
```python
from sentence_transformers import SentenceTransformer
import faiss, json

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index('.scripts/index/faiss_index.bin')
with open('.scripts/index/metadata.json', 'r', encoding='utf-8') as f:
    meta = json.load(f)

def search(query, top_k=3):
    emb = model.encode([query])
    D, I = index.search(emb, top_k)
    return [meta[i]['file'] for i in I[0]]
```

[[02-JARVIS/README|← Voltar ao Command Center]]
