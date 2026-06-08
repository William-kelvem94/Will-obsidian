---
title: "Arquitetura de Software"
date: 2026-05-16
area: "Programação e Engenharia de Software"
tags: [conhecimento, programacao, arquitetura, ddd, solid, microservicos]
related: ["05-Skills/02-software-engineering/advanced-backend-architecture"]
aliases: ["Software Architecture", "Clean Architecture", "DDD"]
---

# Arquitetura de Software

Arquitetura de software é o conjunto de **decisões fundamentais** sobre a estrutura de um sistema: componentes, relacionamentos, princípios e guias de evolução. Como disse Robert Martin: *"Architecture is about intent"* — a arquitetura revela o que o sistema **pretende ser**.

**Referência:** Martin, Robert C. *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall, 2017.

---

## 1. Princípios Fundamentais

### 1.1 Separation of Concerns (SoC)

Dividir o sistema em seções distintas, onde cada uma aborda uma **preocupação** específica.

```
+------------------------------------------+
|           Interface do Usuário            |
+------------------------------------------+
|           Lógica de Aplicação             |
+------------------------------------------+
|           Domínio / Regras de Negócio     |
+------------------------------------------+
|              Infraestrutura               |
+------------------------------------------+
```

### 1.2 Dependency Inversion Principle

Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de **abstrações**.

```python
# Ruim: alto nível depende de baixo nível
class MySQLDatabase:
    def salvar(self, dados: dict) -> None: ...

class UsuarioService:
    def __init__(self):
        self._db = MySQLDatabase()  # Acoplamento direto

# Bom: ambos dependem de abstração
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def salvar(self, dados: dict) -> None: ...

class MySQLDatabase(Database):
    def salvar(self, dados: dict) -> None: ...

class UsuarioService:
    def __init__(self, db: Database):
        self._db = db  # Inversão de dependência
```

```typescript
// Ruim
class MySQLDatabase {
  salvar(dados: Record<string, unknown>): void {}
}

class UsuarioService {
  private db = new MySQLDatabase();
}

// Bom
interface Database {
  salvar(dados: Record<string, unknown>): void;
}

class MySQLDatabase implements Database {
  salvar(dados: Record<string, unknown>): void {}
}

class UsuarioService {
  constructor(private readonly db: Database) {}
}
```

---

## 2. Os 5 Princípios SOLID

SOLID é um acrônimo cunhado por Robert Martin que reúne cinco princípios essenciais da orientação a objetos.

**Referência:** Martin, Robert C. *Agile Software Development, Principles, Patterns, and Practices*. Prentice Hall, 2002.

### 2.1 Single Responsibility Principle (SRP)

> Uma classe deve ter **apenas uma razão para mudar**.

```python
# Ruim: mistura responsabilidades
class Relatorio:
    def gerar_dados(self) -> str: ...
    def formatar_html(self) -> str: ...
    def enviar_por_email(self) -> None: ...

# Bom: cada classe tem uma responsabilidade
class ColetorDados:
    def coletar(self) -> dict: ...

class FormatadorRelatorio:
    def formatar(self, dados: dict) -> str: ...

class ServicoEmail:
    def enviar(self, destinatario: str, corpo: str) -> None: ...
```

```typescript
// Ruim
class Relatorio {
  gerarDados(): string { return ""; }
  formatarHTML(): string { return ""; }
  enviarPorEmail(): void {}
}

// Bom
class ColetorDados {
  coletar(): Record<string, unknown> { return {}; }
}

class FormatadorRelatorio {
  formatar(dados: Record<string, unknown>): string { return ""; }
}

class ServicoEmail {
  enviar(destinatario: string, corpo: string): void {}
}
```

### 2.2 Open/Closed Principle (OCP)

> Entidades devem estar **abertas para extensão, fechadas para modificação**.

```python
from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float: ...

class DescontoFixo(Desconto):
    def __init__(self, percentual: float):
        self._percentual = percentual

    def calcular(self, valor: float) -> float:
        return valor * (1 - self._percentual)

class DescontoProgressivo(Desconto):
    def calcular(self, valor: float) -> float:
        if valor > 1000:
            return valor * 0.8
        if valor > 500:
            return valor * 0.9
        return valor * 0.95

# Novo tipo: basta estender
class DescontoBlackFriday(Desconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.5

def aplicar_desconto(desconto: Desconto, valor: float) -> float:
    return desconto.calcular(valor)
```

```typescript
interface Desconto {
  calcular(valor: number): number;
}

class DescontoFixo implements Desconto {
  constructor(private readonly percentual: number) {}

  calcular(valor: number): number {
    return valor * (1 - this.percentual);
  }
}

class DescontoProgressivo implements Desconto {
  calcular(valor: number): number {
    if (valor > 1000) return valor * 0.8;
    if (valor > 500) return valor * 0.9;
    return valor * 0.95;
  }
}

class DescontoBlackFriday implements Desconto {
  calcular(valor: number): number {
    return valor * 0.5;
  }
}
```

### 2.3 Liskov Substitution Principle (LSP)

> Subtipos devem ser substituíveis por seus tipos base sem alterar a corretude do programa.

```python
class Retangulo:
    def __init__(self):
        self._largura = 0
        self._altura = 0

    def definir_largura(self, valor: int) -> None:
        self._largura = valor

    def definir_altura(self, valor: int) -> None:
        self._altura = valor

    def area(self) -> int:
        return self._largura * self._altura

class Quadrado(Retangulo):
    """Violação de LSP: quadrado restringe o comportamento."""
    def definir_largura(self, valor: int) -> None:
        self._largura = valor
        self._altura = valor

    def definir_altura(self, valor: int) -> None:
        self._largura = valor
        self._altura = valor

# Código cliente que espera Retangulo quebra com Quadrado
def calcular_area(retangulo: Retangulo) -> int:
    retangulo.definir_largura(5)
    retangulo.definir_altura(10)
    return retangulo.area()  # Espera 50, mas Quadrado retorna 100

# Solução: não usar herança, usar interface separada
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self) -> int: ...

class Retangulo(Forma):
    def __init__(self, largura: int, altura: int):
        self._largura = largura
        self._altura = altura

    def area(self) -> int:
        return self._largura * self._altura

class Quadrado(Forma):
    def __init__(self, lado: int):
        self._lado = lado

    def area(self) -> int:
        return self._lado ** 2
```

```typescript
// Violação de LSP
class Retangulo {
  constructor(protected largura: number, protected altura: number) {}

  area(): number {
    return this.largura * this.altura;
  }
}

class Quadrado extends Retangulo {
  constructor(lado: number) {
    super(lado, lado);
  }
}

// Correto: interface comum sem herança problemática
interface Forma {
  area(): number;
}

class Retangulo implements Forma {
  constructor(private largura: number, private altura: number) {}

  area(): number {
    return this.largura * this.altura;
  }
}

class Quadrado implements Forma {
  constructor(private lado: number) {}

  area(): number {
    return this.lado ** 2;
  }
}
```

### 2.4 Interface Segregation Principle (ISP)

> Interfaces específicas são melhores que interfaces genéricas. Muitas interfaces coesas > uma interface "god object".

```python
from abc import ABC, abstractmethod

# Ruim: interface muito abrangente
class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self) -> None: ...
    @abstractmethod
    def comer(self) -> None: ...
    @abstractmethod
    def dormir(self) -> None: ...

# Bom: interfaces segregadas
class Trabalhavel(ABC):
    @abstractmethod
    def trabalhar(self) -> None: ...

class Comivel(ABC):
    @abstractmethod
    def comer(self) -> None: ...

class Dormivel(ABC):
    @abstractmethod
    def dormir(self) -> None: ...

class Humano(Trabalhavel, Comivel, Dormivel):
    def trabalhar(self) -> None: ...
    def comer(self) -> None: ...
    def dormir(self) -> None: ...

class Robo(Trabalhavel):
    def trabalhar(self) -> None: ...
```

```typescript
// Ruim
interface Trabalhador {
  trabalhar(): void;
  comer(): void;
  dormir(): void;
}

// Bom
interface Trabalhavel {
  trabalhar(): void;
}

interface Comivel {
  comer(): void;
}

interface Dormivel {
  dormir(): void;
}

class Humano implements Trabalhavel, Comivel, Dormivel {
  trabalhar(): void {}
  comer(): void {}
  dormir(): void {}
}

class Robo implements Trabalhavel {
  trabalhar(): void {}
}
```

### 2.5 Dependency Inversion Principle (DIP)

Já detalhado na seção 1.2 acima. Módulos de alto nível não devem depender de módulos de baixo nível.

---

## 3. Clean Architecture (Arquitetura Limpa)

Proposta por Robert Martin, a Clean Architecture organiza o sistema em **círculos concêntricos** onde as dependências apontam para **dentro** (do mais concreto para o mais abstrato).

```
                  +---------------------------+
                  |    Frameworks & Drivers   |
                  |  +---------------------+  |
                  |  |  Interface Adapters |  |
                  |  |  +---------------+  |  |
                  |  |  | Use Cases     |  |  |
                  |  |  |  +---------+  |  |  |
                  |  |  |  | Entities|  |  |  |
                  |  |  |  +----+----+  |  |  |
                  |  |  +-------+------+  |  |
                  |  +----------+--------+  |
                  +-------------+-----------+
```

**Regra de Dependência:** O código fonte só pode depender de **dentro para fora**. Nada no círculo interno sabe sobre algo no círculo externo.

### 3.1 Exemplo Prático

```python
# Camada de Domínio (Entities)
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Usuario:
    id: str
    nome: str
    email: str

class RepositorioUsuarios(ABC):
    @abstractmethod
    def buscar_por_id(self, id: str) -> Usuario | None: ...
    @abstractmethod
    def salvar(self, usuario: Usuario) -> None: ...

# Caso de Uso (Application)
class AtualizarEmail:
    def __init__(self, repo: RepositorioUsuarios):
        self._repo = repo

    def executar(self, usuario_id: str, novo_email: str) -> Usuario:
        usuario = self._repo.buscar_por_id(usuario_id)
        if not usuario:
            raise ValueError("Usuário não encontrado")
        usuario.email = novo_email
        self._repo.salvar(usuario)
        return usuario

# Adaptador de Interface (Infra)
class RepositorioUsuariosSQL(RepositorioUsuarios):
    def __init__(self, conexao: str):
        self._conexao = conexao

    def buscar_por_id(self, id: str) -> Usuario | None:
        # SQL query real
        return None

    def salvar(self, usuario: Usuario) -> None:
        # SQL INSERT/UPDATE
        pass
```

```typescript
// Domínio
interface Usuario {
  id: string;
  nome: string;
  email: string;
}

interface RepositorioUsuarios {
  buscarPorId(id: string): Promise<Usuario | null>;
  salvar(usuario: Usuario): Promise<void>;
}

// Caso de Uso
class AtualizarEmail {
  constructor(private readonly repo: RepositorioUsuarios) {}

  async executar(usuarioId: string, novoEmail: string): Promise<Usuario> {
    const usuario = await this.repo.buscarPorId(usuarioId);
    if (!usuario) throw new Error("Usuário não encontrado");
    const atualizado: Usuario = { ...usuario, email: novoEmail };
    await this.repo.salvar(atualizado);
    return atualizado;
  }
}

// Infra
class RepositorioUsuariosSQL implements RepositorioUsuarios {
  constructor(private readonly conexao: string) {}

  async buscarPorId(id: string): Promise<Usuario | null> {
    return null;
  }

  async salvar(usuario: Usuario): Promise<void> {}
}
```

---

## 4. Arquitetura Hexagonal (Ports & Adapters)

Proposta por Alistair Cockburn, a arquitetura hexagonal isola o núcleo da aplicação do mundo externo através de **portas** (interfaces) e **adaptadores** (implementações).

```
  [Cliente] --> [Adaptador Web] --> |Porta In| [Núcleo] |Porta Out| --> [Adaptador DB]
  [CLI]     --> [Adaptador CLI] --> |        |          |         | --> [Adaptador API]
```

- **Portas (Ports):** Interfaces que definem como o mundo externo interage com o sistema.
- **Adaptadores (Adapters):** Implementações concretas das portas.

```python
# Porta de entrada
class ServicoPagamento(ABC):
    @abstractmethod
    def processar(self, pedido_id: str, valor: float) -> bool: ...

# Porta de saída
class RepositorioPedidos(ABC):
    @abstractmethod
    def atualizar_status(self, pedido_id: str, status: str) -> None: ...

# Núcleo da aplicação
class ProcessadorPagamentos:
    def __init__(
        self,
        pagamento: ServicoPagamento,
        pedidos: RepositorioPedidos
    ):
        self._pagamento = pagamento
        self._pedidos = pedidos

    def executar(self, pedido_id: str, valor: float) -> bool:
        if self._pagamento.processar(pedido_id, valor):
            self._pedidos.atualizar_status(pedido_id, "pago")
            return True
        return False

# Adaptadores
class ServicoPagamentoStripe(ServicoPagamento):
    def processar(self, pedido_id: str, valor: float) -> bool:
        # Integração com Stripe
        return True

class RepositorioPedidosPostgres(RepositorioPedidos):
    def atualizar_status(self, pedido_id: str, status: str) -> None:
        # SQL UPDATE
        pass
```

```typescript
// Portas
interface ServicoPagamento {
  processar(pedidoId: string, valor: number): Promise<boolean>;
}

interface RepositorioPedidos {
  atualizarStatus(pedidoId: string, status: string): Promise<void>;
}

// Núcleo
class ProcessadorPagamentos {
  constructor(
    private readonly pagamento: ServicoPagamento,
    private readonly pedidos: RepositorioPedidos,
  ) {}

  async executar(pedidoId: string, valor: number): Promise<boolean> {
    const processado = await this.pagamento.processar(pedidoId, valor);
    if (processado) {
      await this.pedidos.atualizarStatus(pedidoId, "pago");
      return true;
    }
    return false;
  }
}

// Adaptadores
class ServicoPagamentoStripe implements ServicoPagamento {
  async processar(pedidoId: string, valor: number): Promise<boolean> {
    return true;
  }
}

class RepositorioPedidosPostgres implements RepositorioPedidos {
  async atualizarStatus(pedidoId: string, status: string): Promise<void> {}
}
```

---

## 5. Arquitetura em Camadas (Layered Architecture)

A mais tradicional das arquiteturas, organiza o sistema em camadas horizontais onde cada uma só se comunica com a camada imediatamente abaixo.

```
+------------------------------+
|    Presentation Layer        |  (Controllers, Views, DTOs)
+------------------------------+
|    Application Layer         |  (Use Cases, Application Services)
+------------------------------+
|    Domain Layer              |  (Entities, Value Objects, Domain Services)
+------------------------------+
|    Infrastructure Layer      |  (Repositories, DB, External APIs)
+------------------------------+
```

### 5.1 Exemplo

```python
# Presentation Layer
class UsuarioController:
    def __init__(self, service: "UsuarioService"):
        self._service = service

    def criar(self, nome: str, email: str) -> dict:
        usuario = self._service.criar_usuario(nome, email)
        return {"id": usuario.id, "nome": usuario.nome, "email": usuario.email}

# Application Layer
class UsuarioService:
    def __init__(self, repo: "UsuarioRepository"):
        self._repo = repo

    def criar_usuario(self, nome: str, email: str) -> "Usuario":
        usuario = Usuario(id=str(uuid4()), nome=nome, email=email)
        self._repo.salvar(usuario)
        return usuario

# Domain Layer
@dataclass
class Usuario:
    id: str
    nome: str
    email: str

# Infrastructure Layer
class UsuarioRepository:
    def salvar(self, usuario: Usuario) -> None: ...
```

```typescript
// Presentation
class UsuarioController {
  constructor(private readonly service: UsuarioService) {}

  async criar(nome: string, email: string) {
    const usuario = await this.service.criarUsuario(nome, email);
    return { id: usuario.id, nome: usuario.nome, email: usuario.email };
  }
}

// Application
class UsuarioService {
  constructor(private readonly repo: UsuarioRepository) {}

  async criarUsuario(nome: string, email: string): Promise<Usuario> {
    const usuario: Usuario = { id: crypto.randomUUID(), nome, email };
    await this.repo.salvar(usuario);
    return usuario;
  }
}

// Domain
interface Usuario {
  id: string;
  nome: string;
  email: string;
}

// Infrastructure
class UsuarioRepository {
  async salvar(usuario: Usuario): Promise<void> {}
}
```

---

## 6. Microservices vs Monoliths

### Monólito

Todas as funcionalidades em um único processo/deploy.

```
+----------------------------+
|       Single Application    |
| +--------+ +--------+     |
| | Auth   | | Pagamento    | |
| +--------+ +--------+     |
| +--------+ +--------+     |
| | Pedidos| | Notificação  | |
| +--------+ +--------+     |
+----------------------------+
```

**Vantagens:** Simplicidade, deploy único, consistência transacional, baixa latência entre módulos.

**Desvantagens:** Escalabilidade limitada, acoplamento, deploy impacta tudo.

### Microservices

Cada funcionalidade é um serviço independente.

```
+--------+   +--------+   +--------+
| Auth   |   | Pedido |   | Pagto  |
| Service|   | Service|   | Service|
+--------+   +--------+   +--------+
     |            |            |
     +------------+------------+
             [API Gateway]
                  |
            [Cliente]
```

```python
# Microserviço de Pedidos
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

PEDIDOS = {}

@app.route("/pedidos", methods=["POST"])
def criar_pedido():
    dados = request.json
    pedido_id = str(uuid4())
    PEDIDOS[pedido_id] = {"id": pedido_id, **dados}

    # Comunicação com serviço de pagamento
    requests.post(
        "http://pagamento-service/processar",
        json={"pedido_id": pedido_id, "valor": dados["valor"]}
    )

    return jsonify(PEDIDOS[pedido_id]), 201

@app.route("/pedidos/<pedido_id>", methods=["GET"])
def obter_pedido(pedido_id: str):
    pedido = PEDIDOS.get(pedido_id)
    if not pedido:
        return jsonify({"erro": "Não encontrado"}), 404
    return jsonify(pedido)
```

```typescript
// Microserviço de Pedidos (Express)
import express from "express";
import { randomUUID } from "crypto";

const app = express();
app.use(express.json());

interface Pedido {
  id: string;
  clienteId: string;
  valor: number;
  status: string;
}

const pedidos = new Map<string, Pedido>();

app.post("/pedidos", (req, res) => {
  const pedido: Pedido = {
    id: randomUUID(),
    ...req.body,
    status: "criado",
  };
  pedidos.set(pedido.id, pedido);

  fetch("http://pagamento-service/processar", {
    method: "POST",
    body: JSON.stringify({ pedidoId: pedido.id, valor: pedido.valor }),
    headers: { "Content-Type": "application/json" },
  });

  res.status(201).json(pedido);
});

app.listen(3001);
```

---

## 7. Event-Driven Architecture (EDA)

O sistema reage a **eventos** — mensagens que representam fatos ocorridos. Componentes se comunicam via **barramento de eventos**, sem conhecimento direto entre si.

```
[Serviço A] --(evento)--> [Message Broker] --(evento)--> [Serviço B]
                                                          [Serviço C]
                                                          [Serviço D]
```

```python
from dataclasses import dataclass
from typing import Callable

@dataclass
class Evento:
    tipo: str
    dados: dict

class BarramentoEventos:
    def __init__(self):
        self._assinantes: dict[str, list[Callable]] = {}

    def assinar(self, tipo_evento: str, handler: Callable) -> None:
        if tipo_evento not in self._assinantes:
            self._assinantes[tipo_evento] = []
        self._assinantes[tipo_evento].append(handler)

    def publicar(self, evento: Evento) -> None:
        for handler in self._assinantes.get(evento.tipo, []):
            handler(evento)

# Uso
barramento = BarramentoEventos()

def enviar_email(evento: Evento):
    print(f"Email enviado para {evento.dados['email']}")

def atualizar_estoque(evento: Evento):
    print(f"Estoque atualizado para produto {evento.dados['produto_id']}")

barramento.assinar("pedido.criado", enviar_email)
barramento.assinar("pedido.criado", atualizar_estoque)

barramento.publicar(Evento("pedido.criado", {
    "email": "cliente@email.com",
    "produto_id": "123"
}))
```

```typescript
type Handler = (evento: Evento) => void;

interface Evento {
  tipo: string;
  dados: Record<string, unknown>;
}

class BarramentoEventos {
  private assinantes = new Map<string, Handler[]>();

  assinar(tipoEvento: string, handler: Handler): void {
    const handlers = this.assinantes.get(tipoEvento) ?? [];
    handlers.push(handler);
    this.assinantes.set(tipoEvento, handlers);
  }

  publicar(evento: Evento): void {
    const handlers = this.assinantes.get(evento.tipo) ?? [];
    for (const handler of handlers) {
      handler(evento);
    }
  }
}

const barramento = new BarramentoEventos();

barramento.assinar("pedido.criado", (evento) => {
  console.log(`Email enviado para ${evento.dados.email}`);
});

barramento.assinar("pedido.criado", (evento) => {
  console.log(`Estoque atualizado para ${evento.dados.produto_id}`);
});

barramento.publicar({
  tipo: "pedido.criado",
  dados: { email: "cliente@email.com", produto_id: "123" },
});
```

---

## 8. CQRS e Event Sourcing

### CQRS (Command Query Responsibility Segregation)

Separa **comandos** (escrita) de **consultas** (leitura), cada um com seu modelo e otimização.

```
 +---------+     +----------+     +---------+
 | Command  | --> | Write DB  | --> | Query   |
 | Handler  |     | (normal.)|     | Handler |
 +---------+     +----------+     +---------+
      |                                |
 [Event Bus] ---> [Read DB] <----------+
                  (desnorm.)
```

```python
from dataclasses import dataclass

# Command
@dataclass
class CriarPedido:
    cliente_id: str
    itens: list[dict]
    total: float

class CriarPedidoHandler:
    def __init__(self, event_store):
        self._event_store = event_store

    def handle(self, comando: CriarPedido) -> None:
        evento = PedidoCriado(
            pedido_id=str(uuid4()),
            cliente_id=comando.cliente_id,
            itens=comando.itens,
            total=comando.total
        )
        self._event_store.salvar(evento)

# Query
class ConsultaPedidos:
    def __init__(self, read_db):
        self._db = read_db

    def obter_resumo(self, cliente_id: str) -> list[dict]:
        return self._db.query(
            "SELECT * FROM pedidos_resumo WHERE cliente_id = ?",
            (cliente_id,)
        )
```

```typescript
// Command
interface CriarPedido {
  clienteId: string;
  itens: Array<{ produtoId: string; quantidade: number }>;
  total: number;
}

class CriarPedidoHandler {
  constructor(private readonly eventStore: EventStore) {}

  async handle(comando: CriarPedido): Promise<void> {
    const evento: PedidoCriado = {
      tipo: "pedido.criado",
      pedidoId: crypto.randomUUID(),
      clienteId: comando.clienteId,
      itens: comando.itens,
      total: comando.total,
    };
    await this.eventStore.salvar(evento);
  }
}

// Query
class ConsultaPedidos {
  constructor(private readonly db: Database) {}

  async obterResumo(clienteId: string): Promise<PedidoResumo[]> {
    return this.db.query(
      "SELECT * FROM pedidos_resumo WHERE cliente_id = $1",
      [clienteId]
    );
  }
}
```

### Event Sourcing

Em vez de armazenar o estado atual, armazena a **sequência de eventos** que levaram a ele. O estado atual é derivado por **replay** dos eventos.

```python
from dataclasses import dataclass, field
from typing import Protocol

@dataclass
class Evento:
    tipo: str
    dados: dict
    versao: int = 1

class EventStore:
    def __init__(self):
        self._eventos: dict[str, list[Evento]] = {}

    def salvar(self, aggregate_id: str, evento: Evento) -> None:
        if aggregate_id not in self._eventos:
            self._eventos[aggregate_id] = []
        self._eventos[aggregate_id].append(evento)

    def obter_eventos(self, aggregate_id: str) -> list[Evento]:
        return self._eventos.get(aggregate_id, [])

class Conta:
    def __init__(self):
        self._saldo = 0.0

    def aplicar_evento(self, evento: Evento) -> None:
        if evento.tipo == "deposito":
            self._saldo += evento.dados["valor"]
        elif evento.tipo == "saque":
            self._saldo -= evento.dados["valor"]

    def carregar(self, eventos: list[Evento]) -> None:
        for evento in eventos:
            self.aplicar_evento(evento)

    @property
    def saldo(self) -> float:
        return self._saldo

store = EventStore()
store.salvar("conta-1", Evento("deposito", {"valor": 1000}))
store.salvar("conta-1", Evento("saque", {"valor": 200}))

conta = Conta()
conta.carregar(store.obter_eventos("conta-1"))
print(conta.saldo)  # 800
```

```typescript
interface Evento {
  tipo: string;
  dados: Record<string, unknown>;
}

class EventStore {
  private eventos = new Map<string, Evento[]>();

  salvar(aggregateId: string, evento: Evento): void {
    const lista = this.eventos.get(aggregateId) ?? [];
    lista.push(evento);
    this.eventos.set(aggregateId, lista);
  }

  obterEventos(aggregateId: string): Evento[] {
    return this.eventos.get(aggregateId) ?? [];
  }
}

class Conta {
  private saldo = 0;

  aplicarEvento(evento: Evento): void {
    switch (evento.tipo) {
      case "deposito":
        this.saldo += evento.dados.valor as number;
        break;
      case "saque":
        this.saldo -= evento.dados.valor as number;
        break;
    }
  }

  carregar(eventos: Evento[]): void {
    for (const evento of eventos) {
      this.aplicarEvento(evento);
    }
  }

  getSaldo(): number {
    return this.saldo;
  }
}
```

---

## 9. Domain-Driven Design (DDD)

Abordagem de Eric Evans para lidar com **complexidade no coração do software**, focando no **domínio** e na **linguagem ubíqua**.

**Referência:** Evans, Eric. *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley, 2003.

### 9.1 Blocos de Construção do DDD

| Conceito | Descrição | Exemplo |
|---|---|---|
| **Entity** | Objeto com identidade única e contínua | `Usuario`, `Pedido` |
| **Value Object** | Objeto imutável definido por seus atributos | `Endereco`, `Dinheiro` |
| **Aggregate** | Conjunto de objetos tratados como unidade | `Pedido` + `ItemPedido` |
| **Aggregate Root** | A única entrada para um Aggregate | `Pedido` (contém `ItemPedido`) |
| **Domain Service** | Operação que não pertence a uma Entity/Value | `ServicoFrete` |
| **Repository** | Abstração de persistência para Aggregates | `RepositorioPedidos` |
| **Domain Event** | Algo que aconteceu no domínio | `PedidoConfirmado` |
| **Factory** | Criação de objetos complexos | `PedidoFactory` |
| **Bounded Context** | Limite explícito de um modelo | `Contexto de Vendas` |

```python
# Value Object (imutável)
@dataclass(frozen=True)
class Endereco:
    rua: str
    numero: str
    bairro: str
    cidade: str
    cep: str

# Entity
@dataclass
class Cliente:
    id: str
    nome: str
    endereco: Endereco  # Value Object

# Aggregate Root
@dataclass
class ItemPedido:
    produto_id: str
    quantidade: int
    preco_unitario: float

class Pedido:
    def __init__(self, id: str, cliente: Cliente):
        self._id = id
        self._cliente = cliente
        self._itens: list[ItemPedido] = []
        self._eventos: list[DomainEvent] = []

    def adicionar_item(self, produto_id: str, qtd: int, preco: float) -> None:
        item = ItemPedido(produto_id, qtd, preco)
        self._itens.append(item)
        self._eventos.append(ItemAdicionado(
            pedido_id=self._id,
            produto_id=produto_id
        ))

    def total(self) -> float:
        return sum(
            item.quantidade * item.preco_unitario
            for item in self._itens
        )

    def confirmar(self) -> None:
        if not self._itens:
            raise ValueError("Pedido vazio não pode ser confirmado")
        self._eventos.append(PedidoConfirmado(pedido_id=self._id))

    def obter_eventos(self) -> list:
        eventos = self._eventos[:]
        self._eventos.clear()
        return eventos
```

```typescript
// Value Object
class Endereco {
  constructor(
    readonly rua: string,
    readonly numero: string,
    readonly bairro: string,
    readonly cidade: string,
    readonly cep: string,
  ) {}
}

// Entity
interface Cliente {
  id: string;
  nome: string;
  endereco: Endereco;
}

// Aggregate Root
class Pedido {
  private _itens: Array<{ produtoId: string; quantidade: number; precoUnitario: number }> = [];
  private _eventos: DomainEvent[] = [];

  constructor(
    readonly id: string,
    readonly cliente: Cliente,
  ) {}

  adicionarItem(produtoId: string, quantidade: number, precoUnitario: number): void {
    this._itens.push({ produtoId, quantidade, precoUnitario });
    this._eventos.push(new ItemAdicionado(this.id, produtoId));
  }

  total(): number {
    return this._itens.reduce(
      (acc, item) => acc + item.quantidade * item.precoUnitario,
      0,
    );
  }

  confirmar(): void {
    if (this._itens.length === 0) {
      throw new Error("Pedido vazio não pode ser confirmado");
    }
    this._eventos.push(new PedidoConfirmado(this.id));
  }

  obterEventos(): DomainEvent[] {
    const eventos = [...this._eventos];
    this._eventos = [];
    return eventos;
  }
}
```

### 9.2 Bounded Context

Cada contexto limitado tem seu próprio modelo, linguagem e equipe.

```
+-------------------+    +--------------------+
| Contexto de Vendas |    | Contexto de Estoque |
|                   |    |                    |
| Cliente           |    | Cliente (diferente)|
| Pedido            |    | Produto            |
| Produto           |    | Localizacao        |
+--------+----------+    +---------+----------+
         |                         |
         +-----[Anti-Corruption Layer]-----+
```

---

## 10. Architecture Decision Records (ADR)

Documento que registra decisões arquiteturais importantes e seu contexto. Cada ADR contém:

- **Título:** Número e título da decisão
- **Status:** Proposto, Aceito, Depreciado, Substituído
- **Contexto:** Por que a decisão foi necessária
- **Decisão:** O que foi decidido
- **Consequências:** Impactos positivos e negativos

```markdown
# ADR-001: Uso de PostgreSQL como Banco Principal

**Status:** Aceito

**Contexto:**
Precisamos de um banco de dados relacional com suporte a transações ACID,
dados geoespaciais e boa escalabilidade horizontal.

**Decisão:**
Utilizaremos PostgreSQL 15 como banco de dados principal, aproveitando:
- Extensão PostGIS para dados geoespaciais
- Replicação nativa para alta disponibilidade
- Particionamento de tabelas para performance

**Consequências:**
Positivas:
- Maturidade e comunidade ativa
- Zero custo de licenciamento
- Funcionalidades avançadas (CTE, window functions)

Negativas:
- Complexidade operacional maior que SQLite
- Consumo de memória para datasets grandes
```

### Template de ADR

```markdown
# ADR-NNN: [Título Descritivo]

**Status:** [Proposto | Aceito | Depreciado | Substituído]
**Data:** YYYY-MM-DD
**Autor:** [Nome]

## Contexto
[Descreva o problema e forças atuantes]

## Decisão
[Descreva a decisão tomada]

## Alternativas Consideradas
1. Alternativa A - [Por que não foi escolhida]
2. Alternativa B - [Por que não foi escolhida]

## Consequências
Positivas:
- [Lista]

Negativas:
- [Lista]

## Compliance
[Como verificar se a decisão está sendo seguida]
```

---

## 11. Perspectiva Comparativa de Arquiteturas

| Aspecto | Clean Arch | Hexagonal | Camadas | Microservices | EDA |
|---|---|---|---|---|---|
| **Acoplamento** | Baixo | Baixo | Médio | Baixo | Muito baixo |
| **Testabilidade** | Alta | Alta | Média | Alta | Média |
| **Complexidade** | Alta | Alta | Baixa | Muito alta | Alta |
| **Deploy** | Monolítico | Monolítico | Monolítico | Independente | Independente |
| **Escalabilidade** | Vertical | Vertical | Vertical | Horizontal | Horizontal |
| **Consistência** | Forte | Forte | Forte | Eventual | Eventual |
| **适合时间** | Sistemas complexos | Sistemas com I/O variado | CRUD simples | Sistemas grandes | Fluxos assíncronos |

---

## 12. Anti-Patterns Arquiteturais

### Big Ball of Mud (Grande Bola de Lama)

Sistema sem estrutura clara, com dependências emaranhadas. Sintomas:
- Mudança em um lugar quebra em lugares inesperados
- Ninguém sabe onde colocar código novo
- Testes são impossíveis de escrever

### Golden Hammer (Martelo de Ouro)

Usar a mesma solução para todos os problemas. Ex: fazer microsserviços para um CRUD de 2 tabelas.

### Architecture by Implication

Presumir que a arquitetura usada no último projeto serve para o atual.

### Inner Platform Effect

Recriar a plataforma subjacente (ex: reimplementar um banco de dados em memória com objetos).

### Vendor Lock-in

Dependência excessiva de um fornecedor específico, impossibilitando migração.

---

## 13. Referências Bibliográficas

- Martin, R. C. *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall, 2017.
- Martin, R. C. *Agile Software Development, Principles, Patterns, and Practices*. Prentice Hall, 2002.
- Evans, E. *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley, 2003.
- Gamma, E.; Helm, R.; Johnson, R.; Vlissides, J. *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley, 1994.
- Vernon, V. *Implementing Domain-Driven Design*. Addison-Wesley, 2013.
- Newman, S. *Building Microservices*. O'Reilly, 2015.
- Fowler, M. *Patterns of Enterprise Application Architecture*. Addison-Wesley, 2002.
- Cockburn, A. *Hexagonal Architecture (Ports and Adapters)*. alistair.cockburn.us, 2005.
- Hohpe, G.; Woolf, B. *Enterprise Integration Patterns*. Addison-Wesley, 2003.

## Ver Também

- [[04-Conhecimentos/07-Humanidades/Programacao/Design-Patterns]]
- [[04-Conhecimentos/07-Humanidades/Programacao/Paradigmas-de-Programacao]]
- [[04-Conhecimentos/07-Humanidades/Programacao/APIs-e-Integracoes]]
- [[05-Skills/02-software-engineering/advanced-backend-architecture]]
