---
title: "Jarvis Tools and Technologies"
description: "Lista de ferramentas e tecnologias usadas pelo Jarvis e seus papéis no projeto." 
tags:
  - jarvis
  - jarvis-engenharia
  - tools
  - tech
updated: 2026-06-05
date: 2026-04-27
---

# Jarvis Tools and Technologies

Esta nota descreve as ferramentas principais do Jarvis e como cada uma contribui para o ecossistema do projeto.

## 1. LiveKit

### Descrição
- Comunicação de voz em tempo real.
- Transporte de áudio bidirecional para front-end e backend.
- Ideal para reuniões e interação instantânea.

### Configuração
```python
# Backend - FastAPI
from livekit import api, rtc

# .env
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_secret

# Criar token de acesso
async def gerar_token(usuario: str, sala: str):
    token = api.AccessToken(
        api_key=settings.LIVEKIT_API_KEY,
        api_secret=settings.LIVEKIT_API_SECRET
    )
    token.with_identity(usuario)
    token.with_name(usuario)
    token.with_grants(api.VideoGrants(
        room_join=True,
        room=sala,
    ))
    return token.to_jwt()

# Conectar ao room
async def conectar_sala(token: str):
    room = rtc.Room()
    await room.connect(settings.LIVEKIT_URL, token)
    return room
```

```typescript
// Frontend - Next.js
import { Room, RoomEvent } from 'livekit-client';

const conectarVoz = async (token: string) => {
  const room = new Room();
  
  await room.connect('ws://localhost:7880', token);
  
  room.on(RoomEvent.TrackSubscribed, (track) => {
    if (track.kind === 'audio') {
      const audioElement = track.attach();
      document.body.appendChild(audioElement);
    }
  });
  
  return room;
};
```

### Comandos Docker
```bash
# Rodar servidor LiveKit local
docker run --rm \
  -p 7880:7880 \
  -p 7881:7881 \
  -p 7882:7882/udp \
  -e LIVEKIT_KEYS="your_key: your_secret" \
  livekit/livekit-server:latest
```

## 2. Piper

### Descrição
- Síntese de voz local (TTS).
- Cria respostas de voz com timbre natural.
- Usado para tornar Jarvis falante e interativo.

### Instalação e Uso
```bash
# Instalar Piper
pip install piper-tts

# Baixar modelos de voz
# Português BR
wget https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/pt_BR-faber-medium.onnx
wget https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/pt_BR-faber-medium.onnx.json
```

```python
# Backend - Integração
import subprocess
import tempfile
from pathlib import Path

class PiperTTS:
    def __init__(self, model_path: str):
        self.model_path = Path(model_path)
    
    async def sintetizar(self, texto: str) -> bytes:
        """Converte texto em áudio WAV"""
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            output_path = f.name
        
        # Executar Piper
        processo = subprocess.Popen(
            [
                "piper",
                "--model", str(self.model_path),
                "--output_file", output_path
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        processo.communicate(input=texto.encode("utf-8"))
        
        # Ler arquivo de áudio
        with open(output_path, "rb") as audio_file:
            audio_data = audio_file.read()
        
        Path(output_path).unlink()  # Deletar temporário
        return audio_data

# Uso
tts = PiperTTS("models/pt_BR-faber-medium.onnx")
audio = await tts.sintetizar("Olá, como posso ajudar?")
```

### Vozes Recomendadas
- **Português BR**: `pt_BR-faber-medium` (voz masculina, natural)
- **Inglês US**: `en_US-lessac-medium` (voz feminina, clara)
- **Qualidade**: low (rápido) < medium (balanceado) < high (melhor qualidade)

## 3. MediaPipe
- Detecção facial e análise de gestos.
- Extração de landmarks e comportamento em vídeo.
- Serve como base para visão multimodal.

## 4. YOLOv8
- Detecção de objetos em tempo real.
- Permite reconhecer elementos do ambiente.
- Útil em automações de visão e alertas de segurança.

## 5. Playwright
- Automação de browser controlada.
- Permite execução autônoma de tarefas web.
- Útil para navegar, preencher formulários e coletar dados.

## 6. FastAPI
- Backend Python eficiente e fácil de escalar.
- Exposição de APIs para agentes, visão e controle.
- Base para orquestração de serviços.

## 7. Next.js
- Interface web moderna para controle e visualização.
- Permite dashboards e páginas interativas.
- Combina com LiveKit para experiência multimodal.

## 8. Modelos LLM

### Descrição
- Responsável pela inteligência de linguagem.
- Pode usar Gemini, OpenAI ou modelos locais.
- Suporta geração de texto, entendimento e planejamento.

### Ollama - Setup Local
```bash
# Instalar Ollama (Windows)
winget install Ollama.Ollama

# Baixar modelos recomendados
ollama pull llama3.1:8b          # Modelo geral balanceado
ollama pull qwen2.5:7b           # Excelente em PT-BR
ollama pull deepseek-coder:6.7b  # Especializado em código
ollama pull mistral:7b           # Rápido e eficiente

# Testar modelo
ollama run llama3.1:8b "Olá, como você funciona?"
```

### Integração Python
```python
import ollama
from typing import List, Dict

class LocalLLM:
    def __init__(self, model: str = "llama3.1:8b"):
        self.model = model
        self.client = ollama.Client()
    
    async def completar(
        self,
        mensagens: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 2000
    ) -> str:
        """Gera resposta do LLM"""
        response = await self.client.chat(
            model=self.model,
            messages=mensagens,
            options={
                "temperature": temperature,
                "num_predict": max_tokens
            }
        )
        return response["message"]["content"]
    
    async def completar_com_funcoes(
        self,
        mensagens: List[Dict[str, str]],
        funcoes: List[Dict]
    ) -> Dict:
        """Function calling para execução de ações"""
        response = await self.client.chat(
            model=self.model,
            messages=mensagens,
            tools=funcoes
        )
        return response

# Exemplo de uso com RAG
class JarvisLLM:
    def __init__(self):
        self.llm = LocalLLM("llama3.1:8b")
        self.rag = RAGSystem()  # Sistema de retrieval
    
    async def responder(self, pergunta: str) -> str:
        # 1. Buscar contexto relevante
        contexto = await self.rag.buscar(pergunta)
        
        # 2. Construir prompt com contexto
        mensagens = [
            {
                "role": "system",
                "content": f"Você é o Jarvis. Use o contexto: {contexto}"
            },
            {
                "role": "user",
                "content": pergunta
            }
        ]
        
        # 3. Gerar resposta
        resposta = await self.llm.completar(mensagens)
        return resposta
```

### Comparação de Modelos

| Modelo | Tamanho | Velocidade | Qualidade | Uso Recomendado |
|--------|---------|------------|-----------|------------------|
| Llama 3.1 8B | 4.7GB | Média | Alta | Geral, conversas |
| Qwen 2.5 7B | 4.4GB | Rápida | Alta | PT-BR, matemática |
| DeepSeek Coder | 3.8GB | Rápida | Média | Código, debugging |
| Mistral 7B | 4.1GB | Muito rápida | Média | Respostas rápidas |

### System Prompts Recomendados
```python
SYSTEM_PROMPTS = {
    "tecnico": """
        Você é Jarvis, um assistente técnico especializado em
        desenvolvimento fullstack. Seja direto, objetivo e fornecer
        exemplos de código quando relevante.
    """,
    
    "amigavel": """
        Você é Jarvis, um assistente amigável e prestativo.
        Use linguagem calorosa e encoraje o usuário.
        Explique conceitos de forma clara e acessível.
    """,
    
    "filosofico": """
        Você é Jarvis, um assistente reflexivo que ajuda
        o usuário a pensar profundamente sobre questões.
        Faça perguntas instigantes e ofereça perspectivas únicas.
    """
}
```

## 9. RAG / FAISS

### Descrição
- Recuperação de informações da KB.
- Indexação semântica dos documentos.
- Permite ao Jarvis responder com base em seu próprio conhecimento.

### Setup e Implementação
```python
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from pathlib import Path
import json

class RAGSystem:
    def __init__(self, kb_path: str):
        self.kb_path = Path(kb_path)
        self.encoder = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.documentos = []
        
    def indexar_conhecimento(self):
        """Indexa todos os arquivos .md do Knowledge Base"""
        documentos = []
        
        # Ler todos os arquivos markdown
        for md_file in self.kb_path.rglob("*.md"):
            with open(md_file, 'r', encoding='utf-8') as f:
                conteudo = f.read()
                
            # Dividir em chunks
            chunks = self._dividir_em_chunks(conteudo)
            
            for chunk in chunks:
                documentos.append({
                    "arquivo": md_file.name,
                    "caminho": str(md_file),
                    "conteudo": chunk
                })
        
        self.documentos = documentos
        
        # Gerar embeddings
        textos = [doc["conteudo"] for doc in documentos]
        embeddings = self.encoder.encode(textos)
        
        # Criar índice FAISS
        dimensao = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimensao)
        self.index.add(embeddings.astype('float32'))
        
        print(f"Indexados {len(documentos)} chunks")
    
    def _dividir_em_chunks(
        self,
        texto: str,
        tamanho_chunk: int = 500,
        overlap: int = 50
    ) -> List[str]:
        """Divide texto em chunks com overlap"""
        palavras = texto.split()
        chunks = []
        
        for i in range(0, len(palavras), tamanho_chunk - overlap):
            chunk = ' '.join(palavras[i:i + tamanho_chunk])
            chunks.append(chunk)
        
        return chunks
    
    async def buscar(
        self,
        query: str,
        top_k: int = 5
    ) -> List[Dict]:
        """Busca documentos relevantes"""
        # Gerar embedding da query
        query_embedding = self.encoder.encode([query])
        
        # Buscar no índice
        distancias, indices = self.index.search(
            query_embedding.astype('float32'),
            top_k
        )
        
        # Retornar documentos relevantes
        resultados = []
        for i, idx in enumerate(indices[0]):
            doc = self.documentos[idx]
            resultados.append({
                **doc,
                "score": float(distancias[0][i])
            })
        
        return resultados
    
    def salvar_index(self, caminho: str):
        """Persiste índice em disco"""
        faiss.write_index(self.index, f"{caminho}/faiss.index")
        
        with open(f"{caminho}/documentos.json", 'w') as f:
            json.dump(self.documentos, f, ensure_ascii=False)
    
    def carregar_index(self, caminho: str):
        """Carrega índice do disco"""
        self.index = faiss.read_index(f"{caminho}/faiss.index")
        
        with open(f"{caminho}/documentos.json", 'r') as f:
            self.documentos = json.load(f)

# Uso
rag = RAGSystem("C:/Users/willi/Documents/GitHub/Will-obsidian/JARVIS/KnowledgeBase")
rag.indexar_conhecimento()
rag.salvar_index("./rag_index")

# Buscar
resultados = await rag.buscar("Como implementar autenticação JWT?")
for res in resultados:
    print(f"Arquivo: {res['arquivo']}")
    print(f"Score: {res['score']}")
    print(f"Conteúdo: {res['conteudo'][:200]}...\n")
```

### Estratégias Avançadas
```python
# Reranking com cross-encoder
from sentence_transformers import CrossEncoder

class AdvancedRAG(RAGSystem):
    def __init__(self, kb_path: str):
        super().__init__(kb_path)
        self.reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
    
    async def buscar_com_rerank(
        self,
        query: str,
        top_k: int = 20,
        final_k: int = 5
    ) -> List[Dict]:
        # 1. Busca inicial (mais resultados)
        candidatos = await self.buscar(query, top_k)
        
        # 2. Reranking com cross-encoder
        pares = [[query, doc["conteudo"]] for doc in candidatos]
        scores = self.reranker.predict(pares)
        
        # 3. Ordenar por score e retornar top final_k
        for doc, score in zip(candidatos, scores):
            doc["rerank_score"] = float(score)
        
        candidatos.sort(key=lambda x: x["rerank_score"], reverse=True)
        return candidatos[:final_k]
```

## 10. Docker e scripts auxiliares

### Descrição
- Facilita o deploy e o gerenciamento de serviços.
- Scripts PowerShell e batch ajudam a iniciar o ambiente.
- Útil para padronizar o setup local.

### Docker Compose - Jarvis Stack
```yaml
# docker-compose.yml
version: '3.8'

services:
  # Backend FastAPI
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      - JARVIS_KB_PATH=/app/knowledge
      - OLLAMA_HOST=http://ollama:11434
      - REDIS_URL=redis://redis:6379
    volumes:
      - ./JARVIS/KnowledgeBase:/app/knowledge:ro
      - ./backend:/app
    depends_on:
      - redis
      - ollama
    restart: unless-stopped
  
  # Frontend Next.js
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8000
    volumes:
      - ./frontend:/app
    restart: unless-stopped
  
  # Ollama para LLM local
  ollama:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    restart: unless-stopped
  
  # Redis para cache
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    restart: unless-stopped
  
  # LiveKit para voz
  livekit:
    image: livekit/livekit-server:latest
    ports:
      - "7880:7880"
      - "7881:7881"
      - "7882:7882/udp"
    environment:
      - LIVEKIT_KEYS=jarvis_key: jarvis_secret
    restart: unless-stopped

volumes:
  ollama_data:
  redis_data:
```

### Scripts de Gerenciamento
```powershell
# start-jarvis.ps1
# Script completo para iniciar o Jarvis

Write-Host "Iniciando Jarvis..." -ForegroundColor Cyan

# 1. Verificar dependências
Write-Host "Verificando Docker..." -ForegroundColor Yellow
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "Docker não encontrado! Instale o Docker Desktop." -ForegroundColor Red
    exit 1
}

# 2. Verificar .env
if (-not (Test-Path ".env")) {
    Write-Host "Criando .env a partir do template..." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env"
}

# 3. Construir e iniciar serviços
Write-Host "Construindo containers..." -ForegroundColor Yellow
docker-compose build

Write-Host "Iniciando serviços..." -ForegroundColor Yellow
docker-compose up -d

# 4. Aguardar serviços
Write-Host "Aguardando serviços ficarem prontos..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

# 5. Baixar modelo Ollama se necessário
Write-Host "Verificando modelo LLM..." -ForegroundColor Yellow
$modeloExiste = docker exec jarvis-ollama-1 ollama list | Select-String "llama3.1:8b"
if (-not $modeloExiste) {
    Write-Host "Baixando modelo llama3.1:8b..." -ForegroundColor Yellow
    docker exec jarvis-ollama-1 ollama pull llama3.1:8b
}

# 6. Verificar saúde dos serviços
Write-Host "Verificando saúde dos serviços..." -ForegroundColor Yellow
$services = @(
    @{Name="Backend"; Url="http://localhost:8000/health"},
    @{Name="Frontend"; Url="http://localhost:3000"},
    @{Name="Ollama"; Url="http://localhost:11434"}
)

foreach ($service in $services) {
    try {
        $response = Invoke-WebRequest -Uri $service.Url -TimeoutSec 5
        Write-Host "$($service.Name): OK" -ForegroundColor Green
    } catch {
        Write-Host "$($service.Name): ERRO" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "Jarvis está pronto!" -ForegroundColor Green
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Cyan
Write-Host "API: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Para parar: docker-compose down" -ForegroundColor Yellow
```

```bash
# stop-jarvis.sh (Linux/Mac)
#!/bin/bash
echo "Parando Jarvis..."
docker-compose down
echo "Jarvis parado."
```

### Comandos Úteis
```bash
# Iniciar tudo
docker-compose up -d

# Ver logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Reconstruir após mudanças
docker-compose up -d --build

# Parar tudo
docker-compose down

# Limpar volumes (reset completo)
docker-compose down -v

# Executar comando no container
docker-compose exec backend python -m pytest

# Ver uso de recursos
docker stats
```

## Como usar esta nota
- Referencie aqui quando for decidir se deve adicionar uma nova biblioteca ou serviço.
- Atualize sempre que a stack mudar ou houver nova integração importante.
- Use os exemplos de código como referência para implementação.
- Mantenha as configurações Docker atualizadas conforme o projeto evolui.

[[JARVIS/README|← Voltar ao Command Center]]
