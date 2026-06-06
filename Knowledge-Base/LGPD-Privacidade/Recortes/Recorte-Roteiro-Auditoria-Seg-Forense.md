---
title: "Recorte: Roteiro Auditoria & Segurança Forense"
tags: [#recorte, #roteiro, #auditoria, #forense, #lgpd]
updated: 2026-05-24
status: active
---
# ROTEIRO DE AUDITORIA E SEGURANÇA FORENSE – LGPD

## 1. Checklist prático
- Execução semanal dos scripts `audit_sensitives.py`, `tag-linter.py`
- Análise obrigatória dos logs de execução (hash, chain-of-custody)
- Amostragem por área: RH, Saúde, TI, Marketing
- Check dos campos sensíveis/faltantes e duplicidades
- Output anexado a relatórios e lessons learned

## 2. Integração com incidentes
- Checklist de notificação e remediação automática
- Logs forenses anexados ao dashboard e ao artefato do incidente
- Liberação do push/deploy somente após evidência técnica da correção
- Plano de ação gerado para cada falha atuarial
---
