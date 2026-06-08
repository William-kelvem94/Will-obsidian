---
title: "Playbook de Debug de Respostas de IA"
date: 2026-06-07
updated: 2026-06-07
type: playbook
status: active
tags: [conhecimento-geral, ia, debug, qualidade, rag]
related: [[Avaliacao-de-Respostas-de-IA]], [[Context-Engineering]], [[Avaliacao-de-RAG-e-Qualidade-de-Contexto]], [[Prompt-Engineering]]
summary: "Playbook para diagnosticar respostas ruins de IA e decidir se o problema está no prompt, contexto, RAG, fonte ou avaliação."
---

# Playbook de Debug de Respostas de IA

Use este playbook quando uma IA responder de forma fraca, genérica, errada, contraditória ou inútil.

## Diagnóstico rápido

| Sintoma | Causa provável | Ação |
|---|---|---|
| resposta genérica | objetivo vago | definir tarefa, formato e critério |
| resposta inventada | falta de fonte | fornecer contexto ou usar busca |
| resposta longa demais | contexto sem prioridade | pedir síntese por camadas |
| resposta ignora arquivo | recuperação ruim | checar chunks e filtros |
| resposta mistura temas | contexto contaminado | separar notas e domínios |
| resposta não decide | critérios ausentes | informar restrições e objetivo |
| resposta tecnicamente errada | modelo fraco ou dado antigo | verificar fonte e modelo |

## Passo 1 - Checar o pedido

Perguntar:

- o objetivo estava claro?
- havia formato desejado?
- havia critério de qualidade?
- havia restrição explícita?
- a tarefa tinha múltiplos objetivos misturados?

Correção:

- reescrever pedido com tarefa, contexto, saída e critérios;
- dividir tarefa grande em etapas;
- informar o que não deve ser feito.

## Passo 2 - Checar o contexto

Perguntar:

- a IA recebeu informação suficiente?
- recebeu informação demais?
- havia conteúdo antigo junto de conteúdo novo?
- havia contradição entre fontes?
- o contexto tinha ordem de prioridade?

Correção:

- enviar primeiro nota específica;
- depois MOC ou README;
- remover ruído;
- destacar decisões já tomadas;
- indicar lacunas.

## Passo 3 - Checar RAG

Quando há RAG, investigar:

- quais chunks foram recuperados;
- se a nota certa apareceu;
- se apareceu no top-k;
- se o chunk tinha título;
- se o YAML foi preservado;
- se o contexto final ficou coerente.

Correção:

- melhorar título da nota;
- adicionar resumo;
- ajustar tags;
- dividir nota grande;
- criar nota canônica;
- reindexar.

## Passo 4 - Checar fonte

Perguntar:

- existe fonte confiável no vault?
- a nota está atualizada?
- a nota é conceito, decisão, template ou log?
- a IA tratou hipótese como fato?
- havia dado sensível ou incompleto?

Correção:

- criar nota faltante;
- atualizar nota antiga;
- mover log para área correta;
- registrar decisão formal;
- adicionar data e status.

## Passo 5 - Checar modelo

Às vezes o problema não é prompt, é capacidade.

Sinais:

- erro persistente em raciocínio complexo;
- dificuldade com código grande;
- baixa qualidade em português;
- contexto longo demais para o modelo;
- incapacidade de seguir múltiplas restrições.

Correção:

- usar modelo melhor;
- reduzir contexto;
- pedir resposta em etapas;
- usar ferramenta externa;
- validar com outro modelo.

## Checklist final

- [ ] O pedido foi específico?
- [ ] O contexto estava limpo?
- [ ] A fonte correta existia?
- [ ] O RAG recuperou a fonte certa?
- [ ] A resposta citou lacunas?
- [ ] O modelo era adequado?
- [ ] A saída foi avaliada por critério claro?

## Registro de falha

Quando uma resposta falhar muito, registrar:

```md
# Falha de IA - tema

## Pedido original

## Resposta problemática

## Sintoma

## Causa provável

## Correção aplicada

## Aprendizado para o vault
```

## Resumo para IA

Quando uma resposta for ruim, não tentar apenas refazer. Diagnosticar se a falha veio do pedido, contexto, recuperação, fonte, modelo ou avaliação. Corrigir a camada certa.

## Links internos

- [[Avaliacao-de-Respostas-de-IA]]
- [[Context-Engineering]]
- [[Avaliacao-de-RAG-e-Qualidade-de-Contexto]]
- [[Prompt-Engineering]]
