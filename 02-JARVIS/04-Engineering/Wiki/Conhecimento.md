---
title: "PROJECT_JARVIS_5.0 Knowledge"
description: "Base de conhecimento para Jarvis ser um assistente virtual completo e integrado." 
tags:
  - jarvis
  - jarvis-engenharia
  - knowledge
  - assistant
updated: 2026-06-08
date: 2026-04-27
---

# PROJECT_JARVIS_5.0 Knowledge

Esta nota consolida o conhecimento necessário para Jarvis ser um assistente virtual completo.

## 1. Domínio Técnico: Programador Fullstack
Jarvis deve dominar as principais tecnologias de desenvolvimento:

### Frontend
- **JavaScript/TypeScript**: ES6+, async/await, promises, modules, decorators
- **React/Next.js**: Hooks (useState, useEffect, useContext, useReducer), Server Components, App Router, SSR/SSG
- **Estilização**: Tailwind CSS, CSS Modules, styled-components, responsive design
- **UX/Acessibilidade**: WCAG 2.1, ARIA labels, semantic HTML, keyboard navigation
- **Build Tools**: Vite, Webpack, Turbopack, esbuild

### Backend
- **Python**: FastAPI (async/await, dependency injection, Pydantic), Flask, Django
- **Node.js**: Express, NestJS, middleware patterns, event loop optimization
- **Arquitetura**: Clean Architecture, DDD, microservices, monorepo patterns
- **Autenticação**: JWT, OAuth2, Session-based, RBAC, ABAC

### Banco de Dados
- **SQL**: PostgreSQL (jsonb, índices, particionamento), MySQL, SQLite
- **NoSQL**: MongoDB (aggregation pipeline), Redis (pub/sub, caching)
- **ORMs**: Prisma (schema migrations, relations), SQLAlchemy (Core e ORM), TypeORM
- **Otimização**: Query planning, indexação estratégica, connection pooling

### Infraestrutura e DevOps
- **Containers**: Docker (multi-stage builds, volumes, networks), docker-compose
- **Orquestração**: Docker Swarm, Kubernetes básico
- **CI/CD**: GitHub Actions, GitLab CI, automated testing, deployment pipelines
- **Reverse Proxy**: Traefik (labels, middlewares), Nginx, Caddy
- **Monitoramento**: Logs estruturados, health checks, metrics collection

### APIs e Integrações
- **REST**: RESTful principles, HATEOAS, versioning, pagination
- **GraphQL**: Schema design, resolvers, DataLoader, subscriptions
- **WebSockets**: Real-time communication, Socket.io, LiveKit integration
- **gRPC**: Protocol buffers, streaming, service mesh patterns

## 2. Domínio de IA e Assistência

### Modelos de Linguagem (LLMs)
- **Ollama**: Gerenciamento local de modelos, API compatível com OpenAI
- **Modelos Recomendados**:
  - Llama 3.1 (8B, 70B) - balanceado para raciocínio e código
  - Qwen 2.5 (7B, 14B) - excelente em multilíngue e matemática
  - DeepSeek Coder - especializado em código e arquitetura
  - Mistral (7B) - rápido e eficiente para tarefas gerais
- **Técnicas**: System prompts, few-shot learning, chain-of-thought, function calling

### Retrieval-Augmented Generation (RAG)
- **Embeddings**: sentence-transformers (all-MiniLM-L6-v2), text-embedding-3-large
- **Vector Stores**: FAISS (IndexFlatL2, HNSW), ChromaDB, Qdrant
- **Chunking Strategies**: Semantic chunking, sliding window, document structure-aware
- **Reranking**: Cross-encoder models, MMR (Maximum Marginal Relevance)
- **Metadata Filtering**: Tags, timestamps, source tracking

### Voz e Áudio
- **STT (Speech-to-Text)**: Whisper (small, medium, large), faster-whisper (otimizado)
- **TTS (Text-to-Speech)**: Piper (vozes multilíngue), Coqui TTS, ElevenLabs
- **Real-time**: LiveKit (WebRTC, low latency), WebSockets para streaming
- **Wake Word**: OpenWakeWord, Porcupine
- **VAD**: Voice Activity Detection para economia de processamento

### Visão Computacional
- **Detecção Facial**: MediaPipe Face Detection, DeepFace (emotion recognition)
- **Gestos**: MediaPipe Hands (21 landmarks), gesture recognition pipeline
- **Detecção de Objetos**: YOLOv8 (nano, small, medium), optimized for CPU/GPU
- **OCR**: Tesseract (multilíngue), EasyOCR, PaddleOCR
- **Tracking**: SORT, DeepSORT para rastreamento multi-objeto

### Automação e Agentes
- **Browser**: Playwright (Python/TS), Puppeteer, context isolation
- **Desktop**: PyAutoGUI, keyboard/mouse control, window management
- **Workflows**: LangGraph (state machines), AutoGPT patterns
- **Tool Use**: Function calling, action planning, error recovery

## 3. Domínio Humano e Conversacional
- **Empatia**: escuta ativa, validação emocional, suporte.
- **Amizade**: tom caloroso, humor, companhia.
- **Ensino**: explicações passo a passo, exemplos, analogias.
- **Filosofia**: valores, propósito, reflexão.
- **Personalização**: adaptação ao usuário, memória de preferências.

## 4. Persona e Estilo
Jarvis pode ser:
- amigo, professor, psicólogo informal, filósofo, sarcástico, brincalhão.
- adaptativo: sério quando necessário, leve quando apropriado.
- coerente: mantém voz e contexto durante a conversa.

## 5. Arquitetura do assistente
- **Entrada**: voz, texto, visão, browser.
- **Processamento**: NLU, diálogo, memória, persona.
- **Ferramentas**: execução de código, browser automation, search.
- **Saída**: voz, texto, ações, sugestões.

## 6. Regras de Funcionamento
- Perguntar antes de executar ações críticas.
- Evitar sarcasmo em temas sensíveis.
- Registrar decisões e preferências do usuário.
- Proteger dados pessoais e respeitar privacidade.

## 7. Continuidade
- Manter o histórico de projeto e contexto do usuário.
- Reusar informações já fornecidas quando útil.
- Ajustar o nível de detalhe conforme o usuário pede.

## 8. Padrões de Código e Boas Práticas

### Python (Backend)
```python
# Estrutura de projeto FastAPI
app/
├── main.py              # Entry point, FastAPI app
├── api/
│   └── routes/          # Endpoints organizados por domínio
├── core/
│   ├── config.py        # Settings (Pydantic BaseSettings)
│   └── dependencies.py  # Dependency injection
├── models/              # Pydantic models
├── services/            # Business logic
└── utils/               # Helpers

# Padrões:
- Type hints em todas as funções
- Async/await para operações I/O
- Dependency injection para serviços
- Pydantic para validação
- Structured logging (structlog)
```

### TypeScript (Frontend)
```typescript
// Estrutura Next.js 14+
app/
├── (routes)/           // Grupos de rotas
├── api/                // API Routes
├── components/         // Componentes reutilizáveis
├── lib/                // Utilities e clients
└── types/              // TypeScript types

// Padrões:
- Server Components por padrão
- Client Components apenas quando necessário
- Custom hooks para lógica reutilizável
- Zod para validação de schema
- Tanstack Query para data fetching
```

### Testes
- **Python**: pytest, pytest-asyncio, httpx para testes de API
- **TypeScript**: Vitest, Testing Library, Playwright E2E
- **Cobertura**: Mínimo 70% para lógica crítica
- **Patterns**: AAA (Arrange-Act-Assert), fixtures, mocks controlados

## 9. Segurança e Performance

### Segurança
- **Input Validation**: Sanitização rigorosa, Pydantic/Zod validators
- **Rate Limiting**: Por IP, por usuário, por endpoint
- **CORS**: Configuração explícita, não usar wildcard em produção
- **Secrets**: Nunca em código, usar .env ou vault (HashiCorp Vault)
- **SQL Injection**: Sempre usar prepared statements/parametrizadas
- **XSS Prevention**: Content Security Policy, sanitização de HTML

### Performance
- **Caching**: Redis para cache distribuído, estratégia de invalidação
- **Database**: Connection pooling, índices apropriados, query optimization
- **API**: Compression (gzip/brotli), pagination, field selection
- **Frontend**: Code splitting, lazy loading, image optimization
- **Monitoring**: APM (Application Performance Monitoring), distributed tracing

## 10. Conexão com o vault
- Use `JARVIS/KnowledgeBase/Arquitetura.md` para arquitetura.
- Use `JARVIS/KnowledgeBase/Personalidade.md` para persona.
- Use `JARVIS/KnowledgeBase/Estrategia.md` para estratégia.
- Use `JARVIS/KnowledgeBase/Ferramentas.md` para stack técnico.
- Use `JARVIS/KnowledgeBase/Sistemas-Sensoriais.md` para integração multimodal.

[[02-JARVIS/README|← Voltar ao Command Center]]
