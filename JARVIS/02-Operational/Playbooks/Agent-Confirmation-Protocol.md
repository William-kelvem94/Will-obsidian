---
title: "Agent Confirmation Protocol"
description: "Operational rules for when agents should ask for confirmation before reading, writing, executing, or escalating work."
tags: [jarvis, agent, protocol, confirmation, ops]
updated: 2026-05-08
status: active
---

# Agent Confirmation Protocol

This playbook defines when an agent can proceed autonomously and when it must stop for confirmation. It is intentionally non-sensitive and can be loaded by retrieval systems before operational work.

Related context: [[JARVIS/05-System/AGENT-CONTRACT|Agent Contract]], [[JARVIS/05-System/ONBOARDING-AGENTE|Onboarding de Agente Externo]].

## Default Posture

Agents should proceed when the user has clearly requested a bounded operational change in a safe area. Agents should ask before touching private, identity, canonical, destructive, or externally visible surfaces.

The confirmation question should be specific:

- name the action;
- name the files, folders, command, or system affected;
- explain the practical consequence;
- offer a safe default.

## Confirmation Required

Ask for confirmation before:

- editing `Will-Pessoal/`, identity notes, preference notes, or any autobiographical material;
- changing canonical hubs, architecture decisions, contracts, onboarding rules, or map files;
- deleting, moving, renaming, or bulk rewriting notes;
- running commands that may modify many files, install dependencies, access the network, publish data, or alter Git history;
- promoting an improvement suggestion into canonical knowledge;
- storing information that looks private, credential-like, medical, legal, financial, or relational;
- making irreversible decisions on behalf of the user.

## Confirmation Not Usually Required

Proceed without extra confirmation when:

- creating a new note in an approved safe folder requested by the user;
- adding a bounded log, snapshot, learning note, improvement proposal, or playbook;
- fixing formatting in a note the user explicitly asked you to edit;
- reading non-sensitive operational documentation needed to complete the task;
- running local read-only checks such as listing files, searching text, or checking Git status.

## Confirmation Template

Use a concise question:

```text
I can do X in Y, which will affect Z. Should I proceed?
```

If there is a safer option, include it:

```text
I can either add a new proposal note or edit the canonical guide directly. I recommend the proposal note first. Which path should I take?
```

## Risk Labels

Use these labels in reasoning and summaries:

- `low-risk`: additive change in a safe folder;
- `medium-risk`: touches shared operational guidance or project workflow;
- `high-risk`: private, canonical, destructive, irreversible, or externally visible;
- `blocked`: cannot proceed without explicit user decision.

## After Confirmation

Record the decision when it changes future behavior:

- minor one-off consent can stay in the session summary;
- durable policy decisions should become a decision note in `JARVIS/02-Operational/Decisions/`;
- rejected or uncertain suggestions should become an improvement proposal in `JARVIS/05-System/Improvements/`.


[[JARVIS/02-Operational/Playbooks/INDEX|← Voltar ao índice de Playbooks]]
