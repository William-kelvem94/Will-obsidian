---
tags: [skills, seguranca, secrets, vault, env, skills-eng]
updated: 2026-06-13
title: "Secrets Management"
date: 2026-06-01
---

# Secrets Management

Gerenciamento seguro de secrets: senhas, chaves de API, tokens de autenticacao, certificados e qualquer informacao sensivel necessaria para operacao de sistemas.

## Por que Gerenciar Secrets?

Vazamento de secrets e uma das causas mais comuns de incidentes de seguranca. Secrets expostos em repositorios git, variaveis de ambiente em texto claro ou logs podem levar a acesso nao autorizado a sistemas criticos.

```python
# NUNCA faça isso:
API_KEY = "sk-1234567890abcdef"
DB_PASSWORD = "minhasenha123"
SECRET_KEY = "chave-secreta"
```

## Ambiente de Desenvolvimento: .env Files

### Estrutura Basica

```bash
# .env (NUNCA commitar este arquivo)
# Adicione .env ao .gitignore!
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
REDIS_URL=redis://:password@localhost:6379/0
JWT_SECRET_KEY=super-secret-key-change-in-production
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
SENTRY_DSN=https://examplePublicKey@o0.ingest.sentry.io/0
```

```bash
# .env.example (commitar este arquivo, sem valores reais)
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
REDIS_URL=redis://:password@localhost:6379/0
JWT_SECRET_KEY=change-me-in-production
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
OPENAI_API_KEY=
SENTRY_DSN=
```

### Python: Carregando .env

```python
# .env file loading (desenvolvimento apenas)
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega variaveis do .env

DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL nao configurada")

# Validacao com Pydantic Settings
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    redis_url: str
    jwt_secret_key: str
    aws_access_key_id: str = ""
    aws_secret_access_key: str = ""
    openai_api_key: str = ""
    sentry_dsn: str = ""
    environment: str = "development"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
print(f"Ambiente: {settings.environment}")
```

### JavaScript: Carregando .env

```javascript
// Usando dotenv (Node.js)
require("dotenv").config();

const config = {
  databaseUrl: process.env.DATABASE_URL,
  jwtSecret: process.env.JWT_SECRET_KEY,
  openaiApiKey: process.env.OPENAI_API_KEY,
};

// Validacao com Zod
const z = require("zod");

const ConfigSchema = z.object({
  DATABASE_URL: z.string().url(),
  JWT_SECRET_KEY: z.string().min(32),
  OPENAI_API_KEY: z.string().startsWith("sk-"),
  NODE_ENV: z.enum(["development", "staging", "production"]),
  LOG_LEVEL: z.enum(["debug", "info", "warn", "error"]).default("info"),
});

const parsed = ConfigSchema.safeParse(process.env);
if (!parsed.success) {
  console.error("Configuracao invalida:", parsed.error.format());
  process.exit(1);
}

module.exports = parsed.data;
```

### .gitignore para Secrets

```gitignore
# Secrets
.env
.env.local
.env.*.local
*.pem
*.key
*.keystore
service-account.json
credentials.json
secrets/
!secrets/.gitkeep
```

## Git Secrets Prevention

### git-secrets

```bash
# Instalar git-secrets
# winget install --id git-secrets -e

# Configurar no repositorio
git secrets --install
git secrets --register-aws  # Adiciona padroes AWS

# Adicionar padroes customizados
git secrets --add 'sk-[a-zA-Z0-9]{20,}'  # OpenAI keys
git secrets --add 'AKIA[0-9A-Z]{16}'     # AWS Access Key
git secrets --add '-----BEGIN.*PRIVATE.*KEY-----'  # Private keys

# Escanear historico
git secrets --scan-history

# Pre-commit hook (instalado automaticamente com --install)
# Bloqueia commits com secrets detectados
```

### truffleHog

```bash
# Scan rapido de repositorio
trufflehog git file://. --results=verified

# Scan de branch especifica
trufflehog git file://. --branch=main --only-verified

# Scan de organizacao GitHub
trufflehog github --org=my-org --token=$GITHUB_TOKEN
```

### git-crypt

```bash
# Instalar git-crypt
# winget install git-crypt

# Inicializar no repositorio
git-crypt init

# Adicionar GPG key de um usuario
git-crypt add-gpg-user USER-ID

# Criar .gitattributes para arquivos criptografados
echo "secrets/* filter=git-crypt diff=git-crypt" > .gitattributes
echo ".env filter=git-crypt diff=git-crypt" >> .gitattributes
echo "config/production.yml filter=git-crypt diff=git-crypt" >> .gitattributes

# Bloquear/desbloquear
git-crypt lock
git-crypt unlock
```

```yaml
# .gitattributes para git-crypt
secrets/** filter=git-crypt diff=git-crypt
.env filter=git-crypt diff=git-crypt
*.pem filter=git-crypt diff=git-crypt
config/**/*.yml filter=git-crypt diff=git-crypt
```

## Hashicorp Vault

### Conceitos Principais

- **Secrets Engine**: Backend que armazena ou gera secrets (KV, AWS, Database)
- **Path**: Rota para acessar secrets (`secret/data/api-keys`)
- **Policy**: Regras de acesso baseadas em paths
- **Token**: Metodo de autenticacao principal
- **Lease**: Tempo de vida de um secret, com renovacao automatica

### Docker Compose para Vault

```yaml
# docker-compose.vault.yml
version: "3.8"
services:
  vault:
    image: hashicorp/vault:1.16
    container_name: vault
    cap_add:
      - IPC_LOCK
    environment:
      VAULT_DEV_ROOT_TOKEN_ID: root-token-dev-only
      VAULT_DEV_LISTEN_ADDRESS: 0.0.0.0:8200
    ports:
      - "8200:8200"
    volumes:
      - vault-data:/vault/file
    command: server -dev -dev-listen-address=0.0.0.0:8200

volumes:
  vault-data:
```

### Python: Integracao com Vault

```python
import hvac
import os

class VaultClient:
    def __init__(self, url: str, token: str):
        self.client = hvac.Client(url=url, token=token)

    def read_secret(self, path: str, key: str) -> str | None:
        try:
            response = self.client.secrets.kv.v2.read_secret_version(
                path=path,
                mount_point="secret"
            )
            return response["data"]["data"].get(key)
        except hvac.exceptions.InvalidPath:
            return None
        except hvac.exceptions.Forbidden:
            print(f"Acesso negado ao path: {path}")
            return None

    def write_secret(self, path: str, data: dict):
        self.client.secrets.kv.v2.create_or_update_secret(
            path=path,
            secret=data,
            mount_point="secret"
        )

    def rotate_secret(self, path: str, key: str, new_value: str):
        """Rotaciona um secret mantendo versoes anteriores."""
        self.client.secrets.kv.v2.create_or_update_secret(
            path=path,
            secret={key: new_value},
            mount_point="secret"
        )

# Uso
vault = VaultClient(
    url=os.getenv("VAULT_ADDR", "http://localhost:8200"),
    token=os.getenv("VAULT_TOKEN", "root-token-dev-only")
)

# Escrever secret
vault.write_secret("api-keys", {
    "openai": "sk-proj-xxxxxxxx",
    "anthropic": "sk-ant-xxxxxxxx",
    "github_token": "ghp_xxxxxxxx"
})

# Ler secret
openai_key = vault.read_secret("api-keys", "openai")
print(f"OpenAI Key: {openai_key[:10]}...")
```

### Dynamic Secrets (Banco de Dados)

```python
class VaultDatabaseClient:
    def __init__(self, vault_url: str, vault_token: str):
        self.vault = hvac.Client(url=vault_url, token=vault_token)

    def get_database_credentials(self, role_name: str, mount_point: str = "database") -> dict:
        """Gera credenciais de banco de dados sob demanda com TTL."""
        response = self.vault.secrets.database.generate_credentials(
            name=role_name,
            mount_point=mount_point
        )
        return {
            "username": response["data"]["username"],
            "password": response["data"]["password"],
            "lease_id": response["lease_id"],
            "lease_duration": response.get("lease_duration", 3600)
        }

    def renew_lease(self, lease_id: str) -> dict:
        """Renova lease de credenciais."""
        return self.vault.sys.renew_lease(lease_id=lease_id)

# Uso: credenciais temporarias para cada conexao
db_creds = vault_client.get_database_credentials("app-role")
engine = create_engine(
    f"postgresql://{db_creds['username']}:{db_creds['password']}@db:5432/mydb"
)
```

### Policies de Vault

```hcl
# policy-app.hcl - Politica para aplicacao
path "secret/data/api-keys/*" {
  capabilities = ["read"]
}
path "secret/data/database/*" {
  capabilities = ["read"]
}
path "database/creds/app-role" {
  capabilities = ["read"]
}

# policy-admin.hcl - Politica para admin
path "secret/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}
path "sys/*" {
  capabilities = ["read", "update"]
}

# policy-ci.hcl - Politica para CI/CD (apenas escrita)
path "secret/data/ci/*" {
  capabilities = ["create", "update"]
}
```

## AWS Secrets Manager

### Python: AWS Secrets Manager

```python
import boto3
from botocore.exceptions import ClientError
import json

class AWSSecretsManager:
    def __init__(self, region_name: str = "us-east-1"):
        self.client = boto3.client(
            "secretsmanager",
            region_name=region_name
        )

    def get_secret(self, secret_name: str) -> dict:
        try:
            response = self.client.get_secret_value(SecretId=secret_name)
            if "SecretString" in response:
                return json.loads(response["SecretString"])
            return json.loads(response["SecretBinary"].decode("utf-8"))
        except ClientError as e:
            if e.response["Error"]["Code"] == "ResourceNotFoundException":
                print(f"Secret {secret_name} nao encontrado")
            elif e.response["Error"]["Code"] == "AccessDeniedException":
                print(f"Acesso negado ao secret {secret_name}")
            raise

    def create_secret(self, name: str, secret_data: dict, description: str = ""):
        self.client.create_secret(
            Name=name,
            SecretString=json.dumps(secret_data),
            Description=description,
            Tags=[
                {"Key": "Environment", "Value": "production"},
                {"Key": "ManagedBy", "Value": "terraform"},
            ]
        )

    def rotate_secret(self, secret_name: str):
        """Forca rotacao imediata do secret."""
        self.client.rotate_secret(SecretId=secret_name)

    def list_secrets(self, filters: list[dict] | None = None) -> list:
        paginator = self.client.get_paginator("list_secrets")
        secrets = []
        for page in paginator.paginate(Filters=filters or []):
            secrets.extend(page["SecretList"])
        return secrets

# Uso
secrets = AWSSecretsManager()
db_creds = secrets.get_secret("prod/database/primary")
print(f"Conectando como {db_creds['username']} ao {db_creds['host']}")
```

### Terraform: AWS Secrets Manager

```hcl
resource "aws_secretsmanager_secret" "db_credentials" {
  name        = "prod/database/primary"
  description = "Database credentials for production"
  rotation_rules {
    automatically_after_days = 30
  }
  tags = {
    Environment = "production"
    ManagedBy   = "terraform"
  }
}

resource "aws_secretsmanager_secret_version" "db_credentials" {
  secret_id = aws_secretsmanager_secret.db_credentials.id
  secret_string = jsonencode({
    username = "app_user"
    password = random_password.db_password.result
    host     = aws_db_instance.main.address
    port     = 5432
    database = "mydb"
  })
}
```

## Kubernetes Secrets

### Criacao de Secrets

```yaml
# secret.yaml - Manifesto Kubernetes
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
  namespace: production
type: Opaque
stringData:
  DATABASE_URL: postgresql://user:password@db:5432/mydb
  REDIS_URL: redis://:password@redis:6379/0
  JWT_SECRET_KEY: supersecretkey12345678901234567890
---
apiVersion: v1
kind: Pod
metadata:
  name: myapp
spec:
  containers:
    - name: app
      image: myapp:latest
      envFrom:
        - secretRef:
            name: app-secrets
      env:
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-credentials
              key: password
  volumes:
    - name: certs
      secret:
        secretName: tls-certs
```

### External Secrets Operator (ESO)

```yaml
# Sincroniza secrets do AWS Secrets Manager para o Kubernetes
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: app-secrets
spec:
  refreshInterval: "1h"
  secretStoreRef:
    name: aws-secrets-store
    kind: SecretStore
  target:
    name: app-secrets
    creationPolicy: Owner
  data:
    - secretKey: DATABASE_URL
      remoteRef:
        key: prod/database/primary
        property: url
    - secretKey: JWT_SECRET_KEY
      remoteRef:
        key: prod/jwt/secret
        property: key
```

## Melhores Praticas

### Ciclo de Vida de Secrets

```python
class SecretLifecycle:
    """
    Ciclo de vida completo de um secret:
    1. Criacao: geracao aleatoria, segura
    2. Armazenamento: vault, encrypted, nunca em codigo
    3. Distribuicao: injecao segura, nunca em logs
    4. Uso: minimo privilegio, lease com TTL
    5. Rotacao: periodica ou sob demanda
    6. Revogacao: imediata em caso de comprometimento
    7. Destruicao: segura, sem possibilidade de recovery
    """

    @staticmethod
    def generate_api_key(length: int = 32) -> str:
        """Gera chave de API segura com prefixo identificavel."""
        import secrets
        import string
        alphabet = string.ascii_letters + string.digits
        key = "".join(secrets.choice(alphabet) for _ in range(length))
        return f"sk_{key}"  # Prefixo identificavel

    @staticmethod
    def mask_secret(secret: str, visible_chars: int = 4) -> str:
        """Mascara secret para exibicao segura."""
        if len(secret) <= visible_chars:
            return "****"
        return secret[:visible_chars] + "****"

# Uso
new_key = SecretLifecycle.generate_api_key()
print(f"Chave gerada: {SecretLifecycle.mask_secret(new_key)}")
```

### Checklist de Secrets Management

```python
SECRETS_CHECKLIST = {
    "Storage": [
        "Nunca armazenar secrets em codigo fonte",
        "Nunca commitar .env com valores reais",
        "Usar vault centralizado (Hashicorp, AWS Secrets Manager)",
        "Criptografar secrets em repouso e em transito"
    ],
    "Access": [
        "Principio do menor privilegio",
        "Rotacao de credentials periodica",
        "Auditar acesso a secrets",
        "Revogar acesso imediatamente quando necessario"
    ],
    "Distribution": [
        "Injetar via ambiente, nunca em codigo",
        "Usar External Secrets Operator no Kubernetes",
        "Nunca logar secrets",
        "Nao expor secrets em paginas de erro"
    ],
    "Detection": [
        "Pre-commit hooks (git-secrets, truffleHog)",
        "Scan de repositorios regularmente",
        "Monitoramento de acesso a secrets no vault",
        "Alertas de secrets expostos"
    ],
    "Recovery": [
        "Backup criptografado dos vaults",
        "Disaster recovery plan para secrets",
        "Teste de restauracao periodico",
        "Documentacao de procedimentos de emergencia"
    ]
}
```

### Prevencao de Vazamento em Logs

```python
import re
import logging

class SecretFilter(logging.Filter):
    """Filtro que mascara secrets em logs."""
    PATTERNS = [
        (r"sk-[a-zA-Z0-9]{20,}", "sk-****"),      # OpenAI keys
        (r"ghp_[a-zA-Z0-9]{36}", "ghp_****"),      # GitHub tokens
        (r"AKIA[0-9A-Z]{16}", "AKIA****"),         # AWS keys
        (r"-----BEGIN.*PRIVATE.*KEY-----", "****KEY****"),  # Private keys
    ]

    def filter(self, record: logging.LogRecord) -> bool:
        if isinstance(record.msg, str):
            for pattern, replacement in self.PATTERNS:
                record.msg = re.sub(pattern, replacement, record.msg)
        return True

# Configuracao
logging.basicConfig(level=logging.INFO)
logging.getLogger().addFilter(SecretFilter())
```

## Comparacao de Solucoes

| Solucao | Caso de Uso | Vantagens | Limitacoes |
|---------|-------------|-----------|------------|
| .env files | Desenvolvimento local | Simples, rapido | Nao escalavel, sem auditoria |
| git-crypt | Equipes pequenas | Integrado ao Git | Chave compartilhada |
| Hashicorp Vault | Producao, multi-servico | Dynamic secrets, audit, policies | Complexo de operar |
| AWS Secrets Manager | AWS native | Rotacao automatica, integracao | Vendor lock-in |
| Kubernetes Secrets | K8s workloads | Nativo do K8s | Base64 (nao criptografado por padrao) |
| SOPS (Mozilla) | GitOps, IaC | Arquivos criptografados no Git | Gerenciamento de chaves |

## Referencias Cruzadas

- [[seguranca/secure-coding]] - Praticas de codificacao segura
- [[seguranca/supply-chain-security]] - Seguranca na cadeia de suprimentos
- [[seguranca/INDEX]] - Index de seguranca
- [[devops/ci-cd/github-actions]] - CI/CD com secrets
- [[devops/ci-cd/INDEX]] - Pipelines CI/CD
- [[SFIA-Mapping]] - Mapeamento SFIA