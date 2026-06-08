---
title: "Gestão de Memória Long-Term (LTM)"
description: "Padrões de persistência de contexto em bancos de dados vetoriais para continuidade de sessão em agentes de IA."
tags: [memory, long-term-memory, vector-db, chromadb, pinecone, faiss, weaviate, skills-knowledge]
date: 2026-04-27
updated: 2026-06-07
---

# Gestão de Memória Long-Term (LTM)

Para um agente como o [[02-JARVIS/JARVIS/Main|JARVIS]] ter "personalidade" ou "consciência contínua", ele precisa lembrar de sessões antigas que já saíram da *janela de contexto*. A memória em sistemas de IA é um dos componentes mais críticos para construir agentes verdadeiramente inteligentes e contínuos.

A memória de longa duração (LTM) é o que separa um chatbot stateless de um assistente pessoal que conhece sua história, preferências e projetos.

## O Fluxo de Persistência

### 1. Captura de Sessão
Toda interação entre o usuário e o agente precisa ser registrada em um buffer de memória de trabalho (working memory). Esse buffer mantém o histórico completo da conversa atual.

### 2. Compressão e Summarização
Ao final de cada sessão — ou quando o buffer atinge um limite — um script de background roda um LLM menor (como `llama3.2:3b` local ou `gpt-4o-mini`) para resumir a sessão:

```python
# Exemplo de summarization worker
from openai import OpenAI
import chromadb

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def summarize_session(conversation_log: str, user_id: str) -> dict:
    response = client.chat.completions.create(
        model="llama3.2:3b",
        messages=[{
            "role": "system",
            "content": "Resuma a sessão em 3-5 frases. Extraia: \
                        (1) O que foi feito, \
                        (2) Decisões tomadas, \
                        (3) Tópicos importantes, \
                        (4) Sentimento do usuário. \
                        Formato JSON."
        }, {
            "role": "user",
            "content": conversation_log
        }],
        response_format={"type": "json_object"}
    )
    return response.choices[0].message.content
```

### 3. Geração de Embeddings
O resumo é então transformado em um vetor numérico usando um modelo de embedding:

```python
def generate_embedding(text: str) -> list[float]:
    response = client.embeddings.create(
        model="nomic-embed-text",
        input=text
    )
    return response.data[0].embedding
```

### 4. Armazenamento com Metadados Ricos
O vetor é salvo em um banco vetorial com metadados que permitem filtragem precisa:

```python
collection = chromadb_client.get_or_create_collection(
    name="session_memories",
    metadata={"hnsw:space": "cosine"}
)

collection.add(
    embeddings=[embedding],
    documents=[summary],
    metadatas=[{
        "user_id": "will",
        "date": "2026-05-16",
        "project": "JARVIS",
        "session_type": "development",
        "tokens_used": 4523,
        "mood": "productive",
        "tags": ["bug-fix", "python", "refactoring"]
    }],
    ids=["session_20260516_001"]
)
```

## Tipos de Memória em Sistemas de IA

Inspirado na neurociência cognitiva, classificamos a memória de agentes em quatro categorias principais.

### Memória de Trabalho (Working Memory)
Corresponde ao contexto imediato da conversa — o que está dentro da **janela de contexto** do LLM.

- **Capacidade limitada:** Tipicamente 8K-200K tokens dependendo do modelo.
- **Gerenciamento:** Técnicas como [[01-agentic-intelligence/memory-architectures|Memory Architectures]] e sliding window.
- **Estratégia:** Manter apenas os turnos mais recentes, sumarizar os antigos.

```python
class WorkingMemory:
    def __init__(self, max_tokens: int = 128000):
        self.max_tokens = max_tokens
        self.buffer = []
    
    def add_message(self, message: dict):
        self.buffer.append(message)
        self._trim_context()
    
    def _trim_context(self):
        total = sum(len(m["content"].split()) for m in self.buffer)
        while total > self.max_tokens and len(self.buffer) > 1:
            oldest = self.buffer.pop(0)
            total -= len(oldest["content"].split())
```

### Memória Episódica
Armazena experiências passadas — sessões anteriores, interações específicas, eventos.

- **Chave:** `(timestamp, user_id, session_id)`
- **Recuperação:** Por similaridade semântica ou por data.
- **Uso típico:** "Lembrar" de um bug que foi resolvido há duas semanas.

### Memória Semântica
Conhecimento factual e conceitual extraído de múltiplas experiências.

- **Chave:** Conceitos, entidades, relacionamentos.
- **Armazenamento:** Preferencialmente em [[advanced-rag-strategies|GraphRAG]] ou bancos de conhecimento.
- **Uso típico:** Saber que "a API do OpenAI usa tokens por minuto como limite de rate".

### Memória Procedural
Como fazer as coisas — sequências de ações, workflows, instruções.

- **Chave:** Nome da skill, trigger, steps.
- **Armazenamento:** Arquivos de skill (como `SKILL.md`), scripts, funções.
- **Uso típico:** Executar o workflow de deploy de uma skill MCP.

## Bancos de Dados Vetoriais

### ChromaDB (Embedded + Server)
Ideal para desenvolvimento local e prototipagem rápida.

```python
import chromadb

# Modo cliente-servidor para produção
chroma_client = chromadb.HttpClient(host="localhost", port=8000)

collection = chroma_client.get_or_create_collection("memories")

# Busca híbrida com filtro de metadados
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5,
    where={"user_id": "will"},
    where_document={"$contains": "bug"}
)
```

### FAISS (Facebook AI Similarity Search)
Biblioteca de busca vetorial de alto desempenho da Meta. Ideal para operações em memória.

```python
import faiss
import numpy as np

dimension = 768  # nomic-embed-text
index = faiss.IndexFlatIP(dimension)  # Inner Product = Cosine Similarity normalizada

# Adicionar vetores
vectors = np.array(all_embeddings).astype('float32')
index.add(vectors)

# Busca
D, I = index.search(query_vector, k=5)  # Distâncias e Índices
```

### Pinecone (Managed Cloud)
Serviço gerenciado com escalabilidade horizontal. Oferece索引 podados automáticos e replicação.

```python
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key="pc-sk-...")

index = pc.Index("jarvis-memory")

# Upsert com metadados
index.upsert(
    vectors=[{
        "id": "session_001",
        "values": embedding,
        "metadata": {"user": "will", "project": "jarvis"}
    }]
)

# Query com filtro
results = index.query(
    vector=query_embedding,
    filter={"project": "jarvis"},
    top_k=10
)
```

### Weaviate (Graph + Vector)
Banco que combina grafos com vetores, permitindo buscas relacionais complexas.

```python
import weaviate

client = weaviate.Client("http://localhost:8080")

response = client.query.get(
    "Memory", ["summary", "date", "project"]
).with_near_vector({
    "vector": query_embedding
}).with_where({
    "path": ["project"],
    "operator": "Equal",
    "valueString": "jarvis"
}).with_limit(5).do()
```

## Estratégias de Memória Avançadas

### Summarization em Pirâmide
Em vez de resumir tudo em um único passo, use múltiplos níveis de abstração:

1. **Micro-resumos:** A cada 10 turnos, gere um resumo do bloco.
2. **Meso-resumos:** Combine micro-resumos do dia.
3. **Macro-resumos:** Combine meso-resumos da semana.

```python
def pyramidal_summarize(session_logs: list[str], levels: int = 3) -> str:
    current = session_logs
    for level in range(levels):
        summaries = []
        for batch in chunks(current, 5):
            summary = llm_summarize(batch)
            summaries.append(summary)
        current = summaries
    return current[0]  # Resumo final
```

### Reflexão (Reflection Pattern)
O agente não apenas armazena, mas reflete sobre o que aprendeu:

```python
def reflect_on_memories(relevant_memories: list[str]) -> str:
    prompt = f"""Analise estas memórias e extraia:
    1. Padrões recorrentes
    2. Preferências do usuário
    3. Lições aprendidas
    4. Sugestões para o futuro
    
    Memórias: {relevant_memories}"""
    
    return llm_generate(prompt)
```

### Retrieval-Augmented Generation (RAG)
A base de todo sistema moderno de memória. Veja [[advanced-rag-strategies]] para estratégias avançadas.

## Graph-Based Memory

### Integração com Grafos de Conhecimento
Memórias não são apenas vetores — elas formam uma teia de relacionamentos.

```python
# Representação de memória em grafo
memory_graph = {
    "nodes": [
        {"id": "session_1", "type": "session", "label": "Debugging Python bug"},
        {"id": "bug_42", "type": "issue", "label": "Null pointer in parser"},
        {"id": "skill_rag", "type": "knowledge", "label": "Advanced RAG patterns"}
    ],
    "edges": [
        {"from": "session_1", "to": "bug_42", "label": "addressed"},
        {"from": "session_1", "to": "skill_rag", "label": "referenced"}
    ]
}
```

No [[01-agentic-intelligence/advanced-workflows|Advanced Workflows]], o agente pode navegar esse grafo para encontrar conexões não óbvias.

## Memória em LLMs

### Context Window Interna
Onde tudo acontece em tempo real. Modelos modernos como Gemini 1.5 Pro (2M tokens) e Claude 3 (200K tokens) expandiram drasticamente essa capacidade.

### KV Cache
Mecanismo que acelera a inferência ao cachear as chaves e valores de atenção. A quantização do KV cache reduz uso de VRAM em até 50%.
- Ver [[03-infrastructure-mcp/local-llm-ops|Local LLM Ops]] para detalhes de otimização.

### Cache Semântico
Em vez de reprocessar perguntas similares, use um cache de embeddings:

```python
class SemanticCache:
    def __init__(self, threshold: float = 0.95):
        self.cache = {}
        self.threshold = threshold
    
    def get(self, query: str) -> str | None:
        query_emb = embed(query)
        for cached_q, cached_a in self.cache.items():
            cached_emb = embed(cached_q)
            similarity = cosine_similarity(query_emb, cached_emb)
            if similarity > self.threshold:
                return cached_a
        return None
```

## Boas Práticas

1. **Tiered Storage:** Memórias recentes em RAM/FAISS, antigas em ChromaDB/Pinecone, archive em blob storage.
2. **Data Retention Policy:** Defina TTL (time-to-live) para memórias por tipo (ex: memórias episódicas expiram em 90 dias, semânticas em 1 ano).
3. **Privacy First:** Memórias devem ser criptografadas por usuário. Use `user_id` como partition key.
4. **Feedback Loop:** Permita que o usuário edite ou delete memórias. Implemente "esquecimento" via delete lógico.
5. **Batching:** Acumule memórias em lotes para reduzir custos de embedding e storage I/O.

## Métricas de Saúde

- **Hit Rate:** % de vezes que uma memória relevante é encontrada (target: >80%).
- **Latência P95:** Tempo de retrieval (target: <200ms para memórias recentes).
- **Precisão:** Relevância dos resultados retornados.
- **Cobertura:** % de sessões que geraram memórias persistidas.

## Ferramentas MCP Recomendadas

- `vector_search(memory, query, limit)` — Busca semântica no banco vetorial.
- `store_memory(user_id, content, metadata)` — Persiste uma nova memória.
- `reflect_on_session(session_id)` — Dispara reflexão pós-sessão.
- `get_recent_context(user_id, n_days)` — Recupera contexto para continuidade.

---

*Este documento integra-se com [[advanced-rag-strategies]], [[01-agentic-intelligence/memory-architectures|Memory Architectures]], e [[obsidian-neural-vault]].*
