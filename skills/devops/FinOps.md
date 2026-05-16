---
title: "FinOps"
category: "DevOps"
level: 3
description: "Otimizacao de custos em nuvem, alinhamento de gastos com valor e operacoes de IA sustentaveis. Inclui calculadoras, tagging, budgets e otimizacao."
projects:
  - "JARVIS Core"
related_skills:
  - "MLOps"
  - "Kubernetes"
  - "Observabilidade"
resources:
  - "FinOps Foundation"
  - "Cloud cost optimization guides"
  - "AWS/Azure/GCP pricing calculators"
date: 2026-04-29
tags: [skills, devops, finops]
updated: 2026-05-16
---

# FinOps

FinOps integra financas e operacoes de nuvem para controlar custos e maximizar valor. Este documento cobre estrategias de tagging, calculadoras de custo, alertas de orcamento e otimizacao de recursos para infraestrutura de IA.

## Calculadoras de Custo

### Estimativa de Custo de GPU

```python
def estimate_gpu_cost(
    gpu_type: str,
    hours: float,
    region: str = "us-east-1"
) -> dict:
    """Estima custo de treino/inferencia em GPU."""
    prices = {
        "A100-80GB": {"on_demand": 3.93, "spot": 1.20, "reserved_1y": 2.36},
        "V100-32GB": {"on_demand": 2.48, "spot": 0.75, "reserved_1y": 1.49},
        "T4-16GB": {"on_demand": 0.94, "spot": 0.28, "reserved_1y": 0.56},
        "L4-24GB": {"on_demand": 1.44, "spot": 0.43, "reserved_1y": 0.86}
    }

    gpu = prices.get(gpu_type, prices["T4-16GB"])
    return {
        "gpu": gpu_type,
        "horas": hours,
        "on_demand": round(gpu["on_demand"] * hours, 2),
        "spot": round(gpu["spot"] * hours, 2),
        "reserved_1y": round(gpu["reserved_1y"] * hours, 2),
        "economia_spot": f"{round((1 - gpu['spot']/gpu['on_demand']) * 100)}%",
        "economia_reserved": f"{round((1 - gpu['reserved_1y']/gpu['on_demand']) * 100)}%"
    }
```

### Custo por Inferencia

```python
def inference_cost(
    model_size_b: float = 7,
    input_tokens: int = 512,
    output_tokens: int = 256,
    gpu_cost_per_hour: float = 0.94
) -> dict:
    """Estima custo por inferencia de LLM local."""
    # ~1 token/ms em GPU media para modelo 7B
    latency_s = (input_tokens + output_tokens) / 1000
    cost_per_inference = (latency_s / 3600) * gpu_cost_per_hour

    return {
        "model": f"{model_size_b}B",
        "latency_s": round(latency_s, 2),
        "cost_per_inference": round(cost_per_inference, 6),
        "cost_per_1k": round(cost_per_inference * 1000, 4),
        "cost_per_1m": round(cost_per_inference * 1_000_000, 2)
    }
```

## Estrategias de Tagging

```python
TAG_POLICY = {
    "mandatory": [
        "Projeto",        # jarvis-core, gestor-aluguel
        "Ambiente",       # production, staging, dev
        "Criador",        # will, bot-terraform
        "CentroDeCusto",  # eng-ia, eng-infra, data-science
    ],
    "optional": [
        "Recurso",        # gpu, cpu, storage, network
        "AutoDesligar",   # true, false
        "DataExpiracao",  # 2026-12-31
        "BudgetMonthly"   # 500
    ]
}

def validate_tags(resource_tags: dict) -> list[str]:
    """Valida tags contra a politica corporativa."""
    violations = []
    for tag in TAG_POLICY["mandatory"]:
        if tag not in resource_tags:
            violations.append(f"Tag obrigatoria ausente: {tag}")
    return violations
```

## Alertas de Orcamento

### AWS Budget via Terraform

```hcl
resource "aws_budgets_budget" "jarvis_monthly" {
  name         = "jarvis-monthly-budget"
  budget_type  = "COST"
  limit_amount = "500"
  limit_unit   = "USD"
  time_period_start = "2026-01-01_00:00"
  time_unit    = "MONTHLY"

  notification {
    comparison_operator = "GREATER_THAN"
    threshold          = 80
    threshold_type     = "PERCENTAGE"
    notification_type  = "ACTUAL"
    subscriber_email_addresses = ["will@email.com"]
  }

  notification {
    comparison_operator = "GREATER_THAN"
    threshold          = 100
    threshold_type     = "PERCENTAGE"
    notification_type  = "FORECASTED"
    subscriber_email_addresses = ["will@email.com"]
  }

  cost_filters = {
    TagKeyValue = "Projeto$jarvis-core"
  }
}
```

### Script de Alerta de Custo

```python
import boto3
from datetime import datetime, timedelta

def check_cost_anomaly(project: str = "jarvis-core", threshold_pct: float = 20.0):
    """Verifica anomalia de custo comparando com media dos ultimos 7 dias."""
    client = boto3.client("ce", region_name="us-east-1")
    today = datetime.now()
    last_7 = today - timedelta(days=7)

    response = client.get_cost_and_usage(
        TimePeriod={
            "Start": last_7.strftime("%Y-%m-%d"),
            "End": today.strftime("%Y-%m-%d")
        },
        Granularity="DAILY",
        Metrics=["UnblendedCost"],
        Filter={
            "Tags": {
                "Key": "Projeto",
                "Values": [project]
            }
        }
    )

    costs = [float(day["Total"]["UnblendedCost"]["Amount"])
             for day in response["ResultsByTime"]]
    avg_daily = sum(costs[:-1]) / (len(costs) - 1)
    today_cost = costs[-1]
    variance = ((today_cost - avg_daily) / avg_daily) * 100

    if abs(variance) > threshold_pct:
        return {
            "anomaly": True,
            "project": project,
            "today_cost": today_cost,
            "avg_daily": avg_daily,
            "variance_pct": round(variance, 2)
        }
    return {"anomaly": False}
```

## Otimizacao de Recursos

### Instance Right-Sizing

```python
def rightsizing_recommendation(
    current_type: str,
    cpu_utilization_p95: float,
    memory_utilization_p95: float
) -> dict:
    """Recomenda tipo de instancia otimizado baseado em utilizacao."""
    instances = {
        "t3.medium":  {"cpu": 2, "mem_gb": 4,  "cost": 0.0416},
        "t3.large":   {"cpu": 2, "mem_gb": 8,  "cost": 0.0832},
        "t3.xlarge":  {"cpu": 4, "mem_gb": 16, "cost": 0.1664},
        "g4dn.xlarge":{"cpu": 4, "mem_gb": 16, "gpu": "T4", "cost": 0.526}
    }

    current = instances.get(current_type)
    if not current:
        return {"error": "Tipo de instancia desconhecido"}

    metrics = {
        "current": {"type": current_type, "cpu_p95": cpu_utilization_p95,
                    "mem_p95": memory_utilization_p95, "cost": current["cost"]},
        "recommendation": "manter"
    }

    # Se CPU e memoria estao abaixo de 30%, recomenda downsizing
    if cpu_utilization_p95 < 30 and memory_utilization_p95 < 30:
        metrics["recommendation"] = "downsize"
        metrics["potential_savings"] = f"{round(current['cost'] * 0.5, 4)}/h"

    return metrics
```

### Schedule de Auto Desligamento

```yaml
# schedule.yaml
resources:
  - name: gpu-training-instance
    type: g4dn.xlarge
    schedule:
      on: "08:00"
      off: "19:00"
      timezone: "America/Sao_Paulo"
    days: ["monday", "tuesday", "wednesday", "thursday", "friday"]
    estimated_savings_per_month: 320  # USD
```

## Metricas de FinOps

```python
class FinOpsDashboard:
    def __init__(self):
        self.metrics = {}

    def calculate_unit_economics(self, total_cost: float, inferences: int) -> dict:
        return {
            "cost_per_inference": round(total_cost / inferences, 6),
            "inferences_per_dollar": round(inferences / total_cost, 0)
        }

    def savings_rate(self, on_demand_cost: float, actual_cost: float) -> float:
        return round((1 - actual_cost / on_demand_cost) * 100, 2)
```

## Referencias

- [[skills/devops/Kubernetes|Kubernetes]] — Resource limits e cluster optimization
- [[skills/devops/Observabilidade|Observabilidade]] — Custo por metrica e monitoramento
- [[skills/ai/MLOps|MLOps]] — Otimizacao de pipeline de treino
- [[skills/03-infrastructure-mcp/local-llm-ops|Local LLM Ops]] — Custos de inferencia local vs nuvem
