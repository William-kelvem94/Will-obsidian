---
tags: [mcp, infrastructure, automation, skills-mcp]
updated: 2026-04-27
title: "MCP Ecosystem & Servers"
date: 2026-04-27
---

# MCP Ecosystem & Servers

Model Context Protocol (MCP) is the bridge between the LLM and your local system.

## Padrões Avançados de MCP (Referência)
Para aprofundamento veja: [[advanced-mcp-integrations|Integrações MCP Avançadas e LLMs Locais]]

## Standard MCP Servers
- **Filesystem**: `read_file`, `write_file`, `list_dir`. The core of local coding assistance.
- **Terminal/Shell**: `run_command`. Critical for running tests, build scripts, and git operations.
- **Memory**: Transient and persistent memory layers for cross-session context.
- **Web/Browser**: `fetch_url`, `search_web`. For real-time research and documentation access.

## Advanced & Custom Servers
- **Obsidian Vault Server**: Custom MCP to search and link your personal knowledge base.
- **SQLite/Database Server**: Direct SQL execution for data-driven agent tasks.
- **GitHub API Server**: For repository management, PR reviews, and issue tracking.

## Configuration (JSON)
Common implementation in `claude_desktop_config.json` or `config.json`:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "D:/Documents/GitHub"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

## Security Best Practices
- **Path Restriction**: Only allow agents to access specific project directories.
- **Read-Only Mode**: Start with read-only access for new/untested agents.
- **Approval Loops**: Require manual confirmation for destructive commands (`rm`, `drop table`, etc.).
