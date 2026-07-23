---
title: Will Bot — execução real e memória por URL
tipo: sessao-projeto
data: 2026-07-23
projeto: Will Bot
tags:
  - will-bot
  - playwright
  - docker
  - memoria-operacional
---

# Will Bot — execução real e memória por URL

## Objetivo

Transformar o protótipo Agent Studio AI em uma entrega executável, removendo simulações e conectando navegador, memória, cofre, provedores e chat.

## Ações e decisões

- Renomeada a identidade visível para Will Bot.
- Criado Dockerfile de produção e ajustado o Compose.
- Ativado Chromium real via Playwright; a imagem oficial foi abandonada por tempo de build, e a imagem Node Alpine com Chromium foi validada.
- Removidos fallbacks que inventavam sucesso para Ollama/LM Studio e removidos presets e credenciais fictícios.
- Adicionada persistência local em JSON e proteção do executor de código, desativado por padrão.
- Adicionada memória operacional por origem de URL, com passos, instruções, conta associada, `lastUsedAt` e `useCount`.
- Adicionado botão explícito para salvar configurações de provedores.
- Adicionado seletor próprio no chat para usar o provedor, modelo, endpoint, chave, temperatura e prompt selecionados.
- Persistido o provedor ativo em `data/active-llm-provider.json`; a chave configurada no cartão do Gemini passou a ser considerada.
- Iniciada a unificação em uma tarefa operacional persistida com plano, aprovação, execução e resultado.

## Testes e resultados

- TypeScript, lint e build de produção passaram.
- Container respondeu às APIs e o executor protegido retornou `403` conforme esperado.
- Healthcheck funcional foi corrigido para não depender de `wget` ausente na imagem Alpine.
- Teste ponta a ponta controlado confirmou navegação Chromium, inspeção DOM, preenchimento real, extração de `real@example.com` e screenshot em base64.
- O SQL do Supabase está preparado, mas o backend observado ainda mantém parte dos dados em memória.
- A automação real foi validada; a camada de tarefas ainda está em refatoração e requer validação final de ponta a ponta.

## Riscos e próximos passos

- Concluir e testar o ciclo completo de tarefa operacional no frontend e backend.
- Validar persistência real após reinicialização do container e confirmar a fronteira entre armazenamento local e Supabase.
- Manter segredos fora de notas e revisar arquivos de dados antes de qualquer publicação.

## Fonte

- Sessão Codex de 23/07/2026, consolidada por eventos operacionais relevantes; prompts, raciocínio privado, payloads extensos e chaves foram excluídos.
