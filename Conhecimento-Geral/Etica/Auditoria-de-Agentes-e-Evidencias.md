---
title: "Auditoria de Agentes e Evidencias"
area: "Conhecimento-Geral/Etica"
tags: ["ethics","audit","agents","logging","traceability"]
created: "2026-05-08"
status: "draft"
---

# Auditoria de Agentes e Evidencias

Auditoria nao e vigiar tudo: e permitir investigacao, reproducao e responsabilizacao quando algo da errado. Para agentes, auditoria boa e:

- proporcional (nao vaza conteudo sensivel)
- util (ajuda a entender e reverter)
- padronizada (sempre o mesmo formato)

## O que auditar (minimo util)

- Identidade do agente: nome/versao/config (sem segredos)
- Acoes executadas: comandos e arquivos tocados
- Evidencias: outputs resumidos e sinais
- Decisoes: por que escolheu um caminho
- Resultados: passou/falhou verificacoes

## O que nao auditar por padrao

- Conteudo completo de requests/responses de clientes
- Documentos pessoais, conversas, transcricoes integrais
- Secrets: tokens, chaves, cookies, headers de auth

## Formatos de evidencia

Preferir:

- referencias a arquivos e linhas
- hashes/ids internos
- contagens e percentuais

Evitar:

- colagens de payloads
- dumps de variaveis de ambiente

## Politicas de retencao (heuristica)

- curto prazo: logs detalhados (sanitizados) para debug
- medio prazo: resumos de incidente e decisoes
- longo prazo: aprendizados e guardrails, nao logs brutos

## Relacionado

- [[Politica-de-Logs-para-Agentes]]
- [[Transparencia-de-Decisao-e-Rastreabilidade]]
- [[Minimizacao-de-Dados-para-RAG-e-Agentes]]

