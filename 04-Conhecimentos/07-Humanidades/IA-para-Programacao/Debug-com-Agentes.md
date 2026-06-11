---
title: "Debug com Agentes"
description: "Como usar agentes de IA para investigar bugs sem chutar, sem reescrever o sistema e sem perder tempo."
tags: [ia, debug, programacao, agentes, qualidade]
updated: 2026-05-08
status: active
---

# Debug com Agentes

O erro mais comum em debug com IA e deixar o agente "inventar" a causa. O objetivo e transformar o agente em um operador de investigacao: observar, reduzir hipotese, validar.

## Entrada Minima (o que fornecer)

- sintoma observavel (erro, log, screenshot, stack trace);
- como reproduzir (passos e dados);
- ambiente (OS, versao, flags, variaveis relevantes);
- escopo permitido (quais pastas/arquivos pode tocar);
- como validar a correcao (teste, comando, comportamento).

## Loop de Investigacao (curto)

1. Reproduzir (ou simular mentalmente com dados concretos).
2. Reduzir o espaco: onde pode estar (camada, modulo, boundary).
3. Formar 2-4 hipoteses pequenas e testaveis.
4. Testar com probes baratos (logs, asserts, unit test curto).
5. Fix pequeno e localizado.
6. Validar e registrar aprendizado.

## Probes Baratos

- procurar a origem do erro com `rg` (nomes, mensagens, endpoints);
- ler primeiro os testes existentes e o README do modulo;
- adicionar log temporario (e remover depois);
- criar um teste minimo que falha antes e passa depois;
- isolar configuracao/feature flag.

## Anti-padroes

- refatorar antes de entender o bug;
- mudar varias coisas de uma vez;
- "corrigir" so o sintoma (ex: try/except sem criterio);
- ignorar validacao.

## Relacionado

- [[04-Conhecimentos/07-Humanidades/IA-para-Programacao/Engenharia-de-Contexto]]
- [[04-Conhecimentos/07-Humanidades/IA-para-Programacao/Avaliacao-de-Respostas-de-IA]]
- [[02-JARVIS/02-Operational/Playbooks/Agent-Confirmation-Protocol]]


[[04-Conhecimentos/07-Humanidades/IA-para-Programacao/INDEX|← Voltar ao índice de IA para Programação]]
