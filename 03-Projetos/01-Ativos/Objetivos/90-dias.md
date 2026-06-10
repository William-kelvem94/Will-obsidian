---
title: "90 Dias de Objetivos"
description: "Plano de 90 dias para projetos prioritários do vault, com metas e entregáveis concretos." 
tags:
  - objetivos
  - projetos
  - 90-dias
  - metas
updated: 2026-06-10
date: 2026-04-27
---

# Objetivos para os Próximos 90 Dias

## Visão geral
Este documento reúne as prioridades do vault para o próximo ciclo de 90 dias, com foco em projetos estratégicos, pesquisa e entrega.

## Objetivos do vault
- Consolidar o vault como um hub de projetos bem organizados e inteligíveis.
- Tornar as notas de estratégia e execução conectadas e fáceis de navegar.
- Estabelecer um fluxo claro: estratégia → objetivos → execução.

## Projetos prioritários
### 1. gestor_aluguel_2.0
- Objetivo: lançar um MVP funcional com deploy Vercel + Neon e testes de pagamento.
- Entregáveis:
  - deploy do frontend em Vercel.
  - banco Postgres em Neon configurado.
  - autenticação Clerk com MFA funcionando.
  - fluxo de pagamento sandbox com Asaas/Stripe.

### 2. Auto-boletos
- Objetivo: estabilizar a extração de boletos e migrar para banco escalável.
- Entregáveis:
  - parser OCR semântico implementado.
  - Neon Postgres e Prisma operando.
  - frontend shadcn com revisão de boleto.
  - documentação de deploy local e CI.

### 3. PROJECT_JARVIS_5.0
- Objetivo: provar o conceito multimodal com voz + visão + automação.
- Entregáveis:
  - backend Ollama local integrado.
  - pipeline de voz em LiveKit + Piper.
  - visão leve com YOLOv8 nano.
  - roteiro de agentes e orquestração inicial.

### 4. DEEP-LEARNING
- Objetivo: criar um agente AI local com RAG válido para uso de negócio.
- Entregáveis:
  - FastAPI + Gradio protótipo funcionando.
  - inferência local testada com Ollama ou TF Lite.
  - pipeline de dataset PT-BR para LoRA.

### 5. IA-LOCAL
- Objetivo: consolidar função Jarvis offline com memória e voz.
- Entregáveis:
  - voice local com faster-whisper e Piper.
  - memória FAISS estável.
  - fluxo seguro de automação de PC.

## Objetivos de pesquisa
- Validar referências de AI local em [[03-Projetos/03-Estudos/EstudosPesquisas/AI-Local-Gratuita|AI-Local-Gratuita]].
- Documentar deploy Docker gratuito em [[03-Projetos/03-Estudos/EstudosPesquisas/Docker-Prod-Gratis|Docker-Prod-Gratis]].
- Capturar boas práticas de SaaS Next.js em [[03-Projetos/03-Estudos/EstudosPesquisas/Next.js-SaaS-Evolution|Next.js-SaaS-Evolution]].

## Resultado esperado no final do ciclo
- Uma pasta de objetivos clara com foco em execução.
- Projetos principais com milestones definidos e status registrado.
- Conexão explícita entre estratégia e implementação.
- Menos duplicação entre notas públicas e privadas.

## Revisão e ajustes
- Revise este plano a cada 30 dias.
- Atualize entregáveis e prioridades conforme testes e validações.
- Mantenha o fluxo: `Projetos/EstudosFocados` → `Projetos/Objetivos` → `Projetos/Plano-de-Acao` → `Projetos/Privados`.
