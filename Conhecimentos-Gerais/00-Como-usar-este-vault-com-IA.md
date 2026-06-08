---
title: "Como usar este vault com IA"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, ia, rag, contexto, token-economy]
related: [[README]], [[01-IA/Prompt-Engineering]], [[01-IA/RAG-e-Memoria-para-Agentes]], [[01-IA/Token-Economy]]
summary: "Guia operacional para usar o vault como fonte de contexto com qualquer IA, reduzindo tokens e aumentando precisão."
---

# Como usar este vault com IA

Esta nota explica como o vault deve ser usado como fonte de contexto para assistentes de IA. O foco é reduzir repetição, economizar tokens e aumentar a qualidade das respostas.

## Regra central

Antes de uma tarefa grande, selecione notas relevantes e envie apenas o contexto necessário. A IA deve receber primeiro o material mais específico e depois os índices gerais.

## Hierarquia de contexto

1. Pedido atual do usuário.
2. Nota específica do projeto ou tema.
3. README ou MOC da pasta.
4. Conhecimento geral do vault.
5. Conhecimento externo da IA.

## Tipos de notas

| Tipo | Função | Uso ideal |
|---|---|---|
| `moc` | mapa de conteúdo | navegação e visão geral |
| `guide` | guia explicativo | regras e contexto estruturado |
| `playbook` | procedimento | execução passo a passo |
| `concept` | conceito atômico | definição e relações |
| `template` | modelo | criação de novas notas |
| `checklist` | validação | revisão antes de entrega |

## Como escolher contexto

Para uma pergunta técnica, enviar:

- nota do tema específico;
- índice da área;
- decisões relevantes;
- erros conhecidos;
- objetivo final.

Para uma análise pessoal ou estratégica, enviar:

- nota de contexto principal;
- linha do tempo relevante;
- decisões já tomadas;
- limites e preferências;
- pergunta exata.

## Chunking recomendado para RAG

- Usar cabeçalhos Markdown como fronteiras naturais.
- Preservar YAML.
- Preservar links internos.
- Evitar quebrar tabelas no meio.
- Manter blocos de código inteiros.
- Preferir chunks de 300 a 900 palavras para conteúdo conceitual.
- Preferir chunks menores para checklists e comandos.

## Padrão de resposta ideal baseada no vault

Uma resposta boa deve conter:

1. resumo curto;
2. notas ou temas usados;
3. diagnóstico ou decisão;
4. passos práticos;
5. lacunas de informação.

## Erros comuns

- Enviar contexto demais sem foco.
- Misturar notas pessoais e técnicas sem necessidade.
- Repetir definições que já existem no vault.
- Criar notas sem YAML.
- Criar notas sem links internos.
- Usar nomes vagos como `coisas.md`, `ideias.md` ou `teste.md`.

## Relações

- [[01-IA/Prompt-Engineering]] para melhorar pedidos.
- [[01-IA/RAG-e-Memoria-para-Agentes]] para memória e busca semântica.
- [[01-IA/Token-Economy]] para reduzir custo de contexto.
- [[05-Dados/Taxonomia-Metadados-e-Ontologia]] para padronizar metadados.
