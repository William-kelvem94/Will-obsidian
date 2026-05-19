---
title: "JARVIS — Neural Command Center"
description: "Ponto central da inteligência JARVIS 5.0. Estrutura em camadas para memória, identidade e operação."
tags: [jarvis, hub, brain, intelligence]
updated: 2026-05-03
date: 2026-04-27
---

# JARVIS — Neural Command Center 🧠

Esta pasta é o **Núcleo do Cérebro** do JARVIS. Reorganizado para uma arquitetura de camadas (tiers) que facilita o processamento por agentes de IA e a gestão de contexto.

## 🏛️ Arquitetura em Camadas

### 01. Tier 1: Identity & Core (Who/Why)
*Define quem é o Jarvis e para quem ele trabalha.*
- [[01-Identity/Will/README|Will Persona]] — Perfil, preferências e valores do Will.
- [[01-Identity/Persona/Personalidade|Personality Registry]] — Tom, voz e comportamento base.
- [[01-Identity/Persona/Task-Subroutines|Task Subroutines]] — Adaptação de persona por tarefa (Coder, Searcher, Strategy).

### 02. Tier 2: Operational State (Current)
*O que está acontecendo agora.*
- [[02-Operational/Context/Estado|Context Flow]] — Projeto ativo, energia e foco momentâneo.
- [[02-Operational/Decisions/INDEX|Decision Log]] — Histórico de escolhas técnicas e pessoais.
- [[02-Operational/Config/CONFIG|System Config]] — Variáveis de ambiente e integrações.

### 03. Tier 3: Memory Stream (History)
*A linha do tempo do Jarvis.*
- [[03-Memory/Logs/INDEX|Neural Logs]] — Diários de interações (YYYY-MM-DD).
- [[03-Memory/Snapshots/INDEX|Episodic Snapshots]] — Eventos significativos e marcos de aprendizado.

### 04. Tier 4: Engineering & Wiki (How)
*O motor técnico e base de conhecimento.*
- [[04-Engineering/Architecture/SegundoCerebro|System Architecture]] — Como o Jarvis é construído.
- [[04-Engineering/Playbooks/Workflows-Praticos|Playbooks]] — Fluxos de trabalho testados para coding e automação.
- [[04-Engineering/Codebase-Maps/INDEX|Codebase Maps]] — Mapas de repositórios para agentes de programação.
- [[04-Engineering/Wiki/Conhecimento|Technical Wiki]] — Base de conhecimento técnica expandida.
- [[04-Engineering/Architecture/Neural-Indexing|Neural Indexing]] — Como otimizar RAG para este vault.

### 05. Tier 5: Evolution & Blueprints (Future)
*Como o Jarvis melhora.*
- [[05-System/Evolution/INDEX|Learning Base]] — Novos padrões e conhecimentos adquiridos.
- [[05-System/Blueprints/INDEX|Mind Templates]] — Modelos para captura e estruturação de dados.
- [[05-System/Maps/INDEX|Nexus Map]] — Visão geral da conexão entre todos os arquivos.
- [[05-System/Guides/INDEX|System Guides]] — Governança operacional para agentes e melhorias.
- [[05-System/Improvements/INDEX|Improvement Queue]] — Sugestões automáticas pendentes de revisão.

---

## ⚡ Protocolo de Carregamento de Agente
Qualquer IA operando neste diretório deve seguir o fluxo:
1. Ler `01-Identity/Will/` para alinhar valores.
2. Ler `02-Operational/Context/` para entender o foco.
3. Carregar o Sub-Persona apropriado em `01-Identity/Persona/Task-Subroutines.md`.
4. Consultar `04-Engineering/Playbooks/` para executar ações padronizadas.
5. Seguir `05-System/AGENT-CONTRACT.md` antes de escrever no vault.

---
*Mantenha o cérebro limpo. Evolua sempre.*
