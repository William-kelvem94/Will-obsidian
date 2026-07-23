---
title: "Curadoria de Memória e Recuperação em Camadas"
updated: 2026-07-10
type: architecture
status: active
tags: [memoria, contexto, recall, jarvis, agentes]
indexavel: true
uso_ia: livre
related: [[RAG-e-Memoria-para-Agentes]], [[Context-Engineering]], [[../../02-JARVIS/TOKEN-COMPRESSION]]
---

# Memória em camadas

| Camada | Conteúdo | Recuperação |
|---|---|---|
| 0 | estado da sessão | sempre que necessário |
| 1 | perfil, objetivos e restrições | início da tarefa |
| 2 | decisões, preferências e fatos estáveis | busca semântica + links |
| 3 | episódios, logs e histórico | sob demanda |
| 4 | fontes brutas e arquivo | investigação explícita |

## Operações

`write` captura; `consolidate` transforma episódios em fatos; `link` conecta contexto; `decay` reduz prioridade; `supersede` preserva histórico e aponta para o atual; `forget` remove apenas conforme política; `recall` recupera pelo menor conjunto suficiente.

## Promoção

Promover uma memória quando ela é reutilizável, validada, relevante para objetivos e segura para o nível de privacidade. Um fato contraditório não deve substituir silenciosamente o anterior.

## Escore operacional

`prioridade = relevância × confiança × recência × reutilização × segurança`.

Privacidade é guardrail, não multiplicador: conteúdo proibido não é recuperado mesmo que tenha alta relevância.

## Fontes

- [MemGPT](https://arxiv.org/abs/2310.08560)
- [A-Mem](https://arxiv.org/html/2502.12110v9)
