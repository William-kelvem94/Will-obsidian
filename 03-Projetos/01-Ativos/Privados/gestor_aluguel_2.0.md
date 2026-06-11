---
title: "gestor_aluguel_2.0 (Clonado)"
source: "d:/Documents/GitHub/gestor_aluguel_2.0"
language: TypeScript
private: true
description: "SaaS Imobiliário Enterprise: Next.js 15, Multi-tenant, AI-Driven."
updated: 2026-06-10
tags: [privados, nextjs, typescript, prisma, saas, ai, projetos]
date: 2026-04-27
---

# Gestor de Aluguel 2.0 🏠 [[../Projetos.md|Projetos]]

**Status**: 🚀 Produção / Estabilização
**Escala**: Enterprise Multi-tenant (43+ Models Prisma)

## 🌐 Visão Geral (Pública)
Plataforma SaaS imobiliário completo com gestão de imóveis, inquilinos, contratos dinâmicos (TipTap/Yjs), financeiro integrado (Asaas) e portal para o inquilino.

## 🛠️ Detalhes de Engenharia (Privado)
- **Framework**: Next.js 15 (App Router).
- **Inteligência**: Google Gemini para análise de risco de inadimplência.
- **Integrações**: WhatsApp (WAHA) e n8n para webhooks.
- **Segurança**: MFA/TOTP, Audit Logs e Rate Limiting.

## 🎯 Meta 90 Dias (Ciclo Abr/Jun 2026)
- [ ] Deploy do frontend em Vercel.
- [ ] Banco Postgres em Neon configurado.
- [ ] Autenticação Clerk com MFA funcionando.
- [ ] Fluxo de pagamento sandbox com Asaas/Stripe.

**Estratégia**: [[../EstudosFocados/gestor_aluguel_2.0|Roadmap de Evolução SaaS]]

## 📈 Atualizações Recentes (Junho 2026)
- **Organização de Arquivos e Logs**: Centralização de arquivos temporários de teste e logs na raiz do projeto para subpastas dedicadas `/logs` e `/temp`, mantendo o repositório organizado e o Git devidamente configurado para ignorá-los.
- **Sinalização do Capítulo 4 do TCC**: Consolidação física e linkagem no índice `docs/README.md` de todos os relatórios de validação, roteiros e backups de evidências Word (`.docx`).
- **Compatibilidade Local com Windows**: Ajuste de incompatibilidades de shell Unix (`rm -rf` no script `clean` e crashes de caminho no analisador de projeto) para permitir o funcionamento perfeito de todas as ferramentas locais do desenvolvedor no Windows.
- **Validação de E2E no Vercel**: Restauração da configuração do Playwright para rodar testes diretamente contra o site hospedado em produção no Vercel (`https://gestor-aluguel-2-0.vercel.app`).

**Links:** [[gestor_aluguel_2.0-tcc-analise-evolucao|📄 Análise TCC]] | [[GitHub-Completo]] | [[03-Projetos/03-Estudos/EstudosPesquisas/README|🔬 Recursos]] #saas #enterprise #nextjs #prisma #tcc

## 📊 Sincronização Local de Código (Automática)
*Dados técnicos lidos do repositório físico em 2026-06-05 22:19:31*

- **Caminho Físico Local:** `D:/DOCUMENTOS/GitHub/gestor_aluguel_2.0`
- **Branch Ativa:** `main`
- **Último Commit:** `71cb2ed4 - feat: criar portal devops e migração do monitoramento (2026-06-05)`
- **Repositório Remoto (Origin):** [https://github.com/William-kelvem94/Domni.git](https://github.com/William-kelvem94/Domni.git)
- **Descrição de README:** [![Version](https://img.shields.io/badge/version-1.0.0--beta.1-blue.svg)](#)

### 🛠️ Configurações e Arquivos de Infraestrutura
- [x] Dockerfile
- [ ] docker-compose.yml
- [x] Arquivo .env.example
- [x] Tailwind CSS
- [x] TypeScript config
- [ ] Vite Bundler
- [x] Next.js configuration
- [ ] Next.js configuration (mjs)
- [x] TypeScript/JavaScript npm
- [ ] Python dependencies

### 📦 Principais Dependências Mapeadas
- **Node.js (package.json):** `^0.24.0, ^3.10.0, ^1.0.7, ^5.19.1, ^1.1.2, ^1.1.15`