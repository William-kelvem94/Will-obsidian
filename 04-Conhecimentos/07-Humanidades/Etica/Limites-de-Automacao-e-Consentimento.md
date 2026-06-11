---
title: "Limites de Automacao e Consentimento"
area: "04-Conhecimentos/07-Humanidades/Etica"
tags: ["ethics","automation","consent","agents","safety"]
created: "2026-05-08"
status: "draft"
---

# Limites de Automacao e Consentimento

Automacao e um multiplicador. O limite etico/pratico e quando a automacao passa a:

- agir sobre recursos de terceiros sem autorizacao explicita
- alterar estado sem reversibilidade
- operar com baixa evidenca em ambiente real (producao)

## Niveis de consentimento (pratico)

1. Implicito: tarefas locais e reversiveis, sem dados sensiveis.
2. Explicito: tarefas com risco moderado (alterar configs, dependencias, migracoes).
3. Dupla confirmacao: tarefas de alto impacto (producao, dinheiro, dados pessoais, integracoes externas).

## Regras de limite para agentes de programacao

- Nao executar automacao que envia dados para fora sem confirmacao.
- Nao rodar comandos destrutivos sem confirmacao e sem backup.
- Nao alterar "hubs canonicamente lidos" sem revisar impacto.
- Nao persistir credenciais/segredos em notas.

## Kill switches (sempre que houver autonomia)

- flag para desligar automacao
- limite de tempo/quantidade (rate limit)
- modo dry-run
- logs resumidos e auditaveis

## Relacionado

- [[Seguranca-vs-Utilidade-Tradeoffs]]
- [[Auditoria-de-Agentes-e-Evidencias]]
- [[Politica-de-Logs-para-Agentes]]


[[04-Conhecimentos/07-Humanidades/Etica/INDEX|← Voltar ao índice de Ética]]
