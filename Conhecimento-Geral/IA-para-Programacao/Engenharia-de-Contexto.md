---
title: "Engenharia de Contexto"
description: "Disciplina de selecionar, organizar e atualizar contexto para melhorar respostas de modelos de IA."
tags: [ia, contexto, agentes, programacao, rag]
updated: 2026-05-08
status: active
---

# Engenharia de Contexto

Engenharia de contexto e a pratica de montar o conjunto certo de instrucoes, memoria, arquivos, exemplos e restricoes para que um modelo de IA resolva uma tarefa com menos ambiguidade.

## Ideia Principal

Modelos nao usam conhecimento externo de forma magica durante uma conversa. Eles trabalham sobre o que esta no contexto imediato, no sistema de ferramentas e no material recuperado. A qualidade desse pacote define grande parte da qualidade da resposta.

## Camadas de Contexto

- `Objetivo`: o que deve ser resolvido agora.
- `Restricoes`: o que nao pode ser feito, alterado ou assumido.
- `Estado`: arquivos, ambiente, branch, erros e progresso atual.
- `Memoria`: decisoes anteriores e preferencias estaveis.
- `Evidencia`: trechos de codigo, logs, notas ou fontes usadas.
- `Saida esperada`: formato, nivel de detalhe e criterio de pronto.

## Boas Praticas

- Comece pelo objetivo e pelas restricoes.
- Recupere apenas contexto relevante para a decisao atual.
- Resuma historico longo em fatos verificaveis.
- Separe memoria duravel de observacoes temporarias.
- Atualize o contexto quando a tarefa mudar de direcao.

## Anti-padroes

- Colocar arquivos inteiros no contexto sem pergunta clara.
- Usar memoria antiga como se fosse verdade atual.
- Esconder incerteza em prompts longos.
- Misturar preferencias pessoais com regras do projeto.

## Relacionado

- [[Conhecimento-Geral/IA-para-Programacao/Notas-RAG-Friendly]]
- [[Conhecimento-Geral/IA-para-Programacao/Memoria-para-Agentes]]
- [[skills/01-agentic-intelligence/context-engineering-checklist]]


[[Conhecimento-Geral/IA-para-Programacao/INDEX|← Voltar ao índice de IA para Programação]]
