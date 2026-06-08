---
title: "SLO/SLI/SLA (Basics)"
category: "DevOps"
level: 3
description: "Service reliability basics: defining SLIs, setting SLOs, and using error budgets."
date: 2026-05-08
updated: 2026-06-07
tags: [skills, devops, slo, reliability]
---

# SLO/SLI/SLA (Basics)

Definitions:
- SLI: how you measure reliability (latency, availability, correctness).
- SLO: the target for an SLI (e.g., 99.9% success).
- SLA: a contractual commitment (often with penalties).

## Choose SLIs That Match Users

Good SLIs:
- request success ratio for critical endpoints
- end-to-end job completion success ratio
- time-to-first-byte for user-facing operations

Bad SLIs:
- CPU usage
- memory usage
- "uptime" of a component that users do not directly see

## Error Budgets

Error budget = 1 - SLO.
Use error budgets to balance:
- shipping features
- stability work

Operational policy example:
- If budget burn is high: freeze risky changes, fix reliability.
- If budget is healthy: ship faster.

## Burn Rate Alerting (Practical)

Use two windows:
- Fast window catches sudden regressions.
- Slow window catches sustained issues.

Alerts should trigger when action is possible (rollback, mitigation, reroute).

