---
title: "Log Query Cheatsheet"
category: "DevOps"
level: 2
description: "Portable patterns for querying logs during incidents (tool-agnostic)."
date: 2026-05-08
updated: 2026-06-01
tags: [skills, devops, logs, cheatsheet]
---

# Log Query Cheatsheet

Tool-agnostic patterns. Translate to your log tool (grep, Loki, ELK, etc).

## Start Broad

- service = X AND (level >= ERROR) last 15m
- service = X AND event = "request_failed" last 15m

## Group by Stable Key

- group by error_code
- group by endpoint/route
- group by upstream dependency name

## Correlate

- filter by request_id / trace_id from an alert or trace
- pivot from trace to logs: trace_id = ...

## Hunt Regressions

- compare last 15m vs previous 60m
- look for new error_codes or spikes in existing ones
- correlate with version/build id changes

## Detect Log Storms

- count logs per second by service
- identify repeated messages with high volume
- apply sampling/rate limit if safe

