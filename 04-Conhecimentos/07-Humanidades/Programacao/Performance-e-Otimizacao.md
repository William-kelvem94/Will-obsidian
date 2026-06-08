---
title: "Performance e Otimização"
date: 2026-05-16
area: "Programação e Engenharia de Software"
tags: [conhecimento, programacao, performance, otimizacao, profiling]
related: ["04-Conhecimentos/07-Humanidades/Programacao/Banco-de-Dados"]
aliases: ["Performance Optimization", "Profiling", "Caching"]
---

## Visão Geral

Performance é sobre latência, throughput e utilização de recursos. Otimizar significa encontrar gargalos com dados (não achismo) e aplicar técnicas que maximizem eficiência dentro das restrições do sistema.

## Profiling

Antes de otimizar, **meça**. Nunca otimize sem dados.

### cProfile (Python)

```python
import cProfile
import pstats

# Perfilamento básico
def processar_dados():
    total = 0
    for i in range(1000000):
        total += i ** 2
    return total

cProfile.run("processar_dados()", sort="cumtime")

# Salvar para análise
profiler = cProfile.Profile()
profiler.enable()
processar_dados()
profiler.disable()
profiler.dump_stats("perfil.prof")

# Análise programática
stats = pstats.Stats("perfil.prof")
stats.sort_stats(pstats.SortKey.CUMULATIVE)
stats.print_stats(20)  # Top 20
```

```bash
# SnakeViz — visualização web
python -m snakeviz perfil.prof

# py-spy — profiler para produção (sem modificar código)
py-spy record -o profile.svg --pid 12345
py-spy top --pid 12345

# flamegraph
py-spy record -o flamegraph.svg --pid 12345 --duration 30
```

### Profiling em Produção

```python
# Context manager para profiling pontual
import contextlib
import cProfile
import time

@contextlib.contextmanager
def profile_block(nome: str):
    prof = cProfile.Profile()
    prof.enable()
    inicio = time.perf_counter()
    try:
        yield
    finally:
        prof.disable()
        duracao = time.perf_counter() - inicio
        stats = pstats.Stats(prof)
        stats.sort_stats(pstats.SortKey.CUMULATIVE)
        stats.print_stats(10)
        print(f"=== {nome}: {duracao:.3f}s ===")

# Uso
with profile_block("processamento_lote"):
    processar_lote(dados)
```

### APM Tools

```yaml
# Datadog APM — tracing distribuído
# New Relic, Dynatrace, Sentry Performance
# OpenTelemetry — padrão aberto para observabilidade
```

## Caching

### Estratégias

```
┌──────────────────────────────────────────────┐
│            Browser Cache (HTTP)               │
│   Cache-Control, ETag, Expires                │
├──────────────────────────────────────────────┤
│            CDN (CloudFront, Cloudflare)        │
│   Edge caching, cache invalidation             │
├──────────────────────────────────────────────┤
│            Application Cache (Redis/Memcached) │
│   In-memory, distributed, cache-aside          │
├──────────────────────────────────────────────┤
│            Database Cache (Buffer Pool)        │
│   PostgreSQL shared_buffers, InnoDB pool       │
└──────────────────────────────────────────────┘
```

### Redis Cache

```python
# Cache-aside pattern
import redis.asyncio as redis
import json
from typing import Optional

class CacheService:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
        self.TTL_PADRAO = 300

    async def get_or_compute(
        self, key: str, compute_func, ttl: Optional[int] = None
    ):
        # Tentar cache primeiro
        cached = await self.redis.get(key)
        if cached is not None:
            return json.loads(cached)

        # Calcular valor
        value = await compute_func()

        # Armazenar em cache
        await self.redis.setex(
            key, ttl or self.TTL_PADRAO, json.dumps(value)
        )
        return value

    async def invalidate(self, pattern: str):
        """Invalida cache por padrão"""
        cursor = 0
        while True:
            cursor, keys = await self.redis.scan(cursor, match=pattern)
            if keys:
                await self.redis.delete(*keys)
            if cursor == 0:
                break
```

```python
# Cache Stampede — proteção com mutex
import aioredlock

lock = aioredlock.Aioredlock([redis_instance])

async def get_or_compute_with_mutex(key: str, compute_func, ttl: int = 300):
    cached = await redis.get(key)
    if cached is not None:
        return json.loads(cached)

    # Lock distribuído — só um processo computa
    async with await lock.lock(f"lock:{key}", lock_timeout=10):
        # Double-check após adquirir lock
        cached = await redis.get(key)
        if cached is not None:
            return json.loads(cached)

        value = await compute_func()
        await redis.setex(key, ttl, json.dumps(value))
        return value
```

### HTTP Caching

```python
# FastAPI — cache control
from fastapi import FastAPI, Response
from datetime import timedelta

app = FastAPI()

@app.get("/api/produtos")
async def listar_produtos(response: Response):
    response.headers["Cache-Control"] = "public, max-age=3600, stale-while-revalidate=60"
    response.headers["ETag"] = f'"{hash(produtos)}"'
    return produtos
```

```typescript
// Next.js — Cache de página estática
export const dynamic = 'force-static';  // SSG
export const revalidate = 3600;        // ISR — revalida a cada hora
```

### CDN

```typescript
// Cloudflare Workers — cache personalizado
addEventListener('fetch', (event) => {
    event.respondWith(handleRequest(event.request));
});

async function handleRequest(request: Request): Promise<Response> {
    const url = new URL(request.url);
    const cacheKey = new Request(url.toString(), request);

    const cache = caches.default;
    let response = await cache.match(cacheKey);

    if (!response) {
        response = await fetch(request);
        // Cache por 1 hora no edge
        response = new Response(response.body, response);
        response.headers.set('Cache-Control', 'public, max-age=3600');
        event.waitUntil(cache.put(cacheKey, response.clone()));
    }

    return response;
}
```

## Otimização de Queries SQL

### EXPLAIN ANALYZE

```sql
-- Identificar scans sequenciais em tabelas grandes
EXPLAIN (ANALYZE, BUFFERS, TIMING)
SELECT p.*, u.nome
FROM pedidos p
JOIN usuarios u ON u.id = p.usuario_id
WHERE p.criado_em > '2025-01-01'
ORDER BY p.total DESC
LIMIT 50;

-- O que procurar no output:
-- "Seq Scan on pedidos" → precisa de índice
-- "Sort Method: external merge" → falta índice de ordenação
-- "actual rows=1" vs "estimated rows=1000" → estatísticas desatualizadas
-- "Buffers: shared hit=5" vs "shared read=1000" → dados não estão em cache
```

### Índices para Performance

```sql
-- Índice composto com ordem correta
CREATE INDEX idx_pedidos_status_data
    ON pedidos (status, criado_em DESC);

-- Index-only scan: incluir colunas selecionadas
CREATE INDEX idx_cobrindo_pedidos
    ON pedidos (status, criado_em DESC)
    INCLUDE (total, usuario_id);

-- Índices parciais para consultas frequentes
CREATE INDEX idx_pedidos_abertos
    ON pedidos (criado_em DESC)
    WHERE status IN ('pendente', 'processando');
```

### N+1 Problem

```python
# Detectando N+1 no Django
from django.db import connection
from django.test import override_settings

# Antes — 1 + 100 queries
autores = Autor.objects.all()
for autor in autores:  # 1 query
    livros = autor.livros.all()  # N queries
    print(len(livros))

# Depois — 2 queries
autores = Autor.objects.prefetch_related('livros').all()

# N+1 no SQLAlchemy
from sqlalchemy.orm import selectinload

# Antes
stmt = select(Usuario)
usuarios = session.scalars(stmt)
for u in usuarios:
    print(len(u.posts))  # N+1

# Depois
stmt = select(Usuario).options(selectinload(Usuario.posts))
```

### Paginação Eficiente

```sql
-- ❌ OFFSET-based (lento em páginas profundas)
SELECT * FROM pedidos ORDER BY id LIMIT 20 OFFSET 100000;

-- ✅ Keyset (cursor-based) pagination
SELECT * FROM pedidos
WHERE (criado_em, id) < ('2026-05-16', 50000)
ORDER BY criado_em DESC, id DESC
LIMIT 20;
```

## Network

### Latency e Bandwidth

```
Latency (1 byte):
  L1 cache:     ~0.5 ns
  L2 cache:     ~7 ns
  RAM:          ~100 ns
  SSD:          ~150 μs
  Network (DC): ~500 μs
  Network (cross-region): ~50-200 ms
```

### Connection Pooling

```python
# SQLAlchemy — pool de conexões
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://user:pass@host/db",
    pool_size=20,           # conexões mantidas abertas
    max_overflow=10,        # conexões extras sob demanda
    pool_timeout=30,        # tempo máximo esperando conexão
    pool_recycle=3600,      # reciclar conexões velhas
    pool_pre_ping=True,     # verificar conexão antes de usar
)
```

```typescript
// Node.js — conexão HTTP com keep-alive
import http from 'http';
import https from 'https';

const agent = new http.Agent({
    keepAlive: true,
    keepAliveMsecs: 1000,
    maxSockets: 50,
    maxFreeSockets: 10,
    timeout: 30000,
});

const response = await fetch('https://api.exemplo.com', {
    agent,
});
```

### gRPC vs REST

```protobuf
// gRPC — binary protocol (Protocol Buffers)
// 10x mais rápido que JSON em serialização

service UsuarioService {
    rpc BuscarUsuario (BuscarRequest) returns (Usuario);
    rpc ListarUsuarios (ListarRequest) returns (stream Usuario);
}

message BuscarRequest {
    int32 id = 1;
}

message Usuario {
    int32 id = 1;
    string nome = 2;
    string email = 3;
}
```

## Algoritmos e Estruturas de Dados

### Big O Analysis

```python
# Escolha a estrutura certa para a operação dominante
# Lista: O(1) append, O(n) insert/delete no meio
# Dict/Set: O(1) lookup, insert, delete
# Heapq: O(log n) push/pop, O(1) min
# Deque: O(1) append/pop em ambas pontas

from collections import deque
import heapq

# LRU Cache — OrderedDict mantém ordem de inserção
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # O(1)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # O(1)
```

### Otimização de Loops

```python
import numpy as np

# ❌ Loop Python puro
def soma_quadrados_py(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

# ✅ NumPy vectorized (SIMD + C)
def soma_quadrados_np(n):
    arr = np.arange(n, dtype=np.float64)
    return np.sum(arr ** 2)

# ❌ Concatenação em loop
resultados = []
for item in dados:
    resultados += [item * 2]  # O(n²) — cria nova lista

# ✅ List comprehension
resultados = [item * 2 for item in dados]  # O(n)

# ❌ Lookup em lista
itens = list(range(1000000))
"alvo" in itens  # O(n)

# ✅ Lookup em set
itens_set = set(itens)
"alvo" in itens_set  # O(1)
```

## Memória

### Garbage Collection

```python
# Python — Garbage Collection cíclico
import gc

gc.set_threshold(700, 10, 10)  # geração 0, 1, 2
gc.collect()  # força coleta manual

# Desabilitar GC (útil para servidores单线程 de curta duração)
gc.disable()

# Memory leak: closures com referências cíclicas
def criar_leak():
    dados = []
    def adicionar(item):
        dados.append(item)  # closure mantém referência a dados
    return adicionar

# Profiling de memória
from memory_profiler import profile

@profile
def processar_grande():
    dados = [x for x in range(10000000)]
    return sum(dados)
```

```bash
# Filbert — memory profiler interativo
pip install filprofiler
python -m filprofiler run meu_script.py

# objgraph — visualizar referências
pip install objgraph
```

### Object Pooling

```python
# Pool de objetos para reduzir alocação
from queue import Queue

class ConnectionPool:
    def __init__(self, factory, size: int = 10):
        self._pool = Queue(maxsize=size)
        for _ in range(size):
            self._pool.put(factory())

    def acquire(self, timeout: float = 5.0):
        return self._pool.get(timeout=timeout)

    def release(self, conn):
        self._pool.put(conn)

# Uso com context manager
from contextlib import contextmanager

@contextmanager
def get_connection(pool):
    conn = pool.acquire()
    try:
        yield conn
    finally:
        pool.release(conn)
```

## I/O Bound vs CPU Bound

| Tipo | Característica | Solução |
|------|---------------|---------|
| **CPU Bound** | Processador é o gargalo | Paralelismo real (multiprocessing), algoritmos eficientes, C extensions |
| **I/O Bound** | Espera por disco/rede | Async I/O, threads, caching, connection pooling |

```python
import asyncio
import aiohttp
from concurrent.futures import ProcessPoolExecutor
import time

# I/O Bound — async I/O
async def fetch_urls(urls: list[str]) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_one(session, url) for url in urls]
        return await asyncio.gather(*tasks)

async def fetch_one(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()

# CPU Bound — multiprocessing
def compute_intensive(dados: list[float]) -> list[float]:
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(processar_lote, dados))
    return results

# PyPy — JIT compiler para Python puro (2-10x mais rápido em CPU bound)
# Cython — extensões C para Python
# Numba — JIT para NumPy
```

```python
# FastAPI — async para I/O, sync para CPU
from fastapi import FastAPI
from concurrent.futures import ThreadPoolExecutor
import asyncio

app = FastAPI()
executor = ThreadPoolExecutor(max_workers=4)

@app.get("/api/relatorio")
async def gerar_relatorio():
    # I/O — async
    dados = await buscar_dados_banco()

    # CPU — executa em thread separada para não bloquear event loop
    loop = asyncio.get_event_loop()
    resultado = await loop.run_in_executor(executor, processar_dados, dados)

    return resultado
```

## Lazy Loading

```python
# Generator — lazy evaluation
def ler_grande_arquivo(caminho: str):
    with open(caminho, 'r') as f:
        for linha in f:
            yield linha.strip()

# Processa linha por linha sem carregar tudo em memória
for linha in ler_grande_arquivo("dados_100gb.csv"):
    processar(linha)

# Lazy property — computa apenas quando acessado
class Relatorio:
    @property
    def total_vendas(self):
        # Só computa quando acessado
        return sum(v.valor for v in self.vendas)
```

```javascript
// JavaScript — IntersectionObserver para lazy loading de imagens
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src;
            observer.unobserve(img);
        }
    });
});

document.querySelectorAll('img[data-src]').forEach(img => {
    observer.observe(img);
});
```

## Benchmarking e Load Testing

### Locust

```python
# locustfile.py
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task(3)
    def ver_produtos(self):
        self.client.get("/api/produtos")

    @task(1)
    def criar_pedido(self):
        self.client.post("/api/pedidos", json={
            "produto_id": 1,
            "quantidade": 2
        })

    @task
    def buscar_usuario(self):
        with self.client.get(
            "/api/usuario/1",
            catch_response=True,
            name="buscar_usuario"
        ) as response:
            if response.status_code != 200:
                response.failure(f"Status: {response.status_code}")
```

```bash
locust -f locustfile.py --host=https://api.exemplo.com --users=100 --spawn-rate=10
# Abre http://localhost:8089 para controle em tempo real
```

### k6

```javascript
// k6 load test
import http from 'k6/http';
import { check, sleep } from 'k6';
import { Counter, Trend } from 'k6/metrics';

const myTrend = new Trend('request_duration');

export const options = {
    stages: [
        { duration: '2m', target: 100 },  // ramp up
        { duration: '5m', target: 100 },  // steady
        { duration: '2m', target: 0 },     // ramp down
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'],  // 95% das requests < 500ms
        http_req_failed: ['rate<0.01'],    // < 1% de erro
    },
};

export default function () {
    const payload = JSON.stringify({ email: 'teste@teste.com', senha: '123' });
    const params = {
        headers: { 'Content-Type': 'application/json' },
        tags: { type: 'login' },
    };

    const res = http.post('https://api.exemplo.com/login', payload, params);

    check(res, {
        'status 200': (r) => r.status === 200,
        'resposta < 300ms': (r) => r.timings.duration < 300,
    });

    myTrend.add(res.timings.duration);
    sleep(1);
}
```

### wrk (HTTP Benchmark)

```bash
wrk -t12 -c400 -d30s --latency https://api.exemplo.com/produtos
# Result: 12000 requests/sec, Latency p99 45ms
```

## Anti-patterns

```python
# ❌ Premature optimization — otimizar sem medir
# ❌ Magic numbers sem explicação
# ❌ Over-engineering para cenários que não existem
# ❌ Cache sem estratégia de invalidação
# ❌ Índices em todas as colunas sem análise de uso

# ❌ N+1 em GraphQL
# query {
#   usuarios {
#     nome
#     posts {  -- N+1: resolve 1 usuario + N posts
#       titulo
#     }
#   }
# }
# ✅ DataLoader para batch + cache
```

## Referências

- **Martin Kleppmann — "Designing Data-Intensive Applications"** (2017). Capítulos sobre armazenamento, replicação, particionamento.
- **Brendan Gregg — "Systems Performance: Enterprise and the Cloud"** (2020). O livro definitivo sobre performance de sistemas.
- **Cary Millsap — "Thinking Clearly About Performance"** (2010). Abordagem metódica para otimização.
- **"The Art of PostgreSQL"** — Dimitri Fontaine. Otimização de queries SQL.
- **"High Performance Browser Networking"** — Ilya Grigorik (2013). Performance web e de rede.
- **"Database Internals"** — Alex Petrov (2019). Estruturas de armazenamento e indexação.
- **"Effective Python: 90 Specific Ways to Write Better Python"** — Brett Slatkin. Itens sobre performance.
- **Flamegraph** — Brendan Gregg: https://www.brendangregg.com/flamegraphs.html
- **Locust** — https://locust.io/
- **k6** — https://k6.io/
- **py-spy** — https://github.com/benfred/py-spy
