---
title: "Arquitetura Backend Avançada (Python & TS)"
description: "Guia profundo sobre padrões de design avançados em Python e TypeScript para construção de serviços massivos e orquestradores de IA."
tags: [software-engineering, backend, python, typescript, arquitetura, microservices, event-driven, cqrs, observability, skills-eng]
date: 2026-04-27
updated: 2026-06-05
---

# Arquitetura Backend Avançada

Para que o [[JARVIS/Main|JARVIS]] e seus sistemas operem com máxima eficiência, precisamos ir além do simples "CRUD com Flask" e adotar padrões de design resilientes e escaláveis.

## 1. Microservices vs Monoliths

### Monólito: Quando Usar
- Time pequeno (< 10 devs)
- Produto em fase inicial (MVP)
- Baixa complexidade de domínio
- Latência crítica (evita overhead de rede)

```python
# Monólito bem estruturado com módulos
# app/
# ├── agents/         # Módulo de agente
# ├── knowledge/      # Módulo de conhecimento
# ├── infrastructure/ # DB, cache, message bus
# └── api/            # FastAPI routes

# Vantagem: deploy único, sem complexidade de rede
```

### Microservices: Quando Migrar
- Times independentes por domínio
- Escalabilidade diferente por serviço
- Poliglotismo (cada serviço usa a melhor tecnologia)
- Deployment independente

```python
# Serviço de Agentes (Porta 8001)
# Serviço de Conhecimento/RAG (Porta 8002)
# Serviço de Cache (Porta 8003)
# API Gateway (Porta 80)
```

### Estratégia de Migração (Strangler Fig Pattern)
```python
class StranglerFigRouter:
    """Roteia requisições gradualmente para o novo microsserviço"""
    
    def route(self, request):
        if self.feature_flags.is_enabled("new_rag_service"):
            # 10% do tráfego vai para o novo serviço
            if hash(request.user_id) % 100 < 10:
                return self.new_rag_service.handle(request)
        return self.legacy_monolith.handle(request)
```

## 2. Event-Driven Architecture

### Message Broker: RabbitMQ vs Kafka vs Redis Streams

| Característica | RabbitMQ | Kafka | Redis Streams |
|---------------|----------|-------|---------------|
| Throughput | ~10K msg/s | ~1M msg/s | ~100K msg/s |
| Persistência | Sim | Sim (log) | Sim (opcional) |
| Ordem | Não garante | Garante por partição | Garante |
| Retenção | Até consumir | Configurável | Configurável |
| Caso de uso | Tasks, RPC | Event sourcing, streams | Cache + fila |

### Implementação com RabbitMQ e Celery
```python
# tasks.py - Tarefas assíncronas para processamento de IA
from celery import Celery

app = Celery("jarvis", broker="redis://localhost:6379/0")

@app.task(bind=True, max_retries=3, default_retry_delay=60)
def process_rag_query(self, query: str, user_id: str):
    try:
        # Pipeline de RAG completo
        chunks = retrieve_chunks(query)
        reranked = rerank_chunks(query, chunks)
        response = llm_generate(query, reranked)
        
        # Salva resultado em cache
        cache_response(user_id, query, response)
        return response
    except ConnectionError as exc:
        raise self.retry(exc=exc)

@app.task
def generate_embeddings_batch(note_ids: list[str]):
    """Task de background para atualizar embeddings"""
    for note_id in note_ids:
        note = get_note(note_id)
        embedding = embed(note.content)
        vector_db.upsert(note_id, embedding, note.metadata)
```

### Event Sourcing
```python
# Event sourcing para o sistema de notas
from datetime import datetime

class EventStore:
    def __init__(self):
        self.events = []
    
    def append(self, event: dict):
        self.events.append({
            **event,
            "timestamp": datetime.utcnow().isoformat(),
            "event_id": str(uuid4())
        })
    
    def replay(self, aggregate_id: str) -> list[dict]:
        return [e for e in self.events if e["aggregate_id"] == aggregate_id]

# Uso: Cada nota tem seu stream de eventos
store.append({
    "aggregate_id": "note_123",
    "type": "note.created",
    "data": {"title": "RAG Strategies", "content": "..."}
})
store.append({
    "aggregate_id": "note_123",
    "type": "note.updated",
    "data": {"title": "Advanced RAG Strategies"}
})
```

## 3. CQRS e Event Sourcing

### Command Query Responsibility Segregation

Separa operações de leitura (Query) e escrita (Command):

```python
# COMMAND: Altera estado
class CreateNoteCommand:
    def __init__(self, repo: WriteRepository):
        self.repo = repo
    
    def execute(self, title: str, content: str, tags: list[str]) -> str:
        note_id = str(uuid4())
        self.repo.save(Note(id=note_id, title=title, content=content, tags=tags))
        
        # Dispara evento para atualizar índices
        event_bus.publish("note.created", {"note_id": note_id, "tags": tags})
        return note_id

# QUERY: Lê dados (pode vir de uma fonte diferente)
class SearchNotesQuery:
    def __init__(self, read_repo: ReadRepository):
        self.read_repo = read_repo  # Pode ser Elasticsearch, Redis, etc.
    
    def execute(self, query: str, tags: list[str] | None = None) -> list[dict]:
        return self.read_repo.search(query=query, tags=tags)
```

### Materialized Views para Leitura
```python
# A view de leitura é atualizada por eventos
class NotesMaterializedView:
    def __init__(self, redis_client):
        self.redis = redis_client
    
    def on_note_created(self, event: dict):
        note_data = get_full_note(event["note_id"])
        self.redis.set(
            f"note:{event['note_id']}",
            json.dumps(note_data)
        )
        # Atualiza índices de busca
        for tag in note_data["tags"]:
            self.redis.sadd(f"tag:{tag}:notes", event["note_id"])
```

## 4. API Gateways e Service Mesh

### API Gateway com FastAPI
```python
from fastapi import FastAPI, Request
import httpx

app = FastAPI(title="JARVIS API Gateway")

SERVICES = {
    "agents": "http://agent-service:8001",
    "knowledge": "http://knowledge-service:8002",
    "cache": "http://cache-service:8003",
    "monitoring": "http://monitoring-service:8004",
}

@app.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def gateway(service: str, path: str, request: Request):
    if service not in SERVICES:
        return {"error": f"Service '{service}' not found"}, 404
    
    # Rate limiting por serviço
    if not rate_limiter.check(service, request.client.host):
        return {"error": "rate_limit_exceeded"}, 429
    
    # Roteamento com timeout
    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                method=request.method,
                url=f"{SERVICES[service]}/{path}",
                headers=dict(request.headers),
                content=await request.body(),
                timeout=30.0,
            )
            return response.json(), response.status_code
        except httpx.TimeoutException:
            return {"error": "service_timeout"}, 504
```

### Service Mesh com Consul + Envoy (Conceitual)
```hcl
# service.hcl - Configuração Consul para service discovery
service {
  name = "knowledge-service"
  port = 8002
  tags = ["rag", "ai", "v1"]
  
  check {
    http     = "http://localhost:8002/health"
    interval = "10s"
    timeout  = "5s"
  }
  
  connect {
    sidecar_service {
      proxy {
        upstreams = [
          {
            destination_name = "vector-db"
            local_bind_port  = 8500
          },
          {
            destination_name = "cache-service"
            local_bind_port  = 8501
          }
        ]
      }
    }
  }
}
```

## 5. Database Patterns

### Read Replicas
```python
# Configuração de múltiplas fontes de dados
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class DatabaseRouter:
    def __init__(self):
        self.master = create_engine("postgresql://user:pass@master:5432/db")
        self.replicas = [
            create_engine(f"postgresql://user:pass@replica-{i}:5432/db")
            for i in range(3)
        ]
        self.replica_index = 0
    
    def get_writer(self) -> Session:
        return Session(self.master)
    
    def get_reader(self) -> Session:
        self.replica_index = (self.replica_index + 1) % len(self.replicas)
        return Session(self.replicas[self.replica_index])

# Uso
db = DatabaseRouter()

# Escrita vai para o master
with db.get_writer() as session:
    session.add(new_note)
    session.commit()

# Leitura vai para uma réplica
with db.get_reader() as session:
    notes = session.query(Note).all()
```

### Sharding (Particionamento Horizontal)
```python
class ShardManager:
    def __init__(self):
        self.shards = {
            0: create_engine("postgresql://.../db_shard_0"),
            1: create_engine("postgresql://.../db_shard_1"),
            2: create_engine("postgresql://.../db_shard_2"),
        }
    
    def get_shard(self, shard_key: str) -> Session:
        shard_id = hash(shard_key) % len(self.shards)
        return Session(self.shards[shard_id])

# Uso: Shard por user_id
shard = shard_manager.get_shard(user_id)
with shard:
    notes = shard.query(Note).filter(Note.user_id == user_id).all()
```

## 6. Caching Strategies

### Cache em Múltiplas Camadas
```python
class MultiLayerCache:
    """L1: RAM (dict), L2: Redis, L3: CDN"""
    
    def __init__(self):
        self.l1: dict[str, tuple[float, str]] = {}  # local cache
        self.l2 = redis.Redis(host="localhost", port=6379)
        self.l1_ttl = 60  # 1 minuto em RAM
        self.l2_ttl = 3600  # 1 hora em Redis
    
    def get(self, key: str) -> str | None:
        # L1 - RAM (ultra-rápido)
        if key in self.l1:
            value, expiry = self.l1[key]
            if time.time() < expiry:
                return value
            del self.l1[key]
        
        # L2 - Redis
        value = self.l2.get(key)
        if value:
            self.l1[key] = (time.time() + self.l1_ttl, value)
            return value
        
        return None
    
    def set(self, key: str, value: str):
        self.l1[key] = (time.time() + self.l1_ttl, value)
        self.l2.setex(key, self.l2_ttl, value)

# Cache Aside Pattern
def get_agent_config(agent_id: str) -> dict:
    cache = MultiLayerCache()
    
    config = cache.get(f"agent:{agent_id}:config")
    if config:
        return json.loads(config)
    
    # Cache miss - busca no banco
    config = database.query("SELECT config FROM agents WHERE id = ?", agent_id)
    cache.set(f"agent:{agent_id}:config", json.dumps(config))
    return config
```

### Cache Invalidation Strategies
```python
# 1. Write-Through: Cache é atualizado junto com o banco
def update_note(note_id: str, content: str):
    database.update("notes", note_id, {"content": content})
    cache.set(f"note:{note_id}", content)  # Write-through

# 2. Cache Invalidation por Evento
def on_note_updated(event: dict):
    cache.delete(f"note:{event['note_id']}")  # Próxima leitura dá cache miss
    cache.delete(f"note:{event['note_id']}:embeddings")  # Embedding também invalida

# 3. TTL Estratégico por Tipo de Dado
CACHE_TTLS = {
    "agent_config": 3600,      # 1h - muda pouco
    "user_preferences": 86400, # 24h - muda raramente
    "session_context": 300,    # 5min - volátil
    "search_results": 60,      # 1min - frescos
}
```

## 7. Observabilidade

### Logs Estruturados
```python
import structlog

logger = structlog.get_logger()

# Em cada requisição
logger.info("rag_query_executed",
    user_id=user_id,
    query_length=len(query),
    chunks_retrieved=len(chunks),
    latency_ms=latency,
    model_used=model,
    cache_hit=cache_hit,
)
```

### Métricas com Prometheus
```python
from prometheus_client import Counter, Histogram, Gauge
import time

REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

RAG_LATENCY = Histogram(
    "rag_query_duration_seconds",
    "RAG query latency",
    ["model"],
    buckets=[0.1, 0.5, 1.0, 2.5, 5.0, 10.0]
)

ACTIVE_CONNECTIONS = Gauge(
    "active_websocket_connections",
    "Active WebSocket connections"
)

@app.post("/query")
async def query_rag(request: QueryRequest):
    start = time.time()
    try:
        result = await rag_pipeline.execute(request.query)
        REQUESTS_TOTAL.labels(method="POST", endpoint="/query", status=200).inc()
        RAG_LATENCY.labels(model=request.model).observe(time.time() - start)
        return result
    except Exception:
        REQUESTS_TOTAL.labels(method="POST", endpoint="/query", status=500).inc()
        raise
```

### Tracing Distribuído (OpenTelemetry)
```python
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

tracer = trace.get_tracer("jarvis")

async def process_rag_query(query: str):
    with tracer.start_as_current_span("rag_pipeline") as span:
        span.set_attribute("query", query[:100])
        
        with tracer.start_as_current_span("chunking"):
            chunks = chunk_document(query)
            span.set_attribute("chunks_count", len(chunks))
        
        with tracer.start_as_current_span("embedding"):
            embeddings = embed_chunks(chunks)
        
        with tracer.start_as_current_span("search"):
            results = vector_search(embeddings)
        
        span.set_attribute("results_count", len(results))
        return results
```

### Health Checks e Readiness Probes
```python
from fastapi import FastAPI
from pydantic import BaseModel

class HealthStatus(BaseModel):
    status: str  # healthy | degraded | unhealthy
    version: str
    uptime: float
    dependencies: dict[str, str]

@app.get("/health", response_model=HealthStatus)
async def health_check():
    deps = {}
    
    # Verifica cada dependência
    for name, check in DEPENDENCIES.items():
        try:
            check()
            deps[name] = "healthy"
        except Exception as e:
            deps[name] = f"unhealthy: {e}"
    
    status = "healthy" if all(v == "healthy" for v in deps.values()) else "degraded"
    if any("unhealthy" in v for v in deps.values()):
        status = "unhealthy"
    
    return HealthStatus(
        status=status,
        version="2.0.0",
        uptime=time.time() - start_time,
        dependencies=deps,
    )
```

## 8. Filas de Tarefas (Task Queues)

### Arquitetura Completa
```python
# Frontend envia task -> Backend retorna Task ID -> Worker processa -> Result salvo
from celery import Celery
from celery.result import AsyncResult

celery_app = Celery("jarvis", broker="redis://localhost:6379/0")

@celery_app.task(bind=True, max_retries=3)
def long_running_ai_task(self, task_data: dict):
    """Processamento pesado de IA em background"""
    try:
        result = ai_pipeline.execute(task_data)
        save_result(task_data["task_id"], result)
        return result
    except Exception as exc:
        self.retry(exc=exc, countdown=60 * (2 ** self.request.retries))

# Frontend/API envia a task
@app.post("/tasks")
async def create_task(task_data: dict):
    task = long_running_ai_task.delay(task_data)
    return {"task_id": task.id, "status": "pending"}

# Frontend consulta o resultado
@app.get("/tasks/{task_id}")
async def get_task(task_id: str):
    task = AsyncResult(task_id, app=celery_app)
    if task.ready():
        return {"status": "completed", "result": task.result}
    return {"status": "pending"}
```

## 9. Resiliência e Padrões de Tolerância a Falhas

### Circuit Breaker
```python
import pybreaker

rag_breaker = pybreaker.CircuitBreaker(
    fail_max=5,
    reset_timeout=60,
    exclude=[requests.Timeout],
)

@app.post("/query")
async def query_with_circuit_breaker(request: QueryRequest):
    try:
        result = rag_breaker.call(rag_pipeline.execute, request.query)
        return result
    except pybreaker.CircuitBreakerError:
        # Circuito aberto - usa fallback (cache ou resposta genérica)
        return {
            "status": "fallback",
            "data": get_cached_response(request.query)
        }
```

### Bulkhead Pattern
```python
from concurrent.futures import ThreadPoolExecutor
import threading

class Bulkhead:
    def __init__(self, max_concurrent: int):
        self.semaphore = threading.Semaphore(max_concurrent)
    
    async def execute(self, func, *args):
        if not self.semaphore.acquire(blocking=False):
            raise Exception("Bulkhead full - too many concurrent requests")
        try:
            return await func(*args)
        finally:
            self.semaphore.release()

# Separa pools por prioridade
rag_pool = Bulkhead(5)     # Máximo 5 chamadas RAG simultâneas
embed_pool = Bulkhead(10)  # Máximo 10 chamadas de embedding
```

---

*Consulte também: [[backend]], [[04-knowledge-systems/advanced-rag-strategies]], [[03-infrastructure-mcp/local-llm-ops]], [[devops/Monitoramento]].*
