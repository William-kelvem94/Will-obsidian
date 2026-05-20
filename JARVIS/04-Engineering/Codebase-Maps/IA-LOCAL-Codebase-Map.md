---
title: "IA-LOCAL Codebase Map"
description: "Mapa RAG-friendly do projeto IA-LOCAL para agentes de programacao."
created: 2026-05-08
updated: 2026-05-08
type: codebase-map
project: IA-LOCAL
domain: engineering
language_primary: Python
language_secondary: Markdown
code_root: "D:/Documents/GitHub/IA-LOCAL"
vault_sources:
  - "Projetos/01-Ativos/Privados/IA-LOCAL.md"
  - "Projetos/03-Estudos/EstudosPesquisas/IA-LOCAL.md"
  - "JARVIS/04-Engineering/Perception/IA-LOCAL-Local-Agent.md"
  - "JARVIS/04-Engineering/Perception/IA-LOCAL-Obsidian-Usage.md"
confidence: vault-notes-only
tags:
  - ia-local
  - jarvis
  - faiss
  - whisper
  - piper
  - desktop-automation
  - rag
  - codebase-map
---

# IA-LOCAL Codebase Map

## One-liner

IA-LOCAL e o nucleo local do JARVIS: um assistente Python com memoria vetorial, voz, automacao de desktop, modelos locais/remotos e consumo do vault Obsidian como segundo cerebro.

## Fontes locais relevantes

- Nota de projeto: [[Projetos/01-Ativos/Privados/IA-LOCAL]]
- Nota de evolucao: [[Projetos/03-Estudos/EstudosPesquisas/IA-LOCAL]]
- Arquitetura local: [[JARVIS/04-Engineering/Perception/IA-LOCAL-Local-Agent]]
- Uso com Obsidian: [[JARVIS/04-Engineering/Perception/IA-LOCAL-Obsidian-Usage]]
- Observacao: nesta rodada nao houve leitura do codigo real de `D:/Documents/GitHub/IA-LOCAL`; este mapa consolida o que ja esta no vault.

## Stack documentada

| Camada | Tecnologia citada | Funcao provavel |
|---|---|---|
| Linguagem | Python 3.8+ | Runtime principal do agente local. |
| Memoria | FAISS + sentence-transformers | Busca vetorial e RAG. |
| Busca hibrida planejada | BM25 + FAISS | Melhor recall para notas e memorias. |
| Voz STT | Whisper, faster-whisper planejado | Transcricao local. |
| Voz TTS | PyTTSx3/TTS, Piper PT-BR planejado | Resposta falada local. |
| Automacao | PyAutoGUI, Keyboard, pydirectinput planejado | Controle de PC e hotkeys. |
| Modelos | Llama.cpp, OpenRouter, Ollama planejado | LLM local/remoto com fallback. |
| Infra | Docker + Docker Compose | Empacotamento e reproducibilidade. |

## Estrutura documentada

| Caminho documentado | Papel para agentes |
|---|---|
| `jarvis_project/core/jarvis_brain.py` | Motor de decisao e logica de conversa. |
| `jarvis_project/core/memory_manager.py` | Interface com banco vetorial e RAG. |
| `jarvis_project/interfaces/pc_controller.py` | Controle de hardware/desktop. |
| `jarvis_project/interfaces/voice_interface.py` | Audio buffer, STT e voz. |
| `jarvis_project/learning/dream_generator.py` | Processamento de memorias em background. |
| `.env` | Configuracao local e chaves; nao abrir nem copiar. |
| `obsidian_clone/` | Possivel clone do vault consumido pelo agente, segundo docs. |

## Modelo mental para agentes

1. IA-LOCAL carrega configuracao local e aponta para um vault/cloned vault.
2. `memory_manager.py` indexa notas e memorias em FAISS.
3. Entrada por voz ou texto passa por `jarvis_brain.py`.
4. O brain recupera contexto relevante, escolhe modelo local/remoto e gera resposta.
5. Se houver acao de PC, `pc_controller.py` executa operacoes com limites.
6. `dream_generator.py` pode consolidar memorias e aprendizados em background.

## Areas que pedem cuidado

- Automacao de desktop pode executar acoes reais; exigir modo dry-run ou confirmacao para operacoes destrutivas.
- Hotkeys e controle de mouse dependem do foco da janela.
- Indices FAISS podem ficar desatualizados; preferir index incremental com metadados de arquivo e mtime.
- STT/TTS local varia por hardware; tratar falta de microfone/modelo como degradacao graciosa.
- OpenRouter e outros provedores remotos implicam chaves e rede; o modo local deve funcionar sem expor segredos.
- O vault contem dados pessoais; filtros de escopo e logs devem evitar vazamento.

## Proximos probes seguros

- Rodar `rg --files` no projeto real e localizar `jarvis_project/`, `memory_manager.py`, `voice_interface.py`, `pc_controller.py`.
- Ler README, requirements e compose antes de executar.
- Mapear chamadas de modelo com `rg -n "openrouter|ollama|llama|model|chat|completion"`.
- Mapear indexacao com `rg -n "faiss|sentence|embedding|chunk|bm25|vector"`.
- Mapear acoes de PC com `rg -n "pyautogui|keyboard|pydirectinput|hotkey|click|typewrite"`.
- Confirmar caminho do vault clonado e formato esperado de ingestao.

## Tarefas provaveis para agentes

- Implementar busca hibrida FAISS + BM25 com ranking explicavel.
- Migrar STT para faster-whisper com selecao de modelo por hardware.
- Adicionar Piper TTS PT-BR como provider local configuravel.
- Trocar provider remoto por Ollama local mantendo fallback.
- Criar suite de testes com vault fixture pequeno e sem dados privados.
- Adicionar limites de seguranca para automacao de desktop: allowlist, confirmacao e logs.

## Perguntas abertas

- O IA-LOCAL ainda usa OpenRouter como padrao ou ja existe Ollama local parcial?
- O clone Obsidian e sincronizado por copia, symlink ou configuracao manual?
- A memoria vetorial persiste em arquivo local, SQLite, Chroma ou apenas FAISS bruto?
- O `dream_generator.py` escreve notas no vault ou apenas memoria interna?

[[JARVIS/04-Engineering/Codebase-Maps/INDEX|← Voltar ao índice de Codebase-Maps]]
