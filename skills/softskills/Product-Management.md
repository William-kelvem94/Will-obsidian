---
title: "Product Management"
category: "Softskills"
level: 3
description: "Gestao de produtos para priorizar valor, alinhar stakeholders e conduzir entregas com foco em impacto real. Inclui OKR, Scrum, Lean e priorizacao."
projects:
  - "JARVIS Core"
related_skills:
  - "Observabilidade"
  - "Kubernetes"
  - "MLOps"
resources:
  - "Inspired (Marty Cagan)"
  - "Lean Startup (Eric Ries)"
  - "Product management frameworks overview"
date: 2026-04-29
tags: [skills, softskills, product-management]
updated: 2026-05-16
---

# Product Management

Product management define valor, valida solucoes com usuarios e garante que o desenvolvimento entregue impacto real. Este documento cobre frameworks (OKR, Scrum, Lean), gestao de stakeholders e metodos de priorizacao.

## Frameworks de Gestao

### OKR (Objectives and Key Results)

```markdown
## Objective: Tornar JARVIS um assistente de codigo confiavel para o dia a dia

### Key Results
| KR | Meta | Atual | Dono |
|----|------|-------|------|
| KR1: Precisao do RAG em perguntas tecnicas | > 85% | 72% | Will |
| KR2: Tempo medio de resposta do agente | < 3s | 5.2s | Will |
| KR3: Tarefas completadas sem intervencao | > 70% | 45% | Will |
| KR4: NPS dos usuarios do JARVIS | > 50 | 32 | Will |

### Iniciativas
- [ ] Otimizar pipeline de chunking semantico (afeta KR1)
- [ ] Implementar cache de embeddings (afeta KR2)
- [ ] Adicionar loop de feedback com RL (afeta KR3)
```

### Scrum (Adaptado para Projetos Individuais)

```markdown
## Sprint Planning Template

### Sprint Goal
[Frase unica descrevendo o objetivo da sprint]

### Backlog Selecionado
| Item | Estimativa | Prioridade | Dependencias |
|------|------------|------------|--------------|
| [US-01] Implementar busca hibrida BM25 + vetorial | 8 pts | P0 | - |
| [US-02] Adicionar cache Redis para queries frequentes | 5 pts | P1 | US-01 |
| [US-03] Dashboard de metricas RAG | 3 pts | P2 | US-01 |

### Definition of Done
- [ ] Codigo revisado e testado
- [ ] Documentacao atualizada
- [ ] Metricas coletadas
- [ ] PR merged na main
```

### Lean Startup — Build-Measure-Learn

```python
class LeanExperiment:
    def __init__(self, hypothesis: str, metric: str, success_criteria: float):
        self.hypothesis = hypothesis        # "Acreditamos que X resolve o problema Y"
        self.metric = metric                # "Taxa de retencao apos 7 dias"
        self.success_criteria = success_criteria
        self.results = []

    def build(self, mvp: callable):
        """Constroi a versao minima viavel."""
        self.mvp = mvp
        return self

    def measure(self, users: list):
        """Coleta metricas do MVP com usuarios reais."""
        for user in users:
            result = self.mvp(user)
            self.results.append(result)
        return self

    def learn(self) -> dict:
        """Analisa resultados e decide pivotar ou perseverar."""
        avg_result = sum(self.results) / len(self.results)
        return {
            "hypothesis": self.hypothesis,
            "result": avg_result,
            "success": avg_result >= self.success_criteria,
            "decision": "perseverar" if avg_result >= self.success_criteria else "pivotar",
            "insights": self._generate_insights()
        }
```

## Metodos de Priorizacao

### RICE Score

```python
def rice_score(
    reach: int,        # Quantos usuarios serao impactados por mes
    impact: float,     # 0.25 (minimo) a 3 (massivo)
    confidence: float, # 0.2 (baixo), 0.5 (medio), 0.8 (alto), 1.0 (muito alto)
    effort: int        # Homem-meses estimados
) -> float:
    """Calcula prioridade RICE: (Reach * Impact * Confidence) / Effort."""
    return (reach * impact * confidence) / effort

# Exemplo
features = [
    {"name": "Busca semantica", "reach": 500, "impact": 3, "confidence": 0.8, "effort": 3},
    {"name": "Cache Redis", "reach": 1000, "impact": 2, "confidence": 1.0, "effort": 1},
    {"name": "Dark mode", "reach": 200, "impact": 0.5, "confidence": 0.5, "effort": 0.5},
]

for f in features:
    f["rice"] = rice_score(f["reach"], f["impact"], f["confidence"], f["effort"])

# Ordenado por RICE: Cache Redis > Busca semantica > Dark mode
```

### Matriz de Valor vs Esforco

```python
def value_effort_matrix(features: list[dict]) -> dict:
    """Classifica features em 4 quadrantes."""
    classified = {"alto_valor_baixo_esforco": [],
                  "alto_valor_alto_esforco": [],
                  "baixo_valor_baixo_esforco": [],
                  "baixo_valor_alto_esforco": []}

    for f in features:
        if f["value"] >= 7 and f["effort"] <= 3:
            classified["alto_valor_baixo_esforco"].append(f)
        elif f["value"] >= 7 and f["effort"] > 3:
            classified["alto_valor_alto_esforco"].append(f)
        elif f["value"] < 7 and f["effort"] <= 3:
            classified["baixo_valor_baixo_esforco"].append(f)
        else:
            classified["baixo_valor_alto_esforco"].append(f)

    return classified
```

## Gestao de Stakeholders

### Mapa de Stakeholders

| Stakeholder | Interesse | Influencia | Estrategia |
|-------------|-----------|------------|------------|
| **Eu (Will)** | Produtividade pessoal | Alta | Dono do produto |
| **Futuros usuarios** | Ferramenta funcional | Baixa (agora) | Pesquisas e feedback |
| **Comunidade open-source** | Contribuicoes e docs | Media | Documentar e compartilhar |

### Template de Comunicacao

```markdown
## Status Update - Semana {{semana}}

### Concluido
- [Feature] Busca hibrida implementada e testada
- [Bugfix] Correcao de timeout no RAG com contextos longos

### Em andamento
- Cache Redis (70%) — previsao de conclusao: {{data}}
- Dashboard de metricas (30%) — previsao: {{data}}

### Bloqueios
- Nenhum no momento

### Proximos passos
1. Finalizar cache Redis
2. Iniciar testes A/B de modelos de embedding
3. Atualizar documentacao de arquitetura
```

## Metricas de Produto

```python
class ProductMetrics:
    def __init__(self):
        self.metrics = {
            "engagement": {
                "daily_active_users": 0,
                "sessions_per_user": 0.0,
                "avg_session_duration_min": 0.0
            },
            "quality": {
                "task_completion_rate": 0.0,
                "hallucination_rate": 0.0,
                "user_satisfaction_nps": 0
            },
            "business": {
                "cost_per_session": 0.0,
                "monthly_active_users": 0,
                "retention_d7": 0.0
            }
        }

    def update_nps(self, responses: list[int]) -> float:
        """Calcula Net Promoter Score (0-100)."""
        promoters = sum(1 for r in responses if r >= 9)
        detractors = sum(1 for r in responses if r <= 6)
        total = len(responses)
        return round(((promoters - detractors) / total) * 100, 1)
```

## Referencias

- [[skills/ai/MLOps|MLOps]] — Metricas de qualidade de modelo para produto
- [[skills/devops/FinOps|FinOps]] — Custo como feature e trade-offs de produto
- [[skills/devops/Observabilidade|Observabilidade]] — Dados para decisoes de produto
- [[Comunicacao-Tecnica|Comunicacao Tecnica]] — Documentacao e apresentacao para stakeholders
