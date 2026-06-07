---
title: "Session to Memory Protocol"
description: "Protocolo para transformar uma sessao de trabalho em memoria reutilizavel no vault."
tags: [jarvis, memoria, protocolo, agentes, operacao, jarvis-operacao]
updated: 2026-06-07
status: active
date: 2026-06-01
---

# Session to Memory Protocol

Este protocolo define quando uma sessao deve virar memoria no Obsidian.

## Quando Registrar

Registre memoria quando houver:

- decisao tecnica importante;
- descoberta sobre um projeto;
- erro recorrente corrigido;
- novo comando de setup, teste ou deploy;
- mudanca em arquitetura;
- regra nova para agentes;
- aprendizado que deve sobreviver ao chat.

## Onde Registrar

- Decisao: `JARVIS/02-Operational/Decisions/`
- Aprendizado reutilizavel: `JARVIS/03-Memory/Learned-Patterns/`
- Marco de sessao: `JARVIS/03-Memory/Snapshots/`
- Sugestao pendente: `JARVIS/05-System/Improvements/`
- Mapa tecnico de projeto: `JARVIS/04-Engineering/Codebase-Maps/`

## Formato Minimo

```md
---
title: "..."
description: "..."
tags: [jarvis, memoria]
updated: YYYY-MM-DD
status: active
---

# Titulo

## Contexto

## O que mudou

## Como validar

## Relacionado
```

## Nao Registrar

- detalhes privados sem pedido explicito;
- texto temporario sem utilidade futura;
- conteudo duplicado de README;
- suposicoes nao verificadas como fato.

## Relacionado

- [[JARVIS/05-System/AGENT-CONTRACT]]
- [[Conhecimento-Geral/IA-para-Programacao/Memoria-para-Agentes]]


[[JARVIS/README|← Voltar ao Command Center]]
