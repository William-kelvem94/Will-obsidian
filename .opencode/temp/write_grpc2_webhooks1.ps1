$path = "D:\GitHub\Will-obsidian\Conhecimento-Geral\Programacao\APIs-e-Integracoes.md"
$content = @'
```typescript
import grpc from "@grpc/grpc-js";
import protoLoader from "@grpc/proto-loader";

const packageDef = protoLoader.loadSync("usuarios.proto", {});
const grpcObj = grpc.loadPackageDefinition(packageDef);

function getUsuario(
  call: grpc.ServerUnaryCall<any, any>,
  callback: grpc.sendUnaryData<any>
) {
  const usuario = usuariosDB.get(call.request.id);
  if (!usuario) {
    return callback({
      code: grpc.status.NOT_FOUND,
      details: "Nao encontrado",
    });
  }
  callback(null, usuario);
}

function atualizarUsuarioStream(call: grpc.ServerDuplexStream<any, any>) {
  call.on("data", (req: any) => {
    const usuario = usuariosDB.get(req.id);
    if (usuario) {
      if (req.nome) usuario.nome = req.nome;
      if (req.email) usuario.email = req.email;
      call.write(usuario);
    }
  });
  call.on("end", () => call.end());
}

const server = new grpc.Server();
server.addService(UsuarioService, {
  GetUsuario: getUsuario,
  AtualizarUsuarioStream: atualizarUsuarioStream,
});
server.bindAsync(
  "0.0.0.0:50051",
  grpc.ServerCredentials.createInsecure(),
  () => server.start()
);
```

---

## 4. Webhooks

Mecanismo de comunicacao **assincrono** onde um sistema envia dados automaticamente para uma URL pre-configurada quando um evento ocorre. Diferente de APIs tradicionais (polling), webhooks sao push-based.

```
[Servico A] ----(POST HTTP)----> [Servico B]
  (evento ocorre)                  (URL configurada)
```

### 4.1 Implementacao

```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
WEBHOOKS: list[dict] = []

@app.route("/webhooks/register", methods=["POST"])
def registrar_webhook():
    dados = request.get_json()
    WEBHOOKS.append({
        "url": dados["url"],
        "eventos": dados.get("eventos", ["*"]),
        "secret": dados.get("secret", ""),
    })
    return jsonify({"status": "registrado"}), 201

def disparar_evento(tipo: str, dados: dict) -> None:
    payload = {
        "evento": tipo,
        "timestamp": "2026-05-16T10:00:00Z",
        "dados": dados,
    }
    for wh in WEBHOOKS:
        if tipo in wh["eventos"] or "*" in wh["eventos"]:
            try:
                headers = {
                    "Content-Type": "application/json",
                    "X-Webhook-Signature": gerar_assinatura(payload, wh["secret"]),
                }
                requests.post(wh["url"], json=payload, headers=headers, timeout=10)
            except requests.RequestException as e:
                print(f"Falha ao enviar webhook: {e}")

@app.route("/api/pedidos", methods=["POST"])
def criar_pedido():
    dados = request.get_json()
    pedido = {"id": str(uuid4()), **dados}
    disparar_evento("pedido.criado", pedido)
    return jsonify(pedido), 201
```
'@
Add-Content -Path $path -Value $content
Write-Host "OK"
