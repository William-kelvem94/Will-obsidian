---
title: "Documentacao Tecnica, Runbooks e ADRs"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, documentacao, runbook, adr, engenharia-software]
related: [[../../02-Engenharia-de-Software/Arquitetura-Web-Moderna]], [[../../02-Engenharia-de-Software/Observabilidade-Logs-e-Monitoramento]], [[../../08-Vida-Pratica/Decisao-e-Priorizacao]], [[../../99-Templates/Template-ADR-Decisao-Arquitetural]]
summary: "Guia para criar documentação técnica útil: README, runbook, playbook, ADR, changelog e registros operacionais."
---

# Documentação Técnica, Runbooks e ADRs

Documentação boa reduz dependência de memória humana. Ela transforma conhecimento espalhado em orientação reutilizável.

## Tipos de documentação

| Tipo | Função |
|---|---|
| README | explicar o projeto e como rodar |
| runbook | operar ou recuperar sistema |
| playbook | resolver problema conhecido |
| ADR | registrar decisão arquitetural |
| changelog | registrar mudanças relevantes |
| guia de setup | preparar ambiente |
| dicionário | explicar termos e dados |

## README forte

Um README útil responde:

- o que é o projeto;
- qual problema resolve;
- como rodar;
- quais dependências existem;
- quais variáveis são necessárias;
- como testar;
- como fazer deploy;
- onde olhar logs;
- quem mantém.

## Runbook

Runbook é documentação operacional. Ele diz como agir quando algo precisa ser operado, verificado ou recuperado.

Estrutura:

- objetivo;
- pré-requisitos;
- comandos;
- validação;
- rollback;
- riscos;
- contatos;
- histórico.

## ADR

ADR significa Architecture Decision Record. Ele registra decisões importantes, contexto e consequências.

Estrutura simples:

- contexto;
- decisão;
- alternativas consideradas;
- consequências positivas;
- consequências negativas;
- data;
- status.

## Documentação para IA

Uma documentação boa para IA precisa ter:

- títulos descritivos;
- YAML;
- resumo;
- links internos;
- exemplos;
- critérios;
- ausência de ambiguidade;
- separação entre fato, decisão e hipótese.

## Erros comuns

- documentar só depois que esqueceu;
- README sem comandos reais;
- decisão importante perdida em chat;
- runbook sem rollback;
- documentação desatualizada;
- arquivo enorme sem índice;
- copiar tutorial externo sem adaptar ao projeto.

## Checklist

- [ ] O projeto tem README?
- [ ] O setup funciona seguindo o README?
- [ ] Decisões importantes têm ADR?
- [ ] Problemas recorrentes têm playbook?
- [ ] Operações críticas têm runbook?
- [ ] A documentação tem data de atualização?
- [ ] Há links para arquivos relacionados?

## Resumo para IA

Documentação técnica deve permitir continuidade. Para avaliar um projeto, verificar README, setup, decisões, runbooks, logs, rollback e atualização.

## Links internos

- [[../../02-Engenharia-de-Software/Arquitetura-Web-Moderna]]
- [[../../02-Engenharia-de-Software/Observabilidade-Logs-e-Monitoramento]]
- [[../../08-Vida-Pratica/Decisao-e-Priorizacao]]
- [[../../99-Templates/Template-ADR-Decisao-Arquitetural]]
