$path = "D:\GitHub\Will-obsidian\Conhecimento-Geral\Programacao\APIs-e-Integracoes.md"
$content = @'

---

## 2. GraphQL

Linguagem de consulta para APIs desenvolvida pelo Facebook (2015). Permite que o cliente solicite exatamente os dados que precisa.

**Referencia:** GraphQL Specification (graphql.org)

### 2.1 Schema e Types

```graphql
type Usuario {
  id: ID!
  nome: String!
  email: String!
  pedidos: [Pedido!]!
}

type Pedido {
  id: ID!
  total: Float!
  data: String!
  status: StatusPedido!
}

enum StatusPedido {
  PENDENTE
  CONFIRMADO
  ENVIADO
  ENTREGUE
}

type Query {
  usuario(id: ID!): Usuario
  usuarios: [Usuario!]!
  pedidos(usuarioId: ID!): [Pedido!]!
}

type Mutation {
  criarUsuario(nome: String!, email: String!): Usuario!
  criarPedido(usuarioId: ID!, total: Float!): Pedido!
}

type Subscription {
  pedidoCriado: Pedido!
}
```

### 2.2 Resolvers

```python
import strawberry
from typing import Optional

@strawberry.type
class Usuario:
    id: strawberry.ID
    nome: str
    email: str

@strawberry.type
class Pedido:
    id: strawberry.ID
    total: float
    status: str

@strawberry.type
class Query:
    @strawberry.field
    def usuario(self, id: strawberry.ID) -> Optional[Usuario]:
        return USUARIOS_DB.get(str(id))

    @strawberry.field
    def usuarios(self) -> list[Usuario]:
        return list(USUARIOS_DB.values())

    @strawberry.field
    def pedidos(self, usuario_id: strawberry.ID) -> list[Pedido]:
        return PEDIDOS_DB.get(str(usuario_id), [])

@strawberry.type
class Mutation:
    @strawberry.mutation
    def criar_usuario(self, nome: str, email: str) -> Usuario:
        usuario = Usuario(id=strawberry.ID(str(uuid4())), nome=nome, email=email)
        USUARIOS_DB[str(usuario.id)] = usuario
        return usuario

schema = strawberry.Schema(query=Query, mutation=Mutation)
```
'@
Add-Content -Path $path -Value $content
Write-Host "OK"
