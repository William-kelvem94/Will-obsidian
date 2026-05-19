---
title: "Avaliacao de Respostas de IA"
description: "Criterios praticos para julgar se uma resposta de IA e correta, util e segura para uso."
tags: [ia, avaliacao, qualidade, respostas, agentes]
updated: 2026-05-08
status: active
---

# Avaliacao de Respostas de IA

Avaliacao de respostas de IA e o processo de comparar a saida do modelo com a tarefa real, as evidencias disponiveis e o impacto de uso. Uma boa avaliacao olha para utilidade, fidelidade, limites e custo de erro.

## Criterios Centrais

- `Correcao`: a resposta bate com os fatos, o codigo ou as regras do dominio.
- `Completude`: cobre as partes essenciais do pedido sem inventar escopo.
- `Aderencia`: respeita formato, idioma, restricoes e contexto do usuario.
- `Rastreabilidade`: deixa claro de onde vieram fatos, inferencias e incertezas.
- `Acionabilidade`: entrega passos, exemplos ou decisoes que podem ser usados.
- `Seguranca`: evita expor dados sensiveis, comandos destrutivos ou conselhos indevidos.

## Sinais de Risco

- Afirma certeza onde ha contexto insuficiente.
- Ignora uma restricao explicita do usuario.
- Mistura fatos verificados com suposicoes sem marcar a diferenca.
- Produz uma resposta bonita, mas impossivel de executar.
- Explica demais e nao resolve a tarefa principal.

## Rubrica Simples

Use uma escala de 0 a 2 para cada criterio:

- `0`: falha ou ausente.
- `1`: parcialmente atendido.
- `2`: atendido com clareza.

Uma resposta pronta para uso deve ter pontuacao alta em `correcao`, `aderencia` e `seguranca`. Em tarefas de programacao, `acionabilidade` tambem deve ser alta porque o resultado precisa virar mudanca concreta.

## Perguntas de Revisao

- O modelo respondeu ao pedido ou apenas falou sobre o tema?
- Quais partes dependem de informacao nao fornecida?
- O usuario conseguiria executar o proximo passo sem perguntar de novo?
- A resposta preserva dados, arquivos e decisoes sensiveis?

## Relacionado

- [[Conhecimento-Geral/IA-para-Programacao/Engenharia-de-Contexto]]
- [[Conhecimento-Geral/IA-para-Programacao/Workflow-Humano-Agente]]
- [[skills/01-agentic-intelligence/response-evaluation-rubric]]

