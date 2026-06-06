---
title: "Agent Runbook Template"
category: "DevOps"
level: 2
description: "A copy-paste template for runbooks designed to be executed by agents safely."
date: 2026-05-08
updated: 2026-06-05
tags: [skills, devops, template, agents, runbook]
---

# Agent Runbook Template

## Purpose

What incident/problem class this runbook addresses.

## Scope

- System/service:
- Environment(s):
- In-scope symptoms:
- Out-of-scope:

## Preconditions

- Required access:
- Required tools:
- Allowed directories to edit:
- Forbidden actions:

## Safety Rules (Stop Conditions)

Stop and ask for human confirmation if:
- data loss risk is non-trivial
- credentials/secrets would be exposed
- irreversible actions are required
- blast radius is unclear

## Inputs

- Service name:
- Time window:
- Alert name or user report:

## Procedure

1. Triage
2. Diagnose
3. Mitigate
4. Validate
5. Record actions

## Validation

Success criteria:
- error ratio:
- latency:
- user-facing checks:

## Rollback

Exact rollback steps:

## Evidence

- dashboards:
- trace ids:
- log queries:
- deploy ids:
- config changes:

## Post-incident Actions

- Runbook updates:
- Preventive fixes:
- Monitoring improvements:

