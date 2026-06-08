---
title: "Template Runbook Operacional"
date: 2026-06-07
updated: 2026-06-07
type: template
status: active
tags: [conhecimento-geral, template, runbook, operacao, devops]
related: [[../15-Documentacao/Documentacao-Tecnica-Runbooks-e-ADRs]], [[../02-Engenharia-Software/Observabilidade-Logs-e-Monitoramento]], [[../02-Engenharia-Software/Docker-e-DevOps]]
summary: "Template para documentar operação, diagnóstico, validação e recuperação de sistemas."
---

# Template Runbook Operacional

Use este modelo para documentar como operar, diagnosticar ou recuperar um sistema.

```md
---
title: "Runbook - Nome da operação"
date: YYYY-MM-DD
updated: YYYY-MM-DD
type: runbook
status: active
tags: [runbook, operacao]
related: [[]]
summary: "Resumo curto da operação."
---

# Runbook - Nome da operação

## Objetivo

O que este runbook resolve?

## Quando usar

Quais sintomas ou cenários indicam uso?

## Pré-requisitos

- acesso necessário:
- ferramentas:
- ambiente:
- permissões:

## Passos

1. 
2. 
3. 

## Validação

Como saber que funcionou?

## Logs relevantes

Onde olhar logs?

## Rollback

Como voltar atrás?

## Riscos

- 

## Pós-ação

- registrar incidente;
- atualizar documentação;
- criar issue se necessário;
- revisar causa raiz.
```

## Quando criar runbook

Criar runbook para operações repetíveis, incidentes recorrentes, deploys, backups, restauração, reset de ambiente e diagnóstico.

## Links internos

- [[../15-Documentacao/Documentacao-Tecnica-Runbooks-e-ADRs]]
- [[../02-Engenharia-Software/Observabilidade-Logs-e-Monitoramento]]
- [[../02-Engenharia-Software/Docker-e-DevOps]]
