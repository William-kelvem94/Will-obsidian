---
title: "Observabilidade"
category: "DevOps"
level: 3
description: "Metricas, logs e tracing para entender e diagnosticar sistemas. Inclui configs Prometheus, dashboards Grafana, alertas e pads de logging."
projects:
  - "JARVIS Core"
related_skills:
  - "FinOps"
  - "Kubernetes"
  - "MLOps"
resources:
  - "Prometheus and Grafana guides"
  - "Distributed tracing best practices"
  - "OpenTelemetry documentation"
date: 2026-04-29
tags: [skills, devops, observability]
updated: 2026-06-01
---

# Observabilidade

Observabilidade e a capacidade de inferir o estado interno de um sistema a partir de metricas, logs e traces. Este documento cobre configuracao de Prometheus, dashboards Grafana, regras de alerta e pads de logging.

## Prometheus — Configuracoes

### prometheus.yml

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

alerting:
  alertmanagers:
    - static_configs:
        - targets: ["alertmanager:9093"]

rule_files:
  - "alerts/*.yml"

scrape_configs:
  - job_name: "jarvis-api"
    metrics_path: /metrics
    static_configs:
      - targets: ["jarvis-api:8000"]
        labels:
          service: api
          environment: production

  - job_name: "node-exporter"
    static_configs:
      - targets: ["node-exporter:9100"]

  - job_name: "postgres"
    static_configs:
      - targets: ["postgres-exporter:9187"]
```

### Exportando Metricas Customizadas (Python)

```python
from prometheus_client import Counter, Histogram, Gauge, generate_latest
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

REQUESTS = Counter(
    "http_requests_total",
    "Total de requisicoes HTTP",
    ["method", "endpoint", "status"]
)

LATENCY = Histogram(
    "http_request_duration_seconds",
    "Duracao das requisicoes HTTP",
    ["endpoint"],
    buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 5.0]
)

ACTIVE_USERS = Gauge(
    "active_users_total",
    "Numero de usuarios ativos no momento"
)

@app.get("/metrics")
async def metrics():
    return PlainTextResponse(media_type="text/plain", content=generate_latest())
```

## Grafana — Dashboards

### Dashboard JSON Model (trecho)

```json
{
  "title": "JARVIS - Visao Geral",
  "panels": [
    {
      "title": "Latencia P99",
      "type": "graph",
      "targets": [{
        "expr": "histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))",
        "legendFormat": "P99 - {{endpoint}}"
      }],
      "yaxes": [{"format": "s", "label": "Latencia"}]
    },
    {
      "title": "Taxa de Erro",
      "type": "stat",
      "targets": [{
        "expr": "sum(rate(http_requests_total{status=~\"5..\"}[5m])) / sum(rate(http_requests_total[5m])) * 100",
        "legendFormat": "Erro %"
      }],
      "thresholds": [{"value": 1, "color": "yellow"}, {"value": 5, "color": "red"}]
    },
    {
      "title": "Requisoes por minuto",
      "type": "graph",
      "targets": [{
        "expr": "sum(rate(http_requests_total[1m]))",
        "legendFormat": "RPM"
      }]
    }
  ]
}
```

## Regras de Alerta

### alerts.yml

```yaml
groups:
  - name: jarvis-alerts
    rules:
      - alert: HighErrorRate
        expr: |
          sum(rate(http_requests_total{status=~"5.."}[5m]))
          / sum(rate(http_requests_total[5m])) * 100 > 5
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Taxa de erro acima de 5%"
          description: "A taxa de erro do {{ $labels.service }} esta em {{ $value }}%"

      - alert: HighLatency
        expr: |
          histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m])) > 2
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Latencia P99 acima de 2s"

      - alert: ServiceDown
        expr: up{job="jarvis-api"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Servico {{ $labels.job }} indisponivel"

      - alert: HighMemoryUsage
        expr: |
          (node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes)
          / node_memory_MemTotal_bytes * 100 > 85
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "Uso de memoria acima de 85%"
```

## Padroes de Logging

### Logging Estruturado (Python)

```python
import structlog
import logging

structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.dev.ConsoleRenderer()
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    context_class=dict,
    logger_factory=structlog.PrintLoggerFactory(),
    cache_logger_on_first_use=True
)

logger = structlog.get_logger()

logger.info("requisicao recebida",
    method="GET",
    path="/api/users",
    user_id=42,
    duration_ms=145.3
)

logger.error("falha no banco de dados",
    database="postgres",
    error="connection_timeout",
    retry_count=3
)
```

### Correlacao com Trace ID

```python
import uuid
from contextvars import ContextVar

trace_id_var: ContextVar[str] = ContextVar("trace_id", default="")

class TraceMiddleware:
    async def __call__(self, request, call_next):
        trace_id = request.headers.get("X-Trace-ID", str(uuid.uuid4()))
        trace_id_var.set(trace_id)
        response = await call_next(request)
        response.headers["X-Trace-ID"] = trace_id
        return response

logger.info("processando pagamento",
    trace_id=trace_id_var.get(),
    order_id=order.id,
    amount=order.total
)
```

## OpenTelemetry Tracing

```python
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="otel-collector:4317"))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("query-rag") as span:
    span.set_attribute("query", user_query)
    span.set_attribute("chunks_retrieved", len(chunks))

    with tracer.start_as_current_span("embedding") as embed_span:
        embedding = generate_embedding(user_query)
        embed_span.set_attribute("model", "text-embedding-3-small")

    with tracer.start_as_current_span("search") as search_span:
        results = vector_store.search(embedding)
        search_span.set_attribute("results_count", len(results))
```

## Referencias

- [[skills/devops/Kubernetes|Kubernetes]] — Monitoramento de clusters K8s
- [[skills/devops/FinOps|FinOps]] — Custo por metrica e economia otimizada
- [[skills/ai/MLOps|MLOps]] — Monitoramento de drift e qualidade de modelo
- [[skills/03-infrastructure-mcp/advanced-mcp-integrations|MCP Avancado]] — Monitoramento de servidores MCP
## Notas Praticas (Agentes)

- [[observability-practical|Observability Practical]]
- [[logging-practical|Logging Practical]]
- [[metrics-practical|Metrics Practical]]
- [[tracing-practical|Tracing Practical]]
- [[slo-sli-sla-basics|SLO/SLI/SLA Basics]]
- [[incident-response-practical|Incident Response Practical]]
- [[runbooks-for-agents|Runbooks for Agents]]
- [[minimal-alerting-policy|Minimal Alerting Policy]]
- [[opsec-minimum|OPSEC Minimum]]
