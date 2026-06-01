---
title: "Next.js App Router Patterns (Agent Playbook)"
category: "Frontend"
level: 3
description: "Practical patterns for Next.js App Router: data fetching, server/client boundaries, caching, routing, and error handling."
tags: [skills, frontend, nextjs, app-router]
updated: 2026-06-01
date: 2026-06-01
---

# Next.js App Router Patterns (Agent Playbook)

This note is written for programming agents working in a Next.js App Router codebase.

## North Star

Prefer server-first composition, keep client components small and isolated, and make routing/error states explicit.

## Server vs Client Boundary

Use Server Components by default.

Use Client Components only when you need:
- State with hooks (useState/useEffect/useReducer)
- Browser-only APIs (localStorage, media devices, clipboard)
- DOM measurements, animations tied to layout
- Event handlers on interactive UI

Signals you crossed the boundary too early:
- A top-level layout/page is marked `"use client"`
- Large data fetching moved to the client without a strong reason
- Lots of props drilling of data that could have been fetched server-side

## Data Fetching Patterns

Prefer fetching in Server Components and passing plain data down.

Patterns:
- `page.tsx` fetches data and renders a server tree.
- A Client Component receives `initialData` and only handles interactions/mutations.
- Use Route Handlers for API endpoints when needed, but prefer server actions when appropriate for internal app mutations.

Anti-patterns:
- Fetching the same data in multiple siblings without sharing (consider lifting fetch to parent server component).
- Calling internal APIs over HTTP from server components (prefer direct function/module calls when in the same codebase).

## Caching and Revalidation (Mental Model)

Think in three layers:
- Request memoization (within a single render/request)
- Data cache (across requests)
- Route cache (HTML/RSC output)

Rules of thumb:
- If data must always be fresh, make freshness explicit (revalidate = 0 or dynamic routes).
- If data can be slightly stale, use time-based revalidation and show last-updated metadata if it matters.
- For user-specific data, be careful with caching and authentication boundaries.

## Loading, Error, Not Found

Always design the "triplet":
- `loading.tsx`: skeleton/placeholder that matches final layout
- `error.tsx`: recoverable UI with retry and helpful diagnostics (no secrets)
- `not-found.tsx`: clear "missing" UX with a way back

Agent checklist:
- Ensure errors are scoped (segment-level) not global unless necessary.
- Avoid blank screens: always render something in loading/error paths.

## Routing Patterns

Use route groups `(group)` to organize without affecting URL.

Use parallel routes `@slot` for dashboards with independently loading panes.

Use intercepting routes for modals where:
- direct URL should render a full page
- in-app navigation should render as a modal over the list

## Mutations

Prefer a single mutation strategy per codebase section:
- Server Actions for internal mutations
- Route Handler API for external consumers or cross-app boundaries

Requirements:
- Idempotency where possible
- Explicit optimistic UI rules (what can be optimistic and what cannot)
- Clear invalidation/revalidation strategy after mutation

## Safe Probes for Agents

Before changing architecture:
- Search for `"use client"` in `app/` and identify why each exists.
- Find `loading.tsx`, `error.tsx`, `not-found.tsx` coverage.
- Find data fetching entry points (ORM client, fetch wrappers).
- Locate any cache/revalidate helpers and centralize understanding.

