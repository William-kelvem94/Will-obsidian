---
title: "SHAP e LIME no COMPAS: Explicabilidade e Fairness"
area: "Tecnologia e Sociedade"
related: ["Viés Algorítmico", "Vigilância Algorítmica", "Ética de IA", "Transparência Algorítmica"]
tags: [conhecimento, tutorial, python, shap, lime, fairness, compas, machine-learning, explicabilidade, bias]
updated: 2026-05-18
aliases: ["Tutorial SHAP LIME", "Explicabilidade COMPAS", "Fairness ML Tutorial"]
---

# SHAP e LIME no COMPAS: Tutorial Prático de Explicabilidade e Fairness

## Visão Geral

Este tutorial ensina **na prática** como usar SHAP e LIME para explicar predições de machine learning, usando o dataset **COMPAS** (Correctional Offender Management Profiling for Alternative Sanctions). Você vai treinar um classificador, explicar suas decisões e avaliar métricas de公平 (fairness).

> **Por que COMPAS?** O COMPAS é um dos datasets mais estudados em _fairness_ e ética de ML. Foi alvo de uma investigação da *ProPublica* (2016) que revelou viés racial nas predições de reincidência. É o exemplo canônico de como um modelo pode ser acurado no geral, mas profundamente injusto para grupos minorizados.

```

```

---

## 1. Setup: Instalação e Imports

### 1.1 Instalação das Dependências

Execute no terminal ou em uma célula do notebook:

```python
# Instala pacotes principais
!pip install shap lime scikit-learn pandas numpy matplotlib seaborn

# Opcional: aif360 para datasets built-in e métricas de fairness
!pip install aif360

# Se for baixar o COMPAS do Kaggle, instale também:
# !pip install kagglehub
```

### 1.2 Imports

```python
"""
==============================================================================
IMPORTS — SHAP, LIME, sklearn, pandas, numpy, matplotlib
==============================================================================
"""

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sklearn — pipeline, modelo e métricas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score
)

# SHAP
import shap

# LIME
import lime
import lime.lime_tabular

# Ajustes de plotagem
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["font.size"] = 12
sns.set_style("whitegrid")

print("Todos os imports foram carregados com sucesso!")
```

```

```

---

## 2. Carregando o Dataset COMPAS

### 2.1 Opção A: Via aif360 (recomendado — mais simples)

```python
"""
==============================================================================
OPÇÃO A — Carregar COMPAS via aif360.datasets
==============================================================================
O aif360 (AI Fairness 360) da IBM inclui o COMPAS como dataset built-in.
"""

from aif360.datasets import CompasDataset

# Carrega o COMPAS já pré-processado
# protected_attribute: 'race' (0 = Caucasian, 1 = African-American)
compas = CompasDataset(
    protected_attribute_names=["race"],
    privileged_classes=[[1]],              # 1 = Caucasian
    features_to_drop=["age_cat", "c_charge_degree"]
)

# Converte para DataFrame para exploração
df = compas.convert_to_dataframe()[0]
df.rename(columns={"two_year_recid": "recidiva"}, inplace=True)

print(f"Shape: {df.shape}")
print(f"Colunas: {list(df.columns)}")
print(f"\nTarget (recidiva):\n{df['recidiva'].value_counts()}")
print(f"\nRaça:\n{df['race'].value_counts()}")
print(f"\nPrimeiras 5 linhas:\n{df.head()}")
```

### 2.2 Opção B: Download manual via URL direta

```python
"""
==============================================================================
OPÇÃO B — Download manual do CSV compas-scores-two-years.csv
==============================================================================
Caso o aif360 não funcione ou você queira os dados brutos.
"""

import urllib.request
import os

url = (
    "https://raw.githubusercontent.com/propublica/compas-analysis/"
    "master/compas-scores-two-years.csv"
)
filename = "compas-scores-two-years.csv"

if not os.path.exists(filename):
    print("Baixando COMPAS da ProPublica...")
    urllib.request.urlretrieve(url, filename)
    print("Download concluído!")
else:
    print("Arquivo já existe. Usando versão local.")

df_raw = pd.read_csv(filename)
print(f"Shape raw: {df_raw.shape}")
print(f"Colunas raw: {list(df_raw.columns[:20])}...")

# --- Pré-processamento básico (adaptado da ProPublica) ---

# Filtra casos válidos
df_raw = df_raw[df_raw["days_b_screening_arrest"].notna()]
df_raw = df_raw[df_raw["days_b_screening_arrest"].between(-30, 30)]
df_raw = df_raw[df_raw["is_recid"] != -1]
df_raw = df_raw[df_raw["c_charge_degree"] != "O"]

# Target: reincidência em 2 anos
df_raw["recidiva"] = (df_raw["two_year_recid"] == 1).astype(int)

# Features selecionadas (mesmo conjunto do estudo original)
features = [
    "age",                          # Idade
    "juv_fel_count",                # Ofensas juvenis (felony)
    "juv_misd_count",               # Ofensas juvenis (misdemeanor)
    "juv_other_count",              # Outras ofensas juvenis
    "priors_count",                 # Ofensas prévias (adulto)
    "c_charge_degree",              # Grau da ofensa (F/M)
    "sex",                          # Sexo
    "race",                         # Raça
]

df = df_raw[features + ["recidiva"]].copy()

# Codifica variáveis categóricas
df["c_charge_degree"] = (df["c_charge_degree"] == "F").astype(int)
df["sex"] = (df["sex"] == "Male").astype(int)
df["race"] = (df["race"] == "Caucasian").astype(int)

print(f"Shape processado: {df.shape}")
print(f"\nTarget:\n{df['recidiva'].value_counts()}")
print(f"\nInfo:\n{df.info()}")
print(f"\nPrimeiras 5 linhas:\n{df.head()}")
```

### 2.3 Opção C: Kaggle (via kagglehub)

```python
"""
==============================================================================
OPÇÃO C — Download via Kaggle Hub
==============================================================================
Se preferir baixar do Kaggle diretamente.
"""

# import kagglehub
# path = kagglehub.dataset_download("danofer/compass")
# df = pd.read_csv(f"{path}/compas-scores-two-years.csv")
# ... depois aplica o mesmo pré-processamento da Opção B
```

> **Escolha**: Recomendo a **Opção A (aif360)** por já vir pré-processada. Se falhar, use a **Opção B**.

```

```

---

## 3. Preparação dos Dados e Treinamento do Classificador

```python
"""
==============================================================================
SEPARAÇÃO TREINO/TESTE E TREINAMENTO
==============================================================================
Vamos treinar dois modelos:
  1. LogisticRegression (interpretável por natureza)
  2. RandomForest (caixa-preta, ideal para SHAP/LIME)

Isso permite comparar a explicação de um modelo simples vs. complexo.
"""

# --- Separa features e target ---
feature_cols = ["age", "juv_fel_count", "juv_misd_count", "juv_other_count",
                "priors_count", "c_charge_degree", "sex", "race"]
target_col = "recidiva"

X = df[feature_cols].values
y = df[target_col].values

# --- Split treino/teste (70/30) ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print(f"Treino: {X_train.shape[0]} amostras")
print(f"Teste:  {X_test.shape[0]} amostras")
print(f"Target train:\n{pd.Series(y_train).value_counts()}")
print(f"Target test:\n{pd.Series(y_test).value_counts()}")

# --- Padronização (importante para LogisticRegression) ---
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --- Modelo 1: Regressão Logística ---
print("\n--- Treinando LogisticRegression ---")
lr = LogisticRegression(C=1.0, max_iter=1000, random_state=42)
lr.fit(X_train_scaled, y_train)

y_pred_lr = lr.predict(X_test_scaled)
y_prob_lr = lr.predict_proba(X_test_scaled)[:, 1]

print(f"Acurácia:  {accuracy_score(y_test, y_pred_lr):.3f}")
print(f"AUC-ROC:   {roc_auc_score(y_test, y_prob_lr):.3f}")
print(f"F1-Score:  {f1_score(y_test, y_pred_lr):.3f}")
print(f"Precisão:  {precision_score(y_test, y_pred_lr):.3f}")
print(f"Recall:    {recall_score(y_test, y_pred_lr):.3f}")

# Coeficientes
print("\nCoeficientes da Regressão Logística:")
for nome, coef in zip(feature_cols, lr.coef_[0]):
    print(f"  {nome:20s}: {coef:+.4f}")

# --- Modelo 2: Random Forest ---
print("\n--- Treinando RandomForestClassifier ---")
rf = RandomForestClassifier(n_estimators=200, max_depth=10,
                            random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)  # RF não precisa de scaling

y_pred_rf = rf.predict(X_test)
y_prob_rf = rf.predict_proba(X_test)[:, 1]

print(f"Acurácia:  {accuracy_score(y_test, y_pred_rf):.3f}")
print(f"AUC-ROC:   {roc_auc_score(y_test, y_prob_rf):.3f}")
print(f"F1-Score:  {f1_score(y_test, y_pred_rf):.3f}")

print(f"\nFeature Importances (Random Forest):")
importancias = pd.DataFrame({
    "feature": feature_cols,
    "importancia": rf.feature_importances_
}).sort_values("importancia", ascending=False)
print(importancias.to_string(index=False))
```

```python
"""
==============================================================================
MATRIZ DE CONFUSÃO — Visualização
==============================================================================
"""

def plot_confusion_matrix(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=["Não reincidiu", "Reincidiu"],
                yticklabels=["Não reincidiu", "Reincidiu"])
    plt.title(title)
    plt.ylabel("Real")
    plt.xlabel("Predito")
    plt.show()

plot_confusion_matrix(y_test, y_pred_lr, "Matriz de Confusão — LogisticRegression")
plot_confusion_matrix(y_test, y_pred_rf, "Matriz de Confusão — RandomForest")
```

---

## 4. SHAP: Explicando as Predições

SHAP (SHapley Additive exPlanations) usa teoria dos jogos cooperativos para atribuir a cada feature uma contribuição para a predição. O valor SHAP de uma feature é a mudança esperada no output quando aquela feature é "incluída" no modelo.

### 4.1 Criando o Explainer SHAP

```python
"""
==============================================================================
SHAP — EXPLAINER
==============================================================================
O KernelExplainer funciona para qualquer modelo (model-agnostic).
O TreeExplainer é específico para modelos baseados em árvores (mais rápido).
"""

# Para LogisticRegression: usamos KernelExplainer
# (usa uma amostra do background para estimar valores SHAP)

# Amostra de background (100 pontos representativos)
background = shap.kmeans(X_train_scaled, k=50)

print("Criando KernelExplainer para LogisticRegression...")
shap_explainer_lr = shap.KernelExplainer(
    lr.predict_proba, background
)

# Para RandomForest: TreeExplainer (muito mais rápido)
print("Criando TreeExplainer para RandomForest...")
shap_explainer_rf = shap.TreeExplainer(rf)

print("Explainers criados!")
```

### 4.2 Calculando SHAP Values para o Conjunto de Teste

```python
"""
==============================================================================
CALCULANDO SHAP VALUES
==============================================================================
Calculamos SHAP para uma amostra pequena (50-100 pontos) para
não sobrecarregar o computador.
"""

# Amostra de 100 pontos do teste
X_test_sample = X_test[:100]
X_test_sample_scaled = X_test_scaled[:100]

# --- Logistic Regression ---
print("Calculando SHAP para LogisticRegression (pode levar alguns segundos)...")
shap_values_lr = shap_explainer_lr.shap_values(X_test_sample_scared)

# SHAP retorna uma lista: [SHAP para classe 0, SHAP para classe 1]
# Usamos shap_values_lr[1] para a classe "reincidiu" (classe 1)
shap_values_lr_class1 = shap_values_lr[1]

print(f"Shape dos SHAP values: {shap_values_lr_class1.shape}")

# --- Random Forest ---
print("Calculando SHAP para RandomForest...")
shap_values_rf = shap_explainer_rf.shap_values(X_test_sample)

# Para classificação binária, TreeExplainer retorna shape (n_amostras, n_features, n_classes)
shap_values_rf_class1 = shap_values_rf[:, :, 1]

print(f"Shape dos SHAP values RF: {shap_values_rf_class1.shape}")
```

### 4.3 Summary Plot (Feature Importance Global)

O **summary plot** mostra, para cada feature, a distribuição dos valores SHAP em todas as amostras. Features são ordenadas por importância.

```python
"""
==============================================================================
SHAP — SUMMARY PLOT
==============================================================================
Interpretação:
- Cada ponto = uma observação do dataset.
- Posição horizontal = valor SHAP (quanto mais à direita, mais a feature
  contribuiu para a predição de reincidência).
- Cor = valor da feature (vermelho = alto, azul = baixo).
- Largura da barra = densidade de pontos.

Para o LogisticRegression:
"""

print("=== SHAP SUMMARY PLOT — LogisticRegression ===")
shap.summary_plot(
    shap_values_lr_class1,
    X_test_sample_scaled,
    feature_names=feature_cols,
    show=False
)
plt.title("SHAP Summary Plot — LogisticRegression (classe: reincidiu)")
plt.tight_layout()
plt.show()

# Para o RandomForest:
print("\n=== SHAP SUMMARY PLOT — RandomForest ===")
shap.summary_plot(
    shap_values_rf_class1,
    X_test_sample,
    feature_names=feature_cols,
    show=False
)
plt.title("SHAP Summary Plot — RandomForest (classe: reincidiu)")
plt.tight_layout()
plt.show()
```

**Interpretação do Summary Plot:**

- **priors_count** (número de ofensas prévias) é geralmente a feature mais importante: mais ofensas prévias (cor vermelha) → SHAP positivo → maior probabilidade de reincidência.
- **age** é a segunda mais importante: quanto mais jovem (cor azul), maior a contribuição para reincidência; pessoas mais velhas contribuem negativamente (não reincidir).
- **race** (raça): veja se os pontos vermelhos (raça == 1, Caucasian) concentram-se à esquerda (contribuição negativa) e os azuis (raça == 0, African-American) à direita (contribuição positiva). **Isso é o viés racial!**
- **sex**: homens (sex == 1) tendem a ter SHAP positivo, contribuindo para reincidência.

### 4.4 Force Plot (Explicação de uma Predição Individual)

O **force plot** mostra como cada feature "empurra" a predição da base (valor esperado) para o valor predito.

```python
"""
==============================================================================
SHAP — FORCE PLOT
==============================================================================
Explica uma predição individual. Vamos escolher dois casos:
  1. Uma pessoa que o modelo previu como reincidente (probabilidade alta)
  2. Uma pessoa que o modelo previu como não reincidente (probabilidade baixa)
"""

# Índices de exemplo
idx_alto_risco = np.argmax(y_prob_rf[:100])    # maior prob prevista
idx_baixo_risco = np.argmin(y_prob_rf[:100])    # menor prob prevista

print(f"Índice alto risco: {idx_alto_risco}, prob = {y_prob_rf[idx_alto_risco]:.3f}")
print(f"Índice baixo risco: {idx_baixo_risco}, prob = {y_prob_rf[idx_baixo_risco]:.3f}")

# --- Force Plot para LogisticRegression ---
print("\n=== FORCE PLOT — LogisticRegression (Alto Risco) ===")
shap.force_plot(
    shap_explainer_lr.expected_value[1],
    shap_values_lr_class1[idx_alto_risco],
    X_test_sample_scaled[idx_alto_risco],
    feature_names=feature_cols,
    matplotlib=True,
    show=False
)
plt.title(f"Force Plot — LR (Alto Risco) — Prob: {y_prob_lr[idx_alto_risco]:.3f}")
plt.tight_layout()
plt.show()

print("\n=== FORCE PLOT — LogisticRegression (Baixo Risco) ===")
shap.force_plot(
    shap_explainer_lr.expected_value[1],
    shap_values_lr_class1[idx_baixo_risco],
    X_test_sample_scaled[idx_baixo_risco],
    feature_names=feature_cols,
    matplotlib=True,
    show=False
)
plt.title(f"Force Plot — LR (Baixo Risco) — Prob: {y_prob_lr[idx_baixo_risco]:.3f}")
plt.tight_layout()
plt.show()

# --- Force Plot para RandomForest ---
print("\n=== FORCE PLOT — RandomForest (Alto Risco) ===")
shap.force_plot(
    shap_explainer_rf.expected_value[1],
    shap_values_rf_class1[idx_alto_risco],
    X_test_sample[idx_alto_risco],
    feature_names=feature_cols,
    matplotlib=True,
    show=False
)
plt.title(f"Force Plot — RF (Alto Risco) — Prob: {y_prob_rf[idx_alto_risco]:.3f}")
plt.tight_layout()
plt.show()

print("\n=== FORCE PLOT — RandomForest (Baixo Risco) ===")
shap.force_plot(
    shap_explainer_rf.expected_value[1],
    shap_values_rf_class1[idx_baixo_risco],
    X_test_sample[idx_baixo_risco],
    feature_names=feature_cols,
    matplotlib=True,
    show=False
)
plt.title(f"Force Plot — RF (Baixo Risco) — Prob: {y_prob_rf[idx_baixo_risco]:.3f}")
plt.tight_layout()
plt.show()
```

**Interpretação do Force Plot:**

- O **valor base** (expected value) é a probabilidade média de reincidência no dataset (~45%).
- Features em **vermelho** empurram a predição *para cima* (aumentam a prob).
- Features em **azul** empurram *para baixo* (diminuem a prob).
- Quanto maior a barra, maior o impacto.

No caso de alto risco, você provavelmente verá:
- `priors_count` alto (vermelho) empurrando para direita.
- `age` baixo (azul) também empurrando para direita (jovens têm mais risco).
- Se a pessoa for African-American (`race=0`, representado como valor baixo → azul no force plot — **cuidado com a interpretação**: cor azul significa valor baixo da feature, mas se `race=0` for codificado como African-American, o SHAP pode mostrar contribuição positiva para reincidência mesmo sendo azul).

> **⚠️ Atenção**: A cor no force plot representa o *valor da feature* (alto/baixo), não a *direção do impacto*. Uma feature com valor baixo (azul) pode ter contribuição positiva. Isso é uma fonte comum de confusão.

### 4.5 Dependence Plot (Relação Feature-Predição)

O **dependence plot** mostra como o valor SHAP de uma feature varia com seu valor, revelando relações lineares ou não-lineares.

```python
"""
==============================================================================
SHAP — DEPENDENCE PLOT
==============================================================================
Mostra a relação entre o valor de uma feature e seu impacto (SHAP value).
Útil para detectar não-linearidades e interações.
"""

# Dependence plot para 'priors_count' (geralmente a feature mais importante)
print("=== DEPENDENCE PLOT — priors_count (RandomForest) ===")
shap.dependence_plot(
    "priors_count",
    shap_values_rf_class1,
    X_test_sample,
    feature_names=feature_cols,
    interaction_index="age",          # destaca interação com age
    show=False
)
plt.title("SHAP Dependence Plot — priors_count (interação: age)")
plt.tight_layout()
plt.show()

# Dependence plot para 'age'
print("\n=== DEPENDENCE PLOT — age (RandomForest) ===")
shap.dependence_plot(
    "age",
    shap_values_rf_class1,
    X_test_sample,
    feature_names=feature_cols,
    interaction_index="priors_count",
    show=False
)
plt.title("SHAP Dependence Plot — age (interação: priors_count)")
plt.tight_layout()
plt.show()

# Dependence plot para 'race' — CRÍTICO para análise de viés
print("\n=== DEPENDENCE PLOT — race (RandomForest) ===")
shap.dependence_plot(
    "race",
    shap_values_rf_class1,
    X_test_sample,
    feature_names=feature_cols,
    interaction_index="priors_count",
    show=False
)
plt.title("SHAP Dependence Plot — race (interação: priors_count)")
plt.tight_layout()
plt.show()
```

**Interpretação do Dependence Plot:**

- **priors_count**: relação crescente — quanto mais ofensas prévias, maior o SHAP value (maior contribuição para reincidência). A cor mostra interação com `age`: para jovens (azul), o impacto é ainda maior.
- **age**: relação negativa — quanto mais velho, menor o SHAP value. Jovens têm contribuição positiva para reincidência.
- **race**: **se o modelo for justo, a nuvem de pontos para `race=0` e `race=1` deveria estar centrada em SHAP=0**. Se os pontos de `race=0` (African-American) estiverem sistematicamente acima de zero, **o modelo está usando raça como preditor de reincidência** — o que é eticamente problemático.

> **📌 Nota**: No COMPAS original, a ProPublica mostrou que African-Americans recebiam scores de risco mais altos mesmo controlando por ofensas prévias e idade. O dependence plot de `race` revela visualmente esse viés.

### 4.6 Waterfall Plot (Alternativa Didática ao Force Plot)

```python
"""
==============================================================================
SHAP — WATERFALL PLOT (mais legível que force plot)
==============================================================================
"""

# Para um único caso
idx = 5  # escolha um índice
print(f"=== WATERFALL PLOT — RandomForest (caso {idx}) ===")

shap.waterfall_plot(
    shap.Explanation(
        values=shap_values_rf_class1[idx],
        base_values=shap_explainer_rf.expected_value[1],
        data=X_test_sample[idx],
        feature_names=feature_cols
    ),
    show=False
)
plt.title(f"Waterfall Plot — Caso {idx} (prob prevista: {y_prob_rf[idx]:.3f})")
plt.tight_layout()
plt.show()
```

---

## 5. LIME: Explicando uma Predição Individual

LIME (Local Interpretable Model-agnostic Explanations) cria um modelo linear simples **localmente** ao redor da predição que se quer explicar. Diferente do SHAP (que tem base teórica sólida em Shapley values), o LIME é mais heurístico, mas é mais intuitivo.

### 5.1 Criando o Explainer LIME

```python
"""
==============================================================================
LIME — EXPLAINER TABULAR
==============================================================================
O LimeTabularExplainer precisa dos dados de treino (não escalados)
para gerar perturbações realistas.
"""

# Cria explainer para LogisticRegression (usando dados escalados)
lime_explainer_lr = lime.lime_tabular.LimeTabularExplainer(
    X_train_scaled,
    feature_names=feature_cols,
    class_names=["Não reincidiu", "Reincidiu"],
    mode="classification",
    random_state=42
)

# Cria explainer para RandomForest (usando dados originais)
lime_explainer_rf = lime.lime_tabular.LimeTabularExplainer(
    X_train,
    feature_names=feature_cols,
    class_names=["Não reincidiu", "Reincidiu"],
    mode="classification",
    random_state=42
)

print("Explainers LIME criados!")
```

### 5.2 Explicando um Caso com LIME

```python
"""
==============================================================================
LIME — EXPLICAÇÃO DE UM CASO INDIVIDUAL
==============================================================================
"""

# Escolhe um caso do teste
idx = 10
print(f"Explicando caso {idx} com LIME")
print(f"Valores reais: {dict(zip(feature_cols, X_test[idx]))}")
print(f"Classe real: {y_test[idx]} ('Reincidiu' se 1)")
print(f"Probabilidade LR: {y_prob_lr[idx]:.3f}")
print(f"Probabilidade RF: {y_prob_rf[idx]:.3f}")

# --- Explicação para LogisticRegression ---
print("\n=== LIME — LogisticRegression ===")
exp_lr = lime_explainer_lr.explain_instance(
    X_test_scaled[idx],
    lr.predict_proba,
    num_features=len(feature_cols)
)

# Mostra a explicação (formatada)
exp_lr.show_in_notebook(show_table=True)

# Também mostra como texto
print("\nExplicação em texto:")
print(exp_lr.as_list())

# --- Explicação para RandomForest ---
print("\n=== LIME — RandomForest ===")
exp_rf = lime_explainer_rf.explain_instance(
    X_test[idx],
    rf.predict_proba,
    num_features=len(feature_cols)
)

exp_rf.show_in_notebook(show_table=True)

print("\nExplicação em texto:")
print(exp_rf.as_list())
```

### 5.3 Visualizando a Explicação LIME

```python
"""
==============================================================================
LIME — GRÁFICO DE BARRAS
==============================================================================
Mostra o peso de cada feature na decisão local.
"""

# LogisticRegression
fig_lr = exp_lr.as_pyplot_figure()
plt.title("LIME — LogisticRegression (pesos locais)")
plt.tight_layout()
plt.show()

# RandomForest
fig_rf = exp_rf.as_pyplot_figure()
plt.title("LIME — RandomForest (pesos locais)")
plt.tight_layout()
plt.show()
```

**Interpretação do LIME:**

- Cada barra mostra o peso (positivo ou negativo) que a feature teve na predição.
- **Verde = contribuiu para a classe positiva** (reincidiu).
- **Vermelho = contribuiu para a classe negativa** (não reincidiu).
- Diferente do SHAP, o LIME mostra explicitamente faixas de valores: por exemplo, `priors_count > 3` contribui para reincidência, enquanto `age > 45` contribui contra.

**Exemplo de saída LIME**:
```
[(priors_count > 3.00, 0.25),
 (age <= 25.00, 0.18),
 (race <= 0.00, 0.12),    # race=0 = African-American → contribui para reincidência
 (juv_fel_count <= 0.00, -0.08), ...]
```

Isso lê-se como:
- Ter mais de 3 ofensas prévias aumenta a probabilidade em ~25 pontos percentuais.
- Ter idade <= 25 anos aumenta em ~18 pp.
- Ser African-American (`race=0`) aumenta em ~12 pp — **viés explícito**.
- Não ter ofensas juvenis reduz a probabilidade em ~8 pp.

> **⚠️ Limitação do LIME**: As explicações podem ser instáveis (pequenas variações nos dados geram explicações diferentes). SHAP é mais estável e teoricamente fundamentado.

### 5.4 Comparando SHAP vs. LIME para o Mesmo Caso

```python
"""
==============================================================================
COMPARAÇÃO DIRETA — SHAP vs. LIME no mesmo caso
==============================================================================
"""

idx_comp = 15

# SHAP values para este caso (RandomForest)
shap_val = shap_values_rf_class1[idx_comp]

# LIME para o mesmo caso
exp = lime_explainer_rf.explain_instance(
    X_test[idx_comp], rf.predict_proba, num_features=len(feature_cols)
)

print(f"=== COMPARAÇÃO SHAP vs. LIME — Caso {idx_comp} ===")
print(f"Classe real: {y_test[idx_comp]}")
print(f"Prob predita RF: {y_prob_rf[idx_comp]:.3f}")
print()

print(f"{'Feature':20s} {'Valor':8s} {'SHAP':8s} {'LIME':8s}")
print("-" * 44)
for i, nome in enumerate(feature_cols):
    lime_weight = dict(exp.as_list()).get(nome, 0)
    print(f"{nome:20s} {X_test[idx_comp][i]:8.2f} "
          f"{shap_val[i]:+8.4f} {lime_weight:+8.4f}")
```

---

## 6. Métricas de Fairness

Fairness (equidade) em ML não tem uma definição única. Existem dezenas de métricas, muitas vezes conflitantes entre si (é matematicamente impossível satisfazer todas simultaneamente). Vamos calcular as mais comuns.

```python
"""
==============================================================================
MÉTRICAS DE FAIRNESS — DISPARATE IMPACT, EQUAL OPPORTUNITY
==============================================================================
Usando o grupo protegido 'race' (0 = African-American, 1 = Caucasian).

Métricas:
  1. Disparate Impact Ratio (DIR): razão entre taxas de predição positiva
     para o grupo desprivilegiado vs. privilegiado.
     - Ideal: > 0.80 (regra dos 80% do EEOC/USA)
     - Se DIR < 0.80, o modelo tem impacto adverso.

  2. Equal Opportunity Difference (EOD): diferença na True Positive Rate
     (recall) entre grupos.
     - Ideal: 0 (igualdade de oportunidades).
     - Se EOD > 0, o grupo privilegiado tem mais verdadeiros positivos.

  3. Predictive Parity: diferença na precisão entre grupos.
"""

# --- Separa predições por grupo ---
mask_privileged = (X_test[:, feature_cols.index("race")] == 1)  # Caucasian
mask_unprivileged = (X_test[:, feature_cols.index("race")] == 0)  # African-American

print("=== GRUPOS PROTEGIDOS ===")
print(f"Privilegiados (Caucasian): {mask_privileged.sum()} amostras")
print(f"Não-privilegiados (African-American): {mask_unprivileged.sum()} amostras")

# --- Para LogisticRegression ---
print("\n--- LogisticRegression ---")

y_pred_lr_test = lr.predict(X_test_scaled)
y_prob_lr_test = lr.predict_proba(X_test_scaled)[:, 1]

# 1. Disparate Impact Ratio (DIR)
pred_pos_priv = y_pred_lr_test[mask_privileged].mean()
pred_pos_unpriv = y_pred_lr_test[mask_unprivileged].mean()
dir_lr = pred_pos_unpriv / pred_pos_priv if pred_pos_priv > 0 else np.inf

print(f"\n1. Disparate Impact Ratio (DIR): {dir_lr:.4f}")
print(f"   Tx pred. positiva (Caucasian):       {pred_pos_priv:.3f}")
print(f"   Tx pred. positiva (African-American): {pred_pos_unpriv:.3f}")
print(f"   Regra dos 80%: {'PASSOU' if dir_lr >= 0.80 else 'FALHOU'} "
      f"(DIR >= 0.80: {dir_lr >= 0.80})")

# 2. Equal Opportunity Difference (EOD)
# TPR = recall = TP / (TP + FN)
y_true_priv = y_test[mask_privileged]
y_true_unpriv = y_test[mask_unprivileged]
y_pred_priv = y_pred_lr_test[mask_privileged]
y_pred_unpriv = y_pred_lr_test[mask_unprivileged]

tpr_priv = recall_score(y_true_priv, y_pred_priv) if y_true_priv.sum() > 0 else 0
tpr_unpriv = recall_score(y_true_unpriv, y_pred_unpriv) if y_true_unpriv.sum() > 0 else 0
eod_lr = tpr_priv - tpr_unpriv

print(f"\n2. Equal Opportunity Difference (EOD): {eod_lr:.4f}")
print(f"   TPR (Caucasian):       {tpr_priv:.3f}")
print(f"   TPR (African-American): {tpr_unpriv:.3f}")
print(f"   Ideal: 0. | Diferença: {abs(eod_lr):.3f}")

# 3. Predictive Parity (diferença na precisão)
prec_priv = precision_score(y_true_priv, y_pred_priv, zero_division=0)
prec_unpriv = precision_score(y_true_unpriv, y_pred_unpriv, zero_division=0)
pp_lr = prec_priv - prec_unpriv

print(f"\n3. Predictive Parity Difference: {pp_lr:.4f}")
print(f"   Precisão (Caucasian):       {prec_priv:.3f}")
print(f"   Precisão (African-American): {prec_unpriv:.3f}")

# --- Para RandomForest ---
print("\n--- RandomForest ---")

y_pred_rf_test = rf.predict(X_test)
y_prob_rf_test = rf.predict_proba(X_test)[:, 1]

# 1. DIR
pred_pos_priv_rf = y_pred_rf_test[mask_privileged].mean()
pred_pos_unpriv_rf = y_pred_rf_test[mask_unprivileged].mean()
dir_rf = pred_pos_unpriv_rf / pred_pos_priv_rf if pred_pos_priv_rf > 0 else np.inf

print(f"\n1. Disparate Impact Ratio (DIR): {dir_rf:.4f}")
print(f"   Regra dos 80%: {'PASSOU' if dir_rf >= 0.80 else 'FALHOU'}")

# 2. EOD
y_pred_rf_priv = y_pred_rf_test[mask_privileged]
y_pred_rf_unpriv = y_pred_rf_test[mask_unprivileged]

tpr_priv_rf = recall_score(y_true_priv, y_pred_rf_priv) if y_true_priv.sum() > 0 else 0
tpr_unpriv_rf = recall_score(y_true_unpriv, y_pred_rf_unpriv) if y_true_unpriv.sum() > 0 else 0
eod_rf = tpr_priv_rf - tpr_unpriv_rf

print(f"\n2. Equal Opportunity Difference (EOD): {eod_rf:.4f}")
print(f"   TPR (Caucasian):       {tpr_priv_rf:.3f}")
print(f"   TPR (African-American): {tpr_unpriv_rf:.3f}")

# 3. Predictive Parity
prec_priv_rf = precision_score(y_true_priv, y_pred_rf_priv, zero_division=0)
prec_unpriv_rf = precision_score(y_true_unpriv, y_pred_rf_unpriv, zero_division=0)
print(f"\n3. Predictive Parity Difference: {prec_priv_rf - prec_unpriv_rf:.4f}")

# --- Tabela resumo ---
print("\n" + "=" * 60)
print("RESUMO DAS MÉTRICAS DE FAIRNESS")
print("=" * 60)
resumo = pd.DataFrame({
    "Métrica": [
        "Disparate Impact (DIR)",
        "Equal Opportunity Diff (EOD)",
        "Predictive Parity Diff"
    ],
    "LogisticRegression": [f"{dir_lr:.3f}", f"{eod_lr:.3f}",
                           f"{prec_priv - prec_unpriv:.3f}"],
    "RandomForest": [f"{dir_rf:.3f}", f"{eod_rf:.3f}",
                     f"{prec_priv_rf - prec_unpriv_rf:.3f}"],
    "Ideal": [">= 0.80", "0.00", "0.00"]
})
print(resumo.to_string(index=False))
```

### Interpretação das Métricas de Fairness

**Disparate Impact (DIR):**
- Mede *desigualdade de outcomes*: o modelo prediz reincidência para African-Americans numa taxa diferente da de Caucasians?
- **Se DIR < 0.80**: o modelo tem *adverse impact* — está penalizando o grupo não-privilegiado.
- No COMPAS, DIR costuma ficar entre **0.60–0.75** — indicando que African-Americans são classificados como reincidentes com mais frequência.

**Equal Opportunity Difference (EOD):**
- Mede *desigualdade de acertos*: o modelo identifica corretamente reincidentes reais com a mesma taxa para ambos os grupos?
- **Se EOD > 0**: o modelo é melhor para Caucasians (mais verdadeiros positivos).
- No COMPAS, o modelo tipicamente tem **maior TPR para African-Americans**, o que soa contra-intuitivo: significa que African-American reincidentes são *mais corretamente identificados*. Mas o problema é que African-American *não-reincidentes* também são mais frequentemente classificados como reincidentes (falsos positivos).

**Trade-off entre métricas:**
- Não é possível maximizar DIR e EOD simultaneamente (Kleinberg et al., 2017).
- A escolha de qual métrica priorizar é uma **decisão ética e política**, não técnica.

> **Leitura recomendada**: Barocas, Hardt & Narayanan (2019). *Fairness and Machine Learning: Limitations and Opportunities*. Disponível em: https://fairmlbook.org

---

## 7. Discussão dos Resultados

### 7.1 O que SHAP e LIME Revelam sobre Viés?

**SHAP Summary Plot:**
- `race` aparece como uma das features mais importantes no modelo.
- Para African-American (`race=0`), o SHAP value é tipicamente positivo (contribui para reincidência).
- Isso significa que o modelo **aprendeu a usar raça como preditor**, mesmo que indiretamente (via correlações com outras features como priors_count e c_charge_degree).

**SHAP Dependence Plot (race):**
- Mostra que, mesmo controlando por `priors_count`, African-Americans têm SHAP values sistematicamente mais altos.
- Isso é consistente com a descoberta da ProPublica: African-Americans recebem scores de risco mais altos mesmo quando têm o mesmo histórico criminal que Caucasians.

**LIME para casos individuais:**
- Em casos onde `race=0`, o LIME frequentemente lista `race <= 0.00` como um fator que contribui para a predição de reincidência.
- Isso é explícito e preocupante: o modelo está usando raça na tomada de decisão.

### 7.2 Como as Métricas de Fairness se Comportam?

| Métrica | Resultado Típico | Interpretação |
|---------|------------------|---------------|
| DIR | 0.60–0.75 (FALHA) | African-Americans recebem predição positiva com mais frequência |
| EOD | 0.05–0.15 | TPR ligeiramente maior para African-Americans |
| Predictive Parity | 0.05–0.15 | Precisão menor para African-Americans (mais falsos positivos) |

**O problema central do COMPAS:** O modelo tem **falsos positivos desproporcionais** para African-Americans. Ou seja: pessoas que *não* vão reincidir são classificadas erroneamente como reincidentes com mais frequência se forem African-American.

**Consequência prática:** No sistema judicial, um falso positivo significa que uma pessoa pode ser presa preventivamente, ter a fiança negada ou receber uma sentença mais severa com base em uma predição incorreta — e isso acontece desproporcionalmente com pessoas negras.

### 7.3 Limitações da Análise

1. **Correlação não é causalidade**: SHAP e LIME mostram correlações, não causalidade. O fato de `race` ter SHAP alto não significa que o modelo seja racista no sentido intencional — mas o *efeito* é discriminatório.
2. **Definição de fairness contestável**: Diferentes definições de fairness levam a conclusões diferentes. Um modelo pode ser "justo" segundo uma métrica e injusto segundo outra.
3. **Dados históricos enviesados**: O COMPAS foi treinado em dados do sistema judicial, que já é enviesado. O modelo apenas reproduz (e amplifica) esses vieses.
4. **Explicabilidade não resolve fairness**: Explicar uma decisão enviesada não torna a decisão justa. É um passo necessário mas insuficiente.

---

## 8. Erros Comuns e Troubleshooting

### Erro 1: `ImportError: No module named 'shap'`

```bash
pip install shap
```

Se persistir, instale em ambiente virtual ou reinicie o kernel.

### Erro 2: `KernelExplainer` muito lento

```python
# Reduza o background dataset
background = shap.kmeans(X_train, k=20)

# OU use uma amostra aleatória
background = shap.sample(X_train, 50)
```

### Erro 3: `TreeExplainer` requer xgboost, lightgbm ou sklearn

```python
# Para RandomForest do sklearn, funciona direto:
explainer = shap.TreeExplainer(rf)
# Para xgboost:
# import xgboost; model = xgboost.XGBClassifier(); explainer = shap.TreeExplainer(model)
```

### Erro 4: LIME mostra pesos inconsistentes entre execuções

```python
# Use random_state para reprodutibilidade:
exp = lime_explainer.explain_instance(
    X_test[idx], model.predict_proba,
    num_features=5, random_state=42
)
```

### Erro 5: `aif360` não instala ou dá erro

```bash
# Tente:
pip install aif360[COMPAS]
# OU instale manualmente os requisitos:
pip install numpy scipy pandas scikit-learn
```

### Erro 6: matplotlib não mostra os plots (Jupyter/VS Code)

```python
# No Jupyter:
%matplotlib inline

# No VS Code Python Interactive:
# plt.show() já deve funcionar
```

### Erro 7: SHAP force plot não aparece (output estático)

```python
# Use matplotlib=True para forçar output estático:
shap.force_plot(..., matplotlib=True)
```

---

## 9. Datasets Alternativos para Praticar

### 9.1 Adult Income (Census Income)

- **Problema**: Predizer se renda > $50K/ano.
- **Grupo protegido**: raça, gênero.
- **Onde encontrar**: `aif360.datasets.AdultDataset`, `sklearn.datasets.fetch_openml("adult")`, Kaggle.
- **Por que é bom para prática**: Dataset limpo, bem documentado, viés de gênero e raça bem estudado.

```python
from aif360.datasets import AdultDataset
adult = AdultDataset()
```

### 9.2 German Credit

- **Problema**: Classificar risco de crédito (bom/mau).
- **Grupo protegido**: idade, gênero, status estrangeiro.
- **Onde encontrar**: `aif360.datasets.GermanDataset`, UCI, Kaggle.
- **Por que é bom**: Dataset pequeno (1000 linhas), rápido para treinar e explicar.

```python
from aif360.datasets import GermanDataset
german = GermanDataset()
```

### 9.3 COMPAS (versões diferentes)

- **Problema**: Mesmo COMPAS, mas com diferentes pré-processamentos.
- **Onde encontrar**: `aif360.datasets.CompasDataset` tem parâmetros adicionais.
- **Por que explorar**: Diferentes escolhas de pré-processamento levam a diferentes conclusões sobre viés.

### 9.4 Bank Marketing (UCI)

- **Problema**: Predizer se cliente vai fazer depósito a prazo.
- **Grupo protegido**: idade, estado civil.
- **Onde encontrar**: UCI, Kaggle, `sklearn.datasets.fetch_openml("bank-marketing")`.

### 9.5 ProPublica e Open Police

- Dados reais de policiamento e sistema criminal.
- Mais sujos, mas mais realistas para análise de viés sistêmico.

### 9.6 Synthetic Fairness Datasets

Use o `aif360.datasets.BankDataset` ou gere dados sintéticos com correlações artificiais para testar diferentes métricas de fairness.

---

## 10. Adaptando o Tutorial para Diferentes Modelos

### 10.1 XGBoost / LightGBM

```python
import xgboost as xgb

xgb_model = xgb.XGBClassifier(n_estimators=100, max_depth=6, random_state=42)
xgb_model.fit(X_train, y_train)

# SHAP TreeExplainer funciona diretamente
shap_explainer_xgb = shap.TreeExplainer(xgb_model)
shap_values_xgb = shap_explainer_xgb.shap_values(X_test[:100])

# LIME
lime_explainer_xgb = lime.lime_tabular.LimeTabularExplainer(
    X_train, feature_names=feature_cols,
    class_names=["Não reincidiu", "Reincidiu"], mode="classification"
)
```

### 10.2 Redes Neurais (Keras/TensorFlow)

```python
from tensorflow import keras

# Modelo simples
nn_model = keras.Sequential([
    keras.layers.Dense(16, activation="relu", input_shape=(X_train.shape[1],)),
    keras.layers.Dense(8, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")
])
nn_model.compile(optimizer="adam", loss="binary_crossentropy")
nn_model.fit(X_train_scaled, y_train, epochs=20, batch_size=32, verbose=0)

# SHAP com GradientExplainer (para modelos diferenciáveis)
shap_explainer_nn = shap.GradientExplainer(nn_model, X_train_scaled[:100])
shap_values_nn = shap_explainer_nn.shap_values(X_test_scaled[:100])

# LIME
lime_explainer_nn = lime.lime_tabular.LimeTabularExplainer(
    X_train_scaled, feature_names=feature_cols,
    class_names=["Não reincidiu", "Reincidiu"], mode="classification"
)
exp_nn = lime_explainer_nn.explain_instance(
    X_test_scaled[0], nn_model.predict, num_features=5
)
```

### 10.3 SVM

```python
from sklearn.svm import SVC

svm_model = SVC(kernel="rbf", probability=True, random_state=42)
svm_model.fit(X_train_scaled, y_train)

# SHAP com KernelExplainer (model-agnostic, lento)
background_svm = shap.kmeans(X_train_scaled, k=20)
shap_explainer_svm = shap.KernelExplainer(svm_model.predict_proba, background_svm)
shap_values_svm = shap_explainer_svm.shap_values(X_test_scaled[:50])
```

### 10.4 Dicas Gerais de Adaptação

| Modelo | SHAP Explainer | Velocidade | Observação |
|--------|---------------|------------|------------|
| LogisticRegression | `KernelExplainer` | Lento | Use `kmeans` para background |
| DecisionTree/RF | `TreeExplainer` | Rápido | É o mais eficiente |
| XGBoost/LightGBM | `TreeExplainer` | Rápido | Suporte built-in |
| Redes Neurais | `GradientExplainer` | Médio | Aproxima SHAP via gradientes |
| SVM / KNN | `KernelExplainer` | Lento | Precisa de background pequeno |
| Qualquer modelo | `KernelExplainer` | Lento | Fallback universal |

---

## 11. Conclusão e Próximos Passos

### O que você aprendeu

1. **Carregar e pré-processar** o dataset COMPAS (via aif360 ou raw da ProPublica).
2. **Treinar classificadores** (LogisticRegression e RandomForest) para predizer reincidência.
3. **Aplicar SHAP** (summary plot, force plot, dependence plot) para explicar predições global e localmente.
4. **Aplicar LIME** para explicações locais e comparar com SHAP.
5. **Calcular métricas de fairness** (Disparate Impact, Equal Opportunity, Predictive Parity).
6. **Interpretar os resultados** à luz do debate sobre viés algorítmico no sistema judicial.

### Próximos Passos Sugeridos

1. **Técnicos**:
   - Implementar técnicas de *debiasing*: reweighting, adversarial debiasing, fairness constraints.
   - Usar `aif360` para aplicar algoritmos de mitigação de viés (pré-processamento, em-processamento, pós-processamento).
   - Testar com diferentes definições de fairness (demographic parity, equalized odds, etc.).

2. **Críticos**:
   - Ler o artigo original da ProPublica: "Machine Bias" (Angwin et al., 2016).
   - Estudar o debate sobre COMPAS: Northpointe (criador do COMPAS) contestou a metodologia da ProPublica.
   - Refletir: *é possível ter um modelo de risco criminal justo? Ou o problema é o próprio uso de ML no sistema judicial?*

3. **Práticos**:
   - Aplicar o mesmo pipeline a outros datasets (Adult, German Credit).
   - Construir um dashboard interativo com `shap` e `plotly` para explorar explicações.
   - Escrever um relatório de auditoria de fairness para um modelo real.

### Referências

- Lundberg, S. M., & Lee, S.-I. (2017). "A Unified Approach to Interpreting Model Predictions." *NeurIPS*.
- Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "Why Should I Trust You?": Explaining the Predictions of Any Classifier." *KDD*.
- Angwin, J., Larson, J., Mattu, S., & Kirchner, L. (2016). "Machine Bias." *ProPublica*.
- Barocas, S., Hardt, M., & Narayanan, A. (2019). *Fairness and Machine Learning*. fairmlbook.org.
- Bellamy, R. K. E., et al. (2019). "AI Fairness 360: An Extensible Toolkit for Fairness." *IBM Journal of Research and Development*.
- Kleinberg, J., Mullainathan, S., & Raghavan, M. (2017). "Inherent Trade-Offs in the Fair Determination of Risk Scores." *ITCS*.

---

*Tutorial criado em 2026-05-18. Parte do vault de conhecimento de Tecnologia e Sociedade.*

**Tags:** `#shap` `#lime` `#fairness` `#compas` `#explicabilidade` `#ml` `#tutorial` `#python`

[[Conhecimento-Geral/Tecnologia-e-Sociedade/INDEX|← Voltar ao índice de Tecnologia e Sociedade]]
