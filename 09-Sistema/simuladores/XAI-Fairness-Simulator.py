"""
================================================================================
 XAI-Fairness-Simulator — Simulador Interativo de Explicabilidade e Fairness
================================================================================
 
 Um aplicativo Streamlit completo que demonstra:
   - Carregamento do dataset COMPAS (ProPublica)
   - Treinamento de modelos (LogisticRegression, RandomForest, XGBoost)
   - Explicações SHAP (summary, force, dependence plots)
   - Explicações LIME para instâncias individuais
   - Cálculo de métricas de fairness (Disparate Impact, Equal Opportunity,
     Equalized Odds)
   - Visualização de viés entre grupos demográficos
   - Técnicas de mitigação (Reweighing, Threshold Optimizer)
   - Exportação de relatórios em HTML

 Instalação das dependências necessárias:
   pip install streamlit pandas numpy matplotlib seaborn scikit-learn
   pip install shap lime xgboost aif360 fairlearn

 Para executar:
   streamlit run "XAI-Fairness-Simulator.py"

 Autor: Will-obsidian
 Data:   Maio 2026
 Licença: MIT
================================================================================
"""

# ============================================================================
# IMPORTS COM TRATAMENTO DE ERROS
# ============================================================================
import sys
import warnings
import io
import base64
import urllib.request
import os
from pathlib import Path

warnings.filterwarnings("ignore")

# --- Streamlit ---
try:
    import streamlit as st
except ImportError:
    print("ERRO: Streamlit não está instalado.")
    print("Para instalar: pip install streamlit")
    print("Depois execute: streamlit run XAI-Fairness-Simulator.py")
    sys.exit(1)

# --- Científicos ---
import numpy as np
import pandas as pd

# --- Visualização ---
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import seaborn as sns
    HAS_MPL = True
except ImportError:
    HAS_MPL = False
    st.warning("matplotlib/seaborn não disponíveis. Gráficos serão limitados.")

# --- Scikit-learn ---
try:
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler, LabelEncoder
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import (
        accuracy_score, precision_score, recall_score, f1_score,
        roc_auc_score, confusion_matrix, classification_report
    )
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False
    st.error("scikit-learn não instalado: pip install scikit-learn")

# --- SHAP ---
try:
    import shap
    HAS_SHAP = True
except ImportError:
    HAS_SHAP = False
    st.warning("SHAP não instalado. Explicações SHAP desabilitadas. pip install shap")

# --- LIME ---
try:
    import lime
    import lime.lime_tabular
    HAS_LIME = True
except ImportError:
    HAS_LIME = False
    st.warning("LIME não instalado. Explicações LIME desabilitadas. pip install lime")

# --- XGBoost ---
try:
    import xgboost as xgb
    HAS_XGB = True
except ImportError:
    HAS_XGB = False

# --- AIF360 (opcional) ---
try:
    from aif360.algorithms.preprocessing.optim_preproc_helpers.data_preproc_functions import load_preproc_data_compas
    from aif360.metrics import BinaryLabelDatasetMetric, ClassificationMetric
    from aif360.datasets import BinaryLabelDataset
    HAS_AIF360 = True
except ImportError:
    HAS_AIF360 = False

# --- Fairlearn (opcional) ---
try:
    from fairlearn.metrics import (
        demographic_parity_difference as fl_dp_diff,
        demographic_parity_ratio as fl_dp_ratio,
        equalized_odds_difference as fl_eo_diff,
        equal_opportunity_difference as fl_eq_opp_diff,
    )
    from fairlearn.postprocessing import ThresholdOptimizer
    HAS_FAIRLEARN = True
except ImportError:
    HAS_FAIRLEARN = False


# ============================================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================================
st.set_page_config(
    page_title="XAI & Fairness Simulator",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================================
# ESTILO CSS PERSONALIZADO
# ============================================================================
st.markdown("""
<style>
    .main-header { font-size: 2.2rem; color: #1E3A5F; text-align: center;
                   margin-bottom: 0.5rem; font-weight: 700; }
    .sub-header { font-size: 1.1rem; color: #4A6FA5; text-align: center;
                  margin-bottom: 1.5rem; }
    .metric-card { background-color: #f0f2f6; border-radius: 10px; padding: 1rem;
                   margin: 0.5rem 0; border-left: 4px solid #1E3A5F; }
    .metric-pass { border-left-color: #28a745; }
    .metric-fail { border-left-color: #dc3545; }
    .metric-title { font-size: 0.9rem; color: #666; }
    .metric-value { font-size: 1.5rem; font-weight: 700; }
    .metric-label { font-size: 0.8rem; color: #999; }
    .info-box { background-color: #e8f4f8; border-radius: 8px; padding: 1rem;
                margin: 1rem 0; border-left: 4px solid #17a2b8; }
    .warning-box { background-color: #fff3cd; border-radius: 8px; padding: 1rem;
                   margin: 1rem 0; border-left: 4px solid #ffc107; }
    .stButton>button { background-color: #1E3A5F; color: white; }
    .stButton>button:hover { background-color: #2A5080; }
</style>
""", unsafe_allow_html=True)


# ============================================================================
# FUNÇÕES DE CARREGAMENTO DE DADOS (CACHEADAS)
# ============================================================================
@st.cache_data(show_spinner="Baixando dataset COMPAS da ProPublica...")
def load_compas_data():
    """
    Baixa e pré-processa o dataset COMPAS do repositório oficial da ProPublica.
    Retorna um DataFrame limpo e pronto para modelagem.
    """
    url = (
        "https://raw.githubusercontent.com/propublica/compas-analysis/"
        "master/compas-scores-two-years.csv"
    )
    filename = "compas-scores-two-years.csv"
    filepath = Path(filename)

    if not filepath.exists():
        try:
            urllib.request.urlretrieve(url, filename)
        except Exception as e:
            st.error(f"Falha ao baixar COMPAS: {e}")
            st.info("Tentando fallback via cache do sistema...")
            raise e

    df = pd.read_csv(filename)

    df = df[df["days_b_screening_arrest"].notna()]
    df = df[df["days_b_screening_arrest"].between(-30, 30)]
    df = df[df["is_recid"] != -1]
    df = df[df["c_charge_degree"] != "O"]
    df = df[df["score_text"] != "N/A"]

    df["two_year_recid"] = df["is_recid"].astype(int)

    feature_cols = [
        "age", "priors_count", "juv_fel_count", "juv_misd_count",
        "juv_other_count", "sex", "race", "c_charge_degree"
    ]
    target_col = "two_year_recid"

    df_model = df[feature_cols + [target_col]].dropna().copy()

    df_model["sex"] = (df_model["sex"] == "Male").astype(int)
    df_model["race"] = (df_model["race"] == "Caucasian").astype(int)
    df_model["c_charge_degree"] = (df_model["c_charge_degree"] == "F").astype(int)

    return df_model


@st.cache_data(show_spinner="Preparando dados de treino/teste...")
def prepare_train_test(df_model, test_size=0.3, random_state=42):
    """
    Separa features e target, padroniza e divide em treino/teste.
    """
    feature_cols = [
        "age", "priors_count", "juv_fel_count", "juv_misd_count",
        "juv_other_count", "sex", "race", "c_charge_degree"
    ]
    target_col = "two_year_recid"

    X = df_model[feature_cols].values
    y = df_model[target_col].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    dataset_info = {
        "feature_names": feature_cols,
        "target_name": target_col,
        "n_train": X_train.shape[0],
        "n_test": X_test.shape[0],
        "n_features": X_train.shape[1],
        "pos_rate_train": y_train.mean(),
        "pos_rate_test": y_test.mean(),
    }

    return X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled, scaler, dataset_info


# ============================================================================
# FUNÇÕES DE TREINAMENTO (CACHEADAS)
# ============================================================================
@st.cache_data(show_spinner="Treinando modelo...")
def train_model(model_type, params, X_train, y_train, X_train_scaled=None):
    """
    Treina o modelo selecionado com os hiperparâmetros fornecidos.
    """
    if model_type == "LogisticRegression":
        model = LogisticRegression(
            C=params.get("C", 1.0),
            max_iter=params.get("max_iter", 1000),
            solver=params.get("solver", "lbfgs"),
            random_state=42,
            n_jobs=-1,
        )
        model.fit(X_train_scaled, y_train)
    elif model_type == "RandomForest":
        model = RandomForestClassifier(
            n_estimators=params.get("n_estimators", 100),
            max_depth=params.get("max_depth", 10),
            min_samples_split=params.get("min_samples_split", 2),
            min_samples_leaf=params.get("min_samples_leaf", 1),
            random_state=42,
            n_jobs=-1,
        )
        model.fit(X_train, y_train)
    elif model_type == "XGBoost":
        if not HAS_XGB:
            st.error("XGBoost não está instalado. pip install xgboost")
            return None
        model = xgb.XGBClassifier(
            n_estimators=params.get("n_estimators", 100),
            max_depth=params.get("max_depth", 6),
            learning_rate=params.get("learning_rate", 0.1),
            subsample=params.get("subsample", 1.0),
            colsample_bytree=params.get("colsample_bytree", 1.0),
            random_state=42,
            n_jobs=-1,
            eval_metric="logloss",
        )
        model.fit(X_train, y_train)
    else:
        return None

    return model


@st.cache_data(show_spinner="Calculando predições...")
def get_predictions(model, X_test, X_test_scaled, model_type):
    """
    Obtém predições e probabilidades do modelo treinado.
    """
    if model_type == "LogisticRegression":
        y_pred = model.predict(X_test_scaled)
        y_prob = model.predict_proba(X_test_scaled)[:, 1]
    else:
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]
    return y_pred, y_prob


# ============================================================================
# FUNÇÕES DE SHAP (CACHEADAS)
# ============================================================================
@st.cache_data(show_spinner="Calculando SHAP values...")
def compute_shap(_model, X_sample, feature_names, model_type):
    """
    Calcula SHAP values usando o explainer adequado para cada tipo de modelo.
    """
    if not HAS_SHAP:
        return None, None

    try:
        is_tree = model_type in ("RandomForest", "XGBoost")
        if is_tree:
            explainer = shap.TreeExplainer(_model)
            shap_values = explainer.shap_values(X_sample)
            if isinstance(shap_values, list):
                shap_values = shap_values[1]
        else:
            background = shap.kmeans(X_sample, k=min(50, X_sample.shape[0]))
            explainer = shap.KernelExplainer(_model.predict_proba, background)
            sv = explainer.shap_values(X_sample)
            if isinstance(sv, list):
                shap_values = sv[1]
            else:
                shap_values = sv

        expected_value = (
            explainer.expected_value[1]
            if isinstance(explainer.expected_value, (list, np.ndarray))
            and len(explainer.expected_value) > 1
            else explainer.expected_value
        )

        return shap_values, expected_value

    except Exception as e:
        st.warning(f"Erro ao calcular SHAP: {e}")
        return None, None


# ============================================================================
# FUNÇÕES DE FAIRNESS
# ============================================================================
def compute_fairness_metrics(y_true, y_pred, y_prob, group, privileged_value=1):
    """
    Calcula as principais métricas de fairness.
    """
    results = {}
    mask_priv = group == privileged_value
    mask_unpriv = group != privileged_value

    if mask_priv.sum() == 0 or mask_unpriv.sum() == 0:
        return {"erro": "Amostra insuficiente em um dos grupos."}

    # 1. Disparate Impact Ratio
    rate_priv = y_pred[mask_priv].mean()
    rate_unpriv = y_pred[mask_unpriv].mean()
    di_ratio = rate_unpriv / rate_priv if rate_priv > 0 else float("inf")
    results["di_ratio"] = di_ratio
    results["di_pass"] = di_ratio >= 0.80
    results["pred_rate_priv"] = rate_priv
    results["pred_rate_unpriv"] = rate_unpriv

    # 2. Demographic Parity Difference
    results["dp_diff"] = rate_unpriv - rate_priv

    # 3. Equal Opportunity Difference (TPR difference)
    mask_priv_pos = mask_priv & (y_true == 1)
    mask_unpriv_pos = mask_unpriv & (y_true == 1)
    tpr_priv = y_pred[mask_priv_pos].mean() if mask_priv_pos.sum() > 0 else 0.0
    tpr_unpriv = y_pred[mask_unpriv_pos].mean() if mask_unpriv_pos.sum() > 0 else 0.0
    results["tpr_priv"] = tpr_priv
    results["tpr_unpriv"] = tpr_unpriv
    results["eo_diff"] = tpr_unpriv - tpr_priv

    # 4. Equalized Odds (Average odds difference)
    mask_priv_neg = mask_priv & (y_true == 0)
    mask_unpriv_neg = mask_unpriv & (y_true == 0)
    fpr_priv = y_pred[mask_priv_neg].mean() if mask_priv_neg.sum() > 0 else 0.0
    fpr_unpriv = y_pred[mask_unpriv_neg].mean() if mask_unpriv_neg.sum() > 0 else 0.0
    results["fpr_priv"] = fpr_priv
    results["fpr_unpriv"] = fpr_unpriv
    results["avg_odds_diff"] = ((tpr_unpriv - tpr_priv) + (fpr_unpriv - fpr_priv)) / 2

    # 5. Métricas gerais
    results["acc"] = accuracy_score(y_true, y_pred)
    results["prec"] = precision_score(y_true, y_pred, zero_division=0)
    results["rec"] = recall_score(y_true, y_pred, zero_division=0)

    return results


def apply_reweighing(X_train, y_train, group_train, privileged_value=1):
    """
    Aplica a técnica Reweighing (pré-processamento):
    atribui pesos às amostras para balancear os grupos.
    """
    n = len(y_train)
    weights = np.ones(n)

    mask_priv = group_train == privileged_value
    mask_unpriv = group_train != privileged_value

    n_priv = mask_priv.sum()
    n_unpriv = mask_unpriv.sum()
    n_pos = y_train.sum()
    n_neg = n - n_pos

    if n_priv == 0 or n_unpriv == 0:
        return weights, "Amostra insuficiente em um grupo."

    # Probabilidades esperadas sob independência
    p_priv = n_priv / n
    p_unpriv = n_unpriv / n
    p_pos = n_pos / n
    p_neg = n_neg / n

    for i in range(n):
        is_unpriv = mask_unpriv.iloc[i] if hasattr(mask_unpriv, "iloc") else mask_unpriv[i]
        is_pos = y_train.iloc[i] if hasattr(y_train, "iloc") else y_train[i]

        if is_unpriv and is_pos:
            weights[i] = (p_priv * p_pos) / (
                (n_unpriv / n) * (n_pos / n)
            ) if n_unpriv > 0 and n_pos > 0 else 1.0
        elif is_unpriv and not is_pos:
            weights[i] = (p_priv * p_neg) / (
                (n_unpriv / n) * (n_neg / n)
            ) if n_unpriv > 0 and n_neg > 0 else 1.0
        elif not is_unpriv and is_pos:
            weights[i] = (p_unpriv * p_pos) / (
                (n_priv / n) * (n_pos / n)
            ) if n_priv > 0 and n_pos > 0 else 1.0
        else:
            weights[i] = (p_unpriv * p_neg) / (
                (n_priv / n) * (n_neg / n)
            ) if n_priv > 0 and n_neg > 0 else 1.0

    weights = np.clip(weights, 0.1, 10.0)
    return weights, "Reweighing aplicado com sucesso."


# ============================================================================
# FUNÇÕES DE VISUALIZAÇÃO
# ============================================================================
def plot_confusion_matrix(y_true, y_pred, title="Matriz de Confusão"):
    """Plota a matriz de confusão usando seaborn."""
    fig, ax = plt.subplots(figsize=(5, 4))
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(
        cm, annot=True, fmt="d", cmap="Blues", ax=ax,
        xticklabels=["Não Reincidiu", "Reincidiu"],
        yticklabels=["Não Reincidiu", "Reincidiu"],
    )
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.set_ylabel("Real")
    ax.set_xlabel("Predito")
    plt.tight_layout()
    return fig


def plot_feature_importance(model, feature_names, model_type, title="Importância de Features"):
    """Plota a importância das features (para modelos que suportam)."""
    if model_type == "LogisticRegression":
        if hasattr(model, "coef_"):
            importances = np.abs(model.coef_[0])
        else:
            return None
    else:
        if hasattr(model, "feature_importances_"):
            importances = model.feature_importances_
        else:
            return None

    idx_sort = np.argsort(importances)[::-1]
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = sns.color_palette("viridis", len(importances))
    bars = ax.barh(range(len(importances)), importances[idx_sort], color=colors)
    ax.set_yticks(range(len(importances)))
    ax.set_yticklabels([feature_names[i] for i in idx_sort])
    ax.set_xlabel("Importância")
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.invert_yaxis()
    plt.tight_layout()
    return fig


def plot_shap_summary(shap_values, X_sample, feature_names):
    """
    Gera o SHAP Summary Plot (beeswarm) e retorna a figura matplotlib.
    """
    if not HAS_SHAP or shap_values is None:
        return None
    try:
        fig, ax = plt.subplots(figsize=(9, 6))
        shap.summary_plot(
            shap_values, X_sample, feature_names=feature_names,
            show=False, alpha=0.7,
        )
        plt.tight_layout()
        return fig
    except Exception as e:
        st.warning(f"Erro ao gerar SHAP summary plot: {e}")
        return None


def plot_shap_dependence(shap_values, X_sample, feature_names, feature_idx):
    """
    Gera o SHAP Dependence Plot para uma feature específica.
    """
    if not HAS_SHAP or shap_values is None:
        return None
    try:
        feat_name = feature_names[feature_idx]
        fig, ax = plt.subplots(figsize=(8, 5))
        shap.dependence_plot(
            feature_idx, shap_values, X_sample,
            feature_names=feature_names, show=False,
        )
        plt.title(f"Dependence Plot: {feat_name}", fontsize=13, fontweight="bold")
        plt.tight_layout()
        return fig
    except Exception as e:
        st.warning(f"Erro ao gerar SHAP dependence plot: {e}")
        return None


def plot_shap_force(shap_values, expected_value, X_instance, feature_names):
    """
    Gera o SHAP Force Plot para uma instância específica.
    """
    if not HAS_SHAP or shap_values is None:
        return None
    try:
        fig, ax = plt.subplots(figsize=(10, 3))
        shap.force_plot(
            expected_value, shap_values, X_instance,
            feature_names=feature_names, matplotlib=True, show=False,
        )
        plt.tight_layout()
        return fig
    except Exception as e:
        st.warning(f"Erro ao gerar SHAP force plot: {e}")
        return None


def plot_fairness_comparison(metrics_before, metrics_after, group_names):
    """
    Gráfico comparativo de métricas de fairness antes e depois da mitigação.
    """
    labels = ["DI Ratio", "DP Diff", "EO Diff", "Avg Odds Diff"]
    if metrics_before is None:
        return None

    before_vals = [
        metrics_before.get("di_ratio", 0),
        metrics_before.get("dp_diff", 0),
        metrics_before.get("eo_diff", 0),
        metrics_before.get("avg_odds_diff", 0),
    ]
    after_vals = None
    if metrics_after:
        after_vals = [
            metrics_after.get("di_ratio", 0),
            metrics_after.get("dp_diff", 0),
            metrics_after.get("eo_diff", 0),
            metrics_after.get("avg_odds_diff", 0),
        ]

    x = np.arange(len(labels))
    width = 0.3
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(x - width / 2, before_vals, width, label="Antes", color="#dc3545", alpha=0.8)
    if after_vals:
        ax.bar(x + width / 2, after_vals, width, label="Depois", color="#28a745", alpha=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.axhline(y=0.8, color="gray", linestyle="--", alpha=0.5, label="DI=0.8 (limite)")
    ax.axhline(y=0.0, color="black", linewidth=0.5)
    ax.set_ylabel("Valor")
    ax.set_title("Comparação de Métricas: Antes vs Depois da Mitigação", fontsize=12, fontweight="bold")
    ax.legend()
    plt.tight_layout()
    return fig


def plot_group_rates(y_pred, group, group_names=("Não-Brancos", "Brancos")):
    """
    Gráfico de barras comparando taxas de predição positiva entre grupos.
    """
    uniq = np.unique(group)
    rates = [y_pred[group == v].mean() for v in uniq]
    labels = group_names if len(group_names) == len(uniq) else [f"Grupo {v}" for v in uniq]

    fig, ax = plt.subplots(figsize=(6, 4))
    colors = ["#ff6b6b", "#4ecdc4"]
    bars = ax.bar(labels, rates, color=colors[:len(uniq)], alpha=0.8, edgecolor="gray")
    for bar, rate in zip(bars, rates):
        ax.text(
            bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01,
            f"{rate:.2%}", ha="center", fontsize=11, fontweight="bold",
        )
    ax.set_ylabel("Taxa de Predição Positiva")
    ax.set_title("Taxa de Reincidência Predita por Grupo", fontsize=12, fontweight="bold")
    ax.set_ylim(0, max(rates) * 1.2 if rates else 1)
    plt.tight_layout()
    return fig


def plot_roc_curve(y_true, y_prob, title="Curva ROC"):
    """Plota a curva ROC."""
    from sklearn.metrics import roc_curve, auc
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    roc_auc = auc(fpr, tpr)

    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(fpr, tpr, color="#1E3A5F", lw=2, label=f"AUC = {roc_auc:.3f}")
    ax.plot([0, 1], [0, 1], "k--", lw=1, alpha=0.6)
    ax.fill_between(fpr, tpr, alpha=0.15, color="#1E3A5F")
    ax.set_xlabel("Taxa de Falsos Positivos (FPR)")
    ax.set_ylabel("Taxa de Verdadeiros Positivos (TPR)")
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.legend(loc="lower right")
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1.05])
    plt.tight_layout()
    return fig


# ============================================================================
# FUNÇÃO PARA EXPORTAR RELATÓRIO HTML
# ============================================================================
def generate_html_report(metrics, fairness_df, model_name, dataset_info):
    """
    Gera um relatório HTML com os resultados da análise.
    """
    di_ratio = metrics.get("di_ratio", 0)
    eo_diff = metrics.get("eo_diff", 0)
    aod = metrics.get("avg_odds_diff", 0)
    acc = metrics.get("acc", 0)
    di_status = "✅ PASSOU" if di_ratio >= 0.80 else "❌ FALHOU"

    html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head><meta charset="UTF-8">
    <title>Relatório de Fairness - {model_name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; color: #333; }}
        h1 {{ color: #1E3A5F; border-bottom: 2px solid #1E3A5F; }}
        h2 {{ color: #2A5080; margin-top: 30px; }}
        table {{ border-collapse: collapse; width: 100%; margin: 15px 0; }}
        th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
        th {{ background-color: #1E3A5F; color: white; }}
        tr:nth-child(even) {{ background-color: #f2f2f2; }}
        .pass {{ color: green; font-weight: bold; }}
        .fail {{ color: red; font-weight: bold; }}
        .summary {{ background: #f0f2f6; padding: 15px; border-radius: 8px; }}
    </style>
    </head>
    <body>
    <h1>⚖️ Relatório de Auditoria de Fairness</h1>
    <p><strong>Modelo:</strong> {model_name}</p>
    <p><strong>Dataset:</strong> COMPAS (ProPublica)</p>
    <p><strong>Atributo Sensível:</strong> Raça (Brancos = privilegiado)</p>
    <p><strong>Target:</strong> Reincidência em 2 anos</p>
    <p><strong>Gerado em:</strong> {pd.Timestamp.now().strftime('%d/%m/%Y %H:%M')}</p>

    <h2>📊 Informações do Dataset</h2>
    <table>
        <tr><th>Métrica</th><th>Valor</th></tr>
        <tr><td>Amostras de treino</td><td>{dataset_info['n_train']}</td></tr>
        <tr><td>Amostras de teste</td><td>{dataset_info['n_test']}</td></tr>
        <tr><td>Features</td><td>{dataset_info['n_features']}</td></tr>
        <tr><td>Taxa de reincidência (treino)</td><td>{dataset_info['pos_rate_train']:.1%}</td></tr>
        <tr><td>Taxa de reincidência (teste)</td><td>{dataset_info['pos_rate_test']:.1%}</td></tr>
    </table>

    <h2>📈 Métricas de Desempenho</h2>
    <table>
        <tr><th>Métrica</th><th>Valor</th></tr>
        <tr><td>Acurácia</td><td>{acc:.3f}</td></tr>
        <tr><td>Disparate Impact Ratio</td><td>{di_ratio:.3f} - <span class="{'pass' if di_ratio >= 0.80 else 'fail'}">{di_status}</span></td></tr>
        <tr><td>Equal Opportunity Diff</td><td>{eo_diff:.4f}</td></tr>
        <tr><td>Average Odds Diff</td><td>{aod:.4f}</td></tr>
    </table>

    <h2>📋 Detalhamento por Grupo</h2>
    {fairness_df.to_html(index=False, classes="table") if fairness_df is not None else "<p>Sem dados de grupo.</p>"}

    <div class="summary">
    <h3>🔍 Interpretação</h3>
    <p><strong>Disparate Impact (Regra dos 80%):</strong>
    {'O modelo PASSOU no teste de impacto desproporcional (DI >= 0.80).' if di_ratio >= 0.80 else 'O modelo FALHOU no teste de impacto desproporcional (DI < 0.80). O grupo não-branco recebe predições positivas com frequência significativamente menor.'}</p>
    <p><strong>Equal Opportunity:</strong>
    {'Diferença de TPR entre grupos é baixa (próxima de zero).' if abs(eo_diff) < 0.05 else 'Diferença de TPR entre grupos é significativa, indicando tratamento desigual.'}</p>
    <p><strong>Equalized Odds:</strong>
    {'Diferença média de TPR e FPR é baixa.' if abs(aod) < 0.05 else 'Diferença média de TPR e FPR é significativa.'}</p>
    </div>

    <p style="color: #999; font-size: 0.9em; margin-top: 40px;">
    Relatório gerado pelo XAI & Fairness Simulator.</p>
    </body></html>
    """
    return html


# ============================================================================
# FUNÇÃO PRINCIPAL DO APP
# ============================================================================
def main():
    # ------------------------------------------------------------------
    # SIDEBAR
    # ------------------------------------------------------------------
    st.sidebar.markdown(
        "<h1 style='font-size:1.5rem; color:#1E3A5F;'>⚖️ XAI & Fairness</h1>",
        unsafe_allow_html=True,
    )
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    # Seção de dados
    st.sidebar.subheader("1. 📂 Dados")
    data_option = st.sidebar.selectbox(
        "Fonte de dados",
        ["COMPAS (ProPublica)"],
        help="Dataset COMPAS de reincidência criminal (ProPublica, 2016)",
    )

    test_size = st.sidebar.slider(
        "Proporção de teste", 0.1, 0.5, 0.3, 0.05,
        help="Porcentagem dos dados reservada para teste",
    )

    # Seção de modelo
    st.sidebar.subheader("2. 🧠 Modelo")
    model_type = st.sidebar.selectbox(
        "Tipo de modelo",
        ["RandomForest", "LogisticRegression", "XGBoost"],
        help="Escolha o classificador para treinar",
    )

    with st.sidebar.expander("⚙️ Hiperparâmetros", expanded=False):
        if model_type == "LogisticRegression":
            C = st.number_input("C (inverso da regularização)", 0.01, 10.0, 1.0, 0.1,
                                help="Menor C = mais regularização")
            max_iter = st.number_input("Iterações máximas", 100, 10000, 1000, 100)
            solver = st.selectbox("Solver", ["lbfgs", "liblinear", "newton-cg"])
            params = {"C": C, "max_iter": max_iter, "solver": solver}

        elif model_type == "RandomForest":
            n_estimators = st.slider("Nº de árvores", 10, 500, 100, 10)
            max_depth = st.slider("Profundidade máxima", 1, 50, 10, 1)
            min_samples_split = st.slider("Min. amostras por split", 2, 20, 2)
            min_samples_leaf = st.slider("Min. amostras por folha", 1, 20, 1)
            params = {
                "n_estimators": n_estimators,
                "max_depth": max_depth,
                "min_samples_split": min_samples_split,
                "min_samples_leaf": min_samples_leaf,
            }

        elif model_type == "XGBoost":
            n_estimators = st.slider("Nº de estimadores", 10, 500, 100, 10)
            max_depth = st.slider("Profundidade máxima", 1, 20, 6)
            learning_rate = st.slider("Taxa de aprendizado", 0.01, 0.5, 0.1, 0.01)
            subsample = st.slider("Subamostragem", 0.5, 1.0, 1.0, 0.1)
            colsample_bytree = st.slider("Colunas por árvore", 0.3, 1.0, 1.0, 0.1)
            params = {
                "n_estimators": n_estimators,
                "max_depth": max_depth,
                "learning_rate": learning_rate,
                "subsample": subsample,
                "colsample_bytree": colsample_bytree,
            }

    # Seção de explicação
    st.sidebar.subheader("3. 🔍 Análise")
    use_shap = st.sidebar.checkbox(
        "Ativar SHAP", value=True,
        help="SHAP (SHapley Additive exPlanations) — explicações baseadas em teoria dos jogos",
    )
    use_lime = st.sidebar.checkbox(
        "Ativar LIME", value=True,
        help="LIME (Local Interpretable Model-agnostic Explanations) — explicações locais",
    )

    # Seção de mitigação
    st.sidebar.subheader("4. 🛠️ Mitigação")
    use_mitigation = st.sidebar.checkbox(
        "Aplicar mitigação de viés",
        value=False,
        help="Tenta reduzir o viés usando técnicas de pré ou pós-processamento",
    )
    mitigation_method = st.sidebar.selectbox(
        "Método de mitigação",
        ["Reweighing (pré-processamento)", "Threshold Optimizer (pós-processamento)"],
        help="Reweighing: reweighting das amostras. Threshold Optimizer: ajuste do limiar de decisão.",
    ) if use_mitigation else None

    # Botão de processar
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    process_button = st.sidebar.button(
        "🚀 Processar Análise Completa",
        type="primary",
        use_container_width=True,
    )

    # Informações laterais
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)
    with st.sidebar.expander("ℹ️ Sobre"):
        st.markdown("""
        **XAI & Fairness Simulator** v1.0

        Simulador interativo para análise de explicabilidade
        e fairness em machine learning.

        - Dataset: COMPAS (ProPublica)
        - Atributo sensível: Raça
        - Target: Reincidência em 2 anos

        [Repositório GitHub](https://github.com/propublica/compas-analysis)
        """)

    # ------------------------------------------------------------------
    # MAIN AREA
    # ------------------------------------------------------------------
    st.markdown(
        "<div class='main-header'>⚖️ XAI & Fairness Simulator</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div class='sub-header'>"
        "Análise interativa de explicabilidade (SHAP/LIME) e fairness "
        "no dataset COMPAS</div>",
        unsafe_allow_html=True,
    )

    # Verificações de dependências
    missing = []
    if not HAS_SHAP:
        missing.append("SHAP")
    if not HAS_LIME:
        missing.append("LIME")
    if missing:
        st.warning(
            f"⚠️ Dependências opcionais não encontradas: {', '.join(missing)}. "
            f"pip install {' '.join(missing)} para funcionalidade completa."
        )

    # ------------------------------------------------------------------
    # CARREGAMENTO E PRÉ-PROCESSAMENTO
    # ------------------------------------------------------------------
    if not process_button:
        st.info(
            "👈 Configure os parâmetros na barra lateral e clique em "
            "**'Processar Análise Completa'** para iniciar."
        )
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Dataset", "COMPAS", "ProPublica")
        with col2:
            st.metric("Amostras", "~6.172", "após filtros")
        with col3:
            st.metric("Features", "8", " + target binário")
        with col4:
            st.metric("Atributo Sensível", "Raça", "Branco/Não-Branco")
        return

    with st.spinner("Carregando e preparando dados..."):
        try:
            df_model = load_compas_data()
            X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled, scaler, dataset_info = prepare_train_test(
                df_model, test_size=test_size
            )
        except Exception as e:
            st.error(f"❌ Erro ao carregar dados: {e}")
            st.stop()

    feature_names = dataset_info["feature_names"]

    # ------------------------------------------------------------------
    # TREINAMENTO
    # ------------------------------------------------------------------
    with st.spinner(f"Treinando modelo {model_type}..."):
        model = train_model(model_type, params, X_train, y_train, X_train_scaled)
        if model is None:
            st.error("Falha no treinamento do modelo.")
            st.stop()

        y_pred, y_prob = get_predictions(model, X_test, X_test_scaled, model_type)

    # ------------------------------------------------------------------
    # MÉTRICAS DE DESEMPENHO
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("## 📊 Desempenho do Modelo")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        acc = accuracy_score(y_test, y_pred)
        st.metric("Acurácia", f"{acc:.3f}")
    with col2:
        prec = precision_score(y_test, y_pred, zero_division=0)
        st.metric("Precisão", f"{prec:.3f}")
    with col3:
        rec = recall_score(y_test, y_pred, zero_division=0)
        st.metric("Recall", f"{rec:.3f}")
    with col4:
        f1 = f1_score(y_test, y_pred)
        st.metric("F1-Score", f"{f1:.3f}")
    with col5:
        try:
            auc = roc_auc_score(y_test, y_prob)
            st.metric("AUC-ROC", f"{auc:.3f}")
        except Exception:
            st.metric("AUC-ROC", "N/A")

    col_a, col_b = st.columns(2)
    with col_a:
        fig_cm = plot_confusion_matrix(y_test, y_pred, f"Matriz de Confusão — {model_type}")
        if fig_cm:
            st.pyplot(fig_cm)
            plt.close(fig_cm)

    with col_b:
        fig_fi = plot_feature_importance(
            model, feature_names, model_type,
            f"Importância de Features — {model_type}"
        )
        if fig_fi:
            st.pyplot(fig_fi)
            plt.close(fig_fi)
        elif HAS_SHAP:
            st.info("Use SHAP abaixo para importância de features mais robusta.")

    # ------------------------------------------------------------------
    # SHAP ANALYSIS
    # ------------------------------------------------------------------
    if use_shap and HAS_SHAP:
        st.markdown("---")
        st.markdown("## 🔬 Análise SHAP (SHapley Additive exPlanations)")
        st.markdown(
            "<div class='info-box'>"
            "<strong>SHAP</strong> usa teoria dos jogos cooperativos para atribuir "
            "a cada feature uma contribuição para a predição. "
            "Propriedades desejáveis: eficiência, simetria, dummy e aditividade."
            "</div>",
            unsafe_allow_html=True,
        )

        n_shap = min(200, X_test.shape[0])
        X_shap = X_test[:n_shap]
        X_shap_scaled = X_test_scaled[:n_shap]

        with st.spinner("Calculando SHAP values..."):
            shap_values, expected_value = compute_shap(model, X_shap, feature_names, model_type)

        if shap_values is not None:
            tab_summary, tab_dependence, tab_force = st.tabs(
                ["📈 Summary Plot", "📉 Dependence Plot", "🔍 Force Plot"]
            )

            with tab_summary:
                st.markdown(
                    "<div class='info-box'>"
                    "<strong>Interpretação:</strong> Cada ponto = uma observação. "
                    "Posição horizontal = valor SHAP (direita = contribui para reincidência). "
                    "Cor = valor da feature (vermelho = alto, azul = baixo)."
                    "</div>",
                    unsafe_allow_html=True,
                )
                fig_summary = plot_shap_summary(shap_values, X_shap, feature_names)
                if fig_summary:
                    st.pyplot(fig_summary)
                    plt.close(fig_summary)

                # Bar plot alternativo
                try:
                    fig_bar, ax_bar = plt.subplots(figsize=(8, 5))
                    shap.summary_plot(
                        shap_values, X_shap, feature_names=feature_names,
                        plot_type="bar", show=False,
                    )
                    plt.title("SHAP Feature Importance (Bar)", fontsize=12, fontweight="bold")
                    plt.tight_layout()
                    st.pyplot(fig_bar)
                    plt.close(fig_bar)
                except Exception:
                    pass

            with tab_dependence:
                st.markdown(
                    "<div class='info-box'>"
                    "<strong>Interpretação:</strong> Mostra a relação entre o valor "
                    "da feature (eixo X) e seu impacto SHAP (eixo Y). "
                    "A cor revela interação com outra feature."
                    "</div>",
                    unsafe_allow_html=True,
                )
                dep_feature = st.selectbox(
                    "Selecione a feature para o Dependence Plot",
                    feature_names,
                    index=feature_names.index("priors_count")
                    if "priors_count" in feature_names
                    else 0,
                )
                dep_idx = feature_names.index(dep_feature)
                fig_dep = plot_shap_dependence(shap_values, X_shap, feature_names, dep_idx)
                if fig_dep:
                    st.pyplot(fig_dep)
                    plt.close(fig_dep)

                # Dependence plot para race (crítico para fairness)
                if "race" in feature_names:
                    st.markdown(
                        "<div class='warning-box'>"
                        "<strong>⚠️ Análise de Viés:</strong> O dependence plot para "
                        "<code>race</code> revela se o modelo usa raça como preditor. "
                        "Se os pontos para <code>race=0</code> (não-brancos) estiverem "
                        "sistematicamente acima de zero, o modelo discrimina."
                        "</div>",
                        unsafe_allow_html=True,
                    )
                    race_idx = feature_names.index("race")
                    fig_dep_race = plot_shap_dependence(
                        shap_values, X_shap, feature_names, race_idx
                    )
                    if fig_dep_race:
                        st.pyplot(fig_dep_race)
                        plt.close(fig_dep_race)

            with tab_force:
                st.markdown(
                    "<div class='info-box'>"
                    "<strong>Interpretação:</strong> Features em <span style='color:red;'>"
                    "vermelho</span> empurram a predição para cima (reincidência), "
                    "features em <span style='color:blue;'>azul</span> empurram para baixo. "
                    "Soma das contribuições + valor base = probabilidade final."
                    "</div>",
                    unsafe_allow_html=True,
                )
                instance_idx = st.number_input(
                    "Índice da instância no dataset de teste",
                    0, X_shap.shape[0] - 1, 0, 1,
                )
                st.write(
                    f"**Valor base (prob. média):** {expected_value:.3f}  |  "
                    f"**Prob. predita:** {y_prob[instance_idx]:.3f}  |  "
                    f"**Classe real:** {'Reincidiu' if y_test[instance_idx] == 1 else 'Não reincidiu'}"
                )

                fig_force = plot_shap_force(
                    shap_values[instance_idx],
                    expected_value,
                    X_shap[instance_idx],
                    feature_names,
                )
                if fig_force:
                    st.pyplot(fig_force)
                    plt.close(fig_force)

                # Waterfall plot
                try:
                    st.markdown("##### Waterfall Plot (alternativa didática)")
                    fig_wf, ax_wf = plt.subplots(figsize=(8, 6))
                    shap.plots.waterfall(
                        shap.Explanation(
                            values=shap_values[instance_idx],
                            base_values=expected_value,
                            data=X_shap[instance_idx],
                            feature_names=feature_names,
                        ),
                        show=False,
                    )
                    st.pyplot(fig_wf)
                    plt.close(fig_wf)
                except Exception:
                    pass
        else:
            st.warning("Não foi possível calcular SHAP values para este modelo.")

    # ------------------------------------------------------------------
    # LIME ANALYSIS
    # ------------------------------------------------------------------
    if use_lime and HAS_LIME:
        st.markdown("---")
        st.markdown("## 🔍 Análise LIME (Local Interpretable Model-agnostic Explanations)")
        st.markdown(
            "<div class='info-box'>"
            "<strong>LIME</strong> aproxima localmente o modelo complexo por um "
            "modelo linear interpretável na vizinhança da instância explicada. "
            "Útil para explicações rápidas e intuitivas."
            "</div>",
            unsafe_allow_html=True,
        )

        with st.spinner("Criando LIME explainer..."):
            try:
                if model_type == "LogisticRegression":
                    lime_explainer = lime.lime_tabular.LimeTabularExplainer(
                        X_train_scaled,
                        feature_names=feature_names,
                        class_names=["Não Reincidiu", "Reincidiu"],
                        mode="classification",
                        random_state=42,
                        discretize_continuous=True,
                    )
                    lime_data = X_test_scaled
                    lime_predict_fn = model.predict_proba
                else:
                    lime_explainer = lime.lime_tabular.LimeTabularExplainer(
                        X_train,
                        feature_names=feature_names,
                        class_names=["Não Reincidiu", "Reincidiu"],
                        mode="classification",
                        random_state=42,
                        discretize_continuous=True,
                    )
                    lime_data = X_test
                    lime_predict_fn = model.predict_proba
            except Exception as e:
                st.error(f"Erro ao criar LIME explainer: {e}")
                lime_explainer = None

        if lime_explainer is not None:
            lime_instance_idx = st.number_input(
                "Índice da instância para explicação LIME",
                0, X_test.shape[0] - 1, 5, 1, key="lime_idx",
            )

            try:
                exp = lime_explainer.explain_instance(
                    lime_data[lime_instance_idx],
                    lime_predict_fn,
                    num_features=len(feature_names),
                )

                st.markdown(
                    f"**Classe real:** {'Reincidiu' if y_test[lime_instance_idx] == 1 else 'Não reincidiu'}  |  "
                    f"**Prob. predita:** {y_prob[lime_instance_idx]:.3f}"
                )

                col_lime1, col_lime2 = st.columns(2)

                with col_lime1:
                    st.markdown("##### Tabela de Pesos Locais")
                    lime_list = exp.as_list()
                    lime_df = pd.DataFrame(
                        lime_list, columns=["Feature (condição)", "Peso"]
                    )
                    lime_df["Peso"] = lime_df["Peso"].round(4)
                    lime_df["Impacto"] = lime_df["Peso"].apply(
                        lambda x: "⬆ Favorece reincidência" if x > 0
                        else "⬇ Favorece não reincidência"
                    )
                    st.dataframe(lime_df, use_container_width=True)

                with col_lime2:
                    st.markdown("##### Gráfico de Barras LIME")
                    try:
                        fig_lime = exp.as_pyplot_figure()
                        if fig_lime:
                            fig_lime.suptitle(
                                f"LIME — Explicação Local (Instância {lime_instance_idx})",
                                fontsize=12, fontweight="bold",
                            )
                            st.pyplot(fig_lime)
                            plt.close(fig_lime)
                    except Exception:
                        st.info("Gráfico LIME não disponível.")

                st.markdown(
                    "<div class='warning-box'>"
                    "<strong>⚠️ Limitação:</strong> LIME pode ser instável entre execuções. "
                    "Para análises rigorosas, prefira SHAP (mais estável e fundamentado)."
                    "</div>",
                    unsafe_allow_html=True,
                )

            except Exception as e:
                st.error(f"Erro ao gerar explicação LIME: {e}")

    # ------------------------------------------------------------------
    # FAIRNESS METRICS
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("## ⚖️ Métricas de Fairness")
    st.markdown(
        "<div class='info-box'>"
        "<strong>Fairness</strong> não tem uma definição única. "
        "Calculamos aqui as métricas mais comuns para o atributo protegido <strong>Raça</strong> "
        "(0 = Não-Branco, 1 = Branco/privilegiado). "
        "<a href='https://fairmlbook.org' target='_blank'>Saiba mais</a>"
        "</div>",
        unsafe_allow_html=True,
    )

    group_test = X_test[:, feature_names.index("race")]

    metrics = compute_fairness_metrics(y_test, y_pred, y_prob, group_test, privileged_value=1)

    if "erro" in metrics:
        st.error(metrics["erro"])
    else:
        # Cartões de métricas
        mcol1, mcol2, mcol3, mcol4 = st.columns(4)

        with mcol1:
            di_ratio = metrics["di_ratio"]
            di_pass = metrics["di_pass"]
            st.markdown(
                f"<div class='metric-card {'metric-pass' if di_pass else 'metric-fail'}'>"
                f"<div class='metric-title'>Disparate Impact Ratio</div>"
                f"<div class='metric-value'>{di_ratio:.3f}</div>"
                f"<div class='metric-label'>{'✅ PASSOU (≥ 0.80)' if di_pass else '❌ FALHOU (< 0.80)'}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )

        with mcol2:
            eo_diff = metrics["eo_diff"]
            eo_pass = abs(eo_diff) < 0.05
            st.markdown(
                f"<div class='metric-card {'metric-pass' if eo_pass else 'metric-fail'}'>"
                f"<div class='metric-title'>Equal Opportunity Diff</div>"
                f"<div class='metric-value'>{eo_diff:.4f}</div>"
                f"<div class='metric-label'>{'✅ Baixa diferença' if eo_pass else '❌ Diferença significativa'}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )

        with mcol3:
            aod = metrics["avg_odds_diff"]
            aod_pass = abs(aod) < 0.05
            st.markdown(
                f"<div class='metric-card {'metric-pass' if aod_pass else 'metric-fail'}'>"
                f"<div class='metric-title'>Average Odds Diff</div>"
                f"<div class='metric-value'>{aod:.4f}</div>"
                f"<div class='metric-label'>{'✅ Baixa diferença' if aod_pass else '❌ Diferença significativa'}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )

        with mcol4:
            dp_diff = metrics["dp_diff"]
            dp_pass = abs(dp_diff) < 0.05
            st.markdown(
                f"<div class='metric-card {'metric-pass' if dp_pass else 'metric-fail'}'>"
                f"<div class='metric-title'>Demographic Parity Diff</div>"
                f"<div class='metric-value'>{dp_diff:.4f}</div>"
                f"<div class='metric-label'>{'✅ Próximo de 0' if dp_pass else '❌ Diferença significativa'}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )

        # Tabela detalhada
        st.markdown("##### 📋 Detalhamento por Grupo")
        fairness_detail_df = pd.DataFrame(
            {
                "Métrica": [
                    "Taxa de Predição Positiva",
                    "True Positive Rate (TPR)",
                    "False Positive Rate (FPR)",
                ],
                "Brancos (Privilegiado)": [
                    f"{metrics['pred_rate_priv']:.3f}",
                    f"{metrics['tpr_priv']:.3f}",
                    f"{metrics['fpr_priv']:.3f}",
                ],
                "Não-Brancos (Desprivilegiado)": [
                    f"{metrics['pred_rate_unpriv']:.3f}",
                    f"{metrics['tpr_unpriv']:.3f}",
                    f"{metrics['fpr_unpriv']:.3f}",
                ],
                "Diferença": [
                    f"{metrics['dp_diff']:.3f}",
                    f"{metrics['eo_diff']:.3f}",
                    f"{metrics['fpr_unpriv'] - metrics['fpr_priv']:.3f}",
                ],
            }
        )
        st.dataframe(fairness_detail_df, use_container_width=True)

        # Gráficos de fairness
        fcol1, fcol2 = st.columns(2)
        with fcol1:
            fig_grp = plot_group_rates(
                y_pred, group_test,
                group_names=["Não-Brancos", "Brancos"],
            )
            if fig_grp:
                st.pyplot(fig_grp)
                plt.close(fig_grp)

        with fcol2:
            fig_roc = plot_roc_curve(y_test, y_prob, "Curva ROC")
            if fig_roc:
                st.pyplot(fig_roc)
                plt.close(fig_roc)

        # Interpretação detalhada
        with st.expander("📖 Interpretação das Métricas de Fairness"):
            st.markdown("""
            **Disparate Impact Ratio (Regra dos 80%)**
            - Mede a razão entre a taxa de predição positiva do grupo desprivilegiado e do grupo privilegiado.
            - **DI ≥ 0.80**: Aceitável (sem impacto desproporcional).
            - **DI < 0.80**: Evidência de impacto adverso (discriminação).
            - No COMPAS, DI costuma ficar entre 0.60-0.75, indicando que não-brancos são classificados como reincidentes com maior frequência.

            **Equal Opportunity Difference**
            - Diferença na True Positive Rate (TPR) entre grupos.
            - Ideal: 0 (o modelo identifica corretamente reincidentes reais com a mesma taxa).
            - Se > 0: grupo privilegiado tem mais verdadeiros positivos.

            **Equalized Odds (Average Odds Difference)**
            - Média das diferenças de TPR e FPR entre grupos.
            - Foi a métrica usada pela ProPublica para demonstrar viés no COMPAS.
            - Ideal: 0.

            **Demographic Parity Difference**
            - Diferença simples na taxa de predição positiva entre grupos.
            - Ideal: 0.

            > ⚠️ **Atenção:** Não é possível maximizar todas as métricas simultaneamente.
            > A escolha de qual métrica priorizar é uma decisão ética e política
            > (Kleinberg et al., 2017).
            """)

    # ------------------------------------------------------------------
    # MITIGAÇÃO DE VIÉS
    # ------------------------------------------------------------------
    if use_mitigation:
        st.markdown("---")
        st.markdown("## 🛠️ Mitigação de Viés")

        metrics_after = None

        if mitigation_method == "Reweighing (pré-processamento)":
            with st.spinner("Aplicando Reweighing..."):
                group_train = X_train[:, feature_names.index("race")]
                weights, msg = apply_reweighing(
                    X_train, y_train, group_train, privileged_value=1
                )
                st.info(msg)

                # Retreinar com pesos
                if model_type == "LogisticRegression":
                    model_mit = LogisticRegression(
                        C=params.get("C", 1.0), max_iter=params.get("max_iter", 1000),
                        random_state=42, n_jobs=-1,
                    )
                    model_mit.fit(X_train_scaled, y_train, sample_weight=weights)
                else:
                    if model_type == "RandomForest":
                        model_mit = RandomForestClassifier(
                            n_estimators=params.get("n_estimators", 100),
                            max_depth=params.get("max_depth", 10),
                            random_state=42, n_jobs=-1,
                        )
                    elif model_type == "XGBoost" and HAS_XGB:
                        model_mit = xgb.XGBClassifier(
                            n_estimators=params.get("n_estimators", 100),
                            max_depth=params.get("max_depth", 6),
                            random_state=42, n_jobs=-1, eval_metric="logloss",
                        )
                    else:
                        model_mit = RandomForestClassifier(
                            n_estimators=100, random_state=42, n_jobs=-1,
                        )
                    model_mit.fit(X_train, y_train, sample_weight=weights)

                if model_type == "LogisticRegression":
                    y_pred_mit = model_mit.predict(X_test_scaled)
                    y_prob_mit = model_mit.predict_proba(X_test_scaled)[:, 1]
                else:
                    y_pred_mit = model_mit.predict(X_test)
                    y_prob_mit = model_mit.predict_proba(X_test)[:, 1]

                metrics_after = compute_fairness_metrics(
                    y_test, y_pred_mit, y_prob_mit, group_test, privileged_value=1
                )

        elif mitigation_method == "Threshold Optimizer (pós-processamento)":
            if HAS_FAIRLEARN:
                with st.spinner("Aplicando ThresholdOptimizer..."):
                    try:
                        group_train = X_train[:, feature_names.index("race")]
                        group_test_fairlearn = group_test

                        threshold_opt = ThresholdOptimizer(
                            estimator=model,
                            constraints="equalized_odds",
                            objective="accuracy",
                            predict_method="predict_proba" if model_type == "LogisticRegression"
                            else "predict_proba",
                            prefit=True,
                        )

                        threshold_opt.fit(
                            X_train if model_type != "LogisticRegression" else X_train_scaled,
                            y_train,
                            sensitive_features=group_train,
                        )

                        y_pred_mit = threshold_opt.predict(
                            X_test if model_type != "LogisticRegression" else X_test_scaled,
                            sensitive_features=group_test_fairlearn,
                            random_state=42,
                        )
                        y_prob_mit = y_prob  # mantém probs originais

                        metrics_after = compute_fairness_metrics(
                            y_test, y_pred_mit, y_prob_mit, group_test, privileged_value=1
                        )
                    except Exception as e:
                        st.error(f"Erro no ThresholdOptimizer: {e}")
                        st.info(
                            "ThresholdOptimizer requer fairlearn instalado e modelo "
                            "com predict_proba."
                        )
            else:
                st.warning(
                    "Fairlearn não instalado. pip install fairlearn"
                )

        if metrics_after:
            # Comparação
            st.markdown("### 📊 Comparação Antes vs. Depois da Mitigação")

            comp_cols = ["Métrica", "Antes", "Depois", "Melhora"]
            comp_data = [
                ["Disparate Impact Ratio",
                 f"{metrics.get('di_ratio', 0):.4f}",
                 f"{metrics_after.get('di_ratio', 0):.4f}",
                 f"{metrics_after.get('di_ratio', 0) - metrics.get('di_ratio', 0):+.4f}"],
                ["Equal Opportunity Diff",
                 f"{metrics.get('eo_diff', 0):.4f}",
                 f"{metrics_after.get('eo_diff', 0):.4f}",
                 f"{abs(metrics.get('eo_diff', 0)) - abs(metrics_after.get('eo_diff', 0)):+.4f}"],
                ["Avg Odds Diff",
                 f"{metrics.get('avg_odds_diff', 0):.4f}",
                 f"{metrics_after.get('avg_odds_diff', 0):.4f}",
                 f"{abs(metrics.get('avg_odds_diff', 0)) - abs(metrics_after.get('avg_odds_diff', 0)):+.4f}"],
                ["Acurácia",
                 f"{metrics.get('acc', 0):.4f}",
                 f"{metrics_after.get('acc', 0):.4f}",
                 f"{metrics_after.get('acc', 0) - metrics.get('acc', 0):+.4f}"],
            ]
            comp_df = pd.DataFrame(comp_cols[1:]).T
            comp_df = pd.DataFrame(comp_data, columns=comp_cols)
            st.dataframe(comp_df, use_container_width=True)

            fig_comp = plot_fairness_comparison(metrics, metrics_after, group_names=["Não-Brancos", "Brancos"])
            if fig_comp:
                st.pyplot(fig_comp)
                plt.close(fig_comp)

            st.markdown(
                "<div class='info-box'>"
                "<strong>Nota:</strong> Mitigação de viés geralmente envolve "
                "um trade-off com acurácia. Observe se a acurácia caiu e se as "
                "métricas de fairness melhoraram."
                "</div>",
                unsafe_allow_html=True,
            )

    # ------------------------------------------------------------------
    # EXPORTAR RELATÓRIO
    # ------------------------------------------------------------------
    st.markdown("---")
    st.markdown("## 📤 Exportar Relatório")

    fairness_df_export = None
    try:
        fairness_df_export = pd.DataFrame(
            {
                "Métrica": ["DI Ratio", "DP Diff", "EO Diff", "Avg Odds Diff"],
                "Valor": [
                    f"{metrics.get('di_ratio', 0):.4f}",
                    f"{metrics.get('dp_diff', 0):.4f}",
                    f"{metrics.get('eo_diff', 0):.4f}",
                    f"{metrics.get('avg_odds_diff', 0):.4f}",
                ],
            }
        )
    except Exception:
        pass

    html_report = generate_html_report(
        metrics, fairness_df_export, model_type, dataset_info
    )

    b64 = base64.b64encode(html_report.encode("utf-8")).decode("utf-8")
    href = f'<a href="data:text/html;base64,{b64}" download="relatorio_fairness_{model_type}.html">\
        <button style="background:#1E3A5F;color:white;padding:10px 20px;border:none;\
        border-radius:5px;cursor:pointer;">📥 Baixar Relatório HTML</button></a>'
    st.markdown(href, unsafe_allow_html=True)

    st.markdown(
        "<div style='text-align:center; color:#999; font-size:0.9rem; margin-top: 3rem;'>"
        "XAI & Fairness Simulator v1.0 | Dataset COMPAS (ProPublica) | "
        "Maio 2026"
        "</div>",
        unsafe_allow_html=True,
    )


# ============================================================================
# ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    main()
