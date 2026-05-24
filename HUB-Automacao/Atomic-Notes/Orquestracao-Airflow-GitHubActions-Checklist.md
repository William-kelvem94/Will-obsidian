---
title: "Atomic Note – Orquestração Airflow, GitHub Actions, Pipelines"
tags: [#atomic, #airflow, #githubactions, #orquestracao, #automacao]
updated: 2026-05-24
status: active
---
# ORQUESTRAÇÃO AIRFLOW & GITHUB ACTIONS – ATOMIC NOTE

## 1. Frameworks de Orquestração
- Airflow: DAGs, Monitoramento, SLA, sensores e triggers customizados
- GitHub Actions: pipelines CI/CD, jobs condicionais, secrets, reusabilidade de workflows
- Prefect/Jenkins: comparação prática vs Airflow

## 2. Principais tópicos checklist
- Templates prontos de deploy
- Monitoramento centralizado de falhas
- Triggers automáticos de rollback
- Notificações scriptadas para times (Slack, email)
- Validação de outputs RPA e evidência para compliance
- Logs auditáveis obrigatórios por job/pipeline

## 3. Exemplo de pipeline (Airflow)
```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG('exemplo_automacao', start_date=datetime(2026,5,1), schedule_interval='@daily')

task1 = BashOperator(
    task_id='executar_script',
    bash_command='python3 scripts/rotina.py',
    dag=dag
)
```

## 4. Lições aprendidas
- Toda falha gera lesson learned obrigatória (registro atomic note)
- Adoção de padrão log-evidence = maior eficiência, menor retrabalho
---
