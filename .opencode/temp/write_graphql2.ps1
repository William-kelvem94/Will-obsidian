$path = "D:\GitHub\Will-obsidian\Conhecimento-Geral\Programacao\APIs-e-Integracoes.md"
$content = @'
```typescript
import { ApolloServer, gql } from "apollo-server";

const typeDefs = gql`
  type Usuario {
    id: ID!
    nome: String!
    email: String!
    pedidos: [Pedido!]!
  }

  type Pedido {
    id: ID!
    total: Float!
    status: String!
  }

  type Query {
    usuario(id: ID!): Usuario
    usuarios: [Usuario!]!
  }

  type Mutation {
    criarUsuario(nome: String!, email: String!): Usuario!
  }

  type Subscription {
    pedidoCriado: Pedido!
  }
`;

interface Usuario {
  id: string;
  nome: string;
  email: string;
}

const usuariosDB = new Map<string, Usuario>();

const resolvers = {
  Query: {
    usuario: (_: unknown, { id }: { id: string }) => usuariosDB.get(id) ?? null,
    usuarios: () => Array.from(usuariosDB.values()),
  },
  Mutation: {
    criarUsuario: (_: unknown, { nome, email }: { nome: string; email: string }) => {
      const usuario: Usuario = { id: String(usuariosDB.size + 1), nome, email };
      usuariosDB.set(usuario.id, usuario);
      return usuario;
    },
  },
  Usuario: {
    pedidos: (parent: Usuario) => [],
  },
};

const server = new ApolloServer({ typeDefs, resolvers });
server.listen().then(({ url }) => console.log(`Server ready at ${url}`));
```

### 2.3 N+1 Problem

Problema onde uma consulta GraphQL dispara N+1 queries ao banco de dados. Solucao: DataLoader (batching + caching).

```python
from dataloader import DataLoader

class PedidosLoader(DataLoader):
    def batch_load(self, usuario_ids: list[str]) -> list[list[Pedido]]:
        resultados = db.query(
            "SELECT * FROM pedidos WHERE usuario_id IN (?)",
            (usuario_ids,)
        )
        by_user: dict[str, list[Pedido]] = {}
        for p in resultados:
            by_user.setdefault(str(p.usuario_id), []).append(p)
        return [by_user.get(uid, []) for uid in usuario_ids]

loader = PedidosLoader()

@strawberry.type
class Usuario:
    @strawberry.field
    async def pedidos(self) -> list[Pedido]:
        return await loader.load(self.id)
```

```typescript
import DataLoader from "dataloader";

const pedidosLoader = new DataLoader(async (usuarioIds: readonly string[]) => {
  const pedidos = await db.query(
    "SELECT * FROM pedidos WHERE usuario_id = ANY($1)",
    [usuarioIds]
  );
  const byUser = new Map<string, Pedido[]>();
  for (const p of pedidos) {
    const list = byUser.get(p.usuario_id) ?? [];
    list.push(p);
    byUser.set(p.usuario_id, list);
  }
  return usuarioIds.map(id => byUser.get(id) ?? []);
});

const resolvers = {
  Usuario: {
    pedidos: (parent: Usuario) => pedidosLoader.load(parent.id),
  },
};
```

### 2.4 GraphQL vs REST

| Aspecto | REST | GraphQL |
|---|---|---|
| Over-fetching | Comum (retorna dados extras) | Nunca |
| Under-fetching | Comum (precisa multiplas requests) | Nunca |
| Versionamento | URL ou headers | Evolucao do schema |
| Cache | Nativo (HTTP caching) | Requer configuracao |
| Complexidade | Baixa a media | Media a alta |
| Tooling | Maduro (Postman, cURL) | Playground, Apollo DevTools |
| Upload arquivos | Nativo | Requer extensao (multipart) |
'@
Add-Content -Path $path -Value $content
Write-Host "OK"
