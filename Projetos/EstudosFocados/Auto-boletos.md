---
title: "Estudos Focado: Auto-boletos"
description: "Centro estratégico do projeto Auto-boletos: valor, riscos, roadmap e critérios para escalonamento." 
tags:
  - auto-boletos
  - projetos
  - analise
  - estrategia
  - saas
  - ocr
date: 2026-04-27
updated: 2026-04-27
---

# Estudos Focado: Auto-boletos [[README]] [[Privados/Auto-boletos]]

**Quartel-General da Estratégia**
- Esta nota consolida as decisões de produto e a direção do Auto-boletos antes da implementação técnica.
- Aqui são definidas as hipóteses de valor, o plano de monetização e o roadmap de evolução.
- Se um requisito não estiver claro, a decisão deve ser registrada neste documento.

## Missão do projeto
Criar uma plataforma de automação de boletos para administração de imóveis que reduz trabalho manual, aumenta a precisão da extração de dados e gera uma experiência de pagamento mais confiável.

## Proposta de valor
- Para imobiliárias pequenas/médias: reduzir o tempo gasto em boletos e diminuir erros de cadastro.
- Para proprietários: gerar boletos e relatórios mais rápidos com menos falhas de leitura.
- Para o produto: transformar automação local em SaaS escalável com assinaturas e integração de pagamentos.

## Contexto estratégico
- Projeto baseado em clone privado de Python/Flask com frontend React/Vite.
- Força atual: fluxo funcional com OCR e automação de login.
- Fraqueza principal: depende de regex e SQLite, o que limita escalabilidade e robustez.
- O próximo ciclo precisa focar em confiabilidade e processamento semântico.

## Usuário e métricas de sucesso
**Usuários-alvo**
- Administradoras de até 100 imóveis.
- Proprietários que precisam automatizar boletos Equatorial.
- Pequenos síndicos sem equipe de TI.

**Métricas chave**
- Taxa de extração correta de boleto > 95%.
- Tempo médio para processar um boleto < 30 segundos.
- Disponibilidade do sistema > 99% em ambiente local/proxy.
- Conversão de protótipo para MVP de 1 cliente piloto.

## Hipóteses estratégicas
- Os usuários aceitam rodar a solução local via Docker para economizar custos de SaaS completo.
- O OCR com Tesseract e embeddings pode substituir a maioria das regex existentes.
- Um backend PostgreSQL em Neon é suficiente para escalar de 1 a 10 clientes.
- Pagamentos Asaas/Stripe podem ser integrados sem bloquear o MVP inicial.

## Roadmap estratégico
### MVP 1.0 — Confiabilidade e base de dados (4 semanas)
- Reestruturar parser de boleto usando embeddings + regras mínimas.
- Migrar SQLite para Neon Postgres + Prisma.
- Refatorar backend Flask para separar extração, processamento e APIs.
- Definir versão inicial do frontend com tema shadcn e dark mode.

### 1.5 — Produção local e automação robusta (8 semanas)
- Implementar Traefik e HTTPS local.
- Adicionar BullMQ para extração assíncrona de boletos.
- Criar painel de monitoramento mínimo (logs, tentativas, erros).
- Preparar deploy frontend em Vercel com backend local híbrido.

### 2.0 — Escala SaaS e monetização (16 semanas)
- Lançar multi-tenant com tenant isolado no Prisma.
- Conectar Stripe/Asaas para pagamentos e boletos de cobrança.
- Criar PWA ou app Expo para acesso móvel básico.

## Arquitetura proposta
- `backend/` [Flask] = API principal, autenticação, jobs, integração Equatorial.
- `extract/` = OCR + embeddings + validação de campos.
- `frontend/` = React/Vite + shadcn + dashboards.
- `infra/` = Docker Compose, Traefik, Postgres, Redis/BullMQ.

## Dependências críticas
- Docker local ou Compose para ambiente do cliente.
- Neon Postgres free tier para banco persistente.
- Ollama ou outra AI local para análise semântica.
- Stripe/Asaas para pagamentos sandbox.

## Riscos e mitigação
- OCR falha em layout novo: criar fallback de validação e captura manual.
- Login Equatorial bloqueado por bot: separar fluxo de CAPTCHA e alertar usuário.
- Banco SQLite não escala: migrar imediatamente para Postgres.
- UI confusa: priorizar fluxo principal e UX simples.

## Decisões pendentes
- Usar Ollama local ou modelo hospedado para análise semântica?
- Executar o backend em Vercel como API proxy ou em Docker Compose puro?
- Abrir suporte inicial somente a Equatorial ou estender para outras utilities?

## Rota de execução
1. Confirmar validação de layout de boleto com 5 casos reais.
2. Implementar Postgres + Prisma e testar importação/consulta.
3. Substituir parser regex por embeddings/AI no fluxo de extração.
4. Atualizar frontend com componente de revisão manual de campos.
5. Documentar deploy e manutenção em `Privados`.

## Diário de Bordo
- 09/04/2026 10:56:08 — nota criada como estratégia initial.
- 09/04/2026 10:56:11 — roadmap e prioridades definidas.

## Próximas ações imediatas
- Documentar o fluxo completo de extração de boleto e erros conhecidos.
- Validar a viabilidade de Neon Postgres para esse MVP.
- Definir o mínimo de dados necessários para o primeiro cliente piloto.
- Listar as APIs e endpoints necessários para integração Asaas/Stripe.

## Referências
- [[../EstudosPesquisas/Auto-boletos|Estudo Auto-boletos]]
- [[../EstudosPesquisas/AI-Local-Gratuita|AI Local Gratuita]]
- [[../Plano-de-Acao|Plano de Ação]]

