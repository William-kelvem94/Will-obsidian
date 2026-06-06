---
title: "Kaggle — Datasets, Competições e Aprendizado em Ciência de Dados"
description: "Guia completo sobre Kaggle: como usar datasets públicos, competições, notebooks e estratégias para aprender ciência de dados na prática."
tags: [kaggle, datasets, competicao, data-science, skills]
nivel: intermediário
updated: 2026-06-05
backlinks: []
assets: []
referencias: []
sensivel: false
date: 2026-06-01
---

# Kaggle — Datasets, Competições e Aprendizado em Ciência de Dados

## O que é Kaggle?

Kaggle é a maior plataforma de ciência de dados do mundo, fundada em 2010 e adquirida pelo Google em 2017. Reúne:

- **Datasets públicos:** milhares de datasets prontos para uso
- **Competições:** desafios com premiações em dinheiro e reputação
- **Kernels/Notebooks:** ambiente de execução Jupyter na nuvem (GPU/TPU grátis)
- **Courses:** cursos gratuitos de Python, ML, SQL, etc.
- **Discussion:** fóruns técnicos com a comunidade de dados

Para quem está aprendendo, Kaggle é o melhor laboratório de data science disponível.

---

## Datasets Públicos

### Como Encontrar Datasets

```
https://www.kaggle.com/datasets
```

Filtros úteis:
- **Task:** Classificação, Regressão, NLP, Visão Computacional
- **Size:** Small (< 1GB), Medium (1-10GB), Large (> 10GB)
- **License:** CC0, MIT, GPL, etc.
- **File type:** CSV, JSON, Parquet, SQLite
- **Recently updated:** para datasets atualizados

### Baixando Datasets

```bash
# Via CLI do Kaggle
kaggle datasets download -d utkarshx27/heart-disease-dataset
unzip heart-disease-dataset.zip -d data/

# Ou via API Python
import kagglehub
path = kagglehub.dataset_download("utkarshx27/heart-disease-dataset")
```

### Datasets Clássicos para Aprender

| Dataset | Tarefa | Features | Tamanho |
|---------|--------|----------|---------|
| **Titanic** | Classificação binária | 12 colunas | 891 linhas |
| **Housing Prices** | Regressão | 80 colunas | 1460 linhas |
| **Digit Recognizer** | Visão (MNIST) | 784 pixels | 42000 imagens |
| **Spaceship Titanic** | Classificação | 14 colunas | 8700 linhas |
| **Heart Disease** | Classificação médica | 14 colunas | 303 linhas |

### ETL de Datasets Kaggle

Para integrar datasets Kaggle em pipelines, veja [[data-engineering/etl-pipelines]]. Um fluxo típico:

```python
import pandas as pd
import kagglehub

# Download + leitura
path = kagglehub.dataset_download("datasets-identifier")
df = pd.read_csv(f"{path}/train.csv")

# Limpeza (consulte [[skills/Data-Cleaning]])
df = df.drop_duplicates()
df = df.fillna(df.median(numeric_only=True))
```

---

## Competições

### Tipos de Competição

| Tipo | Exemplo | Característica |
|------|---------|----------------|
| **Featured** | Google AI, NATO | Patrocinadas, premiação alta |
| **Research** | LLM Science Exam | Acadêmicas, sem premiação |
| **Getting Started** | Titanic | Para iniciantes, tutorial incluso |
| **Playground** | 2026 Data Survey | Sintéticas, sazonais |
| **InClass** | - | Exclusivas para cursos |

### Estrutura de uma Competição

```
Treino (com labels) → seu modelo → Submissão (previsões) → Leaderboard Público (30%) + Privado (70%)
```

- **Public Leaderboard:** baseado em 30% dos dados de teste. Disponível durante a competição.
- **Private Leaderboard:** baseado nos 70% restantes. Revelado após o término.

**Armadilha:** Otimizar demais para o Public LB pode levar a overfitting. Sempre valide localmente.

### Workflow de Competição

```python
# EDA inicial (Análise Exploratória)
# Consulte [[skills/Data-Cleaning]] para limpeza
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

print(train.info())
print(train.isnull().sum())
print(train.describe())

# Correlações
plt.figure(figsize=(12, 8))
sns.heatmap(train.corr(numeric_only=True), annot=True, fmt=".2f")
plt.show()
```

Após EDA, construa pipelines conforme [[skills/Scikit-Learn]]:

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestClassifier(n_estimators=500, random_state=42))
])

scores = cross_val_score(pipeline, X_train, y_train, cv=5, scoring="accuracy")
print(f"CV Score: {scores.mean():.4f} ± {scores.std():.4f}")

# Treino final + predição
pipeline.fit(X_train, y_train)
predictions = pipeline.predict(test)

# Submissão
submission = pd.DataFrame({
    "PassengerId": test["PassengerId"],
    "Transported": predictions
})
submission.to_csv("submission.csv", index=False)
```

---

## Notebooks (Kernels)

### Vantagens dos Notebooks Kaggle

- **GPU/TPU grátis:** Tesla P100, T4, TPU v3 (até 30h/semana)
- **Dados pré-carregados:** sem download manual
- **Versionamento:** cada notebook é versionado
- **Fork:** copie e modifique notebooks da comunidade
- **Output público:** compartilhe visualizações e resultados

### Estratégia de Aprendizado com Notebooks

1. **Leia notebooks de ouro** (Gold Medal solutions)
2. **Fork e modifique** — entenda cada linha, mude parâmetros, quebre propositalmente
3. **Publique seus notebooks** — ensinar é a melhor forma de aprender
4. **Compare abordagens:** XGBoost vs Neural Network vs Ensemble

### Exemplo: Análise Exploratória

```python
# Notebook público típico
import plotly.express as px

# Distribuição de variáveis
fig = px.histogram(train, x="Age", color="Survived", nbins=30,
                   title="Distribuição de Idade por Sobrevivência",
                   barmode="overlay")
fig.show()

# Pairplot (relações entre variáveis)
fig = px.scatter_matrix(train, dimensions=["Age", "Fare", "Pclass", "SibSp"],
                        color="Survived")
fig.show()
```

---

## Estratégias para Aprender Data Science no Kaggle

### Rota de Aprendizado Progressiva

| Nível | Competições | Foco |
|-------|-------------|------|
| **1. Iniciante** | Titanic, Spaceship Titanic | EDA, pandas, gráficos básicos |
| **2. Intermediário** | Housing Prices, Digit Recognizer | Feature engineering, pipelines |
| **3. Avançado** | Playground Seasonal, Tabular Playground | Ensemble, tuning, validação robusta |
| **4. Especialista** | Featured Competitions | Stacking, NLP, visão computacional |

### Hábitos de um Kaggle Eficiente

1. **Suba uma baseline simples primeiro.** Regressão logística ou média. Depois refine.
2. **Validação robusta > métrica de leaderboard.** K-Fold estratificado é obrigatório.
3. **Feature engineering é o que separa top 10% do resto.** Consulte [[skills/Data-Cleaning]].
4. **Leia as discussões.** O fórum tem mais valor que qualquer curso.
5. **Não persiga Public LB.** Valide localmente com CV bem desenhado.
6. **Documente cada experimento.** Notebook + anotações no vault.

### Ferramentas Essenciais

- **Scikit-Learn:** pipelines, preprocessing, modelos baseline. Veja [[skills/Scikit-Learn]].
- **XGBoost / LightGBM:** modelos campeões de competições tabulares.
- **Pandas + NumPy:** manipulação de dados. Veja [[skills/Data-Cleaning]].
- **Matplotlib + Seaborn:** visualização para EDA.
- **Optuna:** otimização de hiperparâmetros (melhor que GridSearchCV para grandes espaços).

```python
import optuna
from sklearn.ensemble import RandomForestClassifier

def objective(trial):
    params = {
        "n_estimators": trial.suggest_int("n_estimators", 100, 1000),
        "max_depth": trial.suggest_int("max_depth", 3, 30),
        "min_samples_split": trial.suggest_int("min_samples_split", 2, 20),
        "min_samples_leaf": trial.suggest_int("min_samples_leaf", 1, 10)
    }
    model = RandomForestClassifier(**params, random_state=42)
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring="accuracy")
    return scores.mean()

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=50)
print(study.best_params)
```

---

## Conexões com o Vault

### Data Cleaning

Kaggle datasets raramente vêm limpos. Consulte [[skills/Data-Cleaning]] para técnicas de tratamento de nulos, outliers e encoding — habilidades essenciais para qualquer competição.

### Scikit-Learn

[[skills/Scikit-Learn]] é a biblioteca principal para construir modelos baseline e pipelines. A maioria das soluções vencedoras combina Scikit-Learn + XGBoost.

### Engenharia de Dados

Para datasets grandes (+10GB), consulte [[data-engineering/etl-pipelines]] para estratégias de processamento distribuído e otimização de memória.

### Projetos

Use o [[skills/Skill-Project-Matrix]] para mapear competições Kaggle como projetos de aprendizado no seu plano de desenvolvimento.

---

## Boas Práticas

1. **Nunca compartilhe soluções durante a competição.** Violação das regras.
2. **Use `cross_val_score` antes de submeter.** Evita overfitting no Public LB.
3. **Feature engineering antes de tuning.** Features bem construídas valem mais que hiperparâmetros otimizados.
4. **Mantenha um caderno de experimentos.** Documente cada submissão, feature testada, e score.
5. **Participe dos fóruns.** Pergunte, responda, compartilhe.
6. **Estude soluções vencedoras.** Após a competição, leia os notebooks dos medalhistas.

---

*Consulte também: [[skills/Data-Cleaning]], [[skills/Scikit-Learn]], [[data-engineering/etl-pipelines]], [[02-software-engineering/algorithms-data-structures]].*

[[skills/README|← Voltar à Taxonomia de Skills]]
