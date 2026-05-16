$path = "D:\GitHub\Will-obsidian\Conhecimento-Geral\Programacao\APIs-e-Integracoes.md"
$content = @'
```python
from flask import Flask, jsonify, request, abort
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class Usuario:
    id: int
    nome: str
    email: str

USUARIOS: dict[int, Usuario] = {}
proximo_id = 1

@app.route("/api/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify([u.__dict__ for u in USUARIOS.values()])

@app.route("/api/usuarios/<int:usuario_id>", methods=["GET"])
def obter_usuario(usuario_id: int):
    usuario = USUARIOS.get(usuario_id)
    if not usuario:
        abort(404, "Usuario nao encontrado")
    return jsonify(usuario.__dict__)

@app.route("/api/usuarios", methods=["POST"])
def criar_usuario():
    global proximo_id
    dados = request.get_json()
    if not dados or "nome" not in dados or "email" not in dados:
        abort(400, "Nome e email obrigatorios")
    usuario = Usuario(id=proximo_id, nome=dados["nome"], email=dados["email"])
    USUARIOS[proximo_id] = usuario
    proximo_id += 1
    return jsonify(usuario.__dict__), 201

@app.route("/api/usuarios/<int:usuario_id>", methods=["PUT"])
def atualizar_usuario(usuario_id: int):
    dados = request.get_json()
    usuario = USUARIOS.get(usuario_id)
    if not usuario:
        abort(404)
    usuario.nome = dados.get("nome", usuario.nome)
    usuario.email = dados.get("email", usuario.email)
    return jsonify(usuario.__dict__)

@app.route("/api/usuarios/<int:usuario_id>", methods=["DELETE"])
def deletar_usuario(usuario_id: int):
    if usuario_id not in USUARIOS:
        abort(404)
    del USUARIOS[usuario_id]
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
```

```typescript
import express, { Request, Response } from "express";

interface Usuario {
  id: number;
  nome: string;
  email: string;
}

const app = express();
app.use(express.json());

const usuarios = new Map<number, Usuario>();
let proximoId = 1;

app.get("/api/usuarios", (_req: Request, res: Response) => {
  res.json(Array.from(usuarios.values()));
});

app.get("/api/usuarios/:id", (req: Request, res: Response) => {
  const usuario = usuarios.get(Number(req.params.id));
  if (!usuario) return res.status(404).json({ erro: "Nao encontrado" });
  res.json(usuario);
});

app.post("/api/usuarios", (req: Request, res: Response) => {
  const { nome, email } = req.body;
  if (!nome || !email) {
    return res.status(400).json({ erro: "Nome e email obrigatorios" });
  }
  const usuario: Usuario = { id: proximoId++, nome, email };
  usuarios.set(usuario.id, usuario);
  res.status(201).json(usuario);
});

app.put("/api/usuarios/:id", (req: Request, res: Response) => {
  const usuario = usuarios.get(Number(req.params.id));
  if (!usuario) return res.status(404).json({ erro: "Nao encontrado" });
  usuario.nome = req.body.nome ?? usuario.nome;
  usuario.email = req.body.email ?? usuario.email;
  res.json(usuario);
});

app.delete("/api/usuarios/:id", (req: Request, res: Response) => {
  const id = Number(req.params.id);
  if (!usuarios.has(id)) return res.status(404).json({ erro: "Nao encontrado" });
  usuarios.delete(id);
  res.status(204).send();
});
```
'@
Add-Content -Path $path -Value $content
Write-Host "OK"
