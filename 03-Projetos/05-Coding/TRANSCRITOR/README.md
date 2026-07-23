---
title: TRANSCRITOR — Engenharia e Histórico
project: TRANSCRITOR
repository: https://github.com/William-kelvem94/TRANSCRITOR
status: ativo
updated: 2026-07-23
tags: [projeto, coding, microservicos, transcricao, whisper]
---

# TRANSCRITOR — Engenharia e Histórico

Hub técnico e histórico do projeto TRANSCRITOR. Esta pasta registra arquitetura, decisões, bugs, correções, testes, releases e sessões de desenvolvimento.

## Acesso rápido

- [[../../01-Ativos/Privados/TRANSCRITOR|Página principal do projeto]]
- [[Arquitetura]]
- [[Roadmap]]
- [[Historico-de-Commits]]
- [[Bugs-e-Correcoes/Indice]]
- [[Testes-e-Validacoes/Estado-Atual]]
- [[Sessoes-de-Desenvolvimento/2026-07-23-Pente-fino-pratico]]

## Estado atual

- Branch principal: `main`
- Repositório: [GitHub — TRANSCRITOR](https://github.com/William-kelvem94/TRANSCRITOR)
- Último commit registrado: `b07c4e1d` — correção do encaminhamento e leitura da DLQ
- Execução local: Docker Compose
- Interface: React + TypeScript + Vite
- Backend: FastAPI em microsserviços
- Infraestrutura: PostgreSQL, Redis, RabbitMQ, Prometheus, Grafana e Jaeger
- Transcrição: Whisper em processamento síncrono e assíncrono

## Como usar esta documentação

1. O estado atual fica nesta página e em [[Testes-e-Validacoes/Estado-Atual]].
2. Cada decisão estrutural deve virar uma nota em `Decisoes/`.
3. Cada bug relevante deve ser registrado em `Bugs-e-Correcoes/`.
4. Cada sessão de trabalho importante deve ser registrada em `Sessoes-de-Desenvolvimento/`.
5. Commits e releases devem ser adicionados à trilha histórica, sempre com evidência.

## Regra de registro

Registrar o que mudou, por que mudou, como foi validado e o que ainda falta. Não guardar apenas o resultado final: preservar também os problemas encontrados e as decisões que evitaram regressões.
