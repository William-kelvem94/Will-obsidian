---
title: "Hub JARVIS"
date: 2026-06-07
updated: 2026-06-07
type: moc
status: active
tags: [hub, jarvis, ia, agentes, memoria]
summary: "Hub de navegação para a área JARVIS, conectando identidade, memória, agentes, RAG e IA local."
---

# Hub JARVIS

Este hub centraliza a navegação da área JARVIS e separa o que é memória do agente, conhecimento geral, arquitetura e operação.

## Entrada principal

- [[../JARVIS/README|JARVIS Command Center]]

## Memória e identidade

- [[../JARVIS/03-Memory/fatos_rapidos]]
- [[../Cerebro-Will]]
- [[../Will-Pessoal/README|Will-Pessoal]]

## Conhecimento útil para o JARVIS

- [[../Conhecimentos-Gerais/01-IA/RAG-e-Memoria-para-Agentes]]
- [[../Conhecimentos-Gerais/01-IA/Arquitetura-RAG-para-Obsidian-e-JARVIS]]
- [[../Conhecimentos-Gerais/01-IA/IA-Local-Ollama-e-Modelos-Abertos]]
- [[../Conhecimentos-Gerais/01-IA/Context-Engineering]]
- [[../Conhecimentos-Gerais/00-Ontologia-de-Conhecimento-para-IA]]

## Skills relacionadas

- [[../skills/01-agentic-intelligence/multi-agent-orchestration]]
- [[../skills/03-infrastructure-mcp/mcp-servers]]
- [[../skills/04-knowledge-systems/obsidian-neural-vault]]

## Regra de separação

| Tipo de conteúdo | Onde deve ficar |
|---|---|
| memória do agente | `JARVIS/` |
| conhecimento estável | `Conhecimentos-Gerais/` |
| habilidades técnicas | `skills/` |
| projetos em execução | `Projetos/` |
| contexto pessoal profundo | `Will-Pessoal/` |

## Próximas melhorias

- Criar mapa de memória do JARVIS.
- Separar memória episódica, semântica e operacional.
- Criar playbooks de atualização de memória.
- Definir política de dados sensíveis antes de indexar tudo em RAG.
