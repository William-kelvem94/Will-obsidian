---
title: "Workflow Humano Agente"
description: "Padrao de colaboracao em que humano e agente dividem contexto, execucao e verificacao."
tags: [ia, agentes, workflow, colaboracao, programacao]
updated: 2026-05-08
status: active
---

# Workflow Humano Agente

Workflow humano agente e um modo de trabalho em que o humano define objetivo, criterio e limites, enquanto o agente coleta contexto, executa passos reversiveis, verifica resultados e reporta decisoes.

## Divisao de Responsabilidade

- `Humano`: prioridade, julgamento de produto, permissao para riscos e decisao final.
- `Agente`: leitura do ambiente, proposta tecnica, edicao controlada, testes e resumo.
- `Ferramentas`: execucao, busca, versionamento, validacao e recuperacao de contexto.

## Ciclo Operacional

1. Definir objetivo e limites.
2. Mapear contexto minimo necessario.
3. Fazer mudancas pequenas e explicaveis.
4. Validar com testes, leitura ou revisao.
5. Registrar o que mudou e o que ficou pendente.

## Pontos de Controle

- Antes de editar arquivos sensiveis.
- Antes de comandos destrutivos.
- Quando ha conflito entre instrucao nova e memoria antiga.
- Quando uma suposicao pode causar perda de dados.

## Saida Ideal

A saida ideal nao e apenas uma resposta. E um estado melhor do projeto: arquivos atualizados, validacao registrada, riscos claros e proximos passos pequenos.

## Relacionado

- [[Conhecimento-Geral/IA-para-Programacao/Avaliacao-de-Respostas-de-IA]]
- [[Conhecimento-Geral/IA-para-Programacao/Engenharia-de-Contexto]]
- [[skills/01-agentic-intelligence/human-agent-collaboration-loop]]

