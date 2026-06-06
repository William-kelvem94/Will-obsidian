---
title: "Observability (Practical)"
category: "DevOps"
level: 3
description: "Practical patterns for logs, metrics, and traces that actually help during incidents."
date: 2026-05-08
updated: 2026-06-05
tags: [skills, devops, observability]
---

# Observability (Practical)

Goal: make debugging cheaper than guessing. "Practical" means signals that:

- Answer common questions fast (what broke, where, when, how big, who is impacted).
- Can be trusted (consistent naming, stable units, clear cardinality).
- Survive pressure (works at 3am, not only in demos).

## The Three Signals

Logs:
- Best for: details and forensics.
- Risk: noise and missing structure.

Metrics:
- Best for: trends, alerting, capacity.
- Risk: missing context; high cardinality can blow up cost.

Traces:
- Best for: request path, latency breakdown, dependency mapping.
- Risk: sampling hides edge cases; instrumentation drift.

## Minimal Baseline (Start Here)

Per service:
- Health: request rate, error rate, latency (p50/p95/p99).
- Saturation: CPU, memory, disk, queue depth, thread pool, connection pool.
- Dependencies: database latency/errors, cache hit rate, external API latency/errors.

Across the system:
- One "golden dashboard" per user journey or critical capability.
- One "top errors" view per service (grouped by stable error code).

## Naming and Labels (Keep It Queryable)

Metrics:
- Use clear unit suffixes: `_seconds`, `_bytes`, `_total`.
- Prefer low-cardinality labels: `service`, `endpoint`, `method`, `status_class`.
- Avoid unbounded labels: `user_id`, `email`, `full_url`, `exception_message`.

Logs:
- Structure JSON when possible.
- Always include: `timestamp`, `level`, `service`, `env`, `request_id` (or trace id), `event`.

Traces:
- Propagate context across HTTP, queues, and background jobs.
- Use stable span names: `HTTP GET /route`, `db.query`, `cache.get`.

## What To Alert On

Alert on symptoms, not causes:
- SLO burn rate (fast + slow windows).
- Sustained high error ratio.
- Latency regression with real impact (p95/p99 over threshold).

Use pages for urgent, actionable, user-impact issues.
Use tickets for non-urgent, long-horizon risks (capacity, tech debt).

## Verification Checklist

- Can I identify "what changed" in the last hour?
- Can I answer "which users are impacted" without reading raw logs?
- Can I jump from an alert to a trace and then to correlated logs?
- Are dashboards and alerts versioned and reviewed like code?

## Promote to Runbook

When an incident repeats:
- Extract the shortest working diagnosis + mitigation path.
- Create a runbook that a tired agent can execute safely.

