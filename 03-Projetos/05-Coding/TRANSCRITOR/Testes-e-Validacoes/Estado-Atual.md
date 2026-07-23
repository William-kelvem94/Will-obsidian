---
title: TRANSCRITOR — Estado Atual e Validações
project: TRANSCRITOR
updated: 2026-07-23
tags: [testes, validacao, smoke-test, e2e]
---

# Estado atual e validações

## Validações aprovadas

- Cadastro, login e refresh token via API.
- Cadastro e login real pela Web UI.
- Isolamento de arquivos entre usuários.
- Upload normal e upload chunked.
- Transcrição síncrona com Whisper.
- Transcrição assíncrona com RabbitMQ e Redis.
- Sumarização extractive.
- Jobs, cancelamento e persistência de status.
- Batch e acompanhamento de progresso.
- Download TXT, JSON e PDF.
- Lint e build da Web UI.
- E2E Chromium: 15 testes aprovados.
- Health detalhado: todos os serviços saudáveis na última validação.
- Prometheus: alvos configurados como `up`.
- Testes unitários: 14 aprovados na última execução.
- Teste de DLQ: aprovado após remover duplicidade de encaminhamento.

## Limitações conhecidas

- A suíte completa de integração pode exceder o tempo limite quando executada em conjunto.
- Firefox e WebKit não estão instalados no ambiente atual.
- A observabilidade ainda não cobre todos os microsserviços com métricas Prometheus uniformes.
- A autenticação interna entre serviços ainda depende dos headers propagados pelo Gateway.

## Evidências

- Commits de correção: [[../Historico-de-Commits]].
- Fluxo prático registrado em [[../Sessoes-de-Desenvolvimento/2026-07-23-Pente-fino-pratico]].
