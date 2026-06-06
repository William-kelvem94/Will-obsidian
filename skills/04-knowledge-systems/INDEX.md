---
title: "Sistemas de Conhecimento e RAG Avancado"
description: "Hub central para sistemas de gestao de conhecimento, pipelines RAG modernos (GraphRAG, Hibrido) e gestao de memoria."
tags: [knowledge-systems, rag, memoria, hub, skills-knowledge]
date: 2026-04-27
updated: 2026-06-05
---

# Sistemas de Conhecimento (Knowledge Systems)

O armazenamento e a recuperacao de conhecimento sao o coracao de um agente de IA. Sem isso, o LLM e apenas uma calculadora de palavras — precisa de contexto, memoria e fontes confiaveis para gerar respostas uteis. Este hub conecta a teoria dos sistemas de conhecimento a implementacao pratica, desde o segundo cerebro no Obsidian ate pipelines de RAG em producao.

## Taxonomia do Conhecimento

| Tipo | Descricao | Exemplo | Implementacao |
|------|-----------|---------|---------------|
| **Memoria Episodica** | Eventos e experiencias especificas | "Usuario pediu para criar API de usuarios em 15/05" | Banco vetorial com timestamp |
| **Memoria Semantica** | Fatos e conceitos gerais | "FastAPI usa Pydantic para validacao" | Grafos de conhecimento |
| **Memoria Procedural** | Habilidades e pads | "Como criar um deployment no K8s" | MCP tools e scripts |
| **Conhecimento Explicito** | Documentos estruturados | "Manual de arquitetura do JARVIS" | Vault Obsidian com frontmatter |
| **Conhecimento Tacito** | Inferido de pads de uso | "Usuario prefere exemplos tipo Rust" | Analytics e feedback loops |

## Arquitetura do Sistema

```
Entrada (Query/Comando)
    |
    v
[Query Engine] -- reescrita, decomposicao, HyDE
    |
    v
[Router de Recuperacao]
    |--- Busca Vetorial (pgvector/FAISS)
    |--- Busca Lexical (BM25/FTS)
    |--- Grafo de Conhecimento (GraphRAG)
    |
    v
[Fusao / Re-ranking] -- RRF, Cross-encoder
    |
    v
[Injecao no Contexto] -- Prompt + Memoria + Chunks
    |
    v
[LLM] -- Geracao fundamentada
```

## Componentes do Sistema

### 1. Obsidian Vault (Fonte Primaria)
O vault do Obsidian funciona como banco de dados de conhecimento semi-estruturado. Cada nota contem:
- **Frontmatter** com metadados (tags, data, nivel, projetos)
- **Wiki-links** para criar um grafo de conhecimento navegavel
- **Conteudo semantico** em markdown, ideal para chunking

### 2. Pipeline de RAG (Motor de Recuperacao)
O pipeline transforma notas estaticas em contexto dinamico para o LLM. Componentes principais:
- **Chunking semantico**: Divide documentos por fronteiras semanticas (paragrafos, secoes)
- **Embeddings**: Converte chunks em vetores (text-embedding-3-small, 1536d)
- **Indice vetorial**: Armazena e busca vetores (pgvector HNSW ou FAISS)
- **Re-ranking**: Refina resultados com cross-encoder
- **Fusao**: Combina resultados de multiplas estrategias (RRF)

### 3. Gestao de Memoria (Persistencia de Estado)
Sistema de memoria de longo prazo que permite ao agente:
- Lembrar interacoes passadas (memoria episodica)
- Acumular conhecimento (memoria semantica)
- Executar habilidades automaticamente (memoria procedural)

## Notas Principais

### [[obsidian-neural-vault|Obsidian Neural Vault]]
A base do "Segundo Cerebro" — um vault do Obsidian projetado para ser o sistema de conhecimento central de um agente de IA. Aborda arquitetura do vault: estrutura de pastas (Conhecimento-Geral, JARVIS, skills), convencoes de nomenclatura, wiki-links para grafo navegavel, frontmatter estruturado para metadados, estrategias de tagging, MOCs (Maps of Content) e a distincao entre notas atomicas e notas-indice. Explica como o vault funciona como um banco de dados de conhecimento semi-estruturado que alimenta o pipeline de RAG do JARVIS, com cada nota servindo como um chunk semanticamente rico.

### [[advanced-rag-strategies|Estrategias Avancadas de RAG]]
Alem do RAG ingenuo ("buscar + colocar no prompt"), esta nota explora estrategias de ponta: GraphRAG (Microsoft) — que constroi um grafo de conhecimento e usa navegacao em grafo para perguntas que exigem sintese; chunking semantico por fronteiras semanticas; busca hibrida combinando BM25 com busca vetorial usando RRF (Reciprocal Rank Fusion); re-ranking com cross-encoder; query rewriting e query decomposition para perguntas complexas; HyDE (Hypothetical Document Embeddings); multi-hop RAG para perguntas que exigem multiplas rodadas; e agentes RAG que decidem dinamicamente quais fontes consultar.

### [[memory-management|Gestao de Memoria Long-Term]]
Estrutura de bancos vetoriais para memoria persistente de agentes de IA. Cobre: modelagem de memoria episodica vs. semantica vs. procedural (inspirada na neurociencia), estrategias de indexacao vetorial (HNSW, IVFFlat no pgvector), forgetting mechanisms (LRU, importancia temporal), consolidation (sumarizacao noturna de memorias episodicas em semanticas), memory retrieval com recency, relevance e importance scoring, e integracao com o pipeline RAG para fornecer ao LLM um contexto continuo e evolutivo. Inclui exemplos com PostgreSQL/pgvector e FAISS, alem de estrategias de buffer de curto prazo (context window) e transferencia para memoria de longo prazo.

## Exemplo de Fluxo Integrado

```python
class KnowledgeSystem:
    def __init__(self, vault_path: str, vector_store, llm_client):
        self.vault = ObsidianVault(vault_path)
        self.vector_store = vector_store
        self.llm = llm_client
        self.memory = MemoryManager()

    async def query(self, user_input: str, user_id: str) -> str:
        # 1. Recuperar memoria do usuario
        memories = await self.memory.retrieve(user_id, user_input)

        # 2. Buscar chunks relevantes no vault
        query_embedding = embed(user_input)
        chunks = self.vector_store.similarity_search(query_embedding, k=5)

        # 3. Re-ranking dos resultados
        reranked = rerank_cross_encoder(user_input, chunks)

        # 4. Montar contexto
        context = self._build_context(reranked, memories)

        # 5. Gerar resposta
        response = await self.llm.generate(
            system="Use o contexto e as memorias para responder.",
            context=context,
            query=user_input
        )

        # 6. Atualizar memoria
        await self.memory.store(user_id, user_input, response)

        return response
```

## Diretorios de Implementacao

- **`rag-implementation/`** — Implementacoes em codigo de RAG (scripts Python, pipelines completos)
- **`rag-pipeline/`** — Arquitetura do fluxo de dados RAG (embeddings, armazenamento vetorial, query engine)
- **`monitoring/`** — Metricas de qualidade de recuperacao e geracao (precisao, recall, latencia)

## Metricas de Qualidade

| Metrica | Descricao | Alvo | Ferramenta |
|---------|-----------|------|------------|
| Recall@K | Fração de chunks relevantes recuperados | > 0.85 | RAGAS |
| Precision@K | Precisao dos chunks recuperados | > 0.80 | RAGAS |
| Faithfulness | Fidelidade ao contexto fornecido | > 0.90 | RAGAS |
| Answer Relevancy | Relevancia da resposta gerada | > 0.85 | RAGAS |
| Latencia P95 | Tempo total de recuperacao + geracao | < 3s | Prometheus |

## Como o Pipeline RAG se Conecta ao Vault

1. **Ingestao** — Notas do vault sao processadas por chunking semantico (fronteiras de paragrafos/secoes)
2. **Embedding** — Cada chunk e convertido em vetor de 1536 dimensoes (text-embedding-3-small ou similar)
3. **Armazenamento** — Vetores indexados em pgvector (HNSW) ou FAISS no diretorio `rag-pipeline/`
4. **Recuperacao** — Query engine converte pergunta em embedding, busca chunks similares, aplica re-ranking
5. **Geracao** — Contexto recuperado + memoria de longo prazo sao injetados no prompt do LLM, gerando resposta fundamentada

## Componentes Relacionados no Ecosistema JARVIS

- **MCP Servers**: Transporte de dados entre sistemas usando [[skills/03-infrastructure-mcp/mcp-servers|MCP]]
- **Backend Skills**: APIs para servicos de conhecimento em [[skills/02-software-engineering/backend|Backend]]
- **Database Skills**: Modelagem vetorial e indices em [[skills/02-software-engineering/database|Database]]
- **Prompt Engineering**: Templates para injecao de contexto em [[skills/ai/Engenharia-de-Prompts|Engenharia de Prompts]]

## Roteiro de Estudo

1. **[[obsidian-neural-vault|Obsidian Neural Vault]]** — Entenda como o conhecimento e estruturado no Obsidian
2. **[[advanced-rag-strategies|RAG Avancado]]** — Aprenda a extrair conhecimento inteligentemente
3. **[[memory-management|Gestao de Memoria]]** — Faca o agente aprender e reter informacao ao longo do tempo
4. **Explore `rag-implementation/`** — Veja scripts e pipelines de RAG em acao
5. **Configure `monitoring/`** — Meça qualidade das respostas com RAGAS e Prometheus
6. **Integre com MCP** — Conecte o sistema de conhecimento aos servidores MCP

## Referencias

- [[skills/02-software-engineering/Bancos-de-Dados/PostgreSQL-Advanced|PostgreSQL Avancado]] — pgvector, indices HNSW, modelagem vetorial
- [[Conhecimento-Geral/Matematica/Algebra-Linear-Essencial|Algebra Linear]] — Fundamentos de embeddings e similaridade por cosseno
- [[Conhecimento-Geral/Neurociencia/Sistemas-de-Memoria|Sistemas de Memoria]] — Inspiracao biologica para arquiteturas de memoria artificial
- [[JARVIS/05-System/Blueprints/Template-Memoria-Episodica|Template Memoria Episodica]] — Estrutura de dados para capturar memorias no JARVIS
- [[skills/03-infrastructure-mcp/mcp-servers|MCP Servers]] — Transporte de dados entre sistemas de conhecimento
- [[skills/03-infrastructure-mcp/advanced-mcp-integrations|MCP Avancado]] — Orquestracao multi-servidor para pipelines RAG
- [[skills/ai/Generative-Models|Generative Models]] — Modelos para sintese e aumentacao de dados
- [[skills/ai/MLOps|MLOps]] — Pipeline de deploy e monitoramento de sistemas RAG
- [[skills/ai/Engenharia-de-Prompts|Engenharia de Prompts]] — Templates de prompt para injecao de contexto
