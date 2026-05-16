---
tags: [skills, seguranca, secure-coding, python, javascript]
updated: 2026-05-16
title: "Secure Coding Practices"
---

# Secure Coding Practices

Guia de codificacao segura com exemplos praticos em Python e JavaScript. Aborda as principais categorias de vulnerabilidade com codigo vulneravel e corrigido para cada uma.

## 1. Input Validation

Validar toda entrada do usuario antes de processar. Dados nao confiaveis podem vir de parametros de URL, corpo de requisicao, headers, uploads de arquivo e fontes externas.

### Python: Validacao de Entrada

```python
import re
from email_validator import validate_email, EmailNotValidError
from pydantic import BaseModel, Field, validator

# Abordagem 1: Validacao manual com regex
def validate_username(username: str) -> str:
    if not re.match(r"^[a-zA-Z0-9_]{3,30}$", username):
        raise ValueError("Username deve ter 3-30 caracteres alfanumericos")
    return username

def validate_age(age: str) -> int:
    try:
        age_int = int(age)
        if not (0 < age_int < 150):
            raise ValueError
        return age_int
    except (ValueError, TypeError):
        raise ValueError("Idade deve ser um numero entre 1 e 149")

# Abordagem 2: Pydantic para validacao declarativa
class UserInput(BaseModel):
    username: str = Field(..., min_length=3, max_length=30, regex=r"^[a-zA-Z0-9_]+$")
    email: str = Field(..., max_length=254)
    age: int = Field(..., gt=0, lt=150)

    @validator("email")
    def validate_email_format(cls, v):
        try:
            validate_email(v)
        except EmailNotValidError as e:
            raise ValueError(str(e))
        return v

# Uso
user_input = UserInput(username="joao_silva", email="joao@example.com", age=28)
```

### JavaScript: Validacao de Entrada

```javascript
const z = require("zod");

// Schema de validacao com Zod
const UserSchema = z.object({
  username: z
    .string()
    .min(3)
    .max(30)
    .regex(/^[a-zA-Z0-9_]+$/),
  email: z.string().email().max(254),
  age: z.number().int().positive().max(149),
});

// Sanitizacao de HTML (anti-XSS)
const createDOMPurify = require("dompurify");
const { JSDOM } = require("jsdom");
const window = new JSDOM("").window;
const DOMPurify = createDOMPurify(window);

function sanitizeHtml(input) {
  return DOMPurify.sanitize(input, { ALLOWED_TAGS: ["b", "i", "em", "strong"] });
}

// Uso
app.post("/api/users", (req, res) => {
  try {
    const data = UserSchema.parse(req.body);
    data.bio = sanitizeHtml(data.bio);
    res.json({ success: true, data });
  } catch (err) {
    res.status(400).json({ error: err.errors });
  }
});
```

### Principios de Input Validation
- **Allowlist (whitelist)**: Defina o que e permitido, rejeite o resto
- **Denylist (blacklist)**: Facil de contornar, evite usar
- **Validar no servidor**: Validacao no cliente e apenas UX, nunca seguranca
- **Normalizar antes de validar**: Unicode normalization (NFC, NFKC)

```python
import unicodedata

def normalize_and_validate(input_str: str) -> str:
    normalized = unicodedata.normalize("NFKC", input_str)
    if re.match(r"^[a-zA-Z0-9_]+$", normalized):
        return normalized
    raise ValueError("Caracteres invalidos apos normalizacao")
```

## 2. Output Encoding

Prevenir XSS e injecao de codigo codificando dados antes de renderizar no contexto apropriado.

### Contextos de Encoding

| Contexto | Encoding | Exemplo |
|----------|----------|---------|
| HTML Body | HTML Entity Encoding | `&` -> `&amp;` |
| HTML Attribute | Attribute Encoding | `"` -> `&quot;` |
| JavaScript String | Unicode Escaping | `'` -> `\x27` |
| URL Parameter | URL Encoding | ` ` -> `%20` |
| CSS String | CSS Escaping | `\` -> `\\` |

### Python: Output Encoding

```python
import html
import json
from urllib.parse import quote

# HTML Encoding
user_input = '<script>alert("xss")</script>'
safe_html = html.escape(user_input)
print(safe_html)
# Output: &lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;

# JSON Encoding (sempre usar json.dumps, nunca concatenar)
data = {"user": user_input, "role": "admin"}
safe_json = json.dumps(data, ensure_ascii=False)

# URL Encoding
url_safe = quote("parametro com espacos & simbolos")
print(url_safe)
# Output: parametro%20com%20espacos%20%26%20simbolos
```

### JavaScript: Output Encoding (React/Next.js)

```javascript
// React escapa automaticamente no JSX
function UserProfile({ user }) {
  return (
    <div>
      {/* React faz html.escape automaticamente */}
      <h1>{user.name}</h1>
      {/* dangerouslySetInnerHTML requer sanitizacao explicita */}
      <div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(user.bio) }} />
    </div>
  );
}

// Para templates fora do React
function encodeHtml(str) {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#x27;");
}

// JavaScript String encoding
function encodeJsString(str) {
  return str
    .replace(/\\/g, "\\\\")
    .replace(/'/g, "\\x27")
    .replace(/"/g, "\\x22")
    .replace(/\n/g, "\\n")
    .replace(/\r/g, "\\r");
}
```

### Content Security Policy (CSP)

```python
# Configuracao de CSP em FastAPI
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self' 'nonce-random123'; "
        "style-src 'self' 'unsafe-inline'; "
        "img-src 'self' https:; "
        "font-src 'self'; "
        "object-src 'none'; "
        "frame-ancestors 'none'; "
        "base-uri 'self'; "
        "form-action 'self'"
    )
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "0"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response
```

## 3. Authentication

Implementacao segura de autenticacao: hash de senhas, JWT, MFA, gerenciamento de sessoes.

### Python: Autenticacao Segura

```python
from argon2 import PasswordHasher
from datetime import datetime, timedelta
import jwt
import secrets

ph = PasswordHasher(
    time_cost=3,        # Numero de iteracoes
    memory_cost=65536,  # 64 MB de memoria
    parallelism=4,      # Threads paralelas
    hash_len=32,        # Tamanho do hash
    salt_len=16         # Tamanho do salt
)

# Hash de senha
def hash_password(password: str) -> str:
    return ph.hash(password)

# Verificacao de senha
def verify_password(password: str, password_hash: str) -> bool:
    try:
        return ph.verify(password_hash, password)
    except:
        return False

# JWT Token (acesso e refresh)
SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = timedelta(minutes=30)
REFRESH_TOKEN_EXPIRE = timedelta(days=7)

def create_access_token(user_id: int, roles: list[str]) -> str:
    payload = {
        "sub": str(user_id),
        "roles": roles,
        "type": "access",
        "exp": datetime.utcnow() + ACCESS_TOKEN_EXPIRE,
        "iat": datetime.utcnow(),
        "jti": secrets.token_hex(16)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(user_id: int) -> str:
    payload = {
        "sub": str(user_id),
        "type": "refresh",
        "exp": datetime.utcnow() + REFRESH_TOKEN_EXPIRE,
        "iat": datetime.utcnow(),
        "jti": secrets.token_hex(16)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("type") != "access":
            raise ValueError("Tipo de token invalido")
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token expirado")
    except jwt.InvalidTokenError:
        raise ValueError("Token invalido")
```

### JavaScript: Autenticacao com bcrypt e JWT

```javascript
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const crypto = require("crypto");

const SECRET_KEY = crypto.randomBytes(32).toString("hex");
const SALT_ROUNDS = 12;

async function hashPassword(password) {
  return bcrypt.hash(password, SALT_ROUNDS);
}

async function verifyPassword(password, hash) {
  return bcrypt.compare(password, hash);
}

function generateTokens(userId, roles) {
  const accessToken = jwt.sign(
    {
      sub: userId,
      roles,
      type: "access",
    },
    SECRET_KEY,
    { expiresIn: "30m", jwtid: crypto.randomUUID() }
  );

  const refreshToken = jwt.sign(
    {
      sub: userId,
      type: "refresh",
    },
    SECRET_KEY,
    { expiresIn: "7d", jwtid: crypto.randomUUID() }
  );

  return { accessToken, refreshToken };
}

function verifyAccessToken(token) {
  try {
    const decoded = jwt.verify(token, SECRET_KEY);
    if (decoded.type !== "access") throw new Error("Invalid token type");
    return decoded;
  } catch (err) {
    throw new Error("Invalid or expired token");
  }
}
```

### Boas Praticas de Autenticacao
- Hash de senhas com Argon2id (ou bcrypt/scrypt como fallback)
- Nunca armazenar senhas em texto claro
- Implementar lockout apos N tentativas falhas
- Usar MFA para acoes sensiveis
- Refresh tokens rotativos e com expiracao
- Rate limiting em endpoints de login
- Nao revelar se usuario existe ou nao na mensagem de erro

## 4. Authorization (RBAC/ABAC)

Controle de acesso baseado em roles (RBAC) ou atributos (ABAC).

### Python: RBAC Pattern

```python
from functools import wraps
from fastapi import HTTPException, Depends
from typing import List

class RBACMiddleware:
    def __init__(self):
        # Matrix de permissoes: role -> {resource: [actions]}
        self.permissions = {
            "admin": {
                "users": ["create", "read", "update", "delete"],
                "invoices": ["create", "read", "update", "delete"],
                "reports": ["create", "read", "update", "delete"],
            },
            "manager": {
                "users": ["read"],
                "invoices": ["create", "read", "update"],
                "reports": ["create", "read"],
            },
            "viewer": {
                "users": ["read"],
                "invoices": ["read"],
                "reports": ["read"],
            },
        }

    def check_permission(self, role: str, resource: str, action: str) -> bool:
        role_perms = self.permissions.get(role, {})
        return action in role_perms.get(resource, [])

rbac = RBACMiddleware()

def require_permission(resource: str, action: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, current_user: User = Depends(get_current_user), **kwargs):
            if not rbac.check_permission(current_user.role, resource, action):
                raise HTTPException(
                    status_code=403,
                    detail=f"Permissao negada: {action} em {resource}"
                )
            return await func(*args, current_user=current_user, **kwargs)
        return wrapper
    return decorator

# Uso
@app.get("/api/invoices")
@require_permission("invoices", "read")
async def list_invoices(current_user: User = Depends(get_current_user)):
    return await get_invoices_for_user(current_user.id)
```

### JavaScript: ABAC com Policy Engine

```javascript
// Attribute-Based Access Control
class ABACEngine {
  constructor() {
    this.policies = [
      {
        name: "owner-access",
        effect: "allow",
        condition: (user, resource) =>
          resource.ownerId === user.id,
      },
      {
        name: "admin-access",
        effect: "allow",
        condition: (user, resource) =>
          user.roles.includes("admin"),
      },
      {
        name: "deny-outside-business-hours",
        effect: "deny",
        condition: (user, resource) => {
          const hour = new Date().getHours();
          return hour < 8 || hour > 18;
        },
      },
    ];
  }

  authorize(user, action, resource) {
    let allowed = false;
    for (const policy of this.policies) {
      if (policy.condition(user, resource)) {
        if (policy.effect === "deny") return false;
        if (policy.effect === "allow") allowed = true;
      }
    }
    return allowed;
  }
}

// Uso
const abac = new ABACEngine();
app.get("/api/invoices/:id", (req, res) => {
  const resource = invoices.find((i) => i.id === req.params.id);
  if (!abac.authorize(req.user, "read", resource)) {
    return res.status(403).json({ error: "Acesso negado" });
  }
  res.json(resource);
});
```

## 5. Session Management

Gerenciamento seguro de sessoes de usuario.

```python
import uuid
from datetime import datetime, timedelta

class SessionManager:
    def __init__(self, redis_client):
        self.redis = redis_client
        self.session_ttl = timedelta(hours=1)

    async def create_session(self, user_id: int) -> str:
        session_id = str(uuid.uuid4())
        session_data = {
            "user_id": user_id,
            "created_at": datetime.utcnow().isoformat(),
            "ip_address": None,
            "user_agent": None
        }
        await self.redis.setex(
            f"session:{session_id}",
            self.session_ttl,
            json.dumps(session_data)
        )
        return session_id

    async def get_session(self, session_id: str) -> dict | None:
        data = await self.redis.get(f"session:{session_id}")
        if not data:
            return None
        # Renovar TTL em cada acesso
        await self.redis.expire(f"session:{session_id}", self.session_ttl)
        return json.loads(data)

    async def invalidate_session(self, session_id: str):
        await self.redis.delete(f"session:{session_id}")

    async def invalidate_all_user_sessions(self, user_id: int):
        # Invalida todas as sessoes de um usuario (ex: troca de senha)
        pattern = f"session:*"
        async for key in self.redis.scan_iter(match=pattern):
            data = await self.redis.get(key)
            if data and json.loads(data).get("user_id") == user_id:
                await self.redis.delete(key)
```

### Seguranca em Sessoes
- Gerar session IDs com `secrets` ou `uuid4`
- Armazenar sessoes no servidor (Redis, banco de dados)
- Cookies com flags: HttpOnly, Secure, SameSite=Lax/Strict
- Rotacionar session ID apos login
- Invalidar sessoes antigas no logout e troca de senha
- Definir TTL e renovar em cada acesso

```javascript
// Cookies seguros
app.use(
  session({
    secret: process.env.SESSION_SECRET,
    name: "__Host-session-id",  // Prefixo __Host para cookies seguros
    cookie: {
      httpOnly: true,    // Nao acessivel por JavaScript
      secure: true,      // Apenas HTTPS
      sameSite: "strict", // Previne CSRF
      maxAge: 3600000,   // 1 hora
    },
    resave: false,
    saveUninitialized: false,
  })
);
```

## 6. Cryptography Best Practices

### Python: Criptografia

```python
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64

# Dados em repouso: AES-GCM com Fernet (simples)
def encrypt_data(data: bytes, key: bytes) -> bytes:
    cipher = Fernet(key)
    return cipher.encrypt(data)

def decrypt_data(token: bytes, key: bytes) -> bytes:
    cipher = Fernet(key)
    return cipher.decrypt(token)

# Dados em repouso: AES-GCM direto (com Associated Data)
def encrypt_aead(data: bytes, aad: bytes, key: bytes) -> tuple[bytes, bytes]:
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, data, aad)
    return nonce, ct

def decrypt_aead(nonce: bytes, ct: bytes, aad: bytes, key: bytes) -> bytes:
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, ct, aad)

# Derivacao de chave a partir de senha (PBKDF2)
def derive_key(password: str, salt: bytes | None = None) -> tuple[bytes, bytes]:
    if salt is None:
        salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt
```

```python
# Uso correto de hash para integridade
import hashlib
import hmac

def hash_file(filepath: str) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def verify_hmac(message: bytes, key: bytes, expected_hmac: bytes) -> bool:
    computed = hmac.new(key, message, hashlib.sha256).digest()
    return hmac.compare_digest(computed, expected_hmac)
```

### JavaScript: Criptografia

```javascript
const crypto = require("crypto");

const ALGORITHM = "aes-256-gcm";
const IV_LENGTH = 12;
const TAG_LENGTH = 16;

function encrypt(text, key) {
  const iv = crypto.randomBytes(IV_LENGTH);
  const cipher = crypto.createCipheriv(ALGORITHM, Buffer.from(key, "hex"), iv);

  let encrypted = cipher.update(text, "utf8", "hex");
  encrypted += cipher.final("hex");
  const authTag = cipher.getAuthTag().toString("hex");

  return {
    encrypted,
    iv: iv.toString("hex"),
    authTag,
  };
}

function decrypt(encrypted, iv, authTag, key) {
  const decipher = crypto.createDecipheriv(
    ALGORITHM,
    Buffer.from(key, "hex"),
    Buffer.from(iv, "hex")
  );
  decipher.setAuthTag(Buffer.from(authTag, "hex"));

  let decrypted = decipher.update(encrypted, "hex", "utf8");
  decrypted += decipher.final("utf8");
  return decrypted;
}

// Hash com salt (bcrypt)
const bcrypt = require("bcrypt");
async function hashPassword(password) {
  return bcrypt.hash(password, 12);
}

// HMAC para integridade
function signMessage(message, secret) {
  return crypto
    .createHmac("sha256", secret)
    .update(message)
    .digest("hex");
}

function verifySignature(message, signature, secret) {
  const computed = signMessage(message, secret);
  return crypto.timingSafeEqual(
    Buffer.from(computed),
    Buffer.from(signature)
  );
}
```

### Algoritmos Recomendados

| Uso | Algoritmo | Observacao |
|-----|-----------|------------|
| Hash de senha | Argon2id | Preferencial, seguido de bcrypt/scrypt |
| Criptografia simetrica | AES-256-GCM | Autenticado, nonce de 12 bytes |
| Criptografia assimetrica | Curve25519 (X25519) | ECDH para troca de chaves |
| Assinatura digital | Ed25519 | Performance e seguranca |
| Hash integridade | SHA-256 / SHA-3 | Nunca MD5 ou SHA-1 |
| HMAC | HMAC-SHA256 | Para autenticacao de mensagens |
| KDF | PBKDF2 / Argon2id | Derivacao de chave a partir de senha |

## Resumo de Praticas

```python
# Checklist de Secure Coding
SECURE_CODING_CHECKLIST = {
    "Input Validation": [
        "Validar todo input contra allowlist",
        "Normalizar antes de validar (Unicode NFKC)",
        "Rejeitar dados invalidos, nunca sanitizar silenciosamente"
    ],
    "Output Encoding": [
        "Codificar para o contexto de saida (HTML, JS, URL, CSS)",
        "Usar CSP para mitigar XSS",
        "Nunca confiar em dados do banco como seguros"
    ],
    "Authentication": [
        "Usar Argon2id para hash de senhas",
        "Implementar rate limiting em login",
        "JWT com expiracao curta + refresh token",
        "MFA para acoes sensiveis"
    ],
    "Authorization": [
        "Verificar permissoes em toda requisicao",
        "Nao confiar em roles vindas do cliente",
        "Principio do menor privilegio"
    ],
    "Session Management": [
        "Sessoes armazenadas no servidor",
        "Cookies: HttpOnly, Secure, SameSite",
        "Invalidar sessoes no logout/troca de senha"
    ],
    "Cryptography": [
        "Usar algoritmos modernos (AES-GCM, Argon2, Ed25519)",
        "Nao implementar criptografia proprias",
        "Gerenciar chaves com vault/secrets manager"
    ]
}
```

## Referencias Cruzadas

- [[seguranca/owasp-top-10]] - OWASP Top 10 com exemplos
- [[seguranca/INDEX]] - Index de seguranca
- [[seguranca/secrets-management]] - Gerenciamento de chaves e secrets
- [[seguranca/prompt-injection-defense]] - Seguranca para sistemas LLM
- [[seguranca/supply-chain-security]] - Seguranca de dependencias
- [[02-software-engineering\advanced-backend-architecture]] - Arquitetura segura
- [[devops\Observabilidade]] - Logging e monitoramento