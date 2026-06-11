---
title: "Recorte: Exemplos Output — Auditoria Scripts LGPD"
tags: [#recorte, #auditoria, #output, #scripts, #lgpd]
updated: 2026-05-24
status: active
---
# EXEMPLOS — OUTPUTS DE AUDITORIA/COMPLIANCE

## 1. Output YAML — Auditoria
```yaml
- file: dados/salarios_funcionarios.md
  conforme: false
  motivo: ausência campo confidential
  owner: @gestor-rh
- file: dados/planilha_dependentes.md
  conforme: false
  motivo: dado pessoal exposto (email, nome, CPF)
  owner: @rh-direto
- file: dados/fornecedores.md
  conforme: true
  owner: @financeiro
```

## 2. Output JSON — Incidentes
```json
[
  {"file": "dados/notas_medicas.md","conforme": false, "motivo": "ausência compliance", "owner":"@gestor-saude"},
  {"file": "dados/acoes_marketing.md","conforme": true, "owner": "@leads-marketing"}
]
```

## 3. Integração CI/CD
- Output de scripts utilizado como artefato de bloqueio de push/deploy
- Todos outputs versionados, com hash em chain-of-custody
- Outputs anexados aos relatórios formais do hub LGPD
---
