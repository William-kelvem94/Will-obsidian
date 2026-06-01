---
title: "PROJECT_JARVIS_5.0 Codebase Map"
description: "Mapa RAG-friendly do monorepo PROJECT_JARVIS_5.0 para agentes de programacao."
created: 2026-05-08
updated: 2026-06-01
type: codebase-map
project: PROJECT_JARVIS_5.0
domain: engineering
language_primary: Python
language_secondary: TypeScript
code_root: "D:/DOCUMENTOS/GitHub/PROJECT_JARVIS_5.0"
vault_sources:
  - "Projetos/01-Ativos/Privados/PROJECT_JARVIS_5.0.md"
  - "Projetos/03-Estudos/EstudosPesquisas/PROJECT_JARVIS_5.0.md"
confidence: observed-local-code-and-vault-notes
tags:
  - project-jarvis-5
  - jarvis-engenharia
  - fastapi
  - nextjs
  - livekit
  - perception
  - rag
  - codebase-map
date: 2026-06-01
---

# PROJECT_JARVIS_5.0 Codebase Map

## One-liner

PROJECT_JARVIS_5.0 e um monorepo de assistente multimodal: backend FastAPI, frontend Next.js 15, telemetria, percepcao local, automacao de browser, segundo cerebro Obsidian e motor de IA em cascata.

## Fontes locais relevantes

- Nota de projeto: [[Projetos/01-Ativos/Privados/PROJECT_JARVIS_5.0]]
- Nota de evolucao: [[Projetos/03-Estudos/EstudosPesquisas/PROJECT_JARVIS_5.0]]
- Knowledge base: [[Projetos/01-Ativos/Privados/PROJECT_JARVIS_5.0-KnowledgeBase/README]]
- Codigo real lido em modo somente leitura: `D:\DOCUMENTOS\GitHub\PROJECT_JARVIS_5.0`

## Estrutura observada no codigo real

| Caminho | Papel para agentes |
|---|---|
| `README.md` | Visao canonica de boot, arquitetura, portas, stack e testes. |
| `package.json` | Scripts raiz para frontend, backend e Docker. |
| `start-jarvis.bat` | Boot oficial citado no README. |
| `backend/app/main.py` | Provavel entrada FastAPI principal. Leia antes de alterar rotas. |
| `backend/app/routes.py` | Rotas HTTP agregadas. Bom ponto para entender contrato API. |
| `backend/app/chat_pipeline.py` | Pipeline de chat e orquestracao conversacional. |
| `backend/app/smart_router.py` | Roteamento inteligente entre provedores/capacidades. |
| `backend/app/kb_loader.py` | Carregamento da base de conhecimento local. |
| `backend/app/utils/second_brain_connector.py` | Conector do segundo cerebro Obsidian. |
| `backend/app/utils/obsidian_graph.py` | Grafo Obsidian; relevante para links e memoria contextual. |
| `backend/app/perception/` | Face, gesture, object e voice engines. |
| `backend/app/voice/` | TTS e barge-in. |
| `backend/app/tools/` | Ferramentas acionaveis: browser, arquivos, memoria, percepcao, OS e AI. |
| `backend/app/security/` | Biometria, sentinel, blackbox e holodeck. Tratar como area sensivel. |
| `backend/app/telemetry_server.py` | Servico de telemetria na porta 8001. |
| `frontend/app/` | App Router do Next.js. |
| `frontend/components/app/` | Experiencia principal do cockpit. |
| `frontend/components/cockpit/` | HUD, painel, console, orb e telemetria. |
| `frontend/components/agents-ui/` | Componentes de controle e visualizacao de agente/voz. |
| `frontend/lib/jarvis-endpoints.ts` | Cliente/contratos de chamadas ao backend. |
| `frontend/hooks/` | Hooks de voz, debug, telemetria, reconnect e dados Jarvis. |
| `docs/` | Arquitetura, install, startup, health, multi-agent e auditorias. |
| `scripts/` | Diagnosticos, start, restart, setup, monitor e validadores. |
| `docker-compose.yml` | Composicao raiz para executar servicos via Docker. |

## Stack e dependencias observadas

- Backend: Python, FastAPI, Uvicorn, pydantic-settings, aiohttp, requests, loguru, psutil, watchfiles.
- Percepcao: MediaPipe, OpenCV, NumPy, Ultralytics/YOLOv8, mss, Pillow, PyAutoGUI, onnxruntime.
- Voz: openwakeword, WebRTC VAD, librosa, faster-whisper, sounddevice, edge-tts, pygame.
- Memoria e RAG: ChromaDB, sentence-transformers, faiss-cpu, NetworkX segundo o README.
- Browser e automacao: Playwright, watchdog.
- Frontend: Next.js 15.5.9, React 19, Tailwind CSS 4, Motion, Radix UI, lucide-react, shadcn-style components, Three/Vanta/Rive.
- Testes: pytest no backend; Jest, Testing Library, ESLint e TypeScript no frontend.

## Comandos e portas citados

| Objetivo | Comando/porta |
|---|---|
| Boot oficial | `start-jarvis.bat` |
| Frontend dev | `pnpm --dir frontend dev` ou `pnpm dev` na raiz |
| Backend dev | `cd backend && uvicorn app.main:app --reload` |
| Docker | `docker compose up --build` |
| Teste raiz | `python -m unittest discover -s backend -p 'test*.py'` |
| Teste backend recomendado no README | `cd backend && python -m pytest tests/ -v` |
| Teste frontend | `pnpm --dir frontend test` |
| Typecheck frontend | `pnpm --dir frontend typecheck` |
| API | `http://localhost:8000` |
| Telemetria | `http://localhost:8001` |
| Cockpit | `http://localhost:3000` |

## Modelo mental para agentes

1. Entrada do usuario chega pelo cockpit Next.js ou por API/backend.
2. Frontend conversa com backend via endpoints centralizados em `frontend/lib/jarvis-endpoints.ts`.
3. Backend roteia chat/capacidades por `chat_pipeline.py`, `smart_router.py`, `engineer_brain.py` e ferramentas em `backend/app/tools/`.
4. Segundo cerebro entra por `kb_loader.py`, `second_brain_connector.py` e grafo Obsidian.
5. Percepcao e voz ficam em modulos separados para face, gesto, objeto, engine de voz, TTS e barge-in.
6. Telemetria roda como servico separado, util para dashboards e diagnosticos.

## Areas que pedem cuidado

- `.env`, `env/.env`, `frontend/.env*` e logs locais podem conter segredos ou dados privados.
- `backend/app/security/` tem semantica de seguranca; altere apenas com testes e leitura completa.
- `backend/app/tools/system_executor.py` e ferramentas de OS podem executar comandos. Valide permissoes e limites.
- Automacao de browser/desktop depende de foco, estado da tela e ambiente Windows.
- Percepcao e voz usam dependencias pesadas; mudancas podem quebrar instalacao em maquinas CPU/GPU diferentes.
- Existem pastas historicas em `docs/archive/research/`; trate como referencia, nao fluxo canonico.

## Proximos probes seguros

- Ler `docs/guides/JARVIS_STARTUP.md`, `docs/ROOT_STRUCTURE.md`, `docs/ARCHITECTURE.md` e `docs/LOCAL_ARCHITECTURE_V5.md`.
- Mapear endpoints FastAPI com `rg -n "APIRouter|@app|@router" backend/app`.
- Mapear chamadas frontend ao backend com `rg -n "fetch|jarvis|api" frontend/lib frontend/hooks frontend/components`.
- Mapear testes existentes antes de editar: `rg --files backend/tests frontend/__tests__ frontend | rg "test|spec"`.
- Confirmar se o roteiro atual usa LM Studio, Gemini, OpenRouter, Ollama ou fallback misto lendo `backend/app/config.py` e `backend/app/smart_router.py`.

## Tarefas provaveis para agentes

- Estabilizar contrato API entre `frontend/lib/jarvis-endpoints.ts` e rotas FastAPI.
- Criar testes de integracao para chat, telemetria e status de capacidades.
- Documentar comandos individuais de desenvolvimento alem do `start-jarvis.bat`.
- Implementar ou validar modo offline total com Ollama sem remover fallback existente.
- Melhorar observabilidade de percepcao/voz sem bloquear o boot quando hardware ou modelo faltar.

## Perguntas abertas

- Qual provider de LLM deve ser padrao em ambiente local: LM Studio, Ollama, Gemini ou OpenRouter?
- O backend canonico e `backend/app/main.py` apenas, ou existem shims historicos ainda usados?
- O frontend atual deve preservar a UI "Luxury Cockpit" ou migrar para uma superficie operacional mais simples?
- Quais testes sao obrigatorios antes de mexer em percepcao, voz ou ferramentas de OS?

[[JARVIS/04-Engineering/Codebase-Maps/INDEX|← Voltar ao índice de Codebase-Maps]]
