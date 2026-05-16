---
title: "Sistemas de Conhecimento e RAG Avançado"
description: "Hub central para sistemas de gestão de conhecimento, pipelines RAG modernos (GraphRAG, Híbrido) e gestão de memória."
tags: [knowledge-systems, rag, memoria, hub, skills-knowledge]
date: 2026-04-27
updated: 2026-05-16
---

# Sistemas de Conhecimento (Knowledge Systems)

O armazenamento e a recuperação de conhecimento são o coração de um agente de IA. Sem isso, o LLM é apenas uma calculadora de palavras — precisa de contexto, memória e fontes confiáveis para gerar respostas úteis. Esta área conecta a teoria dos sistemas de conhecimento à implementação prática, desde o segundo cérebro no Obsidian até pipelines de RAG em produção.

## Notas principais

### [[obsidian-neural-vault|Obsidian Neural Vault]]
A base do "Segundo Cérebro" — um vault do Obsidian projetado para ser o sistema de conhecimento central de um agente de IA. Esta nota descreve a arquitetura do vault: estrutura de pastas (Conhecimento-Geral, JARVIS, skills), convenções de nomenclatura, uso extensivo de _wiki-links_ para criar um grafo de conhecimento navegável, e _frontmatter_ estruturado para metadados. Explica como o vault funciona como um banco de dados de conhecimento semi-estruturado que alimenta o pipeline de RAG do JARVIS, com cada nota servindo como um _chunk_ semanticamente rico. Aborda também estratégias de _tagging_, _MOCs_ (Maps of Content) e a distinção entre notas atômicas e notas-índice.

### [[advanced-rag-strategies|Estratégias Avançadas de RAG]]
Além do RAG ingênuo ("buscar + colocar no prompt"), esta nota explora as estratégias de ponta para recuperação de informação em sistemas de IA. Cobre: _GraphRAG_ (Microsoft) — que constrói um grafo de conhecimento a partir dos documentos e usa navegação em grafo para responder perguntas que exigem síntese; _chunking semântico_ — dividir documentos por fronteiras semânticas (parágrafos, seções, sentenças completas) em vez de tamanho fixo; _busca híbrida_ — combinar busca lexical (BM25, FTS) com busca vetorial (embeddings) usando fusão ponderada (RRF, _Reciprocal Rank Fusion_); _re-ranking_ com modelos cross-encoder para refinar resultados; _query rewriting_ e _query decomposition_ para perguntas complexas; _HyDE_ (_Hypothetical Document Embeddings_); _multi-hop RAG_ para perguntas que exigem múltiplas rodadas de recuperação; e _agentes RAG_ que decidem dinamicamente quais fontes consultar.

### [[memory-management|Gestão de Memória Long-Term]]
Como estruturar bancos de dados vetoriais para memória persistente de agentes de IA. Esta nota aborda: modelagem de memória episódica vs. semântica vs. procedural (inspirada na neurociência), estratégias de indexação vetorial (HNSW, IVFFlat no pgvector), _forgetting mechanisms_ (LRU, importância temporal), _consolidation_ (sumarização noturna de memórias episódicas em memórias semânticas), _memory retrieval_ com _recency_, _relevance_ e _importance_ scoring, e integração com o pipeline RAG para fornecer ao LLM um contexto contínuo e evolutivo. Inclui exemplos de implementação com PostgreSQL/pgvector e FAISS, além de estratégias de _buffer_ de memória de curto prazo (context window) e transferência para memória de longo prazo.

## Diretórios de implementação

- **`rag-implementation/`** — Implementações em código de RAG (scripts Python, pipelines completos).
- **`rag-pipeline/`** — Arquitetura do fluxo de dados RAG (embeddings, armazenamento vetorial, query engine).

## Como RAG se conecta ao Conhecimento-Geral

O pipeline de RAG é a ponte que transforma as notas estáticas do [[Conhecimento-Geral/INDEX|Conhecimento-Geral]] em contexto dinâmico para o LLM:

1. **Ingestão** — As notas do Conhecimento-Geral (Direito Digital, Neurociência, Matemática, Cultura) são processadas pelo pipeline de _chunking semântico_.
2. **Embedding** — Cada _chunk_ é convertido em um vetor de 1536 dimensões (OpenAI text-embedding-3-small ou similar).
3. **Armazenamento** — Os vetores são indexados no pgvector (HNSW) ou FAISS no diretório `rag-pipeline/`.
4. **Recuperação** — Quando o JARVIS recebe uma pergunta, o _query engine_ converte a pergunta em embedding, busca os _chunks_ mais similares, aplica _re-ranking_ e retorna o contexto.
5. **Geração** — O contexto recuperado é injetado no _prompt_ do LLM junto com a memória de longo prazo, gerando uma resposta fundamentada nas notas.

## Roteiro de estudo

1. **Comece pelo vault** — [[obsidian-neural-vault|Obsidian Neural Vault]] para entender como o conhecimento é estruturado no Obsidian.
2. **Domine a recuperação** — [[advanced-rag-strategies|Estratégias Avançadas de RAG]] para aprender como extrair esse conhecimento de forma inteligente.
3. **Gerencie a memória** — [[memory-management|Gestão de Memória Long-Term]] para fazer o agente aprender e reter informação ao longo do tempo.
4. **Implemente** — Explore os diretórios `rag-implementation/` e `rag-pipeline/` para ver o código em ação.

## Referências

- [[skills/02-software-engineering/Bancos-de-Dados/PostgreSQL-Advanced|PostgreSQL Avançado]] — pgvector, índices HNSW, modelagem vetorial.
- [[Conhecimento-Geral/Matematica/Algebra-Linear-Essencial|Álgebra Linear]] — Fundamentos matemáticos de embeddings e similaridade por cosseno.
- [[Conhecimento-Geral/Neurociencia/Sistemas-de-Memoria|Sistemas de Memória]] — Inspiração biológica para arquiteturas de memória artificial.
- [[JARVIS/05-System/Blueprints/Template-Memoria-Episodica|Template Memória Episódica]] — Estrutura de dados para capturar memórias no JARVIS.
