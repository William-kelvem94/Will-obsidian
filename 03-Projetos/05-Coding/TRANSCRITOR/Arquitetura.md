---
title: TRANSCRITOR — Arquitetura
project: TRANSCRITOR
updated: 2026-07-23
tags: [arquitetura, microsservicos, backend, frontend]
---

# Arquitetura

## Visão geral

O TRANSCRITOR é uma aplicação web de transcrição e sumarização de áudio/vídeo. A Web UI conversa com o API Gateway, que autentica o usuário, aplica regras de entrada e encaminha operações para os microsserviços internos.

```text
Web UI (React/Vite)
        |
        v
API Gateway (FastAPI)
   |       |       |       |
   v       v       v       v
Storage  File Mgmt  Transcription  Summarization
   |                         |
   +--> PostgreSQL            +--> Whisper / Redis / RabbitMQ

Batch Processor coordena jobs compostos.
Audio Extraction usa FFmpeg para extrair áudio de vídeo.
Prometheus/Grafana/Jaeger sustentam observabilidade.
```

## Componentes

| Componente | Responsabilidade |
|---|---|
| Web UI | Login, cadastro, upload, dashboard, jobs, resultados e configurações |
| API Gateway | Entrada única, autenticação, autorização de usuário, proxy e composição de respostas |
| Storage | Usuários, arquivos lógicos, jobs e resultados no PostgreSQL |
| File Management | Upload, download, armazenamento físico e upload chunked |
| Transcription | Whisper, processamento síncrono/assíncrono e resultados em Redis |
| Summarization | Resumo extractive e modelos configuráveis, síncrono/assíncrono |
| Batch Processor | Orquestra processamento em lote e acompanha arquivos individuais |
| Audio Extraction | Extração com FFmpeg e filas próprias |
| RabbitMQ | Filas, retries e dead-letter queues |
| Redis | Cache, tokens, estado e resultados temporários |

## Fluxos críticos

### Transcrição assíncrona

1. Usuário autentica na Web UI.
2. Arquivo é enviado ao Gateway e ao File Management.
3. Gateway chama `/api/v1/transcribe/async` no serviço de transcrição.
4. Serviço cria job, publica mensagem no RabbitMQ e processa com Whisper.
5. Resultado e erro são persistidos no Redis.
6. Gateway expõe status e resultado para a Web UI.

### Sumarização

O modo padrão local é `extractive`. Ele não carrega pipeline Hugging Face; por isso o health check reconhece esse modo como operacional.

### Segurança atual

O Gateway protege a entrada e propaga identidade por headers internos. A autenticação criptográfica própria entre todos os microsserviços ainda é uma evolução pendente.
