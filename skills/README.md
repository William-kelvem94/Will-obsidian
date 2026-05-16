---
tags: [skills, hub, index, taxonomy]
updated: 2026-05-16
title: "Skills - Taxonomia Pessoal"
date: 2026-04-27
---

# Skills — Taxonomia Pessoal

Este diretorio converge competencias tecnicas e estrategicas em um inventario vivo, organizado por categorias, pronto para alimentar o crescimento do segundo cerebro e orientar o desenvolvimento do JARVIS.

## Indice de Categorias

### [[skills/02-software-engineering/README|Engenharia de Software (Fullstack)]]
Backend, frontend e banco de dados com exemplos praticos em FastAPI, React, Vue, PostgreSQL e MongoDB.

### [[skills/03-infrastructure-mcp/mcp-servers|Infraestrutura e MCP]]
Model Context Protocol, servidores MCP customizados, integracao com LLMs locais (Ollama), orquestracao multi-servidor.

### [[skills/04-knowledge-systems/INDEX|Sistemas de Conhecimento (Knowledge Systems)]]
RAG avancado (GraphRAG, busca hibrida), gestao de memoria (episodica, semantica, procedural), vault Obsidian como segundo cerebro.

### [[skills/ai/Generative-Models|Inteligencia Artificial]]
Modelos generativos (Transformer, Difusao, GANs), aprendizado por reforco (PPO, DQN), MLOps, engenharia de prompts.

### [[skills/devops/Kubernetes|DevOps]]
Kubernetes (Pods, Deployments, Helm, RBAC), observabilidade (Prometheus, Grafana, OpenTelemetry), FinOps (custos, tagging, budgets).

### [[skills/frontend/Web-Components|Frontend]]
Web Components (Custom Elements, Shadow DOM, Lit), pads de componente agnosticos a framework.

### [[skills/softskills/Product-Management|Softskills]]
Product Management (OKR, Scrum, Lean, RICE), comunicacao tecnica, gestao de stakeholders.

## Mapa de Navegacao

```
skills/
  README.md              (este hub)
  Skill-Project-Matrix.md
  SFIA-Mapping.md
  02-software-engineering/
    README.md            -- Hub fullstack
    backend.md           -- FastAPI, Express, JWT
    frontend.md          -- React, Vue, Zustand, testes
    database.md          -- Migracoes, indices, pool
    INDEX.md             -- Indice completo
  03-infrastructure-mcp/
    mcp-servers.md       -- Implementacao e configuracao
    advanced-mcp-integrations.md -- Orquestracao multicamada
    local-llm-ops.md     -- Operacoes com LLMs locais
  04-knowledge-systems/
    INDEX.md             -- Hub knowledge systems
    obsidian-neural-vault.md
    advanced-rag-strategies.md
    memory-management.md
  05-testing/
    SKILL.md
  06-monitoring/
    SKILL.md
  07-rag-implementation/
    SKILL.md
  ai/
    Generative-Models.md
    Reinforcement-Learning.md
    MLOps.md
    Engenharia-de-Prompts.md
  devops/
    Kubernetes.md
    Observabilidade.md
    FinOps.md
  frontend/
    Web-Components.md
  softskills/
    Product-Management.md
    Comunicacao-Tecnica.md
```

## Como usar este hub

1. **Navegue por categoria** — Cada diretorio tem um README ou INDEX com visao geral
2. **Use como referencia** — Cada nota contem exemplos de codigo prontos para uso
3. **Conecte habilidades** — Wiki-links relacionam skills complementares
4. **Atualize regularmente** — Frontmatter com `updated` para controle de versionamento
5. **Mantenha consistencia** — Siga o template em `Templates/Skill-Template.md`

## Relacoes entre Categorias

As categorias nao sao isoladas — skills se complementam:

- **Backend + Database + MLOps** = Pipeline de dados para RAG
- **Engenharia de Prompts + Knowledge Systems** = Agente RAG completo
- **Kubernetes + Observabilidade + FinOps** = Infraestrutura sustentavel
- **Frontend + Web Components** = Interfaces agnosticas
- **Product Management + Softskills** = Alinhamento estrategico

## Proximos passos

- Explore cada categoria usando os links acima
- Use `Templates/Skill-Template.md` para criar novas notas de skill
- Mantenha o frontmatter completo com tags, nivel e projetos relacionados
- Vincule skills relacionadas para criar um grafo de aprendizado
- Registre projetos praticos em `projects` no frontmatter para conectar aprendizado e execucao

## Referencias

- [[Skill-Project-Matrix|Matriz Skill-Projeto]] — Mapeamento de competencias vs projetos
- [[SFIA-Mapping|Mapeamento SFIA]] — Alinhamento com framework SFIA de habilidades de TI
- [[JARVIS/05-System/Blueprints|Blueprints do JARVIS]] — Documentos de arquitetura do agente
