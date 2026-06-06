---
title: "Runbooks for Agents"
category: "DevOps"
level: 3
description: "How to write runbooks that autonomous agents can execute safely and repeatably."
date: 2026-05-08
updated: 2026-06-05
tags: [skills, devops, agents, runbook]
---

# Runbooks for Agents

Agents are fast and literal. Runbooks must be explicit, constrained, and safe.

## Runbook Contract

Each runbook must include:
- Scope: what system and what incident class.
- Preconditions: required access, env, and current state.
- Safety rules: what must NOT be changed automatically.
- Commands: exact commands to run, in order.
- Validation: how to confirm success and how to roll back.
- Escalation: when to stop and ask for human confirmation.

## Make Steps Verifiable

Bad:
- "Check the logs"

Good:
- "Query error ratio for service X over last 15 minutes; if > 2% proceed to step 4"

## Prefer Reversible Actions

In order:
- feature flag disable
- traffic shift
- rollback
- rate limiting
- capacity add

Avoid:
- schema changes
- data migrations
- "quick patch" deploys without tests

## Agent Guardrails

Always specify:
- which folders/files are allowed to edit
- which commands are allowed
- where outputs should be recorded (log note, incident note)

## Make It RAG-friendly

Use:
- short sections
- stable headings
- consistent naming for systems and services
- a "last verified" date

