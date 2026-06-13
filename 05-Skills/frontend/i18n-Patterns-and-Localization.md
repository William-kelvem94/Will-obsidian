---
title: "i18n Patterns and Localization (Agents)"
category: "Frontend"
level: 3
description: "Patterns for internationalization: message organization, formatting, pluralization, dates, and routing."
tags: [skills, frontend, i18n, localization]
updated: 2026-06-13
date: 2026-06-01
---

# i18n Patterns and Localization (Agents)

## Principles

- Separate messages from code.
- Avoid concatenated strings.
- Make locale explicit where it affects formatting.

## Message Organization

Preferred:
- Namespace by feature: `billing.*`, `tenants.*`, `auth.*`
- Keep short, stable keys.
- Add developer notes for ambiguous strings.

Avoid:
- Keys that include UI copy (hard to change).
- Duplicated keys across features with slightly different meaning.

## Formatting

Rules:
- Use locale-aware date/number formatting.
- Treat currency formatting as a function of locale + currency code.
- Handle pluralization with the i18n framework, not manual `if` strings.

## RTL and Layout

If RTL is a possibility:
- Avoid directional assumptions (`ml-2` vs logical spacing utilities if available).
- Icons with direction should flip when appropriate.

## Routing and Locale

Decide one strategy:
- Locale prefix in URL (`/en/...`, `/pt/...`)
- Locale stored in cookie/session and resolved server-side

Agent checklist:
- Ensure links preserve locale.
- Ensure server-side rendering uses the correct locale.
- Avoid caching bugs mixing locales.

## Safe Agent Steps

- Add a single key and wire it end-to-end.
- Confirm fallback behavior when key missing.
- Confirm dates/numbers render correctly in at least two locales.

