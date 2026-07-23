---
title: Sessão — Pente-fino prático do TRANSCRITOR
project: TRANSCRITOR
date: 2026-07-23
tags: [sessao, debugging, docker, github]
---

# Sessão — Pente-fino prático

## Objetivo

Revisar o projeto em uso real, reproduzir falhas, corrigir contratos quebrados e validar os containers e fluxos principais.

## O que foi investigado

- Login e cadastro.
- Dashboard e carregamento dinâmico.
- Upload normal e chunked.
- Transcrição real com Whisper.
- Sumarização e download.
- Jobs, batch e cancelamento.
- RabbitMQ, Redis e DLQ.
- Health checks e Prometheus.
- E2E Chromium e autenticação real.

## Correções relevantes

- Gateway passou a encaminhar a transcrição assíncrona para a rota correta.
- Resultados foram normalizados na Web UI.
- Jobs passaram a persistir status no Storage.
- Upload chunked foi implementado com validação de UUID.
- Sumarização, batch e downloads tiveram contratos corrigidos.
- DLQ deixou de duplicar mensagens.
- Health check do modo extractive foi corrigido.
- Endpoint Prometheus do extrator foi corrigido.

## Validação

- Fluxo real: cadastro → login → upload → job → Whisper → resultado.
- E2E Chromium: 15 aprovados.
- Autenticação real pela UI: aprovada.
- Health dos containers: aprovado.
- Testes unitários: 14 aprovados.
- Teste de DLQ: aprovado após correção.

## Histórico Git

Ver [[../Historico-de-Commits]] para os hashes e títulos dos commits produzidos durante a estabilização.

## Pendências deixadas conscientemente

- Completar autenticação criptográfica interna.
- Uniformizar métricas dos microsserviços.
- Instalar Firefox/WebKit para ampliar E2E.
- Tornar a suíte completa de integração mais rápida e determinística.
