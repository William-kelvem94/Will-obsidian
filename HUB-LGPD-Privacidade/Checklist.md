---
title: "Checklist de Compliance & Auditoria LGPD - Completo"
tags: [#checklist, #lgpd, #auditoria]
updated: 2026-05-24
status: active
---
# CHECKLIST DE COMPLIANCE & AUDITORIA LGPD

## Itens obrigatórios em cada ciclo/semanal
- [ ] Todos os arquivos sensíveis possuem frontmatter completo (owner, confidential, compliance, review_due)?
- [ ] Algum arquivo identificado por scripts como portador de dado pessoal exposto sem consentimento ou autorização base legal?
- [ ] Scripts de auditoria (`audit_sensitives.py`, `tag-linter.py`) executados toda semana e falha bloqueando push?
- [ ] Recuperação de histórico: toda alteração sensível está devidamente versionada e logada?
- [ ] Notificações e alertas de incidentes enviados para owners, DPO e (quando necessário) ANPD?
- [ ] Revisão, treinamento e lessons learned feitas por todos os times com artefato sensível no ciclo?

## Métricas críticas/documentadas
- Taxa de conformidade semanal (% arquivos conformes)
- Tempo médio de resposta e mitigação
- % incidentes reincidentes
- Aderência a planos de resposta e templates de comunicação ANPD
