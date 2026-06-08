---
title: "Hubs Centrais do Vault"
date: 2026-06-07
updated: 2026-06-07
type: moc
status: active
tags: [hub, vault, organizacao, moc]
summary: "Camada central de navegação do vault, reunindo os principais domínios sem mover conteúdo existente."
---

# Hubs Centrais do Vault

Esta pasta funciona como a camada de navegação superior do Obsidian. Ela não substitui o conteúdo existente; ela organiza os caminhos principais para reduzir confusão e facilitar uso por humanos e IA.

## Domínios principais

| Domínio | Função | Hub |
|---|---|---|
| Entrada geral | início do vault | [[../Bem-vindo|Neural Hub]] |
| JARVIS | IA, agentes e memória | [[Hub-JARVIS]] |
| Projetos | execução e portfólio | [[Hub-Projetos]] |
| Conhecimentos | estudos e base para IA | [[Hub-Conhecimentos]] |
| Skills | habilidades e capacidades técnicas | [[Hub-Skills]] |
| Will Pessoal | perfil, vida e contexto pessoal | [[Hub-Will-Pessoal]] |
| Operações | manutenção do vault | [[Hub-Operacoes-do-Vault]] |
| Templates | modelos reutilizáveis | [[Hub-Templates]] |

## Regra de organização

Cada área do vault deve ter:

- um hub principal;
- um README ou INDEX;
- links para notas centrais;
- separação clara entre conhecimento, projeto, memória e operação;
- metadados em YAML;
- nomes descritivos.

## O que esta camada resolve

- reduz duplicidade de navegação;
- evita confusão entre `Conhecimentos-Gerais` e `Conhecimento-Geral`;
- cria uma entrada estável para IA;
- preserva links antigos enquanto a migração estrutural é planejada;
- permite reorganização progressiva sem perda de conteúdo.

## Próximo passo

A reorganização física das pastas deve seguir [[../07-Operacoes-do-Vault/Reestruturacao-Geral-do-Vault]].
