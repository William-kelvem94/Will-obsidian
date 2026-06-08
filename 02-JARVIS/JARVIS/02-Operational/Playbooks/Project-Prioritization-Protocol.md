---
title: "Project Prioritization Protocol"
description: "A non-sensitive scoring protocol for agents to compare projects, choose next actions, and explain tradeoffs."
tags: [jarvis, project, prioritization, protocol, ops, jarvis-operacao]
updated: 2026-06-07
status: active
date: 2026-06-01
---

# Project Prioritization Protocol

This playbook helps agents prioritize operational work without relying on private context. It is designed for triage, planning, and session handoff.

Related context: [[03-Projetos/Projetos]], [[02-JARVIS/JARVIS/02-Operational/Dashboard|Operational Dashboard]], [[02-JARVIS/JARVIS/02-Operational/Project-Health-Report|Project Health Report]].

## Priority Inputs

Rank work using observable signals:

- explicit user request;
- deadline or blocking dependency;
- current project status;
- impact on reliability, safety, or delivery;
- amount of uncertainty removed;
- effort required to reach a useful checkpoint;
- reversibility of the next step.

Avoid inferring priority from private identity, emotion, or personal history unless the user directly provides that context for the task.

## Scoring Grid

Use 0 to 3 for each dimension:

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| User pull | no current ask | implied | mentioned | explicit request |
| Blocking power | none | local | blocks one project | blocks multiple workflows |
| Impact | cosmetic | convenience | meaningful utility | safety, reliability, or delivery |
| Clarity | vague | partial | mostly scoped | clear next action |
| Effort fit | too large | multi-session | session-sized | small checkpoint |
| Reversibility | risky | moderate | easy to adjust | additive or reversible |

Suggested priority score:

```text
priority = user_pull + blocking_power + impact + clarity + effort_fit + reversibility
```

## Choosing The Next Action

Prefer the action that:

- satisfies an explicit request;
- unblocks the most future work;
- can be verified in the current session;
- creates a durable artifact;
- avoids sensitive areas unless required.

When scores tie, choose the smallest reversible step that improves context quality.

## Agent Response Pattern

When presenting priority, include:

- the chosen next action;
- one sentence explaining why;
- any blocker or confirmation needed;
- what will be produced by the end.

Example:

```text
I will create a review checklist first because it is additive, safe, and unblocks future automatic improvements.
```

## Reprioritization Triggers

Re-score when:

- the user changes the goal;
- a command or test reveals a blocker;
- a supposedly safe edit touches canonical or private context;
- a higher-risk action requires confirmation;
- the session time or available context changes.


[[02-JARVIS/JARVIS/02-Operational/Playbooks/INDEX|← Voltar ao índice de Playbooks]]
