---
title: "Tailwind and shadcn/ui Conventions (Agent Standards)"
category: "Frontend"
level: 2
description: "Conventions for Tailwind + shadcn/ui: class strategy, design tokens, variants, composition, and consistency."
tags: [skills, frontend, tailwind, shadcn]
updated: 2026-06-07
date: 2026-06-01
---

# Tailwind and shadcn/ui Conventions (Agent Standards)

## Goals

- Keep UI consistent across features and pages.
- Make styling changes predictable and reviewable.
- Avoid class soup and variant sprawl.

## Class Strategy

Rules:
- Prefer composition over custom CSS for most layout/spacing.
- Use design tokens (CSS variables) for colors, radii, and semantic intent.
- Keep classes grouped by purpose: layout, spacing, typography, color, states.

Good signs:
- Shared utilities for `cn()` and variants (`cva` if used).
- Components expose `className` and forward refs.

Anti-patterns:
- Inline long `className` strings duplicated across files.
- Magic colors (`text-[#123456]`) without token reasoning.
- Mixing arbitrary values everywhere (`w-[37px]`) when design tokens would work.

## Variants (CVA) Rules

Keep variants small and meaningful:
- `variant`: intent (default, destructive, outline)
- `size`: spacing/typography scale (sm, md, lg)
- `state`: rarely as a variant; prefer conditional classes or data attributes

Avoid:
- Variants encoding business meaning (use props and compose).
- Deep combinatorial explosion.

## shadcn/ui Usage Rules

Prefer using shadcn components as baseline primitives.

When customizing:
- Extend via wrapper components rather than editing the generated primitives everywhere.
- Keep `asChild` semantics consistent for links/buttons.
- Ensure focus styles are preserved (`focus-visible`).

## Forms

Rules:
- One form strategy (react-hook-form or equivalent) per area.
- Errors are shown close to fields and in an accessible summary when needed.
- Use consistent label/help/error spacing.

## Table/Dashboard Density

For operational UIs:
- Prefer compact spacing and predictable columns.
- Avoid excessive cards; use tables, lists, and split panes.
- Keep empty states informative but not verbose.

## Review Checklist (Quick)

- Are colors coming from tokens, not literals?
- Are variants minimal and reusable?
- Does focus ring exist and look consistent?
- Are spacing and typography aligned across similar screens?
- Is `className` duplication reduced?

