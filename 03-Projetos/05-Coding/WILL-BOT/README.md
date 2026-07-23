---
title: Will Bot — Hub operacional
tipo: projeto
status: prototipo-executavel
tags:
  - projeto
  - will-bot
  - playwright
  - automacao
---

# Will Bot

Hub operacional do projeto Agent Studio AI renomeado para Will Bot.

## Estado atual

- Aplicação React/TypeScript/Vite com servidor Express.
- Execução real de navegador com Playwright e Chromium no Docker.
- Navegação, inspeção DOM, preenchimento, extração, JavaScript e screenshots reais.
- Memória operacional persistente por origem de URL em `data/url-memory.json`.
- Cofre, provedores de IA e chat com seleção explícita do provedor configurado.
- Persistência local em JSON; o SQL do Supabase existe, mas o backend observado ainda usa armazenamento em memória para parte dos dados.
- Automação de navegador deixou de ser simulada; integrações de provedor offline agora retornam erro real.

## Validações

- `tsc --noEmit` e build de produção passaram.
- Lint e build passaram após os ajustes de execução.
- Imagem Docker com Chromium Alpine foi construída.
- Teste ponta a ponta em página controlada confirmou navegação, DOM, preenchimento, extração e screenshot.
- Healthcheck foi ajustado para usar Node, pois a imagem Alpine não inclui `wget`.

## Decisões e limites

- O fluxo inicial abre vazio em `about:blank`, sem credenciais ou workflows fictícios.
- O chat tem seletor próprio e usa exatamente o provedor escolhido, sem fallback silencioso.
- A memória por URL deve ser consultada antes das ações e atualizada após execuções reais.
- A camada de tarefas operacionais está em refatoração: objetivo, URL, memória, conta, plano, aprovação, execução e resultado devem formar uma unidade persistida.

## Sessões

- [[Sessoes/2026-07-23-Will-Bot-Execucao-Real]]
