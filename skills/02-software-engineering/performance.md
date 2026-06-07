---
tags: [performance, profiling, caching, load-testing, monitoring, optimization, skills-eng]
updated: 2026-06-07
title: "Performance Engineering - Full-Stack Performance"
date: 2026-06-01
---

# Performance Engineering

Engenharia de performance full-stack. Este guia cobre desde profiling de aplicacoes ate load testing em producao, com exemplos praticos em Python e JavaScript. Referencia para identificar e resolver gargalos antes que afetem usuarios.

## Taxonomia de Topicos

- Profiling de aplicacoes
- Otimizacao de database queries
- Memory profiling e leak detection
- Estrategias de caching
- Padroes async e concorrencia
- Load testing (k6, Locust)
- Performance budgets
- Frontend performance
- Backend performance
- APM tools

## Profiling de Aplicacoes

### Python - cProfile

```python
import cProfile
import pstats
import io

def funcao_lenta():
    """Exemplo de funcao para profiling."""
    total = 0
    for i in range(1000000):
        total += i
    return total

# Profiling programatico
def profile_function(func, *args, **kwargs):
    profiler = cProfile.Profile()
    profiler.enable()
    result = func(*args, **kwargs)
    profiler.disable()

    # Gera relatorio
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream)
    stats.sort_stats("cumulative")
    stats.print_stats(20)  # Top 20 funcoes

    print(stream.getvalue())
    return result

# Uso
profile_function(funcao_lenta)

# Profiling via linha de comando
# python -m cProfile -o profile.stats meu_script.py
# python -c "import pstats; pstats.Stats('profile.stats').sort_stats('cumulative').print_stats(20)"
```

### Python - line_profiler (por linha)

```bash
pip install line_profiler
```

```python
from line_profiler import LineProfiler

def processar_dados():
    dados = carregar_arquivo("grande.csv")       # Linha 1
    dados_filtrados = filtrar(dados)              # Linha 2
    dados_transformados = transformar(dados_filtrados)  # Linha 3
    salvar(dados_transformados, "resultado.csv")  # Linha 4

# Setup do profiler
lp = LineProfiler()
lp.add_function(processar_dados)
lp.add_function(carregar_arquivo)
lp.add_function(filtrar)
lp.add_function(transformar)

# Executa
lp.runcall(processar_dados)

# Imprime resultado
lp.print_stats()
```

```bash
# Via CLI
kernprof -l -v meu_script.py
```

### Node.js - Clinic.js

```bash
npm install -g clinic
```

```javascript
// app.js - Aplicacao Express para profiling
const express = require("express");
const app = express();

app.get("/api/lento", async (req, res) => {
  // Simula operacao pesada
  const resultado = await operacaoPesada();
  res.json(resultado);
});

app.listen(3000);

// Profiling com Clinic
// clinic doctor -- node app.js
// clinic flame -- node app.js
// clinic bubbleprof -- node app.js
```

### Chrome DevTools - Performance Panel

```
1. Abrir DevTools (F12)
2. Ir para aba Performance
3. Clicar em Record
4. Executar a acao a ser medida
5. Parar gravacao
6. Analisar:
   - FPS (deve manter 60fps)
   - CPU Usage (picos indicam bottlenecks)
   - Heap (crescimento contante = memory leak)
   - Main Thread (blocos longos > 50ms sao problemas)
```

### async-profiler (Java/Kotlin)

```bash
# Download
git clone https://github.com/async-profiler/async-profiler.git
cd async-profiler && make

# Profiling de processo Java
./profiler.sh -d 30 -f flamegraph.html <PID>

# Profiling com eventos especificos
./profiler.sh -e cpu -d 30 -f cpu_flame.html <PID>
./profiler.sh -e alloc -d 30 -f alloc_flame.html <PID>
./profiler.sh -e lock -d 30 -f lock_flame.html <PID>

# Gerar flamegraph
./profiler.sh -d 30 -f profile.svg --title "CPU Profile" <PID>
```

## Database Query Optimization

### EXPLAIN ANALYZE - PostgreSQL

```sql
-- Analise basica de query
EXPLAIN ANALYZE
SELECT u.nome, p.titulo
FROM usuarios u
JOIN pedidos p ON p.usuario_id = u.id
WHERE u.status = 'ativo'
  AND p.criado_em > '2026-01-01'
ORDER BY p.criado_em DESC
LIMIT 100;
```

```
-- Exemplo de output
Limit  (cost=0.87..45.23 rows=100 width=64) (actual time=0.045..2.341 rows=100 loops=1)
  ->  Nested Loop  (cost=0.87..12543.12 rows=28234 width=64) (actual time=0.044..2.310 rows=100 loops=1)
        ->  Index Scan Backward using idx_pedidos_criado_em on pedidos p
              (cost=0.43..8921.45 rows=28234 width=32) (actual time=0.032..1.120 rows=100 loops=1)
              Index Cond: (criado_em > '2026-01-01'::date)
        ->  Index Scan using usuarios_pkey on usuarios u
              (cost=0.43..0.12 rows=1 width=32) (actual time=0.011..0.011 rows=1 loops=100)
              Index Cond: (id = p.usuario_id)
              Filter: (status = 'ativo'::text)
Planning Time: 0.892 ms
Execution Time: 2.456 ms
```

### Estrategias de Indexacao

```sql
-- B-Tree (default, igualdade e range)
CREATE INDEX idx_usuarios_email ON usuarios(email);

-- Composite index (ordem importa!)
CREATE INDEX idx_pedidos_usuario_status ON pedidos(usuario_id, status);

-- Partial index (apenas subset dos dados)
CREATE INDEX idx_pedidos Pendentes ON pedidos(usuario_id)
WHERE status = 'pendente';

-- Covering index (INCLUDE para index-only scans)
CREATE INDEX idx_pedidos_covering ON pedidos(usuario_id, criado_em)
INCLUDE (total, status);

-- GIN (arrays, JSONB, full-text)
CREATE INDEX idx_usuarios_tags ON usuarios USING GIN(tags);
CREATE INDEX idx_usuarios_metadata ON usuarios USING GIN(metadata);

-- BRIN (dados com correlacao temporal/espacial)
CREATE INDEX idx_logs_timestamp ON logs USING BRIN(timestamp);

-- Expression index
CREATE INDEX idx_usuarios_email_lower ON usuarios(LOWER(email));
```

### Detecao de N+1 Queries

```python
# Python - Detectando N+1 com SQLAlchemy
from sqlalchemy import event
from collections import Counter
import re

class NPlusOneDetector:
    def __init__(self, threshold: int = 5):
        self.threshold = threshold
        self.queries = Counter()

    def __enter__(self):
        event.listen(
            db.engine,
            "before_cursor_execute",
            self._track_query,
        )
        return self

    def __exit__(self, *args):
        event.remove(
            db.engine,
            "before_cursor_execute",
            self._track_query,
        )
        self.report()

    def _track_query(self, conn, cursor, statement, parameters, context, executemany):
        # Normaliza query (remove valores)
        normalized = re.sub(r"'[^']*'", "?", statement)
        normalized = re.sub(r"\d+", "?", normalized)
        self.queries[normalized] += 1

    def report(self):
        for query, count in self.queries.items():
            if count >= self.threshold:
                print(f"[N+1 DETECTED] Executada {count} vezes:")
                print(f"  {query[:120]}...")

# Uso
with NPlusOneDetector(threshold=5):
    usuarios = session.query(Usuario).all()
    for u in usuarios:
        print(u.pedidos)  # Isso dispara N+1!
```

```python
# Solucao: Eager Loading
from sqlalchemy.orm import joinedload, selectinload

# joinedload: JOIN na mesma query (1:1 ou poucos 1:N)
usuarios = session.query(Usuario).options(
    joinedload(Usuario.perfil)
).all()

# selectinload: Query separada com IN (1:N muitos)
usuarios = session.query(Usuario).options(
    selectinload(Usuario.pedidos)
).all()
```

```javascript
// JavaScript/TypeScript - N+1 com DataLoader (GraphQL)
const DataLoader = require("dataloader");

// Batch function para carregar pedidos por usuario
const pedidosPorUsuarioLoader = new DataLoader(async (usuarioIds) => {
  const pedidos = await db.pedidos.findMany({
    where: { usuario_id: { in: usuarioIds } },
  });

  // Agrupa por usuario_id
  const map = {};
  usuarioIds.forEach((id) => (map[id] = []));
  pedidos.forEach((p) => map[p.usuario_id].push(p));

  return usuarioIds.map((id) => map[id]);
});

// Uso no resolver GraphQL
const resolvers = {
  Usuario: {
    pedidos: (usuario) => pedidosPorUsuarioLoader.load(usuario.id),
  },
};
```

## Memory Profiling e Leak Detection

### Python - tracemalloc

```python
import tracemalloc
import gc

# Inicia tracking
tracemalloc.start()

# ... executa codigo ...

# Snapshot atual
snapshot = tracemalloc.take_snapshot()
stats = snapshot.statistics("lineno")

# Top 10 alocacoes
for stat in stats[:10]:
    print(f"{stat.count} blocos: {stat.size / 1024:.1f} KB")
    print(f"  {stat.traceback.format()}")

# Compara com snapshot anterior
def compare_snapshots():
    snap1 = tracemalloc.take_snapshot()

    # ... executa operacao suspeita ...

    snap2 = tracemalloc.take_snapshot()

    top_stats = snap2.compare_to(snap1, "lineno")

    for stat in top_stats[:10]:
        print(f"{stat.size_diff:+.1f} KB ({stat.count_diff:+} blocos)")
        print(f"  {stat.traceback.format()}")

# Forca garbage collection e reporta ciclos
gc.collect()
print(f"Objetos nao coletados: {gc.garbage}")
```

### Python - memory_profiler

```bash
pip install memory_profiler
```

```python
from memory_profiler import profile

@profile
def processar_grande_arquivo():
    dados = []
    with open("grande.csv") as f:
        for linha in f:
            dados.append(linha.strip().split(","))
    return dados

# Uso via CLI
# mprof run meu_script.py
# mprof plot
```

### Node.js - Heap Snapshots

```javascript
// Captura heap snapshot programaticamente
const fs = require("fs");
const v8 = require("v8");

function captureHeapSnapshot(filename = "heap.heapsnapshot") {
  const stream = v8.getHeapSnapshot();
  const file = fs.createWriteStream(filename);
  stream.pipe(file);
  return new Promise((resolve) => file.on("finish", resolve));
}

// Uso
async function debugMemory() {
  await captureHeapSnapshot("antes.heapsnapshot");

  // ... executa operacao suspeita ...

  await captureHeapSnapshot("depois.heapsnapshot");
  console.log("Snapshots capturados. Compare no Chrome DevTools.");
}

// Via CLI (Node.js 16+)
// node --heapsnapshot-signal=SIGUSR2 app.js
// kill -USR2 <PID>  # Gera snapshot no disco
```

### Node.js - Clinic.js Heap Profiler

```bash
# Detecta memory leaks
clinic heap-profiler -- node app.js

# Analisa output
# Abre arquivo .clinic.html no navegador
```

## Estrategias de Caching

### Redis - Cache com Python

```python
import redis
import json
from functools import wraps
from typing import Any

redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

def cache_result(key_prefix: str, ttl: int = 300):
    """Decorator para cache de resultados em Redis."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Gera chave unica
            cache_key = f"{key_prefix}:{func.__name__}:{hash(str(args) + str(kwargs))}"

            # Tenta cache
            cached = redis_client.get(cache_key)
            if cached:
                return json.loads(cached)

            # Executa funcao
            result = func(*args, **kwargs)

            # Salva no cache
            redis_client.setex(cache_key, ttl, json.dumps(result, default=str))
            return result
        return wrapper
    return decorator

# Uso
@cache_result("usuarios", ttl=600)
def buscar_usuario(usuario_id: int) -> dict:
    return db.query(Usuario).filter_by(id=usuario_id).first()
```

### Redis - Write-Through Cache

```python
class WriteThroughCache:
    """
    Write-Through: escreve no cache e DB simultaneamente.
    Garante consistencia, mas write e mais lento.
    """
    def __init__(self, redis_client, db_session):
        self.redis = redis_client
        self.db = db_session

    def get(self, key: str, loader_func):
        """Get com cache-aside pattern."""
        cached = self.redis.get(key)
        if cached:
            return json.loads(cached)

        # Cache miss - carrega do DB
        result = loader_func()
        if result:
            self.redis.setex(key, 3600, json.dumps(result, default=str))
        return result

    def set(self, key: str, value: Any, ttl: int = 3600):
        """Write-through: atualiza cache e DB."""
        # Salva no DB primeiro
        self.db.add(value)
        self.db.commit()

        # Atualiza cache
        self.redis.setex(key, ttl, json.dumps(value.to_dict(), default=str))

    def invalidate(self, key: str):
        """Invalida cache."""
        self.redis.delete(key)
```

### Redis - Write-Behind Cache

```python
import threading
import queue
import time

class WriteBehindCache:
    """
    Write-Behind: escreve no cache imediatamente,
    flush para DB em batch assincrono.
    Alta performance de write, risco de perda de dados.
    """
    def __init__(self, redis_client, db_session, flush_interval: int = 5):
        self.redis = redis_client
        self.db = db_session
        self.flush_interval = flush_interval
        self.write_queue = queue.Queue()
        self.running = True

        # Thread de flush
        self.flush_thread = threading.Thread(target=self._flush_loop, daemon=True)
        self.flush_thread.start()

    def set(self, key: str, value: Any, ttl: int = 3600):
        """Write-behind: cache imediato, DB assincrono."""
        self.redis.setex(key, ttl, json.dumps(value, default=str))
        self.write_queue.put((key, value))

    def _flush_loop(self):
        """Thread que flush writes para o DB."""
        batch = []
        while self.running:
            try:
                item = self.write_queue.get(timeout=self.flush_interval)
                batch.append(item)

                # Flush quando batch enche ou timeout
                if len(batch) >= 100:
                    self._flush_batch(batch)
                    batch = []
            except queue.Empty:
                if batch:
                    self._flush_batch(batch)
                    batch = []

    def _flush_batch(self, batch: list):
        """Salva batch no DB."""
        try:
            for _, value in batch:
                self.db.merge(value)
            self.db.commit()
        except Exception as e:
            print(f"Erro no flush: {e}")
            self.db.rollback()

    def stop(self):
        self.running = False
        self.flush_thread.join()
```

### CDN Caching Headers

```python
from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/api/dados")
def get_dados(response: Response):
    response.headers["Cache-Control"] = "public, max-age=300, s-maxage=600"
    response.headers["ETag"] = '"abc123"'
    return {"dados": "..."}

@app.get("/api/dinamico")
def get_dinamico(response: Response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    return {"dados": "..."}

# Static files com cache longo
app.mount("/static", StaticFiles(directory="static"), name="static")
```

### Cache Headers Guide

| Header | Valor | Quando Usar |
|---|---|---|
| Cache-Control | `public, max-age=3600` | Conteudo estatico, CDN |
| Cache-Control | `private, max-age=300` | Conteudo por usuario |
| Cache-Control | `no-cache, no-store` | Dados sensiveis, tempo real |
| Cache-Control | `stale-while-revalidate=60` | Disponibilidade > frescor |
| ETag | `"hash-do-conteudo"` | Validacao condicional |
| Last-Modified | `Wed, 16 May 2026 12:00:00 GMT` | Validacao por data |

## Async Patterns e Concorrencia

### Python - asyncio para I/O Bound

```python
import asyncio
import aiohttp
from typing import List

async def fetch_url(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()

async def fetch_all(urls: List[str]) -> List[dict]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks, return_exceptions=True)

# Execucao
urls = [f"https://api.exemplo.com/dados/{i}" for i in range(100)]
resultados = asyncio.run(fetch_all(urls))
```

### Python - ThreadPoolExecutor vs ProcessPoolExecutor

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def io_bound_task(url: str) -> dict:
    """I/O bound: usa ThreadPoolExecutor."""
    return httpx.get(url).json()

def cpu_bound_task(n: int) -> int:
    """CPU bound: usa ProcessPoolExecutor."""
    return sum(i * i for i in range(n))

# I/O Bound - ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=20) as executor:
    urls = [f"https://api.exemplo.com/{i}" for i in range(100)]
    resultados = list(executor.map(io_bound_task, urls))

# CPU Bound - ProcessPoolExecutor
with ProcessPoolExecutor(max_workers=4) as executor:
    numeros = [1000000] * 8
    resultados = list(executor.map(cpu_bound_task, numeros))
```

### Node.js - Worker Threads para CPU Bound

```javascript
const { Worker, isMainThread, parentPort, workerData } = require("worker_threads");

// worker.js
if (isMainThread) {
  // Thread principal
  function runWorker(data) {
    return new Promise((resolve, reject) => {
      const worker = new Worker(__filename, { workerData: data });
      worker.on("message", resolve);
      worker.on("error", reject);
    });
  }

  // Uso
  async function processar() {
    const resultado = await runWorker({ numeros: [1, 2, 3, 4, 5] });
    console.log(resultado);
  }
} else {
  // Worker thread
  const { numeros } = workerData;
  const resultado = numeros.reduce((sum, n) => sum + n * n, 0);
  parentPort.postMessage(resultado);
}
```

## Load Testing

### k6 - Script Completo

```javascript
// load-test.js
import http from "k6/http";
import { check, sleep } from "k6";
import { Rate, Trend } from "k6/metrics";

// Custom metrics
const errorRate = new Rate("erros");
const apiLatency = new Trend("api_latency");

// Configuracoes de carga
export const options = {
  stages: [
    { duration: "30s", target: 50 },    // Ramp up para 50 usuarios
    { duration: "1m", target: 50 },     // Mantem 50 usuarios
    { duration: "30s", target: 200 },   // Spike para 200
    { duration: "1m", target: 200 },    // Sustenta pico
    { duration: "30s", target: 0 },     // Ramp down
  ],
  thresholds: {
    http_req_duration: ["p(95)<500"],   // 95% das requests < 500ms
    http_req_failed: ["rate<0.01"],     // < 1% de erros
    erros: ["rate<0.05"],               // < 5% erro customizado
    api_latency: ["p(90)<300"],         // 90% < 300ms
  },
};

const BASE_URL = "https://api.jarvis.local";

export default function () {
  // Teste 1: Listar usuarios
  const listRes = http.get(`${BASE_URL}/v2/usuarios?limit=20`);
  const listOk = check(listRes, {
    "status e 200": (r) => r.status === 200,
    "response tem data": (r) => JSON.parse(r.body).data !== undefined,
    "latencia < 200ms": (r) => r.timings.duration < 200,
  });
  errorRate.add(!listOk);
  apiLatency.add(listRes.timings.duration);

  sleep(1);

  // Teste 2: Criar usuario
  const payload = JSON.stringify({
    email: `user_${__VU}_${__ITER}@test.com`,
    nome: `Usuario ${__VU}`,
    senha: "senha123",
  });

  const params = {
    headers: { "Content-Type": "application/json" },
  };

  const createRes = http.post(`${BASE_URL}/v2/usuarios`, payload, params);
  check(createRes, {
    "criacao status 201": (r) => r.status === 201,
    "retorna id": (r) => JSON.parse(r.body).id !== undefined,
  });

  sleep(2);
}
```

```bash
# Executa teste local
k6 run load-test.js

# Executa com output para Cloud
k6 cloud load-test.js

# Executa com output para InfluxDB + Grafana
k6 run --out influxdb=http://localhost:8086/k6 load-test.js
```

### Locust - Script Python

```python
# locustfile.py
from locust import HttpUser, task, between, events
import random
import json

class UsuarioUser(HttpUser):
    wait_time = between(1, 3)  # Espera 1-3s entre tasks

    def on_start(self):
        """Login antes dos testes."""
        response = self.client.post("/auth/login", json={
            "email": "test@jarvis.local",
            "senha": "senha123",
        })
        self.token = response.json().get("access_token")
        self.headers = {"Authorization": f"Bearer {self.token}"}

    @task(3)  # Peso 3 - executa 3x mais
    def listar_usuarios(self):
        self.client.get(
            "/v2/usuarios?limit=20",
            headers=self.headers,
            name="/v2/usuarios",
        )

    @task(2)
    def obter_usuario(self):
        user_id = random.randint(1, 1000)
        self.client.get(
            f"/v2/usuarios/{user_id}",
            headers=self.headers,
            name="/v2/usuarios/[id]",
        )

    @task(1)
    def criar_usuario(self):
        payload = {
            "email": f"user_{random.randint(1, 99999)}@test.com",
            "nome": f"Usuario {random.randint(1, 1000)}",
            "senha": "senha123",
        }
        self.client.post(
            "/v2/usuarios",
            json=payload,
            headers=self.headers,
            name="/v2/usuarios POST",
        )

    @task(1)
    def buscar(self):
        termos = ["joao", "maria", "admin", "teste"]
        termo = random.choice(termos)
        self.client.get(
            f"/v2/usuarios?search={termo}",
            headers=self.headers,
            name="/v2/usuarios search",
        )

# Eventos customizados
@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("Teste iniciado!")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("Teste finalizado!")
```

```bash
# Web UI
locust -f locustfile.py --host=https://api.jarvis.local

# Headless (CI/CD)
locust -f locustfile.py --headless \
  --users 100 \
  --spawn-rate 10 \
  --run-time 5m \
  --host=https://api.jarvis.local
```

## Performance Budgets

### Definindo Budgets

```json
{
  "performance-budgets": {
    "frontend": {
      "bundle-size": {
        "total": "250KB",
        "initial-js": "150KB",
        "initial-css": "50KB",
        "largest-asset": "100KB"
      },
      "metrics": {
        "lcp": "2.5s",
        "fcp": "1.0s",
        "cls": "0.1",
        "fid": "100ms",
        "ttfb": "800ms"
      }
    },
    "backend": {
      "api-latency": {
        "p50": "100ms",
        "p95": "500ms",
        "p99": "1000ms"
      },
      "database": {
        "query-p50": "50ms",
        "query-p95": "200ms",
        "connection-pool": "20 max"
      },
      "memory": {
        "heap-limit": "512MB",
        "gc-pause": "50ms"
      }
    }
  }
}
```

### Webpack Bundle Analyzer

```bash
npm install --save-dev webpack-bundle-analyzer
```

```javascript
// webpack.config.js
const BundleAnalyzerPlugin = require("webpack-bundle-analyzer").BundleAnalyzerPlugin;

module.exports = {
  plugins: [
    new BundleAnalyzerPlugin({
      analyzerMode: "static",
      reportFilename: "bundle-report.html",
    }),
  ],
};
```

### Lighthouse CI

```yaml
# .lighthouserc.yml
ci:
  collect:
    url:
      - https://jarvis.local/
      - https://jarvis.local/dashboard
    numberOfRuns: 3
  assert:
    assertions:
      "categories:performance": ["error", {"minScore": 0.9}]
      "largest-contentful-paint": ["error", {"maxNumericValue": 2500}]
      "cumulative-layout-shift": ["error", {"maxNumericValue": 0.1}]
  upload:
    target: temporary-public-storage
```

## Frontend Performance

### Code Splitting com Next.js

```javascript
// Lazy loading de componentes
import dynamic from "next/dynamic";

const GraficoPesado = dynamic(() => import("../components/GraficoPesado"), {
  loading: () => <p>Carregando...</p>,
  ssr: false,  // Desabilita SSR se nao necessario
});

// Lazy loading de rotas
const AdminPage = dynamic(() => import("../pages/admin"), {
  ssr: false,
});

// Prefetch de rotas
import Link from "next/link";

<Link href="/dashboard" prefetch={true}>
  Dashboard
</Link>;
```

### Image Optimization

```javascript
import Image from "next/image";

<Image
  src="/hero.jpg"
  alt="Hero"
  width={1200}
  height={600}
  priority  // LCP image - carrega imediatamente
  sizes="(max-width: 768px) 100vw, 1200px"
  placeholder="blur"
  blurDataURL="data:image/jpeg;base64,/9j/4AAQSkZJRg..."
/>;
```

## Backend Performance

### Connection Pooling

```python
# SQLAlchemy - Pool configurado
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://user:pass@localhost/db",
    pool_size=20,           # Conexoes persistentes
    max_overflow=10,        # Conexoes extras sob carga
    pool_timeout=30,        # Timeout para obter conexao
    pool_recycle=1800,      # Recicla conexoes a cada 30min
    pool_pre_ping=True,     # Verifica conexao antes de usar
)
```

```javascript
// Node.js - PostgreSQL pool
const { Pool } = require("pg");

const pool = new Pool({
  max: 20,               // Max conexoes
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 5000,
});

// Uso com transacao
async function criarPedidoComItens(pedido, itens) {
  const client = await pool.connect();
  try {
    await client.query("BEGIN");

    const result = await client.query(
      "INSERT INTO pedidos (...) VALUES (...) RETURNING id",
      [pedido...]
    );
    const pedidoId = result.rows[0].id;

    for (const item of itens) {
      await client.query(
        "INSERT INTO itens_pedido (pedido_id, ...) VALUES ($1, ...)",
        [pedidoId, item...]
      );
    }

    await client.query("COMMIT");
    return pedidoId;
  } catch (e) {
    await client.query("ROLLBACK");
    throw e;
  } finally {
    client.release();
  }
}
```

### Batch Operations

```python
# SQLAlchemy - Bulk insert
from sqlalchemy.dialects.postgresql import insert

def bulk_insert_usuarios(usuarios: list[dict]):
    """Insert em batch - muito mais rapido que individual."""
    stmt = insert(Usuario).values(usuarios)
    stmt = stmt.on_conflict_do_nothing(index_elements=["email"])
    db.execute(stmt)
    db.commit()

# 10.000 registros:
# Individual: ~30s
# Bulk: ~0.5s
```

## APM Tools

### OpenTelemetry - Python

```python
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from fastapi import FastAPI

# Setup tracing
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(
    BatchSpanProcessor(OTLPSpanExporter(endpoint="localhost:4317"))
)
trace.set_tracer_provider(tracer_provider)

# Setup metrics
meter_provider = MeterProvider()
metrics.set_meter_provider(meter_provider)

# Instrumentacao automatica
app = FastAPI()
FastAPIInstrumentor.instrument_app(app)

# Tracing custom
tracer = trace.get_tracer("jarvis-api")

@app.get("/usuarios/{id}")
def obter_usuario(id: str):
    with tracer.start_as_current_span("obter_usuario") as span:
        span.set_attribute("usuario.id", id)
        usuario = db.query(Usuario).get(id)
        span.set_attribute("usuario.found", usuario is not None)
        return usuario
```

### OpenTelemetry - Node.js

```javascript
const { NodeSDK } = require("@opentelemetry/sdk-node");
const { getNodeAutoInstrumentations } = require("@opentelemetry/auto-instrumentations-node");
const { OTLPTraceExporter } = require("@opentelemetry/exporter-trace-otlp-grpc");

const sdk = new NodeSDK({
  traceExporter: new OTLPTraceExporter({ url: "http://localhost:4317" }),
  instrumentations: [getNodeAutoInstrumentations()],
});

sdk.start();
```

### Datadog APM

```python
# ddtrace - Python
from ddtrace import tracer, patch

# Patch automatico
patch(fastapi=True, sqlalchemy=True, redis=True, httpx=True)

# Spans custom
@tracer.wrap(service="jarvis-api", resource="processar_pedido")
def processar_pedido(pedido_id: str):
    with tracer.trace("validar_pedido"):
        validar(pedido_id)

    with tracer.trace("salvar_pedido"):
        salvar(pedido_id)
```

```bash
# Datadog Agent - docker-compose
# docker-compose.yml
services:
  datadog:
    image: gcr.io/datadoghq/agent:7
    environment:
      - DD_API_KEY=sua-api-key
      - DD_APM_ENABLED=true
      - DD_APM_NON_LOCAL_TRAFFIC=true
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - /proc/:/host/proc/:ro
      - /sys/fs/cgroup/:/host/sys/fs/cgroup:ro
```

## Referencias Cruzadas

- [[database]] - Fundamentos de banco de dados
- [[Bancos-de-Dados/PostgreSQL-Advanced|PostgreSQL Avancado]] - Otimizacao avancada de queries
- [[backend]] - Implementacao backend
- [[api-design]] - Design de APIs eficientes
- [[advanced-backend-architecture|Advanced Backend Architecture]] - Arquitetura para escala
- [[../devops/Observabilidade|Observabilidade]] - Monitoring e alerting
- [[../data-engineering/INDEX|Data Engineering]] - Performance de data pipelines
