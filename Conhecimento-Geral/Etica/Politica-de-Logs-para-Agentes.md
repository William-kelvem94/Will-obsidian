---
title: "Politica de Logs para Agentes"
area: "Conhecimento-Geral/Etica"
tags: ["ethics","logging","privacy","agents","governance"]
created: "2026-05-08"
status: "draft"
---

# Politica de Logs para Agentes

Logs sao necessarios para operar e depurar, mas tambem sao um vetor de vazamento. Uma politica de logs para agentes precisa equilibrar: observabilidade, privacidade, custo e risco.

## Objetivos

- Permitir reproducao de problemas sem expor dados sensiveis.
- Permitir auditoria de decisoes e acoes.
- Definir retencao e escopo (onde fica, por quanto tempo, quem acessa).

## Niveis de log (proposta simples)

1. INFO: eventos de alto nivel (inicio/fim, tarefa, resultado).
2. DEBUG (sanitizado): sinais tecnicos (erros, stacks), sem payloads.
3. TRACE (temporario): somente em incidente, com tempo limitado, e sempre sanitizado.

## Regras de sanitizacao (must)

- Nunca logar: tokens, chaves, cookies, headers de auth, documentos pessoais.
- Redigir PII: email, cpf, telefone, enderecos.
- "Shape only": quando preciso, logar o formato (campos) e nao o conteudo.

## Retencao (heuristica)

- DEBUG: dias a semanas
- INFO: semanas a meses (depende do projeto)
- TRACE: horas a poucos dias (incidente)

## Checklist antes de aumentar verbosidade

- Qual pergunta o log vai responder?
- O log pode conter PII ou segredos?
- Existe alternativa: metricas, contagens, amostragem?
- Quem tera acesso a esse log?
- Quando e como sera apagado?

## Relacionado

- [[Privacidade-by-Default-para-Agentes]]
- [[Auditoria-de-Agentes-e-Evidencias]]
- [[Minimizacao-de-Dados-para-RAG-e-Agentes]]


[[Conhecimento-Geral/Etica/INDEX|← Voltar ao índice de Ética]]
