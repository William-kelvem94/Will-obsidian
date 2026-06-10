---
title: "Evolução IA-LOCAL (JARVIS)"
description: "FAISS memória avançada, Whisper Turbo, Piper TTS PT-BR, pyautogui stealth."
tags:
  - jarvis
  - projetos
  - evolucao
date: 2026-04-27
updated: 2026-06-10
---

# Evolução IA-LOCAL (JARVIS) [[README]]

**Atual**: JARVIS Python FAISS Whisper PC control, OpenRouter.

**Melhorias gratuitas/locais**:

1. **Memória FAISS + Hybrid Search**:
   - Faiss-cpu + BM25 hybrid (melhor recall)
   - `pip install rank-bm25 faiss-cpu`
   - Index incremental + chunking semântico sentence-transformers
   - Tut: https://github.com/langchain-ai/langchain (community edition free)

2. **Voice Turbo Local**:
   - Whisper faster-whisper (2x speed): `pip install faster-whisper`
   - Piper TTS PT-BR voices: https://github.com/rhasspy/piper/releases (voices/wavs pt-BR ultra-low-latency)
   - Distil-Whisper small (50% faster): `pip install distil-whisper`

3. **PC Control Stealth**:
   - Pyautogui + pydirectinput (anti-detection games)
   - `pip install pydirectinput keyboard` (hotkeys silenciosas)

4. **Offline LLM Ollama**:
   - Migre OpenRouter para Ollama local em jarvis_brain.py
   - Model: `ollama run llama3.2:3b` (rápido CPU)

**Roadmap**:
- [ ] Hybrid FAISS + BM25 memory
- [ ] Piper TTS + faster-whisper
- [ ] Ollama local replace API

Recursos: [[AI-Local-Gratuita]] [[README]] #faiss #whisper #piper
