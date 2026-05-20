---
title: "Code Review com Agentes"
description: "Como usar IA para revisar PRs e patches com foco em bugs, regressao e risco, nao em estilo."
tags: [ia, code-review, programacao, agentes, qualidade]
updated: 2026-05-08
status: active
---

# Code Review com Agentes

Um agente bom em code review e paranoico com gentileza: ele procura falhas, mas com evidencia. O objetivo e reduzir risco, nao impor preferencia.

## Checklist de Review

- comportamento: o que mudou de verdade?
- compatibilidade: quebra API, contrato, config, env?
- seguranca: loga tokens? abre permissao? executa comandos perigosos?
- concorrencia: race conditions, deadlocks, retries?
- dados: migra, valida, perde informacao?
- observabilidade: logs/metricas suficientes para diagnostico?
- testes: existe teste? cobre o caso? falha antes, passa depois?

## Padrao de Comentarios

Um comentario bom inclui:

- o risco (qual falha pode acontecer);
- a evidencia (arquivo e trecho);
- a sugestao minima (como melhorar sem refatorar tudo);
- como validar (teste/comando).

## Quando Pedir Confirmacao

Antes de sugerir mudanca grande, o agente deve pedir confirmacao se:

- envolve renomear/mover muita coisa;
- altera contratos compartilhados;
- toca em seguranca, auth, pagamentos, dados pessoais;
- muda dependencias ou builds.

## Relacionado

- [[Conhecimento-Geral/IA-para-Programacao/Avaliacao-de-Respostas-de-IA]]
- [[JARVIS/02-Operational/Playbooks/Decision-Logging-Protocol]]
- [[JARVIS/02-Operational/Playbooks/Agent-Confirmation-Protocol]]


[[Conhecimento-Geral/IA-para-Programacao/INDEX|← Voltar ao índice de IA para Programação]]
