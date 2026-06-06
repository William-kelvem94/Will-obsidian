---
title: "Estratégias Avançadas de RAG (GraphRAG e Híbrido)"
description: "Análise profunda sobre como recuperar dados para IAs além do Vector Search tradicional."
tags: [rag, graphrag, hybrid-search, embeddings, reranking, chunking, self-rag, skills-knowledge]
date: 2026-04-27
updated: 2026-06-05
---

# Estratégias Avançadas de RAG (Retrieval-Augmented Generation)

O RAG "Vanilla" (apenas Vector Search) falha quando a resposta exige agregar conceitos de múltiplos documentos ou buscar palavras exatas. Precisamos de abordagens híbridas e inteligentes para transformar um sistema de busca em um verdadeiro orquestrador de conhecimento.

Este documento expande os conceitos de [[memory-management]] e se aprofunda em estratégias de retrieval de última geração.

## 1. Naive RAG vs Advanced RAG

### Naive RAG (O Problema)
O fluxo padrão: chunk → embed → store → retrieve → generate.

**Limitações críticas:**
- **Perda de contexto global:** Recupera apenas blocos isolados, sem visão do documento completo.
- **Chunking cego:** Corta textos a cada N caracteres sem considerar semântica.
- **Falta de re-ranqueamento:** Assume que os top-k resultados do embedding são sempre os melhores.
- **Sem tratamento de consultas complexas:** Perguntas multi-parte ou comparativas falham.

### Advanced RAG (A Solução)
Adiciona camadas de pré-processamento, pós-processamento e orquestração:

```python
class AdvancedRAGPipeline:
    def __init__(self):
        self.retriever = HybridRetriever()
        self.reranker = CrossEncoderReranker()
        self.query_transformer = QueryTransformer()
    
    def query(self, user_question: str) -> str:
        # 1. Transformação da query
        queries = self.query_transformer.expand(user_question)
        
        # 2. Retrieval híbrido
        candidates = []
        for q in queries:
            candidates.extend(self.retriever.search(q))
        
        # 3. Reranking
        ranked = self.reranker.rerank(user_question, candidates)
        
        # 4. Geração com contexto
        return self.generate(ranked[:5])
```

## 2. Chunking Estratégico

A qualidade do RAG começa na divisão dos documentos. Um chunk mal feito destrói a recuperação.

### Chunking Recursivo
Divide o texto hierarquicamente, respeitando a estrutura natural:

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    separators=["\n## ", "\n### ", "\n\n", "\n", ". ", " ", ""],
    chunk_size=512,
    chunk_overlap=128,
    length_function=len,
)
```

### Chunking Semântico (Embedding-Based)
Detecta mudanças de tópico usando embeddings:

```python
def semantic_chunking(text: str, threshold: float = 0.3) -> list[str]:
    sentences = split_sentences(text)
    chunks = []
    current_chunk = [sentences[0]]
    
    for i in range(1, len(sentences)):
        emb_prev = embed(sentences[i-1])
        emb_curr = embed(sentences[i])
        similarity = cosine_similarity(emb_prev, emb_curr)
        
        if similarity < threshold:  # Mudança de tópico
            chunks.append(" ".join(current_chunk))
            current_chunk = []
        current_chunk.append(sentences[i])
    
    return chunks
```

### Agentic Chunking
O próprio LLM decide onde e como dividir:

```python
def agentic_chunk(document: str) -> list[dict]:
    prompt = f"""Analise este documento e divida em chunks semânticos.
    Para cada chunk, retorne:
    - content: texto do chunk
    - summary: resumo de 1 frase
    - topics: lista de tópicos
    - entities: entidades mencionadas
    
    Documento: {document[:8000]}"""
    
    response = llm_generate(prompt, response_format={"type": "json_object"})
    return json.loads(response)["chunks"]
```

## 3. Query Transformation

Antes de buscar, transforme a pergunta do usuário em múltiplas queries otimizadas.

### HyDE (Hypothetical Document Embedding)
Gere um documento hipotético que responderia à pergunta, e use *esse* documento para buscar:

```python
def hyde_query(question: str) -> list[float]:
    # Gera uma resposta hipotética
    hypothetical = llm_generate(
        f"Write a paragraph that answers: {question}"
    )
    # Embed a resposta, não a pergunta
    return embed(hypothetical)
```

### Multi-Query
Expanda a pergunta original em múltiplas variações:

```python
def multi_query_expansion(question: str) -> list[str]:
    prompt = f"""Generate 5 different versions of this question 
    that capture different aspects. Return as JSON list.
    
    Question: {question}"""
    
    variants = llm_generate(prompt)
    return [question] + json.loads(variants)
```

### Step-Back Prompting
Para perguntas específicas, primeiro faça uma pergunta mais geral:

```python
def step_back(question: str) -> tuple[str, str]:
    step_back_q = llm_generate(
        f"What broader concept or principle is needed to answer: {question}"
    )
    return step_back_q, question
```

## 4. Reranking (Re-ranqueamento)

O embedding inicial é rápido mas impreciso. O reranker faz uma segunda passagem mais criteriosa.

### Cross-Encoder Reranker
Processa pares (query, documento) e pontua a relevância:

```python
from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(query: str, candidates: list[str], top_k: int = 5):
    pairs = [[query, doc] for doc in candidates]
    scores = model.predict(pairs)
    ranked = sorted(zip(candidates, scores), key=lambda x: x[1], reverse=True)
    return [doc for doc, score in ranked[:top_k]]
```

### Cohere Rerank
API gerenciada com modelos especializados:

```python
import cohere

co = cohere.Client("api-key")

results = co.rerank(
    model="rerank-english-v3.0",
    query="What is the best RAG strategy?",
    documents=candidates,
    top_n=5
)
```

### RRF (Reciprocal Rank Fusion)
Combina múltiplos rankings sem treino:

```python
def rrf(rankings: list[list[str]], k: int = 60) -> list[str]:
    scores = {}
    for ranking in rankings:
        for rank, doc_id in enumerate(ranking):
            scores[doc_id] = scores.get(doc_id, 0) + 1 / (k + rank)
    return sorted(scores, key=scores.get, reverse=True)
```

## 5. Hybrid Search

Combina o melhor da busca semântica (entende intenção) com a busca lexical (precisão de termos).

### Dense + Sparse (BM25)

```python
class HybridRetriever:
    def __init__(self):
        self.dense_index = FAISSIndex()  # Embeddings
        self.sparse_index = BM25Index()  # Term frequency
    
    def search(self, query: str, alpha: float = 0.5):
        dense_results = self.dense_index.search(query)
        sparse_results = self.sparse_index.search(query)
        
        return rrf([dense_results, sparse_results])
```

### Elasticsearch + Vector
Configure um índice híbrido no Elasticsearch:

```json
{
  "mappings": {
    "properties": {
      "content": {"type": "text"},
      "content_vector": {
        "type": "dense_vector",
        "dims": 768,
        "index": true,
        "similarity": "cosine"
      }
    }
  }
}
```

```python
# Query híbrida via Elasticsearch
query = {
    "size": 10,
    "query": {
        "script_score": {
            "query": {"match": {"content": search_term}},
            "script": {
                "source": "cosineSimilarity(params.query_vector, 'content_vector') + 1.0",
                "params": {"query_vector": query_emb}
            }
        }
    }
}
```

## 6. GraphRAG

Criado pela Microsoft, o [[memory-management#Graph-Based Memory|GraphRAG]] combina Grafos de Conhecimento com RAG.

### Como Funciona
1. **Extração de Entidades:** O LLM lê cada chunk e extrai entidades e relacionamentos.
2. **Construção do Grafo:** Cria nós (entidades) e arestas (relacionamentos).
3. **Comunidades:** Agrupa nós em comunidades usando algoritmos como Leiden.
4. **Sumarização:** Gera resumos para cada comunidade.
5. **Consulta:** Para responder, navega pelas comunidades relevantes.

### Implementação com NetworkX + LLM

```python
import networkx as nx

G = nx.Graph()

def extract_entities_and_relations(text: str) -> tuple:
    prompt = f"""Extract entities and relations from:
    {text}
    
    Return JSON: {{"entities": [{{"name": ..., "type": ...}}],
    "relations": [{{"source": ..., "target": ..., "type": ...}}]}}"""
    
    result = json.loads(llm_generate(prompt))
    return result["entities"], result["relations"]

# Populate graph
for chunk in chunks:
    entities, relations = extract_entities_and_relations(chunk)
    for ent in entities:
        G.add_node(ent["name"], type=ent["type"])
    for rel in relations:
        G.add_edge(rel["source"], rel["target"], type=rel["type"])

# Query traversal
def graphrag_query(question: str, G: nx.Graph, top_k: int = 10):
    entities_in_question = extract_key_entities(question)
    
    # Find relevant subgraph
    subgraph_nodes = set()
    for entity in entities_in_question:
        if entity in G:
            subgraph_nodes.add(entity)
            subgraph_nodes.update(nx.neighbors(G, entity))
    
    subgraph = G.subgraph(subgraph_nodes)
    community_summaries = summarize_communities(subgraph)
    
    return llm_generate(f"Question: {question}\nContext: {community_summaries}")
```

### No Obsidian
Os links `[[Wiki]]` formam nativamente um GraphRAG! Ao usar o vault como RAG, o orquestrador deve ler também os backlinks. Veja [[obsidian-neural-vault]] para detalhes.

## 7. Self-RAG

O modelo decide quando e como buscar informação, refletindo sobre a própria relevância.

```python
def self_rag(question: str) -> str:
    # 1. O modelo decide se precisa buscar
    need_retrieval = llm_generate(
        f"Can you answer '{question}' from internal knowledge? (yes/no)"
    )
    
    if need_retrieval.lower() == "no":
        return llm_generate(question)  # Resposta direta
    
    # 2. Busca
    docs = retrieve(question)
    
    # 3. Avalia relevância de cada documento
    relevant_docs = []
    for doc in docs:
        is_relevant = llm_generate(
            f"Is this relevant to '{question}'? {doc[:500]} (yes/no)"
        )
        if is_relevant.lower() == "yes":
            relevant_docs.append(doc)
    
    # 4. Gera resposta com citações
    return generate_with_citations(question, relevant_docs)
```

## 8. Corrective RAG (CRAG)

Quando a busca retorna resultados ruins, o sistema tenta corrigir ou rejeitar:

```python
def corrective_rag(question: str) -> str:
    docs = retrieve(question)
    
    # Avaliação da qualidade dos documentos
    quality = evaluate_quality(question, docs)
    
    if quality == "high":
        return generate(question, docs)
    elif quality == "medium":
        # Tenta corrigir com busca na web
        web_results = web_search(question)
        return generate(question, docs + web_results)
    else:
        # Rejeita e tenta gerar sem contexto
        return generate(question, [])
```

## 9. RAPTOR (Recursive Abstractive Processing)

Constrói uma árvore de sumários em múltiplos níveis de abstração:

```python
def raptor_build(chunks: list[str], levels: int = 3):
    tree = [chunks]  # Nível 0: chunks originais
    
    for level in range(1, levels + 1):
        previous = tree[level - 1]
        # Agrupa chunks similares
        clusters = cluster_by_similarity(previous)
        # Sumariza cada cluster
        summaries = [llm_summarize(cluster) for cluster in clusters]
        tree.append(summaries)
    
    return tree

def raptor_query(tree: list[list[str]], question: str) -> str:
    # Busca do topo da árvore para baixo
    for level in reversed(range(len(tree))):
        relevant = retrieve_from_level(tree[level], question)
        if relevant:
            return generate(question, relevant)
    return generate(question, tree[0])
```

## 10. Avaliação de RAG

### Métricas-Chave
- **Faithfulness:** A resposta é fiel ao contexto recuperado?
- **Answer Relevance:** A resposta responde à pergunta?
- **Context Precision:** O contexto recuperado é todo relevante?
- **Context Recall:** Todo contexto relevante foi recuperado?

### Framework de Testes (RAGAS)

```python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy

dataset = {
    "question": [...],
    "answer": [...],
    "contexts": [...],
    "ground_truth": [...]
}

scores = evaluate(dataset, metrics=[faithfulness, answer_relevancy])
```

## Boas Práticas

1. **Nunca confie em um único método de retrieval.** Sempre combine dense + sparse.
2. **Avalie seu chunking.** Teste diferentes estratégias e meça o hit rate.
3. **Reranking é obrigatório** para produção. O custo computacional compensa em precisão.
4. **Documente seus pipelines** como [[rag-implementation/SKILL.md|SKILLs]] reutilizáveis.
5. **Monitore latências:** Retrieval deve ficar abaixo de 500ms. Reranking + geração podem chegar a 5s.

## Ferramentas MCP Recomendadas

- `hybrid_search(query, index_name, top_k)` — Busca combinada densa + esparsa.
- `graph_query(query, graph_name)` — Navegação no grafo de conhecimento.
- `rerank(query, documents)` — Re-ranqueamento com cross-encoder.
- `evaluate_rag(response, context, ground_truth)` — Avaliação de qualidade da resposta.

---

*Consulte também: [[memory-management]], [[obsidian-neural-vault]], [[01-agentic-intelligence/memory-architectures|Memory Architectures]].*
