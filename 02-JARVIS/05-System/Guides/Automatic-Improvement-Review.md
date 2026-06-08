---
title: "Automatic Improvement Review"
description: "Governance guide for reviewing, accepting, rejecting, and promoting automatically generated improvement proposals."
tags: [jarvis, improvement, review, governance, agent, jarvis-sistema]
updated: 2026-06-08
status: active
date: 2026-06-01
---

# Automatic Improvement Review

This guide defines how agents should handle automatic improvement suggestions before they become durable system behavior.

Related context: [[02-JARVIS/05-System/Improvements/INDEX|Improvements Index]], [[02-JARVIS/02-Operational/Playbooks/Session-to-Learning-Protocol|Session To Learning Protocol]], [[02-JARVIS/02-Operational/Playbooks/Agent-Confirmation-Protocol|Agent Confirmation Protocol]].

## Principle

An improvement proposal is not a rule. It is a candidate change that needs evidence, scope, and review before it modifies canonical guidance.

## Review States

Use these states:

- `proposed`: captured but not evaluated;
- `accepted`: approved for implementation;
- `implemented`: reflected in a guide, playbook, script, or process;
- `rejected`: intentionally not adopted;
- `deferred`: useful but not timely;
- `superseded`: replaced by a better proposal.

## Review Checklist

Before accepting a proposal, verify:

- it solves a repeated or high-impact problem;
- it does not require private context to be useful;
- it has a clear owner or target area;
- it names the files or workflows it would change;
- it can be reversed or revised;
- it does not conflict with the agent contract;
- it has a verification method.

## Promotion Rules

Promote an improvement only when one of these is true:

- the user explicitly requests implementation;
- multiple sessions show the same pattern;
- the proposal fixes a safety or reliability gap;
- the change is additive, low-risk, and improves agent behavior.

Even then, prefer scoped edits. Update the nearest relevant guide rather than rewriting multiple hubs.

## Rejection Rules

Reject or defer when:

- the benefit is vague;
- the proposal depends on sensitive or personal data;
- it duplicates an existing rule;
- it makes agents more autonomous in high-risk areas without confirmation;
- it would reorganize the vault for aesthetics rather than retrieval or operational value.

## Implementation Record

When implementing an accepted improvement, record:

- proposal source;
- files changed;
- behavior changed;
- verification performed;
- remaining limits.

This record can live in the improvement note, final session summary, or a decision note if the change affects future policy.

## Agent Review Prompt

Agents can use this prompt to review a proposal:

```text
Review this improvement as proposed, accepted, deferred, rejected, or superseded. Explain the operational value, risk, target files, and verification method. Do not edit canonical notes unless explicitly approved.
```


[[02-JARVIS/05-System/Guides/INDEX|← Voltar ao índice de Guides]]
