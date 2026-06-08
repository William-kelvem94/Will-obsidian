---
title: "MLOps"
category: "AI"
level: 3
description: "Operacionalizacao de modelos de IA: pipelines de treino, deploy, monitoramento, deteccao de drift e governanca continua."
projects:
  - "JARVIS Core"
  - "RAG-Local-Guide"
related_skills:
  - "FinOps"
  - "Observabilidade"
  - "Kubernetes"
resources:
  - "Google Cloud MLOps Guide"
  - "Papers sobre drift detection"
  - "MLflow e Kubeflow documentacao"
date: 2026-04-29
tags: [skills, ai, mlops]
updated: 2026-06-08
---

# MLOps

MLOps e a pratica de levar modelos de machine learning da experimentacao para producao com automacao, validacao e governanca. Este documento cobre deteccao de drift, model registry, pipelines YAML, A/B testing e monitoramento.

## Deteccao de Drift

### Data Drift

```python
from scipy.stats import ks_2samp
import numpy as np

def detect_data_drift(reference: np.ndarray, current: np.ndarray, threshold: float = 0.05) -> dict:
    """Detecta drift em features numericas usando KS test."""
    results = {}
    for col in reference.columns:
        stat, p_value = ks_2samp(reference[col], current[col])
        results[col] = {
            "drift": bool(p_value < threshold),
            "p_value": p_value,
            "statistic": stat
        }
    return results
```

### Model Drift

```python
class ModelMonitor:
    def __init__(self, model, reference_metrics: dict):
        self.model = model
        self.reference_metrics = reference_metrics

    def evaluate_drift(self, X_new, y_new) -> dict:
        predictions = self.model.predict(X_new)
        current_accuracy = accuracy_score(y_new, predictions)

        drift_detected = abs(current_accuracy - self.reference_metrics["accuracy"]) > 0.05

        return {
            "drift_detected": drift_detected,
            "current_accuracy": current_accuracy,
            "reference_accuracy": self.reference_metrics["accuracy"],
            "degradation": self.reference_metrics["accuracy"] - current_accuracy
        }
```

## Model Registry com MLflow

```python
import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("jarvis-rag")

with mlflow.start_run() as run:
    # Log parametros
    mlflow.log_param("model_type", "sentence-transformer")
    mlflow.log_param("embedding_dim", 384)
    mlflow.log_param("chunk_size", 512)

    # Log metricas
    mlflow.log_metric("recall@5", 0.87)
    mlflow.log_metric("precision@5", 0.82)
    mlflow.log_metric("latency_ms", 45.3)

    # Log artefatos
    mlflow.log_artifact("vector_store/index.faiss")
    mlflow.log_artifact("config.yaml")

    # Registrar modelo
    mlflow.sklearn.log_model(model, "embedding-model")

    # Registrar no registry
    model_version = mlflow.register_model(
        f"runs:/{run.info.run_id}/embedding-model",
        "JarvisEmbeddingModel"
    )
```

## Pipeline YAML (Kubeflow / Vertex AI)

```yaml
name: rag-training-pipeline
description: Pipeline de treino e deploy do modelo de embeddings RAG

components:
  - name: ingest-data
    image: gcr.io/jarvis/ingest:latest
    args:
      - --source: "/vault/notas"
      - --chunk_size: 512

  - name: train-embeddings
    image: gcr.io/jarvis/train:latest
    args:
      - --model: "sentence-transformers/all-MiniLM-L6-v2"
      - --epochs: 3
      - --batch_size: 32
    depends: [ingest-data]

  - name: evaluate
    image: gcr.io/jarvis/evaluate:latest
    args:
      - --test_set: "gs://jarvis-data/test.parquet"
    depends: [train-embeddings]

  - name: deploy
    image: gcr.io/jarvis/deploy:latest
    args:
      - --target: "production"
      - --replicas: 2
    depends: [evaluate]
    condition: "metrics.recall@5 > 0.85"
```

## A/B Testing para Modelos

```python
class ModelRouter:
    def __init__(self, model_a, model_b, traffic_split: float = 0.5):
        self.model_a = model_a
        self.model_b = model_b
        self.split = traffic_split
        self.metrics = {"a": [], "b": []}

    def predict(self, input_data):
        import random
        if random.random() < self.split:
            result = self.model_a.predict(input_data)
            self.metrics["a"].append(result)
            return result, "model_a"
        else:
            result = self.model_b.predict(input_data)
            self.metrics["b"].append(result)
            return result, "model_b"

    def get_winner(self):
        score_a = self._evaluate(self.metrics["a"])
        score_b = self._evaluate(self.metrics["b"])
        return "model_a" if score_a > score_b else "model_b"
```

## Monitoramento com Prometheus

```python
from prometheus_client import Histogram, Counter, Gauge, start_http_server

LATENCY = Histogram(
    "model_inference_latency_seconds",
    "Latencia de inferencia do modelo",
    buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 5.0]
)

REQUESTS = Counter(
    "model_requests_total",
    "Total de requisicoes ao modelo",
    ["model_version", "status"]
)

DRIFT_SCORE = Gauge(
    "model_drift_score",
    "Score de drift do modelo (0-1)"
)

@LATENCY.time()
def predict(input_data):
    try:
        result = model.predict(input_data)
        REQUESTS.labels(model_version="v2", status="success").inc()
        return result
    except Exception:
        REQUESTS.labels(model_version="v2", status="error").inc()
        raise
```

## Pipeline CI/CD para ML

```yaml
# .github/workflows/ml-pipeline.yml
name: ML Training Pipeline
on:
  push:
    branches: [main]
    paths: ["models/**", "data/**"]

jobs:
  train:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Train model
        run: python train.py
      - name: Evaluate
        run: python evaluate.py
      - name: Deploy if metrics pass
        if: ${{ env.RECALL > 0.85 }}
        run: python deploy.py
```

## Referencias

- [[05-Skills/ai/Reinforcement-Learning|Reinforcement Learning]] — RL para otimizacao continua de modelos
- [[05-Skills/devops/FinOps|FinOps]] — Otimizacao de custos de treino e inferencia
- [[05-Skills/devops/Kubernetes|Kubernetes]] — Orquestracao de servicos de ML
- [[05-Skills/devops/Observabilidade|Observabilidade]] — Dashboards e alertas para modelos
- [[05-Skills/04-knowledge-systems/INDEX|Knowledge Systems]] — RAG como pipeline MLOps
