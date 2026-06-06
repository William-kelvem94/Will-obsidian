---
title: "Testing UI Practical (Agents)"
category: "Frontend"
level: 3
description: "Practical UI testing for agents: unit vs integration vs e2e, mocking strategy, and stable selectors."
tags: [skills, frontend, testing]
updated: 2026-06-05
date: 2026-06-01
---

# Testing UI Practical (Agents)

## Testing Pyramid (UI Reality)

Aim for:
- Few unit tests for pure helpers and small logic
- More integration/component tests for user flows inside the app
- A small number of E2E tests for critical paths

## What To Test

Test outcomes, not implementation:
- UI shows expected content
- Buttons trigger the expected action
- Errors are displayed correctly
- Disabled/loading states behave

Avoid brittle tests:
- Snapshot tests for large UI trees
- Tests that depend on CSS classes or exact markup unless needed

## Selectors

Prefer:
- Role-based queries (buttons by label)
- Accessible names
- `data-testid` only as a fallback for complex widgets

## Mocking Strategy

Rules:
- Mock the network at one layer (not multiple).
- Keep fixtures small and representative.
- Do not hardcode time; use fake timers only when necessary.

## E2E Stability

Rules:
- Keep tests deterministic (seed data, stable IDs).
- Avoid sleeps; wait for conditions.
- Verify accessibility-relevant behavior (focus, keyboard) in at least one test.

## Agent Workflow

- Add tests for the bug/feature you changed.
- Run the narrowest test set first.
- If flakiness appears, fix the cause (timing, selectors, dependency on animations).

