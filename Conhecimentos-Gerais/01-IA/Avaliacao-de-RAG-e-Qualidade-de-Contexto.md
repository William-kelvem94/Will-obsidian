---
title: "Avaliacao de RAG e Qualidade de Contexto"
date: 2026-06-07
updated: 2026-06-07
type: checklist
status: active
tags: [conhecimento-geral, ia, rag, avaliacao, contexto]
related: [[RAG-e-Memoria-para-Agentes]], [[Embeddings-e-Busca-Semantica]], [[Context-Engineering]], [[Avaliacao-de-Respostas-de-IA]]
summary: "Checklist e critérios para avaliar se um sistema RAG recupera contexto correto, suficiente e seguro."
---

# Avaliação de RAG e Qualidade de Contexto

Um sistema RAG só é bom quando recupera o contexto certo e o modelo usa esse contexto corretamente. Busca vetorial forte com contexto ruim ainda produz resposta ruim.

## O que avaliar

| Camada | Pergunta |
|---|---|
| fonte | os documentos são confiáveis? |
| chunking | os trechos preservam sentido? |
| recuperação | os resultados são relevantes? |
| montagem | o contexto final está bem ordenado? |
| geração | o LLM usou o contexto sem inventar? |
| resposta | a saída ajuda o usuário? |

## Métricas práticas

| Métrica | Descrição |
|---|---|
| precisão da recuperação | resultados retornados são relevantes |
| cobertura | contexto inclui tudo que era necessário |
| atualidade | documentos estão atualizados |
| fidelidade | resposta respeita as fontes |
| rastreabilidade | dá para saber de onde veio a informação |
| economia | contexto não é maior que o necessário |

## Testes manuais

Criar perguntas de avaliação:

- pergunta com resposta em uma nota específica;
- pergunta que exige combinar duas notas;
- pergunta que não tem resposta no vault;
- pergunta com termo parecido, mas tema diferente;
- pergunta sobre dado antigo e dado novo;
- pergunta que exige dizer "não sei".

## Sinais de RAG bom

- retorna nota específica antes da genérica;
- preserva título e caminho do arquivo;
- não mistura notas incompatíveis;
- reconhece lacuna;
- cita ou menciona fontes internas;
- evita contexto excessivo;
- responde com base no trecho recuperado.

## Sinais de RAG ruim

- retorna sempre notas genéricas;
- ignora notas recentes;
- usa chunk sem título;
- perde contexto de tabela;
- mistura projetos diferentes;
- responde algo que não estava nos documentos;
- não sabe dizer de onde tirou a resposta.

## Checklist de qualidade

- [ ] O chunk tem título compreensível?
- [ ] O caminho do arquivo foi preservado?
- [ ] O YAML foi indexado?
- [ ] Links internos foram preservados?
- [ ] Notas duplicadas foram evitadas?
- [ ] Conteúdo sensível está separado?
- [ ] Há teste para pergunta sem resposta?
- [ ] Há avaliação humana periódica?

## Processo de melhoria

1. Identificar perguntas que falharam.
2. Ver quais chunks foram recuperados.
3. Ver se a nota certa existe.
4. Melhorar título, resumo ou tags.
5. Ajustar chunking.
6. Reindexar.
7. Testar novamente.

## Resumo para IA

Avaliar RAG exige verificar a cadeia inteira: documento, chunk, busca, contexto montado e resposta final. O objetivo é recuperar menos contexto, mas mais relevante.

## Links internos

- [[RAG-e-Memoria-para-Agentes]]
- [[Embeddings-e-Busca-Semantica]]
- [[Context-Engineering]]
- [[Avaliacao-de-Respostas-de-IA]]
