---
title: "Component Boundaries and Ownership (Agent Playbook)"
category: "Frontend"
level: 3
description: "How to draw component boundaries: primitives vs composites, server vs client, ownership, and API design."
tags: [skills, frontend, architecture, components]
updated: 2026-06-07
date: 2026-06-01
---

# Component Boundaries and Ownership (Agent Playbook)

## Why This Matters

Agents tend to over-factor or under-factor. This playbook aims for stable boundaries.

## Layering Model

1. Primitives: buttons, inputs, dialog, tooltip, table primitives
2. Composites: domain-agnostic composed UI (search bar, date range picker)
3. Feature Components: domain-specific components (InvoiceList, TenantForm)
4. Pages/Routes: orchestration, data fetching, layout composition

Rule:
- If it knows business rules, it is a feature component.
- If it knows data fetching, it is usually a page/route server component.

## Ownership Rules

Pick one owner:
- If a component is used by multiple features, put it in shared UI.
- If it is specific, keep it near the feature route.

Avoid:
- Shared folders becoming junk drawers.
- Feature components living in generic UI folders.

## Component APIs

Good API traits:
- Small prop surface
- Accepts children for composition when appropriate
- Exposes callbacks for events (not internal state leakage)
- Has sensible defaults

Anti-patterns:
- Dozens of boolean props.
- Props that encode layout specifics (prefer wrapper composition).
- Passing entire data models when only a few fields are used.

## Server/Client Boundary Applied

Prefer:
- Server component fetches and renders feature shell
- Small client component handles interactions

Do not:
- Mark the page component as client for convenience
- Fetch everything in the client and lose streaming/error boundaries

## Refactor Heuristics

Refactor into a new component when:
- The UI block repeats in 2+ places with real shared logic
- The block has a stable interface and tests can cover it
- The naming becomes clearer (it reduces cognitive load)

Do not refactor when:
- It is a one-off UI
- It is volatile and still evolving
- You cannot name it well

## "Agent Guardrails" For PRs

- If you introduce a shared component, list the consuming routes.
- If you move a component, check imports and update any story/test references.
- If you change props, ensure call sites are updated and behavior is preserved.

