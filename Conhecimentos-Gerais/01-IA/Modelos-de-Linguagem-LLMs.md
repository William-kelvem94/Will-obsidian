---
title: "Modelos de Linguagem LLMs"
date: 2026-06-07
updated: 2026-06-07
type: concept
status: active
tags: [conhecimento-geral, ia, llm, modelos-de-linguagem]
related: [[Prompt-Engineering]], [[Context-Engineering]], [[RAG-e-Memoria-para-Agentes]], [[IA-Local-Ollama-e-Modelos-Abertos]]
summary: "Nota canônica sobre o que são LLMs, como funcionam em alto nível, limites, usos e riscos práticos."
---

# Modelos de Linguagem LLMs

LLMs, ou Large Language Models, são modelos treinados para prever, transformar e gerar linguagem a partir de padrões aprendidos em grandes quantidades de texto e código.

## Ideia central

Um LLM não é uma mente humana nem um banco de dados. Ele é um sistema estatístico capaz de gerar respostas plausíveis com base no contexto recebido e nos padrões aprendidos durante treinamento.

## O que um LLM faz bem

- resumir textos;
- explicar conceitos;
- gerar rascunhos;
- ajudar com código;
- comparar opções;
- estruturar planos;
- transformar formatos;
- extrair informação;
- simular revisão crítica;
- criar documentação.

## O que um LLM faz mal

- garantir verdade sem fonte;
- lembrar contexto privado não enviado;
- saber fatos recentes sem busca;
- substituir especialista em área crítica;
- executar tarefas sem ferramenta;
- entender intenção ambígua com perfeição;
- manter consistência em conversas longas sem memória externa.

## Conceitos importantes

| Conceito | Explicação |
|---|---|
| token | unidade de texto processada pelo modelo |
| contexto | texto disponível na conversa ou prompt |
| janela de contexto | limite de tokens que o modelo consegue ler |
| temperatura | grau de variação/criatividade na resposta |
| grounding | ancoragem em fonte ou contexto confiável |
| alucinação | resposta plausível, mas incorreta ou inventada |
| fine-tuning | ajuste do modelo com dados adicionais |
| RAG | busca externa usada para fornecer contexto |

## Por que modelos erram

Modelos erram porque geram linguagem provável, não necessariamente verdadeira. Quando falta contexto, o modelo pode preencher lacunas com padrões plausíveis.

## Como reduzir erro

- fornecer contexto específico;
- pedir incertezas;
- usar fontes;
- usar RAG;
- dividir tarefas grandes;
- pedir verificação;
- limitar escopo;
- registrar decisões no vault.

## LLM vs RAG vs fine-tuning

| Técnica | Melhor para | Limite |
|---|---|---|
| prompt | tarefa pontual | depende da janela de contexto |
| RAG | consultar dados externos | depende da qualidade da busca |
| fine-tuning | ajustar estilo ou padrão recorrente | não é ideal para fatos dinâmicos |
| memória | manter preferências e histórico | precisa curadoria |

## Usos no vault

No Obsidian, LLMs podem ajudar a:

- resumir notas longas;
- criar MOCs;
- identificar lacunas;
- transformar reunião em ata;
- gerar planos de estudo;
- criar playbooks;
- revisar documentação;
- preparar dados para RAG.

## Riscos no vault

- misturar fato com interpretação;
- resumir demais e perder nuance;
- apagar contexto importante;
- criar links inexistentes;
- duplicar conhecimento;
- gerar confiança falsa.

## Checklist para usar LLM bem

- [ ] O objetivo está claro?
- [ ] O contexto enviado é suficiente?
- [ ] O modelo precisa de fonte atual?
- [ ] A resposta deve citar evidência?
- [ ] A tarefa envolve risco alto?
- [ ] O resultado precisa ser revisado?
- [ ] Há nota no vault que já resolve parte do problema?

## Resumo para IA

LLMs são úteis para raciocinar sobre linguagem e estruturar conhecimento, mas precisam de contexto, verificação e limites. Para tarefas do vault, devem priorizar notas canônicas, MOCs e registros atualizados antes de inferir.

## Links internos

- [[Prompt-Engineering]]
- [[Context-Engineering]]
- [[RAG-e-Memoria-para-Agentes]]
- [[IA-Local-Ollama-e-Modelos-Abertos]]
