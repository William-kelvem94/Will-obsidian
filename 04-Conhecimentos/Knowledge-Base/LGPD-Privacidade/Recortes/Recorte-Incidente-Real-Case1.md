---
title: "Recorte de Incidente Real – Correção, Notificação, Resposta"
tags: [#recorte, #incidente, #case, #lgpd, #auditado]
updated: 2026-05-24
status: active
---
# RECORTE DE INCIDENTE REAL – LGPD

## 1. Descrição do Evento
Em fevereiro de 2025, rotina semanal de auditoria automatizada identificou arquivo planilha com dados de dependentes expostos (nome, email, responsáveis) sem controles mínimos de anonimização nem campo “consentimento” no frontmatter. Vazamento detectado pelo script `audit_sensitives.py` antes de push de release, bloqueando CI/CD.

## 2. Ação corretiva
- Correção imediata: adição dos campos owner, confidential, compliance, consentimento, data revisão.
- Backup do incidente armazenado via chain-of-custody.
- Commit bloqueado até campo compliance válido/adaptado.

## 3. Notificação
- Comunicação feita a todos owners identificados e, conforme matriz de risco, titulares afetados e DPO.
- Template formal de notificação ANPD utilizado (ver arquivos associados).
- Logs, scripts de varredura e output YAML anexados à documentação regulatória.

## 4. Lessons Learned
- Adotado linter automático em todos pipelines sensíveis (CI/CD).
- Rotina obrigatória de revisão semanal para times críticos.
- Discussão do incidente registrada em fórum interno de privacidade & compliance.
---
