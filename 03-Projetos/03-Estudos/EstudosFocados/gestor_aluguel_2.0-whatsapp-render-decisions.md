---
title: "Gestor de Aluguel 2.0 - Decisões WAHA, n8n, Render e Supabase"
date: 2026-06-01
tags: [projetos]
updated: 2026-06-08
---

# Gestor de Aluguel 2.0 - Decisões WAHA, n8n, Render e Supabase

## Estado atual

- o projeto já tem base de WAHA e n8n
- o SaaS principal continua separado
- WhatsApp é canal auxiliar
- n8n é automacao

## O que foi conversado

1. automacao primeiro
2. bot de leitura depois
3. acoes sensiveis continuam no app
4. se forem para o WhatsApp, precisam de confirmacao dupla

## O que decidimos por enquanto

- nao mexer agora no WAHA/n8n
- manter o que ja existe no projeto
- documentar a direcao
- deixar a ativacao para depois, com calma

## Observacoes importantes

- Render free pode dormir
- WAHA sem disco persistente e mais arriscado
- n8n precisa de disponibilidade para webhooks e agendamentos
- Supabase nao e host ideal para containers persistentes

## Sugestao de uso

- WhatsApp como aviso e consulta
- app como fonte de verdade
- confirmacao dupla para acoes criticas

## Arquivos principais

- [D:\GitHub\gestor_aluguel_2.0\docs\WHATSAPP_RENDER_DECISIONS.md](D:\GitHub\gestor_aluguel_2.0\docs\WHATSAPP_RENDER_DECISIONS.md)
- [D:\GitHub\gestor_aluguel_2.0\docs\WHATSAPP_N8N_ACTIVATION_STATUS.md](D:\GitHub\gestor_aluguel_2.0\docs\WHATSAPP_N8N_ACTIVATION_STATUS.md)
- [D:\GitHub\gestor_aluguel_2.0\docs\RENDER_WAHA_N8N.md](D:\GitHub\gestor_aluguel_2.0\docs\RENDER_WAHA_N8N.md)

