---
title: "IA Local, Ollama e Modelos Abertos"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, ia-local, ollama, modelos-abertos, llm]
related: [[Modelos-de-Linguagem-LLMs]], [[RAG-e-Memoria-para-Agentes]], [[Context-Engineering]], [[../02-Engenharia-de-Software/Docker-e-DevOps]]
summary: "Guia prático para entender IA local, Ollama, modelos abertos, privacidade, hardware, limitações e integração com vaults."
---

# IA Local, Ollama e Modelos Abertos

IA local é a execução de modelos no próprio computador ou servidor, sem depender obrigatoriamente de APIs externas. Isso pode trazer mais privacidade, controle e previsibilidade de custo.

## Quando faz sentido

- dados sensíveis;
- testes offline;
- automações internas;
- custo previsível;
- integração com arquivos locais;
- estudos de IA;
- protótipos com RAG local;
- controle de versão de modelos.

## Quando não faz sentido

- máquina fraca para o modelo desejado;
- necessidade de altíssima qualidade geral;
- baixa tolerância a configuração técnica;
- tarefa exige dados atuais da web;
- equipe precisa de SLA forte sem infraestrutura.

## Componentes

| Componente | Função |
|---|---|
| runtime | executa o modelo |
| modelo | arquivo com pesos e arquitetura |
| quantização | reduz tamanho e consumo |
| prompt | instrução da tarefa |
| contexto | dados usados na resposta |
| RAG | consulta arquivos externos |
| API local | permite integração com apps |

## Ollama

Ollama facilita baixar e executar modelos localmente. Ele pode ser usado como base para assistentes, automações e projetos RAG.

## Critérios para escolher modelo

| Critério | Pergunta |
|---|---|
| tamanho | cabe na RAM/VRAM? |
| idioma | responde bem em português? |
| código | entende programação? |
| contexto | aceita contexto suficiente? |
| velocidade | responde em tempo útil? |
| licença | permite o uso desejado? |
| qualidade | resolve a tarefa real? |

## Hardware

Modelos locais dependem de:

- RAM;
- VRAM;
- CPU;
- GPU;
- velocidade de armazenamento;
- refrigeração;
- tamanho do contexto.

## Integração com Obsidian

Fluxo possível:

1. Obsidian guarda notas em Markdown.
2. Script lê notas relevantes.
3. Chunks são indexados.
4. Modelo local recebe contexto.
5. Resposta cita arquivos internos.
6. Nova informação é salva no vault.

## Riscos

- achar que local significa automaticamente seguro;
- usar modelo pequeno para tarefa complexa;
- não versionar prompts;
- indexar dados sensíveis sem controle;
- misturar memória bruta e conhecimento curado;
- não medir qualidade das respostas.

## Checklist

- [ ] O modelo cabe no hardware?
- [ ] A licença permite o uso?
- [ ] O idioma é adequado?
- [ ] O contexto é suficiente?
- [ ] Dados sensíveis estão separados?
- [ ] Existe avaliação de qualidade?
- [ ] O vault tem notas bem estruturadas?

## Resumo para IA

IA local dá controle e privacidade, mas exige curadoria, avaliação e infraestrutura. Para o Will, faz sentido como base do JARVIS, especialmente junto de Obsidian, RAG e Docker.

## Links internos

- [[Modelos-de-Linguagem-LLMs]]
- [[RAG-e-Memoria-para-Agentes]]
- [[Context-Engineering]]
- [[../02-Engenharia-de-Software/Docker-e-DevOps]]
