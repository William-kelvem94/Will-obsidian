---
title: "Estudos Focado: IA-LOCAL (JARVIS)"
description: "Análise assistente + roadmap autônomo."
tags:
  - jarvis
  - analise
---

# Estudos Focado: IA-LOCAL [[README]] [[Privados/IA-LOCAL]]

**Status Atual**:
- Tecnologias: Python FAISS memory, Whisper voice, pyautogui PC control, OpenRouter LLM.
- Forças: Memória vetorial FAISS, voice interface, start.bat fácil.
- Fraquezas: Depend API LLM, Whisper lento CPU, pyautogui detectável, no vision/multi-modal.

**Análise**:
- Scope: Assistente texto/voz PC básico.
- Ambitions: Jarvis full offline multi-modal (voice/vision/screen/tasks autônomas).

**Roadmap gratuito**:

**MVP 1.0 Offline (1 mês)**:
- Ollama llama3.2:3b local replace OpenRouter.
- faster-whisper + Piper TTS PT-BR.

**1.5 Vision (2 meses)**:
- MediaPipe face/gesture + Tesseract screen OCR.

**2.0 Autônomo (4 meses)**:
- LangGraph multi-agent (planning + execution).
- PyAutoGUI stealth + pydirectinput.

**Cronograma**:
| Fase | Tempo | Deliver |
|------|-------|---------|
| 1.0 Offline | 4 sem | Ollama/Piper |
| 1.5 Vision | 8 sem | MediaPipe OCR |
| 2.0 Agent | 16 sem | LangGraph tasks |

Recursos: [[EstudosPesquisas/IA-LOCAL]] [[AI-Local-Gratuita]] #ollama #mediapipe

## Detalhamento Expandido
- Escopo atual: assistente pessoal local com memória vetorial, voz e controle básico de PC.
- Tecnologias usadas: Python, FAISS, Whisper, pyautogui, OpenRouter.
- Falta principal: motor offline para LLM e visão multimodal mais confiável.
- Entregáveis chave:
  - substituição de OpenRouter por Ollama local
  - integração de faster-whisper e Piper TTS PT-BR
  - visão com MediaPipe e OCR de tela

### Riscos e pontos de atenção
- PyAutoGUI pode ser detectável e frágil em diferentes resoluções de tela.
- Whisper CPU pode ser lento para uso em tempo real.
- Mais sensores adicionam complexidade e necessidade de testes em Windows.

## Diário de Bordo
- 09/04/2026 10:56:40: arquivo criado/atualizado com foco no Jarvis local.
- 09/04/2026 10:56:43: definido roadmap offline, visão e autonomia.
- Status de versão: nota local, sem histórico Git rastreado para este arquivo.

### Próximas ações concretas
- Configurar Ollama local e testar inferência no PC.
- Trocar Whisper por faster-whisper e integrar Piper TTS.
- Adicionar pipeline de visão com MediaPipe e OCR de tela.
- Criar rotina de logs de uso e segurança para automações.
