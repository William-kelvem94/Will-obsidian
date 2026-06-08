---
title: "Segurança"
date: 2026-05-16
area: "Programação e Engenharia de Software"
tags: [conhecimento, seguranca, owasp, criptografia, auth, secure-coding, api-security]
related: ["04-Conhecimentos/07-Humanidades/Programacao/INDEX", "04-Conhecimentos/07-Humanidades/Programacao/APIs-e-Integracoes", "04-Conhecimentos/07-Humanidades/Programacao/DevOps-e-Infra"]
aliases: ["Security", "OWASP", "Secure Coding", "Cryptography", "Application Security"]
---

# Segurança

> *"Security is not a product, but a process."* — Bruce Schneier

---

## 1. OWASP Top 10 (2021)

A lista da **Open Web Application Security Project** (OWASP) é atualizada periodicamente para refletir as ameaças mais críticas em aplicações web.

### 1.1 A01 — Broken Access Control

Falhas de controle de acesso permitem que usuários ajam fora das permissões pretendidas.

**Exemplos:**
- IDOR (Insecure Direct Object Reference): `/api/users/12345` — usuário pode acessar perfil de outro
- Path traversal: `../../etc/passwd`
- Elevação de privilégio vertical (user → admin)

```python
# ERRADO — sem verificação de propriedade
@app.get("/api/orders/{order_id}")
def get_order(order_id: int):
    order = db.query(Order).get(order_id)
    return order  # qualquer um pode ver qualquer pedido

# CERTO — verifica proprietário
@app.get("/api/orders/{order_id}")
def get_order(order_id: int, user: User = Depends(get_current_user)):
    order = db.query(Order).filter(
        Order.id == order_id,
        Order.user_id == user.id  # escopo obrigatório
    ).first()
    if not order:
        raise HTTPException(status_code=404)
    return order
```

### 1.2 A02 — Cryptographic Failures

Dados sensíveis expostos por criptografia fraca ou ausente.

**Problemas comuns:**
- Tráfego HTTP (sem TLS)
- Senhas armazenadas em plaintext ou hash fraco (MD5, SHA1)
- Chaves hardcoded no código-fonte
- Certificados TLS expirados

### 1.3 A03 — Injection

Injeção de código malicioso via entrada não validada.

**Tipos de injeção:**
- **SQL Injection** — clássica, cega, out-of-band
- **NoSQL Injection** — MongoDB, Couchbase
- **Command Injection** — execução de comandos do SO
- **LDAP Injection, XPath Injection, Template Injection (SSTI)**

```python
# ERRADO — SQL Injection direta
query = f"SELECT * FROM users WHERE email = '{email}'"

# CERTO — prepared statement / ORM parameter binding
user = db.query(User).filter(User.email == email).first()

# CERTO — raw SQL com parâmetros
cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
```

```typescript
// ERRADO — NoSQL Injection
const user = await db.collection("users").findOne({
  email: req.body.email, // { "$gt": "" } retorna tudo!
});

// CERTO — validação + sanitização
import { z } from "zod";
const schema = z.object({ email: z.string().email() });
const { email } = schema.parse(req.body);
const user = await db.collection("users").findOne({ email });
```

### 1.4 A04 — Insecure Design

Falhas no design da arquitetura que criam riscos de segurança.

**Exemplos:**
- Rate limiting ausente em endpoints críticos
- Trust boundary violations (confiar em dados do client)
- Falta de mecanismos de account recovery seguros

### 1.5 A05 — Security Misconfiguration

Configurações padrão inseguras ou serviços desnecessários expostos.

**Problemas comuns:**
- Debug habilitado em produção (`DEBUG=True` no Django/Flask)
- CORS muito permissivo (`Access-Control-Allow-Origin: *`)
- Headers de segurança ausentes (HSTS, CSP, X-Frame-Options)
- Buckets S3 públicos
- Portas expostas desnecessariamente

### 1.6 A06 — Vulnerable and Outdated Components

Dependências com CVEs conhecidas.

**Mitigações:**
- SCA (Software Composition Analysis) — Dependabot, Snyk, Renovate
- Manter imagem Docker base atualizada (`docker scan`, `trivy`)
- Monitorar NVD (National Vulnerability Database)

### 1.7 A07 — Identification and Authentication Failures

Falhas na autenticação e gerenciamento de identidade.

**Exemplos:**
- Credenciais fracas (sem política de senhas)
- Enumeração de usuários (mensagens de erro diferentes para "usuário existe" vs. "senha errada")
- Session fixation ou tokens previsíveis
- Falta de MFA

### 1.8 A08 — Software and Data Integrity Failures

Falhas que comprometem a integridade de software ou dados.

**Exemplos:**
- CI/CD pipeline inseguro (sem verificação de assinatura)
- Dependências sem verificação de integrity (supply chain)
- Atualizações automáticas sem validação de origem

### 1.9 A09 — Security Logging and Monitoring Failures

Falta de logging e monitoramento que impede detecção de incidentes.

**Requisitos mínimos:**
- Log de todas as autenticações (sucesso e falha)
- Log de mudanças em dados críticos
- Log de violações de controle de acesso
- Alertas automatizados para padrões suspeitos
- Proteção contra log injection (sanitizar entradas)

### 1.10 A10 — Server-Side Request Forgery (SSRF)

Aplicação faz requisições a URLs fornecidas pelo atacante.

```python
# ERRADO — SSRF possível
url = request.form["url"]
response = requests.get(url)  # pode acessar http://169.254.169.254 (metadata AWS)

# CERTO — allowlist de URLs permitidas
ALLOWED_URLS = {"https://api.trusted.com", "https://cdn.trusted.com"}
url = request.form["url"]
parsed = urlparse(url)
if f"{parsed.scheme}://{parsed.netloc}" not in ALLOWED_URLS:
    raise HTTPException(status_code=403)
response = requests.get(url)
```

---

## 2. Autenticação

### 2.1 Armazenamento Seguro de Senhas

```python
import bcrypt

# Hash (custo 12 ≈ 250ms no hardware moderno)
senha = b"minha_senha_segura"
salt = bcrypt.gensalt(rounds=12)
hash_senha = bcrypt.hashpw(senha, salt)
# $2b$12$LJ3m4ys3Lk3m4ys3Lk3m4u...

# Verificação
if bcrypt.checkpw(senha_fornecida.encode(), hash_armazenado):
    print("Senha correta")
```

```python
import argon2

ph = argon2.PasswordHasher(
    time_cost=3,        # número de iterações
    memory_cost=65536,  # 64 MB de memória
    parallelism=4,      # threads paralelas
    hash_len=32,
    salt_len=16,
)

hash_ = ph.hash("minha_senha")
# $argon2id$v=19$m=65536,t=3,p=4$c29tZXNhbHQ$Rmd...

try:
    ph.verify(hash_, "minha_senha")
    if ph.check_needs_rehash(hash_):
        hash_ = ph.hash("minha_senha")  # rehash automático
except argon2.exceptions.VerifyMismatchError:
    print("Senha incorreta")
```

**Comparação de algoritmos de hash de senha:**

| Algoritmo | Resistência a GPU | Resistência a ASIC | Memória | Recomendado |
|-----------|-------------------|--------------------|---------|-------------|
| **bcrypt** | Boa | Baixa | Fixa (4 KB) | ✅ Sim (custo ≥ 10) |
| **scrypt** | Muito boa | Muito boa | Configurável | ✅ Sim |
| **Argon2id** | Excelente | Excelente | Configurável | ✅ **Preferido** (vencedor PHC 2015) |
| **PBKDF2** | Fraca | Fraca | Baixa | ⚠️ Apenas legado |
| MD5/SHA1 | ❌ | ❌ | Nula | ❌ Nunca usar |

### 2.2 Session Management

```python
import secrets
from datetime import datetime, timedelta

SESSION_DURATION = timedelta(hours=2)
SESSION_REFRESH = timedelta(minutes=15)

class SessionManager:
    def __init__(self, redis_client):
        self.redis = redis_client

    def create_session(self, user_id: str) -> str:
        session_id = secrets.token_urlsafe(32)
        self.redis.setex(
            f"session:{session_id}",
            int(SESSION_DURATION.total_seconds()),
            user_id,
        )
        # Armazenar também por usuário (para revogação)
        self.redis.sadd(f"user_sessions:{user_id}", session_id)
        return session_id

    def validate_session(self, session_id: str) -> str | None:
        user_id = self.redis.get(f"session:{session_id}")
        if user_id:
            # Refresh sliding expiration
            self.redis.expire(
                f"session:{session_id}",
                int(SESSION_DURATION.total_seconds()),
            )
        return user_id

    def revoke_all_sessions(self, user_id: str):
        sessions = self.redis.smembers(f"user_sessions:{user_id}")
        for session_id in sessions:
            self.redis.delete(f"session:{session_id}")
        self.redis.delete(f"user_sessions:{user_id}")
```

### 2.3 Autenticação Multifator (MFA)

```python
import pyotp
import qrcode

# Geração de chave secreta TOTP (Time-based One-Time Password)
secret = pyotp.random_base32()
# Formato: JBSWY3DPEHPK3PXP

# URI para Google Authenticator / Authy
uri = pyotp.totp.TOTP(secret).provisioning_uri(
    name="user@example.com",
    issuer_name="MyApp",
)
# otpauth://totp/MyApp:user@example.com?secret=JBSWY...&issuer=MyApp

# Gerar QR code para o usuário escanear
qrcode.make(uri).save("mfa_qr.png")

# Verificar código
totp = pyotp.TOTP(secret)
codigo = input("Digite o código do autenticador: ")
if totp.verify(codigo):
    print("✅ MFA válido!")
```

### 2.4 OAuth 2.0 e OpenID Connect

```
┌─────────┐          ┌──────────┐          ┌──────────┐
│  Client │          │   Auth   │          │ Resource │
│   App   │          │  Server  │          │  Server  │
└────┬────┘          └────┬─────┘          └────┬─────┘
     │ 1. Authorization   │                     │
     │    Request          │                     │
     ├───────────────────►│                     │
     │                    │                     │
     │ 2. Authorization   │                     │
     │    Grant (code)    │                     │
     │◄───────────────────┤                     │
     │                    │                     │
     │ 3. Access Token    │                     │
     │    Request          │                     │
     ├───────────────────►│                     │
     │                    │                     │
     │ 4. Access Token +  │                     │
     │    ID Token        │                     │
     │◄───────────────────┤                     │
     │                    │                     │
     │ 5. API Request +   │                     │
     │    Access Token    │                     │
     ├─────────────────────────────────────────►│
     │                    │                     │
     │ 6. Response        │                     │
     │◄─────────────────────────────────────────┤
```

---

## 3. Autorização

### 3.1 RBAC (Role-Based Access Control)

```python
from enum import Enum
from functools import wraps

class Role(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"
    GUEST = "guest"

ROLE_HIERARCHY = {
    Role.GUEST: 0,
    Role.USER: 1,
    Role.MANAGER: 2,
    Role.ADMIN: 3,
}

PERMISSIONS = {
    "user:read": [Role.GUEST, Role.USER, Role.MANAGER, Role.ADMIN],
    "user:write": [Role.USER, Role.MANAGER, Role.ADMIN],
    "user:delete": [Role.ADMIN],
    "billing:read": [Role.MANAGER, Role.ADMIN],
    "billing:write": [Role.ADMIN],
    "admin:all": [Role.ADMIN],
}


def require_permission(permission: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = get_current_user()
            user_role = user.role
            allowed_roles = PERMISSIONS.get(permission, [])
            if user_role not in allowed_roles:
                raise HTTPException(status_code=403, detail="Insufficient permissions")
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### 3.2 ABAC (Attribute-Based Access Control)

```python
# ABAC avalia atributos do usuário, recurso, ambiente
def check_access(user, resource, action, context):
    rules = [
        # Admins podem fazer tudo
        user.role == "admin",
        # Usuário pode editar próprio perfil
        action == "edit"
        and resource.type == "profile"
        and resource.owner_id == user.id,
        # Manager pode editar recursos do seu departamento
        user.role == "manager"
        and action == "edit"
        and resource.department == user.department,
        # Qualquer um pode ler recursos públicos
        action == "read" and resource.visibility == "public",
    ]
    return any(rules)
```

### 3.3 Policy Engines — OPA (Open Policy Agent)

```rego
# policy.rego
package app.auth

default allow = false

# Admin tem acesso total
allow {
    input.user.role == "admin"
}

# Usuário pode acessar próprio recurso
allow {
    input.method == "GET"
    input.path == input.user.id
    input.user.role == "user"
}

# Manager pode acessar recursos do seu time
allow {
    input.method == "GET"
    input.resource.team == input.user.team
    input.user.role == "manager"
}
```

```python
# Python — chamando OPA
import httpx

opa_url = "http://opa:8181/v1/data/app/auth/allow"
decision = httpx.post(
    opa_url,
    json={
        "input": {
            "user": {"id": "123", "role": "user", "team": "eng"},
            "method": "GET",
            "path": "/api/orders/456",
            "resource": {"team": "eng", "type": "order"},
        },
    },
).json()

if decision.get("result"):
    print("✅ Acesso permitido")
    return handler(request)
else:
    raise HTTPException(status_code=403)
```

---

## 4. Criptografia

### 4.1 Hash Functions (Unidirecionais)

```python
import hashlib

# ❌ NUNCA use para senhas
md5 = hashlib.md5(b"dados").hexdigest()
sha1 = hashlib.sha1(b"dados").hexdigest()

# ✅ Para integridade (checksums, assinaturas)
sha256 = hashlib.sha256(b"dados").hexdigest()
sha3_256 = hashlib.sha3_256(b"dados").hexdigest()
blake2b = hashlib.blake2b(b"dados", digest_size=32).hexdigest()

# HMAC (Hash-based Message Authentication Code)
import hmac
key = b"chave-secreta"
message = b"mensagem"
hmac_digest = hmac.new(key, message, hashlib.sha256).hexdigest()
```

### 4.2 Criptografia Simétrica — AES

```python
from cryptography.fernet import Fernet

# Geração de chave (256 bits)
key = Fernet.generate_key()
cipher = Fernet(key)

# Criptografar
token = cipher.encrypt(b"Mensagem secreta")
# gAAAAABm...

# Descriptografar
plaintext = cipher.decrypt(token)
print(plaintext.decode())  # Mensagem secreta
```

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# AES-256-GCM (modo autenticado — preferido)
key = os.urandom(32)  # 256 bits
nonce = os.urandom(12)  # 96 bits recomendado para GCM
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
ciphertext, tag = cipher.encrypt_and_digest(b"Mensagem secreta")
# ciphertext + tag verificam autenticidade

# AES-256-CBC (apenas confidencialidade, precisa de HMAC)
iv = os.urandom(16)
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
ciphertext = cipher.encrypt(pad(b"Mensagem secreta", AES.block_size))
```

### 4.3 Criptografia Assimétrica — RSA e ECC

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Geração de par de chaves RSA (2048 bits mínimo)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()

# Criptografar com chave pública
message = b"Mensagem secreta"
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

# Descriptografar com chave privada
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)
```

```python
from cryptography.hazmat.primitives.asymmetric import ec

# ECDSA (Elliptic Curve Digital Signature Algorithm)
private_key = ec.generate_private_key(ec.SECP256R1())  # P-256
public_key = private_key.public_key()

# Assinar
message = b"Mensagem importante"
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256()),
)

# Verificar
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("✅ Assinatura válida")
except:
    print("❌ Assinatura inválida")
```

**Comparação RSA vs ECC:**

| Parâmetro | RSA-2048 | ECC P-256 |
|-----------|----------|-----------|
| Tamanho da chave | 2048 bits | 256 bits |
| Segurança equivalente | 112 bits | 128 bits |
| Performance (assinatura) | Lenta | Rápida |
| Performance (verificação) | Rápida | Mais rápida |
| Tamanho da assinatura | 256 bytes | 64 bytes |
| Resistência quântica | ❌ Não | ❌ Não |

### 4.4 TLS (Transport Layer Security)

```yaml
# Configuração segura nginx
server {
    listen 443 ssl http2;
    server_name api.mydomain.com;

    # Certificados
    ssl_certificate     /etc/ssl/certs/fullchain.pem;
    ssl_certificate_key /etc/ssl/private/privkey.pem;

    # TLS 1.3 + 1.2 apenas (sem 1.1 ou 1.0)
    ssl_protocols TLSv1.2 TLSv1.3;

    # Cipher suites seguras
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers on;

    # HSTS (HTTP Strict Transport Security)
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload";

    # OCSP Stapling
    ssl_stapling on;
    ssl_stapling_verify on;
    resolver 8.8.8.8 8.8.4.4 valid=300s;
}
```

**Cipher suites recomendadas (2026):**
- TLS_AES_128_GCM_SHA256 (TLS 1.3)
- TLS_AES_256_GCM_SHA384 (TLS 1.3)
- ECDHE-RSA-AES128-GCM-SHA256 (TLS 1.2)
- ECDHE-ECDSA-AES128-GCM-SHA256 (TLS 1.2)

---

## 5. Secure Coding

### 5.1 Input Validation

```python
from pydantic import BaseModel, EmailStr, Field, validator
import re

class UserInput(BaseModel):
    username: str = Field(min_length=3, max_length=30, pattern=r"^[a-zA-Z0-9_]+$")
    email: EmailStr
    age: int = Field(ge=0, le=150)

    @validator("username")
    def no_sql_injection(cls, v):
        # Sanitização adicional
        if ";" in v or "--" in v:
            raise ValueError("Invalid characters")
        return v


# Validação manual (sem framework)
def sanitize_filename(filename: str) -> str:
    """Remove path traversal e caracteres perigosos."""
    basename = os.path.basename(filename)
    clean = re.sub(r"[^\w\-.]", "", basename)
    if not clean:
        raise ValueError("Invalid filename")
    return clean
```

### 5.2 Output Encoding (Prevenção de XSS)

```python
import html

user_input = '<script>alert("xss")</script>'
safe_output = html.escape(user_input, quote=True)
# &lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;

# Contextos de encoding:
# HTML Body: html.escape()
# HTML Attribute: html.escape() + aspas
# JavaScript: json.dumps() + escaping
# CSS: escaping específico
# URL: urllib.parse.quote()
```

```typescript
// React já faz escape automático
const MyComponent = ({ userInput }: { userInput: string }) => {
  // ✅ React escapa por padrão
  return <div>{userInput}</div>;
};

// Apenas quando necessário — dangerouslySetInnerHTML
const sanitized = DOMPurify.sanitize(userInput);
return <div dangerouslySetInnerHTML={{ __html: sanitized }} />;
```

### 5.3 Prepared Statements (SQL Injection Prevention)

```python
# ✅ ORM (SQLAlchemy)
user = session.query(User).filter(User.email == email).first()

# ✅ Raw SQL com placeholders
cursor.execute(
    "SELECT * FROM users WHERE email = %s AND active = %s",
    (email, True),
)

# ❌ String formatting
cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")

# ✅ Django ORM
User.objects.filter(email=email, active=True).first()
```

### 5.4 CSRF Protection

```python
# Flask-WTF
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()
csrf.init_app(app)

@app.route("/transfer", methods=["POST"])
@csrf.exempt  # apenas para webhooks com verificação alternativa
def transfer():
    ...

# Django (built-in)
# settings.py
MIDDLEWARE = [
    "django.middleware.csrf.CsrfViewMiddleware",
    ...
]

# Template
<form method="post">
    {% csrf_token %}
    <input name="amount" type="text">
</form>
```

### 5.5 HTTP Security Headers

```python
# FastAPI — middleware de segurança
from starlette.middleware.base import BaseHTTPMiddleware

SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "X-XSS-Protection": "0",  # desabilitar legado (modern browsers ignoram)
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
    "Content-Security-Policy": "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'",
}

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        for header, value in SECURITY_HEADERS.items():
            response.headers[header] = value
        return response
```

---

## 6. Secret Management

### 6.1 Boas Práticas

```python
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # ✅ Nunca hardcoded
    database_url: str
    redis_url: str = "redis://localhost:6379/0"
    jwt_secret: str
    aws_access_key_id: str | None = None
    aws_secret_access_key: str | None = None
    log_level: str = "INFO"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()

# .env (nunca commitado!)
# DATABASE_URL=postgres://user:pass@prod:5432/db
# JWT_SECRET=super-secret-key-123
```

### 6.2 HashiCorp Vault

```python
import hvac

client = hvac.Client(url="https://vault.example.com:8200")
client.token = os.environ["VAULT_TOKEN"]

# Ler segredo
secret = client.secrets.kv.v2.read_secret_version(
    path="prod/api",
    mount_point="secrets",
)
db_password = secret["data"]["data"]["database_password"]

# Gerar credenciais dinâmicas (PostgreSQL)
creds = client.secrets.database.generate_credentials(
    name="readonly-role",
    mount_point="database",
)
# creds expiram automaticamente após TTL configurado
```

### 6.3 AWS Secrets Manager

```python
import boto3
from botocore.exceptions import ClientError

def get_secret(secret_name: str) -> dict:
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager")

    try:
        response = client.get_secret_value(SecretId=secret_name)
        return json.loads(response["SecretString"])
    except ClientError as e:
        raise
```

---

## 7. Dependências e Supply Chain

### 7.1 Software Composition Analysis (SCA)

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
    open-pull-requests-limit: 10
    labels:
      - "dependencies"
      - "security"
    allow:
      - dependency-type: "direct"

  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    groups:
      react:
        patterns:
          - "react*"
          - "@types/react*"
```

```bash
# Trivy — scanning de containers e dependências
trivy image myapp:latest
trivy fs --scanners vuln,secret,misconfig .
trivy repo https://github.com/org/repo

# Snyk
snyk test --all-projects
snyk monitor  # monitoramento contínuo

# pip-audit (Python)
pip-audit --requirement requirements.txt
```

### 7.2 Software Bill of Materials (SBOM)

```bash
# Gerar SBOM com CycloneDX
cyclonedx-py requirements.txt -o sbom.xml
cyclonedx-npm --output sbom.json

# Verificar assinatura de pacotes
cosign verify-blob --signature sbom.sig --key cosign.pub sbom.json
```

### 7.3 CI/CD Security

```yaml
# GitHub Actions — security scanning
name: Security Scan
on: [push]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: SAST (Semgrep)
        uses: semgrep/semgrep-action@v1
        with:
          config: p/default

      - name: SCA (Snyk)
        uses: snyk/actions/python@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          args: --severity-threshold=high

      - name: Trivy
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: fs
          severity: HIGH,CRITICAL
```

---

## 8. API Security

### 8.1 JWT (JSON Web Tokens)

```python
from datetime import datetime, timedelta
import jwt

SECRET = settings.jwt_secret
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = timedelta(minutes=30)
REFRESH_TOKEN_EXPIRE = timedelta(days=7)


def create_access_token(user_id: str, roles: list[str]) -> str:
    payload = {
        "sub": user_id,
        "roles": roles,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + ACCESS_TOKEN_EXPIRE,
        "type": "access",
        "jti": secrets.token_hex(16),  # unique token ID
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)


def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        if payload.get("type") != "access":
            raise HTTPException(status_code=401, detail="Invalid token type")
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


def create_refresh_token(user_id: str) -> str:
    payload = {
        "sub": user_id,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + REFRESH_TOKEN_EXPIRE,
        "type": "refresh",
        "jti": secrets.token_hex(16),
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)
```

### 8.2 Rate Limiting

```python
# FastAPI + slowapi
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)


@app.get("/api/public")
@limiter.limit("100/minute")
def public_endpoint(request: Request):
    return {"message": "public"}


@app.post("/api/auth/login")
@limiter.limit("5/minute")  # mitigar brute force
def login(request: Request):
    ...


# Rate limiting por usuário autenticado
def get_user_key(request: Request):
    return request.headers.get("X-API-Key", get_remote_address(request))


@limiter.limit("1000/hour", key_func=get_user_key)
@app.get("/api/private")
def private_endpoint(request: Request):
    ...
```

### 8.3 CORS (Cross-Origin Resource Sharing)

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://app.mydomain.com",
        "https://admin.mydomain.com",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
    expose_headers=["X-Request-Id"],
    max_age=3600,
)
```

### 8.4 API Keys Management

```python
import secrets
import hashlib

class APIKeyManager:
    def __init__(self, db):
        self.db = db

    def generate_api_key(self, user_id: str, name: str) -> str:
        """Generate API key and store hash."""
        # Prefixo para identificar o tipo de chave
        prefix = "sk_live_" if user_id == "prod" else "sk_test_"
        raw_key = prefix + secrets.token_urlsafe(48)
        key_hash = hashlib.sha256(raw_key.encode()).hexdigest()

        self.db.execute(
            "INSERT INTO api_keys (user_id, name, key_hash, created_at) VALUES (%s, %s, %s, NOW())",
            (user_id, name, key_hash),
        )
        return raw_key  # mostrar apenas uma vez!

    def validate_api_key(self, raw_key: str) -> str | None:
        key_hash = hashlib.sha256(raw_key.encode()).hexdigest()
        result = self.db.fetchone(
            "SELECT user_id FROM api_keys WHERE key_hash = %s AND revoked = FALSE",
            (key_hash,),
        )
        return result["user_id"] if result else None
```

### 8.5 IDOR Prevention Checklist

- [ ] Usuário só acessa recursos que possui
- [ ] UUIDs em vez de IDs sequenciais ( `/api/users/550e8400-e29b-41d4-a716-446655440000` )
- [ ] Autorização em nível de dado, não apenas de rota
- [ ] Testes de segurança automatizados para cada endpoint
- [ ] Log de todas as tentativas de acesso negado

---

## Referências

- OWASP Foundation. (2021). *OWASP Top 10 — 2021*. https://owasp.org/Top10/
- Howard, M. & Lipner, S. (2006). *The Security Development Lifecycle*. Microsoft Press.
- Stuttard, D. & Pinto, M. (2011). *The Web Application Hacker's Handbook* (2ª ed.). Wiley.
- Ferguson, N., Schneier, B. & Kohno, T. (2010). *Cryptography Engineering*. Wiley.
- Ylonen, T. & Lonvick, C. (2006). *The Secure Shell (SSH) Protocol Architecture*. RFC 4251.
- NIST. (2023). *NIST SP 800-63B: Digital Identity Guidelines — Authentication and Lifecycle Management*.
- OWASP Cheat Sheet Series — https://cheatsheetseries.owasp.org/
- JWT.io — https://jwt.io/

---

## Conexões

- [[04-Conhecimentos/07-Humanidades/Programacao/INDEX]] — Índice geral da área de programação
- [[04-Conhecimentos/07-Humanidades/Programacao/APIs-e-Integracoes]] — Segurança em APIs e integrações
- [[04-Conhecimentos/07-Humanidades/Programacao/DevOps-e-Infra]] — Segurança em infraestrutura e CI/CD
- [[04-Conhecimentos/07-Humanidades/Direito-Digital/GDPR-e-Privacidade]] — Privacidade e proteção de dados
- [[04-Conhecimentos/07-Humanidades/Etica/Etica-de-IA-e-Alinhamento]] — Implicações éticas de segurança

---

*"The only secure system is the one that is powered off, cast in a block of concrete and sealed in a lead-lined room with armed guards."* — Gene Spafford
