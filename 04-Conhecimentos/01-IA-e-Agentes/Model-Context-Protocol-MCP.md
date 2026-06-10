---
title: Model Context Protocol (MCP)
tags: [mcp, architecture, ai-agents, protocol]
date: 2026-06-09
---

# Model Context Protocol (MCP)

The Model Context Protocol (MCP) is an open standard designed to standardize how Large Language Models (LLMs) interact with external data sources and tools. It decouples the model's reasoning capabilities from the specific implementation of data retrieval and tool execution.

## 1. Architectural Overview

MCP operates on a client-server architecture where an **MCP Client** (the LLM-powered application) connects to one or more **MCP Servers** (adapters for specific data sources or tools).

### Transport Layers
The protocol abstracts the underlying transport to allow for flexible deployments:
- **stdio**: Used for local processes where the client spawns the server as a child process. Communication occurs via standard input and output.
- **SSE (Server-Sent Events)**: Used for remote servers via HTTP. The client sends requests via POST, and the server streams updates/responses via SSE.

## 2. Core Primitive Definitions

### Resources
Resources are read-only data sources that the server exposes to the client.
- **URI-based**: Each resource is identified by a unique URI (e.g., `postgres://database/table`).
- **Templates**: Servers can define URI templates to allow clients to discover dynamic resources.

### Tools
Tools are executable functions that the LLM can invoke to perform actions in the real world.
- **Schema**: Tools are defined using JSON Schema to specify expected arguments and types.
- **Call Cycle**: `Client request` $\rightarrow$ `Server execution` $\rightarrow$ `Result returned to LLM` $\rightarrow$ `LLM integrates result into context`.

### Prompts
Pre-defined templates that guide the LLM on how to use the server's capabilities for specific workflows.

## 3. Implementation Guide: Building a Custom MCP Server

### Protocol Lifecycle
1. **Initialization**: The client sends an `initialize` request containing its capabilities. The server responds with its own capabilities and server information.
2. **Operation**: The client calls `resources/list`, `tools/call`, or `prompts/get`.
3. **Shutdown**: Graceful termination of the connection.

### Custom Tool Definition (TypeScript Example)
```typescript
const server = new McpServer({
  name: "Technical-Document-Manager",
  version: "1.0.0"
});

server.tool("query-docs", {
  query: z.string().describe("The search term for the technical docs"),
}, async ({ query }) => {
  const result = await db.search(query);
  return {
    content: [{ type: "text", text: result.join("\n") }]
  };
});
```

## 4. Security Model

### Sandbox and Permissions
MCP servers should operate under the principle of least privilege:
- **Execution Isolation**: Servers should be run in containers or restricted environments to prevent arbitrary code execution on the host.
- **Consent Layer**: The MCP Client must implement a "Human-in-the-loop" confirmation before executing any tool that modifies state (Write/Delete).
- **Transport Security**: When using SSE, TLS is mandatory to prevent man-in-the-middle attacks.

## 5. Advanced Edge Cases and Optimization

### Context Window Management
Since MCP can pull massive amounts of data into the context, servers should implement:
- **Pagination**: For resource listing.
- **Summarization**: Pre-processing large files before returning them to the client.
- **Differential Updates**: Only sending changed portions of a resource.

### Latency Reduction
- **Caching**: Implementing server-side caching for frequently accessed resources.
- **Parallel Tool Calls**: Allowing the client to invoke multiple tools in a single turn to minimize round-trips.

## References
- [MCP Specification](https://modelcontextprotocol.io)
- [JSON Schema Standard](https://json-schema.org)
