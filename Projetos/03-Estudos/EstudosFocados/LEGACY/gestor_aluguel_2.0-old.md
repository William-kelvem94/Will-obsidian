---
title: "Estudos Focado: gestor_aluguel_2.0"
description: "Documento de estratégia para o gestor_aluguel_2.0: produto SaaS imobiliário, monetização e roadmap de AI local." 
tags:
  - gestor
  - projetos
  - analise
  - estrategia
  - saas
  - imobiliario
date: 2026-04-27
updated: 2026-05-10
---

# Estudos Focado: gestor_aluguel_2.0 [[README]] [[Privados/gestor_aluguel_2.0]]

**Quartel-General da Estratégia**
- Esta nota define a estratégia do SaaS imobiliário antes de executar a próxima fase.
- Aqui são decididas as prioridades de monetização, AI local, deploy e modelo de dados.
- Referências técnicas: [[../EstudosPesquisas/README|Estudos e Pesquisas]].

## Missão do projeto
Construir uma plataforma de gestão de imóveis que permita administradoras e proprietários gerenciarem contratos, cobranças, inadimplência e comunicação de forma integrada.

## Proposta de valor
- Para administradoras: reduzir atrito operacional com contratos, financeiro e comunicação automática.
- Para inquilinos: facilidade de pagamento e transparência via portal.
- Para o produto: posicionar como SaaS imobiliário com AI preditiva e suporte local/ou híbrido.

## Usuário e mercado
**Segmento alvo**
- Administradoras de 10 a 500 imóveis.
- Proprietários que já usam sistemas manuais ou planilhas.
- Pequenas imobiliárias em busca de upgrade digital.

**Tamanho de mercado**
- O produto se encaixa em um mercado de SaaS para gestão imobiliária com potencial de R$49-199 por imóvel/mês.
- A diferenciação está em AI local/híbrida e integrações de pagamento.

## Métricas de sucesso
- Número de clientes pagantes no primeiro MVP > 3.
- Tempo para emitir contrato/recibo < 10 minutos.
- Redução de inadimplência projetada em >10%.
- Taxa de ativação do portal inquilino > 50%.

## Hipóteses estratégicas
- O mercado aceita um MVP com deploy hobby em Vercel e banco Neon free.
- Fallback para AI local é necessário para reduzir custo de Gemini.
- Automatizar contratos e notificações é o valor mais importante.
- Modelagem multi-tenant em Prisma é adequada para crescimento.

## Situação atual e gaps
- Produto robusto com Next.js 15, Prisma e muitos módulos já conectados.
- Gap de deploy/infra: ainda vale validar a esteira de produção e o comportamento de runtime.
- Gap de monetização: ainda precisa de uma visão comercial fechada e repetível.
- Gap de AI: há bastante IA no código, mas o custo/operacional ainda merece estratégia.

## Arquitetura estratégica
- Frontend: Next.js App Router + Tailwind + Radix/shadcn.
- Backend/DB: Prisma + Postgres com `saasTenantId` em toda a base.
- AI: Gemini, OCR, RAG, treinamento e microserviço Python de apoio.
- Pagamentos: Asaas como integração principal observada no código.
- Observabilidade: Sentry, Pino, audit logs, health checks e métricas.

## Mapa técnico confirmado no código

- **Entrada**: `server.ts` e `src/app/layout.tsx`.
- **Rotas protegidas**: `src/app/(protected)/dashboard`, `usuarios`, `perfil`, `relatorios`.
- **Portal do inquilino**: `src/app/portal` com APIs próprias.
- **Core de negócio**: imóveis, inquilinos, contratos, pagamentos, manutenção, documentos, notificações e equipe.
- **Integrações**: Asaas, n8n, WAHA/WhatsApp, email, Supabase Storage, push notifications.
- **IA**: `src/lib/ai`, `src/app/api/ai`, `infrastructure/microservices/ai-service`.
- **Base de dados**: `prisma/schema.prisma` com tenant isolation e tabelas de suporte para auditoria, chat, webhooks e preferências.

## Roadmap estratégico
### Fase 1 — MVP de deploy e vendas (4 semanas)
- Publicar/estabilizar ambiente de produção com a stack atual.
- Fechar onboarding, cadastro e jornada principal do gestor.
- Validar primeiro cliente piloto.

### Fase 2 — AI local e documentos (8 semanas)
- Avaliar custo real de IA e pontos onde o fallback local faz sentido.
- Consolidar OCR e extração de dados de documentos.
- Refinar previsões e alertas de inadimplência.

### Fase 3 — Monetização e escala (16 semanas)
- Definir modelo comercial e pricing.
- Explorar automações, parceiros e fluxos de retenção.
- Evoluir mobile/PWA só se isso entrar como vantagem clara.

## Dependências e decisões
- Host: Vercel hobby vs deploy local/container.
- AI: manter Gemini ou migrar gradualmente para Ollama.
- Pagamentos: Asaas como principal ou Stripe direto.
- Dados: multi-tenant isolado vs esquema único com tenantId.

## Fluxos principais confirmados

- **Contrato**: UI/API de contratos -> `ContractService` -> valida tenant -> cria contrato -> gera cronograma financeiro -> pode abrir cobrança Asaas -> atualiza propriedade/inquilino -> audit log -> e-mail.
- **Pagamento**: UI/API de payments -> `PaymentService` -> valida contrato/tenant -> cria pagamento local -> histórico + auditoria -> sincroniza Asaas quando aplicável.
- **Portal do inquilino**: `/portal` -> login/registro por token -> `portal/layout.tsx` -> `TenantAuthGuard` -> páginas protegidas e APIs próprias do portal.

## Checklist provável de correção

- Tenant isolation
- Sincronia contrato -> parcelas -> Asaas
- Webhook Asaas atualizando pagamento local
- Token do portal e guard de autenticação
- Status de property/tenant/contract após transições
- Auditoria e histórico nas mutações
- Rotas do portal e contratos vinculados
- Regressões de UI nas páginas cliente

## Arquivos-chave por fluxo

- Contrato: `src/app/(protected)/contratos/page.tsx`, `src/app/api/contracts/route.ts`, `src/lib/services/contract-service.ts`
- Pagamento: `src/app/(protected)/financeiro/page.tsx`, `src/app/api/payments/route.ts`, `src/lib/services/payment-service.ts`
- Portal: `src/app/portal/page.tsx`, `src/app/portal/layout.tsx`, `src/components/portal/TenantAuthGuard.tsx`, `src/app/portal/api/contracts/route.ts`, `src/lib/auth/tenant-auth.ts`

## Tabela curta

| Fluxo | Tela | API | Service | Banco | Risco |
|---|---|---|---|---|---|
| Contrato | Contratos admin | `src/app/api/contracts/route.ts` | `src/lib/services/contract-service.ts` | `Contract`, `Payment`, `Tenant`, `Property` | tenant scope e cronograma |
| Pagamento | Financeiro admin | `src/app/api/payments/route.ts` | `src/lib/services/payment-service.ts` | `Payment`, `Contract` | status divergente do Asaas |
| Portal | Portal do inquilino | `src/app/portal/api/contracts/route.ts` | `src/lib/auth/tenant-auth.ts` | `TenantUser`, `TenantContract` | vazamento entre tenants |

## Auditoria resumida

- Webhook Asaas com risco de falha por `timingSafeEqual`
- Cobrança automática com risco de `UNDEFINED` no tipo do Asaas
- Contrato `DRAFT` marcando imóvel como `OCCUPIED`
- Stub incompleto em `billingNextMonth`
- `GET /api/contracts` com side effect de mutação
- `GET /api/payments/[id]` com `JSON.parse` frágil e campo ausente
- Portal expondo token também no JSON
- Build ignorando erros de TS/ESLint em Docker
- `openGraph.url` hardcoded para localhost
- Falhas do Asaas retornando `null` silenciosamente
- Side effects de expiração em leitura de contratos
- Melhorias: reduzir `any`, padronizar sessão do portal, adicionar testes

## Riscos
- Custo de Gemini inviabiliza o modelo sem fallback.
- Multi-tenant aumenta complexidade de segurança e dados.
- UX pesado ou onboarding ruim pode bloquear adoção.
- Dependência de Neon free limita escala inicial.

## Decisões pendentes
- Priorizar AI local ou fechar MVP sem AI avançada?
- Abrir marketplace de fornecedores agora ou depois do lançamento do core?
- Usar PWA para inquilino ou app mobile nativo mais tarde?

## Diário de Bordo
- 09/04/2026 10:56:32 — nota criada com visão estratégica.
- 09/04/2026 10:56:39 — roadmap e metas de monetização definidas.

## Próximas ações imediatas
- Criar roteiro de lançamento para piloto em Vercel.
- Mapear jornada de vendas para administradoras.
- Definir arquitetura de fallback Ollama local.
- Elaborar proposta de valor e preço inicial.

## Referências
- [[../EstudosPesquisas/gestor_aluguel_2.0|Pesquisa Gestor Aluguel]]
- [[../EstudosPesquisas/Next.js-SaaS-Evolution|Next.js SaaS Evolution]]
- [[../Plano-de-Acao|Plano de Ação]]

## WhatsApp + n8n

Status atual:
- O app j� tem clientes, rotas e dashboard para WAHA/n8n.
- Os clientes agora aceitam `WAHA_API_URL`/`WAHA_URL` e `N8N_WEBHOOK_URL`/`N8N_URL`.
- O reposit�rio ainda n�o cont�m todos os workflows exportados do n8n para importa��o 1-clique.

O que j� existe no projeto:
- `src/lib/integrations/whatsapp-client.ts`
- `src/lib/integrations/n8n-client.ts`
- `src/lib/services/webhook-service.ts`
- `src/app/api/whatsapp/start/route.ts`
- `src/app/api/whatsapp/session/route.ts`
- `src/app/api/integrations/whatsapp/send/route.ts`
- `src/app/api/integrations/whatsapp/status/route.ts`
- `src/app/api/n8n/payments/route.ts`
- `src/app/api/n8n/contracts/route.ts`
- `src/app/api/n8n/properties/route.ts`
- `src/app/api/n8n/notify/route.ts`
- `src/app/api/webhooks/trigger/route.ts`
- `src/app/api/webhooks/receive/route.ts`
- `src/components/integrations/IntegrationDashboard.tsx`

Pr�ximo passo recomendado:
1. Subir Docker com app + n8n + WAHA.
2. Configurar `N8N_API_KEY`, `N8N_WEBHOOK_SECRET`, `WAHA_API_URL`, `WAHA_API_KEY`, `WAHA_SESSION_NAME`.
3. Conectar a sess�o default no WAHA.
4. Importar/criar os workflows de lembrete no n8n.
5. Testar `/api/integrations/n8n/test` e `/api/integrations/whatsapp/status`.
