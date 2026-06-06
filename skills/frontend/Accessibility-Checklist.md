---
title: "Accessibility Checklist (Agents)"
category: "Frontend"
level: 2
description: "A practical a11y checklist for UI changes: keyboard, focus, semantics, ARIA, color contrast, and screen readers."
tags: [skills, frontend, a11y, accessibility]
updated: 2026-06-05
date: 2026-06-01
---

# Accessibility Checklist (Agents)

Use this checklist before marking a UI PR as ready.

## Keyboard

- All interactive elements are reachable by Tab.
- Logical tab order (no traps).
- Enter/Space activate buttons and controls properly.
- Escape closes dialogs/menus where appropriate.

## Focus

- Visible focus ring exists (`:focus-visible`).
- Focus is moved into dialogs on open and restored on close.
- No focus loss after async updates.

## Semantics

- Use `button` for actions, `a` for navigation.
- Headings follow a logical order (no skipping levels unnecessarily).
- Form fields have labels, not just placeholders.
- Lists/tables use proper HTML elements.

## ARIA (Use Sparingly)

Rules:
- Prefer native semantics first.
- Use ARIA only when necessary.
- Do not lie: ARIA must match actual behavior.

Common needs:
- `aria-label` for icon-only buttons
- `aria-expanded`, `aria-controls` for disclosure widgets
- `aria-describedby` linking inputs to help/error text

## Contrast and Motion

- Text contrast is sufficient for normal and small text.
- Non-text UI elements (icons, focus ring) have visible contrast.
- Respect reduced motion preferences for animations.

## Errors and Status

- Validation errors are announced and visible.
- Async actions show status (loading, success, failure) without relying only on color.
- Toasts are not the only way to communicate critical errors.

## Agent "Quick Tests"

- Test with keyboard only for the main flow.
- Use browser accessibility tree inspection for key components.
- Run any configured a11y lint/tests if available.

