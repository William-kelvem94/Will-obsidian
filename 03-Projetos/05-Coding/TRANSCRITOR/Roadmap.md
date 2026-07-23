---
title: TRANSCRITOR — Roadmap
project: TRANSCRITOR
updated: 2026-07-23
tags: [roadmap, fases, planejamento]
---

# Roadmap e fases

## Fase 1 — Base e arquitetura

- [x] Estruturar microsserviços.
- [x] Criar API Gateway.
- [x] Integrar PostgreSQL, Redis e RabbitMQ.
- [x] Criar Web UI.

## Fase 2 — Autenticação e experiência inicial

- [x] Cadastro e login reais.
- [x] Refresh token.
- [x] Proteção de rotas da Web UI.
- [x] Tema claro/escuro e padronização visual inicial.

## Fase 3 — Fluxos de negócio

- [x] Upload normal.
- [x] Upload chunked para arquivos grandes.
- [x] Transcrição síncrona.
- [x] Transcrição assíncrona.
- [x] Sumarização síncrona e assíncrona.
- [x] Jobs, resultados e downloads.
- [x] Processamento batch.

## Fase 4 — Estabilização prática

- [x] Corrigir falhas de contrato entre Gateway e serviços.
- [x] Corrigir consumo de filas e DLQ.
- [x] Corrigir persistência de status de jobs.
- [x] Corrigir dashboard, resultados e carregamento dinâmico da Web UI.
- [x] Validar fluxo real de login, upload e transcrição.
- [x] Validar E2E Chromium e autenticação real.
- [x] Corrigir health check do modo extractive.
- [x] Corrigir coleta Prometheus do extrator de áudio.

## Fase 5 — Próximos riscos

- [ ] Autenticação criptográfica própria entre microsserviços.
- [ ] Completar métricas Prometheus dos demais serviços.
- [ ] Alertas operacionais com limiares úteis.
- [ ] Testes E2E completos em Firefox e WebKit.
- [ ] Scans automatizados de vulnerabilidades e segredos.
- [ ] Testes de falha, retry e recuperação de broker mais abrangentes.
- [ ] Documentar contrato de produção, certificados e gestão de segredos.
