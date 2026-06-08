---
tags: [skills, skills-eng, backend, api]
updated: 2026-06-08
title: "Backend Skills - FastAPI, Express, Autenticacao"
date: 2026-04-27
---

# Backend Skills — FastAPI, Express e Padroes de API

Referencia pratica para construcao de APIs robustas com FastAPI (Python) e Express (Node.js), cobrindo autenticacao, validacao, middleware e tratamento de erros.

## FastAPI — Padroes Essenciais

### Injecao de Dependencia

```python
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session

app = FastAPI()

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = await decode_token(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Credenciais invalidas")
    return user

@app.get("/users/me")
async def read_users_me(
    current_user = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    return current_user
```

### Middleware de Auditoria

```python
import time
from fastapi import Request

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    elapsed = time.time() - start
    print(f"{request.method} {request.url.path} - {elapsed:.3f}s")
    return response
```

### Validacao com Pydantic

```python
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    senha: str = Field(..., min_length=8)
    roles: list[str] = ["usuario"]

class UserResponse(BaseModel):
    id: int
    nome: str
    email: str
    criado_em: datetime
    ativo: bool

    model_config = {"from_attributes": True}
```

### Tratamento de Erros Centralizado

```python
from fastapi import Request
from fastapi.responses import JSONResponse

class AppError(Exception):
    def __init__(self, codigo: str, mensagem: str, status: int = 400):
        self.codigo = codigo
        self.mensagem = mensagem
        self.status = status

@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status,
        content={"erro": exc.codigo, "mensagem": exc.mensagem}
    )

@app.exception_handler(ValidationError)
async def validation_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={"erro": "validacao", "detalhes": exc.errors()}
    )
```

## Fluxos de Autenticacao

### JWT com OAuth2 (FastAPI)

```python
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "sua-chave-secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401)
    except JWTError:
        raise HTTPException(status_code=401)
    return await get_user(user_id)
```

### Express com JWT

```javascript
const jwt = require('jsonwebtoken');

function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  if (!token) return res.sendStatus(401);

  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
}
```

## Padroes Arquiteturais

- **Repository Pattern**: Abstraia o acesso a dados em repositorios
- **Service Layer**: Centralize logica de negocio em servicos
- **DTO Pattern**: Use objetos de transferencia para separar camadas
- **Unit of Work**: Agrupe operacoes em transacoes atomicas

## Exemplo de Estrutura de Projeto

```
app/
  core/
    config.py          # Configuracoes globais
    security.py        # JWT, hashing
    exceptions.py      # Erros personalizados
  models/
    user.py            # Modelos SQLAlchemy
  schemas/
    user.py            # Schemas Pydantic
  services/
    user_service.py    # Logica de negocio
  api/
    v1/
      endpoints/
        users.py       # Rotas
      deps.py          # Dependencias compartilhadas
  main.py              # App FastAPI
```

## Testes

```python
from fastapi.testclient import TestClient

def test_create_user(client: TestClient):
    response = client.post("/users/", json={
        "nome": "Teste",
        "email": "teste@email.com",
        "senha": "senha123"
    })
    assert response.status_code == 201
    assert response.json()["email"] == "teste@email.com"
```

## Referencias

- [[database|Database]] — Modelagem e migracoes para persistencia
- [[05-Skills/ai/MLOps|MLOps]] — Pipelines de deploy e CI/CD
- [[05-Skills/devops/Kubernetes|Kubernetes]] — Orquestracao de servicos em producao
- [[advanced-backend-architecture|Arquitetura Avancada]] — Padroes para sistemas complexos
