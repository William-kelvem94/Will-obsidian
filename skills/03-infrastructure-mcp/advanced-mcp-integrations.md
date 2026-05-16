---
title: "Integracoes MCP Avancadas e Infraestrutura Local de IA"
description: "Orquestracao multi-servidor MCP, composicao de ferramentas, agregacao de recursos e integracao com LLMs locais (Ollama)."
tags: [mcp, infrastructure, local-llm, ollama, skills-mcp, advanced]
date: 2026-04-27
updated: 2026-05-16
---

# Integracoes MCP Avancadas — Multi-Servidor, Composicao e Agregacao

Alem do servidor MCP basico, e possivel orquestrar multiplos servidores, compor ferramentas em workflows complexos e agregar recursos de diferentes fontes. Este documento explora padroes avancados para infrastrutura MCP em producao.

## Orquestracao Multi-Servidor

### Roteador de Ferramentas

Um servidor central que descobre e roteia chamadas para servidores especializados.

```python
from mcp import ClientSession
from mcp.client.stdio import stdio_client

class ToolRouter:
    def __init__(self):
        self.servers = {}

    async def register_server(self, name: str, command: list[str]):
        process = await create_process(command)
        read, write = process.stdout, process.stdin
        session = await ClientSession(read, write).__aenter__()
        tools = await session.list_tools()
        self.servers[name] = {"session": session, "tools": tools.tools}

    async def route_tool(self, tool_name: str, args: dict):
        for name, server in self.servers.items():
            for tool in server["tools"]:
                if tool.name == tool_name:
                    return await server["session"].call_tool(tool_name, args)
        raise ValueError(f"Tool {tool_name} nao encontrada em nenhum servidor")

router = ToolRouter()
await router.register_server("vault", ["python", "-m", "vault_mcp"])
await router.register_server("db", ["python", "-m", "db_mcp"])
result = await router.route_tool("search_vault", {"query": "machine learning"})
```

## Composicao de Ferramentas

### Pipeline de Ferramentas Encadeadas

```python
class ToolComposer:
    def __init__(self, router: ToolRouter):
        self.router = router

    async def pipeline_rag(self, query: str) -> str:
        # Passo 1: Buscar notas relevantes
        notes = await self.router.route_tool("search_vault", {
            "query": query, "limit": 5
        })

        # Passo 2: Extrair contexto relevante
        context = await self.router.route_tool("extract_relevant", {
            "notes": notes, "query": query
        })

        # Passo 3: Consultar memoria do usuario
        memory = await self.router.route_tool("get_memory", {
            "query": query
        })

        # Passo 4: Gerar resposta com LLM local
        response = await self.router.route_tool("llm_complete", {
            "system": "Use o contexto e a memoria para responder.",
            "context": context,
            "memory": memory,
            "query": query
        })

        return response
```

## Agregacao de Recursos

### Resource Aggregator

Agrega recursos de multiplos servidores em uma resposta unificada.

```python
@app.list_resources()
async def list_resources() -> list[Resource]:
    vault_notes = await vault_session.list_resources()
    db_tables = await db_session.list_resources()
    memory_items = await memory_session.list_resources()

    return [
        Resource(uri=f"aggregated://notes/{n.uri.split('/')[-1]}", name=n.name)
        for n in vault_notes
    ] + [
        Resource(uri=f"aggregated://tables/{t.name}", name=t.name)
        for t in db_tables
    ]
```

## Integracao com LLMs Locais (Ollama)

### Proxy entre MCP e Ollama

```python
import httpx
from mcp.server import Server

app = Server("ollama-proxy")

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "llm_complete":
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": arguments.get("model", "qwen2.5-coder:7b"),
                    "prompt": arguments["prompt"],
                    "system": arguments.get("system", ""),
                    "stream": False,
                    "options": {"temperature": 0.3, "num_predict": 2048}
                }
            )
            data = response.json()
            return [TextContent(type="text", text=data["response"])]
```

## Cache Distribuido entre Servidores

```python
from redis import asyncio as aioredis

class MCPSessionCache:
    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.redis = aioredis.from_url(redis_url)

    async def cache_tool_result(self, tool: str, args: dict, result: str, ttl: int = 300):
        key = f"mcp:cache:{tool}:{hash(json.dumps(args, sort_keys=True))}"
        await self.redis.setex(key, ttl, result)

    async def get_cached(self, tool: str, args: dict) -> str | None:
        key = f"mcp:cache:{tool}:{hash(json.dumps(args, sort_keys=True))}"
        return await self.redis.get(key)
```

## Monitoramento de Servidores MCP

```python
import logging
from datetime import datetime

class MCPMonitor:
    def __init__(self):
        self.metrics = {
            "tool_calls": 0,
            "errors": 0,
            "latency_ms": []
        }

    async def monitor_call(self, tool: str, args: dict, call_fn):
        start = datetime.now()
        self.metrics["tool_calls"] += 1
        try:
            result = await call_fn(tool, args)
            elapsed = (datetime.now() - start).total_seconds() * 1000
            self.metrics["latency_ms"].append(elapsed)
            return result
        except Exception as e:
            self.metrics["errors"] += 1
            logging.error(f"Falha na tool {tool}: {e}")
            raise
```

## Referencias

- [[mcp-servers|MCP Servers]] — Fundamentos e configuracao basica
- [[skills/04-knowledge-systems/memory-management|Gestao de Memoria]] — Memoria persistente via MCP
- [[skills/04-knowledge-systems/advanced-rag-strategies|RAG Avancado]] — Pipeline RAG via MCP
- [[skills/devops/Observabilidade|Observabilidade]] — Monitoramento de servidores MCP
