# ⚖️ XAI & Fairness Simulator — Instruções de Uso

Simulador interativo em **Streamlit** para análise de Explicabilidade (XAI) e Fairness em Machine Learning, usando o dataset **COMPAS** da ProPublica.

---

## 📦 Instalação

### 1. Pré-requisitos

- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)

### 2. Instalar dependências

```bash
# Dependências principais
pip install streamlit pandas numpy matplotlib seaborn scikit-learn

# SHAP — explicações baseadas em teoria dos jogos
pip install shap

# LIME — explicações locais
pip install lime

# XGBoost — modelo adicional (opcional, mas recomendado)
pip install xgboost

# AIF360 (IBM) — dataset e métricas de fairness (opcional)
pip install aif360

# Fairlearn (Microsoft) — mitigação ThresholdOptimizer (opcional)
pip install fairlearn
```

### 3. Para instalar tudo de uma vez (recomendado)

```bash
pip install streamlit pandas numpy matplotlib seaborn scikit-learn shap lime xgboost aif360 fairlearn
```

---

## 🚀 Como Executar

### Pelo terminal:

```bash
streamlit run "XAI-Fairness-Simulator.py"
```

### Pelo diretório:

```bash
cd "C:\Users\willi\Documents\GitHub\Will-obsidian\simuladores"
streamlit run "XAI-Fairness-Simulator.py"
```

O Streamlit abrirá automaticamente o navegador em `http://localhost:8501`.

---

## 🧭 Navegação pelo Simulador

### Barra Lateral (Controles)

| Seção | Descrição |
|-------|-----------|
| **1. Dados** | Seleção da fonte (COMPAS) e proporção de split treino/teste |
| **2. Modelo** | Escolha do modelo: LogisticRegression, RandomForest ou XGBoost |
| **3. Análise** | Ativar/desativar SHAP e LIME (mais lentos, mas informativos) |
| **4. Mitigação** | Aplicar Reweighing (pré) ou ThresholdOptimizer (pós) para reduzir viés |

### Área Principal (Visualizações)

| Aba | Conteúdo |
|-----|----------|
| **Desempenho** | Matriz de confusão, importância de features, métricas (acurácia, precisão, recall, F1, AUC) |
| **SHAP Summary** | Beeswarm plot — importância global das features (cor = valor, posição = impacto) |
| **SHAP Dependence** | Relação feature-valor vs impacto (interação entre features) |
| **SHAP Force** | Explicação local de uma instância (forças empurrando para cima/baixo) |
| **LIME** | Explicação local com pesos lineares e tabela detalhada |
| **Fairness** | Disparate Impact, Equal Opportunity, Equalized Odds, Demographic Parity |
| **Mitigação** | Comparação antes/depois da técnica de mitigação escolhida |
| **Exportar** | Download de relatório HTML completo |

---

## 📊 Sobre o Dataset COMPAS

- **Fonte:** ProPublica (2016) — [compas-analysis](https://github.com/propublica/compas-analysis)
- **Problema:** Predizer reincidência criminal em 2 anos
- **Amostras:** ~6.172 após filtros padrão
- **Features:** idade, gênero, raça, histórico criminal, tipo de acusação
- **Atributo sensível:** Raça (Brancos = privilegiado, Não-Brancos = desprivilegiado)
- **Target:** `two_year_recid` (0 = não reincidiu, 1 = reincidiu)

### Viés conhecido (descoberta da ProPublica)

- Não-brancos têm **~2x mais falsos positivos** que brancos
- Brancos têm **~1,7x mais falsos negativos** que não-brancos
- O modelo é igualmente acurado no geral (~61%), mas profundamente injusto

---

## 📐 Métricas de Fairness Implementadas

| Métrica | Fórmula | Ideal | Interpretação |
|---------|---------|-------|---------------|
| **Disparate Impact Ratio** | P(Ŷ=1\|não-branco) / P(Ŷ=1\|branco) | ≥ 0.80 | Regra dos 80% (EEOC) |
| **Demographic Parity Diff** | P(Ŷ=1\|não-branco) − P(Ŷ=1\|branco) | ≈ 0 | Diferença bruta de outcomes |
| **Equal Opportunity Diff** | TPR_não-branco − TPR_branco | ≈ 0 | Diferença de acertos nos positivos |
| **Average Odds Diff** | (ΔTPR + ΔFPR) / 2 | ≈ 0 | Métrica da ProPublica |

---

## 🛠️ Técnicas de Mitigação

| Técnica | Tipo | Descrição |
|---------|------|-----------|
| **Reweighing** | Pré-processamento | Atribui pesos às amostras para balancear grupos |
| **Threshold Optimizer** | Pós-processamento | Ajusta limiar de decisão por grupo (fairlearn) |

Ambas visam reduzir o viés, geralmente com pequena perda de acurácia.

---

## ⚠️ Solução de Problemas

**Erro: streamlit não é reconhecido**
- Verifique se o Python está no PATH. Tente: `python -m streamlit run ...`

**Erro: SHAP/LIME não encontrados**
- Execute: `pip install shap lime`

**Erro: Conexão ao baixar COMPAS**
- O simulador baixa o CSV da URL da ProPublica. Verifique sua conexão.
- Fallback: o arquivo pode ser baixado manualmente de:
  `https://raw.githubusercontent.com/propublica/compas-analysis/master/compas-scores-two-years.csv`

**Streamlit não abre no navegador**
- Acesse manualmente: `http://localhost:8501`
- Verifique se a porta 8501 está livre

**Memória insuficiente**
- Reduza o número de amostras para SHAP (já limitado a 200)
- Use LogisticRegression (mais leve que RandomForest/XGBoost)

---

## 📁 Estrutura de Arquivos

```
simuladores/
├── XAI-Fairness-Simulator.py          # Aplicativo principal
├── XAI-Fairness-Simulator-Instructions.md  # Este arquivo
└── (compas-scores-two-years.csv)      # Baixado automaticamente
```

---

## 📚 Referências

- [Machine Bias — ProPublica (2016)](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)
- [SHAP — Lundberg & Lee (NeurIPS 2017)](https://shap.readthedocs.io)
- [LIME — Ribeiro et al. (KDD 2016)](https://github.com/marcotcr/lime)
- [AI Fairness 360 (IBM)](https://aif360.mybluemix.net)
- [Fairlearn (Microsoft)](https://fairlearn.org)
- [Fairness & ML — Barocas, Hardt & Narayanan](https://fairmlbook.org)
- [EU AI Act — Regulamento 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689)

---

> **Autor:** Will-obsidian | **Data:** Maio 2026 | **Licença:** MIT
