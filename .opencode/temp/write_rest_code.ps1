$path = "D:\GitHub\Will-obsidian\Conhecimento-Geral\Programacao\APIs-e-Integracoes.md"
$content = @'
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
'@
Add-Content -Path $path -Value $content
Write-Host "OK"
