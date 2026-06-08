---
title: "Padrão de Commits em PT-BR"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [documentacao, git, commits, ptbr, padrao]
related: [[Documentacao-Tecnica-Runbooks-e-ADRs]], [[../../02-Engenharia-de-Software/Git-e-Controle-de-Versao]]
summary: "Define o padrão obrigatório de mensagens de commit em português do Brasil para manter histórico claro, rastreável e útil."
---

# Padrão de Commits em PT-BR

Todos os commits futuros devem ser escritos em **português do Brasil**, com mensagem clara, objetiva e detalhada o suficiente para explicar a mudança sem precisar abrir o diff.

## Regra principal

A mensagem do commit deve explicar:

1. o que foi alterado;
2. por que foi alterado;
3. onde a alteração impacta;
4. se houve remoção, criação, atualização ou reorganização;
5. se não houve perda de conteúdo.

## Formato recomendado

```txt
tipo: resumo curto em PT-BR

Descrição detalhada em uma ou mais linhas, explicando contexto,
escopo da mudança e impacto esperado.
```

## Tipos úteis

| Tipo | Uso |
|---|---|
| `docs` | documentação, notas e guias |
| `feat` | nova funcionalidade ou nova área |
| `fix` | correção de problema |
| `refactor` | reorganização sem mudar comportamento |
| `chore` | manutenção |
| `remove` | remoção intencional |
| `restore` | restauração de conteúdo |

## Exemplos bons

```txt
docs: adiciona guia de CI/CD como conhecimento geral

Cria uma nota explicando CI/CD apenas como conteúdo de estudo,
sem configurar workflow ativo no projeto.
```

```txt
remove: remove workflow ativo de CI do PROJECT_JARVIS

Remove o arquivo .github/workflows/ci.yml para impedir execuções
automáticas e notificações indesejadas do GitHub Actions.
```

## Evitar

- mensagens em inglês;
- mensagens vagas como `update`, `fix`, `changes`;
- commits sem contexto;
- misturar alterações sem relação;
- remover conteúdo sem explicar motivo.

## Observação

Esta regra vale para alterações feitas por IA ou por humanos neste ecossistema de repositórios.
