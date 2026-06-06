---
title: "Data Cleaning — Limpeza e Pré-processamento de Dados"
description: "Guia completo de limpeza de dados: valores nulos, outliers, normalização, encoding, deduplicação e validação com pandas, numpy e OpenRefine."
tags: [data-cleaning, preprocessing, pandas, qualidade-dados, skills]
nivel: avancado
updated: 2026-06-05
backlinks: []
assets: []
referencias: []
sensivel: false
date: 2026-06-01
---

# Data Cleaning — Limpeza e Pré-processamento de Dados

## O que é Limpeza de Dados?

Limpeza de dados (data cleaning) é o processo de detectar, corrigir ou remover registros corrompidos, imprecisos, incompletos ou irrelevantes de um conjunto de dados. É a etapa mais crítica e mais demorada de qualquer pipeline de dados — estima-se que 60-80% do tempo de um cientista de dados é gasto nessa fase.

Dados sujos geram modelos enviesados, métricas enganosas e decisões erradas. Um modelo treinado com dados sujos é um modelo que aprende padrões irreais.

### Por que os dados ficam sujos?

- Erros de entrada manual (digitação, formulários)
- Sensores com falha (leituras duplicadas, valores fora de escala)
- Integração de múltiplas fontes (schemas conflitantes, formatos diferentes)
- Dados ausentes por razões sistêmicas (falha de rede, downtime)
- Duplicatas geradas por processos batch repetidos

### Data Cleaning vs Data Wrangling vs Preprocessing

| Termo | Escopo |
|-------|--------|
| **Data Cleaning** | Correção de erros, remoção de ruído |
| **Data Wrangling** | Transformação e mapeamento para formato útil |
| **Preprocessing** | Preparação para algoritmos (encoding, scaling) |

Na prática, os três se sobrepõem. Este guia cobre o espectro completo.

---

## Técnicas de Limpeza de Dados

### 1. Valores Nulos (Missing Data)

Valores nulos (NaN, None, NA) são onipresentes. A abordagem depende do mecanismo de缺失:

- **MCAR (Missing Completely At Random):** Sem padrão — pode remover ou imputar.
- **MAR (Missing At Random):** Padrão explicável por outras variáveis — imputação condicional.
- **MNAR (Missing Not At Random):** O próprio valor ausente é informativo — requer modelagem especializada.

```python
import pandas as pd
import numpy as np

df = pd.read_csv("dados.csv")

# Diagnóstico
print(df.isnull().sum())
print(df.isnull().mean() * 100)  # % de nulos por coluna

# Visualização
import missingno as msno
msno.matrix(df)
msno.heatmap(df)  # Correlação entre nulos
```

**Estratégias de tratamento:**

```python
# 1. Remoção
df_clean = df.dropna()  # Remove qualquer linha com nulo
df_clean = df.dropna(thresh=len(df.columns) - 2)  # Tolerância de 2 nulos por linha
df_clean = df.drop(columns=["col_com_80p_nulos"])  # Remove colunas com muitos nulos

# 2. Imputação simples
df["coluna"] = df["coluna"].fillna(df["coluna"].median())  # Mediana (robusto)
df["coluna"] = df["coluna"].fillna(df["coluna"].mean())    # Média
df["categoria"] = df["categoria"].fillna("desconhecido")   # Moda

# 3. Imputação avançada
from sklearn.impute import KNNImputer, SimpleImputer

imputer = KNNImputer(n_neighbors=5)
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# 4. Forward/Backward fill (séries temporais)
df["venda"] = df["venda"].ffill()   # Propaga último valor válido
df["venda"] = df["venda"].bfill()   # Próximo valor válido
```

**Regra prática:** Acima de 50% de nulos, considere descartar a coluna. Entre 5-50%, impute. Abaixo de 5%, remova as linhas (a menos que a amostra seja pequena).

### 2. Outliers (Valores Atípicos)

Outliers distorcem médias, variâncias e coeficientes de modelos lineares. Detecção depende da distribuição dos dados.

```python
# Método IQR (para distribuições não-normais)
Q1 = df["preco"].quantile(0.25)
Q3 = df["preco"].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR
outliers = df[(df["preco"] < limite_inferior) | (df["preco"] > limite_superior)]

# Z-Score (para distribuições normais)
from scipy import stats
z_scores = np.abs(stats.zscore(df["preco"]))
outliers = df[z_scores > 3]

# Z-Score Modificado (robusto, para dados não-normais)
from scipy.stats import median_abs_deviation
mad = median_abs_deviation(df["preco"])
mod_z = 0.6745 * (df["preco"] - df["preco"].median()) / mad
outliers = df[mod_z > 3.5]

# Isolation Forest (para dados multidimensionais)
from sklearn.ensemble import IsolationForest
iso = IsolationForest(contamination=0.05, random_state=42)
outliers_mask = iso.fit_predict(df.select_dtypes(include=[np.number])) == -1
```

**O que fazer com outliers:**

- **Remover:** se são erros de medição comprovados.
- **Cap (Winsorizar):** substituir por valores nos limites.
  ```python
  df["preco"] = df["preco"].clip(lower=limite_inferior, upper=limite_superior)
  ```
- **Transformar:** log-transform para reduzir impacto.
  ```python
  df["preco_log"] = np.log1p(df["preco"])
  ```
- **Manter:** se representam eventos raros legítimos (ex: fraudes).

### 3. Normalização e Padronização

Algoritmos baseados em distância (KNN, SVM, PCA) e gradiente descendente exigem features na mesma escala.

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Padronização (Z-Score): média 0, desvio 1
scaler = StandardScaler()
df["preco_std"] = scaler.fit_transform(df[["preco"]])

# Normalização Min-Max: escala para [0, 1]
scaler = MinMaxScaler()
df["preco_norm"] = scaler.fit_transform(df[["preco"]])

# Robust Scaler: usa mediana e IQR (robusto a outliers)
scaler = RobustScaler()
df["preco_robust"] = scaler.fit_transform(df[["preco"]])
```

**Qual usar?**
- `StandardScaler` — padrão para regressão, SVM, PCA.
- `MinMaxScaler` — redes neurais (ativações sigmoid/tanh).
- `RobustScaler` — dados com outliers que você não quer remover.

Para dados não-normais ou com cauda longa, aplique transformação antes de escalar:

```python
# Log transform
df["preco_log"] = np.log1p(df["preco"])

# Box-Cox (requer dados positivos)
from scipy.stats import boxcox
df["preco_boxcox"], lambda_otimo = boxcox(df["preco"] + 1)
```

### 4. Encoding de Variáveis Categóricas

Modelos matemáticos não entendem texto. É preciso converter categorias em números.

```python
# Label Encoding (categorias ordinais)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["tamanho"] = le.fit_transform(df["tamanho"])  # P -> 0, M -> 1, G -> 2

# One-Hot Encoding (categorias nominais)
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse_output=False, drop="first")  # drop="first" evita multicolinearidade
encoded = ohe.fit_transform(df[["cor"]])
df_encoded = pd.concat([df, pd.DataFrame(encoded, columns=ohe.get_feature_names_out(["cor"]))], axis=1)

# Target Encoding (para features de alta cardinalidade)
# Substitui cada categoria pela média do target
target_mean = df.groupby("cidade")["preco"].mean()
df["cidade_encoded"] = df["cidade"].map(target_mean)

# Frequency Encoding
freq = df["cidade"].value_counts() / len(df)
df["cidade_freq"] = df["cidade"].map(freq)
```

**High Cardinality:** quando uma coluna tem centenas de categorias (ex: CEP, cidade), One-Hot explode o espaço. Prefira Target Encoding ou Frequency Encoding.

### 5. Deduplicação

Registros duplicados inflam métricas e introduzem viés de amostragem.

```python
# Duplicatas exatas
duplicatas = df[df.duplicated(keep="first")]
print(f"{len(duplicatas)} duplicatas encontradas")
df_deduplicado = df.drop_duplicates(keep="first")

# Duplicatas parciais (subset de colunas)
df_deduplicado = df.drop_duplicates(subset=["nome", "email"], keep="last")

# Duplicatas fuzzy (pequenas variações)
# Para matched-based dedup, veja [[data-engineering/etl-pipelines]]
from thefuzz import fuzz, process

def dedup_fuzzy(df, col, threshold=85):
    grupos = []
    visitados = set()
    for i, nome in enumerate(df[col]):
        if i in visitados:
            continue
        matches = process.extract(nome, df[col], scorer=fuzz.token_sort_ratio, limit=len(df))
        similares = [j for j, score in matches if score >= threshold and j not in visitados]
        visitados.update(similares)
        grupos.append(similares)
    return grupos
```

### 6. Validação de Dados

Validar dados na entrada evita que sujeira se propague pelo pipeline.

```python
# Validação com Pandera
import pandera as pa
from pandera import Column, Check, DataFrameSchema

schema = DataFrameSchema({
    "idade": Column(int, checks=Check.in_range(0, 120)),
    "email": Column(str, checks=Check.str_matches(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")),
    "salario": Column(float, checks=Check.greater_than(0), nullable=True),
    "data_cadastro": Column(pd.DatetimeTZDtype, checks=Check.less_than("2026-01-01")),
})

try:
    schema.validate(df, lazy=True)
except pa.errors.SchemaErrors as e:
    print(e.failure_cases)

# Validação com Great Expectations
# Consulte [[data-engineering/etl-pipelines#Validação]] para integração com pipelines.
```

---

## Ferramentas

### pandas

A espinha dorsal da limpeza de dados em Python. Oferece:
- `DataFrame.isnull()`, `fillna()`, `dropna()` — nulos
- `DataFrame.duplicated()`, `drop_duplicates()` — dedup
- `DataFrame.apply()` — transformações customizadas
- `pd.to_datetime()`, `pd.to_numeric()` — coerção de tipos

```python
# Pipeline típico
def clean_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop_duplicates(subset=["id"])
    df = df.drop(columns=["coluna_inutil"])
    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    df["preco"] = pd.to_numeric(df["preco"], errors="coerce")
    df["preco"] = df["preco"].fillna(df["preco"].median())
    df = df[df["preco"] > 0]
    df = df[(np.abs(stats.zscore(df["preco"])) < 3)]
    return df
```

### numpy

Operações vetorizadas para cálculo de estatísticas, detecção de outliers e transformações.

```python
# Exemplo: remover linhas com qualquer valor fora de 3 desvios
colunas_numericas = df.select_dtypes(include=[np.number]).columns
mask = np.all(np.abs(stats.zscore(df[colunas_numericas])) < 3, axis=1)
df_clean = df[mask]
```

### OpenRefine

Ferramenta visual (GUI) para exploração e limpeza de dados. Ideal para:
- Exploração inicial de datasets desconhecidos
- Faceting e clustering de valores categóricos
- Transformações complexas com GREL (General Refine Expression Language)
- Deduplicação fuzzy interativa

**Fluxo típico:** Explore dados brutos no OpenRefine → Exporte CSV limpo → Pipeline pandas para feature engineering.

---

## Conexões com o Vault

### RAG e Sistemas de Conhecimento

Dados limpos são essenciais para pipelines RAG. Um chunker que processa documentos sujos gera embeddings de baixa qualidade. Veja [[04-knowledge-systems/advanced-rag-strategies]] para estratégias de chunking que dependem de texto limpo.

No [[04-knowledge-systems/obsidian-neural-vault]], a limpeza de metadados (frontmatter) é feita via scripts de preprocessing — o mesmo princípio de data cleaning aplicado a documentos.

### Machine Learning

Todo modelo em [[02-software-engineering/INDEX]] depende de dados limpos. Técnicas como imputação KNN e encoding são pré-requisitos para [[skills/Scikit-Learn]] e pipelines de ML.

### Engenharia de Dados

A limpeza é o primeiro passo de qualquer pipeline ETL. Veja [[data-engineering/etl-pipelines]] para integração de validação em produção com Great Expectations e [[devops/Observabilidade]] para monitoramento de qualidade de dados.

### Kaggle

Competições do [[skills/Kaggle-Datasets]] são laboratórios de data cleaning. A maioria dos datasets do Kaggle exige tratamento significativo antes de modelar.

---

## Checklist de Quality Gates

| Critério | Técnica | Ferramenta |
|----------|---------|------------|
| Nulos < 5% | Remoção | pandas |
| Nulos 5-50% | Imputação (mediana/KNN) | pandas, sklearn |
| Outliers tratados | IQR ou Z-Score | scipy, sklearn |
| Escalas uniformes | StandardScaler/MinMax | sklearn |
| Categóricas encoded | OneHot/Target | sklearn |
| Duplicatas removidas | Exatas + Fuzzy | pandas, thefuzz |
| Tipos corretos | Coerção + schema validation | pandera |

---

## Boas Práticas

1. **Documente cada transformação.** Um notebook sem documentação é lixo após 1 semana.
2. **Versione seus dados limpos.** Use DVC ou `data/processed/` com hash.
3. **Automatize com pipelines.** Nunca limpe dados manualmente duas vezes. Consulte [[data-engineering/etl-pipelines]].
4. **Valide na ingestão.** Previna sujeira na origem — schema validation no momento da carga.
5. **Preserve os dados brutos.** Nunca sobrescreva o raw. Limpe em uma cópia.
6. **Teste suas regras.** Escreva testes unitários para cada transformação.
7. **Monitore qualidade.** Configure alertas para drift de distribuição. Veja [[devops/Observabilidade]].

---

*Consulte também: [[skills/Scikit-Learn]], [[skills/Kaggle-Datasets]], [[data-engineering/etl-pipelines]], [[04-knowledge-systems/advanced-rag-strategies]].*

[[skills/README|← Voltar à Taxonomia de Skills]]
