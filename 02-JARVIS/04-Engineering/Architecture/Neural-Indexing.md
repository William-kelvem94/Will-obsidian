---
tags: [jarvis, architecture, rag, indexing, jarvis-engenharia]
updated: 2026-06-08
title: "Neural Indexing & RAG Optimization"
date: 2026-04-27
---

# Neural Indexing & RAG Optimization

Guidelines for how the JARVIS brain (this Obsidian Vault) should be indexed and searched by AI agents to achieve maximum precision and context relevance.

## Core Hierarchy
1. **The Semantic Core**: Folders prefixed with `01` and `04` contain the essential identity and logic. These should always be indexed with high weight.
2. **The Stream**: Folder `03-Memory` contains chronological data. This should be queried using a sliding window (e.g., last 3 days of logs).
3. **The Playbooks**: Folder `04-Engineering/Playbooks` contains proven workflows. Agents should check these *before* attempting new tasks.

## Chunking Strategy
- **Atomic Nodes**: Keep notes small (under 1000 words) to prevent context dilution during retrieval.
- **Contextual Headers**: Use rich markdown headers (`##`, `###`) as they act as semantic anchors for embedding models.
- **Cross-Linking**: Utilize `[[backlinks]]` to help the RAG system traverse the knowledge graph when a direct semantic match is weak.

## RAG Enhancement
- **Keyword + Semantic**: Use "Hybrid Search" (keywords like "python" + semantic meaning of "automation").
- **Re-ranking**: After initial retrieval of top 10 chunks, perform a second pass with a more powerful model to select the best 3.
- **Prompt Injection**: Use the current project from `02-Operational/Context/Estado.md` as a global bias for all search queries.

## Monitoring
- Track "Misses": When the agent fails to find information that exists in the vault.
- Update `05-System/Maps/INDEX.md` weekly to ensure no orphans are left behind.

[[02-JARVIS/README|← Voltar ao Command Center]]
