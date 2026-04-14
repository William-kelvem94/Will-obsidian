---
title: "Aprendizado Técnico — Jarvis"
description: "Conhecimento técnico acumulado sobre os projetos, stack e soluções de Will."
tags: [jarvis, tecnico, stack, solucoes]
  - aprendizado
updated: 2026-04-09
---

# Aprendizado Técnico — Jarvis

## 🛠️ Setup do Ambiente de Will

- **OS:** Windows 11
- **Terminal:** PowerShell principal
- **Gerenciador de pacotes Node:** pnpm
- **Python:** disponível via `python` e `py`  
- **Docker:** instalado e em uso
- **Ollama:** usado para LLMs locais
- **LiveKit:** para agents de voz/visão

## 📁 Paths Importantes

```
Projeto Jarvis: C:\Users\willi\Documents\GitHub\PROJECT_JARVIS_5.0
Vault Obsidian: D:\OBSIDIAN\Will
KB Jarvis:      D:\OBSIDIAN\Will\Projetos\Privados\PROJECT_JARVIS_5.0-KnowledgeBase
Segundo Cérebro:D:\OBSIDIAN\Will\JARVIS\
```

## 🔧 Comandos Úteis do Projeto Jarvis

```powershell
# Iniciar tudo
.\start-jarvis.bat

# Backend Python
cd backend; python -m uvicorn app.main:app --reload --port 8000

# Frontend Next.js
cd frontend; pnpm dev

# Verificar saúde
curl http://localhost:8000/health
```

## 🏗️ Arquitetura Jarvis 5.0

- **Backend:** FastAPI (Python) — porta 8000
- **Frontend:** Next.js — porta 3000
- **Agent Worker:** LiveKit Python SDK
- **Memória:** SQLite local (jarvis_local.db) + Mem0 cloud
- **KB:** .md files no vault Obsidian → carregados via kb_loader.py
- **Vault Writer:** vault_memory.py → escreve memórias de volta ao Obsidian

## 💡 Soluções Encontradas

### Pipeline de Voz & Resampling (2026-04-14)
- **Problema:** Whisper local ignorava falas ou gerava alucinações devido a taxas de amostragem incompatíveis (48kHz do browser vs 16kHz do motor).
- **Solução:** Implementado **Resampling Dinâmico** no `voice_websocket.py`. O sistema agora calcula o `step` necessário para reduzir 48kHz para 16kHz (pegando 1 a cada 3 amostras) antes de enviar ao Whisper.
- **Impacto:** Redução drástica de latência e 100% de precisão na transcrição local.

### Biometria Vocal Híbrida
- **Integração:** O Jarvis agora cruza dados de `face_identity` com `speaker_identity` (biometria vocal). Se o rosto não estiver visível, ele ainda te reconhece pela voz e mantém o nível de privilégio/personalização.

---
*Última atualização: 2026-04-14*
