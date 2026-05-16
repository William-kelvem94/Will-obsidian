$path = "D:\GitHub\Will-obsidian\Conhecimento-Geral\Programacao\APIs-e-Integracoes.md"
$content = @"
### 1.3 Status Codes HTTP

Cada metodo tem status codes esperados:

| Codigo | Significado | Uso |
|---|---|---|
| 200 | OK | GET, PUT, PATCH bem-sucedidos |
| 201 | Created | POST bem-sucedido |
| 204 | No Content | DELETE bem-sucedido |
| 400 | Bad Request | Dados invalidos na requisicao |
| 401 | Unauthorized | Autenticacao necessaria |
| 403 | Forbidden | Sem permissao |
| 404 | Not Found | Recurso inexistente |
| 409 | Conflict | Conflito (ex: duplicata) |
| 422 | Unprocessable Entity | Validacao de negocios |
| 429 | Too Many Requests | Rate limit excedido |
| 500 | Internal Server Error | Erro inesperado no servidor |

### 1.4 Versionamento de API

```python
@app.route("/api/v1/usuarios")
def listar_v1():
    return jsonify([{"id": u.id, "nome": u.nome} for u in USUARIOS.values()])

@app.route("/api/v2/usuarios")
def listar_v2():
    return jsonify([
        {"id": u.id, "nome": u.nome, "email": u.email}
        for u in USUARIOS.values()
    ])

@app.route("/api/usuarios")
def listar_por_versao():
    version = request.headers.get("Accept-Version", "1")
    if version == "2":
        return listar_v2()
    return listar_v1()
```

```typescript
const routerV1 = express.Router();
const routerV2 = express.Router();

routerV1.get("/usuarios", (_req: Request, res: Response) => {
  res.json(Array.from(usuarios.values()).map(u => ({ id: u.id, nome: u.nome })));
});

routerV2.get("/usuarios", (_req: Request, res: Response) => {
  res.json(Array.from(usuarios.values()));
});

app.use("/api/v1", routerV1);
app.use("/api/v2", routerV2);
```

### 1.5 HATEOAS

```python
@app.route("/api/usuarios/<int:usuario_id>")
def obter_usuario_hateoas(usuario_id: int):
    usuario = USUARIOS.get(usuario_id)
    if not usuario:
        abort(404)
    return jsonify({
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "_links": {
            "self": {"href": f"/api/usuarios/{usuario.id}"},
            "pedidos": {"href": f"/api/usuarios/{usuario.id}/pedidos"},
            "update": {"href": f"/api/usuarios/{usuario.id}", "method": "PUT"},
            "delete": {"href": f"/api/usuarios/{usuario.id}", "method": "DELETE"},
        }
    })
```

### 1.6 Paginacao

```python
@app.route("/api/usuarios")
def listar_paginado():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    total = len(USUARIOS)
    total_pages = (total + per_page - 1) // per_page
    start = (page - 1) * per_page
    end = start + per_page
    items = list(USUARIOS.values())[start:end]
    return jsonify({
        "data": [u.__dict__ for u in items],
        "pagination": {
            "page": page,
            "per_page": per_page,
            "total": total,
            "total_pages": total_pages,
            "links": {
                "first": f"/api/usuarios?page=1&per_page={per_page}",
                "prev": f"/api/usuarios?page={page-1}&per_page={per_page}" if page > 1 else None,
                "next": f"/api/usuarios?page={page+1}&per_page={per_page}" if page < total_pages else None,
                "last": f"/api/usuarios?page={total_pages}&per_page={per_page}",
            }
        }
    })
```

```typescript
app.get("/api/usuarios", (req: Request, res: Response) => {
  const page = Number(req.query.page) || 1;
  const perPage = Number(req.query.per_page) || 10;
  const items = Array.from(usuarios.values());
  const total = items.length;
  const totalPages = Math.ceil(total / perPage);
  const start = (page - 1) * perPage;
  const end = start + perPage;
  res.json({
    data: items.slice(start, end),
    pagination: {
      page, per_page: perPage, total, total_pages: totalPages,
      links: {
        first: `/api/usuarios?page=1&per_page=${perPage}`,
        prev: page > 1 ? `/api/usuarios?page=${page-1}&per_page=${perPage}` : null,
        next: page < totalPages ? `/api/usuarios?page=${page+1}&per_page=${perPage}` : null,
        last: `/api/usuarios?page=${totalPages}&per_page=${perPage}`,
      },
    },
  });
});
```
"@
Add-Content -Path $path -Value $content
Write-Host "Section REST detalhes escrito"
