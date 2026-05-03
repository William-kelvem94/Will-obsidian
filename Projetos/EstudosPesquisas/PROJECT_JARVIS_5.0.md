---
title: "Evolução PROJECT_JARVIS_5.0"
description: "Melhorias LiveKit + Ollama local, MediaPipe vision gratuita, FastAPI scaling."
tags:
  - jarvis
  - projetos
  - evolucao
date: 2026-04-27
updated: 2026-05-03
---

# Evolução PROJECT_JARVIS_5.0 [[README]]

**Atual**: FastAPI Next LiveKit voice, MediaPipe face/gesture, browser Playwright.

**Melhorias gratuitas/locais**:

1. **Voice AI Local Ollama**:
   - Integre Ollama em backend/agents_worker.py (substitua Gemini)
   - LiveKit + Ollama STT/TTS Piper para offline total
   - Tut: https://livekit.io/agents/ollama/ (exato para Jarvis)

2. **Visão Avançada Gratuita**:
   - MediaPipe + YOLOv8 nano local (object detection gratuita)
   - `pip install ultralytics mediapipe` - detecção objetos + gesture
   - Tut: https://github.com/roboflow/notebooks (YOLOv8 PT-BR)

3. **FastAPI Prod Docker**:
   - Uvicorn Gunicorn cluster + Traefik
   - docker-compose.prod.yml com volumes persistentes

4. **Next.js Performance**:
   - Turbopack, App Router otimizado, shadcn forms + Zod

**Roadmap**:
- [ ] Ollama + Piper STT/TTS offline
- [ ] YOLOv8 object detection
- [ ] Docker swarm self-hosted

Recursos: [[AI-Local-Gratuita]] [[README]] #livekit #mediapipe #ollama
