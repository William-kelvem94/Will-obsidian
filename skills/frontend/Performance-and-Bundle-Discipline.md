---
title: "Frontend Performance and Bundle Discipline (Agents)"
category: "Frontend"
level: 3
description: "Practical performance guidance: bundle size, rendering cost, data waterfalls, images, and measuring safely."
tags: [skills, frontend, performance]
updated: 2026-06-01
date: 2026-06-01
---

# Frontend Performance and Bundle Discipline (Agents)

## Default Mindset

Optimize for:
- fewer client components
- fewer re-renders
- fewer data waterfalls
- smaller bundles

## Bundle Discipline

Rules:
- Avoid importing large libraries in shared entry points.
- Prefer per-route imports and code splitting.
- Keep `"use client"` components narrowly scoped.

Common pitfalls:
- Importing charts/editors into pages that do not need them.
- Importing server-only code into client components.
- Copying utility functions into multiple components (prefer a shared utility module).

## Rendering Cost

Heuristics:
- Virtualize long lists/tables when items > ~200 or rendering is heavy.
- Memoize only when profiling shows benefit; do not guess everywhere.
- Avoid passing unstable props (inline objects/functions) into deep trees.

## Data Waterfalls

Patterns:
- Fetch critical data at the route/server level.
- Aggregate related queries in a server function.
- Stream non-critical UI behind `Suspense`.

## Images and Media

Rules:
- Use responsive images and correct sizes.
- Prefer lazy loading for below-the-fold media.
- Avoid massive background images for operational screens.

## Measurement (Safe)

Before optimizing:
- Identify the user path.
- Measure baseline (LCP/TTI for web, or route transition time for app).
- Change one thing at a time.

Agent report format:
- Baseline metric
- Change made
- New metric
- Any tradeoffs

