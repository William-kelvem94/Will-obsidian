---
title: "Application Monitoring"
description: "Observability, logging, and performance monitoring for production systems"
tags: [monitoring, observability, logging, metrics, performance, devops, skills-mcp]
updated: 2026-05-03
date: 2026-04-27
---

# Application Monitoring Skill

Comprehensive guide to monitoring and observability for production systems.

---

## 🎯 The Three Pillars of Observability

### 1. Logs
**What happened?**
- Events and errors
- Timestamps and context
- Structured data (JSON)

### 2. Metrics
**How much/how many?**
- Request counts
- Response times
- Resource usage

### 3. Traces
**Where did it go?**
- Request flow through system
- Service dependencies
- Bottleneck identification

---

## 📊 Logging Best Practices

### Structured Logging (Python)

```python
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        
        # Add extra fields
        if hasattr(record, "user_id"):
            log_data["user_id"] = record.user_id
        if hasattr(record, "request_id"):
            log_data["request_id"] = record.request_id
        
        # Add exception info
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        return json.dumps(log_data)

# Setup
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Usage
logger.info("User logged in", extra={"user_id": 123, "ip": "192.168.1.1"})
logger.error("Database connection failed", extra={"db_host": "localhost"})
```

### Structured Logging (TypeScript)

```typescript
import winston from 'winston'

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: { service: 'api' },
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' }),
  ],
})

// Usage
logger.info('User logged in', { userId: 123, ip: '192.168.1.1' })
logger.error('Database connection failed', { dbHost: 'localhost', error: err })
```

### Log Levels

```
TRACE   - Very detailed, only in development
DEBUG   - Detailed information for debugging
INFO    - General informational messages
WARNING - Something unexpected, but not an error
ERROR   - Error occurred, but app can continue
CRITICAL/FATAL - Severe error, app might crash
```

**Best practices:**
```python
# ✅ Good - specific and actionable
logger.error(
    "Failed to process payment",
    extra={
        "user_id": user_id,
        "amount": amount,
        "payment_provider": "stripe",
        "error_code": "card_declined"
    }
)

# ❌ Bad - vague and unhelpful
logger.error("Error occurred")
```

---

## 📈 Metrics Collection

### Prometheus Example (FastAPI)

```python
from prometheus_client import Counter, Histogram, Gauge, generate_latest
from fastapi import FastAPI, Response
import time

app = FastAPI()

# Define metrics
request_count = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

request_duration = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration',
    ['method', 'endpoint']
)

active_users = Gauge(
    'active_users',
    'Number of active users'
)

# Middleware to track metrics
@app.middleware("http")
async def metrics_middleware(request, call_next):
    start_time = time.time()
    
    response = await call_next(request)
    
    duration = time.time() - start_time
    
    # Record metrics
    request_count.labels(
        method=request.method,
        endpoint=request.url.path,
        status=response.status_code
    ).inc()
    
    request_duration.labels(
        method=request.method,
        endpoint=request.url.path
    ).observe(duration)
    
    return response

# Metrics endpoint
@app.get("/metrics")
async def metrics():
    return Response(
        content=generate_latest(),
        media_type="text/plain"
    )
```

### Key Metrics to Track

**Application metrics:**
```
- Request rate (requests/sec)
- Error rate (errors/sec, %)
- Response time (p50, p95, p99)
- Active connections
- Queue depth
```

**Infrastructure metrics:**
```
- CPU usage (%)
- Memory usage (MB, %)
- Disk I/O (IOPS, MB/s)
- Network traffic (packets/sec, MB/s)
```

**Business metrics:**
```
- User signups
- Purchases
- Active sessions
- Feature usage
```

---

## 🔍 Distributed Tracing

### OpenTelemetry (Python)

```python
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Setup tracer
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

# Usage in code
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    with tracer.start_as_current_span("get_user") as span:
        span.set_attribute("user.id", user_id)
        
        with tracer.start_as_current_span("database_query"):
            user = await db.fetch_user(user_id)
        
        with tracer.start_as_current_span("cache_store"):
            await cache.set(f"user:{user_id}", user)
        
        return user
```

---

## 🚨 Alerting

### Alert Rules (Prometheus)

```yaml
groups:
  - name: api_alerts
    rules:
      # High error rate
      - alert: HighErrorRate
        expr: |
          rate(http_requests_total{status=~"5.."}[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"
          description: "Error rate is {{ $value }} (>5%)"
      
      # Slow response time
      - alert: SlowResponseTime
        expr: |
          histogram_quantile(0.95, 
            rate(http_request_duration_seconds_bucket[5m])
          ) > 2
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: "API response time is slow"
          description: "P95 latency is {{ $value }}s (>2s)"
      
      # Service down
      - alert: ServiceDown
        expr: up == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Service is down"
          description: "{{ $labels.instance }} is unreachable"
```

### Alert Destinations

```yaml
# alertmanager.yml
route:
  receiver: 'team-slack'
  group_by: ['alertname', 'severity']
  group_wait: 10s
  group_interval: 5m
  repeat_interval: 12h
  
  routes:
    - match:
        severity: critical
      receiver: 'pagerduty'
    
    - match:
        severity: warning
      receiver: 'team-email'

receivers:
  - name: 'team-slack'
    slack_configs:
      - api_url: 'https://hooks.slack.com/services/...'
        channel: '#alerts'
  
  - name: 'pagerduty'
    pagerduty_configs:
      - service_key: '...'
  
  - name: 'team-email'
    email_configs:
      - to: 'team@example.com'
```

---

## 📱 Health Checks

### Basic Health Check

```python
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/health/detailed")
async def detailed_health():
    checks = {
        "database": await check_database(),
        "redis": await check_redis(),
        "disk_space": check_disk_space(),
    }
    
    all_healthy = all(checks.values())
    
    status_code = status.HTTP_200_OK if all_healthy else status.HTTP_503_SERVICE_UNAVAILABLE
    
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "healthy" if all_healthy else "unhealthy",
            "checks": checks
        }
    )

async def check_database():
    try:
        await db.execute("SELECT 1")
        return True
    except Exception:
        return False
```

### Kubernetes Probes

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  template:
    spec:
      containers:
      - name: api
        image: myapi:latest
        ports:
        - containerPort: 8000
        
        # Liveness probe (restart if fails)
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        
        # Readiness probe (remove from load balancer if fails)
        readinessProbe:
          httpGet:
            path: /health/detailed
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 5
          timeoutSeconds: 3
          failureThreshold: 3
```

---

## 🎭 APM (Application Performance Monitoring)

### New Relic Integration

```python
import newrelic.agent

# Initialize
newrelic.agent.initialize('newrelic.ini')

# Decorator for custom instrumentation
@newrelic.agent.background_task()
def process_payment(user_id, amount):
    # Your code
    pass

# Custom metrics
newrelic.agent.record_custom_metric('Custom/PaymentProcessed', amount)

# Custom events
newrelic.agent.record_custom_event('UserSignup', {
    'userId': user_id,
    'plan': 'premium'
})
```

### Sentry (Error Tracking)

```python
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration

sentry_sdk.init(
    dsn="https://...@sentry.io/...",
    integrations=[FastApiIntegration()],
    traces_sample_rate=0.1,  # 10% of requests
    environment="production"
)

# Custom context
with sentry_sdk.configure_scope() as scope:
    scope.set_user({"id": user_id, "email": user_email})
    scope.set_tag("payment_provider", "stripe")
    scope.set_context("payment", {
        "amount": amount,
        "currency": "USD"
    })
```

---

## 🐳 Docker Monitoring

### docker-compose with Prometheus + Grafana

```yaml
version: '3.8'

services:
  # Your app
  api:
    build: .
    ports:
      - "8000:8000"
  
  # Prometheus
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
  
  # Grafana
  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin

volumes:
  prometheus_data:
  grafana_data:
```

```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'api'
    static_configs:
      - targets: ['api:8000']
```

---

## 🔗 Related Resources

- [[JARVIS/04-Engineering/Wiki/CheatSheets/Docker|Docker Cheat Sheet]]
- [[JARVIS/04-Engineering/Playbooks/|Troubleshooting Playbooks]]
- [[skills/03-infrastructure-mcp/|Infrastructure Skills]]

---

*You can't improve what you don't measure. Monitor everything that matters.*
