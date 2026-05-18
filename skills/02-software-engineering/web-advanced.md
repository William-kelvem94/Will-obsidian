---
tags: [skills, skills-eng, web, websockets, webrtc, pwa, web-security, web-performance]
updated: 2026-05-16
title: "Desenvolvimento Web Avancado - WebSockets, WebRTC, PWA, Performance e Seguranca"
date: 2026-05-16
---

# Desenvolvimento Web Avancado

Referencia completa para comunicacao em tempo real, PWAs, service workers, performance web, seguranca, CSS avancado e Web Components. Guia pratico com implementacoes em Python e TypeScript para treinamento do agente JARVIS.

## WebSockets

### Comunicacao Full-Duplex

```
Cliente                          Servidor
  |                                  |
  | -------- HTTP Upgrade -------->  |
  | <------ 101 Switching ---------  |
  |                                  |
  | <==== WebSocket Connection ====> |
  |                                  |
  | --- [Frame] ------------------>  |
  | <----------------- [Frame] ---   |
  | --- [Frame] ------------------>  |
  | <----------------- [Frame] ---   |
  |                                  |
  | -------- Close Frame ----------> |
  | <------- Close Frame ----------  |
```

### API WebSocket no Browser

```typescript
// Cliente WebSocket no browser
const ws = new WebSocket("ws://localhost:8080/ws");

ws.onopen = () => {
  console.log("Conectado");
  ws.send(JSON.stringify({ tipo: "autenticacao", token: "abc123" }));
};

ws.onmessage = (event: MessageEvent) => {
  const dados = JSON.parse(event.data);
  console.log("Recebido:", dados);
};

ws.onerror = (error: Event) => {
  console.error("Erro WebSocket:", error);
};

ws.onclose = (event: CloseEvent) => {
  console.log("Desconectado:", event.code, event.reason);
  // Tentar reconectar
  setTimeout(() => conectar(), 3000);
};

function enviarMensagem(texto: string): void {
  if (ws.readyState === WebSocket.OPEN) {
    ws.send(JSON.stringify({ tipo: "mensagem", texto, timestamp: Date.now() }));
  }
}
```

### Servidor WebSocket com Node.js (ws)

```typescript
import { WebSocketServer, WebSocket } from "ws";

const wss = new WebSocketServer({ port: 8080 });
const clientes = new Set<WebSocket>();

wss.on("connection", (ws: WebSocket) => {
  clientes.add(ws);
  console.log("Cliente conectado. Total:", clientes.size);

  ws.on("message", (data: Buffer) => {
    const msg = JSON.parse(data.toString());
    // Broadcast para todos os clientes
    clientes.forEach(client => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(JSON.stringify({ ...msg, enviadoEm: Date.now() }));
      }
    });
  });

  ws.on("close", () => {
    clientes.delete(ws);
    console.log("Cliente desconectado. Total:", clientes.size);
  });
});
```

### Servidor WebSocket com Python (websockets)

```python
import asyncio
import json
from datetime import datetime
import websockets

clientes = set()

async def handler(websocket):
    clientes.add(websocket)
    print(f"Cliente conectado. Total: {len(clientes)}")
    try:
        async for mensagem in websocket:
            dados = json.loads(mensagem)
            resposta = {
                **dados,
                "enviadoEm": datetime.utcnow().isoformat()
            }
            # Broadcast
            clientes_copia = clientes.copy()
            for cliente in clientes_copia:
                await cliente.send(json.dumps(resposta))
    except websockets.ConnectionClosed:
        pass
    finally:
        clientes.remove(websocket)
        print(f"Cliente desconectado. Total: {len(clientes)}")

async def main():
    async with websockets.serve(handler, "localhost", 8080):
        await asyncio.Future()  # rodar para sempre

asyncio.run(main())
```

### Socket.IO vs WebSockets Puros

| Caracteristica | WebSocket Puro | Socket.IO |
|----------------|---------------|-----------|
| Protocolo | ws:// ou wss:// | Proprio (fallback para HTTP) |
| Reconexao automatica | Manual | Automatica |
| Rooms/Namespaces | Manual | Built-in |
| Broadcast | Manual | Built-in |
| Fallback | Nao | Sim (long-polling) |
| Latencia | Menor | Ligeiramente maior |
| Tamanho do pacote | Menor | Maior (overhead) |

```typescript
// Socket.IO servidor
import { Server } from "socket.io";
import { createServer } from "http";

const httpServer = createServer();
const io = new Server(httpServer, {
  cors: { origin: "http://localhost:3000" },
  transports: ["websocket", "polling"]
});

io.on("connection", (socket) => {
  socket.on("entrar-sala", (sala: string) => {
    socket.join(sala);
  });

  socket.on("mensagem", (dados: { sala: string; texto: string }) => {
    socket.to(dados.sala).emit("nova-mensagem", {
      ...dados,
      autor: socket.id,
      timestamp: Date.now()
    });
  });

  socket.on("disconnect", () => {
    console.log("Cliente desconectado:", socket.id);
  });
});

httpServer.listen(3001);
```

```typescript
// Socket.IO cliente
import { io } from "socket.io-client";

const socket = io("http://localhost:3001", {
  transports: ["websocket"],
  reconnection: true,
  reconnectionDelay: 1000,
  reconnectionAttempts: 10
});

socket.on("connect", () => {
  console.log("Conectado:", socket.id);
  socket.emit("entrar-sala", "geral");
});

socket.on("nova-mensagem", (dados) => {
  console.log(`${dados.autor}: ${dados.texto}`);
});

socket.on("disconnect", (reason) => {
  console.log("Desconectado:", reason);
});
```

### Escalar WebSockets com Redis Pub/Sub

```
Servidor A <----> Redis Pub/Sub <----> Servidor B
    |                                     |
  Cliente 1                            Cliente 2
    |                                     |
    +--------- Mensagem via Redis --------+
```

```typescript
import { Server } from "socket.io";
import { createAdapter } from "@socket.io/redis-adapter";
import { createClient } from "redis";

const pubClient = createClient({ url: "redis://localhost:6379" });
const subClient = pubClient.duplicate();

await Promise.all([pubClient.connect(), subClient.connect()]);

const io = new Server(3001);
io.adapter(createAdapter(pubClient, subClient));

// Agora mensagens sao propagadas entre todos os servidores
io.on("connection", (socket) => {
  socket.on("mensagem", (dados) => {
    io.emit("broadcast", dados); // Funciona entre multiplos servidores
  });
});
```

### Estrategia de Reconexao

```typescript
class WebSocketReconectavel {
  private url: string;
  private ws: WebSocket | null = null;
  private tentativas = 0;
  private maxTentativas = 10;
  private delayBase = 1000;
  private ouvintes: Map<string, Set<(dados: any) => void>> = new Map();

  constructor(url: string) {
    this.url = url;
    this.conectar();
  }

  private conectar(): void {
    this.ws = new WebSocket(this.url);

    this.ws.onopen = () => {
      this.tentativas = 0;
      console.log("Conectado");
    };

    this.ws.onmessage = (event) => {
      const dados = JSON.parse(event.data);
      const ouvintes = this.ouvintes.get(dados.tipo);
      ouvintes?.forEach(fn => fn(dados));
    };

    this.ws.onclose = () => {
      this.reconectar();
    };
  }

  private reconectar(): void {
    if (this.tentativas >= this.maxTentativas) {
      console.error("Maximo de tentativas atingido");
      return;
    }
    // Exponential backoff: 1s, 2s, 4s, 8s...
    const delay = this.delayBase * Math.pow(2, this.tentativas);
    this.tentativas++;
    console.log(`Reconectando em ${delay}ms (tentativa ${this.tentativas})`);
    setTimeout(() => this.conectar(), delay);
  }

  on(tipo: string, fn: (dados: any) => void): void {
    if (!this.ouvintes.has(tipo)) this.ouvintes.set(tipo, new Set());
    this.ouvintes.get(tipo)!.add(fn);
  }

  enviar(tipo: string, dados: any): void {
    if (this.ws?.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify({ tipo, ...dados }));
    }
  }
}
```

## WebRTC

### Comunicacao Peer-to-Peer

```
Cliente A                    Servidor Sinalizacao              Cliente B
   |                                |                             |
   | --- offer (SDP) ------------> |                             |
   |                               | --- offer (SDP) ----------> |
   |                               |                             |
   |                               | <--- answer (SDP) --------- |
   | <--- answer (SDP) ----------- |                             |
   |                               |                             |
   | --- ICE candidates ---------> |                             |
   |                               | --- ICE candidates -------> |
   |                               |                             |
   | <======= Peer Connection (media) =========================> |
```

### Exemplo Completo de Video Chamada

```typescript
// Cliente WebRTC
class VideoCall {
  private peerConnection: RTCPeerConnection;
  private localStream?: MediaStream;
  private onRemoteStream?: (stream: MediaStream) => void;

  constructor(iceServers: RTCIceServer[]) {
    this.peerConnection = new RTCPeerConnection({ iceServers });

    this.peerConnection.ontrack = (event) => {
      this.onRemoteStream?.(event.streams[0]);
    };

    this.peerConnection.onicecandidate = (event) => {
      if (event.candidate) {
        // Enviar candidato ICE para o peer via servidor de sinalizacao
        console.log("ICE candidate:", event.candidate);
      }
    };
  }

  async iniciar(): Promise<MediaStream> {
    this.localStream = await navigator.mediaDevices.getUserMedia({
      video: true,
      audio: true
    });

    this.localStream.getTracks().forEach(track => {
      this.peerConnection.addTrack(track, this.localStream!);
    });

    return this.localStream;
  }

  async criarOferta(): Promise<RTCSessionDescriptionInit> {
    const offer = await this.peerConnection.createOffer();
    await this.peerConnection.setLocalDescription(offer);
    return offer;
  }

  async receberOferta(offer: RTCSessionDescriptionInit): Promise<RTCSessionDescriptionInit> {
    await this.peerConnection.setRemoteDescription(new RTCSessionDescription(offer));
    const answer = await this.peerConnection.createAnswer();
    await this.peerConnection.setLocalDescription(answer);
    return answer;
  }

  async receberResposta(answer: RTCSessionDescriptionInit): Promise<void> {
    await this.peerConnection.setRemoteDescription(new RTCSessionDescription(answer));
  }

  adicionarCandidato(candidate: RTCIceCandidateInit): Promise<void> {
    return this.peerConnection.addIceCandidate(new RTCIceCandidate(candidate));
  }

  encerrar(): void {
    this.localStream?.getTracks().forEach(t => t.stop());
    this.peerConnection.close();
  }
}
```

### Data Channels para Transferencia de Arquivos

```typescript
// Data channel para transferencia de arquivos
const dataChannel = peerConnection.createDataChannel("arquivos", {
  ordered: true
});

dataChannel.onmessage = (event) => {
  const dados = JSON.parse(event.data);
  if (dados.tipo === "arquivo") {
    // Receber chunk do arquivo
    const blob = new Blob([dados.conteudo], { type: dados.mime });
    const url = URL.createObjectURL(blob);
    // Download automatico
    const a = document.createElement("a");
    a.href = url;
    a.download = dados.nome;
    a.click();
  }
};

function enviarArquivo(file: File): void {
  const reader = new FileReader();
  reader.onload = () => {
    dataChannel.send(JSON.stringify({
      tipo: "arquivo",
      nome: file.name,
      mime: file.type,
      conteudo: reader.result
    }));
  };
  reader.readAsArrayBuffer(file);
}
```

## Service Workers

### Ciclo de Vida

```
Install -> Installed -> Activate -> Activated -> Idle
                                    |
                                    v
                            Fetch/Message/Push
                                    |
                                    v
                              Redundant (substituido)
```

### Estrategias de Cache

```typescript
// service-worker.js

const CACHE_NAME = "app-v1";
const URLS_ESTATICOS = [
  "/",
  "/index.html",
  "/styles.css",
  "/app.js",
  "/manifest.json",
  "/icon-192.png"
];

// Install: cache de recursos estaticos
self.addEventListener("install", (event: ExtendableEvent) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(URLS_ESTATICOS))
  );
  self.skipWaiting(); // Ativar imediatamente
});

// Activate: limpar caches antigos
self.addEventListener("activate", (event: ExtendableEvent) => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys
        .filter(key => key !== CACHE_NAME)
        .map(key => caches.delete(key))
      )
    )
  );
  self.clients.claim(); // Controlar clientes imediatamente
});

// Fetch: estrategias de cache
self.addEventListener("fetch", (event: FetchEvent) => {
  const request = event.request;

  // Cache-First: para assets estaticos
  if (request.destination === "image" ||
      request.destination === "style" ||
      request.destination === "font") {
    event.respondWith(cacheFirst(request));
    return;
  }

  // Network-First: para dados da API
  if (request.url.includes("/api/")) {
    event.respondWith(networkFirst(request));
    return;
  }

  // Stale-While-Revalidate: para HTML
  event.respondWith(staleWhileRevalidate(request));
});

async function cacheFirst(request: Request): Promise<Response> {
  const cache = await caches.open(CACHE_NAME);
  const cached = await cache.match(request);
  if (cached) return cached;

  const response = await fetch(request);
  cache.put(request, response.clone());
  return response;
}

async function networkFirst(request: Request): Promise<Response> {
  try {
    const response = await fetch(request);
    const cache = await caches.open(CACHE_NAME);
    cache.put(request, response.clone());
    return response;
  } catch {
    const cached = await caches.match(request);
    if (cached) return cached;
    return new Response("Offline", { status: 503 });
  }
}

async function staleWhileRevalidate(request: Request): Promise<Response> {
  const cache = await caches.open(CACHE_NAME);
  const cached = await cache.match(request);
  const fetchPromise = fetch(request).then(response => {
    cache.put(request, response.clone());
    return response;
  });
  return cached || fetchPromise;
}
```

### Push Notifications

```typescript
// Registrar service worker e solicitar permissao
async function registrarPush(): Promise<void> {
  const registration = await navigator.serviceWorker.register("/sw.js");
  const subscription = await registration.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: urlBase64ToUint8Array(process.env.VAPID_PUBLIC_KEY!)
  });

  // Enviar subscription para o servidor
  await fetch("/api/push/subscribe", {
    method: "POST",
    body: JSON.stringify(subscription)
  });
}

// Service worker - receber push
self.addEventListener("push", (event: PushEvent) => {
  const dados = event.data?.json();
  event.waitUntil(
    self.registration.showNotification(dados.titulo, {
      body: dados.corpo,
      icon: "/icon-192.png",
      badge: "/badge-72.png",
      data: { url: dados.url },
      actions: [
        { action: "abrir", title: "Abrir" },
        { action: "fechar", title: "Fechar" }
      ]
    })
  );
});

self.addEventListener("notificationclick", (event: NotificationEvent) => {
  event.notification.close();
  if (event.action === "abrir") {
    event.waitUntil(clients.openWindow(event.notification.data.url));
  }
});
```

## Progressive Web Apps (PWA)

### Web App Manifest

```json
{
  "name": "Meu Aplicativo",
  "short_name": "MeuApp",
  "description": "Aplicativo PWA completo",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#4285f4",
  "orientation": "portrait-primary",
  "icons": [
    { "src": "/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icon-512.png", "sizes": "512x512", "type": "image/png" },
    { "src": "/icon-maskable.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ],
  "categories": ["productivity"],
  "shortcuts": [
    {
      "name": "Nova Tarefa",
      "url": "/nova-tarefa",
      "icons": [{ "src": "/shortcut-icon.png", "sizes": "96x96" }]
    }
  ]
}
```

### Exemplo Completo de Setup PWA

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#4285f4">
  <link rel="manifest" href="/manifest.json">
  <link rel="apple-touch-icon" href="/icon-192.png">
  <title>Meu PWA</title>
</head>
<body>
  <div id="app"></div>
  <script>
    // Registrar Service Worker
    if ("serviceWorker" in navigator) {
      window.addEventListener("load", async () => {
        const registration = await navigator.serviceWorker.register("/sw.js");
        console.log("SW registrado:", registration.scope);
      });
    }

    // Prompt de instalacao
    let deferredPrompt;
    window.addEventListener("beforeinstallprompt", (e) => {
      e.preventDefault();
      deferredPrompt = e;
      mostrarBotaoInstalacao();
    });

    async function instalar() {
      if (!deferredPrompt) return;
      deferredPrompt.prompt();
      const { outcome } = await deferredPrompt.userChoice;
      console.log("Instalacao:", outcome);
      deferredPrompt = null;
    }
  </script>
</body>
</html>
```

## Performance Web

### Critical Rendering Path

```
HTML Parse -> DOM Tree --+
                         +-> Render Tree -> Layout -> Paint -> Composite
CSSOM Parse -> CSSOM Tree -+

Otimizacoes:
1. Minimizar HTML/CSS/JS
2. Eliminar CSS/JS que bloqueiam renderizacao
3. Usar async/defer para scripts
4. Inline CSS critico
```

### Resource Hints

```html
<!-- Preconnect: estabelecer conexao antecipadamente -->
<link rel="preconnect" href="https://api.exemplo.com">
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>

<!-- DNS-prefetch: resolver DNS antecipadamente -->
<link rel="dns-prefetch" href="https://cdn.exemplo.com">

<!-- Preload: carregar recurso critico com alta prioridade -->
<link rel="preload" href="/font.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/hero.webp" as="image">

<!-- Prefetch: carregar recurso para navegacao futura -->
<link rel="prefetch" href="/proxima-pagina.html">

<!-- Prerender: renderizar pagina completa em background -->
<link rel="prerender" href="/proxima-pagina.html">
```

### Code Splitting e Lazy Loading

```typescript
// React - Lazy loading de componentes
import { lazy, Suspense } from "react";

const Dashboard = lazy(() => import("./Dashboard"));
const Configuracoes = lazy(() => import("./Configuracoes"));

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/config" element={<Configuracoes />} />
      </Routes>
    </Suspense>
  );
}

// Dynamic imports condicionais
async function carregarModulo(feature: string) {
  switch (feature) {
    case "charts":
      return import("./modules/charts");
    case "maps":
      return import("./modules/maps");
    default:
      return import("./modules/default");
  }
}
```

### Web Vitals

| Metrica | Nome | Boa | Precisa Melhorar | Ruim |
|---------|------|-----|------------------|------|
| LCP | Largest Contentful Paint | < 2.5s | < 4.0s | > 4.0s |
| INP | Interaction to Next Paint | < 200ms | < 500ms | > 500ms |
| CLS | Cumulative Layout Shift | < 0.1 | < 0.25 | > 0.25 |

```typescript
// Medir Web Vitals
import { onLCP, onINP, onCLS } from "web-vitals";

onLCP(({ value }) => console.log("LCP:", value));
onINP(({ value }) => console.log("INP:", value));
onCLS(({ value }) => console.log("CLS:", value));

// Enviar para analytics
function enviarParaAnalytics(metrica: { name: string; value: number }) {
  navigator.sendBeacon("/analytics", JSON.stringify(metrica));
}

onLCP(({ value }) => enviarParaAnalytics({ name: "LCP", value }));
```

### Otimizacao de Imagens

```html
<!-- Imagens responsivas -->
<img
  src="imagem-800.webp"
  srcset="imagem-400.webp 400w,
          imagem-800.webp 800w,
          imagem-1200.webp 1200w"
  sizes="(max-width: 600px) 400px,
         (max-width: 1000px) 800px,
         1200px"
  alt="Descricao"
  loading="lazy"
  decoding="async"
  width="800"
  height="600"
>

<!-- Picture element para formatos diferentes -->
<picture>
  <source srcset="imagem.avif" type="image/avif">
  <source srcset="imagem.webp" type="image/webp">
  <img src="imagem.jpg" alt="Descricao" loading="lazy">
</picture>
```

## Seguranca Web

### Content Security Policy (CSP)

```
Header HTTP:
Content-Security-Policy: default-src 'self';
  script-src 'self' https://cdn.exemplo.com;
  style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
  img-src 'self' data: https:;
  font-src 'self' https://fonts.gstatic.com;
  connect-src 'self' https://api.exemplo.com;
  frame-ancestors 'none';
  base-uri 'self';
  form-action 'self';
```

### CORS Deep Dive

```
Simple Request:
Cliente -> Servidor: Origin: https://app.exemplo.com
Servidor -> Cliente: Access-Control-Allow-Origin: https://app.exemplo.com

Preflight Request (metodos nao simples):
Cliente -> Servidor: OPTIONS
  Origin: https://app.exemplo.com
  Access-Control-Request-Method: DELETE
  Access-Control-Request-Headers: Content-Type, Authorization
Servidor -> Cliente:
  Access-Control-Allow-Origin: https://app.exemplo.com
  Access-Control-Allow-Methods: GET, POST, PUT, DELETE
  Access-Control-Allow-Headers: Content-Type, Authorization
  Access-Control-Max-Age: 86400
```

```typescript
// Middleware CORS em Express
import cors from "cors";

app.use(cors({
  origin: ["https://app.exemplo.com", "https://admin.exemplo.com"],
  methods: ["GET", "POST", "PUT", "DELETE"],
  allowedHeaders: ["Content-Type", "Authorization"],
  credentials: true,
  maxAge: 86400
}));

// CORS manual
app.use((req, res, next) => {
  const origemPermitida = process.env.ORIGENS_PERMITIDAS?.split(",") || [];
  const origin = req.headers.origin;

  if (origemPermitida.includes(origin!)) {
    res.setHeader("Access-Control-Allow-Origin", origin!);
    res.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
    res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
    res.setHeader("Access-Control-Allow-Credentials", "true");
    res.setHeader("Access-Control-Max-Age", "86400");
  }

  if (req.method === "OPTIONS") {
    return res.sendStatus(204);
  }
  next();
});
```

### Prevencao de XSS

```typescript
// Sanitizacao de HTML
import DOMPurify from "dompurify";

function renderizarComentario(html: string): string {
  return DOMPurify.sanitize(html, {
    ALLOWED_TAGS: ["b", "i", "em", "strong", "a", "p", "br"],
    ALLOWED_ATTR: ["href", "title"]
  });
}

// Escapar HTML em template
function escaparHtml(texto: string): string {
  return texto
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#x27;");
}

// CSP header para prevenir XSS
app.use((req, res, next) => {
  res.setHeader(
    "Content-Security-Policy",
    "default-src 'self'; " +
    "script-src 'self'; " +
    "style-src 'self' 'unsafe-inline'; " +
    "img-src 'self' data:; " +
    "frame-ancestors 'none'"
  );
  next();
});
```

### Protecao CSRF

```typescript
// Tokens CSRF com csurf
import csrf from "csurf";

app.use(csrf({ cookie: { httpOnly: true, secure: true, sameSite: "strict" } }));

app.use((req, res, next) => {
  res.locals.csrfToken = req.csrfToken();
  next();
});

// No frontend
// <input type="hidden" name="_csrf" value="{{csrfToken}}">

// Cookies SameSite
res.cookie("sessao", token, {
  httpOnly: true,
  secure: true,
  sameSite: "strict", // ou "lax"
  maxAge: 3600000
});
```

### Subresource Integrity (SRI)

```html
<!-- SRI hash gerado com: openssl dgst -sha384 -binary arquivo.js | openssl base64 -A -->
<script
  src="https://cdn.exemplo.com/lib.js"
  integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"
  crossorigin="anonymous"
></script>

<link
  rel="stylesheet"
  href="https://cdn.exemplo.com/styles.css"
  integrity="sha384-..."
  crossorigin="anonymous"
>
```

## CSS Avancado

### Grid e Flexbox Padroes Avancados

```css
/* Grid - Layout responsivo sem media queries */
.grid-auto {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
}

/* Grid - Areas nomeadas */
.layout {
  display: grid;
  grid-template-areas:
    "header header header"
    "sidebar main aside"
    "footer footer footer";
  grid-template-columns: 250px 1fr 200px;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.aside { grid-area: aside; }
.footer { grid-area: footer; }

/* Flexbox - Centralizacao perfeita */
.centralizar {
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Flexbox - Order e flex-grow */
.nav {
  display: flex;
  gap: 1rem;
}
.nav-item { flex: 1; }
.nav-item.destaque { flex: 2; }
```

### CSS Custom Properties (Variaveis)

```css
:root {
  --cor-primaria: #4285f4;
  --cor-secundaria: #34a853;
  --cor-erro: #ea4335;
  --espacamento-xs: 0.25rem;
  --espacamento-sm: 0.5rem;
  --espacamento-md: 1rem;
  --espacamento-lg: 2rem;
  --fonte-titulo: 1.5rem;
  --fonte-corpo: 1rem;
  --sombra: 0 2px 8px rgba(0, 0, 0, 0.1);
  --transicao: 0.2s ease;
}

.botao {
  background: var(--cor-primaria);
  padding: var(--espacamento-sm) var(--espacamento-md);
  border-radius: var(--espacamento-xs);
  transition: var(--transicao);
  box-shadow: var(--sombra);
}

.botao:hover {
  background: color-mix(in srgb, var(--cor-primaria) 80%, black);
}

/* Tema escuro com variaveis */
@media (prefers-color-scheme: dark) {
  :root {
    --cor-fundo: #1a1a2e;
    --cor-texto: #e0e0e0;
    --sombra: 0 2px 8px rgba(0, 0, 0, 0.4);
  }
}
```

### Container Queries

```css
/* Container query - responsivo baseado no container, nao na viewport */
.card-container {
  container-type: inline-size;
  container-name: card;
}

@container card (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 200px 1fr;
    gap: 1rem;
  }
}

@container card (min-width: 600px) {
  .card {
    grid-template-columns: 300px 1fr;
  }
  .card-imagem {
    height: 100%;
  }
}
```

### CSS-in-JS vs CSS Modules vs Tailwind

| Abordagem | Escopo | Performance | DX | Bundle Size |
|-----------|--------|-------------|-----|-------------|
| CSS-in-JS (styled-components) | Automatico | Runtime overhead | Excelente | Maior |
| CSS Modules | Build-time | Zero runtime | Bom | Medio |
| Tailwind CSS | Utility classes | Zero runtime | Bom (curva aprendizado) | Otimizavel |
| CSS puro | Global | Zero runtime | Basico | Menor |

```typescript
// CSS Modules
import styles from "./Componente.module.css";

function Componente() {
  return <div className={styles.container}>Conteudo</div>;
}

/* Componente.module.css */
.container {
  padding: 1rem;
  border-radius: 8px;
}
.container:hover {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
```

## Web Components

### Custom Elements Lifecycle

```
constructor() -> connectedCallback() -> attributeChangedCallback()
                      |                          |
                      v                          v
               disconnectedCallback()     adoptedCallback()
```

### Componente Reutilizavel Completo

```typescript
// Custom Element com Shadow DOM
class CardComponent extends HTMLElement {
  static get observedAttributes() {
    return ["titulo", "imagem", "descricao"];
  }

  private shadow: ShadowRoot;

  constructor() {
    super();
    this.shadow = this.attachShadow({ mode: "open" });
  }

  connectedCallback() {
    this.render();
  }

  attributeChangedCallback(name: string, oldValue: string, newValue: string) {
    if (oldValue !== newValue) {
      this.render();
    }
  }

  private render(): void {
    const titulo = this.getAttribute("titulo") || "";
    const imagem = this.getAttribute("imagem") || "";
    const descricao = this.getAttribute("descricao") || "";

    this.shadow.innerHTML = `
      <style>
        :host {
          display: block;
          border-radius: 8px;
          overflow: hidden;
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
          background: white;
        }
        .imagem {
          width: 100%;
          height: 200px;
          object-fit: cover;
        }
        .conteudo {
          padding: 1rem;
        }
        .titulo {
          font-size: 1.25rem;
          font-weight: bold;
          margin: 0 0 0.5rem 0;
        }
        .descricao {
          color: #666;
          margin: 0;
        }
        ::slotted(*) {
          margin-top: 1rem;
        }
      </style>
      ${imagem ? `<img class="imagem" src="${imagem}" alt="${titulo}">` : ""}
      <div class="conteudo">
        <h3 class="titulo">${titulo}</h3>
        <p class="descricao">${descricao}</p>
        <slot></slot>
      </div>
    `;
  }
}

customElements.define("app-card", CardComponent);

// Uso:
// <app-card titulo="Produto" imagem="/foto.jpg" descricao="Descricao do produto">
//   <button slot="acoes">Comprar</button>
// </app-card>
```

## Referencias Cruzadas

- [[frontend]] - Desenvolvimento frontend com React/Vue
- [[backend]] - Backend com WebSockets e APIs em tempo real
- [[api-design]] - Design de APIs REST e GraphQL
- [[Web-Components]] - Componentes web reutilizaveis
- [[testing-advanced]] - Testes de performance e seguranca
