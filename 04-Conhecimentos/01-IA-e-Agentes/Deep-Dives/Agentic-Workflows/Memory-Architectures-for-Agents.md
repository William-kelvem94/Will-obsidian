---
type: technical-deep-dive
category: agentic-workflows
tags: [memory, rag, vector-db, context-window]
links: 
  - "[[01-IA-e-Agentes/README]]"
  - "[[02-Engenharia-de-Software]]"
---

# Memory Architectures for Agents

Effective agentic behavior requires a sophisticated approach to information persistence and retrieval, mimicking human cognitive structures.

## 1. Episodic vs. Semantic Memory

### Episodic Memory (The "What Happened")
- **Definition**: A chronological record of interactions, tool outputs, and decision paths.
- **Implementation**: Append-only logs or time-series databases.
- **Usage**: Allows the agent to reflect on past mistakes ("I tried X, but it failed with error Y") and avoid repetitive loops.

### Semantic Memory (The "What is Known")
- **Definition**: Structured knowledge about the world, facts, and concepts.
- **Implementation**: Knowledge graphs (KG) or dense vector embeddings.
- **Usage**: Providing the agent with foundational truths that do not change based on the current session.

## 2. Vector DB Integration
Vector databases enable the storage and retrieval of high-dimensional embeddings of text or data.

### Retrieval Strategies
- **Cosine Similarity**: Measuring the angle between the query vector and document vectors.
- **Maximum Inner Product Search (MIPS)**: Optimizing for high-speed retrieval in massive datasets.
- **Hybrid Search**: Combining keyword-based (BM25) search with dense vector retrieval to handle both exact matches and conceptual similarities.

## 3. Long-term Context Management

### RAG (Retrieval-Augmented Generation)
- **Mechanism**: Dynamically injecting relevant snippets of external data into the prompt based on a query.
- **Pros**: Virtually infinite knowledge base, verifiable citations.
- **Cons**: "Lost in the Middle" phenomenon where LLMs ignore information in the center of long prompts.

### Long-Context Windows
- **Mechanism**: Utilizing models with native support for millions of tokens (e.g., Gemini 1.5 Pro).
- **Pros**: Full architectural awareness, no retrieval errors, deep coherence.
- **Cons**: High inference cost, linear or quadratic increase in latency, potential for attention dilution.

### Comparison Matrix

| Feature | RAG | Long-Context |
| :--- | :--- | :--- |
| **Capacity** | Terabytes of data | ~1-10M tokens |
| **Precision** | High (if retrieval is good) | Absolute (all data present) |
| **Latency** | Fast (small prompt) | Slow (massive prompt) |
| **Cost** | Lower per token | Higher per prompt |
