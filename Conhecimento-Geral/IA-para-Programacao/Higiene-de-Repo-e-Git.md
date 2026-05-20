---
title: "Higiene de Repo e Git"
description: "Praticas para agentes trabalharem em repositorios sem destruir historico, sem reverter trabalho e com diffs revisaveis."
tags: [ia, git, repositorio, agentes, programacao]
updated: 2026-05-08
status: active
---

# Higiene de Repo e Git

O objetivo e manter mudancas pequenas, revisaveis e alinhadas com o projeto.

## Regras para Agentes

- ler `git status` antes de editar;
- nao apagar arquivos ou mover pastas sem pedido explicito;
- evitar refatoracoes grandes junto com fix pequeno;
- manter diffs limpos: uma intencao por commit (quando houver commit);
- nao reformatar arquivos inteiros sem necessidade;
- preservar mudancas locais do usuario.

## Checklist Rapido

1. `git status --short`
2. identificar arquivos relevantes com `rg`
3. editar apenas o necessario
4. rodar o teste mais proximo do cambio
5. registrar aprendizado quando for reutilizavel

## Relacionado

- [[Conhecimento-Geral/IA-para-Programacao/Engenharia-de-Contexto]]
- [[JARVIS/02-Operational/Playbooks/Agent-Confirmation-Protocol]]


[[Conhecimento-Geral/IA-para-Programacao/INDEX|← Voltar ao índice de IA para Programação]]
