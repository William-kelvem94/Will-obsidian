---
title: "Scikit-Learn — Machine Learning em Python"
description: "Guia completo do Scikit-Learn: pipelines, pré-processamento, modelos de regressão, classificação, clustering, redução de dimensionalidade, validação e grid search."
tags: [scikit-learn, machine-learning, python, classificacao, regressao]
nivel: avancado
updated: 2026-05-18
backlinks: []
assets: []
referencias: []
sensivel: false
---

# Scikit-Learn — Machine Learning em Python

## Visão Geral

**Scikit-Learn** é a biblioteca de machine learning mais utilizada em Python. Construída sobre NumPy, SciPy e matplotlib, oferece uma API consistente e bem documentada para aprendizado supervisionado e não supervisionado.

### Filosofia da API

Toda transformação e modelo no Scikit-Learn segue o mesmo contrato:

| Método | Supervisão | Descrição |
|--------|-----------|-----------|
| `fit(X, y)` | Supervisionado | Treina o modelo |
| `fit(X)` | Não-supervisionado | Ajusta ao dado |
| `predict(X)` | Ambos | Gera predições |
| `transform(X)` | Ambos | Transforma dados |
| `fit_transform(X, y)` | Ambos | Fit + transform em um passo |
| `score(X, y)` | Supervisionado | Avalia performance |

Essa consistência permite compor pipelines complexos com poucas linhas.

---

## Pipeline de Machine Learning

Um pipeline típico no Scikit-Learn segue:

```
Dados Brutos → Limpeza → Split (Treino/Teste) → Preprocessing → Modelo → Validação → Deploy
```

Cada etapa tem suporte nativo na biblioteca.

### 1. Divisão Treino-Teste

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y  # stratify para classificação
)
```

- `test_size=0.2`: 80% treino, 20% teste
- `random_state`: garante reprodutibilidade
- `stratify`: mantém proporção das classes no split

### 2. Pré-processamento

Consulte [[skills/Data-Cleaning]] para detalhes sobre limpeza. Aqui, o foco é a integração com pipelines.

```python
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

# Definir transformações por tipo de coluna
numeric_features = ["idade", "salario", "tempo_casa"]
categorical_features = ["estado_civil", "escolaridade"]

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="constant", fill_value="desconhecido")),
    ("onehot", OneHotEncoder(drop="first", handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)
```

### 3. Modelos de Regressão

```python
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR

modelos_reg = {
    "Linear Regression": LinearRegression(),
    "Ridge (L2)": Ridge(alpha=1.0),
    "Lasso (L1)": Lasso(alpha=0.1),
    "Random Forest": RandomForestRegressor(n_estimators=100, max_depth=10),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, learning_rate=0.1),
    "SVR": SVR(kernel="rbf", C=100)
}

for nome, modelo in modelos_reg.items():
    modelo.fit(X_train, y_train)
    print(f"{nome}: R² = {modelo.score(X_test, y_test):.3f}")
```

**Quando usar cada um:**

| Modelo | Vantagem | Desvantagem |
|--------|----------|-------------|
| LinearRegression | Interpretável, rápido | Assume linearidade |
| Ridge/Lasso | Regularização, evita overfitting | Requer tuning de alpha |
| RandomForest | Não-linear, robusto a outliers | Pode overfitting, não extrapola |
| GradientBoosting | Alta precisão | Lento para treinar, muitos hiperparâmetros |
| SVR | Bom em alta dimensionalidade | Escolha de kernel crítica |

### 4. Modelos de Classificação

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

modelos_clf = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(max_depth=5),
    "Random Forest": RandomForestClassifier(n_estimators=100),
    "Gradient Boosting": GradientBoostingClassifier(n_estimators=100),
    "SVM": SVC(kernel="rbf", probability=True),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Naive Bayes": GaussianNB()
}

for nome, modelo in modelos_clf.items():
    modelo.fit(X_train, y_train)
    acc = modelo.score(X_test, y_test)
    print(f"{nome}: Acurácia = {acc:.3f}")
```

### 5. Clustering (Não-supervisionado)

```python
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture

# K-Means
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
labels = kmeans.fit_predict(X)

# DBSCAN (baseado em densidade, detecta outliers)
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X)

# Gaussian Mixture (probabilístico)
gmm = GaussianMixture(n_components=5, random_state=42)
labels = gmm.fit_predict(X)
probas = gmm.predict_proba(X)  # Probabilidade de pertencer a cada cluster
```

**Métricas de validação para clustering:**

```python
from sklearn.metrics import silhouette_score, calinski_harabasz_score

print(f"Silhouette: {silhouette_score(X, labels):.3f}")
print(f"Calinski-Harabasz: {calinski_harabasz_score(X, labels):.3f}")

# Método do cotovelo para K ótimo
inertias = []
for k in range(2, 15):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)
```

### 6. Redução de Dimensionalidade

```python
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# PCA (linear, preserva variância)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print(f"Variância explicada: {pca.explained_variance_ratio_.sum():.2%}")

# t-SNE (não-linear, preserva vizinhança)
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
X_tsne = tsne.fit_transform(X)
```

PCA é usado para compressão e pré-processamento. t-SNE é exclusivamente para visualização (não preserve distâncias globais).

---

## Validação e Avaliação

### Cross-Validation

```python
from sklearn.model_selection import cross_val_score, cross_validate

# K-Fold simples
scores = cross_val_score(modelo, X, y, cv=5, scoring="accuracy")
print(f"Acurácia média: {scores.mean():.3f} ± {scores.std():.3f}")

# K-Fold estratificado (mantém proporção de classes)
from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Cross-validate com múltiplas métricas
scoring = ["accuracy", "precision_macro", "recall_macro", "f1_macro"]
results = cross_validate(modelo, X, y, cv=5, scoring=scoring)
for metric, values in results.items():
    if metric.startswith("test_"):
        print(f"{metric}: {values.mean():.3f} ± {values.std():.3f}")
```

### Métricas de Classificação

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score, roc_curve
)

y_pred = modelo.predict(X_test)
y_prob = modelo.predict_proba(X_test)[:, 1]

print(classification_report(y_test, y_pred))

# Matriz de confusão
cm = confusion_matrix(y_test, y_pred)

# ROC-AUC
auc = roc_auc_score(y_test, y_prob)
print(f"AUC-ROC: {auc:.3f}")

# Curva ROC
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
```

### Métricas de Regressão

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_pred = modelo.predict(X_test)

print(f"MAE:  {mean_absolute_error(y_test, y_pred):.3f}")
print(f"RMSE: {mean_squared_error(y_test, y_pred, squared=False):.3f}")
print(f"R²:   {r2_score(y_test, y_pred):.3f}")
```

---

## Grid Search e Otimização de Hiperparâmetros

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from scipy.stats import randint, uniform

# Grid Search (exaustivo)
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [5, 10, 15, None],
    "min_samples_split": [2, 5, 10]
}

grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring="f1",
    n_jobs=-1,
    verbose=1
)
grid.fit(X_train, y_train)
print(f"Melhores params: {grid.best_params_}")
print(f"Melhor score: {grid.best_score_:.3f}")

# Randomized Search (mais eficiente)
param_dist = {
    "n_estimators": randint(50, 500),
    "max_depth": randint(3, 30),
    "min_samples_split": randint(2, 20)
}

random = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_dist,
    n_iter=50,
    cv=5,
    scoring="f1",
    n_jobs=-1,
    random_state=42
)
random.fit(X_train, y_train)
```

---

## Pipelines Completos

O `Pipeline` do Scikit-Learn encadeia transformações e modelo final:

```python
from sklearn.pipeline import Pipeline

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
])

# Treinar pipeline inteiro
pipeline.fit(X_train, y_train)

# Predizer
y_pred = pipeline.predict(X_test)

# Grid Search no pipeline
param_grid = {
    "classifier__n_estimators": [50, 100, 200],
    "classifier__max_depth": [5, 10, None],
    "preprocessor__num__imputer__strategy": ["mean", "median"]
}

grid = GridSearchCV(pipeline, param_grid, cv=5, scoring="f1")
```

---

## Conexões com o Vault

### Data Cleaning e Pré-processamento

O pré-processamento no Scikit-Learn depende de dados limpos. Consulte [[skills/Data-Cleaning]] para estratégias de imputação, tratamento de outliers e encoding — tudo pré-requisito para `ColumnTransformer`.

### Fundamentos Matemáticos

O Scikit-Learn implementa conceitos de:

- **Álgebra linear:** PCA decompõe autovetores da matriz de covariância. SVR usa transformações de kernel (espaços de Hilbert).
- **Probabilidade:** Naive Bayes é puro teorema de Bayes. Gaussian Mixture Models usam EM (Expectation-Maximization).
- **Otimização:** Gradient Boosting desce o gradiente no espaço de funções. SGD (Stochastic Gradient Descent) otimiza via gradiente estocástico.
- **Estatística:** Testes de hipótese em feature selection (`SelectKBest`, `f_classif`).

### Kaggle

O [[skills/Kaggle-Datasets]] é o melhor laboratório para praticar Scikit-Learn. Competições como Titanic, Housing Prices e Digit Recognizer são resolvidas quase inteiramente com Scikit-Learn.

### Produção

Para deploy de modelos Scikit-Learn em produção, veja [[data-engineering/etl-pipelines]] para serialização com `joblib` ou `pickle`, e [[devops/Observabilidade]] para monitoramento de drift.

---

## Boas Práticas

1. **Sempre use `Pipeline`.** Evita data leakage entre treino e teste.
2. **Escolha a métrica certa.** Acurácia é enganosa para classes desbalanceadas — prefira F1, precision/recall, ou AUC-ROC. Veja [[skills/Explainable-AI]] para interpretação.
3. **Validação cruzada sempre.** Um único split pode ser enganoso.
4. **Feature engineering > modelo complexo.** Dados bem preparados ganham de modelos sofisticados.
5. **Documente hiperparâmetros.** O modelo em produção precisa de parâmetros rastreáveis.
6. **Versionamento de modelos.** Use MLflow ou DVC para tracking.

---

## Referência Rápida de Algoritmos

| Tipo | Algoritmo | Quando usar |
|------|-----------|-------------|
| Regressão | `LinearRegression` | Relação linear, interpretável |
| Regressão | `Ridge` | Multicolinearidade |
| Regressão | `RandomForestRegressor` | Não-linear, muitas features |
| Classificação | `LogisticRegression` | Baseline binário |
| Classificação | `RandomForestClassifier` | Tabular, robusto |
| Classificação | `SVC` | Alta dimensionalidade |
| Classificação | `GradientBoostingClassifier` | Precisão máxima |
| Clustering | `KMeans` | Dados esféricos, K conhecido |
| Clustering | `DBSCAN` | Formas arbitrárias, outliers |
| Redução | `PCA` | Compressão linear |
| Redução | `TruncatedSVD` | Matrizes esparsas |

---

*Consulte também: [[skills/Data-Cleaning]], [[skills/Kaggle-Datasets]], [[skills/Explainable-AI]], [[data-engineering/etl-pipelines]], [[02-software-engineering/algorithms-data-structures]].*

[[skills/README|← Voltar à Taxonomia de Skills]]
