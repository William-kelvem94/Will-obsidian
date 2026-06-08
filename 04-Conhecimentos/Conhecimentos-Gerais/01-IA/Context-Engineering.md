---
title: "Context Engineering"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, ia, context-engineering, prompts, rag]
related: [[Modelos-de-Linguagem-LLMs]], [[Prompt-Engineering]], [[Token-Economy]], [[RAG-e-Memoria-para-Agentes]]
summary: "Guia sobre engenharia de contexto: como selecionar, comprimir, ordenar e validar informações para melhorar respostas de IA."
---

# Context Engineering

Context engineering é a disciplina de construir o contexto certo para uma IA. Prompt engineering formula o pedido. Context engineering decide quais informações entram, em qual ordem, com qual prioridade e com qual nível de detalhe.

## Por que importa

Uma IA pode falhar mesmo com um bom prompt se receber contexto ruim. Contexto ruim pode ser incompleto, antigo, contraditório, longo demais, genérico ou sem prioridade.

## Elementos de contexto

| Elemento | Função |
|---|---|
| objetivo | define resultado esperado |
| estado atual | mostra onde o trabalho está |
| restrições | limita escolhas |
| decisões anteriores | evita reabrir debate |
| dados | fundamenta resposta |
| exemplos | calibram estilo e formato |
| critérios | definem qualidade |
| lacunas | mostram o que não se sabe |

## Ordem recomendada

1. Tarefa atual.
2. Objetivo final.
3. Restrições.
4. Estado atual.
5. Dados relevantes.
6. Decisões já tomadas.
7. Formato desejado.
8. Critérios de qualidade.

## Contexto em camadas

| Camada | Uso |
|---|---|
| 1 linha | intenção imediata |
| resumo curto | visão geral |
| nota canônica | conceito principal |
| notas relacionadas | aprofundamento |
| logs | evidência histórica |
| anexos | detalhe bruto |

## Compressão de contexto

Compressão não é apagar. É reduzir sem perder decisão, risco e significado.

Preservar:

- decisões;
- datas;
- nomes;
- restrições;
- exceções;
- riscos;
- números importantes;
- links para fonte completa.

Remover:

- repetição;
- floreio;
- exemplos duplicados;
- conversa lateral;
- ruído sem valor.

## Erros comuns

- mandar contexto demais;
- mandar contexto sem objetivo;
- esconder restrição importante;
- misturar versões antigas e novas;
- não dizer o que mudou;
- deixar a IA inferir prioridade;
- usar logs crus como se fossem conhecimento curado.

## Contexto para o JARVIS

Para um agente como JARVIS, contexto deve ser separado em:

- identidade;
- preferências;
- estado atual;
- projeto ativo;
- conhecimento estável;
- memória episódica;
- ferramentas disponíveis;
- limites de ação.

## Checklist

- [ ] O objetivo está no começo?
- [ ] O contexto é atual?
- [ ] Há notas canônicas relevantes?
- [ ] Dados sensíveis foram removidos quando necessário?
- [ ] Decisões antigas foram preservadas?
- [ ] O modelo sabe o formato de saída?
- [ ] Existe critério para avaliar a resposta?

## Resumo para IA

Context engineering é a arte de montar o contexto certo. Priorize informação específica, atual, estruturada e com hierarquia clara. Contexto demais sem curadoria pode piorar a resposta.

## Links internos

- [[Modelos-de-Linguagem-LLMs]]
- [[Prompt-Engineering]]
- [[Token-Economy]]
- [[RAG-e-Memoria-para-Agentes]]
