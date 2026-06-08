---
title: "Observabilidade, Logs e Monitoramento"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, observabilidade, logs, monitoramento, devops]
related: [[Docker-e-DevOps]], [[Linux-Terminal-e-Shell]], [[Sistemas-Distribuidos-e-Escalabilidade]], [[Testes-e-Qualidade-de-Software]]
summary: "Guia de observabilidade para entender sistemas em execução usando logs, métricas, tracing, alertas e diagnóstico."
---

# Observabilidade, Logs e Monitoramento

Observabilidade é a capacidade de entender o estado interno de um sistema a partir dos sinais que ele produz. Sem observabilidade, produção vira caixa-preta.

## Três pilares

| Pilar | O que mostra |
|---|---|
| logs | eventos e mensagens |
| métricas | números ao longo do tempo |
| traces | caminho de uma requisição |

## Logs bons

Um log bom explica o que aconteceu, onde, quando e com qual contexto mínimo.

Deve incluir:

- timestamp;
- nível;
- serviço;
- operação;
- identificador relevante;
- mensagem clara;
- erro quando existir.

## Níveis de log

| Nível | Uso |
|---|---|
| debug | detalhe para desenvolvimento |
| info | evento normal importante |
| warn | algo estranho, mas recuperável |
| error | falha que precisa atenção |
| fatal | falha crítica |

## Métricas úteis

- tempo de resposta;
- taxa de erro;
- uso de CPU;
- uso de memória;
- requisições por minuto;
- tamanho de fila;
- tempo de processamento;
- disponibilidade.

## Alertas

Alerta bom precisa ser acionável. Se ninguém sabe o que fazer quando toca, o alerta é ruído.

## Erros comuns

- logar pouco;
- logar demais;
- expor dados sensíveis em log;
- não ter correlação entre eventos;
- monitorar métrica que não gera ação;
- ignorar logs até dar problema;
- não registrar contexto do erro.

## Checklist

- [ ] Erros têm stack ou detalhe suficiente?
- [ ] Logs não expõem senha, token ou dado sensível?
- [ ] Há métricas de erro e latência?
- [ ] Existe forma de saber se serviço está vivo?
- [ ] Alertas são acionáveis?
- [ ] Logs incluem identificador de requisição quando necessário?

## Resumo para IA

Ao diagnosticar sistema, procurar logs, métricas e traces antes de supor causa. Observabilidade boa reduz tempo de debugging e torna sistemas distribuídos menos opacos.

## Links internos

- [[Docker-e-DevOps]]
- [[Linux-Terminal-e-Shell]]
- [[Sistemas-Distribuidos-e-Escalabilidade]]
- [[Testes-e-Qualidade-de-Software]]
