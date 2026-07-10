---
title: "Engenharia de Conhecimento para um Segundo Cérebro de IA"
date: 2026-07-10
updated: 2026-07-10
type: guide
status: active
tags: [engenharia-de-conhecimento, segundo-cerebro, ontologia, rag, memoria, pesquisa]
classe_privacidade: publico-tecnico
indexavel: true
uso_ia: livre
fonte_canonica: true
related: [[Mapa-Mestre-de-Conhecimentos-Gerais]], [[Ontologia-de-Conhecimento-para-IA]], [[../01-IA-e-Agentes/RAG-e-Memoria-para-Agentes]]
---

# Engenharia de conhecimento para o WILL-OBSIDIAN

## Tese

Um segundo cérebro útil não é um depósito de textos: é um sistema de decisões sobre captura, estrutura, evidência, ligação, recuperação e revisão. O objetivo é maximizar conhecimento recuperável por unidade de armazenamento e por unidade de contexto.

## Pipeline canônico

`captura → classificação → extração → síntese → ligação → validação → indexação → recuperação → revisão`

Cada nota deve responder: o que é, de onde veio, qual confiança merece, com o que se relaciona, quando deve ser revisada e como pode ser usada por uma IA.

## Tipos de artefato

| Artefato | Função | Destino preferencial |
|---|---|---|
| Fonte | preservar origem e contexto | `wiki/sources` ou `08-Dados-Brutos` |
| Conceito | definir uma ideia reutilizável | `wiki/concepts` ou domínio |
| Entidade | representar pessoa, obra, projeto ou sistema | `wiki/entities` |
| Síntese | condensar várias fontes | `wiki/summaries` |
| Análise | comparar, avaliar ou decidir | `wiki/analysis` |
| Playbook | orientar execução | `05-Skills` ou `07-Operacoes` |
| Memória | preservar contexto operacional | `02-JARVIS` |

## Contrato mínimo de uma nota

1. Título específico e atômico.
2. Afirmação principal em uma frase.
3. Definições e limites do conceito.
4. Evidências ou fontes rastreáveis.
5. Links para notas relacionadas.
6. Incertezas, conflitos e lacunas.
7. Aplicação concreta ao vault.

## Qualidade

Avaliar separadamente precisão, completude, atualidade, rastreabilidade, clareza, recuperabilidade e segurança. Uma nota pode ser bem escrita e ainda assim ter evidência fraca.

## Anti-padrões

Evitar notas gigantes sem unidade semântica, cópia sem síntese, links sem contexto, fatos sem fonte, tags excessivas, mistura de dado privado com conhecimento público e atualização sem registro do que mudou.

## Exercícios

- Converter um artigo em uma fonte, três conceitos, duas entidades e uma síntese.
- Encontrar uma afirmação sem evidência e classificá-la como hipótese.
- Recuperar uma resposta usando apenas links e metadados, sem ler o vault inteiro.

## Fontes

- [RAG survey 2025](https://arxiv.org/abs/2506.00054)
- [RAG survey 2023](https://arxiv.org/abs/2312.10997)
