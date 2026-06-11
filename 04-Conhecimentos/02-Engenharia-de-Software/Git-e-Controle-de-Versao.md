---
title: "Git e Controle de Versao"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, git, versionamento, engenharia-software]
related: [[Arquitetura-Web-Moderna]], [[Docker-e-DevOps]], [[Testes-e-Qualidade-de-Software]]
summary: "Guia prático de Git para versionar projetos, organizar branches, commits, histórico e colaboração."
---

# Git e Controle de Versão

Git é um sistema de controle de versão. Ele registra mudanças, permite voltar no tempo, comparar versões e colaborar com segurança.

## Conceitos

| Conceito | Função |
|---|---|
| repositório | pasta versionada |
| commit | registro de mudança |
| branch | linha paralela de trabalho |
| merge | união de branches |
| pull | trazer mudanças remotas |
| push | enviar mudanças |
| diff | comparação entre versões |
| tag | marca de versão |

## Fluxo básico

1. Criar ou clonar repositório.
2. Criar branch para trabalho.
3. Fazer mudanças pequenas.
4. Revisar diff.
5. Criar commit claro.
6. Enviar para remoto.
7. Abrir pull request quando necessário.
8. Fazer merge após revisão.

## Boas práticas de commit

Um commit bom deve ser pequeno, coerente e ter mensagem clara.

Exemplos de mensagens:

- `Add authentication middleware`
- `Fix dashboard loading state`
- `Update Docker setup docs`
- `Refactor user service validation`

## Padrão de mensagem

```txt
tipo: descrição curta
```

Tipos comuns:

- `feat`: nova funcionalidade;
- `fix`: correção;
- `docs`: documentação;
- `refactor`: melhoria interna;
- `test`: testes;
- `chore`: manutenção.

## Erros comuns

- commit gigante com várias mudanças;
- mensagem vaga;
- trabalhar direto na main sem necessidade;
- resolver conflito sem entender;
- versionar arquivos sensíveis;
- não revisar diff antes do commit;
- misturar formatação e lógica no mesmo commit.

## Checklist antes de commitar

- [ ] O projeto ainda roda?
- [ ] O diff foi revisado?
- [ ] A mensagem explica a mudança?
- [ ] Não há arquivos sensíveis?
- [ ] A mudança é pequena o suficiente?
- [ ] Documentação foi atualizada se necessário?

## Relações

- [[Arquitetura-Web-Moderna]]
- [[Docker-e-DevOps]]
- [[Testes-e-Qualidade-de-Software]]
