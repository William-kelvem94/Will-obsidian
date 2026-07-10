---
title: LLM Wiki Agent Instructions
tags:
  - llm-wiki
  - agents
created: 2026-05-12
updated: 2026-05-12
---

# LLM Wiki Agent Instructions

This vault is an Obsidian-friendly LLM Wiki. Before making durable wiki changes, read `schema/AGENT.md` and follow its raw/wiki/schema separation rules.

The operating principle is:

- `raw/` is immutable evidence.
- `wiki/` is generated synthesis.
- `schema/` is the evolving operating system.

Use the visible skill documentation in `05-Skills/` when the task matches a skill:

- `05-Skills/obsidian-markdown/SKILL.md` for Obsidian markdown, wikilinks, embeds, callouts, and frontmatter.
- `05-Skills/obsidian-bases/SKILL.md` for `.base` files, table/card/list/map views, formulas, filters, and Base validation.
- `05-Skills/obsidian-cli/SKILL.md` when interacting with a running Obsidian instance or verifying plugin/theme behavior through the Obsidian CLI.
- `05-Skills/json-canvas/SKILL.md` for `.canvas` files, visual canvases, and JSON Canvas graph work.
- `05-Skills/defuddle/SKILL.md` for extracting clean markdown from web pages before ingesting or analyzing web sources.

The hidden `.agents/05-Skills/` directory may also exist as an agent-runtime install location. Treat `05-Skills/` as the human-visible copy inside the vault and `.agents/05-Skills/` as compatibility infrastructure.

For practical multi-agent content work, see [[05-Skills/01-agentic-intelligence/multi-agent-orchestration|Orquestracao Multi-Agente e Pipelines de Subagentes]].

## Required Workflow

For `INGEST`, `QUERY`, `LINT`, or `AUDIT`, read `schema/AGENT.md` first.

For substantial source ingests, also read:

- `schema/evolution/ingest-rubric.md`
- `schema/evolution/output-quality-rubric.md`
- `schema/evolution/extraction-patterns.md`

Never modify files under `raw/` unless the user explicitly asks for source-archive setup or organization.
