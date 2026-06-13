---
title: "Metrics (Practical)"
category: "DevOps"
level: 3
description: "Design metrics that enable alerting, capacity planning, and fast debugging."
date: 2026-05-08
updated: 2026-06-13
tags: [skills, devops, metrics, slo]
---

# Metrics (Practical)

Metrics give you fast, cheap queries about system behavior over time.

## Metric Types

- Counters: monotonic totals (requests_total, errors_total).
- Gauges: current value (memory_bytes, queue_depth).
- Histograms/Summaries: distributions (request_duration_seconds).

## Golden Signals (Service)

Start with:
- Traffic: request rate.
- Errors: error ratio.
- Latency: p50/p95/p99.
- Saturation: CPU, memory, queues, pools.

## Cardinality Control

High-cardinality labels kill systems and budgets. Rules:
- Labels must have bounded values.
- Avoid user ids, raw URLs, exception messages, and unbounded tags.
- Prefer grouping: status_class (2xx/4xx/5xx) instead of status_code when possible.

## SLO-first Alerts

If you have SLOs, alert on:
- Error budget burn rate (fast + slow windows).
- Sustained latency over threshold for user-impact endpoints.

Avoid alerting on "CPU > 80%" unless it is proven to predict incidents.

## Capacity and Cost

Track:
- RPS and concurrency vs. latency.
- Queue depth and time-in-queue.
- Database connections, locks, and slow queries.
- Cache hit rate and eviction rate.

## Dashboard Hygiene

Dashboards should answer:
- What is broken?
- How big is the impact?
- What changed recently?
- Which dependency is failing?

If a panel does not answer a question, delete it.

