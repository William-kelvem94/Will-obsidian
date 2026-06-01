---
title: "AI Local Gratuita"
description: "Ollama, Whisper, TTS, RAG, FAISS para Jarvis/Auto-boletos/DEEP-LEARNING."
tags:
  - ai
  - projetos
  - local
  - gratuita
updated: 2026-06-01
date: 2026-04-27
---

# AI Local Gratuita [[README]]

Para evoluir Jarvis, IA-LOCAL, Auto-boletos OCR:

**Ollama (LLMs locais)**:
- Install: `curl -fsSL https://ollama.com/install.sh | sh`
- Models: `ollama run qwen2.5-coder` (coding), `llama3.2` (general)
- Tut: https://ollama.com/library (gratuito, GPU/CPU)

**Whisper (Speech2Text local)**:
- `pip install openai-whisper`
- Models: tiny/base/small (RTF <1s)
- Tut: https://github.com/openai/whisper (offline)

**TTS Piper/Coqui (Text2Speech local)**:
- Piper: https://github.com/rhasspy/piper (voz PT-BR baixa latência)
- `pip install TTS` Coqui fork

**RAG/FAISS (memória)**:
- `pip install faiss-cpu sentence-transformers`
- Tut: https://github.com/microsoft/semantic-kernel/tree/main/dotnet/samples (PT-BR RAG)

**Visão MediaPipe (Jarvis)**:
- `pip install mediapipe`
- Face/gesture: https://developers.google.com/mediapipe/solutions/vision/face_landmarker/python (gratuito)

**Integração com projetos**:
- Jarvis: Ollama + Whisper + Piper + MediaPipe
- Auto-boletos: Whisper OCR fallback + Ollama análise boleto

Recursos: [[README]] #ollama #whisper #mediapipe
