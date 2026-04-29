---
title: "Evolução Auto-boletos"
description: "Melhorias gratuitas/locais: Ollama AI avançada, Docker prod, Playwright headless."
tags:
  - auto-boletos
  - projetos
  - evolucao
date: 2026-04-27
updated: 2026-04-29
---

# Evolução Auto-boletos [[README]]

**Atual**: Flask Docker React OCR Tesseract CAPTCHA.

**Melhorias gratuitas**:

1. **AI Avançada (Ollama local)**:
   - Troque regex por Ollama qwen2.5: análise boleto sem API
   - `ollama run qwen2.5` + langchain for RAG boletos antigos
   - Tut: https://github.com/ollama/ollama-python

2. **Docker Prod**:
   - Traefik reverse proxy gratuito em vez Nginx
   - `docker compose + traefik.yml` (cert Let's Encrypt free)
   - Watchtower auto-update containers

3. **Playwright Headless + Stealth**:
   - Anti-detect browser: `playwright-stealth`
   - `pip install playwright-stealth`

4. **Frontend Vite + Shadcn**:
   - Migre React para Vite + Tailwind shadcn (mais rápido)
   - `npm create vite@latest -- --template react-ts`

**Roadmap**:
- [ ] Ollama OCR + análise semântica
- [ ] Traefik + DB Postgres
- [ ] Shadcn UI + dark mode

Recursos: [[AI-Local-Gratuita]] [[README]] #flask #ollama
