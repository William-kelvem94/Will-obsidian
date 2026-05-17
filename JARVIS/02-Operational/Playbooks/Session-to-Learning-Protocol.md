---
title: "Session To Learning Protocol"
description: "How agents convert a work session into reusable, non-sensitive learning without polluting canonical notes."
tags: [jarvis, learning, protocol, memory, ops, rag]
updated: 2026-05-08
status: active
---

# Session To Learning Protocol

This protocol turns useful session outcomes into future context. It separates raw activity, reusable learning, and canonical knowledge so agents can preserve continuity without overfitting the vault to one session.

Related context: [[JARVIS/03-Memory/README|Memory README]], [[JARVIS/05-System/AGENT-CONTRACT|Agent Contract]].

## Three Output Types

Use the smallest durable artifact that captures value:

- `log`: what happened in a session;
- `learned-pattern`: a reusable pattern observed across work;
- `improvement`: a proposed system change needing review.

Do not turn every session into canonical guidance. Canonical notes should change only after repeated evidence or explicit user direction.

## Extraction Questions

At the end of a useful session, ask:

- What will a future agent need to know to avoid repeating work?
- Which constraint was discovered or clarified?
- Which command, path, or workflow proved reliable?
- Which assumption was wrong?
- Is this a one-time event, a reusable pattern, or a proposed change?

## Safe Content Rules

Keep learning notes non-sensitive:

- summarize operational behavior, not personal identity;
- avoid credentials, private conversations, health, finances, and relationship details;
- refer to folders, protocols, and project states rather than private motivations;
- use neutral phrasing that remains useful to agents.

## Suggested Structure

```markdown
---
title: "Short Learning Title"
description: "Standalone summary of the reusable lesson."
tags: [jarvis, learned-pattern, ops]
updated: YYYY-MM-DD
status: active
---

# Short Learning Title

One-paragraph summary.

## Evidence

- Session or file context that produced the learning.

## Reusable Rule

- The operational rule future agents should apply.

## Limits

- When this learning should not be applied.
```

## Promotion Path

Use this progression:

1. Record raw session facts in memory or final summary.
2. Create a learned pattern if the lesson is reusable.
3. Create an improvement proposal if the system should change.
4. Promote to a canonical guide only after review or explicit instruction.

## Anti-Patterns

Avoid:

- writing private details because they were nearby in context;
- turning a one-off workaround into a permanent rule;
- editing identity or preference notes to explain an operational lesson;
- burying the reusable lesson in a long chronological log;
- omitting the limit conditions that prevent bad retrieval matches.

