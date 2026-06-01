---
tags: [architecture-patterns, software-engineering, clean-architecture, hexagonal, event-driven, microservices, serverless, skills-eng]
updated: 2026-06-01
title: "Architecture Patterns - Software Architecture"
date: 2026-06-01
---

# Architecture Patterns - Padroes de Arquitetura de Software

Catalogo completo de padroes de arquitetura com exemplos praticos em Python e TypeScript.

## Sumario

- [[#Arquitetura em Camadas]]
- [[#Clean Architecture]]
- [[#Arquitetura Hexagonal]]
- [[#Arquitetura Orientada a Eventos]]
- [[#Arquitetura de Microservicos]]
- [[#Arquitetura Serverless]]

---

## Arquitetura em Camadas

### 3-Tier (Tres Camadas)

```ascii
+---------------------------+
|    Presentation Layer     |  <- UI, API endpoints
+---------------------------+
|     Business Logic Layer  |  <- Regras de negocio, servicos
+---------------------------+
|      Data Access Layer    |  <- Repositorios, banco de dados
+---------------------------+
```

**Vantagens:** Separacao de responsabilidades, manutenibilidade, testabilidade.
**Desvantagens:** Acoplamento entre camadas, desempenho em chamadas em cascata, dificil escalabilidade independente.
**Quando usar:** Aplicacoes empresariais tradicionais, sistemas monoliticos, equipes organizadas por camada.

### n-Tier (N Camadas)

```ascii
+--------+  +--------+  +--------+  +--------+  +--------+
| Client |->|  API   |->|Service |->| Domain |->|  Data  |
| Layer  |  | Layer  |  | Layer  |  | Layer  |  | Layer  |
+--------+  +--------+  +--------+  +--------+  +--------+
```

Adiciona camadas intermediarias como servicos, dominio, cache, mensageria.

**Comparacao:**

| Aspecto | 3-Tier | n-Tier |
|---------|--------|--------|
| Complexidade | Baixa | Alta |
| Escalabilidade | Limitada | Flexivel |
| Manutenibilidade | Media | Alta |
| Desempenho | Bom | Variavel |
| Ideal para | Apps simples | Sistemas empresariais |

---

## Clean Architecture (Uncle Bob)

### Regra de Dependencia

```ascii
                    +-----------------------+
                    |   Frameworks & Drivers|  <- Externo (DB, UI, Web)
                    +-----------------------+
                    | Interface Adapters    |  <- Controllers, Presenters
                    +-----------------------+
                    |   Use Cases           |  <- Regras de aplicacao
                    +-----------------------+
                    |   Entities            |  <- Regras de negocio (interno)
                    +-----------------------+
```

**Regra fundamental:** Dependencias apontam SEMPRE para o centro. Camadas externas dependem de internas, nunca o contrario.

### Estrutura de Projeto

```
src/
├── entities/           # Regras de negocio puras
├── use_cases/          # Casos de uso da aplicacao
├── interface_adapters/ # Controllers, presenters, gateways
└── frameworks/         # DB, web framework, external APIs
```

### Python (FastAPI)

```python
# === ENTITIES (camada mais interna) ===
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Pedido:
    id: str
    cliente_id: str
    itens: list[dict]
    status: str
    criado_em: datetime

    def total(self) -> float:
        return sum(item["preco"] * item["quantidade"] for item in self.itens)

    def pode_cancelar(self) -> bool:
        return self.status in ("criado", "pendente")

# === USE CASES ===
from abc import ABC, abstractmethod

class PedidoRepositorio(ABC):
    @abstractmethod
    def salvar(self, pedido: Pedido) -> None: ...
    @abstractmethod
    def buscar(self, id: str) -> Pedido | None: ...

class CriarPedidoUseCase:
    def __init__(self, repositorio: PedidoRepositorio) -> None:
        self._repositorio = repositorio

    def executar(self, cliente_id: str, itens: list[dict]) -> Pedido:
        pedido = Pedido(
            id=f"PED-{len(str(hash(cliente_id)))}",
            cliente_id=cliente_id,
            itens=itens,
            status="criado",
            criado_em=datetime.now()
        )
        self._repositorio.salvar(pedido)
        return pedido

class CancelarPedidoUseCase:
    def __init__(self, repositorio: PedidoRepositorio) -> None:
        self._repositorio = repositorio

    def executar(self, pedido_id: str) -> bool:
        pedido = self._repositorio.buscar(pedido_id)
        if not pedido or not pedido.pode_cancelar():
            return False
        pedido.status = "cancelado"
        self._repositorio.salvar(pedido)
        return True

# === INTERFACE ADAPTERS ===
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class PedidoInput(BaseModel):
    cliente_id: str
    itens: list[dict]

# Repositorio concreto (injetado via DI)
repositorio: PedidoRepositorio = ...  # injetar
criar_pedido = CriarPedidoUseCase(repositorio)
cancelar_pedido = CancelarPedidoUseCase(repositorio)

@app.post("/pedidos")
def criar(input: PedidoInput):
    return criar_pedido.executar(input.cliente_id, input.itens)

@app.delete("/pedidos/{pedido_id}")
def cancelar(pedido_id: str):
    if not cancelar_pedido.executar(pedido_id):
        raise HTTPException(400, "Nao foi possivel cancelar")
    return {"status": "cancelado"}
```

### TypeScript (Express)

```typescript
// === ENTITIES ===
class Pedido {
  constructor(
    public id: string,
    public clienteId: string,
    public itens: Array<{ preco: number; quantidade: number }>,
    public status: string,
    public criadoEm: Date
  ) {}

  total(): number {
    return this.itens.reduce((s, i) => s + i.preco * i.quantidade, 0);
  }

  podeCancelar(): boolean {
    return ["criado", "pendente"].includes(this.status);
  }
}

// === USE CASES ===
interface PedidoRepositorio {
  salvar(pedido: Pedido): Promise<void>;
  buscar(id: string): Promise<Pedido | null>;
}

class CriarPedidoUseCase {
  constructor(private repositorio: PedidoRepositorio) {}

  async executar(clienteId: string, itens: any[]): Promise<Pedido> {
    const pedido = new Pedido(
      `PED-${Date.now()}`,
      clienteId,
      itens,
      "criado",
      new Date()
    );
    await this.repositorio.salvar(pedido);
    return pedido;
  }
}

class CancelarPedidoUseCase {
  constructor(private repositorio: PedidoRepositorio) {}

  async executar(pedidoId: string): Promise<boolean> {
    const pedido = await this.repositorio.buscar(pedidoId);
    if (!pedido || !pedido.podeCancelar()) return false;
    pedido.status = "cancelado";
    await this.repositorio.salvar(pedido);
    return true;
  }
}

// === INTERFACE ADAPTERS ===
import express from "express";
const app = express();
app.use(express.json());

const repositorio: PedidoRepositorio = /* injetar */;
const criarPedido = new CriarPedidoUseCase(repositorio);
const cancelarPedido = new CancelarPedidoUseCase(repositorio);

app.post("/pedidos", async (req, res) => {
  const pedido = await criarPedido.executar(
    req.body.clienteId,
    req.body.itens
  );
  res.json(pedido);
});

app.delete("/pedidos/:id", async (req, res) => {
  const ok = await cancelarPedido.executar(req.params.id);
  if (!ok) return res.status(400).json({ erro: "Nao foi possivel cancelar" });
  res.json({ status: "cancelado" });
});
```

---

## Arquitetura Hexagonal (Ports & Adapters)

### Conceito

```ascii
            +-----------------------------------+
            |          ADAPTERS (entrada)        |
            |  REST API | gRPC | CLI | Events    |
            +---------------|-------------------+
                            |
    +-----------------------v-----------------------+
    |                  PORTS (entrada)               |
    |         Interfaces que o dominio expoe         |
    +-----------------------|-----------------------+
                            |
    +-----------------------v-----------------------+
    |              DOMINIO (CORE)                    |
    |    Entities + Value Objects + Domain Services  |
    +-----------------------|-----------------------+
                            |
    +-----------------------v-----------------------+
    |                  PORTS (saida)                 |
    |     Interfaces que o dominio precisa           |
    +-----------------------|-----------------------+
                            |
            +---------------v-------------------+
            |          ADAPTERS (saida)          |
            |   PostgreSQL | Redis | SMTP | S3   |
            +-----------------------------------+
```

### Python

```python
# === PORTS (Interfaces) ===
from abc import ABC, abstractmethod

# Port de entrada
class ProcessarPedidoPort(ABC):
    @abstractmethod
    def processar(self, cliente_id: str, itens: list[dict]) -> dict: ...

# Port de saida
class EstoquePort(ABC):
    @abstractmethod
    def verificar_disponibilidade(self, sku: str) -> int: ...
    @abstractmethod
    def reservar(self, sku: str, quantidade: int) -> bool: ...

class PagamentoPort(ABC):
    @abstractmethod
    def cobrar(self, valor: float, metodo: str) -> dict: ...

# === DOMINIO (Core) ===
class ProcessarPedidoService(ProcessarPedidoPort):
    def __init__(
        self,
        estoque: EstoquePort,
        pagamento: PagamentoPort
    ) -> None:
        self._estoque = estoque
        self._pagamento = pagamento

    def processar(self, cliente_id: str, itens: list[dict]) -> dict:
        # Verificar estoque
        for item in itens:
            disponivel = self._estoque.verificar_disponibilidade(item["sku"])
            if disponivel < item["quantidade"]:
                raise ValueError(f"SKU {item['sku']} indisponivel")

        # Reservar estoque
        for item in itens:
            self._estoque.reservar(item["sku"], item["quantidade"])

        # Processar pagamento
        total = sum(i["preco"] * i["quantidade"] for i in itens)
        resultado = self._pagamento.cobrar(total, "cartao")

        return {
            "cliente_id": cliente_id,
            "total": total,
            "pagamento": resultado,
            "status": "confirmado"
        }

# === ADAPTERS (entrada - REST) ===
from fastapi import FastAPI

app = FastAPI()
estoque_adapter = ...  # EstoquePostgresAdapter()
pagamento_adapter = ...  # PagamentoStripeAdapter()
servico = ProcessarPedidoService(estoque_adapter, pagamento_adapter)

@app.post("/api/pedidos")
def criar_pedido(cliente_id: str, itens: list[dict]):
    return servico.processar(cliente_id, itens)

# === ADAPTERS (saida - PostgreSQL) ===
class EstoquePostgresAdapter(EstoquePort):
    def verificar_disponibilidade(self, sku: str) -> int:
        # SELECT quantidade FROM estoque WHERE sku = ?
        return 100

    def reservar(self, sku: str, quantidade: int) -> bool:
        # UPDATE estoque SET quantidade = quantidade - ? WHERE sku = ?
        return True

class PagamentoStripeAdapter(PagamentoPort):
    def cobrar(self, valor: float, metodo: str) -> dict:
        # Stripe API call
        return {"status": "success", "transaction_id": "tx_123"}
```

### TypeScript

```typescript
// === PORTS ===
interface ProcessarPedidoPort {
  processar(clienteId: string, itens: any[]): Promise<any>;
}

interface EstoquePort {
  verificarDisponibilidade(sku: string): Promise<number>;
  reservar(sku: string, quantidade: number): Promise<boolean>;
}

interface PagamentoPort {
  cobrar(valor: number, metodo: string): Promise<any>;
}

// === DOMINIO ===
class ProcessarPedidoService implements ProcessarPedidoPort {
  constructor(
    private estoque: EstoquePort,
    private pagamento: PagamentoPort
  ) {}

  async processar(clienteId: string, itens: any[]): Promise<any> {
    for (const item of itens) {
      const disponivel = await this.estoque.verificarDisponibilidade(item.sku);
      if (disponivel < item.quantidade) {
        throw new Error(`SKU ${item.sku} indisponivel`);
      }
    }

    for (const item of itens) {
      await this.estoque.reservar(item.sku, item.quantidade);
    }

    const total = itens.reduce((s, i) => s + i.preco * i.quantidade, 0);
    const resultado = await this.pagamento.cobrar(total, "cartao");

    return { clienteId, total, pagamento: resultado, status: "confirmado" };
  }
}

// === ADAPTERS ===
class EstoquePostgresAdapter implements EstoquePort {
  async verificarDisponibilidade(sku: string): Promise<number> {
    // DB query
    return 100;
  }
  async reservar(sku: string, quantidade: number): Promise<boolean> {
    // DB update
    return true;
  }
}

class PagamentoStripeAdapter implements PagamentoPort {
  async cobrar(valor: number, metodo: string): Promise<any> {
    // Stripe API
    return { status: "success", transactionId: "tx_123" };
  }
}
```

---

## Arquitetura Orientada a Eventos

### Event Sourcing

```ascii
+--------+     +---------+     +-----------+     +-------------+
| Command| --> | Command | --> |   Event   | --> | Event Store |
|        |     | Handler |     | Emitter   |     | (Append-only)|
+--------+     +---------+     +-----------+     +-------------+
                                                         |
                                            +------------v------------+
                                            |   Projections / Views   |
                                            +-------------------------+
```

### CQRS (Command Query Responsibility Segregation)

```ascii
+---------+     +----------+     +-----------+
|  Write  | --> | Command  | --> | Event Sourcing
|  Model  |     |  Side    |     |   Store   |
+---------+     +----------+     +-----------+
                                         |
                                    (projetar)
                                         |
+---------+     +----------+     +-----------+
|  Read   | <-- |  Query   | <-- |   Read    |
|  Model  |     |  Side    |     |   Store   |
+---------+     +----------+     +-----------+
```

### Python

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Any

# === EVENTOS ===
@dataclass
class Evento:
    timestamp: datetime
    dados: dict

@dataclass
class PedidoCriado(Evento): pass

@dataclass
class PedidoPago(Evento): pass

@dataclass
class PedidoCancelado(Evento): pass

# === EVENT STORE ===
class EventStore:
    def __init__(self) -> None:
        self._eventos: list[Evento] = []

    def append(self, evento: Evento) -> None:
        self._eventos.append(evento)

    def get_stream(self, aggregate_id: str) -> list[Evento]:
        return [e for e in self._eventos if e.dados.get("id") == aggregate_id]

# === COMMAND HANDLER ===
class CommandHandler:
    def __init__(self, event_store: EventStore) -> None:
        self._event_store = event_store

    def criar_pedido(self, cliente_id: str, itens: list[dict]) -> str:
        pedido_id = f"PED-{len(self._event_store._eventos) + 1}"
        evento = PedidoCriado(
            timestamp=datetime.now(),
            dados={"id": pedido_id, "cliente_id": cliente_id, "itens": itens}
        )
        self._event_store.append(evento)
        return pedido_id

    def pagar_pedido(self, pedido_id: str, valor: float) -> None:
        evento = PedidoPago(
            timestamp=datetime.now(),
            dados={"id": pedido_id, "valor": valor}
        )
        self._event_store.append(evento)

# === PROJECTIONS (Read Model) ===
class PedidoProjection:
    def __init__(self, event_store: EventStore) -> None:
        self._event_store = event_store

    def get_pedido(self, pedido_id: str) -> dict:
        eventos = self._event_store.get_stream(pedido_id)
        estado: dict[str, Any] = {"id": pedido_id, "status": "criado"}
        for evento in eventos:
            if isinstance(evento, PedidoCriado):
                estado.update(evento.dados)
            elif isinstance(evento, PedidoPago):
                estado["status"] = "pago"
                estado["valor_pago"] = evento.dados["valor"]
        return estado

# === EVENT BUS (Pub/Sub) ===
class EventBus:
    def __init__(self) -> None:
        self._handlers: dict[str, list] = {}

    def subscribe(self, evento: str, handler) -> None:
        self._handlers.setdefault(evento, []).append(handler)

    def publish(self, evento: str, dados: dict) -> None:
        for handler in self._handlers.get(evento, []):
            handler(dados)

# Uso
store = EventStore()
handler = CommandHandler(store)
projection = PedidoProjection(store)

pedido_id = handler.criar_pedido("CLI-1", [{"sku": "A", "preco": 99.9, "quantidade": 2}])
handler.pagar_pedido(pedido_id, 199.8)
print(projection.get_pedido(pedido_id))
```

### TypeScript

```typescript
// === EVENTS ===
interface Evento {
  timestamp: Date;
  dados: Record<string, any>;
}

// === EVENT STORE ===
class EventStore {
  private eventos: Evento[] = [];

  append(evento: Evento): void {
    this.eventos.push(evento);
  }

  getStream(aggregateId: string): Evento[] {
    return this.eventos.filter(e => e.dados.id === aggregateId);
  }
}

// === COMMAND HANDLER ===
class CommandHandler {
  constructor(private eventStore: EventStore) {}

  criarPedido(clienteId: string, itens: any[]): string {
    const pedidoId = `PED-${this.eventStore['eventos'].length + 1}`;
    this.eventStore.append({
      timestamp: new Date(),
      dados: { id: pedidoId, clienteId, itens, tipo: "PedidoCriado" }
    });
    return pedidoId;
  }

  pagarPedido(pedidoId: string, valor: number): void {
    this.eventStore.append({
      timestamp: new Date(),
      dados: { id: pedidoId, valor, tipo: "PedidoPago" }
    });
  }
}

// === PROJECTION ===
class PedidoProjection {
  constructor(private eventStore: EventStore) {}

  getPedido(pedidoId: string): Record<string, any> {
    const eventos = this.eventStore.getStream(pedidoId);
    const estado: Record<string, any> = { id: pedidoId, status: "criado" };
    for (const evento of eventos) {
      if (evento.dados.tipo === "PedidoCriado") {
        Object.assign(estado, evento.dados);
      } else if (evento.dados.tipo === "PedidoPago") {
        estado.status = "pago";
        estado.valorPago = evento.dados.valor;
      }
    }
    return estado;
  }
}

// Uso
const store = new EventStore();
const handler = new CommandHandler(store);
const projection = new PedidoProjection(store);

const pedidoId = handler.criarPedido("CLI-1", [{ sku: "A", preco: 99.9, quantidade: 2 }]);
handler.pagarPedido(pedidoId, 199.8);
console.log(projection.getPedido(pedidoId));
```

---

## Arquitetura de Microservicos

### Decomposicao de Servicos

```ascii
+----------------------------------------------------------------+
|                        API Gateway                              |
+----------------------------------------------------------------+
        |              |              |              |
        v              v              v              v
+-------------+ +-------------+ +-------------+ +-------------+
|  Servico    | |  Servico    | |  Servico    | |  Servico    |
|  Usuario    | |  Pedido     | |  Pagamento  | |  Estoque    |
+-------------+ +-------------+ +-------------+ +-------------+
      |               |              |              |
      v               v              v              v
+-------------+ +-------------+ +-------------+ +-------------+
|   DB User   | |   DB Order  | |   DB Pay    | |   DB Stock  |
+-------------+ +-------------+ +-------------+ +-------------+
```

### Saga Pattern (Transacoes Distribuidas)

```ascii
Criar Pedido --> Reservar Estoque --> Processar Pagamento --> Confirmar Pedido
     |                |                     |                      |
     v                v                     v                      v
  Compensacao:    Compensacao:          Compensacao:             Fim
  Cancelar Pedido  Liberar Estoque      Reembolsar
```

### Python -- API Gateway + Saga

```python
import httpx
from abc import ABC, abstractmethod

# === SAGA PATTERN ===
class SagaStep(ABC):
    @abstractmethod
    async def execute(self, data: dict) -> dict: ...
    @abstractmethod
    async def compensate(self, data: dict) -> None: ...

class ReservarEstoqueStep(SagaStep):
    def __init__(self, estoque_url: str) -> None:
        self._url = estoque_url

    async def execute(self, data: dict) -> dict:
        async with httpx.AsyncClient() as client:
            resp = await client.post(f"{self._url}/reservar", json=data)
            return resp.json()

    async def compensate(self, data: dict) -> None:
        async with httpx.AsyncClient() as client:
            await client.post(f"{self._url}/liberar", json=data)

class ProcessarPagamentoStep(SagaStep):
    def __init__(self, pagamento_url: str) -> None:
        self._url = pagamento_url

    async def execute(self, data: dict) -> dict:
        async with httpx.AsyncClient() as client:
            resp = await client.post(f"{self._url}/cobrar", json=data)
            return resp.json()

    async def compensate(self, data: dict) -> None:
        async with httpx.AsyncClient() as client:
            await client.post(f"{self._url}/reembolsar", json=data)

class SagaOrchestrator:
    def __init__(self, steps: list[SagaStep]) -> None:
        self._steps = steps
        self._executados: list[dict] = []

    async def executar(self, dados_iniciais: dict) -> dict:
        dados = dados_iniciais
        for step in self._steps:
            try:
                dados = await step.execute(dados)
                self._executados.append(dados)
            except Exception:
                # Compensacao em ordem reversa
                for dados_exec in reversed(self._executados):
                    await step.compensate(dados_exec)
                raise RuntimeError("Saga falhou, compensacao executada")
        return dados

# Uso
async def criar_pedido_completo():
    saga = SagaOrchestrator([
        ReservarEstoqueStep("http://estoque:8080"),
        ProcessarPagamentoStep("http://pagamento:8080"),
    ])
    return await saga.executar({
        "pedido_id": "PED-1",
        "itens": [{"sku": "A", "quantidade": 2}],
        "valor": 199.8
    })
```

### TypeScript -- API Gateway

```typescript
import express from "express";
import axios from "axios";

const app = express();
app.use(express.json());

// === SERVICE REGISTRY ===
const services = {
  usuario: "http://usuario:8080",
  pedido: "http://pedido:8080",
  pagamento: "http://pagamento:8080",
  estoque: "http://estoque:8080",
};

// === API GATEWAY ===
app.post("/api/pedidos", async (req, res) => {
  try {
    // 1. Criar pedido
    const pedido = await axios.post(`${services.pedido}/pedidos`, req.body);

    // 2. Reservar estoque
    await axios.post(`${services.estoque}/reservar`, {
      pedidoId: pedido.data.id,
      itens: req.body.itens,
    });

    // 3. Processar pagamento
    await axios.post(`${services.pagamento}/cobrar`, {
      pedidoId: pedido.data.id,
      valor: req.body.total,
    });

    res.json({ status: "confirmado", pedido: pedido.data });
  } catch (error: any) {
    // Compensacao
    const pedidoId = error.response?.data?.pedidoId;
    if (pedidoId) {
      await axios.post(`${services.estoque}/liberar`, { pedidoId }).catch(() => {});
      await axios.post(`${services.pagamento}/reembolsar`, { pedidoId }).catch(() => {});
    }
    res.status(500).json({ erro: "Pedido falhou", detalhes: error.message });
  }
});
```

### Service Mesh Overview

```ascii
+--------------------------------------------------+
|                   Service Mesh                    |
|  +--------------------------------------------+  |
|  |             Control Plane                  |  |
|  |  (Istio Pilot / Linkerd Controller)        |  |
|  +--------------------------------------------+  |
|                          |                       |
|  +-----------+  +-----------+  +-----------+     |
|  |  Sidecar  |  |  Sidecar  |  |  Sidecar  |     |
|  |  (Envoy)  |  |  (Envoy)  |  |  (Envoy)  |     |
|  +-----|-----+  +-----|-----+  +-----|-----+     |
|        |              |              |            |
|  +-----v-----+  +-----v-----+  +-----v-----+     |
|  |  Service  |  |  Service  |  |  Service  |     |
|  |     A     |  |     B     |  |     C     |     |
|  +-----------+  +-----------+  +-----------+     |
+--------------------------------------------------+
```

Responsabilidades: Load balancing, service discovery, mTLS, circuit breaking, observability, rate limiting.

---

## Arquitetura Serverless

### FaaS Patterns

```ascii
+-----------+     +----------------+     +----------------+
|   Event   | --> |    Function    | --> |    Output      |
|  Source   |     |   (Stateless)  |     |   (DB, API)    |
+-----------+     +----------------+     +----------------+
     HTTP               REST API             DynamoDB
     S3                 Lambda               S3
     SQS                Cloud Function        Firestore
     Cron               Azure Function
```

### Cold Start Mitigation

| Estrategia | Descricao | Impacto |
|-----------|-----------|---------|
| Provisioned Concurrency | Manter instancias quentes | Alto custo, baixo latency |
| Keep-Warm Pings | Cron job a cada 5 min | Custo medio, eficacia media |
| Lighter Runtime | Usar runtime mais leve (Go, Rust) | Baixo custo, bom impacto |
| Smaller Packages | Minimizar dependencies | Baixo custo, bom impacto |
| ARM64 (Graviton) | Usar arquitetura ARM | Reduz custo ~20% |

### Python (AWS Lambda)

```python
import json
import os
from typing import Any

# === LAMBDA HANDLER ===
def lambda_handler(event: dict, context: Any) -> dict:
    """AWS Lambda handler para processamento de pedidos"""
    try:
        body = json.loads(event.get("body", "{}"))

        # Validar entrada
        if not body.get("cliente_id") or not body.get("itens"):
            return {
                "statusCode": 400,
                "body": json.dumps({"erro": "Dados incompletos"})
            }

        # Processar pedido
        pedido = processar_pedido(body["cliente_id"], body["itens"])

        return {
            "statusCode": 200,
            "body": json.dumps(pedido),
            "headers": {"Content-Type": "application/json"}
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"erro": str(e)})
        }

def processar_pedido(cliente_id: str, itens: list[dict]) -> dict:
    total = sum(i["preco"] * i["quantidade"] for i in itens)
    return {
        "pedido_id": f"PED-{cliente_id}-{total}",
        "cliente_id": cliente_id,
        "total": total,
        "status": "processado"
    }

# === EVENT-DRIVEN (S3 Trigger) ===
def s3_handler(event: dict, context: Any) -> None:
    """Processa arquivos enviados ao S3"""
    for record in event.get("Records", []):
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]
        print(f"Processando s3://{bucket}/{key}")
        # Processar arquivo...

# === SCHEDULED (EventBridge/Cron) ===
def cron_handler(event: dict, context: Any) -> None:
    """Executa tarefas agendadas"""
    print("Executando limpeza de pedidos expirados...")
    # Limpar pedidos antigos...
```

### TypeScript (GCP Cloud Functions)

```typescript
import { HttpFunction } from "@google-cloud/functions-framework";

// === HTTP FUNCTION ===
export const processarPedido: HttpFunction = async (req, res) => {
  try {
    const { clienteId, itens } = req.body;

    if (!clienteId || !itens) {
      return res.status(400).json({ erro: "Dados incompletos" });
    }

    const pedido = {
      pedidoId: `PED-${clienteId}-${Date.now()}`,
      clienteId,
      total: itens.reduce((s: number, i: any) => s + i.preco * i.quantidade, 0),
      status: "processado",
    };

    res.json(pedido);
  } catch (error: any) {
    res.status(500).json({ erro: error.message });
  }
};

// === EVENT-DRIVEN (Pub/Sub) ===
export const processarEvento: HttpFunction = async (req, res) => {
  const message = Buffer.from(req.body.message.data, "base64").toString();
  const dados = JSON.parse(message);

  console.log("Processando evento:", dados);
  // Processar evento...

  res.status(204).send();
};

// === CLOUD SCHEDULED ===
export const tarefaAgendada: HttpFunction = async (req, res) => {
  console.log("Executando limpeza de pedidos expirados...");
  // Limpar pedidos antigos...
  res.status(204).send();
};
```

---

## Tabela Comparativa de Arquiteturas

| Arquitetura | Complexidade | Escalabilidade | Custo | Ideal para |
|-------------|-------------|----------------|-------|------------|
| 3-Tier | Baixa | Media | Baixo | Apps simples |
| Clean Arch | Media | Media | Medio | Apps empresariais |
| Hexagonal | Alta | Alta | Medio | Dominios complexos |
| Event-Driven | Alta | Alta | Medio-Alto | Sistemas reativos |
| Microservicos | Muito Alta | Muito Alta | Alto | Grandes equipes |
| Serverless | Media | Muito Alta | Variavel | Workloads esporadicos |

## Referencias Cruzadas

- Ver [[design-patterns]] para padroes de projeto GoF
- Ver [[backend]] para implementacoes de servicos
- Ver [[devops/ci-cd/INDEX]] para pipelines de deploy
- Ver [[devops/Kubernetes]] para orquestracao de containers