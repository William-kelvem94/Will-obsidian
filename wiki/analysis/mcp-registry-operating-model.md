---
title: "MCP Registry Operating Model"
date: 2026-06-10
updated: 2026-06-10
type: analysis
status: active
tags: [mcp, registry, governance, tools]
summary: "Operating model for documenting MCPs with maturity, risk, and tool contracts."
---

# MCP Registry Operating Model

## Required fields

- name;
- purpose;
- transport;
- auth;
- read/write scope;
- sensitivity;
- tool list;
- owner;
- maturity;
- failure mode;
- audit logging.

## Operating rules

- default to read-only when possible;
- keep write paths narrow;
- define rollback before release;
- separate local tools from external tools;
- review tool contracts before adding automation.

