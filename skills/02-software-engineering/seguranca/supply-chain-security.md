---
tags: [skills, seguranca, supply-chain, sbom, dependencies, skills-eng]
updated: 2026-06-05
title: "Supply Chain Security"
date: 2026-06-01
---

# Supply Chain Security

Seguranca na cadeia de suprimentos de software: gerenciamento de dependencias, SBOM, assinatura de artefatos e ferramentas de automatizacao como Dependabot e Renovate.

## Introducao

Ataques a cadeia de suprimentos de software tem crescido significativamente. Exemplos notaveis incluem o ataque ao SolarWinds (2020), dependency confusion em pacotes npm/pip e a descoberta de malware em bibliotecas amplamente utilizadas.

```python
# Exemplo: dependency confusion attack
# Um atacante publica um pacote com o mesmo nome de um pacote interno
# no registro publico (PyPI, npm). O gerenciador de pacotes prioriza
# o registro publico se nao configurado corretamente.

# requirements.txt vulneravel
minha-biblioteca-interna>=1.0.0
# Se "minha-biblioteca-interna" nao existir no PyPI mas existir
# em um registro privado, um atacante pode publicar no PyPI
```

## Dependency Management

### Python: Gerenciamento de Dependencias

```python
# requirements.txt - Fixar versoes exatas em producao
flask==2.3.3
sqlalchemy==2.0.23
requests==2.31.0
pydantic==2.5.0
cryptography==41.0.7

# requirements-dev.txt - Dependencias de desenvolvimento separadas
-r requirements.txt
pytest==7.4.3
pytest-cov==4.1.0
bandit==1.7.5
safety==2.4.0b1
```

```python
# Uso de pip-audit para verificar vulnerabilidades
# pip install pip-audit
# pip-audit --requirement requirements.txt
# Output: No known vulnerabilities found
```

```toml
# pyproject.toml moderno com hashes bloqueadas
[project]
name = "myapp"
version = "1.0.0"
dependencies = [
    "flask>=2.3.0",
    "requests>=2.31.0",
]

[tool.pdm.dev-dependencies]
dev = [
    "pytest>=7.4",
]

[tool.pdm.lock]
# Gera lockfile com hashes (pdm.lock)
# Equivalente ao poetry.lock
```

```bash
# Comandos uteis para auditoria
pip list --outdated              # Lista pacotes desatualizados
pip-audit --requirement requirements.txt  # Scaneia CVEs
safety check -r requirements.txt         # Safety DB scan
pipenv check                              # Pipenv audit
```

### JavaScript: Gerenciamento de Dependencias

```json
{
  "name": "myapp",
  "version": "1.0.0",
  "scripts": {
    "audit": "npm audit",
    "outdated": "npm outdated",
    "snyk-test": "snyk test"
  },
  "dependencies": {
    "next": "14.1.0",
    "react": "^18.2.0",
    "zod": "^3.22.0"
  },
  "devDependencies": {
    "typescript": "^5.3.0",
    "eslint": "^8.56.0"
  }
}
```

```bash
# Auditoria de seguranca npm
npm audit                       # Lista vulnerabilidades
npm audit --audit-level=high    # Apenas alta/critica
npm audit fix                   # Corrige automaticamente
npm ls --depth=0                # Lista dependencias diretas
npm ls --all                    # Arvore completa de dependencias
```

```jsonc
// .npmrc configuracao segura
{
  "audit": true,
  "audit-level": "high",
  "fund": false,
  "save-exact": true,
  "engine-strict": true,
  "ignore-scripts": false
}
```

## Software Bill of Materials (SBOM)

SBOM e um inventario formal de todos os componentes que compoem um software: bibliotecas, ferramentas, versoes e suas relacoes.

### Formatos de SBOM

| Formato | Padrao | Descricao |
|---------|--------|-----------|
| SPDX | ISO/IEC 5962 | Formato legivel por humanos e maquinas |
| CycloneDX | OWASP | Focado em seguranca, amplamente adotado |
| SWID | ISO/IEC 19770 | Tags de identificacao de software |

### Geracao de SBOM com ferramentas

```bash
# Usando CycloneDX para Python
pip install cyclonedx-bom
cyclonedx-py -r --format json -o bom.json

# Usando SPDX via spdx-sbom-generator
spdx-sbom-generator -p . -o bom.spdx

# Node.js (CycloneDX)
npx @cyclonedx/cyclonedx-npm --output-file bom.json

# Docker image SBOM (Syft)
syft packages nginx:latest -o json > sbom.json

# Trivy SBOM
trivy image --format cyclonedx --output bom.json nginx:latest
```

```json
{
  "$schema": "http://cyclonedx.org/schema/bom-1.5.schema.json",
  "bomFormat": "CycloneDX",
  "specVersion": "1.5",
  "serialNumber": "urn:uuid:3e671687-395b-41f5-a30f-a58921a69b79",
  "version": 1,
  "metadata": {
    "timestamp": "2026-05-16T10:00:00Z",
    "tools": [
      {
        "vendor": "CycloneDX",
        "name": "cyclonedx-py",
        "version": "4.2.0"
      }
    ],
    "component": {
      "type": "application",
      "name": "jarvis-backend",
      "version": "1.0.0"
    }
  },
  "components": [
    {
      "type": "library",
      "name": "Flask",
      "version": "2.3.3",
      "purl": "pkg:pypi/flask@2.3.3",
      "licenses": [{"license": {"id": "BSD-3-Clause"}}],
      "externalReferences": [
        {
          "type": "website",
          "url": "https://flask.palletsprojects.com/"
        }
      ]
    }
  ],
  "dependencies": [
    {
      "ref": "pkg:pypi/flask@2.3.3",
      "dependsOn": [
        "pkg:pypi/werkzeug@3.0.1",
        "pkg:pypi/jinja2@3.1.2",
        "pkg:pypi/click@8.1.7",
        "pkg:pypi/itsdangerous@2.1.2"
      ]
    }
  ]
}
```

### Validacao de SBOM

```python
import json
from jsonschema import validate

with open("bom.json") as f:
    bom = json.load(f)

# Verificar properties obrigatorias
for component in bom.get("components", []):
    assert component.get("name"), "Componente sem nome"
    assert component.get("version"), f"Componente {component['name']} sem versao"
    assert component.get("purl"), f"Componente {component['name']} sem PURL"

# Calcular metricas
total = len(bom["components"])
with_licenses = sum(1 for c in bom["components"] if c.get("licenses"))
with_cves = sum(1 for c in bom["components"] if c.get("evidence") and c["evidence"].get("vulnerabilities"))

print(f"Total de componentes: {total}")
print(f"Componentes com licenca: {with_licenses} ({with_licenses/total*100:.1f}%)")
print(f"Componentes com CVEs conhecidas: {with_cves}")
```

## Software Signing

Assinatura de artefatos garante integridade e autenticacao de origem.

### Cosign (Sigstore)

```bash
# Instalar cosign (para assinatura de containers e artefatos)
# winget install sigstore.cosign

# Gerar par de chaves
cosign generate-key-pair

# Assinar imagem Docker
cosign sign --key cosign.key ghcr.io/will/jarvis-backend:v1.0.0

# Verificar assinatura
cosign verify --key cosign.pub ghcr.io/will/jarvis-backend:v1.0.0

# Assinar artefato arbitrario
cosign sign-blob --key cosign.key dist/app.tar.gz > dist/app.tar.gz.sig
cosign verify-blob --key cosign.pub --signature dist/app.tar.gz.sig dist/app.tar.gz
```

### GPG Signing para Git

```bash
# Configurar GPG no git
git config --global user.signingkey ABCDEF1234567890
git config --global commit.gpgsign true
git config --global tag.gpgsign true

# Assinar commits
git commit -S -m "feat: adiciona modulo de seguranca"

# Assinar tags
git tag -s v1.0.0 -m "Release v1.0.0"

# Verificar assinaturas
git verify-commit HEAD
git verify-tag v1.0.0
```

```python
# Exemplo: Verificar assinatura GPG programaticamente
import subprocess

def verify_gpg_signature(signature_file: str, data_file: str) -> bool:
    result = subprocess.run(
        ["gpg", "--verify", signature_file, data_file],
        capture_output=True, text=True
    )
    return result.returncode == 0
```

### SLSA (Supply-chain Levels for Software Artifacts)

SLSA e um framework de niveis de seguranca para cadeia de suprimentos:

| Nivel | Descricao | Requisitos |
|-------|-----------|------------|
| SLSA 1 | Build documentado | Scripts de build documentados |
| SLSA 2 | Build com proveniencia | Proveniencia de build gerada |
| SLSA 3 | Build hermetico | Build isolado, sem influencia externa |
| SLSA 4 | Build com auditoria | Reproducivel, revisado por pares |

```yaml
# Exemplo: GitHub Actions com SLSA
name: build-and-attest
on:
  push:
    branches: [main]

jobs:
  build:
    permissions:
      id-token: write
      contents: read
      attestations: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - run: pip install -r requirements.txt
      - run: python -m build

      - name: Generate SLSA provenance
        uses: slsa-framework/slsa-github-generator/.github/actions/generate-attestation@v1
        with:
          artifact-name: dist/*

      - name: Verify SLSA provenance
        run: |
          slsa-verifier verify-artifact \
            --provenance-path dist/*.intoto.jsonl \
            --source-uri github.com/${{ github.repository }} \
            --source-tag ${{ github.ref_name }}
```

## Dependabot

### Configuracao do Dependabot

```yaml
# .github/dependabot.yml
version: 2
updates:
  # Python (pip)
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "daily"
    open-pull-requests-limit: 10
    labels:
      - "dependencies"
      - "python"
    assignees:
      - "will"
    reviewers:
      - "will"
    allow:
      - dependency-type: "direct"
    ignore:
      - dependency-name: "flask"
        versions: [">=3.0.0"]
    commit-message:
      prefix: "chore"
      include: "scope"

  # JavaScript (npm)
  - package-ecosystem: "npm"
    directory: "/frontend"
    schedule:
      interval: "weekly"
      day: "monday"
    open-pull-requests-limit: 5
    labels:
      - "dependencies"
      - "frontend"
    versioning-strategy: increase-if-necessary
    groups:
      react-updates:
        patterns:
          - "react*"
          - "@types/react*"

  # Docker
  - package-ecosystem: "docker"
    directory: "/"
    schedule:
      interval: "weekly"

  # GitHub Actions
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

## Renovate

### Configuracao do Renovate

```jsonc
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": [
    "config:recommended",
    ":automergeLinters",
    ":automergeTesters",
    ":disableDependencyDashboard"
  ],
  "schedule": ["before 9am on monday"],
  "timezone": "America/Sao_Paulo",
  "labels": ["dependencies"],
  "assignees": ["will"],
  "packageRules": [
    {
      "matchUpdateTypes": ["patch"],
      "automerge": true
    },
    {
      "matchPackageNames": ["flask", "django"],
      "enabled": false
    },
    {
      "matchCategories": ["python"],
      "labels": ["python", "dependencies"]
    },
    {
      "matchCategories": ["js"],
      "labels": ["javascript", "dependencies"]
    }
  ],
  "vulnerabilityAlerts": {
    "enabled": true,
    "labels": ["security"],
    "schedule": ["at any time"]
  },
  "osvVulnerabilityAlerts": true,
  "prCreation": "not-pending",
  "prConcurrentLimit": 5,
  "branchConcurrentLimit": 10,
  "rebaseWhen": "auto",
  "lockFileMaintenance": {
    "enabled": true,
    "automerge": true
  }
}
```

## Seguranca em Pipelines Python

```yaml
# .github/workflows/security-scan.yml
name: Security Scan
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  schedule:
    - cron: "0 6 * * 1"

jobs:
  dependencies:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: pip-audit
        run: |
          pip install pip-audit
          pip-audit --requirement requirements.txt --strict

      - name: Safety check
        run: |
          pip install safety
          safety check -r requirements.txt --full-report

      - name: Generate SBOM
        run: |
          pip install cyclonedx-bom
          cyclonedx-py -r --format json -o bom.json

      - name: Upload SBOM
        uses: actions/upload-artifact@v4
        with:
          name: sbom
          path: bom.json
```

## Seguranca em Pipelines Node.js

```yaml
name: Node Security
on: [push, pull_request]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: "npm"
      - run: npm ci
      - run: npm audit --audit-level=high
        continue-on-error: true
      - name: Snyk Security Scan
        uses: snyk/actions/node@v3
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          args: --severity-threshold=high
```

## Docker Image Security

```dockerfile
# Dockerfile com seguranca em mente
FROM python:3.11-slim AS builder

# Usuario nao-root
RUN useradd -m -u 1000 appuser

# Instalar dependencias de build temporarias
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim AS runtime
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /etc/passwd /etc/passwd

WORKDIR /app
COPY app/ .

USER appuser
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000
CMD ["python", "main.py"]
```

```bash
# Scan de imagem Docker
docker pull myapp:latest
trivy image myapp:latest                # Scaneia vulnerabilidades
trivy image --severity HIGH,CRITICAL myapp:latest
grype myapp:latest                      # Scanner alternativo
docker scout cves myapp:latest          # Docker Scout integrado
```

## Verificacao de Checksum e Hashing

```python
import hashlib
import hmac
import requests

INTEGRITY_DB = {
    "flask-2.3.3.tar.gz": {
        "sha256": "a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1",
        "size": 1234567
    }
}

def verify_package_integrity(package_name: str, version: str) -> bool:
    """Verifica checksum de um pacote baixado."""
    filename = f"{package_name}-{version}.tar.gz"
    if filename not in INTEGRITY_DB:
        print(f"Checksum desconhecido para {filename}")
        return False

    with open(filename, "rb") as f:
        content = f.read()

    computed = hashlib.sha256(content).hexdigest()
    expected = INTEGRITY_DB[filename]["sha256"]

    if hmac.compare_digest(computed, expected):
        print(f"{filename}: checksum OK ({computed[:16]}...)")
        return True
    else:
        print(f"{filename}: FALHA no checksum!")
        print(f"  Esperado: {expected}")
        print(f"  Computado: {computed}")
        return False
```

## Monitoramento Continuo

```python
# Script de monitoramento de dependencias
import subprocess
import json
from datetime import datetime

def audit_dependencies():
    report = {
        "timestamp": datetime.utcnow().isoformat(),
        "tools": {}
    }

    # pip-audit
    result = subprocess.run(
        ["pip-audit", "--requirement", "requirements.txt", "--format", "json"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        report["tools"]["pip-audit"] = json.loads(result.stdout)
    else:
        report["tools"]["pip-audit"] = {"error": result.stderr}

    # npm audit
    result = subprocess.run(
        ["npm", "audit", "--json"],
        capture_output=True, text=True,
        cwd="./frontend"
    )
    if result.returncode <= 1:
        report["tools"]["npm-audit"] = json.loads(result.stdout)

    return report

if __name__ == "__main__":
    report = audit_dependencies()
    print(json.dumps(report, indent=2))
```

## Referencias Cruzadas

- [[seguranca/INDEX]] - Index de seguranca
- [[seguranca/secure-coding]] - Praticas de codificacao segura
- [[seguranca/secrets-management]] - Gerenciamento de secrets
- [[seguranca/owasp-top-10]] - OWASP Top 10 com exemplos
- [[devops/ci-cd/INDEX]] - Pipelines CI/CD
- [[devops/ci-cd/github-actions]] - Automacao com GitHub Actions
- [[02-software-engineering\advanced-backend-architecture]] - Arquitetura de backend