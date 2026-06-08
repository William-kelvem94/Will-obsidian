---
title: "Incident Response (Practical)"
category: "DevOps"
level: 3
description: "A lightweight, repeatable incident process that works with human + agent teams."
date: 2026-05-08
updated: 2026-06-08
tags: [skills, devops, incident, runbook]
---

# Incident Response (Practical)

Primary goals:
- Restore service safely.
- Protect users and data.
- Learn without blame.

## Roles (Minimal)

- Incident Commander (IC): coordinates, decides, keeps scope.
- Ops/Responder: executes mitigations.
- Comms: updates stakeholders (internal and external).

One person can hold multiple roles in small teams, but explicitly state it.

## Timeline Template

- T0: detection (alert/user report)
- T+5: confirm impact, assign roles
- T+10: initial mitigation path chosen
- T+30: mitigate or rollback; stabilize
- T+60: confirm recovery and monitor

## Decision Rule Under Uncertainty

Prefer reversible actions:
- rollback
- disable feature flag
- reduce load (rate limit)
- fail open/closed according to policy

Avoid risky deep fixes during the incident.

## Evidence Collection (While You Work)

Capture:
- dashboards/screenshots references
- trace ids
- error codes
- config changes and deploy ids

This makes the postmortem real, not vibes.

## Postmortem Output (Minimal)

- What happened (user impact)
- Root cause and contributing factors
- What worked (detection/mitigation)
- What to fix (actions with owners)
- What runbook to add or update

