$path = "D:\GitHub\Will-obsidian\Conhecimento-Geral\Programacao\APIs-e-Integracoes.md"
$content = @'

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
'@
Add-Content -Path $path -Value $content
Write-Host "OK"
