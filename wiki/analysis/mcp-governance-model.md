---
title: "MCP Governance Model"
date: 2026-06-10
updated: 2026-06-10
type: analysis
status: active
tags: [mcp, governance, security, tools]
summary: "Governance model for expanding MCPs without creating unsafe tool sprawl."
---

# MCP Governance Model

## Model

MCPs should be organized by:

- read-only retrieval tools;
- audited write tools;
- external connectors;
- orchestration tools;
- high-sensitivity tools.

## Governance rules

- every tool needs a contract;
- every write needs scope and rollback;
- sensitive tools need explicit classification;
- external integrations need logs and ownership;
- default posture should be read-only where possible.

