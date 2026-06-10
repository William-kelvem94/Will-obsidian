---
title: "Auto-boletos (Clonado)"
source: "d:/Documents/GitHub/Auto-boletos"
language: Python
private: true
description: "Automação de boletos Equatorial com IA local, Flask, Docker e OCR."
updated: 2026-06-10
tags: [privados, python, flask, docker, ia, automacao, projetos]
date: 2026-04-27
---

# Auto-boletos [[../Projetos.md|Projetos]] [[GitHub-Completo]]

**Status**: 🏗️ Em Desenvolvimento
**Foco**: Automação crítica e processamento de documentos com IA.

## 🌐 Visão Geral (Pública)
Sistema moderno e completo que associa imóveis cadastrados aos dados oficiais da plataforma Equatorial Energy, com **Sistema de IA Local integrado** para análise de débitos e predição de consumo.

## 🛠️ Detalhes de Engenharia (Privado)
- **Backend**: Flask + SQLAlchemy (migrando para Neon DB).
- **Automação**: Playwright (Equatorial Facade) com CAPTCHA handling.
- **IA**: OCR Tesseract + Memória local (Ollama).
- **Frontend**: React/Vite com design responsivo (Tailwind).

## 🎯 Meta 90 Dias (Ciclo Abr/Jun 2026)
- [ ] Parser OCR semântico implementado.
- [ ] Neon Postgres e Prisma operando.
- [ ] Frontend shadcn com revisão de boleto.
- [ ] Documentação de deploy local e CI.

**Estratégia**: [[../EstudosFocados/Auto-boletos|Análise Técnica de Automação]]

## 🏗️ Estrutura
- `src/`: Lógica de automação e modelos de dados.
- `frontend/`: Dashboard de controle dos boletos.
- `docs/`: Documentação de infraestrutura e deployment.

**Links:** [[GitHub-Completo]] | [[05-Skills/Skill-Project-Matrix|📊 Matriz Skills]] #flask #playwright #ocr #python

## 📊 Sincronização Local de Código (Automática)
*Dados técnicos lidos do repositório físico em 2026-06-05 22:19:27*

- **Caminho Físico Local:** `D:/DOCUMENTOS/GitHub/Auto-boletos`
- **Branch Ativa:** `main`
- **Último Commit:** `e371201 - fix: configurar @tailwindcss/postcss para compatibilidade com Tailwind CSS v4 (2026-06-04)`
- **Repositório Remoto (Origin):** [https://github.com/William-kelvem94/Auto-boletos.git](https://github.com/William-kelvem94/Auto-boletos.git)
- **Descrição de README:** [![CI](https://github.com/William-kelvem94/Auto-boletos/actions/workflows/ci.yml/badge.svg)](https://github.com/William-kelvem94/Auto-boletos/actions/...

### 🛠️ Configurações e Arquivos de Infraestrutura
- [x] Dockerfile
- [x] docker-compose.yml
- [x] Arquivo .env.example
- [ ] Tailwind CSS
- [ ] TypeScript config
- [ ] Vite Bundler
- [ ] Next.js configuration
- [ ] Next.js configuration (mjs)
- [ ] TypeScript/JavaScript npm
- [x] Python dependencies

### 📦 Principais Dependências Mapeadas
- **Python (requirements):** `Flask, Flask-SQLAlchemy, Flask-CORS, playwright, python-dotenv, Pillow`