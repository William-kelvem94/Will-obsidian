---
title: "Estudos Focado: gestor_aluguel_2.0"
description: "Documento de estratégia para o gestor_aluguel_2.0: produto SaaS imobiliário, monetização e roadmap de AI local." 
tags:
  - gestor
  - analise
  - estrategia
  - saas
  - imobiliario
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
- Produto robusto com Next.js, Prisma e muitas features.
- Gap de deploy/infra: ainda não há produção estável e fallback offline.
- Gap de monetização: falta checkout e fluxo de vendas claro.
- Gap de AI: dependência Gemini e ausência de infra local barata.

## Arquitetura estratégica
- Frontend: Next.js App Router + shadcn Tailwind.
- Backend/DB: Prisma + Postgres, multi-tenant.
- AI: Gemini para predição e RAG atualmente, Ollama local como fallback.
- Pagamentos: Asaas + Stripe para B2B e cobrança.
- Observabilidade: Sentry, Pino, audit logs.

## Roadmap estratégico
### Fase 1 — MVP de deploy e vendas (4 semanas)
- Publicar no Vercel com Neon Postgres free.
- Implantar auth Clerk com MFA e multi-tenant básico.
- Preparar pipeline de onboarding e documentação comercial.
- Validar primeiro cliente piloto.

### Fase 2 — AI local e documentos (8 semanas)
- Criar fallback Ollama qwen2.5-coder local para predição de inadimplência.
- Adicionar OCR local com Tesseract.js para digitalização de documentos.
- Construir mecanismo de alertas de inadimplência.

### Fase 3 — Monetização e escala (16 semanas)
- Lançar Stripe checkout e checkout Asaas sandbox.
- Explorar marketplace de fornecedores e parcerias.
- Desenvolver PWA ou app móvel leve.

## Dependências e decisões
- Host: Vercel hobby vs deploy local/container.
- AI: manter Gemini ou migrar gradualmente para Ollama.
- Pagamentos: Asaas como principal ou Stripe direto.
- Dados: multi-tenant isolado vs esquema único com tenantId.

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
