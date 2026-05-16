$path = "D:\GitHub\Will-obsidian\Conhecimento-Geral\Programacao\APIs-e-Integracoes.md"
$content = @'

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
'@
Add-Content -Path $path -Value $content
Write-Host "OK"
