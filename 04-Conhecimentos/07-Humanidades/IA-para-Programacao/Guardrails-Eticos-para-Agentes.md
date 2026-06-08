---
title: "Guardrails Eticos para Agentes"
description: "Regras praticas para limitar automacao e reduzir danos quando agentes operam em repositorios e dados reais."
tags: [ia, etica, guardrails, agentes, programacao]
updated: 2026-05-08
status: active
---

# Guardrails Eticos para Agentes

Em programacao, um agente pode causar dano sem \"intencao\": apagar dados, vazar segredos, introduzir backdoors ou automatizar tarefas sem consentimento. Guardrails sao limites operacionais simples para reduzir risco.

## Principios Praticos

- minimo privilegio: agir com o menor poder necessario.
- minimizacao: ler e registrar o minimo de dados.
- explicabilidade: deixar claro o que foi feito e por que.
- reversibilidade: preferir mudancas que podem ser desfeitas.
- consentimento: pedir confirmacao antes de qualquer acao sensivel.

## Areas que exigem confirmacao

- deletar/mover arquivos, migrations, alteracoes de dependencias;
- auth, pagamentos, dados pessoais, seguranca;
- automacao que toca o SO, navegador, rede, integrações.

## Registro de Memoria

No Obsidian:

- registrar decisoes e regras, nao segredos;
- separar sugestoes pendentes de conhecimento confirmado;
- preferir notas atomicas e indexaveis.

## Relacionado

- [[04-Conhecimentos/07-Humanidades/IA-para-Programacao/Segredos-e-Dados-Sensiveis]]
- [[04-Conhecimentos/07-Humanidades/Etica/Etica-de-IA-e-Alinhamento]]
- [[02-JARVIS/05-System/AGENT-CONTRACT]]


[[04-Conhecimentos/07-Humanidades/IA-para-Programacao/INDEX|← Voltar ao índice de IA para Programação]]
