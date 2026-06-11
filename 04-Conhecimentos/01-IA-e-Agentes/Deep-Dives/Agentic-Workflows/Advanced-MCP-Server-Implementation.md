---
type: technical-deep-dive
category: agentic-workflows
tags: [mcp, tool-calling, server-implementation, state-management]
links: 
  - "[[01-IA-e-Agentes/README]]"
  - "[[02-Engenharia-de-Software]]"
---

# Advanced MCP Server Implementation

The Model Context Protocol (MCP) standardizes the interface between LLMs and external data/tools, decoupling the intelligence layer from the execution environment.

## 1. Tool-Calling Schemas
MCP tools utilize JSON Schema to define input parameters, ensuring strict typing and validation before execution.

### Schema Design Principles
- **Strong Typing**: Avoid `string` for everything; use `enum` for fixed options and `number` for quantitative values.
- **Descriptions**: Detailed `description` fields are critical as they serve as the "prompt" for the LLM to understand tool utility.
- **Required Fields**: Clearly delineate mandatory vs. optional parameters to reduce LLM hallucination in tool calls.

## 2. Resource Templates
Resources allow agents to browse and retrieve specific data entities using URI-based templates.

### Implementation
- **URI Patterns**: Implementation of patterns like `obsidian://vault/note/{title}`.
- **Dynamic Resolution**: The server must resolve the template variable `{title}` into a physical file path or database query.
- **MIME Type Mapping**: Correct mapping of content types (e.g., `text/markdown`, `application/json`) to ensure the LLM parses the returned data correctly.

## 3. Secure State Management
Maintaining state across multiple tool calls requires balancing persistence with security.

### State Strategies
- **Stateless Execution**: The preferred model where all required context is passed in the tool call.
- **Session-Based State**: Using session IDs to track a sequence of operations (e.g., a multi-step database migration).
- **Sandboxing**: Execution of tool logic in isolated containers (Docker/gVisor) to prevent Remote Code Execution (RCE) vulnerabilities.

### Security Constraints
- **Input Sanitization**: Strict validation of all inputs to prevent injection attacks.
- **Permission Scoping**: implementing granular access control lists (ACLs) to ensure the agent can only access authorized resources.
- **Audit Logging**: Detailed telemetry of every tool invocation, including inputs and outputs.
