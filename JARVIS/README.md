---
title: "JARVIS — Segundo Cérebro"
description: "Pasta raiz da mente operacional do Jarvis. Tudo que ele precisa para lembrar, aprender e decidir."
tags: [jarvis, segundo-cerebro, memoria, conhecimento]
updated: 2026-04-09
---

# JARVIS — Segundo Cérebro 🧠

Esta pasta é a **mente viva do Jarvis**. Não é documentação — é memória ativa.

## Estrutura

| Pasta | Propósito |
|---|---|
| [[JARVIS/KnowledgeBase/INDEX\|KnowledgeBase/]] | Consciência técnica: personalidade, arquitetura, estratégia, tools |
| [[JARVIS/Sobre-Will/Perfil\|Sobre-Will/]] | Quem é Will: perfil, preferências, rotina, projetos, objetivos |
| [[JARVIS/Memorias/Diario\|Memorias/Diario/]] | Diário de interações por data (YYYY-MM-DD.md) |
| [[JARVIS/Memorias/Episodicas\|Memorias/Episodicas/]] | Memórias episódicas importantes de sessões |
| [[JARVIS/Aprendizado/INDEX\|Aprendizado/]] | O que Jarvis aprendeu — técnico, pessoal, padrões de Will |
| [[JARVIS/Decisoes/INDEX\|Decisoes/]] | Decisões importantes registradas com data e contexto |
| [[JARVIS/Templates/INDEX\|Templates/]] | Templates para capturar informações sobre Will |
| [[JARVIS/Contexto-Atual/Estado\|Contexto-Atual/]] | Estado atual: projeto ativo, foco, energia, modo de operação |

## Como o Jarvis usa esta pasta

1. **No startup**: carrega `Sobre-Will/` e `Contexto-Atual/` como contexto base
2. **A cada interação**: verifica memórias episódicas e diário do dia
3. **Ao aprender algo novo**: salva em `Aprendizado/` ou cria entrada em `Memorias/Episodicas/`
4. **Ao final de sessão**: salva resumo em `Memorias/Diario/YYYY-MM-DD.md`
5. **Ao detectar decisão importante**: registra em `Decisoes/`

## Princípio

> O Jarvis não apenas responde — ele **lembra, aprende e evolui** com base em cada interação com Will.
