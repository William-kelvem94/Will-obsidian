---
title: "Kubernetes"
category: "DevOps"
level: 3
description: "Orquestracao de contêineres para implantar, escalar e gerir aplicacoes distribuidas. Inclui Pods, Deployments, Services, Helm, Ingress e RBAC."
projects:
  - "JARVIS Core"
related_skills:
  - "Observabilidade"
  - "FinOps"
  - "MLOps"
resources:
  - "Kubernetes official docs"
  - "Helm e k8s best practices"
date: 2026-04-29
tags: [skills, devops, kubernetes]
updated: 2026-06-08
---

# Kubernetes

Kubernetes (K8s) automatiza deploy, escalabilidade e gestao de aplicacoes containerizadas. Este documento cobre manifests essenciais, Helm charts, configuracao de Ingress e exemplos de RBAC.

## Pods e Deployments

### Pod Simples

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: jarvis-api
  labels:
    app: jarvis
    component: api
spec:
  containers:
    - name: api
      image: jarvis/api:latest
      ports:
        - containerPort: 8000
      resources:
        requests:
          cpu: "250m"
          memory: "256Mi"
        limits:
          cpu: "500m"
          memory: "512Mi"
      livenessProbe:
        httpGet:
          path: /health
          port: 8000
        initialDelaySeconds: 10
      readinessProbe:
        httpGet:
          path: /ready
          port: 8000
```

### Deployment com Estrategia Rolling Update

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jarvis-api
  namespace: jarvis
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: jarvis-api
  template:
    metadata:
      labels:
        app: jarvis-api
    spec:
      containers:
        - name: api
          image: {{ .Values.image.repository }}:{{ .Values.image.tag }}
          env:
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: jarvis-secrets
                  key: database-url
            - name: LOG_LEVEL
              value: "info"
          ports:
            - containerPort: 8000
```

## Services

```yaml
apiVersion: v1
kind: Service
metadata:
  name: jarvis-api-service
  namespace: jarvis
spec:
  type: ClusterIP
  selector:
    app: jarvis-api
  ports:
    - port: 80
      targetPort: 8000
      protocol: TCP
      name: http
---
apiVersion: v1
kind: Service
metadata:
  name: jarvis-db
spec:
  type: Headless
  selector:
    app: postgres
  ports:
    - port: 5432
      name: postgres
```

## Ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: jarvis-ingress
  namespace: jarvis
  annotations:
    nginx.ingress.kubernetes.io/rate-limit: "10r/m"
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - jarvis.internal
      secretName: jarvis-tls
  rules:
    - host: jarvis.internal
      http:
        paths:
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: jarvis-api-service
                port:
                  number: 80
          - path: /grafana
            pathType: Prefix
            backend:
              service:
                name: grafana
                port:
                  number: 3000
```

## Helm Chart Estruturado

```
jarvis-chart/
  Chart.yaml
  values.yaml
  templates/
    deployment.yaml
    service.yaml
    ingress.yaml
    configmap.yaml
    secrets.yaml
    hpa.yaml
```

### values.yaml

```yaml
image:
  repository: ghcr.io/jarvis/api
  tag: v1.2.3
  pullPolicy: IfNotPresent

replicaCount: 3

resources:
  requests:
    cpu: 250m
    memory: 256Mi
  limits:
    cpu: 1
    memory: 1Gi

autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70
  targetMemoryUtilizationPercentage: 80

ingress:
  enabled: true
  host: jarvis.internal
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
```

### HPA (Horizontal Pod Autoscaler)

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: jarvis-api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: jarvis-api
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 80
```

## RBAC (Role-Based Access Control)

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: jarvis
  name: jarvis-reader
rules:
  - apiGroups: [""]
    resources: ["pods", "services", "configmaps"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  namespace: jarvis
  name: jarvis-reader-binding
subjects:
  - kind: ServiceAccount
    name: jarvis-agent
    namespace: jarvis
roleRef:
  kind: Role
  name: jarvis-reader
  apiGroup: rbac.authorization.k8s.io
```

## ConfigMap e Secrets

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: jarvis-config
data:
  APP_ENV: production
  LOG_LEVEL: info
  CACHE_TTL: "300"
---
apiVersion: v1
kind: Secret
metadata:
  name: jarvis-secrets
type: Opaque
data:
  database-url: {{ .Values.secrets.databaseUrl | b64enc }}
  api-key: {{ .Values.secrets.apiKey | b64enc }}
```

## Comandos uteis

```bash
# Aplicar manifestos
kubectl apply -f deployment.yaml

# Verificar status
kubectl get pods -n jarvis -w

# Logs
kubectl logs -f deployment/jarvis-api -n jarvis

# Escalar manualmente
kubectl scale deployment/jarvis-api --replicas=5 -n jarvis

# Port forward para debug
kubectl port-forward service/jarvis-api-service 8000:80 -n jarvis
```

## Referencias

- [[05-Skills/devops/Observabilidade|Observabilidade]] — Prometheus e Grafana em K8s
- [[05-Skills/devops/FinOps|FinOps]] — Otimizacao de custos em clusters
- [[05-Skills/ai/MLOps|MLOps]] — Deploy de modelos em K8s
- [[05-Skills/03-infrastructure-mcp/mcp-servers|MCP Servers]] — Servidores MCP containerizados
