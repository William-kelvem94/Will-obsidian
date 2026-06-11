---
title: "Segredos e Dados Sensiveis"
description: "Regras praticas para agentes lidarem com tokens, .env, logs e dados pessoais sem vazar ou corromper."
tags: [ia, seguranca, privacidade, agentes, programacao]
updated: 2026-05-08
status: active
---

# Segredos e Dados Sensiveis

Agentes de programacao precisam tratar segredos como material toxico: ler o minimo, nunca copiar para respostas, nunca commitar.

## Exemplos de Segredos

- tokens, chaves, cookies, credenciais;
- `.env` e variantes;
- dumps de banco, backups, logs completos;
- dados pessoais (PII).

## Regras

- nunca colar valores de `.env` em chat ou notas publicas;
- mascarar logs: mostrar apenas prefixo/sufixo quando necessario;
- preferir placeholders: `API_KEY=***`;
- se precisar editar config, pedir confirmacao antes.

## No Vault

O Obsidian e memoria longa. Entao:

- nao registrar segredos em notas;
- registrar apenas o nome da variavel e o proposito;
- guardar "como configurar" sem valores.

## Relacionado

- [[02-JARVIS/05-System/AGENT-CONTRACT]]
- [[04-Conhecimentos/07-Humanidades/Direito-Digital/GDPR-e-Privacidade]]


[[04-Conhecimentos/07-Humanidades/IA-para-Programacao/INDEX|← Voltar ao índice de IA para Programação]]
