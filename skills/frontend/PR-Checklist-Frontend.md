---
title: "PR Checklist for Frontend Changes (Agents)"
category: "Frontend"
level: 2
description: "A PR checklist focused on frontend quality: UX, a11y, performance, tests, and safe rollout."
tags: [skills, frontend, pr-checklist]
updated: 2026-06-05
date: 2026-06-01
---

# PR Checklist for Frontend Changes (Agents)

- Scope is clear and limited to the intended behavior change.
- Empty/loading/error states are handled.
- Accessibility checklist is satisfied (keyboard, focus, semantics).
- No unnecessary `"use client"` added; server/client boundary is justified.
- Performance impact considered (bundle imports, list rendering, images).
- i18n respected (no concatenated strings; formatting uses locale).
- Tests added/updated appropriately (component/integration/e2e as needed).
- Feature flags or safe rollout plan included when risk is high.
- Analytics/logging changes do not leak sensitive data.
- Screenshots or short repro steps included for UI changes when helpful.

