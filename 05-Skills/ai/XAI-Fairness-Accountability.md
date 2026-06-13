---
title: "Explainable AI (XAI), Fairness e Accountability — Expansão Completa"
date: 2026-06-01
tags: [skills]
updated: 2026-06-13
---

# Explainable AI (XAI), Fairness e Accountability — Expansão Completa

## Índice
1. [Introdução Aprofundada](#1-introdução-aprofundada)
2. [Fundamentos Teóricos da XAI](#2-fundamentos-teóricos-da-xai)
3. [Estudo de Caso Completo: COMPAS e a ProPublica](#3-estudo-de-caso-completo-compas-e-a-propublica)
4. [Tutorial Prático: SHAP + LIME + COMPAS (Python)](#4-tutorial-prático-shap--lime--compas-python)
5. [Métricas de Fairness — Código e Interpretação](#5-métricas-de-fairness--código-e-interpretação)
6. [Benchmarks e Datasets Públicos](#6-benchmarks-e-datasets-públicos)
7. [Discussão Crítica: Limites, Controvérsias e Dilemas](#7-discussão-crítica-limites-controvérsias-e-dilemas)
8. [Cross-Mapping: XAI e Outros Domínios](#8-cross-mapping-xai-e-outros-domínios)
9. [Papers, Laboratórios, Comunidades e Onde Acompanhar](#9-papers-laboratórios-comunidades-e-onde-acompanhar)
10. [Exercícios Resolvidos e Propostos](#10-exercícios-resolvidos-e-propostos)
11. [Referências Completas](#11-referências-completas)

---

## 1. Introdução Aprofundada

### 1.1 O Problema da Caixa-Preta

Modelos de machine learning modernos — especialmente deep learning, ensembles (Random Forest, XGBoost) e Large Language Models — atingem acurácia impressionante à custa de interpretabilidade. Um modelo pode ter 99% de acurácia em um dataset de crédito, mas se não pudermos explicar *por que* um cliente específico foi negado, enfrentamos problemas éticos, legais e operacionais.

**A XAI (Explainable Artificial Intelligence)** surge como campo de pesquisa que desenvolve métodos para tornar decisões de modelos compreensíveis para humanos. Não se trata apenas de satisfazer curiosidade: é um requisito para:
- **Conformidade regulatória**: AI Act Europeu (Art. 13, 14, 86), GDPR (Art. 15, 22)
- **Auditabilidade**: verificar se o modelo discrimina grupos protegidos
- **Depuração técnica**: identificar falhas, overfitting, artefatos espúrios
- **Confiança do usuário**: especialmente em domínios de alto risco (saúde, justiça, crédito)

### 1.2 Três Pilares Inseparáveis

| Pilar | Definição | Pergunta Central |
|-------|-----------|------------------|
| **XAI (Explainability)** | Capacidade de fornecer explicações inteligíveis sobre decisões do modelo | *Por que o modelo decidiu X?* |
| **Fairness** | Ausência de viés sistemático contra grupos protegidos por atributos sensíveis (raça, gênero, idade, etc.) | *O modelo trata todos os grupos de forma justa?* |
| **Accountability** | Possibilidade de atribuir responsabilidade por decisões do sistema a pessoas ou organizações | *Quem responde por esta decisão?* |

Estes três pilares são interdependentes: sem XAI não é possível auditar fairness; sem accountability não há incentivo para implementar XAI e fairness.

### 1.3 Taxonomia dos Métodos XAI

```
XAI
├── Métodos Intrínsecos (white-box)
│   ├── Árvores de Decisão
│   ├── Regressão Linear/Logística
│   ├── Modelos Additivos Generalizados (GAMs/EBMs)
│   └── Rule Lists (CORELS)
│
└── Métodos Post-Hoc (black-box)
    ├── Locais
    │   ├── LIME (Local Interpretable Model-agnostic Explanations)
    │   ├── SHAP (SHapley Additive exPlanations)
    │   ├── Contrafactuais (DiCE, Alibi)
    │   └── Grad-CAM (visão computacional)
    │
    └── Globais
        ├── Importância de Features (Permutation Importance)
        ├── Partial Dependence Plots (PDP)
        ├── Accumulated Local Effects (ALE)
        └── Interpretabilidade Mecanicista (LLMs)
```

---

## 2. Fundamentos Teóricos da XAI

### 2.1 SHAP — SHapley Additive exPlanations

**Base teórica:** SHAP fundamenta-se nos valores de Shapley da teoria dos jogos cooperativos (Shapley, 1953). Cada feature é um "jogador" que contribui para a "recompensa" (predição). O valor de Shapley de uma feature é a média de sua contribuição marginal sobre todas as possíveis ordenações das features.

**Propriedades desejáveis (único método que as satisfaz):**
1. **Eficiência**: A soma dos SHAP values de todas as features + valor base = predição
2. **Simetria**: Se duas features contribuem igualmente, seus SHAP values são iguais
3. **Dummy**: Se uma feature não altera a predição, seu SHAP value é zero
4. **Aditividade**: SHAP values de modelos ensemble são a soma dos SHAP values dos modelos base

**Tipos de Explainer:**
- `TreeExplainer`: para modelos baseados em árvores (rápido, exato)
- `KernelExplainer`: model-agnostic (genérico, lento)
- `DeepExplainer`: para redes neurais (aproximado via DeepLIFT)
- `LinearExplainer`: para modelos lineares

### 2.2 LIME — Local Interpretable Model-agnostic Explanations

**Base teórica:** LIME aproxima localmente o modelo complexo por um modelo interpretável (geralmente regressão linear ou Lasso) na vizinhança da instância a ser explicada.

**Processo:**
1. Gera amostras perturbadas ao redor da instância original
2. Calcula a distância das amostras ao ponto original (kernel exponencial)
3. Obtém predições do modelo black-box para cada amostra
4. Treina um modelo linear ponderado pelas distâncias

**Limitação fundamental:** O modelo linear local é apenas uma aproximação — se a fronteira de decisão for muito não linear na vizinhança, a explicação pode ser infiel.

### 2.3 Comparativo SHAP vs LIME

| Aspecto | SHAP | LIME |
|---------|------|------|
| Fundamento | Teoria dos jogos (Shapley Values) | Modelo linear local |
| Escopo | Local e Global | Local apenas |
| Consistência | Sim (monotonicidade garantida) | Não (pode variar entre execuções) |
| Estabilidade | Alta (determinístico para TreeExplainer) | Baixa (semente aleatória influencia) |
| Complexidade | O(2^n_features) (KernelExplainer) | O(n_samples * n_features) |
| Interpretação | Contribuição para predição (escala original) | Peso no modelo linear local |
| Quando usar | Rigor teórico, pesquisa, modelos tree-based | Explicações rápidas, texto/imagem |

---

## 3. Estudo de Caso Completo: COMPAS e a ProPublica

### 3.1 Contexto

O **COMPAS** (Correctional Offender Management Profiling for Alternative Sanctions) é um algoritmo comercial desenvolvido pela Northpointe (atualmente Equivant), usado por tribunais nos EUA para avaliar probabilidade de reincidência de réus. Em 2016, a **ProPublica** publicou uma investigação que se tornou o case mais emblemático de viés algorítmico da história.

### 3.2 Metodologia da ProPublica

1. **Aquisição dos dados:** Solicitação de registros públicos ao xerife do Condado de Broward, Flórida
2. **Período:** Réus avaliados entre 2013 e 2014
3. **Acompanhamento:** 2 anos após a avaliação (até abril de 2016)
4. **Cross-match:** Nome + sobrenome + data de nascimento para cruzar COMPAS com registros criminais (~80.000 registros baixados)
5. **Modelagem:** Regressão logística + Modelo de riscos proporcionais de Cox
6. **Amostra final:** 7.214 registros com 2 anos de acompanhamento; 6.172 usados na regressão

### 3.3 Dataset COMPAS

**Arquivo principal:** `compas-scores-two-years.csv` (disponível no [GitHub da ProPublica](https://github.com/propublica/compas-analysis))

**Colunas principais:**

| Coluna | Descrição |
|--------|-----------|
| `id` | Identificador único |
| `age` | Idade (numérica) |
| `age_cat` | Faixa etária (Less than 25 / 25-45 / Greater than 45) |
| `race` | Raça (African-American, Caucasian, Hispanic, Asian, Native American, Other) |
| `sex` | Gênero (Male/Female) |
| `priors_count` | Número de ocorrências criminais anteriores |
| `juv_fel_count` | Crimes graves na juventude |
| `juv_misd_count` | Contravenções na juventude |
| `c_charge_degree` | Grau da acusação atual (F = Felony, M = Misdemeanor) |
| `decile_score` | Pontuação de risco COMPAS (1-10) |
| `score_text` | Categoria (Low=1-4, Medium=5-7, High=8-10) |
| `two_year_recid` | **Target:** reincidiu em 2 anos? (0=Não, 1=Sim) |

**Estatísticas básicas da amostra:**
- 6.172 registros após limpeza
- 3.175 negros, 2.103 brancos
- 4.997 homens, 1.175 mulheres
- 2.809 reincidentes (45,5%)
- 2 faixas etárias com maior concentração: 25-45 anos

### 3.4 Principais Descobertas da ProPublica

#### Acurácia geral
- O algoritmo previu corretamente a reincidência geral em **61%** dos casos
- Para reincidência violenta, apenas **20%**

#### Viés Racial: Tabela de Contingência

**Réus Brancos:**
| | Baixo Risco | Alto Risco |
|---|---|---|
| Não reincidiu | 1.139 | 349 |
| Reincidiu | 461 | 505 |
- Falso Positivo (FP): **23,45%**
- Falso Negativo (FN): **47,72%**

**Réus Negros:**
| | Baixo Risco | Alto Risco |
|---|---|---|
| Não reincidiu | 990 | 805 |
| Reincidiu | 532 | 1.369 |
- Falso Positivo (FP): **44,85%**
- Falso Negativo (FN): **27,99%**

**Conclusão:** Réus negros eram **quase 2x mais prováveis** de serem falsamente classificados como alto risco (FP: 44,85% vs 23,45%). Réus brancos eram **~1,7x mais prováveis** de serem falsamente classificados como baixo risco (FN: 47,72% vs 27,99%).

#### Regressão Logística (controlando por idade, gênero, histórico criminal)
- Réus negros: **45% mais propensos** a receber pontuação alta
- Para reincidência violenta: **77% mais propensos**
- Jovens (< 25 anos): 2,5x mais propensos
- Mulheres: 19,4% mais propensas

### 3.5 A Resposta da Northpointe e o Debate

A Northpointe contestou os resultados, alegando:
- A métrica correta não é FP/FN, mas **precisão por grupo**: se o score 7 tem a mesma probabilidade de reincidência para negros e brancos, o algoritmo é justo (equal calibration)
- A ProPublica usou threshold inadequado (decile_score >= 5 como alto risco)

**Este debate revelou que AMBOS estavam corretos sob definições diferentes de fairness:**
- ProPublica: **Equalized Odds** (TPR e FPR iguais entre grupos) → COMPAS falha
- Northpointe: **Calibration** (probabilidade predita = probabilidade real para cada grupo) → COMPAS passa

**Implicação:** Não existe definição universal de fairness. A escolha da métrica é uma **decisão ética e política**, não apenas técnica.

### 3.6 Lições do Caso COMPAS

1. **Viés de label/measurement:** O target "reincidência" mede apenas crimes que resultaram em prisão, não crimes reais — há viés de policiamento nos dados
2. **Proxies:** Raça não precisa estar no modelo — CEP, histórico familiar, escolaridade atuam como proxies
3. **Transparência:** O algoritmo COMPAS é proprietário — impossível auditar completamente
4. **Escolha de métrica:** A definição de fairness é política, não matemática
5. **Impacto real:** Réus negros recebem sentenças mais longas baseadas em scores inflados

---

## 4. Tutorial Prático: SHAP + LIME + COMPAS (Python)

### 4.1 Setup — Instalação e Imports

```python
# Instalação (executar uma vez)
# pip install shap lime scikit-learn pandas numpy matplotlib aif360

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

import shap
import lime
import lime.lime_tabular

# Opcional: AIF360 para métricas de fairness
from aif360.metrics import BinaryLabelDatasetMetric, ClassificationMetric
from aif360.datasets import BinaryLabelDataset
```

### 4.2 Carregamento do Dataset COMPAS

**Opção 1: Download direto do repositório ProPublica**

```python
url = 'https://raw.githubusercontent.com/propublica/compas-analysis/master/compas-scores-two-years.csv'
df = pd.read_csv(url)

# Aplicar filtros padrão da ProPublica
df = df[df['days_b_screening_arrest'] <= 30]
df = df[df['days_b_screening_arrest'] >= -30]
df = df[df['is_recid'] != -1]
df = df[df['c_charge_degree'] != 'O']
df = df[df['score_text'] != 'N/A']

# Criar target
df['two_year_recid'] = df['is_recid']

# Selecionar features para o modelo
features = ['age', 'priors_count', 'juv_fel_count', 'juv_misd_count',
            'juv_other_count', 'sex', 'race', 'c_charge_degree']
target = 'two_year_recid'

df_model = df[features + [target]].dropna()
```

**Opção 2: Usando AIF360 (processado e padronizado)**

```python
from aif360.datasets import CompasDataset
from aif360.algorithms.preprocessing.optim_preproc_helpers.data_preproc_functions \
    import load_preproc_data_compas

# Carrega dados pré-processados (afeta apenas African-American/Caucasian)
df_compas = load_preproc_data_compas(protected_attributes=['race'])
```

### 4.3 Preparação dos Dados e Treinamento

```python
# Codificar variáveis categóricas
le_sex = LabelEncoder()
le_race = LabelEncoder()
le_charge = LabelEncoder()

df_model['sex'] = le_sex.fit_transform(df_model['sex'])
df_model['race'] = le_race.fit_transform(df_model['race'])
df_model['c_charge_degree'] = le_charge.fit_transform(df_model['c_charge_degree'])

X = df_model.drop(columns=[target])
y = df_model[target]

# Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Treinar modelo
rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
rf.fit(X_train, y_train)

lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train, y_train)

# Avaliação básica
print("Random Forest:")
print(classification_report(y_test, rf.predict(X_test)))

print("Logistic Regression:")
print(classification_report(y_test, lr.predict(X_test)))
```

### 4.4 Aplicando SHAP

#### 4.4.1 TreeExplainer (para Random Forest — rápido e exato)

```python
# Criar explainer (específico para modelos tree-based)
explainer_rf = shap.TreeExplainer(rf)

# Calcular SHAP values para o conjunto de teste
shap_values_rf = explainer_rf.shap_values(X_test)

# Para classificação binária, shap_values_rf é uma lista de 2 arrays:
# [0] = SHAP para classe 0 (não reincidiu), [1] = SHAP para classe 1 (reincidiu)
# Vamos usar a classe 1 (reincidiu) para análise
shap_values = shap_values_rf[1]
```

#### 4.4.2 Gráfico Summary (Beeswarm) — Visão Global

```python
# Gráfico de resumo: cada ponto é uma amostra,
# posição X = impacto na predição, cor = valor da feature
shap.summary_plot(shap_values, X_test, feature_names=features)

# Gráfico de barras: importância média absoluta
shap.summary_plot(shap_values, X_test, plot_type="bar", feature_names=features)
```

**Interpretação do Summary Plot:**
- `priors_count` é a feature mais importante (maior dispersão horizontal)
- Quanto mais crimes anteriores (vermelho), maior o risco predito (SHAP value positivo)
- `age`: quanto mais jovem (azul), maior o risco
- `race`: valores mais altos (certas raças) empurram para risco maior

#### 4.4.3 Waterfall Plot — Explicação Local

```python
# Explicar a primeira amostra do teste
i = 0
shap.plots.waterfall(shap.Explanation(
    values=shap_values[i],
    base_values=explainer_rf.expected_value[1],
    data=X_test.iloc[i].values,
    feature_names=features
))
```

**Interpretação do Waterfall:**
- `E[f(X)]` = valor base (probabilidade média de reincidência no dataset)
- Barras vermelhas: features que aumentam a probabilidade (empurram para cima)
- Barras azuis: features que diminuem a probabilidade (empurram para baixo)
- Soma das contribuições + valor base = probabilidade final

#### 4.4.4 Dependence Plot — Relação Feature x Impacto

```python
# Como priors_count afeta a predição?
shap.dependence_plot('priors_count', shap_values, X_test,
                     feature_names=features)

# Cor mostrando interação com age
shap.dependence_plot('priors_count', shap_values, X_test,
                     feature_names=features, interaction_index='age')
```

**Interpretação do Dependence Plot:**
- Eixo X: valor da feature
- Eixo Y: SHAP value (impacto na predição)
- Dispersão vertical indica interação com outra feature
- Cor revela qual feature interage (ex: pontos mais escuros = mais jovem)

#### 4.4.5 Force Plot — Visão de "Forças"

```python
# Força para a primeira amostra
shap.force_plot(explainer_rf.expected_value[1], shap_values[0, :],
                X_test.iloc[0, :], feature_names=features,
                matplotlib=True)
```

### 4.5 Aplicando LIME

```python
# Criar explainer (precisa dos dados de treino)
explainer_lime = lime.lime_tabular.LimeTabularExplainer(
    X_train.values,
    feature_names=features,
    class_names=['Não Reincidiu', 'Reincidiu'],
    mode='classification',
    discretize_continuous=True,
    random_state=42
)

# Explicar uma instância específica
i = 0
exp = explainer_lime.explain_instance(
    X_test.iloc[i].values,
    rf.predict_proba,
    num_features=5
)

# Visualizar
exp.show_in_notebook(show_table=True)
exp.as_pyplot_figure()

# Salvar como HTML (para compartilhar)
exp.save_to_file('explicacao_lime_reu.html')
```

**Interpretação da saída LIME:**
- Laranja: features que **favorecem** a classe predita
- Azul: features que **desfavorecem**
- Valores: pesos no modelo linear local

### 4.6 Comparação SHAP vs LIME no COMPAS

```python
# Para a mesma instância, compare as explicações
i = 5

# SHAP
shap.waterfall_plot(shap.Explanation(
    values=shap_values[i],
    base_values=explainer_rf.expected_value[1],
    data=X_test.iloc[i].values,
    feature_names=features
))

# LIME
exp = explainer_lime.explain_instance(
    X_test.iloc[i].values, rf.predict_proba, num_features=5
)
exp.as_pyplot_figure()
plt.show()
```

**Observação prática:** SHAP e LIME frequentemente concordam nas features principais, mas a magnitude relativa pode diferir. SHAP é mais estável entre execuções.

### 4.7 Análise de Fairness com SHAP

```python
# Verificar distribuição dos SHAP values da feature race
race_values = X_test['race'].values
race_shap = shap_values[:, features.index('race')]

# Plotar distribuição do impacto da raça
plt.figure(figsize=(10, 6))
for race_val in np.unique(race_values):
    mask = race_values == race_val
    plt.hist(race_shap[mask], alpha=0.5, label=f'Race Code {race_val}',
             bins=20)
plt.xlabel('SHAP value para feature race')
plt.ylabel('Frequência')
plt.title('Impacto da Raça na Predição por Grupo')
plt.legend()
plt.show()
```

---

## 5. Métricas de Fairness — Código e Interpretação

### 5.1 Disparate Impact (Impacto Desproporcional)

**Conceito:** Razão entre a taxa de outcomes positivos do grupo desprivilegiado e do grupo privilegiado. Baseia-se na "Regra dos 80%" (Four-Fifths Rule) dos EUA.

**Fórmula:**
```
DI = P(Ŷ=1 | A=desprivilegiado) / P(Ŷ=1 | A=privilegiado)
```

**Critério:** DI >= 0.80 é aceitável; DI < 0.80 indica impacto desproporcional.

```python
def disparate_impact(y_pred, group, privileged_group=1):
    """Calcula Disparate Impact Ratio (Regra dos 80%)"""
    rate_priv = np.mean(y_pred[group == privileged_group])
    rate_unpriv = np.mean(y_pred[group != privileged_group])
    if rate_priv == 0:
        return np.nan
    return rate_unpriv / rate_priv

# Exemplo: raça (0 = não-branco, 1 = branco)
group_race = X_test['race'].values
y_pred_rf = rf.predict(X_test)
di = disparate_impact(y_pred_rf, group_race, privileged_group=1)
print(f"Disparate Impact: {di:.4f} {'✓ Aceitável' if di >= 0.80 else '✗ Viés detectado'}")
```

### 5.2 Demographic Parity (Paridade Demográfica)

**Conceito:** A probabilidade de um outcome positivo deve ser igual entre grupos.

```python
def demographic_parity_difference(y_pred, group, privileged_group=1):
    rate_priv = np.mean(y_pred[group == privileged_group])
    rate_unpriv = np.mean(y_pred[group != privileged_group])
    return rate_unpriv - rate_priv

dp = demographic_parity_difference(y_pred_rf, group_race, 1)
print(f"Demographic Parity Diff: {dp:.4f} (0 = perfeito)")
```

### 5.3 Equal Opportunity (Oportunidade Igual)

**Conceito:** A taxa de verdadeiros positivos (TPR) deve ser igual entre grupos — o modelo deve ser igualmente bom em identificar quem realmente vai reincidir.

```python
def equal_opportunity_difference(y_true, y_pred, group, privileged_group=1):
    """Diferença de TPR entre grupos (Equal Opportunity)"""
    mask_priv = (group == privileged_group) & (y_true == 1)
    mask_unpriv = (group != privileged_group) & (y_true == 1)
    tpr_priv = np.mean(y_pred[mask_priv]) if sum(mask_priv) > 0 else np.nan
    tpr_unpriv = np.mean(y_pred[mask_unpriv]) if sum(mask_unpriv) > 0 else np.nan
    return tpr_unpriv - tpr_priv

eo = equal_opportunity_difference(y_test.values, y_pred_rf, group_race, 1)
print(f"Equal Opportunity Diff: {eo:.4f} (0 = perfeito)")
```

### 5.4 Equalized Odds (Chances Equalizadas)

**Conceito:** TPR e FPR devem ser iguais entre grupos (métrica da ProPublica).

```python
def average_odds_difference(y_true, y_pred, group, privileged_group=1):
    """Média das diferenças de TPR e FPR entre grupos"""
    # TPR difference (Equal Opportunity)
    mask_priv_pos = (group == privileged_group) & (y_true == 1)
    mask_unpriv_pos = (group != privileged_group) & (y_true == 1)
    tpr_priv = np.mean(y_pred[mask_priv_pos]) if sum(mask_priv_pos) > 0 else np.nan
    tpr_unpriv = np.mean(y_pred[mask_unpriv_pos]) if sum(mask_unpriv_pos) > 0 else np.nan
    eo_diff = tpr_unpriv - tpr_priv

    # FPR difference
    mask_priv_neg = (group == privileged_group) & (y_true == 0)
    mask_unpriv_neg = (group != privileged_group) & (y_true == 0)
    fpr_priv = np.mean(y_pred[mask_priv_neg]) if sum(mask_priv_neg) > 0 else np.nan
    fpr_unpriv = np.mean(y_pred[mask_unpriv_neg]) if sum(mask_unpriv_neg) > 0 else np.nan
    fpr_diff = fpr_unpriv - fpr_priv

    return (eo_diff + fpr_diff) / 2

aod = average_odds_difference(y_test.values, y_pred_rf, group_race, 1)
print(f"Average Odds Diff: {aod:.4f} (0 = perfeito)")
```

### 5.5 Matriz Comparativa das Métricas

| Métrica | Escopo | Fórmula Chave | Tolerância Comum | O que Mede |
|---------|--------|---------------|------------------|------------|
| Disparate Impact | Outcome (Ŷ) | ratio P(Ŷ=1\|despriv)/P(Ŷ=1\|priv) | >= 0.80 | Distribuição de decisões favoráveis |
| Demographic Parity | Outcome (Ŷ) | diferença P(Ŷ=1\|despriv)-P(Ŷ=1\|priv) | ~0 | Igualdade de seleção |
| Equal Opportunity | TPR | diferença TPR_despriv - TPR_priv | ~0 | Acertos iguais nos positivos |
| Equalized Odds | TPR + FPR | média(TPR_diff, FPR_diff) | ~0 | Acertos e erros iguais |
| Predictive Parity | Precisão (PPV) | diferença PPV_despriv - PPV_priv | ~0 | Significado igual do score |

### 5.6 Usando Bibliotecas Prontas

```python
# AIF360 (IBM)
from aif360.metrics import BinaryLabelDatasetMetric, ClassificationMetric
from aif360.datasets import BinaryLabelDataset

# Criar dataset estruturado
dataset = BinaryLabelDataset(
    df=pd.concat([X_test, y_test], axis=1),
    label_names=['two_year_recid'],
    protected_attribute_names=['race'],
    favorable_label=0,
    unfavorable_label=1,
    privileged_protected_attributes=[[1]]  # race=1 is privileged
)

metric = BinaryLabelDatasetMetric(dataset,
    unprivileged_groups=[{'race': 0}],
    privileged_groups=[{'race': 1}]
)
print(f"Disparate Impact (AIF360): {metric.disparate_impact():.4f}")

# Fairlearn (Microsoft)
from fairlearn.metrics import (
    demographic_parity_difference as dp_diff,
    demographic_parity_ratio as dp_ratio,
    equalized_odds_difference as eo_diff,
    equal_opportunity_difference as eq_opp_diff
)

print(f"DP Ratio: {dp_ratio(y_test, y_pred_rf, sensitive_features=group_race):.4f}")
print(f"EO Diff: {eq_opp_diff(y_test, y_pred_rf, sensitive_features=group_race):.4f}")
```

---

## 6. Benchmarks e Datasets Públicos

### 6.1 Datasets Clássicos para Fairness

| Dataset | Domínio | Atributo Sensível | Target | Amostras | Uso |
|---------|---------|-------------------|--------|----------|-----|
| **COMPAS** | Justiça Criminal | Raça, Sexo | Reincidência (2 anos) | 6.172 | Fairness, XAI, Bias |
| **Adult Income** | Economia | Sexo, Raça | Renda >50K | 48.842 | Fairness, XAI |
| **German Credit** | Finanças | Idade, Sexo | Risco de crédito | 1.000 | Fairness |
| **Bank Marketing** | Marketing | Idade | Depósito a prazo | 45.211 | XAI, PDP |
| **Health Heritage** | Saúde | Raça | Diabetes | 3.000+ | Fairness em saúde |
| **Communities & Crime** | Segurança | Raça | Criminalidade | 1.994 | Fairness |

### 6.2 Benchmarks e Leaderboards

| Ferramenta/Benchmark | Descrição | Link |
|---------------------|-----------|------|
| **AI Fairness 360** | IBM: 70+ métricas, 10+ algoritmos de mitigação | [aif360.mybluemix.net](https://aif360.mybluemix.net) |
| **Fairlearn** | Microsoft: métricas + mitigadores integrados com sklearn | [fairlearn.org](https://fairlearn.org) |
| **What-If Tool** | Google: Interface interativa para análise de fairness | [pair.withgoogle.com](https://pair.withgoogle.com/tools/what-if-tool) |
| **Holistic AI** | Plataforma de auditoria de IA (governança) | [holisticai.com](https://holisticai.com) |
| **Giskard** | Framework open-source de teste de LLMs e ML | [giskard.ai](https://www.giskard.ai) |

### 6.3 Algoritmos de Mitigação de Viés

| Algoritmo | Tipo | Descrição | Implementação |
|-----------|------|-----------|---------------|
| **Reweighing** | Pré-processamento | Atribui pesos às amostras para balancear grupos | AIF360 |
| **Optimized Preprocessing** | Pré-processamento | Transforma dados para reduzir discriminação | AIF360 |
| **Adversarial Debiasing** | In-processing | Treina modelo adversário que prevê atributo sensível | AIF360 |
| **Reject Option Classification** | Pós-processamento | Altera decisões na fronteira de confiança | AIF360 |
| **Calibrated Equalized Odds** | Pós-processamento | Calibra predições para equalizar TPR/FPR | AIF360 |
| **Exponentiated Gradient** | In-processing | Redução a um problema de otimização | Fairlearn |
| **GridSearch** | Pós-processamento | Busca threshold ótimo por grupo | Fairlearn |
| **Threshold Optimizer** | Pós-processamento | Otimiza threshold para métrica de fairness escolhida | Fairlearn |

---

## 7. Discussão Crítica: Limites, Controvérsias e Dilemas

### 7.1 Limitações Técnicas da XAI

1. **Independência de Features:** SHAP e LIME assumem independência entre features ao calcular contribuições. Na prática, features correlacionadas (ex: idade e priors_count) podem gerar atribuições enganosas.

2. **Instabilidade do LIME:** Executar LIME duas vezes na mesma instância pode gerar explicações diferentes. Recomendação: executar múltiplas vezes e verificar consistência.

3. **Falta de Métrica de Qualidade Padrão:** Não há consenso sobre como medir a "qualidade" de uma explicação. "Faithfulness" (fidelidade ao modelo) vs. "plausibility" (plausibilidade para humanos) são conceitos distintos.

4. **XAI não é Causal:** SHAP e LIME explicam correlações aprendidas pelo modelo, não relações causais. Um modelo pode aprender que "guarda-chuva aberto" prediz "chuva", mas a explicação SHAP mostrará guarda-chuva como preditor, não a causa real (chuva).

5. **Custo Computacional:** KernelExplainer do SHAP é O(2^n) no número de features — inviável para modelos com muitas features.

### 7.2 Dilemas Éticos e Controvérsias

**1. Trade-off Acurácia vs. Fairness**
- Mitigar viés geralmente reduz acurácia geral
- **Exemplo COMPAS:** após mitigação, balanced accuracy cai de 67,7% para 66,1%, mas disparate impact melhora de 0,66 para 0,81
- **Decisão de design:** Qual o "preço justo" a pagar por fairness?

**2. Incompatibilidade entre Definições de Fairness**
- Kleinberg et al. (2016) provaram que é impossível satisfazer simultaneamente:
  - Calibration (significado do score igual entre grupos)
  - Equalized Odds (TPR/FPR iguais)
  - Predictive Parity (PPV igual)
- Exceto em casos triviais (prevalência igual ou modelo perfeito)

**3. Fairness Through Unawareness**
- Remover atributos protegidos (raça, gênero) do modelo **não elimina viés**
- Features correlacionadas (CEP, escolaridade, histórico criminal) atuam como proxies
- **Exemplo COMPAS:** mesmo sem raça, o modelo ainda discrimina via priors_count e CEP

**4. Viés de Label/Measurement**
- O target "reincidência" mede apenas crimes que resultaram em prisão
- Negros são mais policiados → mais prisões → mais registros → target enviesado
- **Solução:** Requer intervenção no sistema de justiça, não apenas no algoritmo

**5. Quem é Responsável? (Accountability Gap)**
- Se um modelo de IA comete discriminação, a responsabilidade é:
  - Do desenvolvedor do algoritmo?
  - Da organização que o implantou?
  - Do usuário que seguiu a recomendação?
  - Do regulador que aprovou o sistema?
- **Caso Amazon (2018):** Ninguém foi responsabilizado — o projeto foi cancelado

**6. Regulamentação Fragmentada**
- AI Act europeu: abordagem baseada em risco
- EUA: sem lei federal (NYC Local Law 144, setorial)
- China: regras próprias
- Japão: diretrizes não vinculantes
- **Desafio:** Empresas globais precisam navegar por múltiplos regimes

### 7.3 Incidentes Reais e Lições

| Caso | Ano | Problema | Lição |
|------|-----|----------|-------|
| **COMPAS (ProPublica)** | 2016 | Viés racial em algoritmo de reincidência | Definição de fairness é política; métricas importam |
| **Amazon Recruiting** | 2018 | Viés de gênero em ferramenta de recrutamento | Dados históricos enviesados geram modelos enviesados |
| **Google Photos** | 2015 | Tags racistas (pessoas negras como "gorilas") | Testes de adversidade insuficientes; necessidade de red teaming |
| **Apple Card** | 2019 | Limite de crédito menor para mulheres | Viés de gênero em modelos de crédito |
| **Tay (Microsoft)** | 2016 | Chatbot corrompido em 24h | Falta de safety alignment e monitoramento |
| **SCHUFA (CJEU)** | 2023 | Score de crédito como decisão automatizada | Direito à explicação é exigível judicialmente |

---

## 8. Cross-Mapping: XAI e Outros Domínios

### 8.1 Mapa de Dependências entre Domínios (Mermaid)

```mermaid
graph TB
    %% NÓS CENTRAIS
    XAI(("XAI"))
    Fairness(("Fairness"))
    Accountability(("Accountability"))
    Ethics(("Ethics"))

    %% DOMÍNIOS EXTERNOS
    Law("Direito<br/>AI Act + GDPR")
    HR("RH<br/>Recrutamento")
    Culture("Cultura<br/>Viés Cultural em LLMs")
    SE("Engenharia de Software")
    DataGov("Governança de Dados")
    Society("Sociedade<br/>Impacto Social")

    %% RELAÇÕES
    Law -->|Art.13/14/86| XAI
    Law -->|Art.10 Anexo III| HR
    Law -->|Anexo IV| SE
    Law -->|FRIA + GDPR| DataGov
    Law -->|Direitos Fundamentais| Society

    HR -->|Viés de Gênero/Raça| Fairness
    HR -->|Explicação de Rejeições| XAI
    HR -->|Responsabilidade Legal| Accountability

    Culture -->|Cultural Bias em LLMs| Fairness
    Culture -->|Cultural Alignment Tax| XAI
    Culture -->|Exclusão de Minorias| Society

    XAI -->|SHAP, LIME| Fairness
    XAI -->|Rastreabilidade| Accountability
    XAI -->|Explicações Significativas| Ethics

    Accountability -->|Governança (ISO 42001)| SE
    Accountability -->|Cadeia de Responsabilidade| Law
    Accountability -->|Confiança Pública| Society

    Ethics -->|Princípios: Justiça| Fairness
    Ethics -->|Obrigação Moral de Explicar| XAI
    Ethics -->|Não-Maleficência| Society

    SE -->|Pipeline de IA| XAI
    SE -->|Testes de Viés| Fairness
    SE -->|Documentação Técnica| Accountability

    DataGov -->|Dados Representativos| Fairness
    DataGov -->|Qualidade de Dados| XAI
    DataGov -->|Privacidade (GDPR)| Law

    Society -->|Aceitação/Confiança| Ethics
    Society -->|Proteção de Vulneráveis| Law
    Society -->|Inclusão Digital| Culture

    %% NORMAS
    ISO42001["ISO 42001"]
    NIST["NIST AI RMF"]

    ISO42001 -.->|Gestão| Accountability
    NIST -.->|Riscos| Ethics
```

### 8.2 Conexões Detalhadas por Domínio

#### Direito (AI Act + GDPR)
- **AI Act Art. 13:** Transparência e fornecimento de informações a operadores
- **AI Act Art. 14:** Supervisão humana — XAI alimenta o processo
- **AI Act Art. 86:** Direito à explicação para decisões individuais de alto risco
- **GDPR Art. 22:** Decisões automatizadas — direito à revisão humana
- **GDPR Art. 15:** Direito de acesso — informações significativas sobre a lógica
- **SCHUFA Case (CJEU, 2023):** Score de crédito = decisão automatizada → direito à explicação
- **ISO/IEC 42001:2023:** Sistema de Gestão de IA (certificável)

#### RH (Recrutamento e Seleção)
- **AI Act Anexo III:** Emprego é domínio de alto risco
- **Amazon (2018):** Ferramenta aprendeu a penalizar currículos femininos → cancelada
- **H&M (2024):** Redesenhou algoritmos removendo linguagem generificada
- **Mobley v. Workday (2023-2024):** Ação judicial alegando discriminação racial por IA em triagem
- **NYC Local Law 144:** Exige auditoria de viés em ferramentas de contratação
- **Requisito:** FRIA (Fundamental Rights Impact Assessment) antes da implantação

#### Cultura
- **Cultural Bias em LLMs:** Modelos favorecem valores ocidentais (autoexpressão, individualismo)
- **Cultural Alignment Tax:** Instruction tuning aumenta centralidade nos EUA, reduz nuance cultural
- **Cultural Prompting:** Prefixar prompts com identidade cultural melhora alinhamento em 71-81%
- **LocQA (Google, 2026):** LLMs respondem com normas dos EUA mesmo quando consultados em japonês/hindi
- **UNESCO Recomendação sobre Ética da IA (2021):** Princípios de diversidade cultural

#### Engenharia de Software
- **XAI by Design:** Explicabilidade deve ser considerada desde a fase de design
- **Anexo IV do AI Act:** Documentação técnica detalhada (arquitetura, trade-offs, métricas)
- **Pacotes Python:** `shap`, `lime`, `alibi`, `interpret`, `aif360`, `fairlearn`
- **CI/CD de Fairness:** Integrar testes de viés em pipelines de ML

#### Governança de Dados
- **AI Act Art. 10:** Dados de treino devem ser relevantes, representativos e livres de viés
- **Amazon:** Falha na governança — dados históricos de 10 anos refletiam domínio masculino
- **GDPR Art. 5:** Minimização, exatidão, limitação de finalidade
- **ISO 42001:** Inventário de sistemas de IA, mapeamento de funções, registro de atividades

#### Sociedade
- **Confiança Pública:** Sem XAI e fairness, a aceitação social da IA é prejudicada
- **Direitos Fundamentais:** AI Act exige FRIA para sistemas de alto risco
- **Inclusão vs Exclusão Digital:** LLMs que ignoram culturas não-ocidentais ampliam exclusão
- **UNESCO:** Princípios de proporcionalidade, transparência e responsabilidade humana

---

## 9. Papers, Laboratórios, Comunidades e Onde Acompanhar

### 9.1 Papers Fundamentais (Comentados)

| Título | Ano | Autores | Contribuição | Link |
|--------|-----|---------|--------------|------|
| **Explainable AI (XAI) 2.0: A Manifesto** | 2024 | Luca Longo et al. (18+ autores) | 27 problemas em aberto; roteiro para pesquisa futura | *Information Fusion* |
| **A Critical Survey on Fairness Benefits of XAI** | 2025 | Deck, Schoeffer, De-Arteaga, Kühl | Análise de 175 artigos; 7 alegações sobre XAI para fairness — desalinhamento com evidências | *OpenReview* |
| **Holistic Safety and Responsibility Evaluations of Advanced AI Models** | 2024 | Weidinger et al. (DeepMind) | Framework holístico de avaliação de segurança | DeepMind |
| **Peeking Inside the Black-Box: A Survey on XAI** | 2018 | Adadi & Berrada | Taxonomia seminal; >2000 citações | *IEEE Access* |
| **XAI: Concepts, Taxonomies, Opportunities... Toward Responsible AI** | 2020 | Barredo Arrieta et al. | Framework abrangente; >3500 citações | *Information Fusion* |
| **Why Should I Trust You? Explaining Predictions of Any Classifier** (LIME) | 2016 | Ribeiro, Singh, Guestrin | Artigo fundador do LIME | *KDD 2016* |
| **A Unified Approach to Interpreting Model Predictions** (SHAP) | 2017 | Lundberg & Lee | Artigo fundador do SHAP | *NeurIPS 2017* |
| **It's COMPASlicated: The Messy Relationship Between RAI Datasets and Algorithmic Fairness Benchmarks** | 2021 | Bao et al. | Desaconselha uso do COMPAS para benchmark | *NeurIPS 2021* |
| **Deontic Temporal Logic for Formal Verification of AI Ethics** | 2025 | Priya & Rao | Verificação formal de ética em COMPAS | arXiv:2501.05765 |
| **An Approach to Technical AGI Safety & Security** | 2025 | Dragan, Shah, Legg (DeepMind) | Planejamento proativo de riscos de AGI | DeepMind |

### 9.2 Laboratórios e Grupos de Pesquisa

| Laboratório | Instituição | Foco | Líder/Destaque |
|-------------|-------------|------|----------------|
| **AIEA Lab** | UC Santa Cruz | XAI, NeuroSymbolic AI | Leilani Gilpin |
| **REAL Lab** | UC Santa Cruz | Responsible & Accountable Learning | Yang Liu |
| **Trustworthy ML Group** | Harvard | XAI, fairness, causalidade | Hima Lakkaraju |
| **PAIR** | Google Research | Human-Centered AI, ferramentas de interpretabilidade | Equipe multidisciplinar |
| **Responsible AI & Safety Team** | DeepMind | Avaliação holística de segurança, alignment | Laura Weidinger, Anca Dragan |
| **Trusted AI Group** | IBM Research | AIF360, robustez adversarial, segurança | Pin-Yu Chen |
| **FATE Group** | Microsoft Research | Fairness, Accountability, Transparency, Ethics | — |
| **FAIR - Privacy & Security** | Meta AI | Privacidade, segurança, confiabilidade | — |

### 9.3 Conferências e Eventos

| Conferência | Sigla | Periodicidade | Descrição |
|-------------|-------|---------------|-----------|
| **ACM Fairness, Accountability, and Transparency** | FAccT | Anual (Junho) | Principal conferência do campo (2026: Montreal) |
| **AAAI/ACM AI, Ethics, and Society** | AIES | Anual | Ética e impacto social da IA |
| **IEEE Secure and Trustworthy ML** | SaTML | Anual (Abril) | Segurança e confiabilidade em ML |
| **NeurIPS XAI Workshop** | — | Anual (Dezembro) | Workshop satélite sobre XAI |
| **ICML Responsible AI Workshop** | — | Anual (Julho) | Workshop sobre IA responsável |

### 9.4 Onde Acompanhar Discussões

| Plataforma | Canal | Conteúdo |
|------------|-------|----------|
| **Bluesky** | @facct.bsky.social | Anúncios oficiais do FAccT |
| **LinkedIn** | Trustworthy ML Initiative | Comunidade profissional, seminários |
| **YouTube** | DeepMind Channel | Responsible AI, safety, publicações |
| **GitHub** | `github.com/topics/explainable-ai` | Repositórios, ferramentas, demos |
| **arXiv** | cs.AI, cs.LG, cs.CY | Papers frescos sobre XAI e fairness |
| **Reddit** | r/MachineLearning | Discussões técnicas da comunidade |

### 9.5 Cursos Recomendados

| Curso | Plataforma | Descrição |
|-------|-----------|-----------|
| **Explainable AI Specialization** | Coursera | Profissionais de IA e cientistas de dados |
| **Responsible AI: Transparency, Accountability, Explainability and Privacy** | UC San Diego Extension | Impactos sociais, estudos de caso |
| **Interpretable Machine Learning** | Livro (Christoph Molnar) | Recurso mais completo sobre o tema |
| **People + AI Guidebook** | pair.withgoogle.com | Melhores práticas em IA centrada no humano |
| **AI Explainability in Practice** | Alan Turing Institute | Guia prático (2024) |

---

## 10. Exercícios Resolvidos e Propostos

### 10.1 Exercício Resolvido: Análise de Fairness no COMPAS

**Problema:** Carregue o dataset COMPAS, treine um RandomForestClassifier e determine se há viés racial usando as métricas de Equalized Odds.

**Resolução passo a passo:**

```python
# 1. Setup e carregamento
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

url = 'https://raw.githubusercontent.com/propublica/compas-analysis/master/compas-scores-two-years.csv'
df = pd.read_csv(url)

# 2. Filtros
df = df[df['days_b_screening_arrest'] <= 30]
df = df[df['days_b_screening_arrest'] >= -30]
df = df[df['is_recid'] != -1]
df = df[df['c_charge_degree'] != 'O']
df['two_year_recid'] = df['is_recid']

# 3. Features
features = ['age', 'priors_count', 'sex', 'race', 'c_charge_degree']
target = 'two_year_recid'
df_model = df[features + [target]].dropna()

# Codificar categóricas
le = LabelEncoder()
for col in ['sex', 'race', 'c_charge_degree']:
    df_model[col] = le.fit_transform(df_model[col])

X = df_model.drop(columns=[target])
y = df_model[target]

# 4. Treino
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

# 5. Métricas de fairness
def average_odds_diff(y_true, y_pred, group, priv=1):
    mask_pos_priv = (group == priv) & (y_true == 1)
    mask_pos_unpriv = (group != priv) & (y_true == 1)
    tpr_priv = np.mean(y_pred[mask_pos_priv]) if sum(mask_pos_priv) > 0 else np.nan
    tpr_unpriv = np.mean(y_pred[mask_pos_unpriv]) if sum(mask_pos_unpriv) > 0 else np.nan

    mask_neg_priv = (group == priv) & (y_true == 0)
    mask_neg_unpriv = (group != priv) & (y_true == 0)
    fpr_priv = np.mean(y_pred[mask_neg_priv]) if sum(mask_neg_priv) > 0 else np.nan
    fpr_unpriv = np.mean(y_pred[mask_neg_unpriv]) if sum(mask_neg_unpriv) > 0 else np.nan

    return (tpr_unpriv - tpr_priv + fpr_unpriv - fpr_priv) / 2

grupo = X_test['race'].values
aod = average_odds_diff(y_test.values, y_pred, grupo, priv=1)
print(f"Average Odds Difference: {aod:.4f}")
print(f"Interpretação: {'Viés detectado (difere de 0)' if abs(aod) > 0.05 else 'Viés não detectado'}")

# 6. SHAP para entender o viés
import shap
explainer = shap.TreeExplainer(rf)
shap_values = explainer.shap_values(X_test)[1]
shap.dependence_plot('race', shap_values, X_test, feature_names=features)
```

**Saída esperada:** Average Odds Difference ~ -0.08 a -0.12 (viés contra não-brancos). O dependence plot de `race` mostra SHAP values sistematicamente diferentes entre grupos.

### 10.2 Exercícios Propostos

**Nível 1 — Iniciante:**
1. Carregue o dataset **Adult Income** (shap.datasets.adult()) e treine um XGBoostClassifier. Use SHAP para identificar as top-5 features que mais influenciam predição de renda >50K.
2. Use LIME para explicar a predição de um indivíduo específico e compare com SHAP.

**Nível 2 — Intermediário:**
3. No dataset COMPAS, treine LogisticRegression e RandomForest. Compare os SHAP values das duas models para a feature `race`. O viés muda entre modelos?
4. Implemente o algoritmo Reweighing (pré-processamento) manualmente e meça a melhoria no Disparate Impact antes e depois.

**Nível 3 — Avançado:**
5. Use o pacote `AIF360` para aplicar **Adversarial Debiasing** no COMPAS. Meça o trade-off entre acurácia e fairness antes/depois. Reporte balanced accuracy, disparate impact e average odds difference.
6. Reproduza a análise da ProPublica: compute FP/FN rates por grupo racial e verifique se seus resultados replicam as descobertas originais (FP ~44% negros vs ~23% brancos).
7. Implemente um dashboard interativo (Streamlit ou Gradio) que carregue o COMPAS, treine um modelo e exiba SHAP/LIME + métricas de fairness em tempo real.

### 10.3 Gabarito e Dicas

- **Exercício 5:** Após Adversarial Debiasing, espere redução de ~1-2% na acurácia, mas melhora de 15-25% no disparate impact.
- **Exercício 6:** Use os filtros exatos da ProPublica. O threshold pode alterar resultados — experimente com diferentes cortes de decile_score.
- **Exercício 7:** Use `shap.force_plot()` com `matplotlib=True` e `streamlit` com callbacks para re-treino sob demanda.

---

## 11. Referências Completas

### Papers e Artigos Científicos

1. Lundberg, S.M., & Lee, S.I. (2017). A Unified Approach to Interpreting Model Predictions. *NeurIPS 2017*.
2. Ribeiro, M.T., Singh, S., & Guestrin, C. (2016). Why Should I Trust You?: Explaining Predictions of Any Classifier. *KDD 2016*.
3. Barredo Arrieta, A. et al. (2020). Explainable AI: Concepts, Taxonomies, Opportunities and Challenges Toward Responsible AI. *Information Fusion*, 58, 82-115.
4. Adadi, A., & Berrada, M. (2018). Peeking Inside the Black-Box: A Survey on XAI. *IEEE Access*, 6, 52138-52160.
5. Longo, L. et al. (2024). Explainable AI (XAI) 2.0: A Manifesto of Open Challenges. *Information Fusion*.
6. Deck, L. et al. (2025). A Critical Survey on Fairness Benefits of XAI. *OpenReview*.
7. Weidinger, L. et al. (2024). Holistic Safety and Responsibility Evaluations of Advanced AI Models. *DeepMind*.
8. Bao, M. et al. (2021). It's COMPASlicated. *NeurIPS Datasets & Benchmarks Track*.
9. Dragan, A. et al. (2025). An Approach to Technical AGI Safety & Security. *DeepMind*.
10. Speith, T. (2022). A Review of Taxonomies of XAI Methods. *FAccT '22*.

### Casos e Artigos de Imprensa
11. Angwin, J. et al. (2016). Machine Bias. *ProPublica*. [Link](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)
12. Dastin, J. (2018). Amazon Scraps Secret AI Recruiting Tool That Showed Bias Against Women. *Reuters*.

### Ferramentas e Repositórios
13. AIF360 (IBM). [github.com/Trusted-AI/AIF360](https://github.com/Trusted-AI/AIF360)
14. Fairlearn (Microsoft). [fairlearn.org](https://fairlearn.org)
15. What-If Tool (Google). [pair.withgoogle.com/tools/what-if-tool](https://pair.withgoogle.com/tools/what-if-tool)
16. InterpretML (Microsoft). [interpret.ml](https://interpret.ml)
17. Alibi (Seldon). [github.com/SeldonIO/alibi](https://github.com/SeldonIO/alibi)
18. SHAP. [github.com/shap/shap](https://github.com/shap/shap)
19. LIME. [github.com/marcotcr/lime](https://github.com/marcotcr/lime)
20. COMPAS Dataset (ProPublica). [github.com/propublica/compas-analysis](https://github.com/propublica/compas-analysis)

### Regulações e Padrões
21. EU AI Act — Regulation (EU) 2024/1689
22. GDPR — Regulation (EU) 2016/679
23. ISO/IEC 42001:2023 — AI Management System
24. NIST AI RMF 1.0 (2023)
25. ICO (2024). Explaining Decisions Made with AI. [ico.org.uk](https://ico.org.uk)

### Livros
26. Molnar, C. (2025). *Interpretable Machine Learning*. [christophm.github.io/interpretable-ml-book](https://christophm.github.io/interpretable-ml-book/)
27. Samek, W. et al. (2019). *Explainable AI: Interpreting, Explaining and Visualizing Deep Learning*. Springer.

### Comunidades
28. ACM FAccT Conference: [facctconference.org](https://facctconference.org)
29. Trustworthy ML Initiative: [trustworthyml.org](https://www.trustworthyml.org)
30. DeepMind Responsible AI: [deepmind.google/responsibility-and-safety](https://deepmind.google/responsibility-and-safety/)

---

> **Arquivo expandido em Maio de 2026.** Este é o "padrão de ultra-expansão" para todos os tópicos do vault. Atualizações recomendadas após cada edição do FAccT e principais conferências da área.

> **Tags:** `#XAI` `#fairness` `#accountability` `#responsibleAI` `#COMPAS` `#SHAP` `#LIME` `#FAccT`
