---
tags: [api-design, rest, graphql, grpc, openapi, authentication, rate-limiting, skills-eng]
updated: 2026-06-08
title: "API Design - Contract-First API Development"
date: 2026-06-01
---

# API Design

Design de APIs com abordagem contract-first. Este guia cobre desde especificacao OpenAPI ate padroes avancados de autenticacao, rate limiting e idempotencia. Referencia para construir APIs consistentes, documentadas e production-ready.

## Taxonomia de Topicos

- Especificacao OpenAPI 3.x
- REST vs GraphQL vs gRPC
- Estrategias de versionamento
- Padroes de erro (RFC 7807)
- Rate limiting
- Paginacao
- API Gateways e BFF
- Documentacao-as-code
- Autenticacao
- Idempotencia e retry

## OpenAPI 3.x - Especificacao Completa

OpenAPI e o padrao da industria para definicao de APIs RESTful. Permite geracao automatica de documentacao, clientes e servidores.

### Exemplo Completo - API de Usuarios

```yaml
openapi: "3.1.0"
info:
  title: "JARVIS User API"
  version: "2.0.0"
  description: "API para gestao de usuarios do sistema JARVIS"
  contact:
    name: "Engineering Team"
    email: "eng@jarvis.local"
  license:
    name: "Proprietary"

servers:
  - url: https://api.jarvis.local/v2
    description: Producao
  - url: https://staging-api.jarvis.local/v2
    description: Staging

security:
  - BearerAuth: []

tags:
  - name: usuarios
    description: Operacoes com usuarios
  - name: perfis
    description: Perfis e preferencias

paths:
  /usuarios:
    get:
      operationId: listarUsuarios
      summary: Lista usuarios com paginacao
      tags: [usuarios]
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
            maximum: 100
        - name: cursor
          in: query
          schema:
            type: string
        - name: status
          in: query
          schema:
            type: string
            enum: [ativo, inativo, pendente]
      responses:
        "200":
          description: Lista de usuarios
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/UsuarioCollection"
        "401":
          $ref: "#/components/responses/Unauthorized"
        "429":
          $ref: "#/components/responses/RateLimited"

    post:
      operationId: criarUsuario
      summary: Cria novo usuario
      tags: [usuarios]
      idempotent: true
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/UsuarioCreate"
      responses:
        "201":
          description: Usuario criado
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Usuario"
          headers:
            Location:
              schema:
                type: string
                format: uri
        "400":
          $ref: "#/components/responses/BadRequest"
        "409":
          $ref: "#/components/responses/Conflict"

  /usuarios/{id}:
    get:
      operationId: obterUsuario
      summary: Obtem usuario por ID
      tags: [usuarios]
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        "200":
          description: Usuario encontrado
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Usuario"
        "404":
          $ref: "#/components/responses/NotFound"

    patch:
      operationId: atualizarUsuario
      summary: Atualizacao parcial de usuario
      tags: [usuarios]
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/UsuarioUpdate"
      responses:
        "200":
          description: Usuario atualizado
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Usuario"

components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
    ApiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key

  schemas:
    Usuario:
      type: object
      required: [id, email, criado_em]
      properties:
        id:
          type: string
          format: uuid
          readOnly: true
        email:
          type: string
          format: email
        nome:
          type: string
          maxLength: 255
        status:
          type: string
          enum: [ativo, inativo, pendente]
          default: pendente
        criado_em:
          type: string
          format: date-time
          readOnly: true
        atualizado_em:
          type: string
          format: date-time
          readOnly: true

    UsuarioCreate:
      type: object
      required: [email, senha]
      properties:
        email:
          type: string
          format: email
        senha:
          type: string
          format: password
          minLength: 8
          maxLength: 128
        nome:
          type: string
          maxLength: 255

    UsuarioUpdate:
      type: object
      minProperties: 1
      properties:
        nome:
          type: string
          maxLength: 255
        status:
          type: string
          enum: [ativo, inativo, pendente]

    UsuarioCollection:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: "#/components/schemas/Usuario"
        next_cursor:
          type: string
          nullable: true
        total:
          type: integer

    Error:
      type: object
      required: [type, title, status]
      properties:
        type:
          type: string
          format: uri
          example: "https://api.jarvis.local/errors/validation-error"
        title:
          type: string
          example: "Erro de validacao"
        status:
          type: integer
          example: 400
        detail:
          type: string
          example: "O campo email e obrigatorio"
        instance:
          type: string
          format: uri
        errors:
          type: array
          items:
            $ref: "#/components/schemas/FieldError"

    FieldError:
      type: object
      properties:
        field:
          type: string
          example: "email"
        message:
          type: string
          example: "Formato de email invalido"

  responses:
    BadRequest:
      description: Requisicao invalida
      content:
        application/problem+json:
          schema:
            $ref: "#/components/schemas/Error"
    Unauthorized:
      description: Nao autorizado
      content:
        application/problem+json:
          schema:
            type: object
            properties:
              type:
                type: string
                example: "https://api.jarvis.local/errors/unauthorized"
              title:
                type: string
                example: "Nao autorizado"
              status:
                type: integer
                example: 401
    NotFound:
      description: Recurso nao encontrado
      content:
        application/problem+json:
          schema:
            type: object
            properties:
              type:
                type: string
                example: "https://api.jarvis.local/errors/not-found"
              title:
                type: string
                example: "Nao encontrado"
              status:
                type: integer
                example: 404
    Conflict:
      description: Conflito de recurso
      content:
        application/problem+json:
          schema:
            type: object
            properties:
              type:
                type: string
                example: "https://api.jarvis.local/errors/conflict"
              title:
                type: string
                example: "Email ja em uso"
              status:
                type: integer
                example: 409
    RateLimited:
      description: Limite de requisicoes excedido
      headers:
        Retry-After:
          schema:
            type: integer
            description: Segundos ate proxima tentativa
        X-RateLimit-Limit:
          schema:
            type: integer
        X-RateLimit-Remaining:
          schema:
            type: integer
        X-RateLimit-Reset:
          schema:
            type: integer
            format: int64
      content:
        application/problem+json:
          schema:
            type: object
            properties:
              type:
                type: string
                example: "https://api.jarvis.local/errors/rate-limited"
              title:
                type: string
                example: "Muitas requisicoes"
              status:
                type: integer
                example: 429
```

### Geracao de Clientes a partir do Spec

```bash
# Gerar cliente Python
openapi-generator-cli generate \
  -i openapi.yaml \
  -g python \
  -o ./clients/python \
  --additional-properties=packageName=jarvis_client

# Gerar cliente TypeScript
openapi-generator-cli generate \
  -i openapi.yaml \
  -g typescript-axios \
  -o ./clients/typescript

# Gerar documentacao com Redoc
redocly build-docs openapi.yaml -o docs/api.html

# Validar spec
openapi-validator openapi.yaml
```

## REST vs GraphQL vs gRPC

| Caracteristica | REST | GraphQL | gRPC |
|---|---|---|---|
| Protocolo | HTTP/1.1 ou HTTP/2 | HTTP/2 | HTTP/2 |
| Formato | JSON, XML | JSON | Protobuf (binario) |
| Tipo de comunicacao | Request/Response | Query/Mutation/Subscription | Request/Response, Streaming |
| Over-fetching | Comum (retorna campos demais) | Zero (cliente pede exato) | Zero (schema define campos) |
| Under-fetching | Comum (multiplas calls) | Zero (single query) | Parcial (multiplas calls) |
| Caching | HTTP cache nativo | Requer implementacao custom | Nao suportado nativamente |
| Versionamento | URL ou header | Schema evolution | Protobuf backward-compatible |
| Tooling | Swagger/OpenAPI | GraphQL Playground, Apollo | protoc, grpcurl |
| Curva de aprendizado | Baixa | Media | Alta |
| Ideal para | APIs publicas, CRUD | Frontends complexos, mobile | Microservices internos, streaming |
| Performance | Boa | Media (parsing JSON) | Excelente (binario) |
| Type safety | Via OpenAPI | Nativo (schema) | Nativo (protobuf) |

### Quando Usar Cada Um

```
REST:
  - API publica para terceiros
  - CRUD simples
  - Caching HTTP importante
  - Integracao com sistemas legados

GraphQL:
  - Frontend com necessidades variadas de dados
  - Mobile (reduz over-fetching)
  - Multiplas fontes de dados (federation)
  - Dashboard com queries complexas

gRPC:
  - Comunicacao entre microservices
  - Streaming em tempo real
  - Alta performance requerida
  - Contratos fortes entre equipes
```

## Estrategias de Versionamento

### 1. Versionamento por URL (Mais comum)

```
GET /v1/usuarios
GET /v2/usuarios
```

```python
# FastAPI - Multiplas versoes
from fastapi import APIRouter

v1_router = APIRouter(prefix="/v1")
v2_router = APIRouter(prefix="/v2")

@v1_router.get("/usuarios")
def listar_usuarios_v1():
    # Retorna apenas id e nome
    return [{"id": 1, "nome": "Joao"}]

@v2_router.get("/usuarios")
def listar_usuarios_v2():
    # Retorna objeto completo com status
    return [{"id": 1, "nome": "Joao", "status": "ativo", "email": "joao@email.com"}]
```

### 2. Versionamento por Header

```
GET /usuarios
Header: API-Version: 2026-05-16
```

```python
from fastapi import Request, Header, APIRouter

router = APIRouter()

@router.get("/usuarios")
def listar_usuarios(request: Request, api_version: str = Header("2024-01-01")):
    if api_version >= "2026-01-01":
        return listar_v2()
    return listar_v1()
```

### 3. Content Negotiation

```
GET /usuarios
Accept: application/vnd.jarvis.v2+json
```

```python
from fastapi import Request

@router.get("/usuarios")
def listar_usuarios(request: Request):
    accept = request.headers.get("accept", "")
    if "vnd.jarvis.v2" in accept:
        return listar_v2()
    return listar_v1()
```

### Recomendacao de Versionamento

| Estrategia | Quando Usar | Vantagem | Desvantagem |
|---|---|---|---|
| URL | API publica | Simples, explicito | Polui URLs |
| Header | API interna | URLs limpas | Menos descobrivel |
| Content Negotiation | API madura | RESTful puro | Complexo de implementar |

## Padroes de Erro - RFC 7807 Problem Details

RFC 7807 define um formato padronizado para respostas de erro em APIs HTTP.

### Implementacao em FastAPI

```python
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List

class FieldError(BaseModel):
    field: str
    message: str

class ProblemDetail(BaseModel):
    type: str = "about:blank"
    title: str
    status: int
    detail: Optional[str] = None
    instance: Optional[str] = None
    errors: Optional[List[FieldError]] = None

app = FastAPI()

@app.exception_handler(HTTPException)
async def problem_detail_handler(request: Request, exc: HTTPException):
    problem = ProblemDetail(
        type=f"https://api.jarvis.local/errors/{exc.status_code}",
        title=exc.detail or "Erro desconhecido",
        status=exc.status_code,
        instance=str(request.url),
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=problem.model_dump(exclude_none=True),
        headers={"Content-Type": "application/problem+json"},
    )

@app.exception_handler(ValueError)
async def validation_error_handler(request: Request, exc: ValueError):
    problem = ProblemDetail(
        type="https://api.jarvis.local/errors/validation-error",
        title="Erro de validacao",
        status=400,
        detail=str(exc),
        instance=str(request.url),
    )
    return JSONResponse(
        status_code=400,
        content=problem.model_dump(exclude_none=True),
        headers={"Content-Type": "application/problem+json"},
    )

# Exemplo de uso
@app.post("/usuarios")
async def criar_usuario(email: str):
    if "@" not in email:
        raise ValueError("Email invalido")
    return {"email": email}
```

### Resposta de Erro Exemplo

```json
{
  "type": "https://api.jarvis.local/errors/validation-error",
  "title": "Erro de validacao",
  "status": 400,
  "detail": "O campo email e obrigatorio",
  "instance": "/v2/usuarios",
  "errors": [
    {
      "field": "email",
      "message": "Formato de email invalido"
    },
    {
      "field": "senha",
      "message": "Minimo de 8 caracteres"
    }
  ]
}
```

## Rate Limiting

### Algoritmos de Rate Limiting

#### 1. Token Bucket

```python
import time
import threading
from collections import defaultdict

class TokenBucket:
    """
    Token Bucket: permite bursts ate o tamanho do bucket.
    Tokens sao adicionados a uma taxa fixa.
    """
    def __init__(self, rate: float, capacity: float):
        self.rate = rate           # tokens por segundo
        self.capacity = capacity   # tamanho maximo do bucket
        self.tokens = defaultdict(lambda: capacity)
        self.last_refill = defaultdict(time.time)
        self.lock = threading.Lock()

    def consume(self, key: str, tokens: int = 1) -> bool:
        with self.lock:
            now = time.time()
            elapsed = now - self.last_refill[key]
            self.tokens[key] = min(
                self.capacity,
                self.tokens[key] + elapsed * self.rate
            )
            self.last_refill[key] = now

            if self.tokens[key] >= tokens:
                self.tokens[key] -= tokens
                return True
            return False

# Uso
limiter = TokenBucket(rate=10, capacity=20)  # 10 req/s, burst de 20

def endpoint_protegido(user_id: str):
    if not limiter.consume(user_id):
        return {"error": "Rate limited"}, 429
    return process_request()
```

#### 2. Sliding Window Log

```python
import time
from collections import defaultdict, deque

class SlidingWindowLog:
    """
    Sliding Window Log: registra timestamp de cada request.
    Preciso mas consome mais memoria.
    """
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(deque)

    def allow(self, key: str) -> bool:
        now = time.time()
        window_start = now - self.window_seconds

        # Remove requests fora da janela
        while self.requests[key] and self.requests[key][0] < window_start:
            self.requests[key].popleft()

        if len(self.requests[key]) < self.max_requests:
            self.requests[key].append(now)
            return True
        return False

# Uso
limiter = SlidingWindowLog(max_requests=100, window_seconds=60)
```

#### 3. Sliding Window Counter

```python
import time
import math
from collections import defaultdict

class SlidingWindowCounter:
    """
    Sliding Window Counter: combina fixed windows com ponderacao.
    Eficiente em memoria, boa aproximacao.
    """
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.counters = defaultdict(lambda: {"current": 0, "previous": 0})
        self.window_start = defaultdict(float)

    def allow(self, key: str) -> bool:
        now = time.time()
        current_window = math.floor(now / self.window_seconds)

        if current_window != self.window_start[key]:
            self.counters[key]["previous"] = self.counters[key]["current"]
            self.counters[key]["current"] = 0
            self.window_start[key] = current_window

        # Calcula peso da janela anterior
        elapsed_in_window = now % self.window_seconds
        weight = 1 - (elapsed_in_window / self.window_seconds)
        weighted_count = (
            self.counters[key]["current"] +
            self.counters[key]["previous"] * weight
        )

        if weighted_count < self.max_requests:
            self.counters[key]["current"] += 1
            return True
        return False
```

#### 4. Leaky Bucket

```python
import time
from collections import defaultdict, deque

class LeakyBucket:
    """
    Leaky Bucket: requests sao processados a taxa constante.
    Suaviza o trafego, elimina bursts.
    """
    def __init__(self, rate: float, capacity: int):
        self.rate = rate              # requests por segundo
        self.capacity = capacity      # tamanho da fila
        self.queue = defaultdict(deque)
        self.last_leak = defaultdict(time.time)

    def allow(self, key: str) -> bool:
        now = time.time()
        elapsed = now - self.last_leak[key]
        leaked = elapsed * self.rate

        # "Vaza" requests da fila
        while self.queue[key] and leaked >= 1:
            self.queue[key].popleft()
            leaked -= 1

        self.last_leak[key] = now

        if len(self.queue[key]) < self.capacity:
            self.queue[key].append(now)
            return True
        return False
```

### Rate Limiting com Redis (Producao)

```python
import redis
import time

class RedisRateLimiter:
    """Rate limiter distribuido usando Redis."""

    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client

    def sliding_window(self, key: str, max_requests: int, window: int) -> tuple[bool, dict]:
        """
        Sliding window com Redis sorted set.
        Retorna (allow, headers_dict)
        """
        now = time.time()
        window_start = now - window
        pipe = self.redis.pipeline()

        # Remove entries expiradas
        pipe.zremrangebyscore(key, 0, window_start)
        # Conta requests na janela
        pipe.zcard(key)
        # Adiciona request atual
        pipe.zadd(key, {str(now): now})
        # Define TTL
        pipe.expire(key, window)

        results = pipe.execute()
        count = results[1]

        headers = {
            "X-RateLimit-Limit": str(max_requests),
            "X-RateLimit-Remaining": str(max(0, max_requests - count - 1)),
            "X-RateLimit-Reset": str(int(now + window)),
        }

        if count >= max_requests:
            headers["Retry-After"] = str(window)
            return False, headers

        return True, headers
```

## Padroes de Paginacao

### 1. Offset-Based (Simples, mas ineficiente para datasets grandes)

```python
@app.get("/usuarios")
def listar_usuarios_offset(
    limit: int = Query(20, le=100),
    offset: int = Query(0, ge=0),
):
    usuarios = db.query(Usuario).offset(offset).limit(limit).all()
    total = db.query(Usuario).count()
    return {
        "data": usuarios,
        "limit": limit,
        "offset": offset,
        "total": total,
        "has_more": offset + limit < total,
    }
```

### 2. Cursor-Based (Recomendado para APIs)

```python
import base64
from datetime import datetime

def encode_cursor(created_at: datetime, id: str) -> str:
    data = f"{created_at.iso()}|{id}"
    return base64.b64encode(data.encode()).decode()

def decode_cursor(cursor: str) -> tuple[datetime, str]:
    data = base64.b64decode(cursor).decode()
    created_at_str, id = data.split("|")
    return datetime.fromisoformat(created_at_str), id

@app.get("/usuarios")
def listar_usuarios_cursor(
    limit: int = Query(20, le=100),
    cursor: str | None = None,
):
    query = db.query(Usuario).order_by(Usuario.criado_em.desc(), Usuario.id.desc())

    if cursor:
        created_at, id = decode_cursor(cursor)
        query = query.filter(
            (Usuario.criado_em < created_at) |
            ((Usuario.criado_em == created_at) & (Usuario.id < id))
        )

    # Pega um item extra para saber se ha mais
    usuarios = query.limit(limit + 1).all()
    has_more = len(usuarios) > limit
    if has_more:
        usuarios = usuarios[:-1]

    next_cursor = None
    if usuarios and has_more:
        last = usuarios[-1]
        next_cursor = encode_cursor(last.criado_em, str(last.id))

    return {
        "data": usuarios,
        "next_cursor": next_cursor,
        "has_more": has_more,
    }
```

### 3. Keyset Pagination (Para ordenacao customizada)

```python
@app.get("/usuarios")
def listar_usuarios_keyset(
    limit: int = Query(20, le=100),
    last_id: str | None = None,
    last_score: float | None = None,
):
    query = db.query(Usuario).order_by(Usuario.score.desc(), Usuario.id.asc())

    if last_id and last_score is not None:
        query = query.filter(
            (Usuario.score < last_score) |
            ((Usuario.score == last_score) & (Usuario.id > last_id))
        )

    usuarios = query.limit(limit + 1).all()
    has_more = len(usuarios) > limit
    if has_more:
        usuarios = usuarios[:-1]

    next_params = None
    if usuarios and has_more:
        last = usuarios[-1]
        next_params = {"last_id": str(last.id), "last_score": last.score}

    return {
        "data": usuarios,
        "next": next_params,
        "has_more": has_more,
    }
```

### Comparacao de Paginacao

| Metodo | Performance | Complexidade | Ideal Para |
|---|---|---|---|
| Offset | Degrada com offset alto | Baixa | Datasets pequenos, admin UI |
| Cursor | Constante | Media | APIs publicas, feeds |
| Keyset | Constante | Media-Alta | Ordenacao customizada, rankings |

## API Gateways e BFF Pattern

### API Gateway

```
                    +------------------+
   Cliente -------->|  API Gateway     |
                    |  (Kong, Traefik) |
                    +--------+---------+
                             |
              +--------------+--------------+
              |              |              |
              v              v              v
        +----------+  +----------+  +----------+
        | Servico  |  | Servico  |  | Servico  |
        | Usuarios |  | Pedidos  |  | Pagamento|
        +----------+  +----------+  +----------+
```

### BFF (Backend for Frontend)

```
                    +-----------------+
   Web App ------->|  BFF Web        |--+
                    +-----------------+  |
                                         v
                    +-----------------+  +-----------------+
   Mobile App ---->|  BFF Mobile     |->|  API Gateway    |
                    +-----------------+  +-----------------+
```

### Implementacao BFF com FastAPI

```python
from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

# URLs dos servicos internos
USER_SERVICE = "http://user-service:8001"
ORDER_SERVICE = "http://order-service:8002"

@app.get("/api/web/dashboard")
async def dashboard_web(token: str):
    """BFF Web: agrega dados para dashboard desktop."""
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {token}"}

        # Busca dados em paralelo
        user_resp, orders_resp = await asyncio.gather(
            client.get(f"{USER_SERVICE}/usuarios/me", headers=headers),
            client.get(f"{ORDER_SERVICE}/pedidos/recentes", headers=headers),
        )

        if user_resp.status_code != 200:
            raise HTTPException(status_code=user_resp.status_code)

        user = user_resp.json()
        orders = orders_resp.json()

        # Transforma para formato do frontend web
        return {
            "nome_completo": f"{user['nome']} {user['sobrenome']}",
            "pedidos_recentes": [
                {"id": o["id"], "total": o["total"], "status": o["status"]}
                for o in orders[:5]
            ],
            "stats": {
                "total_pedidos": len(orders),
                "total_gasto": sum(o["total"] for o in orders),
            },
        }

@app.get("/api/mobile/home")
async def home_mobile(token: str):
    """BFF Mobile: resposta otimizada para mobile (menos dados)."""
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {token}"}

        user_resp = await client.get(f"{USER_SERVICE}/usuarios/me", headers=headers)
        user = user_resp.json()

        return {
            "nome": user["nome"],
            "avatar_url": user["avatar"],
            "notificacoes_count": user.get("notificacoes", 0),
        }
```

## Documentacao-as-Code

### Swagger UI com FastAPI

```python
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI(
    title="JARVIS API",
    description="API principal do sistema JARVIS",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="JARVIS API",
        version="2.0.0",
        description="Documentacao completa da API",
        routes=app.routes,
    )

    # Adiciona exemplos globais
    openapi_schema["info"]["contact"] = {
        "name": "Engineering Team",
        "email": "eng@jarvis.local",
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
```

### Geracao com Redocly

```yaml
# redocly.yaml
apis:
  main@v2:
    root: ./openapi.yaml
extends:
  - recommended
rules:
  no-unused-components: error
  operation-summary: error
  tag-description: warn
theme:
  openapi:
    theme:
      colors:
        primary:
          main: "#32329f"
    generateCodeSamples:
      languages:
        - lang: curl
        - lang: Python
        - lang: JavaScript
```

```bash
# Preview local
redocly preview-docs openapi.yaml

# Build estatico
redocly build-docs openapi.yaml -o docs/api.html

# Lint
redocly lint openapi.yaml
```

## Padroes de Autenticacao

### OAuth2 com FastAPI

```python
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

SECRET_KEY = "sua-chave-secreta-aqui"  # Use variavel de ambiente
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais invalidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return user_id
```

### API Key Authentication

```python
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")

VALID_API_KEYS = {
    "sk-proj-abc123": {"user_id": "user_1", "tier": "premium"},
    "sk-proj-def456": {"user_id": "user_2", "tier": "free"},
}

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key not in VALID_API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key invalida",
        )
    return VALID_API_KEYS[api_key]
```

## Idempotencia e Retry Patterns

### Idempotency Key Pattern

```python
import hashlib
from fastapi import Request, HTTPException
from redis import Redis

redis_client = Redis()

def get_idempotency_key(request: Request) -> str | None:
    return request.headers.get("Idempotency-Key")

def check_idempotency(key: str) -> bytes | None:
    """Retorna resposta cached se chave ja foi processada."""
    return redis_client.get(f"idempotency:{key}")

def cache_idempotency(key: str, response: bytes, ttl: int = 3600):
    """Cacha resposta para idempotencia."""
    redis_client.setex(f"idempotency:{key}", ttl, response)

@app.post("/pedidos")
async def criar_pedido(
    request: Request,
    dados: PedidoCreate,
    current_user=Depends(get_current_user),
):
    idempotency_key = get_idempotency_key(request)

    if idempotency_key:
        cached = check_idempotency(idempotency_key)
        if cached:
            return JSONResponse(content=json.loads(cached))

    # Processa pedido
    pedido = processar_pedido(dados, current_user)

    if idempotency_key:
        response_data = {"id": pedido.id, "status": "criado"}
        cache_idempotency(idempotency_key, json.dumps(response_data).encode())
        return response_data

    return {"id": pedido.id, "status": "criado"}
```

### Retry com Exponential Backoff

```python
import time
import random
from functools import wraps

def retry_with_backoff(
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    jitter: bool = True,
):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == max_retries:
                        raise

                    delay = min(base_delay * (2 ** attempt), max_delay)
                    if jitter:
                        delay *= random.uniform(0.5, 1.5)

                    time.sleep(delay)
            return None
        return wrapper
    return decorator

# Uso com httpx
import httpx

@retry_with_backoff(max_retries=3, base_delay=1.0)
def call_external_api(url: str, data: dict):
    response = httpx.post(url, json=data, timeout=10.0)
    response.raise_for_status()
    return response.json()
```

## Referencias Cruzadas

- [[backend]] - Implementacao de APIs com FastAPI e Node.js
- [[seguranca/owasp-top-10|OWASP Top 10]] - Vulnerabilidades comuns em APIs
- [[seguranca/secure-coding|Secure Coding]] - Praticas de codigo seguro
- [[performance]] - Otimizacao de performance de APIs
- [[advanced-backend-architecture|Advanced Backend Architecture]] - Padroes arquiteturais
- [[database]] - Modelagem de dados para APIs
- [[../devops/Observabilidade|Observabilidade]] - Monitoring de APIs em producao
- [[testing/SKILL|Testing]] - Testes de API com httpx e Jest
