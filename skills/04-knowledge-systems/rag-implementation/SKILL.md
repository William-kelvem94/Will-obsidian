---
title: "RAG Implementation"
description: "Retrieval Augmented Generation for LLM knowledge systems"
tags: [rag, embeddings, semantic-search, vector-store, llm, knowledge-base, skills-knowledge]
updated: 2026-06-07
date: 2026-04-27
---

# RAG Implementation Skill

Complete guide to Retrieval Augmented Generation (RAG) for building LLM-powered knowledge systems.

---

## 🎯 What is RAG?

**RAG = Retrieval Augmented Generation**

Instead of relying only on LLM's training data:
1. **Retrieve** relevant documents from your knowledge base
2. **Augment** the LLM prompt with that context
3. **Generate** answer using both LLM knowledge + your documents

**Benefits:**
- ✅ Access to private/recent data not in training
- ✅ Reduce hallucinations (grounded in facts)
- ✅ Source attribution (know where answer came from)
- ✅ No retraining needed

---

## 🏗️ Architecture Overview

```
┌─────────────┐
│   Query     │ "What is JARVIS architecture?"
└──────┬──────┘
       │
       ▼
┌─────────────────────────────┐
│  1. Query Encoding          │
│  (sentence-transformers)    │ → [0.23, -0.45, 0.89, ...]
└──────┬──────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│  2. Vector Search (FAISS)   │
│  Find similar chunks        │ → Top 5 most relevant docs
└──────┬──────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│  3. Context Assembly        │
│  Format for LLM             │ → "Context: [doc1] [doc2]..."
└──────┬──────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│  4. LLM Generation (Ollama) │
│  Answer using context       │ → "JARVIS has 5-tier..."
└─────────────────────────────┘
```

---

## 📦 Components

### 1. Embeddings Generator
**Purpose:** Convert text → vector representations

**Implementation:** `skills/04-knowledge-systems/rag-pipeline/embeddings_generator.py`

**Key features:**
- Uses `sentence-transformers` (all-MiniLM-L6-v2 by default)
- Chunks documents (500 chars default)
- Caches embeddings (only regenerates changed files)
- MD5 hash tracking for changes

**Usage:**
```python
from embeddings_generator import EmbeddingsGenerator

generator = EmbeddingsGenerator(vault_path="./")
embeddings_data = generator.generate_embeddings()
generator.save_embeddings(embeddings_data)
```

**CLI:**
```bash
python embeddings_generator.py /path/to/vault --force
```

### 2. Vector Store
**Purpose:** Fast similarity search over embeddings

**Implementation:** `skills/04-knowledge-systems/rag-pipeline/vector_store.py`

**Key features:**
- FAISS (Facebook AI Similarity Search) backend
- Inner product search (cosine similarity)
- Index persistence (save/load)
- Chunk metadata tracking

**Usage:**
```python
from vector_store import VectorStore

store = VectorStore(dimension=384)
store.load_embeddings("embeddings.json.gz")
store.save_index("vault.index")

# Search
results = store.search("JARVIS architecture", model, top_k=5)
```

### 3. Query Engine
**Purpose:** Combine retrieval + generation

**Implementation:** `skills/04-knowledge-systems/rag-pipeline/query_engine.py`

**Key features:**
- Retrieval from vector store
- Context formatting for LLM
- Ollama integration for generation
- Source attribution
- Interactive mode

**Usage:**
```python
from query_engine import QueryEngine

engine = QueryEngine(index_path="vault.index")

result = engine.query(
    question="What is JARVIS?",
    top_k=5,
    use_llm=True,
    llm_model="llama3.1:8b"
)

print(result["answer"])
for source in result["sources"]:
    print(f"- {source['file']}")
```

**Interactive CLI:**
```bash
python query_engine.py --index vault.index --interactive
```

### 4. Knowledge Indexer (Automation)
**Purpose:** Keep index up to date automatically

**Implementation:** `.scripts/knowledge_indexer.py`

**Key features:**
- Full index build
- Incremental updates (only changed files)
- Watch mode (periodic updates)
- Index verification
- Statistics

**Usage:**
```bash
# Build initial index
python .scripts/knowledge_indexer.py --build

# Update (only changed files)
python .scripts/knowledge_indexer.py --update

# Watch mode (auto-update every 5 min)
python .scripts/knowledge_indexer.py --watch

# Stats
python .scripts/knowledge_indexer.py --stats
```

---

## 🚀 Quick Start Guide

### Step 1: Install Dependencies

```bash
pip install sentence-transformers faiss-cpu requests
```

**Optional (GPU acceleration):**
```bash
pip install faiss-gpu  # Instead of faiss-cpu
```

### Step 2: Build Initial Index

```bash
cd /path/to/vault
python .scripts/knowledge_indexer.py --build
```

This will:
- Generate embeddings for all `.md` files
- Build FAISS index
- Save to `.knowledge_index/`

### Step 3: Query the Knowledge Base

**Option A: Interactive mode**
```bash
cd skills/04-knowledge-systems/rag-pipeline
python query_engine.py --index ../../../.knowledge_index/vault.index --interactive
```

**Option B: Single query**
```bash
python query_engine.py \
  --index .knowledge_index/vault.index \
  --query "What is the vault structure?"
```

**Option C: Python API**
```python
from query_engine import QueryEngine

engine = QueryEngine(index_path=".knowledge_index/vault.index")

result = engine.query(
    question="How do I use RAG?",
    top_k=5,
    use_llm=True,
    stream=True
)
```

### Step 4: Keep Updated

**Manual update:**
```bash
python .scripts/knowledge_indexer.py --update
```

**Auto-update (watch mode):**
```bash
python .scripts/knowledge_indexer.py --watch --interval 300
```

---

## 📊 Configuration

### Embedding Models

| Model | Dimensions | Speed | Quality | Use Case |
|-------|-----------|-------|---------|----------|
| all-MiniLM-L6-v2 | 384 | Fast | Good | Default (balanced) |
| all-mpnet-base-v2 | 768 | Medium | Better | Higher quality |
| paraphrase-multilingual | 384 | Medium | Good | Multi-language |

**Change model:**
```bash
python .scripts/knowledge_indexer.py --build --model all-mpnet-base-v2
```

### Chunking Strategies

**Default:** 500 characters per chunk

**Adjust:**
```python
generator = EmbeddingsGenerator(vault_path="./")
chunks = generator.extract_chunks(file_path, chunk_size=1000)
```

**Best practices:**
- Small chunks (300-500): Better precision, more results
- Large chunks (1000-2000): More context, fewer results
- Hybrid: Split by headings + max size

### Retrieval Parameters

**top_k:** Number of chunks to retrieve
- Small (3-5): Fast, focused
- Large (10-20): More comprehensive, but noisy

**min_score:** Similarity threshold (0-1)
- High (0.5+): Only very relevant chunks
- Low (0.2-0.3): Cast wider net

```python
results = engine.retrieve(
    query="question",
    top_k=5,
    min_score=0.3
)
```

---

## 🎯 Optimization Tips

### 1. Chunk Size by Content Type

```python
# Documentation: smaller chunks
docs_chunks = generator.extract_chunks(file, chunk_size=400)

# Long articles: larger chunks
article_chunks = generator.extract_chunks(file, chunk_size=1000)
```

### 2. Filter by File Type

```python
# Only index specific directories
file_paths = list(vault_path.rglob("*.md"))
file_paths = [f for f in file_paths if "JARVIS" in str(f)]

embeddings_data = generator.generate_embeddings(file_paths=file_paths)
```

### 3. Use GPU for Large Vaults

```python
store = VectorStore(dimension=384)
store.create_index(use_gpu=True)  # Requires faiss-gpu
```

### 4. Hybrid Search (BM25 + Semantic)

Combine keyword search (BM25) with semantic search:

```python
# BM25 search (keyword-based)
keyword_results = bm25_search(query, top_k=10)

# Semantic search
semantic_results = vector_store.search(query, top_k=10)

# Combine scores
combined = merge_results(keyword_results, semantic_results)
```

### 5. Re-ranking

Use a cross-encoder to re-rank retrieved chunks:

```python
from sentence_transformers import CrossEncoder

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

# Get initial results
results = store.search(query, top_k=20)

# Re-rank
pairs = [[query, r["text"]] for r in results]
scores = reranker.predict(pairs)

# Sort by re-ranked scores
reranked = sorted(zip(results, scores), key=lambda x: x[1], reverse=True)
```

---

## 🐛 Common Issues

### Issue: "ImportError: sentence-transformers not found"

**Solution:**
```bash
pip install sentence-transformers
```

### Issue: "ImportError: faiss not found"

**Solution:**
```bash
pip install faiss-cpu  # CPU version
# Or
pip install faiss-gpu  # GPU version (requires CUDA)
```

### Issue: "CUDA out of memory"

**Solutions:**
1. Use CPU instead of GPU
2. Use smaller embedding model
3. Reduce batch size in encoding

```python
# Reduce batch size
embeddings = model.encode(texts, batch_size=8)  # Default is 32
```

### Issue: Slow index build

**Solutions:**
1. Use smaller/faster model (all-MiniLM-L6-v2)
2. Increase chunk size (fewer chunks)
3. Use incremental updates instead of full rebuild

### Issue: Poor quality results

**Solutions:**
1. Increase `top_k` (retrieve more chunks)
2. Lower `min_score` threshold
3. Use better embedding model (all-mpnet-base-v2)
4. Improve chunk boundaries (split by headings)
5. Add metadata filters

---

## 📚 Integration Patterns

### Pattern 1: Chat with Your Notes

```python
def chat_with_vault(engine, history=[]):
    """Conversational RAG with history"""
    
    user_message = input("You: ")
    
    # Include conversation history in retrieval
    context_query = " ".join(history[-3:] + [user_message])
    
    result = engine.query(
        question=user_message,
        context_query=context_query,  # Custom retrieval query
        use_llm=True,
        stream=True
    )
    
    history.append(user_message)
    history.append(result["answer"])
    
    return result["answer"]
```

### Pattern 2: Automatic Documentation Assistant

```python
def doc_assistant(code_snippet):
    """Find relevant docs for code"""
    
    query = f"Documentation for: {code_snippet}"
    
    results = engine.retrieve(query, top_k=3)
    
    # Filter only docs files
    docs_results = [r for r in results if "docs/" in r["file"]]
    
    return docs_results
```

### Pattern 3: Knowledge Graph Augmentation

```python
def hybrid_kg_rag(question):
    """Combine knowledge graph + RAG"""
    
    # 1. Query knowledge graph for entities
    entities = kg.query(question)
    
    # 2. Use entities to enhance retrieval
    expanded_query = f"{question} {' '.join(entities)}"
    
    # 3. RAG with expanded query
    result = engine.query(expanded_query)
    
    return result
```

---

## 🔗 Related Resources

- [[skills/03-infrastructure-mcp/local-llm-ops|Local LLM Ops]] — Ollama setup
- [[JARVIS/KnowledgeBase/SegundoCerebro|Segundo Cérebro]] — Knowledge management philosophy
- [[JARVIS/04-Engineering/Playbooks/Ollama-GPU-Issues|Ollama GPU Troubleshooting]]

---

## 📞 Next Steps

1. **Build your first index:**
   ```bash
   python .scripts/knowledge_indexer.py --build
   ```

2. **Try interactive mode:**
   ```bash
   cd skills/04-knowledge-systems/rag-pipeline
   python query_engine.py --index ../../../.knowledge_index/vault.index --interactive
   ```

3. **Set up auto-update:**
   - Add to startup script
   - Or run as systemd service (Linux)
   - Or Task Scheduler (Windows)

4. **Customize for your use case:**
   - Adjust chunk size
   - Filter specific directories
   - Add metadata enrichment
   - Implement hybrid search

---

*RAG transforms your vault from static notes into an intelligent knowledge system.*
