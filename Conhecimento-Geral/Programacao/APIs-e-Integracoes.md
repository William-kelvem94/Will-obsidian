---
title: "APIs e Integrações"
date: 2026-05-16
area: "Programação e Engenharia de Software"
tags: [conhecimento, programacao, api, rest, graphql, grpc, webhooks]
related: ["Conhecimento-Geral/Programacao/Arquitetura-de-Software"]
aliases: ["API Design", "REST", "GraphQL", "gRPC"]
---

# APIs e Integrações

APIs (Application Programming Interfaces) são contratos que permitem que diferentes sistemas se comuniquem. Este documento cobre os principais estilos de API, protocolos de integração e boas práticas.

**Referência:** Fielding, Roy T. *Architectural Styles and the Design of Network-based Software Architectures*. PhD Dissertation, UC Irvine, 2000. (REST)

---

## 1. REST (Representational State Transfer)

Estilo arquitetural definido por Roy Fielding em sua tese de doutorado. REST não é um protocolo ou formato, mas um conjunto de **restrições arquiteturais**.
---
title: "APIs e Integrações"
date: 2026-05-16
area: "Programação e Engenharia de Software"
tags: [conhecimento, programacao, api, rest, graphql, grpc, webhooks]
related: ["Conhecimento-Geral/Programacao/Arquitetura-de-Software"]
aliases: ["API Design", "REST", "GraphQL", "gRPC"]
---

# APIs e Integrações
## 1. REST (Representational State Transfer)

Estilo arquitetural definido por Roy Fielding em sua tese de doutorado. REST nao e um protocolo ou formato, mas um conjunto de restricoes arquiteturais.

### 1.1 Principios REST

1. Stateless: Cada requisicao contem toda informacao necessaria
2. Cacheable: Respostas devem ser marcadas como cacheaveis ou nao
3. Uniform Interface: Recursos identificados por URIs
4. Layered System: Cliente nao precisa saber se esta falando com o servidor final ou intermediario
5. Code on Demand (opcional): Servidor pode estender funcionalidade do cliente

### 1.2 Recursos e Metodos HTTP

| Metodo | CRUD | Idempotente | Seguro |
|---|---|---|---|
| GET | Read | Sim | Sim |
| POST | Create | Nao | Nao |
| PUT | Update/Replace | Sim | Nao |
| PATCH | Partial Update | Nao | Nao |
| DELETE | Delete | Sim | Nao |
---
title: "APIs e Integracoes"
date: 2026-05-16
area: "Programacao e Engenharia de Software"
tags: [conhecimento, programacao, api, rest, graphql, grpc, webhooks]
related: ["Conhecimento-Geral/Programacao/Arquitetura-de-Software"]
aliases: ["API Design", "REST", "GraphQL", "gRPC"]
---

# APIs e Integracoes

APIs (Application Programming Interfaces) sao contratos que permitem que diferentes sistemas se comuniquem. Este documento cobre os principais estilos de API, protocolos de integracao e boas praticas.

**Referencia:** Fielding, Roy T. *Architectural Styles and the Design of Network-based Software Architectures*. PhD Dissertation, UC Irvine, 2000. (REST)

---

## 1. REST (Representational State Transfer)

Estilo arquitetural definido por Roy Fielding em sua tese de doutorado. REST nao e um protocolo ou formato, mas um conjunto de **restricoes arquiteturais**.

### 1.1 Principios REST

1. **Stateless:** Cada requisicao contem toda informacao necessaria
2. **Cacheable:** Respostas devem ser marcadas como cacheaveis ou nao
3. **Uniform Interface:** Recursos identificados por URIs
4. **Layered System:** Cliente nao precisa saber se esta falando com o servidor final ou intermediario
5. **Code on Demand (opcional):** Servidor pode estender funcionalidade do cliente

### 1.2 Recursos e Metodos HTTP

| Metodo | CRUD | Idempotente | Seguro |
|---|---|---|---|
| GET | Read | Sim | Sim |
| POST | Create | Nao | Nao |
| PUT | Update/Replace | Sim | Nao |
| PATCH | Partial Update | Nao | Nao |
| DELETE | Delete | Sim | Nao |


### 1.3 Status Codes HTTP

Cada metodo tem status codes esperados:

| Codigo | Significado | Uso |
|---|---|---|---|
| 200 | OK | GET, PUT, PATCH bem-sucedidos |
| 201 | Created | POST bem-sucedido |
| 204 | No Content | DELETE bem-sucedido |
| 400 | Bad Request | Dados invalidos na requisicao |
| 401 | Unauthorized | Autenticacao necessaria |
| 403 | Forbidden | Sem permissao |
| 404 | Not Found | Recurso inexistente |
| 409 | Conflict | Conflito (ex: duplicata) |
| 422 | Unprocessable Entity | Validacao de negocios |
| 429 | Too Many Requests | Rate limit excedido |
| 500 | Internal Server Error | Erro inesperado no servidor |
### 1.3 Status Codes HTTP

Cada metodo tem status codes esperados:

| Codigo | Significado | Uso |
|---|---|---|
| 200 | OK | GET, PUT, PATCH bem-sucedidos |
| 201 | Created | POST bem-sucedido |
| 204 | No Content | DELETE bem-sucedido |
| 400 | Bad Request | Dados invalidos na requisicao |
| 401 | Unauthorized | Autenticacao necessaria |
| 403 | Forbidden | Sem permissao |
| 404 | Not Found | Recurso inexistente |
| 409 | Conflict | Conflito (ex: duplicata) |
| 422 | Unprocessable Entity | Validacao de negocios |
| 429 | Too Many Requests | Rate limit excedido |
| 500 | Internal Server Error | Erro inesperado no servidor |

### 1.4 Versionamento de API

```python
@app.route("/api/v1/usuarios")
def listar_v1():
    return jsonify([{"id": u.id, "nome": u.nome} for u in USUARIOS.values()])

@app.route("/api/v2/usuarios")
def listar_v2():
    return jsonify([
        {"id": u.id, "nome": u.nome, "email": u.email}
        for u in USUARIOS.values()
    ])

@app.route("/api/usuarios")
def listar_por_versao():
    version = request.headers.get("Accept-Version", "1")
    if version == "2":
        return listar_v2()
    return listar_v1()
```
```python
from flask import Flask, jsonify, request, abort
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class Usuario:
    id: int
    nome: str
    email: str

USUARIOS: dict[int, Usuario] = {}
proximo_id = 1

@app.route("/api/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify([u.__dict__ for u in USUARIOS.values()])

@app.route("/api/usuarios/<int:usuario_id>", methods=["GET"])
def obter_usuario(usuario_id: int):
    usuario = USUARIOS.get(usuario_id)
    if not usuario:
        abort(404, "Usuario nao encontrado")
    return jsonify(usuario.__dict__)

@app.route("/api/usuarios", methods=["POST"])
def criar_usuario():
    global proximo_id
    dados = request.get_json()
    if not dados or "nome" not in dados or "email" not in dados:
        abort(400, "Nome e email obrigatorios")
    usuario = Usuario(id=proximo_id, nome=dados["nome"], email=dados["email"])
    USUARIOS[proximo_id] = usuario
    proximo_id += 1
    return jsonify(usuario.__dict__), 201

@app.route("/api/usuarios/<int:usuario_id>", methods=["PUT"])
def atualizar_usuario(usuario_id: int):
    dados = request.get_json()
    usuario = USUARIOS.get(usuario_id)
    if not usuario:
        abort(404)
    usuario.nome = dados.get("nome", usuario.nome)
    usuario.email = dados.get("email", usuario.email)
    return jsonify(usuario.__dict__)

@app.route("/api/usuarios/<int:usuario_id>", methods=["DELETE"])
def deletar_usuario(usuario_id: int):
    if usuario_id not in USUARIOS:
        abort(404)
    del USUARIOS[usuario_id]
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
```

```typescript
import express, { Request, Response } from "express";

interface Usuario {
  id: number;
  nome: string;
  email: string;
}

const app = express();
app.use(express.json());

const usuarios = new Map<number, Usuario>();
let proximoId = 1;

app.get("/api/usuarios", (_req: Request, res: Response) => {
  res.json(Array.from(usuarios.values()));
});

app.get("/api/usuarios/:id", (req: Request, res: Response) => {
  const usuario = usuarios.get(Number(req.params.id));
  if (!usuario) return res.status(404).json({ erro: "Nao encontrado" });
  res.json(usuario);
});

app.post("/api/usuarios", (req: Request, res: Response) => {
  const { nome, email } = req.body;
  if (!nome || !email) {
    return res.status(400).json({ erro: "Nome e email obrigatorios" });
  }
  const usuario: Usuario = { id: proximoId++, nome, email };
  usuarios.set(usuario.id, usuario);
  res.status(201).json(usuario);
});

app.put("/api/usuarios/:id", (req: Request, res: Response) => {
  const usuario = usuarios.get(Number(req.params.id));
  if (!usuario) return res.status(404).json({ erro: "Nao encontrado" });
  usuario.nome = req.body.nome ?? usuario.nome;
  usuario.email = req.body.email ?? usuario.email;
  res.json(usuario);
});

app.delete("/api/usuarios/:id", (req: Request, res: Response) => {
  const id = Number(req.params.id);
  if (!usuarios.has(id)) return res.status(404).json({ erro: "Nao encontrado" });
  usuarios.delete(id);
  res.status(204).send();
});
```
### 1.5 HATEOAS (Hypermedia as the Engine of Application State)

Respostas incluem links para navegacao da API, permitindo descoberta.

```python
@app.route("/api/usuarios/<int:usuario_id>")
def obter_usuario_hateoas(usuario_id: int):
    usuario = USUARIOS.get(usuario_id)
    if not usuario:
        abort(404)
    return jsonify({
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "_links": {
            "self": {"href": f"/api/usuarios/{usuario.id}"},
            "pedidos": {"href": f"/api/usuarios/{usuario.id}/pedidos"},
            "update": {"href": f"/api/usuarios/{usuario.id}", "method": "PUT"},
            "delete": {"href": f"/api/usuarios/{usuario.id}", "method": "DELETE"},
        }
    })
```

### 1.6 Paginacao

```python
@app.route("/api/usuarios")
def listar_paginado():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    total = len(USUARIOS)
    total_pages = (total + per_page - 1) // per_page
    start = (page - 1) * per_page
    end = start + per_page
    items = list(USUARIOS.values())[start:end]
    return jsonify({
        "data": [u.__dict__ for u in items],
        "pagination": {
            "page": page,
            "per_page": per_page,
            "total": total,
            "total_pages": total_pages,
            "links": {
                "first": f"/api/usuarios?page=1&per_page={per_page}",
                "prev": f"/api/usuarios?page={page-1}&per_page={per_page}" if page > 1 else None,
                "next": f"/api/usuarios?page={page+1}&per_page={per_page}" if page < total_pages else None,
                "last": f"/api/usuarios?page={total_pages}&per_page={per_page}",
            }
        }
    })
```

```typescript
app.get("/api/usuarios", (req: Request, res: Response) => {
  const page = Number(req.query.page) || 1;
  const perPage = Number(req.query.per_page) || 10;
  const items = Array.from(usuarios.values());
  const total = items.length;
  const totalPages = Math.ceil(total / perPage);
  const start = (page - 1) * perPage;
  const end = start + perPage;
  res.json({
    data: items.slice(start, end),
    pagination: {
      page, per_page: perPage, total, total_pages: totalPages,
      links: {
        first: `/api/usuarios?page=1&per_page=${perPage}`,
        prev: page > 1 ? `/api/usuarios?page=${page-1}&per_page=${perPage}` : null,
        next: page < totalPages ? `/api/usuarios?page=${page+1}&per_page=${perPage}` : null,
        last: `/api/usuarios?page=${totalPages}&per_page=${perPage}`,
      },
    },
  });
});
```

---

## 2. GraphQL

Linguagem de consulta para APIs desenvolvida pelo Facebook (2015). Permite que o cliente solicite exatamente os dados que precisa.

**Referencia:** GraphQL Specification (graphql.org)

### 2.1 Schema e Types

```graphql
type Usuario {
  id: ID!
  nome: String!
  email: String!
  pedidos: [Pedido!]!
}

type Pedido {
  id: ID!
  total: Float!
  data: String!
  status: StatusPedido!
}

enum StatusPedido {
  PENDENTE
  CONFIRMADO
  ENVIADO
  ENTREGUE
}

type Query {
  usuario(id: ID!): Usuario
  usuarios: [Usuario!]!
  pedidos(usuarioId: ID!): [Pedido!]!
}

type Mutation {
  criarUsuario(nome: String!, email: String!): Usuario!
  criarPedido(usuarioId: ID!, total: Float!): Pedido!
}

type Subscription {
  pedidoCriado: Pedido!
}
```

### 2.2 Resolvers

```python
import strawberry
from typing import Optional

@strawberry.type
class Usuario:
    id: strawberry.ID
    nome: str
    email: str

@strawberry.type
class Pedido:
    id: strawberry.ID
    total: float
    status: str

@strawberry.type
class Query:
    @strawberry.field
    def usuario(self, id: strawberry.ID) -> Optional[Usuario]:
        return USUARIOS_DB.get(str(id))

    @strawberry.field
    def usuarios(self) -> list[Usuario]:
        return list(USUARIOS_DB.values())

    @strawberry.field
    def pedidos(self, usuario_id: strawberry.ID) -> list[Pedido]:
        return PEDIDOS_DB.get(str(usuario_id), [])

@strawberry.type
class Mutation:
    @strawberry.mutation
    def criar_usuario(self, nome: str, email: str) -> Usuario:
        usuario = Usuario(id=strawberry.ID(str(uuid4())), nome=nome, email=email)
        USUARIOS_DB[str(usuario.id)] = usuario
        return usuario

schema = strawberry.Schema(query=Query, mutation=Mutation)
```
```typescript
import { ApolloServer, gql } from "apollo-server";

const typeDefs = gql`
  type Usuario {
    id: ID!
    nome: String!
    email: String!
    pedidos: [Pedido!]!
  }

  type Pedido {
    id: ID!
    total: Float!
    status: String!
  }

  type Query {
    usuario(id: ID!): Usuario
    usuarios: [Usuario!]!
  }

  type Mutation {
    criarUsuario(nome: String!, email: String!): Usuario!
  }

  type Subscription {
    pedidoCriado: Pedido!
  }
`;

interface Usuario {
  id: string;
  nome: string;
  email: string;
}

const usuariosDB = new Map<string, Usuario>();

const resolvers = {
  Query: {
    usuario: (_: unknown, { id }: { id: string }) => usuariosDB.get(id) ?? null,
    usuarios: () => Array.from(usuariosDB.values()),
  },
  Mutation: {
    criarUsuario: (_: unknown, { nome, email }: { nome: string; email: string }) => {
      const usuario: Usuario = { id: String(usuariosDB.size + 1), nome, email };
      usuariosDB.set(usuario.id, usuario);
      return usuario;
    },
  },
  Usuario: {
    pedidos: (parent: Usuario) => [],
  },
};

const server = new ApolloServer({ typeDefs, resolvers });
server.listen().then(({ url }) => console.log(`Server ready at ${url}`));
```

### 2.3 N+1 Problem

Problema onde uma consulta GraphQL dispara N+1 queries ao banco de dados. Solucao: DataLoader (batching + caching).

```python
from dataloader import DataLoader

class PedidosLoader(DataLoader):
    def batch_load(self, usuario_ids: list[str]) -> list[list[Pedido]]:
        resultados = db.query(
            "SELECT * FROM pedidos WHERE usuario_id IN (?)",
            (usuario_ids,)
        )
        by_user: dict[str, list[Pedido]] = {}
        for p in resultados:
            by_user.setdefault(str(p.usuario_id), []).append(p)
        return [by_user.get(uid, []) for uid in usuario_ids]

loader = PedidosLoader()

@strawberry.type
class Usuario:
    @strawberry.field
    async def pedidos(self) -> list[Pedido]:
        return await loader.load(self.id)
```

```typescript
import DataLoader from "dataloader";

const pedidosLoader = new DataLoader(async (usuarioIds: readonly string[]) => {
  const pedidos = await db.query(
    "SELECT * FROM pedidos WHERE usuario_id = ANY($1)",
    [usuarioIds]
  );
  const byUser = new Map<string, Pedido[]>();
  for (const p of pedidos) {
    const list = byUser.get(p.usuario_id) ?? [];
    list.push(p);
    byUser.set(p.usuario_id, list);
  }
  return usuarioIds.map(id => byUser.get(id) ?? []);
});

const resolvers = {
  Usuario: {
    pedidos: (parent: Usuario) => pedidosLoader.load(parent.id),
  },
};
```

### 2.4 GraphQL vs REST

| Aspecto | REST | GraphQL |
|---|---|---|
| Over-fetching | Comum (retorna dados extras) | Nunca |
| Under-fetching | Comum (precisa multiplas requests) | Nunca |
| Versionamento | URL ou headers | Evolucao do schema |
| Cache | Nativo (HTTP caching) | Requer configuracao |
| Complexidade | Baixa a media | Media a alta |
| Tooling | Maduro (Postman, cURL) | Playground, Apollo DevTools |
| Upload arquivos | Nativo | Requer extensao (multipart) |

---

## 3. gRPC

Framework de RPC (Remote Procedure Call) desenvolvido pelo Google, usando Protocol Buffers como linguagem de definicao de interface e serializacao.

**Referencia:** gRPC Documentation (grpc.io)

### 3.1 Protocol Buffers (Protobuf)

```protobuf
syntax = "proto3";

package usuarios;

service UsuarioService {
  rpc GetUsuario (GetUsuarioRequest) returns (Usuario);
  rpc ListUsuarios (ListUsuariosRequest) returns (ListUsuariosResponse);
  rpc CriarUsuario (CriarUsuarioRequest) returns (Usuario);
  rpc AtualizarUsuarioStream (stream AtualizaRequest) returns (stream Usuario);
}

message Usuario {
  string id = 1;
  string nome = 2;
  string email = 3;
  int32 idade = 4;
}

message GetUsuarioRequest {
  string id = 1;
}

message ListUsuariosRequest {
  int32 page = 1;
  int32 per_page = 2;
}

message ListUsuariosResponse {
  repeated Usuario usuarios = 1;
  int32 total = 2;
}

message CriarUsuarioRequest {
  string nome = 1;
  string email = 2;
  int32 idade = 3;
}

message AtualizaRequest {
  string id = 1;
  optional string nome = 2;
  optional string email = 3;
}
```

### 3.2 Tipos de Streaming

gRPC oferece 4 tipos de comunicacao:

- **Unary:** Cliente envia 1 request, servidor responde 1 response
- **Server Streaming:** Cliente envia 1 request, servidor responde varios responses
- **Client Streaming:** Cliente envia varios requests, servidor responde 1 response
- **Bidirectional Streaming:** Ambos enviam multiplas mensagens

```python
import grpc
from concurrent import futures
import usuarios_pb2
import usuarios_pb2_grpc

class UsuarioServicer(usuarios_pb2_grpc.UsuarioServiceServicer):
    def GetUsuario(self, request, context):
        usuario = USUARIOS_DB.get(request.id)
        if not usuario:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Usuario nao encontrado")
            return usuarios_pb2.Usuario()
        return usuarios_pb2.Usuario(id=usuario.id, nome=usuario.nome, email=usuario.email)

    def ListUsuarios(self, request, context):
        usuarios = list(USUARIOS_DB.values())
        start = (request.page - 1) * request.per_page
        end = start + request.per_page
        return usuarios_pb2.ListUsuariosResponse(
            usuarios=usuarios[start:end],
            total=len(usuarios)
        )

    def AtualizarUsuarioStream(self, request_iterator, context):
        for req in request_iterator:
            usuario = USUARIOS_DB.get(req.id)
            if usuario:
                if req.HasField("nome"):
                    usuario.nome = req.nome
                if req.HasField("email"):
                    usuario.email = req.email
                yield usuarios_pb2.Usuario(id=usuario.id, nome=usuario.nome, email=usuario.email)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
usuarios_pb2_grpc.add_UsuarioServiceServicer_to_server(UsuarioServicer(), server)
server.add_insecure_port("[::]:50051")
server.start()
server.wait_for_termination()
```
```typescript
import grpc from "@grpc/grpc-js";
import protoLoader from "@grpc/proto-loader";

const packageDef = protoLoader.loadSync("usuarios.proto", {});
const grpcObj = grpc.loadPackageDefinition(packageDef);

function getUsuario(
  call: grpc.ServerUnaryCall<any, any>,
  callback: grpc.sendUnaryData<any>
) {
  const usuario = usuariosDB.get(call.request.id);
  if (!usuario) {
    return callback({
      code: grpc.status.NOT_FOUND,
      details: "Nao encontrado",
    });
  }
  callback(null, usuario);
}

function atualizarUsuarioStream(call: grpc.ServerDuplexStream<any, any>) {
  call.on("data", (req: any) => {
    const usuario = usuariosDB.get(req.id);
    if (usuario) {
      if (req.nome) usuario.nome = req.nome;
      if (req.email) usuario.email = req.email;
      call.write(usuario);
    }
  });
  call.on("end", () => call.end());
}

const server = new grpc.Server();
server.addService(UsuarioService, {
  GetUsuario: getUsuario,
  AtualizarUsuarioStream: atualizarUsuarioStream,
});
server.bindAsync(
  "0.0.0.0:50051",
  grpc.ServerCredentials.createInsecure(),
  () => server.start()
);
```

---

## 4. Webhooks

Mecanismo de comunicacao **assincrono** onde um sistema envia dados automaticamente para uma URL pre-configurada quando um evento ocorre. Diferente de APIs tradicionais (polling), webhooks sao push-based.

```
[Servico A] ----(POST HTTP)----> [Servico B]
  (evento ocorre)                  (URL configurada)
```

### 4.1 Implementacao

```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
WEBHOOKS: list[dict] = []

@app.route("/webhooks/register", methods=["POST"])
def registrar_webhook():
    dados = request.get_json()
    WEBHOOKS.append({
        "url": dados["url"],
        "eventos": dados.get("eventos", ["*"]),
        "secret": dados.get("secret", ""),
    })
    return jsonify({"status": "registrado"}), 201

def disparar_evento(tipo: str, dados: dict) -> None:
    payload = {
        "evento": tipo,
        "timestamp": "2026-05-16T10:00:00Z",
        "dados": dados,
    }
    for wh in WEBHOOKS:
        if tipo in wh["eventos"] or "*" in wh["eventos"]:
            try:
                headers = {
                    "Content-Type": "application/json",
                    "X-Webhook-Signature": gerar_assinatura(payload, wh["secret"]),
                }
                requests.post(wh["url"], json=payload, headers=headers, timeout=10)
            except requests.RequestException as e:
                print(f"Falha ao enviar webhook: {e}")

@app.route("/api/pedidos", methods=["POST"])
def criar_pedido():
    dados = request.get_json()
    pedido = {"id": str(uuid4()), **dados}
    disparar_evento("pedido.criado", pedido)
    return jsonify(pedido), 201
```
```typescript
import express from "express";
import crypto from "crypto";

const app = express();
app.use(express.json());

interface WebhookRegistro {
  url: string;
  eventos: string[];
  secret: string;
}

const webhooks: WebhookRegistro[] = [];

app.post("/webhooks/register", (req, res) => {
  webhooks.push({
    url: req.body.url,
    eventos: req.body.eventos ?? ["*"],
    secret: req.body.secret ?? "",
  });
  res.status(201).json({ status: "registrado" });
});

function dispararEvento(tipo: string, dados: Record<string, unknown>): void {
  const payload = { evento: tipo, timestamp: new Date().toISOString(), dados };
  for (const wh of webhooks) {
    if (wh.eventos.includes(tipo) || wh.eventos.includes("*")) {
      const assinatura = crypto
        .createHmac("sha256", wh.secret)
        .update(JSON.stringify(payload))
        .digest("hex");
      fetch(wh.url, {
        method: "POST",
        body: JSON.stringify(payload),
        headers: {
          "Content-Type": "application/json",
          "X-Webhook-Signature": assinatura,
        },
      }).catch(err => console.error(`Falha webhook ${wh.url}:`, err));
    }
  }
}
```

### 4.2 Retry e Idempotencia

```python
import time
from dataclasses import dataclass

@dataclass
class TentativaWebhook:
    url: str
    payload: dict
    tentativas: int = 0
    max_tentativas: int = 3

def processar_fila_webhook(fila: list[TentativaWebhook]) -> None:
    for item in fila[:]:
        try:
            resp = requests.post(item.url, json=item.payload, timeout=10)
            if resp.status_code == 200:
                fila.remove(item)
        except requests.RequestException:
            item.tentativas += 1
            if item.tentativas >= item.max_tentativas:
                fila.remove(item)
                print(f"Falha definitiva: {item.url}")
            else:
                time.sleep(2 ** item.tentativas)

@app.route("/webhooks/receive", methods=["POST"])
def receber_webhook():
    event_id = request.headers.get("X-Event-ID")
    if event_id in EVENTOS_PROCESSADOS:
        return jsonify({"status": "ja processado"}), 200
    dados = request.get_json()
    processar_evento(dados)
    EVENTOS_PROCESSADOS.add(event_id)
    return jsonify({"status": "ok"}), 200
```

---

## 5. Autenticacao e Autorizacao

### 5.1 API Keys

Chave simples enviada via header ou query parameter.

```python
API_KEYS = {"sk-abc123": {"cliente": "Acme Corp", "taxa": 100}}

def validar_api_key(request):
    api_key = request.headers.get("X-API-Key") or request.args.get("api_key")
    if not api_key or api_key not in API_KEYS:
        abort(401, "API Key invalida")
    return API_KEYS[api_key]
```

```typescript
const API_KEYS = new Map([
  ["sk-abc123", { cliente: "Acme Corp", taxa: 100 }],
]);

function validarApiKey(req: express.Request): void {
  const key = (req.headers["x-api-key"] as string) || (req.query.api_key as string);
  if (!key || !API_KEYS.has(key)) {
    throw new Error("API Key invalida");
  }
}
```

### 5.2 JWT (JSON Web Tokens)

Token autocontido com claims assinadas digitalmente.

```python
import jwt
from datetime import datetime, timedelta

SECRET = "minha-chave-secreta"

def gerar_token(usuario_id: str, role: str) -> str:
    payload = {
        "sub": usuario_id,
        "role": role,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(hours=1),
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def validar_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise PermissionError("Token expirado")
    except jwt.InvalidTokenError:
        raise PermissionError("Token invalido")

@app.route("/login", methods=["POST"])
def login():
    dados = request.get_json()
    if dados["usuario"] == "admin" and dados["senha"] == "123":
        token = gerar_token("user-1", "admin")
        return jsonify({"token": token})
    abort(401)
```
```typescript
import jwt from "jsonwebtoken";

const SECRET = "minha-chave-secreta";

function gerarToken(usuarioId: string, role: string): string {
  return jwt.sign(
    { sub: usuarioId, role },
    SECRET,
    { expiresIn: "1h" }
  );
}

function validarToken(token: string): jwt.JwtPayload {
  return jwt.verify(token, SECRET) as jwt.JwtPayload;
}

app.post("/login", (req, res) => {
  if (req.body.usuario === "admin" && req.body.senha === "123") {
    const token = gerarToken("user-1", "admin");
    res.json({ token });
  } else {
    res.status(401).json({ erro: "Credenciais invalidas" });
  }
});

function authMiddleware(req: express.Request, res: express.Response, next: express.NextFunction): void {
  const auth = req.headers.authorization;
  if (!auth || !auth.startsWith("Bearer ")) {
    res.status(401).json({ erro: "Token nao fornecido" });
    return;
  }
  try {
    const payload = validarToken(auth.slice(7));
    (req as any).usuario = payload;
    next();
  } catch {
    res.status(401).json({ erro: "Token invalido" });
  }
}
```

### 5.3 OAuth 2.0 e OpenID Connect

Fluxos principais do OAuth 2.0:

**Authorization Code Flow (Recomendado para apps web)**

```
[Cliente] -> (1) Auth Request -> [Authorization Server]
[Cliente] <- (2) Auth Code ----- [Authorization Server]
[Cliente] -> (3) Code + Secret -> [Authorization Server]
[Cliente] <- (4) Access Token --- [Authorization Server]
[Cliente] -> (5) Token ---------> [Resource Server]
[Cliente] <- (6) Protected Data - [Resource Server]
```

```python
import requests

def obter_token_client_credentials(client_id: str, client_secret: str, scope: str) -> str:
    resp = requests.post("https://auth.exemplo.com/token", data={
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": scope,
    })
    return resp.json()["access_token"]

def trocar_code_por_token(code: str, client_id: str, client_secret: str, redirect_uri: str) -> dict:
    resp = requests.post("https://auth.exemplo.com/token", data={
        "grant_type": "authorization_code",
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
    })
    return resp.json()
```

```typescript
interface TokenResponse {
  access_token: string;
  refresh_token?: string;
  id_token?: string;
  expires_in: number;
}

async function obterTokenClientCredentials(
  clientId: string, clientSecret: string, scope: string
): Promise<TokenResponse> {
  const resp = await fetch("https://auth.exemplo.com/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      grant_type: "client_credentials",
      client_id: clientId,
      client_secret: clientSecret,
      scope,
    }),
  });
  return resp.json();
}
```

### 5.4 Comparacao de Metodos

| Metodo | Estado | Expira | Revogacao | Uso Tipico |
|---|---|---|---|---|
| API Key | Stateless | Nao (ou longa) | Manual | Servico a servico |
| JWT | Stateless | Sim (curta) | Lista negra (complexo) | Sessoes de usuario |
| OAuth2 Token | Stateless | Sim (curta) | Refresh rotation | Delegacao de acesso |
| Session Cookie | Stateful | Sim | Imediata | Apps web tradicionais |
| Basic Auth | Stateless | Nao | Nao | Legacy, dev |

---

## 6. Documentacao de APIs

### 6.1 OpenAPI / Swagger

```yaml
openapi: "3.0.3"
info:
  title: API de Usuarios
  version: "1.0.0"
  description: API REST para gerenciamento de usuarios

paths:
  /api/usuarios:
    get:
      summary: Lista todos os usuarios
      parameters:
        - name: page
          in: query
          schema: { type: integer, default: 1 }
        - name: per_page
          in: query
          schema: { type: integer, default: 10 }
      responses:
        "200":
          description: Lista de usuarios
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/Usuario"
    post:
      summary: Cria um novo usuario
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/CriarUsuarioInput"
      responses:
        "201":
          description: Usuario criado
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Usuario"

components:
  schemas:
    Usuario:
      type: object
      properties:
        id: { type: integer }
        nome: { type: string }
        email: { type: string, format: email }
    CriarUsuarioInput:
      type: object
      required: [nome, email]
      properties:
        nome: { type: string, example: "Joao Silva" }
        email: { type: string, format: email, example: "joao@email.com" }
```

### 6.2 Geracao automatica com Python

```python
from flask_openapi3 import OpenAPI, Info, Tag
from pydantic import BaseModel, EmailStr

info = Info(title="API Usuarios", version="1.0.0")
app = OpenAPI(__name__, info=info)

class UsuarioBody(BaseModel):
    nome: str
    email: EmailStr

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr

@app.get("/api/usuarios", tags=["Usuarios"])
def listar():
    """Listar todos os usuarios"""
    return [UsuarioResponse(id=1, nome="Joao", email="joao@email.com")]

@app.post("/api/usuarios", tags=["Usuarios"])
def criar(body: UsuarioBody):
    """Criar novo usuario"""
    return UsuarioResponse(id=2, nome=body.nome, email=body.email)

if __name__ == "__main__":
    app.run(debug=True)
```

### 6.3 Documentacao GraphQL

GraphQL tem documentacao embutida via introspeccao. Ferramentas como GraphQL Playground e Apollo Studio Explorer permitem navegar pelo schema.

```graphql
"""
Um usuario do sistema
"""
type Usuario {
  "ID unico do usuario"
  id: ID!
  "Nome completo do usuario"
  nome: String!
  "Email do usuario (unico)"
  email: String!
  "Lista de pedidos do usuario"
  pedidos: [Pedido!]!
}
```

---

## 7. Rate Limiting e Throttling

Protege a API contra abusos e garante uso justo.

```python
import time
from collections import defaultdict
from flask import request, abort

class RateLimiter:
    def __init__(self, max_requests: int = 100, window: int = 60):
        self._max_requests = max_requests
        self._window = window
        self._requests: dict[str, list[float]] = defaultdict(list)

    def check(self, key: str) -> bool:
        now = time.time()
        window_start = now - self._window
        self._requests[key] = [t for t in self._requests[key] if t > window_start]

        if len(self._requests[key]) >= self._max_requests:
            return False

        self._requests[key].append(now)
        return True

rate_limiter = RateLimiter(max_requests=10, window=60)

@app.before_request
def rate_limit():
    cliente = request.headers.get("X-API-Key") or request.remote_addr
    if not rate_limiter.check(cliente):
        abort(429, "Too Many Requests")
```

```typescript
class RateLimiter {
  private requests = new Map<string, number[]>();

  constructor(
    private maxRequests: number,
    private windowMs: number,
  ) {}

  check(key: string): boolean {
    const now = Date.now();
    const windowStart = now - this.windowMs;
    const timestamps = (this.requests.get(key) ?? []).filter(t => t > windowStart);

    if (timestamps.length >= this.maxRequests) return false;

    timestamps.push(now);
    this.requests.set(key, timestamps);
    return true;
  }
}

const rateLimiter = new RateLimiter(10, 60000);

function rateLimitMiddleware(
  req: express.Request,
  res: express.Response,
  next: express.NextFunction
): void {
  const client = (req.headers["x-api-key"] as string) || req.ip!;
  if (!rateLimiter.check(client)) {
    res.status(429).json({ erro: "Too Many Requests" });
    return;
  }
  next();
}

function rateLimitHeaders(
  req: express.Request,
  res: express.Response,
  next: express.NextFunction
): void {
  res.setHeader("X-RateLimit-Limit", "10");
  res.setHeader("X-RateLimit-Remaining", "7");
  res.setHeader("X-RateLimit-Reset", "60");
  next();
}
```

---

## 8. Error Handling Patterns

### 8.1 Problema Padrao de Erros (RFC 7807)

```python
from flask import jsonify

class Problema:
    def __init__(self, title: str, status: int, detail: str, type: str = "about:blank"):
        self.type = type
        self.title = title
        self.status = status
        self.detail = detail

    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "title": self.title,
            "status": self.status,
            "detail": self.detail,
        }

@app.errorhandler(400)
def bad_request(error):
    problema = Problema(
        title="Bad Request",
        status=400,
        detail=str(error.description) if hasattr(error, "description") else "Dados invalidos",
    )
    return jsonify(problema.to_dict()), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify(Problema("Not Found", 404, "Recurso nao encontrado").to_dict()), 404

@app.errorhandler(422)
def unprocessable(error):
    return jsonify(Problema("Unprocessable Entity", 422, str(error)).to_dict()), 422
```

```typescript
interface Problema {
  type: string;
  title: string;
  status: number;
  detail: string;
  errors?: Record<string, string[]>;
}

function problema(
  title: string,
  status: number,
  detail: string,
  errors?: Record<string, string[]>
): Problema {
  return {
    type: "about:blank", title, status, detail,
    ...(errors && { errors }),
  };
}

class AppError extends Error {
  constructor(
    public statusCode: number,
    public detail: string,
    public errors?: Record<string, string[]>,
  ) {
    super(detail);
  }
}

app.use((err: Error, _req: express.Request, res: express.Response, _next: express.NextFunction) => {
  if (err instanceof AppError) {
    res.status(err.statusCode).json(problema(err.message, err.statusCode, err.detail, err.errors));
  } else {
    res.status(500).json(problema("Internal Server Error", 500, "Erro interno"));
  }
});
```

### 8.2 Matriz de Decisao de Erros

| Situacao | Status Code | Mensagem |
|---|---|---|
| Campo obrigatorio faltando | 400 | "Campo X e obrigatorio" |
| Formato invalido (email) | 422 | "Email em formato invalido" |
| Recurso nao encontrado | 404 | "Recurso nao encontrado" |
| Conflito de unicidade | 409 | "Registro ja existe com este email" |
| Token expirado | 401 | "Token de acesso expirado" |
| Sem permissao | 403 | "Acesso negado a este recurso" |
| Rate limit excedido | 429 | "Muitas requisicoes. Tente novamente em N segundos" |
| Servico indisponivel | 503 | "Servico temporariamente indisponivel" |

---

## 9. Seguranca em APIs

### 9.1 Checklist de Seguranca

- [ ] HTTPS obrigatorio (TLS 1.2+)
- [ ] CORS configurado (origens permitidas explicitas)
- [ ] Rate limiting implementado
- [ ] Input validation em todas as entradas
- [ ] SQL injection prevention (ORMs parametrizados)
- [ ] No disclosure de erros internos (stack traces)
- [ ] Content-Type validation (Content-Type: application/json)
- [ ] Tamanho maximo de payload (body-parser limit)
- [ ] Security headers (Helmet no Express)
- [ ] Dependency scanning (OWASP Dependency-Check)

```python
from flask_cors import CORS

CORS(app, origins=["https://meudominio.com"])

@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response
```

```typescript
import helmet from "helmet";
import cors from "cors";

app.use(helmet());
app.use(cors({
  origin: ["https://meudominio.com"],
  methods: ["GET", "POST", "PUT", "DELETE"],
  allowedHeaders: ["Content-Type", "Authorization"],
}));

app.use(express.json({ limit: "1mb" }));
```

---

## 10. Referencias Bibliograficas

- Fielding, R. T. *Architectural Styles and the Design of Network-based Software Architectures*. PhD Dissertation, UC Irvine, 2000.
- GraphQL Foundation. *GraphQL Specification*. graphql.org, 2015.
- Google. *gRPC Documentation*. grpc.io.
- Hardt, D. (Ed.). *The OAuth 2.0 Authorization Framework*. RFC 6749, 2012.
- Jones, M.; Bradley, J.; Sakimura, N. *JSON Web Token (JWT)*. RFC 7519, 2015.
- Nottingham, M. *Problem Details for HTTP APIs*. RFC 7807, 2016.
- Richardson, L.; Amundsen, M.; Ruby, S. *RESTful Web APIs*. O'Reilly, 2013.
- Newman, S. *Building Microservices* (2nd ed.). O'Reilly, 2021.
- Fowler, M. *Patterns of Enterprise Application Architecture*. Addison-Wesley, 2002.

## Ver Tambem

- [[Conhecimento-Geral/Programacao/Arquitetura-de-Software]]
- [[Conhecimento-Geral/Programacao/Design-Patterns]]
- [[Conhecimento-Geral/Programacao/Paradigmas-de-Programacao]]
- [[skills/02-software-engineering/advanced-backend-architecture]]
