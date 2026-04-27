---
title: "Estratégias Avançadas de RAG (GraphRAG e Híbrido)"
description: "Análise profunda sobre como recuperar dados para IAs além do Vector Search tradicional."
tags: [rag, graphrag, hybrid-search, embeddings, skills-knowledge]
date: 2026-04-27
updated: 2026-04-27
---

# 🔍 Estratégias Avançadas de RAG (Retrieval-Augmented Generation)

O RAG "Vanilla" (apenas Vector Search) falha quando a resposta exige agregar conceitos de múltiplos documentos ou buscar palavras exatas. Precisamos de abordagens híbridas.

## 1. O Problema do RAG Tradicional (Naive RAG)
O RAG padrão funciona pegando o texto, quebrando em blocos de 500 palavras (Chunks), convertendo em vetores e buscando proximidade matemática (Cosine Similarity).
**Falha quando:**
- O usuário pergunta "Resuma a evolução de toda a arquitetura". O Vector Search puxará apenas os 5 blocos mais matematicamente parecidos com a pergunta, e ignorará o resto do repositório.

## 2. GraphRAG (Knowledge Graphs)
Criado pela Microsoft, o GraphRAG combina Grafos de Conhecimento com RAG.

### Como funciona:
1. Em vez de apenas salvar blocos de texto, uma IA lê o texto e extrai **Entidades** e **Relacionamentos**. (Ex: "Jarvis" -> [é um] -> "Agente IA", "Ollama" -> [roda no] -> "Jarvis").
2. Isso cria um banco de dados em Grafo (como Neo4j).
3. Quando a IA é perguntada, ela caminha pelas conexões lógicas do Grafo, permitindo responder perguntas sobre "A figura geral" e não apenas fatos isolados.
**No Obsidian:** Os links `[[Wiki]]` formam nativamente um GraphRAG! Ao usar o Vault como RAG, o orquestrador deve ler também os "backlinks".

## 3. Busca Híbrida (Hybrid Search)
Combina o Vector Search com a busca exata de palavras-chave (Lexical Search).

### Algoritmo:
- Usa **Vector (FAISS/Chroma)** para entender a intenção ("Eu quero coisas de aprendizado de máquina").
- Usa **BM25 / ElasticSearch** para bater exatamente a palavra ("sklearn version 1.2").
- Une os resultados usando **RRF (Reciprocal Rank Fusion)**, re-ordenando do mais relevante para os dois critérios.

## 4. Chunking Semântico
Em vez de cortar textos brutalmente a cada 500 caracteres, o "Semantic Chunking" analisa os tokens e corta quando o *assunto* muda (ex: quebrando exatamente no final de um parágrafo ou função `def` em Python). Isso mantém o contexto do bloco purificado.
