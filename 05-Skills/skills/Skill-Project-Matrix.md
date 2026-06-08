---
title: "Matriz Skills-Projetos"
date: 2026-05-16
tags: [skills, projetos, matriz, mapeamento, hub]
related: ["05-Skills/skills/README", "03-Projetos/Projetos/README"]
aliases: ["Skill-Project Matrix", "Mapeamento de Competências"]
updated: 2026-06-07
---

# Matriz Skills-Projetos

Mapeamento completo de todas as skills do vault para todos os projetos ativos. Esta matriz revela quais competências estão sendo aplicadas, onde há sobreposição e quais áreas precisam de desenvolvimento.

## Categorias de Skills

| # | Categoria | Descrição |
|---|-----------|-----------|
| S1 | **Agente Intelligence** | Orquestração multi-agente, workflows autônomos, MCP, prompts, memória |
| S2 | **Engenharia de Software** | Backend (Python/Node), Frontend (React/NextJS), Banco de Dados, Testes, Arquitetura |
| S3 | **Infraestrutura & MCP** | LLMs locais (Ollama), servidores MCP, Docker, GPU, monitoramento |
| S4 | **Sistemas de Conhecimento** | Obsidian Neural Vault, RAG avançado, gestão de memória, pipelines de embedding |
| S5 | **AI & ML** | MLOps, engenharia de prompts, modelos generativos, reinforcement learning |
| S6 | **DevOps** | FinOps, Kubernetes, observabilidade, CI/CD |
| S7 | **Frontend** | Web Components, design systems, componentes reutilizáveis |
| S8 | **Soft Skills** | Comunicação técnica, gestão de produto, documentação |

## Matriz Projetos × Skills

| Projeto | S1 Agentic | S2 Eng. Software | S3 Infra & MCP | S4 Conhecimento | S5 AI & ML | S6 DevOps | S7 Frontend | S8 Soft Skills |
|---------|:----------:|:----------------:|:---------------:|:----------------:|:----------:|:---------:|:-----------:|:--------------:|
| **JARVIS 5.0** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Gestor Aluguel 2.0** | ⭐ | ⭐⭐⭐ | ⭐⭐ | — | ⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **IA-LOCAL** | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐ | — | ⭐ |
| **Auto-boletos** | ⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐ | ⭐ | — | — | ⭐ |
| **Obsidian Second Brain** | ⭐⭐ | ⭐ | ⭐ | ⭐⭐⭐ | ⭐ | — | — | ⭐⭐ |
| **LM Studio** | ⭐ | — | ⭐⭐⭐ | ⭐ | ⭐⭐ | — | — | — |
| **Ollama** | ⭐⭐ | ⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐ | — | ⭐ |
| **VS Code AI** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐ | — | ⭐ |
| **Hermes Agent** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐ | ⭐⭐ | — | — | ⭐ |
| **GitHub Sync** | ⭐⭐ | ⭐⭐ | ⭐ | — | — | ⭐⭐ | — | ⭐ |
| **OpenClaude WK** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | — | — | ⭐ |
| **Automatizador (Python)** | ⭐ | ⭐⭐ | ⭐ | — | — | — | — | — |
| **TRADUTOR-WKP** | — | ⭐⭐ | — | — | ⭐ | — | — | — |
| **CRUDs PHP** | — | ⭐⭐ | — | — | — | — | — | — |
| **Java Atividades** | — | ⭐⭐ | — | — | — | — | — | — |
| **DIA-DAS-MULHERES** | — | ⭐ | — | — | — | — | ⭐ | ⭐⭐ |
| **DEEP-LEARNING** | ⭐ | ⭐ | ⭐ | ⭐ | ⭐⭐⭐ | — | — | ⭐ |

**Legenda:** ⭐⭐⭐ = Uso intenso / essencial · ⭐⭐ = Uso moderado · ⭐ = Uso leve/emergente · — = Não se aplica

## Detalhamento por Projeto

### JARVIS 5.0
- **S1 (Agentic):** Orquestração multi-agente, workflows autônomos, arquiteturas de memória, consenso entre agentes
- **S2 (Eng. Software):** Backend em Python/FastAPI, arquitetura de sistemas distribuídos, PostgreSQL + pgvector
- **S3 (Infra & MCP):** MCP servers customizados, Ollama multi-instância, GPU passthrough, monitoramento
- **S4 (Conhecimento):** Pipeline RAG completo, GraphRAG, memória episódica/semântica, Obsidian como knowledge base
- **S5 (AI & ML):** Modelos generativos locais, fine-tuning, RAG + embeddings
- **S6 (DevOps):** Docker Compose, health checks, métricas Prometheus
- **S7 (Frontend):** Web Components para dashboards, interfaces de agente
- **S8 (Soft Skills):** Documentação extensa, gestão de produto, comunicação técnica

### Gestor Aluguel 2.0
- **S1 (Agentic):** Workflows de notificação e lembretes
- **S2 (Eng. Software):** NextJS/React fullstack, banco de dados, API REST
- **S3 (Infra & MCP):** Deploy em nuvem (Render), Docker, WhatsApp integration (Waha/n8n)
- **S5 (AI & ML):** Chatbot com IA para inquilinos
- **S6 (DevOps):** CI/CD, deploy automatizado
- **S7 (Frontend):** Web Components, design system, UI/UX
- **S8 (Soft Skills):** Product management, pesquisa com usuários, beta testing

### IA-LOCAL
- **S1 (Agentic):** Agentes locais com MCP, automação de tarefas
- **S2 (Eng. Software):** Scripts Python, integração de APIs
- **S3 (Infra & MCP):** ⭐⭐⭐ — Ollama, quantização GGUF/AWQ, vLLM, Docker, GPU
- **S4 (Conhecimento):** RAG local, embeddings, busca semântica
- **S5 (AI & ML):** Modelos open-source, engenharia de prompts, benchmark

### Auto-boletos
- **S1 (Agentic):** Workflow autônomo de faturamento, agendamento de tarefas
- **S2 (Eng. Software):** Automação Python, manipulação de PDFs/CSV
- **S3 (Infra & MCP):** Servidor MCP para tarefas agendadas
- **S4 (Conhecimento):** Base de clientes e regras de negócio

### Obsidian Second Brain
- **S1 (Agentic):** Agentes que consomem o vault via MCP
- **S4 (Conhecimento):** ⭐⭐⭐ — Neural Vault, tagging, grafos de conhecimento, MOCs
- **S8 (Soft Skills):** Organização pessoal, metodologia Zettelkasten, GTD

## Skills por Domínio — Lista Completa

### S1: Agentic Intelligence (13 skills)
| Skill | Arquivo | Nível | Projetos |
|-------|---------|:-----:|----------|
| Multi-Agent Orchestration | `01-agentic-intelligence/multi-agent-orchestration` | Avançado | JARVIS 5.0, Hermes Agent |
| Autonomous Workflows | `01-agentic-intelligence/autonomous-workflow` | Avançado | Auto-boletos, GitHub Sync |
| Advanced Workflows | `01-agentic-intelligence/advanced-workflows` | Avançado | JARVIS 5.0, OpenClaude WK |
| MCP (Model Context Protocol) | `01-agentic-intelligence/mcp` | Avançado | VS Code AI, JARVIS 5.0 |
| MCP Operators | `01-agentic-intelligence/mcp-operators` | Intermediário | VS Code AI |
| Prompt Engineering | `01-agentic-intelligence/prompts` | Avançado | Todos os projetos AI |
| Mini-Agent | `01-agentic-intelligence/mini-agent` | Intermediário | Hermes Agent |
| Memory Architectures | `01-agentic-intelligence/memory-architectures` | Intermediário | JARVIS 5.0 |
| Multi-Agent Consensus | `01-agentic-intelligence/multi-agent-consensus` | Intermediário | JARVIS 5.0 |
| Advanced Reasoning Patterns | `01-agentic-intelligence/advanced-reasoning-patterns` | Avançado | JARVIS 5.0 |
| Best Practices | `01-agentic-intelligence/best-practices` | Intermediário | Todos |
| Quick Reference | `01-agentic-intelligence/quick-reference` | — | Todos |
| Use Cases | `01-agentic-intelligence/use-cases` | — | Documentação |

### S2: Engenharia de Software (5 skills)
| Skill | Arquivo | Nível | Projetos |
|-------|---------|:-----:|----------|
| Advanced Backend Architecture | `02-software-engineering/advanced-backend-architecture` | Avançado | JARVIS 5.0 |
| PostgreSQL Avançado | `02-software-engineering/Bancos-de-Dados/PostgreSQL-Advanced` | Avançado | JARVIS 5.0, Gestor Aluguel |
| Frontend (React/NextJS) | `02-software-engineering/frontend` | Intermediário | Gestor Aluguel 2.0 |
| Backend (Python/Node) | `02-software-engineering/backend` | Avançado | JARVIS 5.0, IA-LOCAL, Automatizador |
| Testing Architecture | `02-software-engineering/testing/SKILL` | Intermediário | Gestor Aluguel, JARVIS 5.0 |

### S3: Infraestrutura & MCP (4 skills)
| Skill | Arquivo | Nível | Projetos |
|-------|---------|:-----:|----------|
| Local LLM Ops | `03-infrastructure-mcp/local-llm-ops` | Avançado | IA-LOCAL, LM Studio, Ollama |
| MCP Servers | `03-infrastructure-mcp/mcp-servers` | Avançado | VS Code AI, JARVIS 5.0 |
| Advanced MCP Integrations | `03-infrastructure-mcp/advanced-mcp-integrations` | Intermediário | OpenClaude WK, JARVIS 5.0 |
| Monitoring | `03-infrastructure-mcp/monitoring/SKILL` | Iniciante | JARVIS 5.0 |

### S4: Sistemas de Conhecimento (4 skills)
| Skill | Arquivo | Nível | Projetos |
|-------|---------|:-----:|----------|
| Obsidian Neural Vault | `04-knowledge-systems/obsidian-neural-vault` | Avançado | Obsidian Second Brain |
| Advanced RAG Strategies | `04-knowledge-systems/advanced-rag-strategies` | Avançado | JARVIS 5.0 |
| Memory Management | `04-knowledge-systems/memory-management` | Intermediário | JARVIS 5.0 |
| RAG Implementation | `04-knowledge-systems/rag-implementation/SKILL` | Intermediário | JARVIS 5.0, IA-LOCAL |

### S5–S8: Demais Categorias (8 skills)
| Skill | Categoria | Nível | Projetos |
|-------|-----------|:-----:|----------|
| MLOps | AI & ML | Intermediário | IA-LOCAL, DEEP-LEARNING |
| Engenharia de Prompts | AI & ML | Avançado | Todos os projetos AI |
| Generative Models | AI & ML | Intermediário | JARVIS 5.0, IA-LOCAL |
| Reinforcement Learning | AI & ML | Iniciante | DEEP-LEARNING |
| FinOps | DevOps | Intermediário | Gestor Aluguel |
| Kubernetes | DevOps | Iniciante | Gestor Aluguel (futuro) |
| Observabilidade | DevOps | Intermediário | JARVIS 5.0 |
| Web Components | Frontend | Intermediário | Gestor Aluguel, JARVIS 5.0 |
| Comunicação Técnica | Soft Skills | Avançado | Todos |
| Product Management | Soft Skills | Intermediário | Gestor Aluguel, JARVIS 5.0 |

## Análise de Cobertura

### Skills Maduras (nível Avançado, aplicação intensa)
| Skill | Justificativa |
|-------|---------------|
| Multi-Agent Orchestration | Base do JARVIS 5.0 e Hermes Agent |
| MCP Protocol | Core de toda a infraestrutura de agentes |
| Local LLM Ops | Documentação robusta, aplicação em 3+ projetos |
| Obsidian Neural Vault | Documentação completa do vault, padrões estabelecidos |
| Advanced RAG Strategies | Pesquisa aprofundada, implementação em andamento |
| Advanced Backend Architecture | Referência arquitetural completa com exemplos |
| Engenharia de Prompts | Aplicada em todos os projetos, com templates e guias |
| PostgreSQL Avançado | Tratado técnico completo, aplicação direta em JARVIS |

### Skills em Desenvolvimento (nível Intermediário, aplicação moderada)
| Skill | Gap | Ação Necessária |
|-------|-----|-----------------|
| Testing Architecture | Sem testes de fato implementados | Criar suite de testes para JARVIS e Gestor Aluguel |
| Kubernetes | Apenas teórico | Implementar cluster local com minikube ou kind |
| Reinforcement Learning | Apenas conceitual | Projeto prático com gymnasium |
| Web Components | Sem biblioteca publicada | Criar package de componentes reutilizáveis |
| Product Management | Sem processos formais | Adotar OKRs trimestrais e sprints |

### Skills Emergentes (nível Iniciante, sem aplicação)
| Skill | Prioridade | Plano |
|-------|:----------:|-------|
| Monitoring (MCP) | Alta | Implementar dashboard de health checks para JARVIS |
| FinOps | Média | Calcular custos de APIs e sugerir otimizações |
| Multi-Modal (Visão) | Alta | Pipeline screenshot → LLaVA → ação para JARVIS |
| GraphRAG | Média | Implementar camada de grafo sobre o pipeline RAG atual |

## Lacunas por Projeto

| Projeto | Lacunas Críticas | Recomendação |
|---------|------------------|--------------|
| **JARVIS 5.0** | Testes automatizados, monitoramento, CI/CD | Implementar pipeline de testes e métricas |
| **Gestor Aluguel 2.0** | Testes E2E, esteira de deploy, documentação de API | Adicionar Playwright + GitHub Actions |
| **IA-LOCAL** | Benchmark sistemático, comparativo de modelos | Criar suite de benchmark com métricas padronizadas |
| **Auto-boletos** | Tratamento de erros, logging, testes | Adicionar retry logic + notificações de falha |
| **Obsidian Second Brain** | Automação de ingestão, backup automatizado | Scripts de manutenção + git auto-commit |
| **CRUDs PHP** | Containerização, testes, documentação | Dockerizar e adicionar PHPUnit |

## Skills que Nenhum Projeto Usa (Órfãs)

| Skill | Motivo | Ação |
|-------|--------|------|
| FinOps | Nenhum projeto em nuvem paga | Revisar se mantém ou arquiva |
| Kubernetes | Infraestrutura atual não justifica | Manter como estudo para futuro |
| Reinforcement Learning | Sem projeto prático alinhado | Criar mini-projeto didático |

---

*Atualizado em: 2026-05-16 · Total: 25 skills mapeadas para 17 projetos*

[[05-Skills/skills/README|← Voltar à Taxonomia de Skills]]
