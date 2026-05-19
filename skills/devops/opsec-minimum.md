---
title: "Operational Security (Minimum)"
category: "DevOps"
level: 3
description: "Minimum operational security practices for small teams and agent-assisted workflows."
date: 2026-05-08
updated: 2026-05-08
tags: [skills, devops, security, opsec]
---

# Operational Security (Minimum)

This is not a full security program. It is the minimum that prevents avoidable incidents.

## Secrets Handling

- Store secrets in a secrets manager or env vars, not in git.
- Rotate leaked tokens immediately.
- Never paste secrets into prompts, issues, or logs.

## Access Control

- Least privilege: grant only what is needed.
- Separate dev/stage/prod credentials.
- Use short-lived tokens where possible.
- Log admin actions (audit trail).

## Backups and Recovery

- Define RPO/RTO per system (even if rough).
- Test restore at least monthly for critical data.
- Keep backup access separate from production access.

## Change Management (Small Team Edition)

- Every prod change has: owner, reason, rollback plan.
- Prefer feature flags and canary where possible.
- Keep a changelog of deploy ids and config changes.

## Agent-specific Rules

- Agents do not get production credentials by default.
- Agents must not run destructive commands without explicit confirmation.
- Agents must record what they changed (files, config, deploy id).

