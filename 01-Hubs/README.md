---
title: "Hubs Centrais do Vault"
date: 2026-06-07
updated: 2026-06-08
type: moc
status: active
tags: [hub, vault, organizacao, moc]
summary: "Camada central de navegacao do vault, reunindo os caminhos canonicos por dominio."
---

# Hubs Centrais do Vault

Esta pasta funciona como a camada de navegacao superior do Obsidian. Cada dominio tem um hub principal e um caminho preferido para humanos e IA.

## Dominios principais

| Domínio | Papel | Hub |
|---|---|---|
| Entrada geral | inicio do vault | [[../Bem-vindo|Neural Hub]] |
| JARVIS | IA, memoria e arquitetura | [[Hub-JARVIS]] |
| Projetos | execucao e historico | [[Hub-Projetos]] |
| Conhecimentos | conhecimento curado | [[Hub-Conhecimentos]] |
| Skills | capacidades tecnicas | [[Hub-Skills]] |
| Will Pessoal | contexto pessoal | [[Hub-Will-Pessoal]] |
| Operacoes | manutencao e governanca | [[Hub-Operacoes-do-Vault]] |
| Templates | modelos reutilizaveis | [[Hub-Templates]] |

## Regra de organizacao

Cada area do vault deve ter:

- um hub principal;
- um README ou INDEX;
- links para notas centrais;
- separacao clara entre evidencia, sintese e regra;
- metadados em YAML;
- nomes descritivos.

## O que esta camada resolve

- reduz duplicidade de navegacao;
- evita confusao entre bases legadas;
- cria uma entrada estavel para IA;
- preserva links antigos enquanto a migracao termina;
- permite reorganizacao progressiva sem perda de conteudo.

## Proximo passo

A reorganizacao fisica das pastas deve seguir [[../07-Operacoes-do-Vault/README]] e [[../07-Operacoes-do-Vault/Reestruturacao-Geral-do-Vault]].
