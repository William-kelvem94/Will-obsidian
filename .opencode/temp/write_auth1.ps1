$path = "D:\GitHub\Will-obsidian\Conhecimento-Geral\Programacao\APIs-e-Integracoes.md"
$content = @'

---

## 5. Autenticacao e Autorizacao

### 5.1 API Keys

Chave simples enviada via header ou query parameter.

```python
API_KEYS = {"sk-abc123": {"cliente": "Acme Corp", "taxa": 100}}

def validar_api_key(request):
    api_key = request.headers.get("X-API-Key") or request.args.get("api_key")
    if not api_key or api_key not in API_KEYS:
        abort(401, "API Key invalida")
    return API_KEYS[api_key]
```

```typescript
const API_KEYS = new Map([
  ["sk-abc123", { cliente: "Acme Corp", taxa: 100 }],
]);

function validarApiKey(req: express.Request): void {
  const key = (req.headers["x-api-key"] as string) || (req.query.api_key as string);
  if (!key || !API_KEYS.has(key)) {
    throw new Error("API Key invalida");
  }
}
```

### 5.2 JWT (JSON Web Tokens)

Token autocontido com claims assinadas digitalmente.

```python
import jwt
from datetime import datetime, timedelta

SECRET = "minha-chave-secreta"

def gerar_token(usuario_id: str, role: str) -> str:
    payload = {
        "sub": usuario_id,
        "role": role,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(hours=1),
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def validar_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise PermissionError("Token expirado")
    except jwt.InvalidTokenError:
        raise PermissionError("Token invalido")

@app.route("/login", methods=["POST"])
def login():
    dados = request.get_json()
    if dados["usuario"] == "admin" and dados["senha"] == "123":
        token = gerar_token("user-1", "admin")
        return jsonify({"token": token})
    abort(401)
```
'@
Add-Content -Path $path -Value $content
Write-Host "OK"
