---
title: "JARVIS — Segundo Cérebro"
description: "Pasta raiz da mente operacional do Jarvis. Tudo que ele precisa para lembrar, aprender e decidir."
tags: [jarvis, segundo-cerebro, memoria, conhecimento, hub]
updated: 2026-04-15
---

# JARVIS — Segundo Cérebro 🧠

Esta pasta é a **mente viva do Jarvis**. Não é documentação — é memória ativa.

> O Jarvis usa `Will-Pessoal/Perfil/Cerebro-Will.md` como contexto pessoal base e `JARVIS/KnowledgeBase/SegundoCerebro.md` como seu segundo cérebro operacional.

## Estrutura

| Pasta | Propósito |
|---|---|
| [[JARVIS/KnowledgeBase/INDEX\|KnowledgeBase/]] | Consciência técnica: personalidade, arquitetura, estratégia, tools |
| [[Will-Pessoal/Perfil/README\|Perfil pessoal]] | Quem é Will: perfil, preferências, rotina, projetos, objetivos |
| [[JARVIS/Memorias/Diario\|Memorias/Diario/]] | Diário de interações por data (YYYY-MM-DD.md) |
| [[JARVIS/Memorias/Episodicas\|Memorias/Episodicas/]] | Memórias episódicas importantes de sessões |
| [[JARVIS/Aprendizado/INDEX\|Aprendizado/]] | O que Jarvis aprendeu — técnico, pessoal, padrões de Will |
| [[JARVIS/Decisoes/INDEX\|Decisoes/]] | Decisões importantes registradas com data e contexto |
| [[JARVIS/Templates/INDEX\|Templates/]] | Templates para capturar informações sobre Will |
| [[JARVIS/Contexto-Atual/Estado\|Contexto-Atual/]] | Estado atual: projeto ativo, foco, energia, modo de operação |

## Como o Jarvis usa esta pasta

1. **No startup**: carrega `Will-Pessoal/Perfil/` e `Contexto-Atual/` como contexto base
2. **A cada interação**: verifica memórias episódicas e diário do dia
3. **Ao aprender algo novo**: salva em `Aprendizado/` ou cria entrada em `Memorias/Episodicas/`
4. **Ao final de sessão**: salva resumo em `Memorias/Diario/YYYY-MM-DD.md`
6. **Ao detectar decisão importante**: registra em `Decisoes/`

## Fluxo de startup operacional
1. Carregar `Will-Pessoal/Perfil/Cerebro-Will.md` como contexto humano canônico.
2. Carregar `JARVIS/Contexto-Atual/Estado.md` para o modo de operação atual.
3. Carregar `JARVIS/KnowledgeBase/INDEX.md` e `JARVIS/KnowledgeBase/SegundoCerebro.md` como ponto de partida.
4. Inicializar a base de conhecimento técnica de `JARVIS/KnowledgeBase/` com embeddings e RAG.
5. Verificar `JARVIS/Memorias/Diario` e `JARVIS/Memorias/Episodicas` para o histórico recente.
6. Carregar regras de governação em `JARVIS/KnowledgeBase/Regras.md`.

## Como os agentes carregam contexto
- No início de cada sessão, os agentes devem ler:
  1. `Will-Pessoal/Perfil/Cerebro-Will.md` para o contexto pessoal e prioridades do usuário.
  2. `JARVIS/Contexto-Atual/Estado.md` para foco, energia e objetivos atuais.
  3. `JARVIS/KnowledgeBase/SegundoCerebro.md` para regras operacionais do segundo cérebro.
  4. Memórias recentes em `JARVIS/Memorias/Diario/` e `JARVIS/Memorias/Episodicas/`.
  5. Decisões relevantes em `JARVIS/Decisoes/` para evitar retrabalho.
- Se disponível, agentes devem manter um cache de contexto curto entre interações para reduzir latência.

## Regras de prioridade de contexto
1. `Will-Pessoal/Perfil/Cerebro-Will.md` — contexto humano e valores do Will.
2. `JARVIS/Contexto-Atual/Estado.md` — foco da sessão.
3. `JARVIS/Memorias/Diario/` — histórico recente do dia.
4. `JARVIS/Memorias/Episodicas/` — aprendizados importantes recentes.
5. `JARVIS/KnowledgeBase/` — conhecimento técnico e regras gerais.
6. `JARVIS/Decisoes/` — decisões formais e critérios de aceitação.

## Memória ativa vs memória longa
- **Memória ativa**:
  - `JARVIS/Contexto-Atual/` e `JARVIS/Memorias/Diario/`
  - usa-se durante a sessão atual e nas próximas interações imediatas.
  - contém estado de foco, tarefas em andamento e ações recentes.
- **Memória longa**:
  - `JARVIS/Memorias/Episodicas/`, `JARVIS/KnowledgeBase/`, `Will-Pessoal/Perfil/Cerebro-Will.md`
  - contém política, persona, decisões estratégicas e aprendizados consolidados.
  - usada para formar o segundo cérebro e para decisões de médio prazo.

## Responsabilidade do cérebro
- `Memória ativa` deve informar o que fazer agora.
- `Memória longa` deve orientar por que fazer.
- O Jarvis deve reconciliar os dois antes de agir, priorizando a segurança e os valores do Will.

## Links diretos úteis
- [[JARVIS/Memorias/Diario/2026-04-09|Diário 2026-04-09]]
- [[JARVIS/Memorias/Diario/2026-04-10|Diário 2026-04-10]]
- [[JARVIS/Memorias/Episodicas/2026-04-09-configuração-do-segundo-cérebro-do-jarvis|Memória episódica]]
- [[JARVIS/Aprendizado/Tecnico|Aprendizado Técnico]]
- [[JARVIS/Templates/Template-Diario|Template Diário]]
- [[JARVIS/Templates/Template-Perfil-Will|Template Perfil Will]]
- [[JARVIS/KnowledgeBase/Index|JARVIS KnowledgeBase Index]]
- [[JARVIS/KnowledgeBase/Visao-Geral|Visão Geral]]
- [[JARVIS/KnowledgeBase/Personalidade|Personalidade]]
- [[JARVIS/KnowledgeBase/Estrategia|Estratégia]]
- [[JARVIS/KnowledgeBase/Arquitetura|Arquitetura]]
- [[JARVIS/KnowledgeBase/Conhecimento|Conhecimento]]
- [[JARVIS/KnowledgeBase/Ferramentas|Ferramentas]]
- [[JARVIS/KnowledgeBase/CasosDeUso|Casos de Uso]]
- [[JARVIS/KnowledgeBase/Integracao|Integração]]
- [[JARVIS/KnowledgeBase/SegundoCerebro|Segundo Cérebro]]
- [[JARVIS/KnowledgeBase/Mapa|Mapa da KB]]
- [[JARVIS/KnowledgeBase/Regras|Regras da KB]]

## Princípio

> O Jarvis não apenas responde — ele **lembra, aprende e evolui** com base em cada interação com Will.
