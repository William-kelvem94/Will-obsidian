---
title: "Plano de Ação dos Projetos"
description: "Checklist detalhado de ações, prioridades e próximos passos para os projetos do vault Obsidian."
tags:
  - plano
  - acoes
  - projetos
date: 2026-04-27
updated: 2026-06-13
---

# Plano de Ação dos Projetos

## Objetivo
Transformar a organização do vault em um plano operacional: priorizar projetos, mapear entregáveis e criar uma rotina de atualização.

## Como o Obsidian está organizado
- `Bem-vindo.md`: entrada principal do cofre.
- `Projetos.md`: MOC do vault com projetos públicos por linguagem.
- `Projetos/GitHub-Completo.md`: inventário geral dos 67 repositórios.
- `Projetos/Privados/`: projetos clonados localmente com notas de análise.
- `Projetos/EstudosFocados/`: roadmap, diário de bordo e visão estratégica.
- `Projetos/Objetivos/`: metas do ciclo, OKRs e planejamento de 90 dias.
- `Projetos/EstudosPesquisas/`: recursos técnicos para evolução dos projetos.
- `Cerebro-Will.md`: perfil, skills e contexto para IA local.

## Ação imediata (hoje)
1. Abra `Projetos/Plano-de-Acao.md` como checklist central.
2. Atualize `Projetos/README.md` e `Bem-vindo.md` com links para as notas de ação.
3. Para cada projeto em `Projetos/Privados/`, confirme se há documentação de execução e run commands.
4. Crie notas de status rápido para os projetos públicos que ainda não têm análise profunda.
5. Use `Projetos/EstudosFocados/` para alinhar roadmap e prioridades dos projetos mais estratégicos.

## Projetos públicos (valem documentação mínima)
### Python
- `Automatizador`
  - status: projeto documentado em nota pública.
  - ação: verificar se o repositório existe no GitHub e se há README atualizado.
  - próximo passo: adicionar sumário de features, run commands e roadmap minimal.

- `TRADUTOR-WKP`
  - status: projeto documentado em nota pública.
  - ação: confirmar dependências Python e oferecer comando de teste.
  - próximo passo: criar checklist de melhorias e deploying se estiver pronto.

### PHP
- `CRUD_VENDAS_WILL`, `CRUD_BASICO4.0`, `CRUD_BASICO-3.0`, `CRUD_BASICO-2.0`, `crud_basico`
  - status: notas placeholder públicas com links GitHub.
  - ação: consolidar esses projetos em uma visão única de CRUD PHP.
  - próximo passo: atualizar cada nota com stack, features e estado atual.

### Java
- `Atividade-01`, `Atividade-03`
  - status: notas específicas de atividades.
  - ação: indexar em `Projetos.md` e garantir que os comandos de compilação/tests estão descritos.
  - próximo passo: documentar propósito e resultados esperados.

### Outros
- `DIA-DAS-MULHERES`
  - status: projeto CSS/PWA documentado.
  - ação: verificar se há hospedagem/demo e se a PWA está funcional.
  - próximo passo: adicionar notas de deploy (Netlify/Vercel) se for o caso.

- `Auto-boletos`, `Gestor Aluguel 2.0`
  - status: presentes tanto em `Projetos/Outros/` quanto em `Projetos/Privados/`.
  - ação: alinhar o histórico público com a versão clonada privada.
  - próximo passo: manter `Outros` como versão resumida/visão e `Privados` como análise profunda.

## Projetos clonados e maiores prioridades
### Auto-boletos
- Status: clone local Python Flask/Docker com AI e OCR.
- Ação: validar se `Docker compose` e `frontend` rodam sem erro.
- Prioridade: alta, porque já tem roadmap e está próximo de MVP.
- Próximos passos:
  - migrar SQLite para Neon Postgres
  - substituir regex por análise semântica OCR
  - melhorar UI com shadcn

### gestor_aluguel_2.0
- Status: clone Next.js SaaS enterprise com Prisma e AI Gemini.
- Ação: revisar documentação de deploy e scripts Docker.
- Prioridade: alta, porque é produto SaaS com monetização clara.
- Próximos passos:
  - configurar Vercel/Neon deploy
  - implementar fallback Ollama local para AI
  - ativar Stripe/Asaas sandbox

### DEEP-LEARNING
- Status: clone AI agent com RAG e speech.
- Ação: confirmar se a API FastAPI e o frontend Gradio existem.
- Prioridade: média-alta, sem modelo offline ainda.
- Próximos passos:
  - testar inferência local Ollama/TensorFlow Lite
  - criar pipeline LoRA PT-BR
  - documentar benchmarks CPU

### IA-LOCAL
- Status: clone JARVIS local com FAISS e voice.
- Ação: validar dependências de `OpenRouter`, `Whisper` e pyautogui.
- Prioridade: média, foco offline e visão.
- Próximos passos:
  - trocar OpenRouter por Ollama offline
  - integrar faster-whisper + Piper TTS
  - adicionar visão MediaPipe e OCR de tela

### PROJECT_JARVIS_5.0
- Status: clone multimodal FastAPI + Next.js + LiveKit.
- Ação: revisar arquitetura de agentes e o script `start-jarvis.bat`.
- Prioridade: média-alta, pois é o projeto mais avançado de voz/vision.
- Próximos passos:
  - preparar backend Ollama local
  - adicionar YOLOv8 nano para visão
  - criar swarm/docker deploy local

### DIA DAS MULHERES
- Status: clone CSS PWA.
- Ação: testar offline e deploy PWA.
- Prioridade: baixa a média.
- Próximos passos:
  - validar `sw.js` e manifest
  - padronizar assets e documentação

### openclaude-wk
- Status: clone TS CLI agent multi-provider.
- Ação: confirmar suporte a OpenAI, Gemini, Ollama, GitHub Models.
- Prioridade: média.
- Próximos passos:
  - documentar providers suportados
  - mapear workflows de dev e deploy

## Notas de pesquisa, objetivos e evolução
- `Projetos/EstudosFocados/` deve ser o repositório de decisões estratégicas.
- `Projetos/Objetivos/` deve ser o repositório de metas e ciclos de 90 dias.
- `Projetos/EstudosPesquisas/` deve conter guias técnicos reutilizáveis.
- Ação: vincular cada projeto privado ao seu checklist de pesquisa e aos seus objetivos relevantes.
- Próximos passos:
  - adicionar links diretos de `EstudosFocados` para `AI-Local-Gratuita`, `Docker-Prod-Gratis`, `Next.js-SaaS-Evolution`.
  - usar essas notas como base para “como evoluir” cada projeto.
  - usar `Projetos/Objetivos/90-dias` como referência de prioridades do ciclo.

## Rotina de atualização do vault
- Sempre que um novo projeto for adicionado, atualize `Projetos.md`, `GitHub-Completo.md` e `Plano-de-Acao.md`.
- Se criar um clone privado, adicione um arquivo em `Projetos/Privados/` com metadata `source:` e `updated:`.
- Para qualquer projeto estratégico, mantenha um bloco `## Diário de Bordo` com datas e atividades.
- Se o projeto for apenas documentação, mantenha-o em `Projetos/Outros/` ou `Projetos/Públicos/` com status claro.
- Se o projeto está em desenvolvimento ativo, coloque em `Projetos/Privados/` e adicione análise.

## Organização de prioridades
### Prioridade alta
- `gestor_aluguel_2.0`
- `Auto-boletos`
- `PROJECT_JARVIS_5.0`

### Prioridade média
- `DEEP-LEARNING`
- `IA-LOCAL`
- `openclaude-wk`

### Prioridade baixa / manutenção
- `DIA DAS MULHERES`
- `Automatizador`
- PHP CRUDs

## Estrutura recomendada para novos projetos
- Notas públicas pequenas e linkadas em `Projetos/`.
- Projetos com código ativo devem ter notas em `Projetos/Privados/`.
- Roadmaps estratégicos devem ficar em `Projetos/EstudosFocados/`.
- Objetivos e metas de ciclo devem ficar em `Projetos/Objetivos/`.
- Recursos gerais devem ficar em `Projetos/EstudosPesquisas/`.

## Checklist de manutenção
- [x] Atualizar índices centrais (`Bem-vindo`, `Projetos.md`, `Projetos/README.md`)
- [x] Criar `Projetos/Plano-de-Acao.md`
- [x] Criar `Projetos/Privados/README.md`
- [ ] Validar execução dos clones privados e registrar status
- [ ] Sincronizar notas públicas com versão privada onde houver duplicação
- [ ] Definir prioridade de entrega para cada projeto nos próximos 30 dias
- [ ] Capturar históricos de commit quando possível

## Observações importantes
- Os dados de `source:` e `updated:` nas notas já funcionam como metadados principais.
- Se você quiser, posso continuar e criar um ficheiro de “roadmap 90 dias” para os 3 projetos mais importantes: `gestor_aluguel_2.0`, `Auto-boletos` e `PROJECT_JARVIS_5.0`.

[[03-Projetos/README|← Voltar ao índice de Projetos]]
