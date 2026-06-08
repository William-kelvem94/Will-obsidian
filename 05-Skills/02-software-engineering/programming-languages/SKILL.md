---
name: programming-languages
description: Development best practices, guidelines, and standards across major languages (Python, Go, Rust, TypeScript).
title: "Programming Languages & Paradigms"
date: 2026-06-08
tags: [skills, programming, polyglot, python, rust, typescript, go, skills-eng]
updated: 2026-06-08
---

# Programming Languages & Paradigms Skill

Use this skill when choosing language-specific features, formatting guidelines, package managers, or optimization strategies.

## Multi-Language Guidelines

### Python
- Follow PEP 8 style guide.
- Use explicit type hinting and static analysis (mypy, ruff).
- Manage dependencies with `uv`, `poetry`, or virtual environments (`venv`).

### Go
- Keep code idiomatic: return errors explicitly, avoid unnecessary abstractions.
- Use go routines and channels for concurrency safely.
- Format strictly with `gofmt`.

### Rust
- Leverage the ownership and borrow checker model for memory safety.
- Write expressive code using pattern matching, enums, and Option/Result types.
- Format and check with `cargo fmt` and `cargo clippy`.

### TypeScript / JavaScript
- Strict type checking enabled (`strict: true` in `tsconfig.json`).
- Prefer async/await over raw Promises or callbacks.
- Use modern package managers (`npm`, `pnpm`, `yarn`) and runtimes (`node`, `bun`, `deno`).
