$path = "D:\GitHub\Will-obsidian\Conhecimento-Geral\Programacao\APIs-e-Integracoes.md"
$content = @'
```typescript
import express from "express";
import crypto from "crypto";

const app = express();
app.use(express.json());

interface WebhookRegistro {
  url: string;
  eventos: string[];
  secret: string;
}

const webhooks: WebhookRegistro[] = [];

app.post("/webhooks/register", (req, res) => {
  webhooks.push({
    url: req.body.url,
    eventos: req.body.eventos ?? ["*"],
    secret: req.body.secret ?? "",
  });
  res.status(201).json({ status: "registrado" });
});

function dispararEvento(tipo: string, dados: Record<string, unknown>): void {
  const payload = { evento: tipo, timestamp: new Date().toISOString(), dados };
  for (const wh of webhooks) {
    if (wh.eventos.includes(tipo) || wh.eventos.includes("*")) {
      const assinatura = crypto
        .createHmac("sha256", wh.secret)
        .update(JSON.stringify(payload))
        .digest("hex");
      fetch(wh.url, {
        method: "POST",
        body: JSON.stringify(payload),
        headers: {
          "Content-Type": "application/json",
          "X-Webhook-Signature": assinatura,
        },
      }).catch(err => console.error(`Falha webhook ${wh.url}:`, err));
    }
  }
}
```

### 4.2 Retry e Idempotencia

```python
import time
from dataclasses import dataclass

@dataclass
class TentativaWebhook:
    url: str
    payload: dict
    tentativas: int = 0
    max_tentativas: int = 3

def processar_fila_webhook(fila: list[TentativaWebhook]) -> None:
    for item in fila[:]:
        try:
            resp = requests.post(item.url, json=item.payload, timeout=10)
            if resp.status_code == 200:
                fila.remove(item)
        except requests.RequestException:
            item.tentativas += 1
            if item.tentativas >= item.max_tentativas:
                fila.remove(item)
                print(f"Falha definitiva: {item.url}")
            else:
                time.sleep(2 ** item.tentativas)

@app.route("/webhooks/receive", methods=["POST"])
def receber_webhook():
    event_id = request.headers.get("X-Event-ID")
    if event_id in EVENTOS_PROCESSADOS:
        return jsonify({"status": "ja processado"}), 200
    dados = request.get_json()
    processar_evento(dados)
    EVENTOS_PROCESSADOS.add(event_id)
    return jsonify({"status": "ok"}), 200
```
'@
Add-Content -Path $path -Value $content
Write-Host "OK"
