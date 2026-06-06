---
title: "Configuração do Jarvis"
description: "Variáveis de ambiente, caminhos e configurações centralizadas do sistema Jarvis."
tags:
  - jarvis
  - jarvis-operacao
  - config
  - ambiente
  - setup
updated: 2026-06-05
date: 2026-04-27
---

# Configuração do Jarvis

Este documento centraliza todas as variáveis de ambiente, caminhos e configurações necessárias para executar o Jarvis.

## Variáveis de Ambiente Essenciais

### Caminhos do Sistema

```bash
# Knowledge Base - Segundo Cérebro
JARVIS_KB_PATH=C:\Users\willi\Documents\GitHub\Will-obsidian\JARVIS\KnowledgeBase

# Código do Projeto
JARVIS_PROJECT_ROOT=C:\Users\willi\Documents\GitHub\PROJECT_JARVIS_5.0

# Vault Obsidian Principal
JARVIS_VAULT_ROOT=D:\OBSIDIAN\Will

# Clone do Vault para IA Local
JARVIS_OBSIDIAN_CLONE=C:\Users\willi\Documents\GitHub\Will-obsidian
```

### Modelos de IA

```bash
# LLM Local (Ollama)
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.1:8b

# Modelos Alternativos
OLLAMA_MODEL_CODE=deepseek-coder:6.7b
OLLAMA_MODEL_FAST=mistral:7b
OLLAMA_MODEL_MULTILANG=qwen2.5:7b

# Embeddings
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
EMBEDDING_DIMENSION=384
```

### Serviços de Voz

```bash
# Text-to-Speech (Piper)
PIPER_MODEL_PATH=./models/pt_BR-faber-medium.onnx
PIPER_VOICE=pt_BR-faber-medium

# Speech-to-Text (Whisper)
WHISPER_MODEL=medium
WHISPER_LANGUAGE=pt

# LiveKit
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=jarvis_key
LIVEKIT_API_SECRET=jarvis_secret
```

### Visão Computacional

```bash
# Configurações de Câmera
JARVIS_CAMERA_INDEX=0
JARVIS_CAMERA_FPS=30
JARVIS_CAMERA_WIDTH=640
JARVIS_CAMERA_HEIGHT=480

# Percepção
JARVIS_PERCEPTION_FPS=1
JARVIS_FACE_DETECTION_CONFIDENCE=0.7
JARVIS_GESTURE_DETECTION_CONFIDENCE=0.8

# YOLOv8
YOLO_MODEL=yolov8n.pt
YOLO_CONFIDENCE=0.5
```

### Banco de Dados e Cache

```bash
# PostgreSQL
DATABASE_URL=postgresql://jarvis:password@localhost:5432/jarvis_db

# Redis
REDIS_URL=redis://localhost:6379
REDIS_TTL=3600

# FAISS
FAISS_INDEX_PATH=./rag_index/faiss.index
FAISS_DOCUMENTS_PATH=./rag_index/documentos.json
```

### Segurança

```bash
# JWT
SECRET_KEY=sua_chave_secreta_aqui_mude_em_producao
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:8000
```

### APIs Externas (Opcional)

```bash
# Fallback para APIs em nuvem
OPENAI_API_KEY=sk-...
GEMINI_API_KEY=...
ANTHROPIC_API_KEY=...

# Usar APIs em nuvem como fallback
USE_CLOUD_FALLBACK=false
```

## Arquivo .env Completo

```bash
# .env
# Copie para seu projeto e ajuste os valores

# ==================== CAMINHOS ====================
JARVIS_KB_PATH=C:\Users\willi\Documents\GitHub\Will-obsidian\JARVIS\KnowledgeBase
JARVIS_PROJECT_ROOT=C:\Users\willi\Documents\GitHub\PROJECT_JARVIS_5.0
JARVIS_VAULT_ROOT=D:\OBSIDIAN\Will
JARVIS_OBSIDIAN_CLONE=C:\Users\willi\Documents\GitHub\Will-obsidian

# ==================== LLM LOCAL ====================
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.1:8b
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# ==================== VOZ ====================
PIPER_MODEL_PATH=./models/pt_BR-faber-medium.onnx
WHISPER_MODEL=medium
WHISPER_LANGUAGE=pt
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=jarvis_key
LIVEKIT_API_SECRET=jarvis_secret

# ==================== VISÃO ====================
JARVIS_CAMERA_INDEX=0
JARVIS_PERCEPTION_FPS=1
YOLO_MODEL=yolov8n.pt

# ==================== DATABASE ====================
DATABASE_URL=postgresql://jarvis:password@localhost:5432/jarvis_db
REDIS_URL=redis://localhost:6379

# ==================== SEGURANÇA ====================
SECRET_KEY=MUDE_ISSO_EM_PRODUCAO_USE_SENHA_FORTE
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# ==================== CORS ====================
CORS_ORIGINS=http://localhost:3000

# ==================== FEATURES ====================
ENABLE_VOICE=true
ENABLE_VISION=true
ENABLE_BROWSER_AUTOMATION=false
USE_CLOUD_FALLBACK=false

# ==================== LOG ====================
LOG_LEVEL=INFO
LOG_FORMAT=json
```

## Configuração Python (Pydantic Settings)

```python
# app/core/config.py
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    """Configurações centralizadas do Jarvis"""
    
    # Caminhos
    jarvis_kb_path: str
    jarvis_project_root: str
    jarvis_vault_root: str
    
    # LLM
    ollama_host: str = "http://localhost:11434"
    ollama_model: str = "llama3.1:8b"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    
    # Voz
    piper_model_path: str = "./models/pt_BR-faber-medium.onnx"
    whisper_model: str = "medium"
    livekit_url: str
    livekit_api_key: str
    livekit_api_secret: str
    
    # Visão
    jarvis_camera_index: int = 0
    jarvis_perception_fps: int = 1
    yolo_model: str = "yolov8n.pt"
    
    # Database
    database_url: str
    redis_url: str
    
    # Segurança
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # CORS
    cors_origins: List[str] = ["http://localhost:3000"]
    
    # Features
    enable_voice: bool = True
    enable_vision: bool = True
    enable_browser_automation: bool = False
    use_cloud_fallback: bool = False
    
    # Log
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# Instância global
settings = Settings()
```

## Validação de Configuração

```python
# scripts/validate_config.py
import sys
from pathlib import Path
from app.core.config import settings

def validar_configuracao():
    """Valida todas as configurações antes de iniciar"""
    
    erros = []
    avisos = []
    
    # Validar caminhos
    kb_path = Path(settings.jarvis_kb_path)
    if not kb_path.exists():
        erros.append(f"Knowledge Base não encontrado: {kb_path}")
    
    # Validar modelos
    piper_path = Path(settings.piper_model_path)
    if settings.enable_voice and not piper_path.exists():
        avisos.append(f"Modelo Piper não encontrado: {piper_path}")
    
    # Validar secrets
    if settings.secret_key == "MUDE_ISSO_EM_PRODUCAO_USE_SENHA_FORTE":
        erros.append("SECRET_KEY ainda está com valor padrão!")
    
    # Validar Ollama
    try:
        import ollama
        ollama.list()
    except Exception as e:
        avisos.append(f"Ollama não está rodando: {e}")
    
    # Mostrar resultados
    if erros:
        print("❌ ERROS DE CONFIGURAÇÃO:")
        for erro in erros:
            print(f"  - {erro}")
        sys.exit(1)
    
    if avisos:
        print("⚠️  AVISOS:")
        for aviso in avisos:
            print(f"  - {aviso}")
    
    print("✅ Configuração validada com sucesso!")

if __name__ == "__main__":
    validar_configuracao()
```

## Checklist de Setup

### Setup Inicial

- [ ] Copiar `.env.example` para `.env`
- [ ] Ajustar todos os caminhos para seu sistema
- [ ] Gerar SECRET_KEY forte: `openssl rand -hex 32`
- [ ] Configurar permissões de acesso aos diretórios

### Serviços Locais

- [ ] Instalar e iniciar Docker
- [ ] Instalar Ollama: `winget install Ollama.Ollama`
- [ ] Baixar modelo LLM: `ollama pull llama3.1:8b`
- [ ] Iniciar Redis: `docker run -d -p 6379:6379 redis:7-alpine`
- [ ] Iniciar PostgreSQL (se usando)

### Modelos de IA

- [ ] Baixar modelo Whisper: executar script de setup
- [ ] Baixar modelo Piper TTS
- [ ] Baixar modelo YOLOv8: `yolo download yolov8n.pt`
- [ ] Baixar modelo de embeddings (automático no primeiro uso)

### Validação

```bash
# Rodar script de validação
python scripts/validate_config.py

# Testar conexões
python scripts/test_connections.py

# Iniciar serviços
docker-compose up -d

# Verificar health
curl http://localhost:8000/health
```

## Troubleshooting

### Erro: "Knowledge Base não encontrado"
- Verifique se `JARVIS_KB_PATH` aponta para pasta correta
- Confirme que a pasta contém arquivos `.md`

### Erro: "Ollama connection refused"
- Verifique se Ollama está rodando: `ollama list`
- Inicie Ollama se necessário

### Erro: "FAISS index not found"
- Execute indexação inicial: `python scripts/index_knowledge_base.py`

### Performance lenta
- Reduza `JARVIS_PERCEPTION_FPS` para 0.5 ou menos
- Use modelo menor: `OLLAMA_MODEL=mistral:7b`
- Desative features não essenciais

## Próximos Passos

1. Configure `.env` baseado neste documento
2. Execute validação: `python scripts/validate_config.py`
3. Inicie serviços: `docker-compose up -d`
4. Acesse dashboard: `http://localhost:3000`
5. Teste comandos de voz: "Hey Jarvis!"

Para mais detalhes, consulte:
- [[Integracao|Integração]] - Como conectar KB ao código
- [[Ferramentas|Ferramentas]] - Setup detalhado de cada ferramenta
- [[Workflows-Praticos|Workflows]] - Exemplos de uso prático

[[JARVIS/README|← Voltar ao Command Center]]
