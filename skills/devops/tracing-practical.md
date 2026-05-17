---
title: "Tracing (Practical)"
category: "DevOps"
level: 3
description: "Distributed tracing patterns for latency breakdowns and dependency debugging."
date: 2026-05-08
updated: 2026-05-08
tags: [skills, devops, traces, performance]
---

# Tracing (Practical)

Tracing helps you see where time and failures happen across services.

## Context Propagation

Ensure trace context is propagated across:
- inbound HTTP
- outbound HTTP
- queues and async workers
- background jobs

If propagation breaks, traces become misleading.

## Span Naming

Use stable, low-cardinality names:
- `HTTP GET /orders/:id`
- `db.query`
- `cache.get`
- `upstream.call`

Avoid span names that include raw ids or unbounded strings.

## Attributes (Tags)

Add attributes that are useful for filtering:
- `service.name`, `deployment.environment`, `version`
- `http.method`, `http.route`, `http.status_code`
- `db.system`, `db.operation`

Be careful with PII and secrets. Prefer hashes and truncation.

## Sampling Strategy

- Tail sampling: keep traces with errors and high latency.
- Head sampling: cheap, but can miss rare failures.

Rule: always keep error traces if possible.

## From Trace to Action

Operational flow:
- Identify slow span.
- Validate dependency health metrics.
- Check correlated logs using trace id.
- Apply mitigation (feature flag, rollback, rate limit, cache warmup).

