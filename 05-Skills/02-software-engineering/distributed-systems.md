---
tags: [distributed-systems, cap-theorem, consensus, message-queues, caching, load-balancing, resilience, microservices, skills-eng]
updated: 2026-06-10
title: "Distributed Systems"
date: 2026-06-01
---

# Sistemas Distribuidos

Fundamentos de sistemas distribuidos para agentes de codificacao.

---

## Teorema CAP

### Conceito

```
        +------------------+
        |    Sistema        |
        |    Distribuido    |
        +--------+---------+
                 |
      +----------+----------+
      |                     |
  Escolha 2 de 3:          |
      |                     |
  +---+---+           +-----+-----+
  |       |           |           |
(C)onsistency      (A)vailability  (P)artition Tolerance
  |                     |           |
  | Todos veem         | Sempre    | Sistema funciona
  | os mesmos          | responde  | mesmo com falhas
  | dados              |           | de rede
  +-------+           +-----+-----+
          |                 |
          +--------+--------+
                   |
            Na pratica: (P) e obrigatorio
            Escolha real: (C)P ou (A)P
```

### Trade-offs com Exemplos Reais

| Sistema | Escolha | Caracteristica |
|---------|---------|----------------|
| PostgreSQL | CP | Consistencia forte, para em particao |
| MongoDB | CP (configuravel) | Pode relaxar consistencia |
| Cassandra | AP | Disponivel, consistencia eventual |
| DynamoDB | AP (configuravel) | Consistencia forte opcional |
| Redis | AP | Disponivel, replicacao assincrona |
| etcd | CP | Consistencia via Raft |
| ZooKeeper | CP | Consistencia forte garantida |

### Extensao PACELC

```
Se Particao (P):
  Escolha entre (A)vailability ou (C)onsistency
SENÃO (Else):
  Escolha entre (L)atency ou (C)onsistency
```

| Banco | P trade-off | E trade-off |
|-------|------------|-------------|
| MongoDB | A | C |
| Cassandra | A | L |
| DynamoDB | A | L |
| etcd | C | C |
| Spanner | C | C |

---

## Algoritmos de Consenso

### Algoritmo Raft

```
    +-------+     +-------+     +-------+
    |Node A |     |Node B |     |Node C |
    |Leader |     |Follower|    |Follower|
    +---+---+     +---+---+     +---+---+
        |             |             |
        |  AppendEntries (heartbeat)|
        |-------------------------->|
        |  AppendEntries (heartbeat)|
        |-------------------------->|
        |             |             |
        |  <--- Heartbeat timeout ---|
        |             |             |
        |    +--------+             |
        |    | Eleicao inicia       |
        |    | (term + 1, vota em si)|
        |    v                      |
    +-------+     +-------+     +-------+
    |Node A |     |Node B |     |Node C |
    |Candid.|     |Follower|    |Follower|
    +---+---+     +---+---+     +---+---+
        |             |             |
        |  RequestVote |            |
        |------------->|            |
        |  RequestVote |            |
        |---------------------------->|
        |             |             |
        |  VoteGranted| VoteGranted |
        |<-------------|            |
        |<---------------------------|
        |             |             |
        |  MAIORIA = 2/3 => LEADER  |
        v
    +-------+
    |Node A |
    |LEADER |
    +-------+
```

**Etapas do Raft:**
1. **Leader Election**: Follower vira candidato ao expirar timeout
2. **Request Vote**: Candidato pede votos; maioria = novo leader
3. **Log Replication**: Leader replica entradas para followers
4. **Safety**: Leader com log mais completo sempre vence

```python
# Exemplo pratico com etcd
import etcd3

client = etcd3.client(host='localhost', port=2379)

# Eleicao distribuida
lease = client.lease(ttl=10)
leader_key = '/cluster/leader'

try:
    # Tenta adquirir lideranca
    success, _ = client.transaction(
        compare=[
            client.transactions.version(leader_key) == 0
        ],
        success=[
            client.transactions.put(leader_key, 'node-1', lease=lease)
        ],
        failure=[]
    )

    if success:
        print("Sou o leader!")
        # Manter alive
        lease.keep_alive()
    else:
        print("Outro node e o leader")
except Exception as e:
    print(f"Erro na eleicao: {e}")
```

```typescript
// Exemplo com etcd3 (TypeScript)
import { Etcd3 } from 'etcd3'

const client = new Etcd3({ hosts: 'localhost:2379' })

async function acquireLeadership(nodeId: string): Promise<boolean> {
  const lease = client.lease(10) // TTL 10s
  const key = '/cluster/leader'

  const acquired = await client
    .lease(10)
    .put(key)
    .value(nodeId)
    .ifDoesNotExist()
    .commit()

  if (acquired) {
    console.log(`${nodeId} e o leader!`)
    // Manter lease vivo
    setInterval(() => lease.keepAliveOnce(), 5000)
  }

  return acquired
}
```

### Paxos (Visao Geral)

```
Fase 1 (Prepare):
  Proponente -> Proposta N -> Acceptors
  Acceptors -> Promise (N, valor_aceito) -> Proponente

Fase 2 (Accept):
  Proponente -> Accept (N, valor) -> Acceptors
  Acceptors -> Accepted (N, valor) -> Proponente
  Proponente -> Learned (valor) -> Learners
```

---

## Transacoes Distribuidas

### Two-Phase Commit (2PC)

```
    Coordinator         Participant A      Participant B
         |                    |                  |
         |--- PREPARE -------|                  |
         |--- PREPARE ------------------------|
         |                    |                  |
         |<-- VOTE_COMMIT ---|                  |
         |<-- VOTE_COMMIT ---------------------|
         |                    |                  |
         |--- COMMIT --------|                  |
         |--- COMMIT -------------------------|
         |                    |                  |
         |<-- ACK -----------|                  |
         |<-- ACK ----------------------------|
         |                    |                  |
```

```python
# Implementacao simplificada de 2PC
from typing import List
import threading

class TwoPhaseCommit:
    def __init__(self, participants: List['Participant']):
        self.participants = participants

    def execute(self, operation):
        # Fase 1: Prepare
        votes = []
        for p in self.participants:
            vote = p.prepare(operation)
            votes.append(vote)

        if all(votes):
            # Fase 2: Commit
            for p in self.participants:
                p.commit()
            return True
        else:
            # Rollback
            for p in self.participants:
                p.rollback()
            return False

class Participant:
    def prepare(self, operation) -> bool:
        try:
            # Valida se pode executar
            self._validate(operation)
            return True
        except Exception:
            return False

    def commit(self):
        # Executa operacao permanentemente
        pass

    def rollback(self):
        # Desfaz operacao
        pass
```

### Saga Pattern

**Coreografia vs Orquestracao:**

```
COREOGRAFIA (Eventos):
  Servico A --[evento]--> Servico B --[evento]--> Servico C
       |                       |                      |
  [compensacao] <-------- [compensacao] <--------- [falha]

ORQUESTRACAO (Coordenador):
                    +---------------+
                    |  Orquestrador  |
                    +-------+-------+
                            |
              +-------------+-------------+
              |             |             |
              v             v             v
        +-----+---+   +-----+---+   +-----+---+
        |Servico A|   |Servico B|   |Servico C|
        +---------+   +---------+   +---------+
```

```python
# Saga com Orquestracao (Python)
from dataclasses import dataclass
from typing import Callable, List

@dataclass
class SagaStep:
    action: Callable
    compensation: Callable

class SagaOrchestrator:
    def __init__(self, steps: List[SagaStep]):
        self.steps = steps
        self.completed_steps: List[int] = []

    def execute(self, context: dict) -> dict:
        try:
            for i, step in enumerate(self.steps):
                step.action(context)
                self.completed_steps.append(i)
            return context
        except Exception as e:
            self._compensate(context)
            raise e

    def _compensate(self, context: dict):
        # Executa compensacoes na ordem inversa
        for i in reversed(self.completed_steps):
            try:
                self.steps[i].compensation(context)
            except Exception:
                # Log de erro de compensacao
                pass

# Uso
saga = SagaOrchestrator([
    SagaStep(
        action=lambda ctx: create_order(ctx),
        compensation=lambda ctx: cancel_order(ctx),
    ),
    SagaStep(
        action=lambda ctx: charge_payment(ctx),
        compensation=lambda ctx: refund_payment(ctx),
    ),
    SagaStep(
        action=lambda ctx: update_inventory(ctx),
        compensation=lambda ctx: restore_inventory(ctx),
    ),
])

result = saga.execute({"user_id": 1, "items": [1, 2, 3]})
```

```typescript
// Saga com Coreografia (TypeScript)
import { EventEmitter } from 'events'

const eventBus = new EventEmitter()

interface SagaEvent {
  type: string
  payload: any
  sagaId: string
}

class OrderSaga {
  private sagaId: string

  constructor() {
    this.sagaId = crypto.randomUUID()
    this.setupListeners()
  }

  private setupListeners() {
    eventBus.on('order.created', (event: SagaEvent) => {
      if (event.sagaId === this.sagaId) {
        this.chargePayment(event.payload)
      }
    })

    eventBus.on('payment.charged', (event: SagaEvent) => {
      if (event.sagaId === this.sagaId) {
        this.updateInventory(event.payload)
      }
    })

    eventBus.on('payment.failed', (event: SagaEvent) => {
      if (event.sagaId === this.sagaId) {
        this.cancelOrder(event.payload)
      }
    })
  }

  start(orderData: any) {
    eventBus.emit('order.create', {
      type: 'order.create',
      payload: orderData,
      sagaId: this.sagaId,
    })
  }

  private chargePayment(data: any) {
    // Logica de pagamento
    eventBus.emit('payment.charge', {
      type: 'payment.charge',
      payload: { orderId: data.id, amount: data.total },
      sagaId: this.sagaId,
    })
  }

  private cancelOrder(data: any) {
    eventBus.emit('order.cancel', {
      type: 'order.cancel',
      payload: { orderId: data.id },
      sagaId: this.sagaId,
    })
  }
}
```

---

## Message Queues

### RabbitMQ vs Kafka

| Aspecto | RabbitMQ | Kafka |
|---------|----------|-------|
| Modelo | Message broker | Streaming platform |
| Roteamento | Exchanges, queues, bindings | Topics, partitions |
| Retencao | Ate ack do consumidor | Baseada em tempo/tamanho |
| Throughput | Medio (~20k msg/s) | Alto (~100k+ msg/s) |
| Ordenacao | Por queue | Por partition |
| Replay | Nao | Sim (offset reset) |
| Ideal para | Task queue, RPC | Event sourcing, streaming |

### RabbitMQ Patterns

```python
# Producer (Python - pika)
import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

# Work Queue
channel.queue_declare(queue='task_queue', durable=True)

channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=json.dumps({"task": "process_image", "id": 123}),
    properties=pika.BasicProperties(delivery_mode=2),  # Persistente
)

# Pub/Sub com Fanout
channel.exchange_declare(exchange='logs', exchange_type='fanout')
channel.basic_publish(exchange='logs', routing_key='', body='Log message')

# Routing com Direct
channel.exchange_declare(exchange='alerts', exchange_type='direct')
channel.queue_declare(queue='critical_alerts')
channel.queue_bind(exchange='alerts', queue='critical_alerts', routing_key='critical')
channel.basic_publish(exchange='alerts', routing_key='critical', body='ALERT!')

# Topics
channel.exchange_declare(exchange='events', exchange_type='topic')
channel.queue_declare(queue='user_events')
channel.queue_bind(exchange='events', queue='user_events', routing_key='user.*')
channel.basic_publish(exchange='events', routing_key='user.created', body='New user')

connection.close()
```

```python
# Consumer (Python)
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
    print(f"Recebido: {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)  # Fair dispatch
channel.basic_consume(queue='task_queue', on_message_callback=callback)

print("Aguardando mensagens...")
channel.start_consuming()
```

```typescript
// Producer (TypeScript - amqplib)
import * as amqp from 'amqplib'

async function producer() {
  const connection = await amqp.connect('amqp://localhost')
  const channel = await connection.createChannel()

  await channel.assertQueue('task_queue', { durable: true })

  channel.sendToQueue('task_queue', Buffer.from(JSON.stringify({
    task: 'process_image',
    id: 123,
  })), { persistent: true })

  console.log('Mensagem enviada')
  await channel.close()
  await connection.close()
}

// Consumer (TypeScript)
async function consumer() {
  const connection = await amqp.connect('amqp://localhost')
  const channel = await connection.createChannel()

  await channel.assertQueue('task_queue', { durable: true })
  await channel.prefetch(1)

  channel.consume('task_queue', (msg) => {
    if (msg) {
      console.log('Recebido:', msg.content.toString())
      channel.ack(msg)
    }
  })
}
```

### Dead Letter Queue e Retry

```python
# DLQ Configuration (Python)
channel.exchange_declare(exchange='dlx', exchange_type='direct')
channel.queue_declare(queue='task_queue.dlq')
channel.queue_bind(exchange='dlx', queue='task_queue.dlq', routing_key='dlq')

channel.queue_declare(
    queue='task_queue',
    durable=True,
    arguments={
        'x-message-ttl': 60000,  # 60s TTL
        'x-dead-letter-exchange': 'dlx',
        'x-dead-letter-routing-key': 'dlq',
        'x-max-retry-count': 3,
    }
)
```

```typescript
// Retry com backoff (TypeScript)
async function processWithRetry(
  channel: amqp.Channel,
  msg: amqp.ConsumeMessage,
  maxRetries: number = 3
) {
  const retryCount = msg.properties.headers?.['x-retry-count'] ?? 0

  try {
    await processMessage(msg.content.toString())
    channel.ack(msg)
  } catch (error) {
    if (retryCount < maxRetries) {
      const delay = Math.pow(2, retryCount) * 1000 // Exponential backoff
      setTimeout(() => {
        channel.sendToQueue(msg.fields.routingKey, msg.content, {
          headers: { 'x-retry-count': retryCount + 1 },
          persistent: true,
        })
        channel.ack(msg)
      }, delay)
    } else {
      // Send to DLQ
      channel.sendToQueue('task_queue.dlq', msg.content, {
        headers: { 'x-original-routing-key': msg.fields.routingKey, 'x-error': error.message },
      })
      channel.ack(msg)
    }
  }
}
```

---

## Service Discovery

### Client-side vs Server-side

```
CLIENT-SIDE:
  +-------+     +------------------+     +-----------+
  |Cliente| --> | Service Registry | --> | Servicos  |
  |       |     | (Consul, etcd)   |     |           |
  +-------+     +------------------+     +-----------+
  Cliente descobre e escolhe instancia

SERVER-SIDE:
  +-------+     +----------+     +-----------+
  |Cliente| --> |   LB     | --> | Servicos  |
  |       |     | (Nginx)  |     |           |
  +-------+     +----------+     +-----------+
  LB descobre e roteia
```

### Consul (Python)

```python
import consul
import requests

c = consul.Consul()

# Registrar servico
c.agent.service.register(
    name='api-service',
    service_id='api-1',
    address='10.0.1.10',
    port=8080,
    check=consul.Check.http('http://10.0.1.10:8080/health', interval='10s', timeout='5s')
)

# Descobrir servico
def get_service_address():
    index, services = c.health.service('api-service', passing=True)
    if services:
        svc = services[0]['Service']
        return f"http://{svc['Address']}:{svc['Port']}"
    raise Exception("Nenhum servico disponivel")

# Uso com load balancing simples
import random

def call_service():
    index, services = c.health.service('api-service', passing=True)
    if not services:
        raise Exception("Servico indisponivel")

    # Random selection (pode usar round-robin, least connections)
    svc = random.choice(services)['Service']
    url = f"http://{svc['Address']}:{svc['Port']}/api/data"
    return requests.get(url).json()
```

### Health Checking Patterns

```python
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/health")
async def health_check():
    """Health check basico"""
    return {"status": "healthy"}

@app.get("/health/ready")
async def readiness_check():
    """Readiness check - servico pronto para receber trafego"""
    checks = {
        "database": await check_database(),
        "cache": await check_cache(),
        "external_api": await check_external_api(),
    }
    all_healthy = all(checks.values())
    return {
        "status": "ready" if all_healthy else "not_ready",
        "checks": checks,
    }

@app.get("/health/live")
async def liveness_check():
    """Liveness check - processo esta vivo"""
    return {"status": "alive"}
```

---

## Distributed Tracing

### OpenTelemetry Setup

```python
# Python - OpenTelemetry
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from fastapi import FastAPI

# Setup
trace.set_tracer_provider(TracerProvider())
jaeger_exporter = JaegerExporter(
    agent_host_name='localhost',
    agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

app = FastAPI()
FastAPIInstrumentor.instrument_app(app)

tracer = trace.get_tracer("order-service")

@app.post("/orders")
async def create_order(order_data: dict):
    with tracer.start_as_current_span("create_order") as span:
        span.set_attribute("order.user_id", order_data["user_id"])

        # Propagacao de contexto para servico externo
        from opentelemetry.propagate import inject
        headers = {}
        inject(headers)

        # Chamada para outro servico
        import httpx
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://payment-service/charge",
                json={"amount": order_data["total"]},
                headers=headers,  # Contexto propagado
            )

        span.set_attribute("payment.status", response.status_code)
        return response.json()
```

```typescript
// TypeScript - OpenTelemetry
import { trace, context, propagation } from '@opentelemetry/api'
import { NodeTracerProvider } from '@opentelemetry/sdk-trace-node'
import { JaegerExporter } from '@opentelemetry/exporter-jaeger'
import { BatchSpanProcessor } from '@opentelemetry/sdk-trace-base'

// Setup
const provider = new NodeTracerProvider()
const exporter = new JaegerExporter({ host: 'localhost', port: 6831 })
provider.addSpanProcessor(new BatchSpanProcessor(exporter))
provider.register()

const tracer = trace.getTracer('order-service')

async function createOrder(orderData: any) {
  return tracer.startActiveSpan('create_order', async (span) => {
    span.setAttribute('order.user_id', orderData.user_id)

    // Propagacao de contexto
    const headers: Record<string, string> = {}
    propagation.inject(context.active(), headers)

    // Chamada para outro servico
    const response = await fetch('http://payment-service/charge', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...headers },
      body: JSON.stringify({ amount: orderData.total }),
    })

    span.setAttribute('payment.status', response.status)
    return response.json()
  })
}
```

### Trace Context Propagation

```
Request -> [Service A] --trace-id: abc, span-id: 1--> [Service B]
              |                                         |
         span: abc.1                              span: abc.2
              |                                         |
              v                                         v
         [Database]                               [Service C]
         span: abc.1.1                            span: abc.2.3
```

---

## Caching em Sistemas Distribuidos

### Estrategias de Invalidacao

| Estrategia | Descricao | Vantagem | Desvantagem |
|-----------|-----------|----------|-------------|
| TTL | Expira apos tempo | Simples | Dados stale possiveis |
| Write-through | Escreve cache + DB同步 | Consistencia | Latencia de escrita |
| Write-behind | Escreve cache, DB async | Alta performance | Risco de perda |
| Cache-aside | App gerencia cache | Flexivel | Complexidade |

### Redis Distributed Cache

```python
# Python - Redis com cache stampede prevention
import redis
import hashlib
import time
from functools import wraps

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def cache_with_lock(key: str, ttl: int = 300):
    """Cache com lock para prevenir cache stampede"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = f"cache:{key}:{hashlib.md5(str(args).encode()).hexdigest()}"
            lock_key = f"lock:{cache_key}"

            # Tenta obter do cache
            value = redis_client.get(cache_key)
            if value:
                return value

            # Tenta adquirir lock
            lock_acquired = redis_client.set(lock_key, "1", nx=True, ex=10)
            if lock_acquired:
                try:
                    # Computa valor
                    result = func(*args, **kwargs)
                    redis_client.setex(cache_key, ttl, result)
                    return result
                finally:
                    redis_client.delete(lock_key)
            else:
                # Outro processo esta computando, espera
                time.sleep(0.1)
                return wrapper(*args, **kwargs)  # Retry
        return wrapper
    return decorator

@cache_with_lock("user_profile", ttl=600)
def get_user_profile(user_id: int) -> dict:
    # Query cara ao banco
    return db.query_user(user_id)
```

```typescript
// TypeScript - Redis com ioredis
import Redis from 'ioredis'
import crypto from 'crypto'

const redis = new Redis()

async function getWithCache<T>(
  key: string,
  ttl: number,
  fetchFn: () => Promise<T>
): Promise<T> {
  const cached = await redis.get(key)
  if (cached) return JSON.parse(cached)

  // Lock para prevenir stampede
  const lockKey = `lock:${key}`
  const acquired = await redis.set(lockKey, '1', 'EX', 10, 'NX')

  if (acquired) {
    try {
      const result = await fetchFn()
      await redis.setex(key, ttl, JSON.stringify(result))
      return result
    } finally {
      await redis.del(lockKey)
    }
  }

  // Espera e retry
  await new Promise((r) => setTimeout(r, 100))
  return getWithCache(key, ttl, fetchFn)
}
```

### Consistent Hashing

```
    Hash Ring (0 - 2^32):

    0         2^31         2^32
    |-----------|------------|
    |           |            |
  Node A     Node B       Node C
  (0x1A2B)   (0x7F3C)    (0xE4D1)

    Chave "user:123" -> hash("user:123") = 0x5A1F
    0x5A1F esta entre 0x1A2B e 0x7F3C -> Node B
```

```python
import hashlib
from bisect import bisect

class ConsistentHash:
    def __init__(self, nodes: list, replicas: int = 150):
        self.ring = []
        self.ring_map = {}
        for node in nodes:
            for i in range(replicas):
                key = hashlib.md5(f"{node}:{i}".encode()).hexdigest()
                int_key = int(key, 16)
                self.ring.append(int_key)
                self.ring_map[int_key] = node
        self.ring.sort()

    def get_node(self, key: str) -> str:
        hash_key = int(hashlib.md5(key.encode()).hexdigest(), 16)
        idx = bisect(self.ring, hash_key) % len(self.ring)
        return self.ring_map[self.ring[idx]]

# Uso
ch = ConsistentHash(['node-a', 'node-b', 'node-c'])
node = ch.get_node('user:123')  # Retorna o node responsavel
```

---

## Load Balancing

### Algoritmos

| Algoritmo | Descricao | Ideal para |
|-----------|-----------|------------|
| Round-robin | Rotacao igual | Servicos homogeneos |
| Weighted RR | Pesos por instancia | Capacidades diferentes |
| Least connections | Menos conexoes ativas | Requests de duracao variada |
| Consistent hashing | Mesma chave -> mesmo node | Sessoes, cache |
| Random | Aleatorio | Simplicidade |

```python
# Round-robin com health check
import threading
from typing import List

class LoadBalancer:
    def __init__(self, backends: List[str]):
        self.backends = backends
        self.current = 0
        self.lock = threading.Lock()
        self.healthy = set(backends)

    def get_backend(self) -> str:
        with self.lock:
            healthy_backends = [b for b in self.backends if b in self.healthy]
            if not healthy_backends:
                raise Exception("Nenhum backend saudavel")

            backend = healthy_backends[self.current % len(healthy_backends)]
            self.current += 1
            return backend

    def mark_unhealthy(self, backend: str):
        self.healthy.discard(backend)

    def mark_healthy(self, backend: str):
        self.healthy.add(backend)
```

### Circuit Breaker

```python
# Python - Circuit Breaker
import time
from enum import Enum

class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.state = CircuitState.CLOSED
        self.last_failure_time = 0

    def call(self, func, *args, **kwargs):
        if self.state == CircuitState.OPEN:
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = CircuitState.HALF_OPEN
            else:
                raise Exception("Circuit breaker aberto")

        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise

    def _on_success(self):
        self.failure_count = 0
        self.state = CircuitState.CLOSED

    def _on_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
```

```typescript
// TypeScript - Circuit Breaker
type CircuitState = 'closed' | 'open' | 'half_open'

class CircuitBreaker {
  private state: CircuitState = 'closed'
  private failureCount = 0
  private lastFailureTime = 0

  constructor(
    private failureThreshold: number = 5,
    private recoveryTimeout: number = 30000
  ) {}

  async call<T>(fn: () => Promise<T>): Promise<T> {
    if (this.state === 'open') {
      if (Date.now() - this.lastFailureTime > this.recoveryTimeout) {
        this.state = 'half_open'
      } else {
        throw new Error('Circuit breaker aberto')
      }
    }

    try {
      const result = await fn()
      this.onSuccess()
      return result
    } catch (error) {
      this.onFailure()
      throw error
    }
  }

  private onSuccess() {
    this.failureCount = 0
    this.state = 'closed'
  }

  private onFailure() {
    this.failureCount++
    this.lastFailureTime = Date.now()
    if (this.failureCount >= this.failureThreshold) {
      this.state = 'open'
    }
  }
}

// Uso
const breaker = new CircuitBreaker(5, 30000)
const result = await breaker.call(() => fetchExternalAPI())
```

### Retry com Exponential Backoff e Jitter

```python
import time
import random

def retry_with_backoff(func, max_retries=3, base_delay=1, max_delay=60):
    for attempt in range(max_retries + 1):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries:
                raise
            delay = min(base_delay * (2 ** attempt), max_delay)
            jitter = random.uniform(0, delay * 0.5)  # Jitter de 50%
            time.sleep(delay + jitter)
```

```typescript
async function retryWithBackoff<T>(
  fn: () => Promise<T>,
  maxRetries = 3,
  baseDelay = 1000,
  maxDelay = 60000
): Promise<T> {
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await fn()
    } catch (error) {
      if (attempt === maxRetries) throw error
      const delay = Math.min(baseDelay * Math.pow(2, attempt), maxDelay)
      const jitter = Math.random() * delay * 0.5
      await new Promise((r) => setTimeout(r, delay + jitter))
    }
  }
  throw new Error('Nao deveria chegar aqui')
}
```

---

## Dados Distribuidos

### Estrategias de Sharding

| Estrategia | Descricao | Vantagem | Desvantagem |
|-----------|-----------|----------|-------------|
| Hash-based | hash(key) % N | Distribuicao uniforme | Rebalanceamento complexo |
| Range-based | Intervalos de chave | Queries de range eficientes | Hot spots |
| Directory-based | Tabela de lookup | Flexivel | Single point of failure |
| Geo-based | Por localizacao | Latencia baixa | Distribuicao desigual |

### Replicacao

```
LEADER-FOLLOWER:
  Writes -> [Leader] --replica--> [Follower 1]
                    --replica--> [Follower 2]
  Reads  -> Qualquer node

MULTI-LEADER:
  Writes -> [Leader A] <--sync--> [Leader B]
  Reads  -> Qualquer node
  
LEADERLESS (Dynamo-style):
  Writes -> [Node A], [Node B], [Node C] (quorum)
  Reads  -> [Node A], [Node B], [Node C] (quorum)
```

### Resolucao de Conflitos

```python
# Vector Clocks
from typing import Dict

class VectorClock:
    def __init__(self, node_id: str, clocks: Dict[str, int] = None):
        self.clocks = clocks or {}
        self.node_id = node_id

    def increment(self):
        self.clocks[self.node_id] = self.clocks.get(self.node_id, 0) + 1

    def merge(self, other: 'VectorClock'):
        all_nodes = set(self.clocks.keys()) | set(other.clocks.keys())
        for node in all_nodes:
            self.clocks[node] = max(
                self.clocks.get(node, 0),
                other.clocks.get(node, 0)
            )

    def happens_before(self, other: 'VectorClock') -> bool:
        # self happened antes de other
        at_least_one_less = False
        for node in set(self.clocks.keys()) | set(other.clocks.keys()):
            if self.clocks.get(node, 0) > other.clocks.get(node, 0):
                return False
            if self.clocks.get(node, 0) < other.clocks.get(node, 0):
                at_least_one_less = True
        return at_least_one_less
```

---

## Referencias Cruzadas

- [[devops/Kubernetes]] - Orquestracao de containers
- [[data-engineering/streaming]] - Processamento de streams
- [[backend]] - Arquitetura backend
- [[api-design]] - Design de APIs
