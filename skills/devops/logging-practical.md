---
title: "Logging (Practical)"
category: "DevOps"
level: 3
description: "Structured logging patterns for fast diagnosis and safe operations."
date: 2026-05-08
updated: 2026-06-07
tags: [skills, devops, logs, opsec]
---

# Logging (Practical)

Logs are your black box recorder. The goal is not "more logs". The goal is "useful logs".

## Principles

- Prefer structured logs (JSON) over free text.
- Log events, not feelings: "payment_failed" beats "something went wrong".
- Separate operator logs from audit logs.
- Never log secrets or personal data that is not required to operate.

## Standard Fields (Baseline)

Include these fields when available:

- `timestamp`
- `level` (DEBUG/INFO/WARN/ERROR)
- `service`
- `env` (dev/stage/prod)
- `version` (git sha or build id)
- `event` (stable event name)
- `request_id` and/or `trace_id`
- `user_id_hash` (hash, not raw id) when necessary

## Stable Error Taxonomy

Create stable error codes:

- `E_AUTH_INVALID_TOKEN`
- `E_DB_TIMEOUT`
- `E_UPSTREAM_502`
- `E_VALIDATION_SCHEMA`

Avoid alerting on raw exception message strings.

## Sampling and Rate Limits

To control cost and noise:
- Sample low-value INFO logs in hot paths.
- Keep ERROR logs unsampled.
- Add log rate limiting to avoid log storms.

## Redaction Rules

Never log:
- API keys, tokens, passwords.
- Full credit card data.
- Full documents, full prompts, or raw user content unless strictly required.

If you must log payload details:
- Use allow-lists, not deny-lists.
- Truncate and hash.

## Correlation

Your operator workflow should be:

1. Alert fires.
2. Dashboard shows impacted endpoints.
3. Trace shows slow spans and failing dependencies.
4. Logs show event + error code with request/trace id.

If any step breaks, fix instrumentation before adding more dashboards.

