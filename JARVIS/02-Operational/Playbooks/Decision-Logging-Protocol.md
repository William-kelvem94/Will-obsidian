---
title: "Decision Logging Protocol"
description: "A reusable protocol for capturing operational decisions with context, alternatives, rationale, impact, and review triggers."
tags: [jarvis, decision, protocol, ops, rag, jarvis-operacao]
updated: 2026-06-05
status: active
date: 2026-06-01
---

# Decision Logging Protocol

Use this protocol when a session produces a decision that future agents should not rediscover from scratch.

Related context: [[JARVIS/02-Operational/Decisions/INDEX|Decision Index]], [[JARVIS/05-System/AGENT-CONTRACT|Agent Contract]].

## What Counts As A Decision

Log a decision when it changes:

- where knowledge should live;
- how agents should behave;
- project priority, ownership, or sequencing;
- an architecture, integration, workflow, or tool choice;
- a safety boundary or confirmation rule;
- the definition of "done" for a repeated process.

Do not log temporary preferences, guesses, or private details unless the user explicitly requests that durable record.

## Minimum Record

Every decision note should answer:

- **Context:** what prompted the decision;
- **Decision:** the chosen policy or action in one sentence;
- **Alternatives:** realistic paths considered;
- **Rationale:** why this path was chosen;
- **Impact:** what changes for future agents or workflows;
- **Review trigger:** when to revisit it;
- **Status:** proposed, active, superseded, or rejected.

## File Placement

Use `JARVIS/02-Operational/Decisions/` for durable operational decisions.

Recommended filename:

```text
YYYY-MM-DD-short-kebab-title.md
```

Prefer one decision per note. If a session creates several unrelated decisions, split them.

## RAG-Friendly Shape

Write the first paragraph as a compact summary that can stand alone in search results. Use headings with predictable names. Link to the affected playbook, project, or guide.

Avoid vague summaries like "updated process." Prefer concrete phrasing:

```text
Agents must store automatic improvement proposals in JARVIS/05-System/Improvements/ before changing canonical guides.
```

## Review Triggers

Add a review trigger when:

- the process fails twice;
- the user overrides the decision;
- a new tool changes the cost of the workflow;
- a project moves from draft to active;
- the decision creates friction for agents or humans.

## Session Close Checklist

Before ending a session that made decisions:

- identify decisions versus ordinary edits;
- write or update the decision note if durable;
- link the note from the relevant operational page if appropriate;
- include the decision in the final summary;
- avoid rewriting personal or identity areas to "make the decision fit."


[[JARVIS/02-Operational/Playbooks/INDEX|← Voltar ao índice de Playbooks]]
