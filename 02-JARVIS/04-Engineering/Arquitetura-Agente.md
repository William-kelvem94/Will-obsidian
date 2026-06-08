---
title: "Arquitetura de Agente Cognitivo"
description: "Visão geral da integração entre servidor MCP, índice RAG e LLM externo para um assistente que lê o vault."
tags: [jarvis, engenharia, mcp, rag, jarvis-engenharia]
updated: 2026-06-08
date: 2026-04-29
---

# Arquitetura de Agente Cognitivo

## Visão Geral

A arquitetura de agente cognitivo do JARVIS conecta três componentes principais:

1. Servidor MCP
2. Índice RAG
3. LLM externo

Esses componentes trabalham juntos para entregar respostas contextualizadas a partir do vault.

## Componentes

### Servidor MCP

O servidor MCP actua como gateway entre o assistente e as ferramentas internas. Ele expõe ações como `read_vault_file` e `search_vault` e implementa políticas de segurança e orquestração.

### Índice RAG

O índice RAG armazena embeddings do conteúdo do vault e permite recuperar trechos relevantes para consultas específicas. Ele é usado para enriquecer prompts antes de enviar ao LLM.

### LLM Externo

O LLM externo processa prompts contextualizados e gera respostas. O modelo recebe tanto a instrução do usuário quanto os fragmentos relevantes retornados pelo RAG.

## Fluxo de Dados

1. Usuário faz uma pergunta ao JARVIS.
2. O servidor MCP decide se deve consultar o vault.
3. Se necessário, o MCP executa `search_vault` para retornar notas relevantes.
4. Os resultados são transformados em contexto e enviados ao LLM junto com a pergunta.
5. O LLM gera uma resposta que pode ser validada e enriquecida pelo agente antes de ser exibida.

## Papel de cada camada

- MCP: orquestração, ferramentas, segurança e lógica de execução.
- RAG: recuperação de contexto e suporte semântico para prompts.
- LLM: geração de linguagem natural e raciocínio sobre os dados fornecidos.

## Benefícios

- O agente consegue ler e interpretar o vault de forma dinâmica.
- O uso de RAG reduz alucinações ao fornecer fatos diretamente da base de conhecimento.
- A arquitetura é modular e permite trocar o LLM externo sem redesenhar o fluxo principal.

## Cenário de Uso

Quando o usuário pede "resuma a nova área de neurociência", o MCP recupera notas de `Conhecimento-Geral/Neurociencia`, compõe o prompt e envia ao LLM. A resposta é retornada com referências ao conteúdo original.

[[02-JARVIS/README|← Voltar ao Command Center]]
