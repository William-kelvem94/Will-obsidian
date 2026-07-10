---
title: "Skills"
date: 2026-06-07
updated: 2026-06-13
type: moc
status: active
tags: [skills, habilidades, hub, organizacao]
summary: "Area canonica para habilidades tecnicas, capacidades e indices por dominio."
---

# Skills

Este diretorio contem o destino canonico para habilidades tecnicas, capacidades e documentacao reutilizavel do vault.

## Caminho principal

- [[../01-Hubs/Hub-Skills|Hub de Skills]]
- [[INDEX|Indice de Skills]]
- [[ROADMAP-EXPANSAO|Roadmap de Expansao de Skills]]

## Organizacao por dominio

### Inteligencia agenetica

- [[01-agentic-intelligence/README|README]]
- [[01-agentic-intelligence/INDEX|Indice]]
- [[01-agentic-intelligence/agentic-workflows/SKILL.md|Fluxos Agentes e MCP]]

### Engenharia de software

- [[02-software-engineering/README|README]]
- [[02-software-engineering/INDEX|Indice]]
- [[02-software-engineering/clean-architecture/SKILL.md|Arquitetura Limpa e SOLID]]
- [[02-software-engineering/programming-languages/SKILL.md|Linguagens de Programacao]]

### Infraestrutura e automacao

- [[03-infrastructure-mcp/testing-automation/SKILL.md|Automacao de Testes e CI/CD]]

### Inteligencia artificial

- [[ai/INDEX|Indice]]
- [[ai/llm-ops-tuning/SKILL.md|LLMOps e Fine-Tuning]]

### Midia e audiovisual

- [[media/ffmpeg-media-processing/SKILL.md|Manipulacao via FFmpeg]]
- [[media/audio-video-editing/SKILL.md|Edicao de Audio e Video]]

### Diagnosticos

- [[diagnostics/advanced-debugging/SKILL.md|Depuracao Avancada]]

## Regra de skill

Uma skill deve ter:

- objetivo;
- quando usar;
- prerequisitos;
- exemplos;
- limitacoes;
- checklist;
- links para projetos onde foi aplicada.

## Escala de crescimento

Quando um dominio crescer rapido, use um `INDEX` auxiliar por subpasta sem alterar o indice principal ate o mapa estabilizar.

## Navegacao rapida

- [[01-agentic-intelligence/README|Agentic Intelligence - fluxos/agents]]
- [[02-software-engineering/README|Engenharia de Software (Fullstack)]]
- [[03-infrastructure-mcp/README|Infraestrutura & MCP]]
- [[04-knowledge-systems/INDEX|Sistemas de Conhecimento, RAG, Memoria]]
- [[ai/INDEX|IA - Generative, RL, MLOps, Prompt Engineering]]
- [[devops/INDEX|DevOps e Observabilidade]]
- [[softskills/INDEX|Softskills, Product Management, Comunicacao]]
- [[frontend/INDEX-Addon|Frontend (Web Components, JS, etc)]]

### Capacidades de Agentes

- [[AGENT-FULLSTACK-CAPABILITIES|Fullstack Agent]] - stack completo de programacao para agentes IA
- [[AGENT-RESEARCH-CAPABILITIES|Research Agent]] - metodologia de pesquisa tecnica e cientifica

## Como esta organizado?

- Cada subpasta e uma trilha tematica, nao um time.
- Use os READMEs para entender area/trilha; links cruzados sempre nos hubs e indexes.
- [[INDEX]] central referencia skills em projetos e dashboards.

## Visualizacao rapida da arvore

```text
skills/
  README.md
  INDEX.md
  ROADMAP-EXPANSAO.md
  01-agentic-intelligence/
  02-software-engineering/
  03-infrastructure-mcp/
  04-knowledge-systems/
  ai/  devops/  frontend/  softskills/
```

## Painel: skills usados e relevantes

- Veja dashboard: [[01-Hubs/dashboards/Skill-Project-Matrix-Dinamica]]
- Todo skill/projeto relevante usa campos `skills_usados` e `projetos_relacionados` para integracao.

## Proxima etapa

- Fechar padrao canonico de skill.
- Expandir trilhas rasas.
- Reduzir drift entre `skills/`, `.agents/skills` e `.continue/skills`.
