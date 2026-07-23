---
title: "Agent Contract - Obsidian Brain"
description: "Contrato operacional para agentes de IA usarem este vault como segundo cerebro do JARVIS e como base de contexto para programacao."
tags: [jarvis, agente, contrato, second-brain, ops, jarvis-sistema]
updated: 2026-06-13
status: active
date: 2026-06-01
---

# Agent Contract - Obsidian Brain

Este vault e uma base viva de contexto. Ele serve ao mesmo tempo como:

- segundo cerebro do JARVIS;
- memoria de trabalho do Will;
- base de conhecimento para modelos locais;
- contexto tecnico para agentes de programacao.

Por isso, agentes devem tratar o vault como uma fonte de verdade, nao como uma pasta qualquer de rascunhos.

## Fontes Canonicas

| Area | Funcao | Leitura | Escrita automatica |
|---|---|---:|---:|
| `02-JARVIS/01-Identity/` | Identidade, preferencias e persona | Sim | Nao |
| `02-JARVIS/02-Operational/` | Estado atual, decisoes e configuracao | Sim | Com cuidado |
| `02-JARVIS/03-Memory/` | Logs, snapshots e aprendizados | Sim | Sim, em subpastas corretas |
| `02-JARVIS/04-Engineering/` | Arquitetura, playbooks e wiki tecnica | Sim | Com confirmacao se alterar conhecimento canonico |
| `02-JARVIS/05-System/` | Sistema, mapas, blueprints e governanca | Sim | Com cuidado |
| `04-Conhecimentos/07-Humanidades/` | Base conceitual ampla | Sim | Com confirmacao |
| `05-Skills/` | Skills tecnicas e agenticas | Sim | Com confirmacao |
| `06-Will-Pessoal/` | Contexto pessoal do Will | Sim, quando relevante | Nao sem pedido explicito |
| `03-Projetos/` | Projetos, estudos e planos | Sim | Com cuidado |

## Regra de Escrita

Agentes podem escrever automaticamente apenas quando a tarefa pedir isso claramente ou quando o arquivo de destino for uma area operacional segura.

Areas seguras para escrita automatica:

- `02-JARVIS/03-Memory/Logs/`
- `02-JARVIS/03-Memory/Snapshots/`
- `02-JARVIS/03-Memory/Learned-Patterns/`
- `02-JARVIS/05-System/Improvements/`
- `.scripts/` somente para manutencao do vault, quando solicitado

Areas que exigem confirmacao antes de edicao:

- `02-JARVIS/01-Identity/`
- `06-Will-Pessoal/`
- hubs principais como `Bem-vindo.md`, `INDEX.md`, `03-Projetos/README.md`
- notas canonicas de arquitetura e regras
- qualquer conteudo privado, autobiografico ou sensivel

## Protocolo de Leitura Inicial

Antes de propor mudancas relevantes, carregue:

1. `Bem-vindo.md`
2. `06-Will-Pessoal/README.md`
3. `07-Operacoes-do-Vault/README.md`
4. `02-JARVIS/README.md`
5. `02-JARVIS/02-Operational/Context/Estado.md`
6. este arquivo

Para tarefas tecnicas, carregue tambem:

- `02-JARVIS/04-Engineering/Playbooks/Workflows-Praticos.md`
- `05-Skills/README.md`
- notas do projeto em `03-Projetos/`

## Contrato com PROJECT_JARVIS_5.0

O projeto `PROJECT_JARVIS_5.0` deve tratar este vault como a fonte viva de conhecimento.

Diretrizes:

- `JARVIS_VAULT_ROOT` deve apontar para a raiz deste vault.
- `JARVIS_KB_PATH` deve apontar para uma subarvore focada, normalmente `02-JARVIS/` ou uma KB dedicada do projeto.
- `data/kb_local/` no projeto deve ser considerado seed/cache/fallback, nao a fonte viva principal.
- Escritas vindas do app devem ir para areas seguras de memoria, nao para hubs canonicos.
- Se o app gerar sugestoes, elas devem cair em `02-JARVIS/05-System/Improvements/` ou em um indice de revisao.

## Padrao de Nota Nova

Notas novas importantes devem conter:

```yaml
---
title: "..."
description: "Resumo claro em 1-2 linhas"
tags: [jarvis]
updated: YYYY-MM-DD
status: draft
---
```

Tambem devem ter ao menos um link para hub, projeto, skill ou conceito relacionado.

## Politica de Memoria

Use esta classificacao:

- `Logs`: eventos diarios e historico bruto;
- `Snapshots`: marcos importantes que resumem uma sessao;
- `Learned-Patterns`: aprendizados reutilizaveis;
- `Decisions`: decisoes tecnicas ou pessoais com motivo;
- `Improvements`: sugestoes pendentes para revisao humana.

## Regra Final

Quando houver duvida entre reorganizar e preservar contexto, preserve. Este vault existe para manter continuidade entre humanos, JARVIS e agentes de programacao.


[[02-JARVIS/README|← Voltar ao Command Center]]
