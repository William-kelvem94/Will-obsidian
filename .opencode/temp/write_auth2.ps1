$path = "D:\GitHub\Will-obsidian\Conhecimento-Geral\Programacao\APIs-e-Integracoes.md"
$content = @'
```typescript
import jwt from "jsonwebtoken";

const SECRET = "minha-chave-secreta";

function gerarToken(usuarioId: string, role: string): string {
  return jwt.sign(
    { sub: usuarioId, role },
    SECRET,
    { expiresIn: "1h" }
  );
}

function validarToken(token: string): jwt.JwtPayload {
  return jwt.verify(token, SECRET) as jwt.JwtPayload;
}

app.post("/login", (req, res) => {
  if (req.body.usuario === "admin" && req.body.senha === "123") {
    const token = gerarToken("user-1", "admin");
    res.json({ token });
  } else {
    res.status(401).json({ erro: "Credenciais invalidas" });
  }
});

function authMiddleware(req: express.Request, res: express.Response, next: express.NextFunction): void {
  const auth = req.headers.authorization;
  if (!auth || !auth.startsWith("Bearer ")) {
    res.status(401).json({ erro: "Token nao fornecido" });
    return;
  }
  try {
    const payload = validarToken(auth.slice(7));
    (req as any).usuario = payload;
    next();
  } catch {
    res.status(401).json({ erro: "Token invalido" });
  }
}
```

### 5.3 OAuth 2.0 e OpenID Connect

Fluxos principais do OAuth 2.0:

**Authorization Code Flow (Recomendado para apps web)**

```
[Cliente] -> (1) Auth Request -> [Authorization Server]
[Cliente] <- (2) Auth Code ----- [Authorization Server]
[Cliente] -> (3) Code + Secret -> [Authorization Server]
[Cliente] <- (4) Access Token --- [Authorization Server]
[Cliente] -> (5) Token ---------> [Resource Server]
[Cliente] <- (6) Protected Data - [Resource Server]
```

```python
import requests

def obter_token_client_credentials(client_id: str, client_secret: str, scope: str) -> str:
    resp = requests.post("https://auth.exemplo.com/token", data={
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": scope,
    })
    return resp.json()["access_token"]

def trocar_code_por_token(code: str, client_id: str, client_secret: str, redirect_uri: str) -> dict:
    resp = requests.post("https://auth.exemplo.com/token", data={
        "grant_type": "authorization_code",
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
    })
    return resp.json()
```

```typescript
interface TokenResponse {
  access_token: string;
  refresh_token?: string;
  id_token?: string;
  expires_in: number;
}

async function obterTokenClientCredentials(
  clientId: string, clientSecret: string, scope: string
): Promise<TokenResponse> {
  const resp = await fetch("https://auth.exemplo.com/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      grant_type: "client_credentials",
      client_id: clientId,
      client_secret: clientSecret,
      scope,
    }),
  });
  return resp.json();
}
```

### 5.4 Comparacao de Metodos

| Metodo | Estado | Expira | Revogacao | Uso Tipico |
|---|---|---|---|---|
| API Key | Stateless | Nao (ou longa) | Manual | Servico a servico |
| JWT | Stateless | Sim (curta) | Lista negra (complexo) | Sessoes de usuario |
| OAuth2 Token | Stateless | Sim (curta) | Refresh rotation | Delegacao de acesso |
| Session Cookie | Stateful | Sim | Imediata | Apps web tradicionais |
| Basic Auth | Stateless | Nao | Nao | Legacy, dev |
'@
Add-Content -Path $path -Value $content
Write-Host "OK"
