---
title: "Prompts para Codigo"
description: "Modelos de prompt para tarefas de codigo com foco em contexto, validacao e seguranca."
tags: [ia, prompts, programacao, agentes]
updated: 2026-05-08
status: active
---

# Prompts para Codigo

Prompts bons descrevem objetivo, estado, restricoes e validacao. Eles reduzem churn e evitam que o agente invente coisas.

## Bugfix

Inclua:

- erro/sintoma + como reproduzir;
- arquivos candidatos (ou permissao para buscar);
- restricoes (nao refatorar, nao renomear, nao mudar deps);
- como validar (teste, comando, comportamento).

Exemplo:

\"Conserte o bug X. Reproduz assim: .... Nao refatore. Limite a ate 3 arquivos. Adicione/ajuste teste para falhar antes e passar depois. Mostre como validar.\"

## Feature Pequena

Inclua:

- definicao de pronto (DoD);
- compatibilidade e contratos;
- rollback/feature flag se precisar.

Exemplo:

\"Implemente a feature Y com DoD: ... Preserve API atual. Se precisar, use feature flag. Inclua validacao.\"

## Docs e Mapas

Inclua:

- publico alvo (humano, agente, ambos);
- onde escrever (pasta/arquivo).

Exemplo:

\"Crie um Codebase Map em `JARVIS/04-Engineering/Codebase-Maps/` para o projeto Z. Nao copie segredos. Liste entrypoints, comandos e riscos.\"

## Relacionado

- [[Conhecimento-Geral/IA-para-Programacao/Engenharia-de-Contexto]]
- [[Conhecimento-Geral/IA-para-Programacao/Segredos-e-Dados-Sensiveis]]


[[Conhecimento-Geral/IA-para-Programacao/INDEX|← Voltar ao índice de IA para Programação]]
