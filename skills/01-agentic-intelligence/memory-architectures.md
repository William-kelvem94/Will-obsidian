---
title: "Arquitetura de Memoria para Agentes: Episodica, Semantica e Trabalho"
description: "Guia profundo sobre como estruturar a memoria de longo e curto prazo para que agentes IA mantenham consistencia de identidade e contexto."
tags: [agentic, memory, rag, context, arquitetura, skills-ai, faiss, chroma]
updated: 2026-06-07
date: 2026-06-01
---

# Arquitetura de Memoria para Agentes Autonomos

A memoria e o que diferencia um "chatbot de sessao unica" de um "agente autonomo continuo" como o JARVIS. A arquitetura correta simula a cognicao humana atraves de tres pilares: Memoria de Trabalho, Memoria Semantica e Memoria Episodica.

## Diagrama de Arquitetura

```
[Usuario] -> [Working Memory (Contexto LLM)]
                  |
         [Retrieval Router]
            /            \
   [Semantic Memory]  [Episodic Memory]
   (FAISS/Chroma)     (JSON Logs + Insights)
            \            /
         [Consolidation Worker]
                  |
         [Long-Term Storage]
```

## 1. Memoria de Trabalho (Working Memory)

E a **Janela de Contexto** atual da LLM.

- **Definicao**: Tudo acessivel ao modelo durante a interacao (historico recente, system prompt, variaveis de ambiente).
- **Desafios**: Limitacao de tokens (128k Claude, 8k/32k modelos locais).
- **Gerenciamento**:
  - **Summarization**: Sub-agente resume conversa antiga e injeta como bloco condensado.
  - **Context Pruning**: Remocao ativa de logs de ferramentas apos uso.

```python
def manage_working_memory(conversation: list, max_tokens: int = 8000) -> list:
    total_tokens = sum(len(m["content"].split()) for m in conversation)
    if total_tokens > max_tokens:
        summary = summarize(conversation[:-3])
        return [{"role": "system", "content": f"Resumo anterior: {summary}"}] + conversation[-3:]
    return conversation
```

## 2. Memoria Semantica (Conhecimento Factual)

Armazena fatos e conhecimentos. E o nucleo do RAG.

### Schema de Banco Vetorial FAISS

```python
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class SemanticMemory:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.encoder = SentenceTransformer(model_name)
        self.dimension = self.encoder.get_sentence_embedding_dimension()
        self.index = faiss.IndexFlatL2(self.dimension)
        self.documents = []
        self.metadata = []

    def add_document(self, text: str, meta: dict):
        vector = self.encoder.encode([text])
        self.index.add(np.array(vector))
        self.documents.append(text)
        self.metadata.append(meta)

    def search(self, query: str, k: int = 3) -> list:
        query_vec = self.encoder.encode([query])
        distances, indices = self.index.search(np.array(query_vec), k)
        results = []
        for i, idx in enumerate(indices[0]):
            if idx != -1:
                results.append({
                    "document": self.documents[idx],
                    "metadata": self.metadata[idx],
                    "score": float(1 / (1 + distances[0][i]))
                })
        return results
```

### Schema de Banco Vetorial Chroma

```python
import chromadb
from chromadb.utils import embedding_functions

chroma_client = chromadb.PersistentClient(path="./memory_db")
collection = chroma_client.get_or_create_collection(
    name="jarvis_semantic",
    embedding_function=embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
)

def add_to_chroma(doc_id: str, text: str, metadata: dict):
    collection.add(
        documents=[text],
        metadatas=[metadata],
        ids=[doc_id]
    )

def search_chroma(query: str, n: int = 5) -> list:
    return collection.query(query_texts=[query], n_results=n)
```

### Algoritmos de Recuperacao

#### Busca por Similaridade (Vector Search)
```python
def vector_search(query, index, k=5):
    distances, indices = index.search(query, k)
    return indices
```

#### Maximum Marginal Relevance (MMR)
Equilibra relevancia e diversidade nos resultados:

```python
def mmr_search(query_vec, doc_vectors, lambda_param=0.7, k=5):
    selected = []
    candidates = list(range(len(doc_vectors)))
    query_norm = query_vec / np.linalg.norm(query_vec)

    for _ in range(k):
        mmr_scores = []
        for idx in candidates:
            sim = np.dot(query_norm, doc_vectors[idx] / np.linalg.norm(doc_vectors[idx]))
            div = max([np.dot(doc_vectors[idx], doc_vectors[s]) for s in selected], default=0)
            mmr = lambda_param * sim - (1 - lambda_param) * div
            mmr_scores.append(mmr)
        best = candidates[np.argmax(mmr_scores)]
        selected.append(best)
        candidates.remove(best)
    return selected
```

#### Busca Hibrida (Vector + BM25)

| Metodo | Vantagem | Desvantagem |
|--------|----------|-------------|
| Vector Search | Similaridade semantica | Perde termos exatos |
| BM25 | Precisao em keywords | Ignora sinonimos |
| Hibrido | Melhor dos dois mundos | Mais complexo |

```python
def hybrid_search(query, vector_index, bm25_index, alpha=0.5):
    vector_results = vector_search(query, vector_index, k=10)
    bm25_results = bm25_index.search(query, k=10)
    combined = {}
    for doc, score in vector_results:
        combined[doc] = combined.get(doc, 0) + alpha * score
    for doc, score in bm25_results:
        combined[doc] = combined.get(doc, 0) + (1 - alpha) * score
    return sorted(combined.items(), key=lambda x: x[1], reverse=True)[:5]
```

## 3. Memoria Episodica (Experiencia)

Registra eventos no tempo - o "diario" do agente.

```python
import json
from datetime import datetime

class EpisodicMemory:
    def __init__(self, log_path: str = "./episodic_logs.jsonl"):
        self.log_path = log_path

    def record(self, action: str, context: str, result: str, success: bool):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "context": context,
            "result": result,
            "success": success
        }
        with open(self.log_path, "a") as f:
            f.write(json.dumps(entry) + "\n")

    def recall_similar(self, action: str, limit: int = 5) -> list:
        episodes = []
        with open(self.log_path, "r") as f:
            for line in f:
                ep = json.loads(line)
                if action in ep["action"]:
                    episodes.append(ep)
        return episodes[-limit:]

    def extract_insights(self):
        failures = []
        with open(self.log_path, "r") as f:
            for line in f:
                ep = json.loads(line)
                if not ep["success"]:
                    failures.append(ep)
        return self._synthesize_lessons(failures)
```

## Fluxo Cognitivo Integrado

1. **Gatilho**: Usuario faz requisicao.
2. **Retrieval Router**:
   - Busca na Memoria Semantica (FAISS) por fatos relacionados.
   - Busca na Memoria Episodica por experiencias similares.
3. **Injecao**: Dados formatados e injetados na Working Memory.
4. **Geracao**: LLM responde ou age com contexto enriquecido.
5. **Consolidacao**: Novas licoes gravadas nas memorias de longo prazo.

```python
class AgentMemory:
    def __init__(self):
        self.working = WorkingMemory()
        self.semantic = SemanticMemory()
        self.episodic = EpisodicMemory()

    def process_query(self, query: str) -> str:
        semantic_ctx = self.semantic.search(query)
        episodic_ctx = self.episodic.recall_similar(query)
        enriched_prompt = self.working.inject_context(query, semantic_ctx, episodic_ctx)
        response = llm_generate(enriched_prompt)
        self.episodic.record("query", query, response, success=True)
        return response
```

## Referencias

- [[advanced-reasoning-patterns]] — Reflexion e aprendizado com erros.
- [[multi-agent-orchestration]] — Memoria compartilhada entre agentes.
- [[project-jarvis-prompts]] — Prompts de RAG e pipeline de memoria.
- [[mcp-operators]] — Operadores para leitura/escrita de arquivos de memoria.
