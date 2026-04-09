---
title: "Estudos Focado: PROJECT_JARVIS_5.0"
description: "Análise + roadmap voice AI vision."
tags:
  - jarvis
  - analise
---

# Estudos Focado: PROJECT_JARVIS_5.0 [[README]] [[Privados/PROJECT_JARVIS_5.0]]

**Status Atual**:
- Tecnologias: FastAPI, Next.js shadcn Tailwind, LiveKit agents voice, MediaPipe face/gesture/voice, Playwright browser.
- Forças: Real-time low-latency voice, vision models gratuitos, dashboard monitoring, docker compose.
- Fraquezas: Depend Gemini (custo), no offline LLM, browser não stealth.

**Análise**:
- Scope: Assistente voz/vision PC control.
- Ambitions: Jarvis offline total (Ollama + Piper), multi-modal (vision + voice + screen), agente autônomo tasks.

**Roadmap gratuito**:

**MVP 1.0 Offline (1 mês)**:
- Ollama backend/agents_worker.py + Piper TTS.
- YOLOv8 nano object detection.

**1.5 Prod (2 meses)**:
- Docker swarm multi-node local.
- gRPC agents + VSCode ext integration.

**2.0 Autônomo (4 meses)**:
- LangGraph agents (multi-step reasoning).
- Screen OCR Tesseract + voice command parse.

**Cronograma**:
| Fase | Tempo | Deliver |
|------|-------|---------|
| 1.0 Offline | 4 sem | Ollama/Piper 100% local |
| 1.5 Prod | 8 sem | Swarm monitoring |
| 2.0 Agent | 16 sem | LangGraph autonomy |

Recursos: [[EstudosPesquisas/PROJECT_JARVIS_5.0]] [[AI-Local-Gratuita]] #livekit #ollama

## Detalhamento Expandido
- Escopo atual: assistente multimodal com voz em tempo real, visão e browser automation.
- Tecnologias usadas: FastAPI, Next.js shadcn, LiveKit, MediaPipe, Playwright.
- Limitações atuais: dependência de Gemini e falta de LLM offline completo.
- Entregáveis chave:
  - backend Ollama local + Piper TTS
  - object detection YOLOv8 nano
  - Docker Swarm local e gRPC para agents

### Riscos e pontos de atenção
- Requisitos de hardware para visão e áudio em tempo real podem ser altos.
- Integração browser + automação precisa ser robusta contra falhas de foco.
- Multi-modalidade aumenta a superfície de teste e manutenção.

## Diário de Bordo
- 09/04/2026 10:56:11: arquivo criado/atualizado com visão Jarvis e stack atual.
- 09/04/2026 10:56:14: roadmap dividido entre offline, produção e autonomia.
- Status de versão: nota local, sem histórico Git rastreado para este arquivo.

### Próximas ações concretas
- Implementar backend Ollama e testar fluxo de voz end-to-end.
- Adicionar detecção de objetos com YOLOv8 e OCR de tela.
- Preparar arquitetura de Docker Swarm e gRPC agents.
- Documentar tarefas autônomas e integração com VSCode/desktop.
