---
tags: [mcp, infrastructure, automation, skills-mcp, server]
updated: 2026-06-10
title: "MCP Ecosystem & Servers"
date: 2026-04-27
---

# MCP Ecosystem & Servers

Model Context Protocol (MCP) e a ponte padronizada entre LLMs e o sistema local. Este documento cobre implementacao de servidores, opcoes de transporte, seguranca e depuracao.

## Arquitetura MCP

O MCP segue um modelo cliente-servidor onde:
- **Cliente MCP**: Claude Desktop, Cursor, ou agente customizado (ex: JARVIS)
- **Servidor MCP**: Processo local (Python/Node) que expoe ferramentas e recursos
- **Transporte**: Camada de comunicacao entre cliente e servidor

## Implementacao de Servidor MCP

### Servidor em Python (SDK Oficial)

```python
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import json

app = Server("jarvis-tools")

@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="search_vault",
            description="Busca notas no vault do Obsidian por similaridade semantica",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Consulta em linguagem natural"},
                    "limit": {"type": "integer", "description": "Maximo de resultados", "default": 5}
                },
                "required": ["query"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "search_vault":
        results = await semantic_search(arguments["query"], arguments.get("limit", 5))
        return [TextContent(type="text", text=json.dumps(results, indent=2))]
    raise ValueError(f"Tool desconhecida: {name}")

async def main():
    async with stdio_server() as (read, write):
        await app.run(read, write)
```

### Servidor em Node.js

```javascript
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';

const server = new Server(
  { name: 'vault-server', version: '1.0.0' },
  { capabilities: { tools: {} } }
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [{
    name: 'read_note',
    description: 'Le o conteudo de uma nota do Obsidian',
    inputSchema: {
      type: 'object',
      properties: {
        path: { type: 'string', description: 'Caminho relativo da nota' }
      },
      required: ['path']
    }
  }]
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === 'read_note') {
    const content = await fs.readFile(request.params.arguments.path, 'utf-8');
    return { content: [{ type: 'text', text: content }] };
  }
  throw new Error('Tool not found');
});

const transport = new StdioServerTransport();
await server.connect(transport);
```

## Opcoes de Transporte

### STDIO (Padrao)

Cliente e servidor comunicam via stdin/stdout. Ideal para processos locais.

```json
{
  "mcpServers": {
    "jarvis": {
      "command": "python",
      "args": ["-m", "jarvis.mcp.server"]
    }
  }
}
```

### SSE (Server-Sent Events)

Permite conexao remota via HTTP. Util para servidores em rede.

```python
from mcp.server.sse import SseServerTransport

sse = SseServerTransport("/messages")

@app.get("/sse")
async def handle_sse(request: Request):
    async with sse.connect_sse(request) as (read, write):
        await app.run(read, write)
```

## Seguranca

- **Restricao de Caminhos**: Limite acesso a diretorios especificos do projeto
- **Modo Read-Only**: Inicie com acesso somente leitura para agentes nao testados
- **Aprovacao Manual**: Exija confirmacao para comandos destrutivos (rm, DROP TABLE)
- **Sandboxing**: Execute servidores em containers Docker para isolamento
- **Validacao de Input**: Nunca confie nos argumentos recebidos — valide e sanitize

### Configuracao Segura

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "D:/GitHub"],
      "env": {
        "MCP_READ_ONLY": "true"
      }
    }
  }
}
```

## Depuracao

- Habilite logging verbose com `--debug` ou variavel `MCP_LOG_LEVEL=debug`
- Use `MCP Inspector` para testar ferramentas isoladamente: `npx @modelcontextprotocol/inspector`
- Simule chamadas de ferramentas via linha de comando para testar logicas
- Monitore erros de conexao e timeout no cliente MCP

### Inspetor MCP

```bash
npx @modelcontextprotocol/inspector python -m jarvis.mcp.server
```

## Servidores MCP Recomendados

- **Filesystem**: Acesso ao sistema de arquivos local
- **Memory**: Memoria transiente e persistente entre sessoes
- **Web**: Fetch de URLs e busca na web
- **Database**: Execucao de SQL em banco local
- **GitHub**: Gerenciamento de repositorios, PRs e issues
- **Obsidian Vault**: Busca e leitura de notas do vault

## Referencias

- [[advanced-mcp-integrations|Integracoes MCP Avancadas]] — Orquestracao multi-servidor
- [[05-Skills/04-knowledge-systems/INDEX|Knowledge Systems]] — RAG e memoria via MCP
- [[05-Skills/devops/Kubernetes|Kubernetes]] — Orquestracao de servidores MCP em container
