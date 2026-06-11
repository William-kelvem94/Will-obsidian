---
title: "POC RPA – Automação de Contratos Financeiros"
tags: [#projeto, #poc, #rpa, #financas, #automacao]
updated: 2026-05-24
status: active
---
# PROJETO POC – AUTOMAÇÃO DE CONTRATOS FINANCEIROS

## 1. Objetivo
Automatizar validação e controle de contratos financeiros usando RPA Python/UiPath.

## 2. Arquitetura macro do fluxo
- Pipeline: ingestão → validação automática de cláusulas → scoring compliance → geração de log (YAML/JSON) → output automatizado para time jurídico
- Triggers: ingestão de contrato, alteração detectada, push relevante
- Logs auditáveis e relatório via Obsidian/PowerBI

## 3. Exemplo de código/roteiro Python
```python
import yaml
with open('contratos.yaml') as f:
    contratos = yaml.safe_load(f)
for c in contratos:
    if 'clausula_invalida' in c:
        print(f"Alerta contrato não conforme: {c['id']}")
```

## 4. Métricas críticas
- % contratos processados sem erro
- Tempo médio de resposta por pipeline
- Ocorrências de não conformidade por tipo

## 5. Lições aprendidas
- Checklist de boa prática validado por squads jurídicas
- Lessons learned documentada a cada update no workflow
---
