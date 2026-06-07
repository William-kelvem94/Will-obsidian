---
tags: [skills, seguranca, owasp, web-security, skills-eng]
updated: 2026-06-07
title: "OWASP Top 10 (2021)"
date: 2026-06-01
---

# OWASP Top 10 (2021)

Guia completo sobre as 10 categorias de risco de seguranca mais criticas para aplicacoes web, conforme o OWASP Top 10 atualizado em 2021. Cada secao inclui descricao, codigo vulneravel, codigo corrigido, deteccao e prevencao.

## A01: Broken Access Control

### Descricao
Falhas no controle de acesso permitem que usuarios nao autorizados acessem funcionalidades ou dados restritos. Inclui escalacao de privilegios, bypass de autorizacao e manipulacao de parametros.

### Codigo Vulneravel (Python/FastAPI)

```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/api/admin/users")
async def list_users(request: Request):
    # VULNERAVEL: confia no header X-Admin-User sem validacao
    user_id = request.headers.get("X-Admin-User", "anonymous")
    return await get_all_users()  # Qualquer um que enviar o header acessa
```

```python
# Exemplo 2: Insecure Direct Object Reference (IDOR)
@app.get("/api/invoices/{invoice_id}")
async def get_invoice(invoice_id: int):
    # VULNERAVEL: nao verifica se o usuario e dono da fatura
    invoice = db.execute("SELECT * FROM invoices WHERE id = ?", (invoice_id,))
    return invoice  # Usuario A pode ver a fatura do Usuario B
```

### Codigo Corrigido

```python
@app.get("/api/admin/users")
async def list_users(current_user: User = Depends(get_current_user)):
    if "admin" not in current_user.roles:
        raise HTTPException(status_code=403, detail="Acesso negado")
    return await get_all_users()

@app.get("/api/invoices/{invoice_id}")
async def get_invoice(invoice_id: int, current_user: User = Depends(get_current_user)):
    invoice = db.execute(
        "SELECT * FROM invoices WHERE id = ? AND user_id = ?",
        (invoice_id, current_user.id)
    ).fetchone()
    if not invoice:
        raise HTTPException(status_code=404, detail="Nao encontrado")
    return invoice
```

### Deteccao
- Testes automatizados de autorizacao
- Ferramentas: Burp Suite (autorizacao forcada), OWASP ZAP
- Code review focado em endpoints sem validacao de role/permissao

### Prevencao
- Implementar controle de acesso centralizado (decorator/middleware)
- Negar por padrao, permitir explicitamente
- Usar RBAC/ABAC com verificacao em cada endpoint
- Nunca confiar em parametros do cliente para decisoes de autorizacao

## A02: Cryptographic Failures

### Descricao
Falhas relacionadas a criptografia: dados sensiveis transitando sem TLS, senhas armazenadas sem hash adequado, uso de algoritmos fracos ou geracao insegura de numeros aleatorios.

### Codigo Vulneravel

```python
import hashlib

# VULNERAVEL: MD5 para hash de senha (fraco e rapido demais)
def store_password(password: str):
    hashed = hashlib.md5(password.encode()).hexdigest()
    db.execute("INSERT INTO users (password) VALUES (?)", (hashed,))

# VULNERAVEL: AES-ECB mode (nao esconde padroes)
from Crypto.Cipher import AES
cipher = AES.new(b"1234567890123456", AES.MODE_ECB)
```

```javascript
// VULNERAVEL: localStorage para dados sensiveis
localStorage.setItem("credit_card", "4012-8888-8888-1881");
```

### Codigo Corrigido

```python
from argon2 import PasswordHasher

# CORRETO: Argon2id para hash de senha
ph = PasswordHasher()
def store_password(password: str):
    hashed = ph.hash(password)
    db.execute("INSERT INTO users (password_hash) VALUES (?)", (hashed,))

def verify_password(password: str, stored_hash: str) -> bool:
    try:
        return ph.verify(stored_hash, password)
    except:
        return False
```

```python
# CORRETO: AES-GCM com nonce aleatorio
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
dado_cifrado = cipher.encrypt(b"dado secreto")
```

### Deteccao
- Verificar uso de HTTPS em toda comunicacao
- Scannear por algoritmos obsoletos (MD5, SHA1, DES, RC4)
- Revisar armazenamento de secrets e chaves

### Prevencao
- Usar bcrypt/argon2/scrypt para senhas
- Sempre usar TLS 1.2+ em producao
- Nao armazenar dados sensiveis desnecessariamente
- Usar criptografia autenticada (AES-GCM, ChaCha20-Poly1305)

## A03: Injection

### Descricao
Injecao ocorre quando dados nao confiaveis sao enviados a um interpretador como parte de um comando ou consulta. SQL, NoSQL, OS command, LDAP injection sao variantes.

### Codigo Vulneravel

```python
# VULNERAVEL: SQL Injection
@app.get("/api/users")
async def get_user(username: str):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return db.execute(query).fetchall()
    # Input: ' OR '1'='1  ->  retorna todos os usuarios
    # Input: '; DROP TABLE users; -- ->  perda de dados
```

```javascript
// VULNERAVEL: NoSQL Injection (MongoDB)
app.get("/api/login", async (req, res) => {
  const { username, password } = req.body;
  const user = await db.collection("users").findOne({
    username: username,
    password: password
  });
  // Input: { "username": "admin", "password": { "$ne": "" } }
  // -> Bypass de autenticacao
});
```

### Codigo Corrigido

```python
# CORRETO: Prepared statements (parametrizacao)
@app.get("/api/users")
async def get_user(username: str):
    query = "SELECT * FROM users WHERE username = ?"
    return db.execute(query, (username,)).fetchall()
```

```javascript
// CORRETO: Sanitizacao no MongoDB 3.6+
app.get("/api/login", async (req, res) => {
  const { username, password } = req.body;
  if (typeof username !== "string" || typeof password !== "string") {
    return res.status(400).json({ error: "Invalid input" });
  }
  const user = await db.collection("users").findOne({
    username: { $eq: username },
    password: { $eq: password }
  });
});
```

### Deteccao
- SAST: Semgrep, CodeQL, SonarQube
- DAST: OWASP ZAP, SQLMap
- Testes: fuzzing de parametros de entrada

### Prevencao
- Sempre usar prepared statements / parameterized queries
- Usar ORM com seguranca embutida (SQLAlchemy, Prisma)
- Validar e sanitizar todo input
- Principio do menor privilegio no banco de dados

## A04: Insecure Design

### Descricao
Riscos relacionados a falhas de design ausentes ou inadequadas. Diferente de implementacao incorreta, aqui o problema e conceitual na arquitetura.

### Exemplos de Falhas de Design

```python
# VULNERAVEL: Rate limit ausente em endpoint de login
@app.post("/api/login")
async def login(username: str, password: str):
    user = authenticate(username, password)
    if user:
        return {"token": create_token(user)}
    return {"error": "Credenciais invalidas"}
    # Ataque: brute force ilimitado de senhas
```

```python
# VULNERAVEL: Password reset sem validacao de identidade
@app.post("/api/reset-password")
async def reset_password(email: str):
    user = db.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    user.password = "nova_senha123"  # Qualquer um pode resetar
    db.commit()
    return {"message": "Senha alterada"}
```

### Codigo Corrigido

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/api/login")
@limiter.limit("5/minute")
async def login(username: str, password: str):
    user = authenticate(username, password)
    if user:
        return {"token": create_token(user)}
    return {"error": "Credenciais invalidas"}
```

```python
@app.post("/api/reset-password")
async def request_reset(email: str):
    user = db.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    if user:
        token = secrets.token_urlsafe(32)
        store_reset_token(user.id, token, expires_in=timedelta(hours=1))
        send_email(email, f"Seu token de reset: {token}")
    return {"message": "Se o email existir, voce recebera um link"}
    # Nao revela se o email existe ou nao
```

### Prevencao
- Threat modeling no inicio do projeto
- Security design review antes da implementacao
- Estabelecer security requirements claros
- Usar security patterns e reference architectures

## A05: Security Misconfiguration

### Descricao
Configuracoes incorretas de seguranca: servidores com defaults inseguros, diretorios listaveis, headers de seguranca ausentes, CORS mal configurado, debug habilitado em producao.

### Codigo Vulneravel

```python
# VULNERAVEL: Debug mode em producao, CORS aberto
app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Qualquer origin pode acessar
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

```yaml
# VULNERAVEL: Docker sem restricoes
FROM python:3.11-slim
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
# Root user, portas expostas, sem healthcheck
```

### Codigo Corrigido

```python
app = FastAPI(debug=False)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://meudominio.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)
```

```yaml
FROM python:3.11-slim
RUN useradd -m -u 1000 appuser
WORKDIR /app
COPY --chown=appuser:appuser . /app
RUN pip install --no-cache-dir -r requirements.txt
USER appuser
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8000/health || exit 1
EXPOSE 8000
CMD ["python", "app.py"]
```

### Deteccao
- Scanners de configuracao: CIS Benchmarks, Lynis
- Headers HTTP: securityheaders.com
- Infrastructure as Code scanning (tfsec, checkov)

### Prevencao
- Remover debug habilitado em producao
- Configurar headers de seguranca (HSTS, CSP, X-Frame-Options)
- Restringir CORS a origens confiaveis
- Usar containers non-root
- Automatizar verificacao de configuracao no pipeline

## A06: Vulnerable and Outdated Components

### Descricao
Uso de componentes com vulnerabilidades conhecidas: bibliotecas desatualizadas, frameworks sem patch, dependencias com CVEs publicas.

### Exemplo

```python
# requirements.txt VULNERAVEL (versoes antigas com CVEs)
Flask==1.0.0          # CVE-2023-30861
PyYAML==4.1           # CVE-2020-14343
requests==2.20.0      # CVE-2018-18074
```

### Codigo Corrigido

```python
# requirements.txt CORRETO (versoes atualizadas e fixadas)
Flask==2.3.3
PyYAML==6.0.1
requests==2.31.0
```

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
    labels:
      - "dependencies"
      - "security"
```

### Deteccao
- Dependabot alerts / GitHub Advisory Database
- `pip audit`, `npm audit`, `safety check`
- SBOM analysis com Trivy ou Grype

### Prevencao
- Manter dependencias atualizadas (Renovate, Dependabot)
- Usar SBOM para inventario de componentes
- Monitorar CVEs das dependencias
- Remover dependencias nao utilizadas

## A07: Identification and Authentication Failures

### Descricao
Falhas em mecanismos de identificacao e autenticacao: senhas fracas, ausencia de MFA, session fixation, credenciais em URL, enumeracao de usuarios.

### Codigo Vulneravel

```python
# VULNERAVEL: Mensagens de erro revelam se usuario existe
@app.post("/api/login")
async def login(username: str, password: str):
    user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    if not user:
        return {"error": "Usuario nao encontrado"}
    if not verify_password(password, user.password_hash):
        return {"error": "Senha incorreta"}
    return {"token": create_session(user.id)}
```

```python
# VULNERAVEL: Sessao sem expiracao
@app.post("/api/login")
async def login(username: str, password: str):
    user = authenticate(username, password)
    session_id = str(uuid.uuid4())
    sessions[session_id] = {"user_id": user.id}  # Sessao nunca expira
    return {"session_id": session_id}
```

### Codigo Corrigido

```python
@app.post("/api/login")
async def login(username: str, password: str):
    user = authenticate(username, password)
    if not user:
        return {"error": "Credenciais invalidas"}  # Mensagem generica
    token = create_jwt(user.id, expires_in=timedelta(hours=1))
    return {"token": token}
```

```python
from datetime import datetime, timedelta
import jwt

def create_jwt(user_id: int, expires_in: timedelta):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + expires_in,
        "iat": datetime.utcnow(),
        "jti": str(uuid.uuid4())
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
```

### Deteccao
- Testar enumeracao de usuarios via mensagens de erro
- Verificar expiracao de sessoes
- Validar politicas de senha

### Prevencao
- Mensagens de erro genericas ("Credenciais invalidas")
- Implementar MFA para acoes sensiveis
- Sessoes com expiracao e refresh token
- Bloquear apos N tentativas falhas
- Usar OAuth 2.0 / OpenID Connect quando possivel

## A08: Software and Data Integrity Failures

### Descricao
Falhas de integridade em software e dados: atualizacoes nao assinadas, pipelines CI/CD inseguros, dependencias sem verificacao de checksum, desserializacao insegura.

### Codigo Vulneravel

```python
# VULNERAVEL: Desserializacao insegura com pickle
import pickle

@app.post("/api/deserialize")
async def deserialize_data(data: bytes):
    obj = pickle.loads(data)  # Executa codigo arbitrario!
    return process(obj)
```

```python
# VULNERAVEL: Downloads sem verificacao de checksum
import requests

def download_dependency(url: str):
    response = requests.get(url)
    with open("lib.whl", "wb") as f:
        f.write(response.content)
    # Nao verifica checksum, nao verifica assinatura
```

### Codigo Corrigido

```python
# CORRETO: Usar JSON ou schemas validados
from pydantic import BaseModel

class UserData(BaseModel):
    name: str
    email: str
    age: int

@app.post("/api/deserialize")
async def deserialize_data(data: UserData):
    return process(data.dict())
```

```python
# CORRETO: Verificar checksum e assinatura
import hashlib
import requests

def download_dependency(url: str, expected_sha256: str):
    response = requests.get(url)
    computed = hashlib.sha256(response.content).hexdigest()
    if not hmac.compare_digest(computed, expected_sha256):
        raise ValueError("Checksum mismatch")
    with open("lib.whl", "wb") as f:
        f.write(response.content)
```

### Deteccao
- Verificar uso de desserializacao de tipos perigosos (pickle, yaml.load)
- Auditar pipelines CI/CD
- Revisar mecanismos de atualizacao

### Prevencao
- Assinar artefatos com cosign ou GPG
- Verificar checksums em downloads
- Usar formatos seguros para serializacao (JSON + schema validation)
- Nao usar pickle/yaml.load com dados nao confiaveis

## A09: Security Logging and Monitoring Failures

### Descricao
Ausencia de logging adequado e monitoramento que impede deteccao de incidentes, investigacao forense e resposta a incidentes.

### Codigo Vulneravel

```python
# VULNERAVEL: Sem logging de tentativas de acesso negado
@app.post("/api/admin/action")
async def admin_action(current_user: User = Depends(get_current_user)):
    if "admin" not in current_user.roles:
        raise HTTPException(status_code=403)
    # Nenhum log registrado, ataque passa despercebido
    perform_admin_action()
```

### Codigo Corrigido

```python
import structlog

logger = structlog.get_logger()

@app.post("/api/admin/action")
async def admin_action(current_user: User = Depends(get_current_user)):
    if "admin" not in current_user.roles:
        logger.warning(
            "admin_access_denied",
            user_id=current_user.id,
            ip=current_user.ip,
            action="admin_action",
            timestamp=datetime.utcnow().isoformat()
        )
        raise HTTPException(status_code=403)
    logger.info("admin_action_performed", user_id=current_user.id)
    perform_admin_action()
```

```yaml
# docker-compose com centralizacao de logs
services:
  app:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
  loki:
    image: grafana/loki:2.9.0
    ports:
      - "3100:3100"
  promtail:
    image: grafana/promtail:2.9.0
    volumes:
      - /var/log:/var/log
    command: -config.file=/etc/promtail/config.yml
```

### Deteccao
- Revisar se eventos de seguranca sao logados
- Verificar integracao com SIEM
- Testar alertas de anomalia

### Prevencao
- Logar todas as tentativas de autenticacao (sucesso e falha)
- Logar acesso negado e excessoes de seguranca
- Centralizar logs (Loki, ELK, Datadog)
- Configurar alertas para padroes anomalos
- Proteger logs contra adulteracao

## A10: Server-Side Request Forgery (SSRF)

### Descricao
SSRF ocorre quando um aplicativo busca um recurso remoto baseado em input do usuario sem validar a URL. Permite acessar recursos internos, cloud metadata e servicos nao expostos.

### Codigo Vulneravel

```python
import requests

# VULNERAVEL: Aceita URL arbitraria do usuario
@app.post("/api/fetch-image")
async def fetch_image(url: str):
    response = requests.get(url)
    # Pode acessar:
    # - http://169.254.169.254/latest/meta-data/ (AWS metadata)
    # - http://localhost:5000/ (servico interno)
    # - file:///etc/passwd (arquivos locais)
    return Response(content=response.content, media_type="image/*")
```

### Codigo Corrigido

```python
from urllib.parse import urlparse
import requests

ALLOWED_DOMAINS = ["images.unsplash.com", "img.example.com"]

@app.post("/api/fetch-image")
async def fetch_image(url: str):
    parsed = urlparse(url)
    if parsed.hostname not in ALLOWED_DOMAINS:
        raise HTTPException(status_code=400, detail="Dominio nao permitido")
    if parsed.scheme not in ("https",):
        raise HTTPException(status_code=400, detail="Apenas HTTPS permitido")
    # Bloquear IPs privados
    import ipaddress
    try:
        ip = ipaddress.ip_address(parsed.hostname)
        if ip.is_private or ip.is_loopback or ip.is_link_local:
            raise HTTPException(status_code=400, detail="IP privado nao permitido")
    except ValueError:
        pass  # Hostname, nao IP (validado na whitelist acima)
    response = requests.get(url, timeout=5)
    return Response(content=response.content, media_type="image/*")
```

```python
# CORRETO: Usar allowlist de URLs completas, nao apenas dominios
ALLOWED_URLS = [
    "https://images.unsplash.com/photo-",
    "https://img.example.com/uploads/"
]
```

### Deteccao
- Testes com payloads de SSRF (cloud metadata, localhost)
- Ferramentas: SSRFmap, Interactsh
- Code review de endpoints que aceitam URLs

### Prevencao
- Validar URL contra allowlist de dominios/IPs
- Bloquear IPs privados (127.0.0.0/8, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16)
- Usar resolvedor DNS separado para servicos internos
- Desabilitar redirecionamentos seguidos (allow_redirects=False)
- Usar uma lista de URLs completas permitidas quando possivel

## Resumo Rapido

| # | Categoria | Mitigacao Principal |
|---|-----------|---------------------|
| A01 | Broken Access Control | Validar permissoes em todo endpoint |
| A02 | Cryptographic Failures | Usar bcrypt/argon2, TLS, AES-GCM |
| A03 | Injection | Prepared statements, sanitizacao |
| A04 | Insecure Design | Threat modeling, security requirements |
| A05 | Security Misconfiguration | Hardening, headers de seguranca |
| A06 | Vulnerable Components | Dependabot, SBOM, auditoria |
| A07 | Auth Failures | MFA, sessoes com expiracao |
| A08 | Integrity Failures | Assinatura de artefatos, JSON validation |
| A09 | Logging Failures | Logs centralizados, alertas |
| A10 | SSRF | Allowlist de URLs, bloquear IPs internos |

## Referencias Cruzadas

- [[seguranca/INDEX]] - Index completo de seguranca
- [[seguranca/secure-coding]] - Praticas de codificacao segura com exemplos
- [[seguranca/supply-chain-security]] - Seguranca na cadeia de fornecedores
- [[02-software-engineering\advanced-backend-architecture]] - Arquitetura segura
- [[devops\Observabilidade]] - Logging e monitoramento
- [[SFIA-Mapping]] - Mapeamento de competencias SFIA

## Ferramentas de Deteccao

| Ferramenta | Tipo | Cobertura |
|------------|------|-----------|
| Semgrep | SAST | A01-A10 (regras customizaveis) |
| OWASP ZAP | DAST | A01-A10 |
| Dependabot | SCA | A06 |
| Trivy | Container Scan | A06, A08 |
| Checkov | IaC Scan | A05 |
| Nuclei | DAST | A01, A05, A10 |