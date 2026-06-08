---
title: "Gestor de Aluguel 2.0 - Render, WAHA e n8n"
date: 2026-06-01
tags: [projetos]
updated: 2026-06-08
---

# Gestor de Aluguel 2.0 - Render, WAHA e n8n

## Decisao atual

- `Render` hospeda apenas a camada de integracao:
  - `n8n`
  - `WAHA`
  - banco do `n8n`
- `Supabase` fica para:
  - banco principal
  - auth
  - storage
- `Vercel` continua como host do SaaS web, se mantivermos esse arranjo

## Estrutura em 3 camadas

### 1. Automacao

- n8n busca dados do SaaS
- WAHA envia mensagens
- uso:
  - lembretes de boleto
  - alertas de vencimento
  - avisos operacionais

### 2. Bot de leitura

- consultas seguras via WhatsApp
- somente leitura no inicio
- exemplos:
  - boletos que vencem hoje
  - contratos perto do vencimento
  - status de um pagamento

### 3. Acoes sensiveis

- criar, editar, cancelar e baixar pago continuam no app
- se algum dia forem para o WhatsApp, precisa de confirmacao dupla

## O que entra no Render

- `render.yaml` com:
  - `gestor-aluguel-n8n`
  - `gestor-aluguel-waha`
  - `gestor-aluguel-n8n-db`
- WAHA com disco persistente em `/app/.sessions`
- n8n com `WEBHOOK_URL` ajustado depois do deploy

## Porque isso faz sentido

- nao conflita com Supabase
- nao mistura runtime do SaaS com automacao
- facilita pausar, testar e trocar workflows
- deixa o WhatsApp como canal, nao como fonte de verdade

## Pontos de atencao

- planos free nao servem bem para esse caso
- WAHA precisa de persistencia
- n8n precisa ficar sempre online para webhooks e rotinas

## Fluxo recomendado

1. subir n8n e WAHA no Render
2. conectar a sessao do WhatsApp
3. testar notificacoes
4. criar bot de leitura
5. deixar acoes sensiveis no app com confirmacao

## Documentos do projeto

- [D:\GitHub\gestor_aluguel_2.0\docs\RENDER_WAHA_N8N.md](D:\GitHub\gestor_aluguel_2.0\docs\RENDER_WAHA_N8N.md)
- [D:\GitHub\gestor_aluguel_2.0\docs\WHATSAPP_N8N_ACTIVATION_STATUS.md](D:\GitHub\gestor_aluguel_2.0\docs\WHATSAPP_N8N_ACTIVATION_STATUS.md)
- [D:\GitHub\gestor_aluguel_2.0\docs\QUICK_START_N8N.md](D:\GitHub\gestor_aluguel_2.0\docs\QUICK_START_N8N.md)

