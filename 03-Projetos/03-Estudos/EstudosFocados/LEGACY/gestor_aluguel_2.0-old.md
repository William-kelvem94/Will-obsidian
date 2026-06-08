---
title: "Estudos Focado: gestor_aluguel_2.0"
description: "Documento de estratÃ©gia para o gestor_aluguel_2.0: produto SaaS imobiliÃ¡rio, monetizaÃ§Ã£o e roadmap de AI local." 
tags:
  - gestor
  - projetos
  - analise
  - estrategia
  - saas
  - imobiliario
date: 2026-04-27
updated: 2026-06-08
---

# Estudos Focado: gestor_aluguel_2.0 [[README]] [[Privados/gestor_aluguel_2.0]]

**Quartel-General da EstratÃ©gia**
- Esta nota define a estratÃ©gia do SaaS imobiliÃ¡rio antes de executar a prÃ³xima fase.
- Aqui sÃ£o decididas as prioridades de monetizaÃ§Ã£o, AI local, deploy e modelo de dados.
- ReferÃªncias tÃ©cnicas: [[../EstudosPesquisas/README|Estudos e Pesquisas]].

## MissÃ£o do projeto
Construir uma plataforma de gestÃ£o de imÃ³veis que permita administradoras e proprietÃ¡rios gerenciarem contratos, cobranÃ§as, inadimplÃªncia e comunicaÃ§Ã£o de forma integrada.

## Proposta de valor
- Para administradoras: reduzir atrito operacional com contratos, financeiro e comunicaÃ§Ã£o automÃ¡tica.
- Para inquilinos: facilidade de pagamento e transparÃªncia via portal.
- Para o produto: posicionar como SaaS imobiliÃ¡rio com AI preditiva e suporte local/ou hÃ­brido.

## UsuÃ¡rio e mercado
**Segmento alvo**
- Administradoras de 10 a 500 imÃ³veis.
- ProprietÃ¡rios que jÃ¡ usam sistemas manuais ou planilhas.
- Pequenas imobiliÃ¡rias em busca de upgrade digital.

**Tamanho de mercado**
- O produto se encaixa em um mercado de SaaS para gestÃ£o imobiliÃ¡ria com potencial de R$49-199 por imÃ³vel/mÃªs.
- A diferenciaÃ§Ã£o estÃ¡ em AI local/hÃ­brida e integraÃ§Ãµes de pagamento.

## MÃ©tricas de sucesso
- NÃºmero de clientes pagantes no primeiro MVP > 3.
- Tempo para emitir contrato/recibo < 10 minutos.
- ReduÃ§Ã£o de inadimplÃªncia projetada em >10%.
- Taxa de ativaÃ§Ã£o do portal inquilino > 50%.

## HipÃ³teses estratÃ©gicas
- O mercado aceita um MVP com deploy hobby em Vercel e banco Neon free.
- Fallback para AI local Ã© necessÃ¡rio para reduzir custo de Gemini.
- Automatizar contratos e notificaÃ§Ãµes Ã© o valor mais importante.
- Modelagem multi-tenant em Prisma Ã© adequada para crescimento.

## SituaÃ§Ã£o atual e gaps
- Produto robusto com Next.js 15, Prisma e muitos mÃ³dulos jÃ¡ conectados.
- Gap de deploy/infra: ainda vale validar a esteira de produÃ§Ã£o e o comportamento de runtime.
- Gap de monetizaÃ§Ã£o: ainda precisa de uma visÃ£o comercial fechada e repetÃ­vel.
- Gap de AI: hÃ¡ bastante IA no cÃ³digo, mas o custo/operacional ainda merece estratÃ©gia.

## Arquitetura estratÃ©gica
- Frontend: Next.js App Router + Tailwind + Radix/shadcn.
- Backend/DB: Prisma + Postgres com `saasTenantId` em toda a base.
- AI: Gemini, OCR, RAG, treinamento e microserviÃ§o Python de apoio.
- Pagamentos: Asaas como integraÃ§Ã£o principal observada no cÃ³digo.
- Observabilidade: Sentry, Pino, audit logs, health checks e mÃ©tricas.

## Mapa tÃ©cnico confirmado no cÃ³digo

- **Entrada**: `server.ts` e `src/app/layout.tsx`.
- **Rotas protegidas**: `src/app/(protected)/dashboard`, `usuarios`, `perfil`, `relatorios`.
- **Portal do inquilino**: `src/app/portal` com APIs prÃ³prias.
- **Core de negÃ³cio**: imÃ³veis, inquilinos, contratos, pagamentos, manutenÃ§Ã£o, documentos, notificaÃ§Ãµes e equipe.
- **IntegraÃ§Ãµes**: Asaas, n8n, WAHA/WhatsApp, email, Supabase Storage, push notifications.
- **IA**: `src/lib/ai`, `src/app/api/ai`, `infrastructure/microservices/ai-service`.
- **Base de dados**: `prisma/schema.prisma` com tenant isolation e tabelas de suporte para auditoria, chat, webhooks e preferÃªncias.

## Roadmap estratÃ©gico
### Fase 1 â MVP de deploy e vendas (4 semanas)
- Publicar/estabilizar ambiente de produÃ§Ã£o com a stack atual.
- Fechar onboarding, cadastro e jornada principal do gestor.
- Validar primeiro cliente piloto.

### Fase 2 â AI local e documentos (8 semanas)
- Avaliar custo real de IA e pontos onde o fallback local faz sentido.
- Consolidar OCR e extraÃ§Ã£o de dados de documentos.
- Refinar previsÃµes e alertas de inadimplÃªncia.

### Fase 3 â MonetizaÃ§Ã£o e escala (16 semanas)
- Definir modelo comercial e pricing.
- Explorar automaÃ§Ãµes, parceiros e fluxos de retenÃ§Ã£o.
- Evoluir mobile/PWA sÃ³ se isso entrar como vantagem clara.

## DependÃªncias e decisÃµes
- Host: Vercel hobby vs deploy local/container.
- AI: manter Gemini ou migrar gradualmente para Ollama.
- Pagamentos: Asaas como principal ou Stripe direto.
- Dados: multi-tenant isolado vs esquema Ãºnico com tenantId.

## Fluxos principais confirmados

- **Contrato**: UI/API de contratos -> `ContractService` -> valida tenant -> cria contrato -> gera cronograma financeiro -> pode abrir cobranÃ§a Asaas -> atualiza propriedade/inquilino -> audit log -> e-mail.
- **Pagamento**: UI/API de payments -> `PaymentService` -> valida contrato/tenant -> cria pagamento local -> histÃ³rico + auditoria -> sincroniza Asaas quando aplicÃ¡vel.
- **Portal do inquilino**: `/portal` -> login/registro por token -> `portal/layout.tsx` -> `TenantAuthGuard` -> pÃ¡ginas protegidas e APIs prÃ³prias do portal.

## Checklist provÃ¡vel de correÃ§Ã£o

- Tenant isolation
- Sincronia contrato -> parcelas -> Asaas
- Webhook Asaas atualizando pagamento local
- Token do portal e guard de autenticaÃ§Ã£o
- Status de property/tenant/contract apÃ³s transiÃ§Ãµes
- Auditoria e histÃ³rico nas mutaÃ§Ãµes
- Rotas do portal e contratos vinculados
- RegressÃµes de UI nas pÃ¡ginas cliente

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
- CobranÃ§a automÃ¡tica com risco de `UNDEFINED` no tipo do Asaas
- Contrato `DRAFT` marcando imÃ³vel como `OCCUPIED`
- Stub incompleto em `billingNextMonth`
- `GET /api/contracts` com side effect de mutaÃ§Ã£o
- `GET /api/payments/[id]` com `JSON.parse` frÃ¡gil e campo ausente
- Portal expondo token tambÃ©m no JSON
- Build ignorando erros de TS/ESLint em Docker
- `openGraph.url` hardcoded para localhost
- Falhas do Asaas retornando `null` silenciosamente
- Side effects de expiraÃ§Ã£o em leitura de contratos
- Melhorias: reduzir `any`, padronizar sessÃ£o do portal, adicionar testes

## Riscos
- Custo de Gemini inviabiliza o modelo sem fallback.
- Multi-tenant aumenta complexidade de seguranÃ§a e dados.
- UX pesado ou onboarding ruim pode bloquear adoÃ§Ã£o.
- DependÃªncia de Neon free limita escala inicial.

## DecisÃµes pendentes
- Priorizar AI local ou fechar MVP sem AI avanÃ§ada?
- Abrir marketplace de fornecedores agora ou depois do lanÃ§amento do core?
- Usar PWA para inquilino ou app mobile nativo mais tarde?

## DiÃ¡rio de Bordo
- 09/04/2026 10:56:32 â nota criada com visÃ£o estratÃ©gica.
- 09/04/2026 10:56:39 â roadmap e metas de monetizaÃ§Ã£o definidas.

## PrÃ³ximas aÃ§Ãµes imediatas
- Criar roteiro de lanÃ§amento para piloto em Vercel.
- Mapear jornada de vendas para administradoras.
- Definir arquitetura de fallback Ollama local.
- Elaborar proposta de valor e preÃ§o inicial.

## ReferÃªncias
- [[../EstudosPesquisas/gestor_aluguel_2.0|Pesquisa Gestor Aluguel]]
- [[../EstudosPesquisas/Next.js-SaaS-Evolution|Next.js SaaS Evolution]]
- [[../Plano-de-Acao|Plano de AÃ§Ã£o]]

## WhatsApp + n8n

Status atual:
- O app já tem clientes, rotas e dashboard para WAHA/n8n.
- Os clientes agora aceitam `WAHA_API_URL`/`WAHA_URL` e `N8N_WEBHOOK_URL`/`N8N_URL`.
- O repositório ainda não contém todos os workflows exportados do n8n para importação 1-clique.

O que já existe no projeto:
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

Próximo passo recomendado:
1. Subir Docker com app + n8n + WAHA.
2. Configurar `N8N_API_KEY`, `N8N_WEBHOOK_SECRET`, `WAHA_API_URL`, `WAHA_API_KEY`, `WAHA_SESSION_NAME`.
3. Conectar a sessão default no WAHA.
4. Importar/criar os workflows de lembrete no n8n.
5. Testar `/api/integrations/n8n/test` e `/api/integrations/whatsapp/status`.
