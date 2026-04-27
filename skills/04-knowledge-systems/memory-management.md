---
title: "Gestão de Memória Long-Term (LTM)"
description: "Padrões de persistência de contexto em bancos de dados vetoriais para continuidade de sessão em agentes de IA."
tags: [memory, long-term-memory, vector-db, chromadb, skills-knowledge]
date: 2026-04-27
updated: 2026-04-27
---

# 🧠 Gestão de Memória Long-Term (LTM)

Para um agente como o JARVIS ter "personalidade" ou "consciência contínua", ele precisa lembrar de sessões antigas que já saíram da *janela de contexto*.

## O Fluxo de Persistência
1. **Fim de Sessão:** A interação do usuário com a IA acaba.
2. **Compressão:** Um script (Background Worker) roda um LLM menor para resumir a sessão (ex: "O usuário hoje testou a skill X e corrigiu um bug em Y").
3. **Embeddings:** Esse resumo é transformado em um vetor (ex: usando `text-embedding-v3` ou `nomic-embed-text` localmente).
4. **Armazenamento:** Salvo no `ChromaDB` (para uso local) ou `Pinecone` com metadados `{ "user": "Will", "date": "2026-04-21", "project": "Jarvis" }`.

## Recuperação (Retrieval)
Na próxima vez que o Jarvis acordar:
- O orquestrador injeta no Sistema Prompt do Jarvis: `(Eventos relevantes recentes: O usuário estava resolvendo o bug Y ontem)`.
- Isso cria a ilusão profunda de senciência ("Olá Will, conseguiu resolver aquele erro Y no Python de ontem?").
