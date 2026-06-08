---
title: "Minimal Alerting Policy"
category: "DevOps"
level: 3
description: "Rules for pages vs tickets, alert quality, and a small set of default alerts."
date: 2026-05-08
updated: 2026-06-07
tags: [skills, devops, alerts, reliability]
---

# Minimal Alerting Policy

The goal is fewer, better alerts.

## Page vs Ticket

Page when:
- user impact is likely and immediate
- there is a clear, time-sensitive action

Ticket when:
- action is not urgent (days/weeks)
- it is an investigation or improvement task

## Alert Quality Rules

Every page alert must include:
- what is failing (service, endpoint, capability)
- how big is the impact (error ratio, affected users)
- where to look (dashboard link, query hint)
- default first action (rollback, flag off, rate limit)

If an alert does not meet this, downgrade to ticket until fixed.

## Default Alert Set (Small Systems)

Per critical service:
- high error ratio sustained
- high latency sustained (p95/p99)
- SLO burn rate (if SLO exists)

Infra:
- disk nearly full
- database connection pool exhausted
- queue depth sustained high

## Silence Policy

Temporary silences must record:
- who
- why
- when it expires

