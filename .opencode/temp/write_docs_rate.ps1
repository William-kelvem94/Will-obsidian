$path = "D:\GitHub\Will-obsidian\Conhecimento-Geral\Programacao\APIs-e-Integracoes.md"
$content = @'

---

## 6. Documentacao de APIs

### 6.1 OpenAPI / Swagger

```yaml
openapi: "3.0.3"
info:
  title: API de Usuarios
  version: "1.0.0"
  description: API REST para gerenciamento de usuarios

paths:
  /api/usuarios:
    get:
      summary: Lista todos os usuarios
      parameters:
        - name: page
          in: query
          schema: { type: integer, default: 1 }
        - name: per_page
          in: query
          schema: { type: integer, default: 10 }
      responses:
        "200":
          description: Lista de usuarios
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/Usuario"
    post:
      summary: Cria um novo usuario
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/CriarUsuarioInput"
      responses:
        "201":
          description: Usuario criado
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Usuario"

components:
  schemas:
    Usuario:
      type: object
      properties:
        id: { type: integer }
        nome: { type: string }
        email: { type: string, format: email }
    CriarUsuarioInput:
      type: object
      required: [nome, email]
      properties:
        nome: { type: string, example: "Joao Silva" }
        email: { type: string, format: email, example: "joao@email.com" }
```

### 6.2 Geracao automatica com Python

```python
from flask_openapi3 import OpenAPI, Info, Tag
from pydantic import BaseModel, EmailStr

info = Info(title="API Usuarios", version="1.0.0")
app = OpenAPI(__name__, info=info)

class UsuarioBody(BaseModel):
    nome: str
    email: EmailStr

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr

@app.get("/api/usuarios", tags=["Usuarios"])
def listar():
    """Listar todos os usuarios"""
    return [UsuarioResponse(id=1, nome="Joao", email="joao@email.com")]

@app.post("/api/usuarios", tags=["Usuarios"])
def criar(body: UsuarioBody):
    """Criar novo usuario"""
    return UsuarioResponse(id=2, nome=body.nome, email=body.email)

if __name__ == "__main__":
    app.run(debug=True)
```

### 6.3 Documentacao GraphQL

GraphQL tem documentacao embutida via introspeccao. Ferramentas como GraphQL Playground e Apollo Studio Explorer permitem navegar pelo schema.

```graphql
"""
Um usuario do sistema
"""
type Usuario {
  "ID unico do usuario"
  id: ID!
  "Nome completo do usuario"
  nome: String!
  "Email do usuario (unico)"
  email: String!
  "Lista de pedidos do usuario"
  pedidos: [Pedido!]!
}
```
'@
Add-Content -Path $path -Value $content
Write-Host "OK"
