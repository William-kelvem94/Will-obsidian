---
title: "IA-LOCAL (Clonado)"
source: "d:/Documents/GitHub/IA-LOCAL"
language: Python
private: true
description: "Assistente de IA avançado (JARVIS) com memória vetorial, processamento de voz e capacidades de automação de desktop."
updated: 2026-06-05
tags: [privados, python, jarvis, ai, voice, projetos]
date: 2026-04-27
---

# IA-LOCAL: JARVIS Core 🧠 [[../Projetos.md|Projetos]] [[GitHub-Completo]]

**Status**: 🏗️ Em Desenvolvimento Ativo
**Foco**: Autonomia Local e Memória Persistente

O **IA-LOCAL** é o motor principal por trás do JARVIS, integrando modelos de linguagem locais e remotos com um sistema de memória vetorial para criar um "segundo cérebro" operacional.

## 🛠️ Tech Stack
| Categoria | Tecnologia |
|---|---|
| **Linguagem** | Python 3.8+ |
| **Memória** | FAISS + Sentence Transformers |
| **Voz** | OpenAI Whisper (STT) + PyTTsx3/TTS |
| **Automação** | PyAutoGUI + Keyboard |
| **Modelos** | Llama.cpp / OpenRouter API |
| **Infra** | Docker + Docker Compose |

## 🏗️ Arquitetura do Sistema
- `jarvis_project/core/`:
    - `jarvis_brain.py`: Motor de decisão e lógica de conversação.
    - `memory_manager.py`: Interface com banco vetorial para RAG.
- `jarvis_project/interfaces/`:
    - `pc_controller.py`: Módulo de visão e controle de hardware.
    - `voice_interface.py`: Gerenciamento de buffers de áudio e transcrição.
- `jarvis_project/learning/`:
    - `dream_generator.py`: Processamento em background de memórias para evolução criativa.

## 🚀 Roadmap de Evolução
- [x] Memória Vetorial Persistente
- [x] Interface de Voz Experimental
- [ ] **Visão Computacional**: Screenshot analysis para contexto visual.
- [ ] **API REST**: Interface para conexão com dashboards externos.
- [ ] **Fine-Tuning Loop**: Automação da coleta de dados para treinamento LoRA.

## 🔗 Conexões no Vault
- [[JARVIS/README|🧠 Hub JARVIS]]: Central de memórias e decisões.
- [[Projetos/03-Estudos/EstudosPesquisas/README|🔬 Recursos]]: Documentação local de IA.
- [[skills/01-agentic-intelligence/autonomous-workflow|🧠 Workflow AAW]]: Como gerenciar este código como agente.

**Links:** [[GitHub-Completo]] | [[Projetos/01-Ativos/Plano-de-Acao|Plano de Ação]] #jarvis #faiss #whisper #python

## 📊 Sincronização Local de Código (Automática)
*Dados técnicos lidos do repositório físico em 2026-06-05 22:19:31*

- **Caminho Físico Local:** `D:/DOCUMENTOS/GitHub/IA-LOCAL`
- **Branch Ativa:** `main`
- **Último Commit:** `1b2125c - feat: initialize n8n-gemini-agent project with essential files and structure (2026-04-30)`
- **Repositório Remoto (Origin):** [https://github.com/William-kelvem94/IA-LOCAL.git](https://github.com/William-kelvem94/IA-LOCAL.git)
- **Descrição de README:** Sem descrição detalhada no README local.

### 🛠️ Configurações e Arquivos de Infraestrutura
- [ ] Dockerfile
- [ ] docker-compose.yml
- [ ] Arquivo .env.example
- [ ] Tailwind CSS
- [ ] TypeScript config
- [ ] Vite Bundler
- [ ] Next.js configuration
- [ ] Next.js configuration (mjs)
- [ ] TypeScript/JavaScript npm
- [ ] Python dependencies

### 📦 Principais Dependências Mapeadas
- Nenhuma dependência estruturada identificada.