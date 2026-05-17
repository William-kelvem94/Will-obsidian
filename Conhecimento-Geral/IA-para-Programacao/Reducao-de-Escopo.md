---
title: "Reducao de Escopo"
description: "Tecnicas para reduzir o escopo de uma tarefa com IA e evitar refatoracoes grandes e diffs ruidosos."
tags: [ia, escopo, programacao, agentes, qualidade]
updated: 2026-05-08
status: active
---

# Reducao de Escopo

Agentes de IA tendem a expandir escopo: refatorar, renomear e reorganizar para \"ficar bonito\". Em repos reais, isso aumenta risco e dificulta review.

## Objetivo

Chegar no menor conjunto de mudancas que resolve o problema e e verificavel.

## Regras Praticas

- uma intencao por mudanca: bugfix, feature, docs ou cleanup (nao misturar).
- comece por leitura, nao por escrita.
- edite perto do problema (arquivo, funcao, boundary).
- preserve convencoes do repo.
- valide com o teste mais proximo.

## Sinais de Escopo Grande Demais

- muitos arquivos tocados sem necessidade;
- mudanca de estilo/formatacao em massa;
- abstracao nova para resolver um caso pequeno;
- mexe em build/deps para \"aproveitar\".

## Como Pedir ao Agente

- \"nao refatore; so conserte o bug\"
- \"limite a N arquivos\"
- \"nao renomeie nada\"
- \"proponha 2 opcoes pequenas e escolha 1\"

## Relacionado

- [[Conhecimento-Geral/IA-para-Programacao/Higiene-de-Repo-e-Git]]
- [[Conhecimento-Geral/IA-para-Programacao/Debug-com-Agentes]]

