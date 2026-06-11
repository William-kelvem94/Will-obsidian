---
title: "Migração pendente de scripts"
date: 2026-06-08
updated: 2026-06-08
type: status
status: active
tags: [sistema, scripts, migracao, pendente]
summary: "Lista de scripts ainda pendentes de migração para 09-Sistema/scripts/legado."
---

# Migração pendente de scripts

Alguns scripts ainda permanecem em `scripts/` e precisam ser movidos para `09-Sistema/scripts/legado/` quando o conector permitir migração por lote ou quando for possível rodar `git mv` localmente.

## Já migrados

- `gen_skill.py`
- `scan_gaps.py`
- `gen_analytics.py`

## Pendentes identificados

- `preprocess_poc.py`
- `gap_recommender.py`
- `gen_bibliography.py`
- `zotero_integrator.py`
- `enrich_frontmatter.py`
- `generate_flashcards.py`
- `preprocess_multimodal.py`
- `jarvis_memory_bridge.py`
- `dedupe_by_hash.py`
- `preprocess_incremental.py`
- `generate_readme_preview.py`
- `audit_sensitives.py`
- `generate_frontmatter_snippets.py`
- `sensitive_files_report.py`
- `preprocess_full.py`
- `generate_dedupe_csv.py`
- `test_skeletons/test_embeddings_skeleton.py`
- `generate_frontmatter_patches.py`
- `generate_indexer_config.py`
- `test_embedding_queries.py`

## Regra

Não apagar scripts antigos sem confirmar que o mesmo conteúdo existe no destino novo e que chamadas internas foram revisadas.
