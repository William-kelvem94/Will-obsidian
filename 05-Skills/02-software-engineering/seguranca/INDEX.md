---
tags: [skills, seguranca, security, index, skills-eng]
updated: 2026-06-10
title: "Seguranca da Informacao - Index"
date: 2026-06-01
---

# Seguranca da Informacao - Index

Guia completo sobre seguranca da informacao abrangendo desde fundamentos clasicos como a triade CIA ate topicos modernos como defesa contra prompt injection em sistemas LLM.

## Taxonomia de Seguranca

### Por Camada
- **Seguranca Fisica**: Controle de acesso a datacenters, biometria, vigilancia
- **Seguranca de Rede**: Firewalls, IDS/IPS, VPNs, segmentacao de rede
- **Seguranca de Aplicacao**: OWASP Top 10, secure coding, SAST/DAST
- **Seguranca de Dados**: Criptografia, DLP, mascaramento, tokenizacao
- **Seguranca de Identidade**: IAM, SSO, MFA, RBAC, Zero Trust
- **Seguranca Operacional**: SOC, threat hunting, incident response
- **Seguranca de Supply Chain**: SBOM, assinatura de artefatos, dependecias

### Por Ciclo de Vida (SDL)
1. **Requisitos**: Modelagem de ameacas, privacy impact assessment
2. **Design**: Threat modeling (STRIDE), security architecture review
3. **Desenvolvimento**: Secure coding standards, SAST, pre-commit hooks
4. **Testes**: DAST, penetration testing, fuzzing
5. **Deploy**: Infrastructure scanning, secret detection, container scanning
6. **Operacao**: Monitoring, incident response, patch management

## Triade CIA

A triade CIA e o modelo fundamental de seguranca da informacao:

### Confidentialidade (Confidencialidade)
- Dados acessiveis apenas por entidades autorizadas
- Mecanismos: criptografia (em repouso e em transito), ACLs, RBAC
- Violacao: vazamento de dados, exposicao de secrets

```python
from cryptography.fernet import Fernet

# Exemplo: criptografar dado sensivel antes de persistir
key = Fernet.generate_key()
cipher = Fernet(key)
dado_sensivel = b"4012-8888-8888-1881"
token = cipher.encrypt(dado_sensivel)
# Persista o token, nunca o dado em texto claro

# Para ler:
dado_original = cipher.decrypt(token)
print(dado_original.decode())
```

### Integrity (Integridade)
- Dados nao sao alterados por entidades nao autorizadas
- Mecanismos: hashing (SHA-256), HMAC, assinaturas digitais
- Violacao: dados corrompidos, man-in-the-middle

```python
import hashlib
import hmac

# Hash de integridade
def verify_integrity(content: bytes, expected_hash: str) -> bool:
    computed = hashlib.sha256(content).hexdigest()
    return hmac.compare_digest(computed, expected_hash)

# Uso em pipeline de dados
with open("relatorio.csv", "rb") as f:
    data = f.read()
if verify_integrity(data, "a1b2c3..."):
    print("Integridade verificada")
```

### Availability (Disponibilidade)
- Sistemas e dados acessiveis quando necessario
- Mecanismos: redundancia, load balancing, backups, chaos engineering
- Violacao: DDoS, ransomware, falha de infraestrutura

```yaml
# docker-compose com redundancia
version: "3.8"
services:
  app:
    image: myapp:latest
    deploy:
      replicas: 3
      resources:
        limits:
          memory: 512M
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 30s
  redis:
    image: redis:7-alpine
    deploy:
      replicas: 2
```

## Threat Modeling com STRIDE

STRIDE e o modelo da Microsoft para categorizar ameacas:

| Tipo | Descricao | Exemplo | Mitigacao |
|------|-----------|---------|-----------|
| **S**poofing | Falsificar identidade | Token JWT roubado | MFA, certificados |
| **T**ampering | Alterar dados | Modificar payload HTTP | Assinatura digital, HMAC |
| **R**epudiation | Negar autoria | Usuario nega ter feito acao | Logs imutaveis, audit trail |
| **I**nformation Disclosure | Vazar dados | SQL injection | Criptografia, parametrizacao |
| **D**enial of Service | Negar servico | DDoS, deplecao de recurso | Rate limiting, auto-scaling |
| **E**levation of Privilege | Escalar privilegio | Path traversal, RCE | RBAC, principle of least privilege |

```python
# Exemplo: modelagem STRIDE para uma API REST
strides_checklist = {
    "Spoofing": [
        "Validar token JWT em toda requisicao",
        "Configurar CORS corretamente",
        "Nao confiar em headers HTTP para identidade"
    ],
    "Tampering": [
        "Usar HTTPS obrigatorio",
        "Validar input em toda entrada",
        "Usar prepared statements no SQL"
    ],
    "Repudiation": [
        "Logar todas as operacoes criticas",
        "Usar correlacao com request ID",
        "Manter logs em storage imutavel"
    ],
    "Information Disclosure": [
        "Nao expor stack traces em producao",
        "Sanitizar respostas de erro",
        "Criptografar dados sensiveis em repouso"
    ],
    "Denial of Service": [
        "Implementar rate limiting por IP/usuario",
        "Configurar timeout em todas as chamadas externas",
        "Usar filas para processamento assincrono"
    ],
    "Elevation of Privilege": [
        "Validar permissoes em cada endpoint",
        "Nao confiar em role vinda do frontend",
        "Principio do menor privilegio"
    ]
}
```

## Security Checklist por Fase

### Pre-Desenvolvimento
- [ ] Modelagem de ameacas (STRIDE) realizada
- [ ] Analise de dependencias (OWASP Dependency-Check)
- [ ] Definicao de security requirements
- [ ] Revisao de arquitetura de seguranca

### Desenvolvimento
- [ ] SAST configurado no pipeline (Semgrep, Bandit)
- [ ] Pre-commit hooks com secret scanning (git-secrets)
- [ ] Code review com foco em seguranca
- [ ] Testes de seguranca unitarios

### Build e CI/CD
- [ ] Scan de imagens Docker (Trivy, Snyk)
- [ ] SBOM gerado para cada artefato
- [ ] Dependencias auditadas (npm audit, pip audit)
- [ ] Assinatura de artefatos (cosign)

### Deploy
- [ ] DAST executado contra ambiente de staging
- [ ] Secrets injetados via vault, nunca no codigo
- [ ] Network policies aplicadas (Kubernetes NetworkPolicy)
- [ ] Health checks e readiness probes configurados

### Operacao
- [ ] Backup automatizado testado
- [ ] Monitoramento de seguranca ativo (SIEM)
- [ ] Incident response plan documentado
- [ ] Patch management em dia

## Matriz de Controles por Categoria

| Categoria | Controle Preventivo | Controle Detectivo | Controle Corretivo |
|-----------|---------------------|--------------------|--------------------|
| Identidade | MFA, RBAC | Login anomaly detection | Revogacao de credenciais |
| Rede | Firewall, WAF | IDS/IPS, network flow logs | Isolamento de segmento |
| Aplicacao | Input validation, CSP | SAST/DAST, WAF alerts | Rollback de versao |
| Dados | Encryption at rest | DLP, data loss alerts | Restore de backup |
| Supply Chain | Dependabot, Renovate | SBOM diff, CVE scan | Pinning de versoes |

## Referencias Cruzadas

- [[seguranca/owasp-top-10]] - Aprofundamento em OWASP Top 10 (2021)
- [[seguranca/secure-coding]] - Praticas de codificacao segura
- [[seguranca/supply-chain-security]] - Seguranca na cadeia de suprimentos
- [[seguranca/secrets-management]] - Gerenciamento de secrets
- [[seguranca/prompt-injection-defense]] - Defesa contra prompt injection em LLMs
- [[02-software-engineering\advanced-backend-architecture]] - Padroes de arquitetura segura
- [[SFIA-Mapping]] - Mapeamento SFIA para seguranca
- [[devops\Observabilidade]] - Monitoramento e observabilidade

## Ferramentas Recomendadas

### SAST (Static Analysis)
- **Semgrep**: Regras customizaveis, suporta Python/JS/TS
- **Bandit**: Seguranca Python
- **ESLint-plugin-security**: Seguranca JavaScript
- **CodeQL**: Analise profunda da GitHub

### DAST (Dynamic Analysis)
- **OWASP ZAP**: Scanner de seguranca web gratuito
- **Burp Suite**: Testes de penetracao profissionais
- **Nuclei**: Scanner baseado em templates YAML

### Dependency Scanning
- **Dependabot**: Automacao GitHub para dependecias
- **Renovate**: Bot de atualizacao de dependecias
- **Trivy**: Scan de vulnerabilidades em containers

### Secrets Management
- **git-secrets**: Pre-commit hook contra secrets
- **truffleHog**: Scan de repositorios git
- **Hashicorp Vault**: Gerenciamento centralizado de secrets

## Principios de Design Seguro

1. **Least Privilege**: Cada entidade tem o minimo de permissoes necessarias
2. **Defense in Depth**: Multiplas camadas de seguranca, nenhuma unica falha e fatal
3. **Fail Secure**: Em caso de falha, o sistema nega acesso por padrao
4. **Secure by Default**: Configuracoes seguras sao o padrao, nao uma opcao
5. **Separation of Duties**: Nenhuma entidade tem controle completo sobre um processo
6. **Economy of Mechanism**: Mecanismos simples sao mais faceis de auditar e proteger
7. **Complete Mediation**: Todo acesso deve ser verificado, sem cache de autorizacao
8. **Open Design**: Seguranca nao depende da obscuridade do algoritmo

```python
# Exemplo: Fail Secure pattern
class FileAccess:
    def read(self, path: str, user: User) -> str:
        # Por padrao, nega acesso
        allowed = False
        try:
            allowed = self._check_permission(path, user)
            if allowed:
                return self._do_read(path)
        except PermissionDeniedError:
            pass  # Nao revela se o arquivo existe ou nao
        finally:
            if not allowed:
                raise PermissionDeniedError("Acesso negado")
```

## Recursos e Referencias

- OWASP: https://owasp.org
- NIST SP 800-53: Security and Privacy Controls
- CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks
- STRIDE: Microsoft Threat Modeling Tool
- MITRE ATT&CK: https://attack.mitre.org