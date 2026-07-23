---
title: TRANSCRITOR — Bugs e Correções
project: TRANSCRITOR
updated: 2026-07-23
tags: [bugs, correcoes, troubleshooting]
---

# Bugs e correções

## Principais incidentes registrados

| Problema | Causa | Correção |
|---|---|---|
| Transcrição assíncrona falhava com mensagem genérica | Gateway usava variável inexistente e rota incorreta | Encaminhamento para `/api/v1/transcribe/async` e serviço correto |
| Resultado da transcrição não carregava | Contrato de resultado diferente entre API e UI | Normalização da resposta na Web UI |
| Dashboard ficava em loading | Endpoint de estatísticas e estados não estavam alinhados | Ajuste de rota e persistência |
| Upload grande não concluía | Rotas chunked ausentes e identificador sem validação | Implementação de upload por partes e validação UUID |
| Sumarização não aparecia na UI | UI enviava body incompatível com parâmetros do Gateway | Ajuste do contrato e busca do resultado |
| Batch falhava ao criar/processar | Rotas antigas e modelo duplicado | Correção de URLs, modelo e estados |
| DLQ recebia mensagens duplicadas | Código publicava manualmente e RabbitMQ também roteava | Remoção do encaminhamento manual |
| Health da sumarização ficava degraded | Modo extractive não possui pipeline carregado | Health check reconhece modo nativo |
| Prometheus recebia 422 no extrator | Endpoint exigia headers de usuário | Endpoint Prometheus sem autenticação e formato correto |

## Regra

Novos bugs devem registrar sintoma, reprodução, causa raiz, arquivos envolvidos, commit, teste de regressão e risco residual.
