---
title: "Explainable AI (XAI)"
area: "AI"
tags: [conhecimento, conceito, xai, explicabilidade, interpretabilidade, ia-explicavel, trustworthiness, skills]
related: ["Machine-Learning-Fundamentos", "Etica-em-IA", "EU-AI-Act"]
aliases: ["XAI", "Interpretable ML", "Explainable Machine Learning", "Explainability"]
created: 2026-05-19
updated: 2026-06-07
date: 2026-06-01
---

# Explainable AI (XAI)

## Definição

Explainable AI (XAI) é o campo da Inteligência Artificial que busca tornar modelos de machine learning interpretáveis e explicáveis para seres humanos. Diferentemente de modelos caixa-preta (black-box) que produzem predições sem justificativa transparente, sistemas XAI fornecem insights sobre **por que** uma decisão foi tomada, **como** o modelo chegou a uma conclusão e **quais** fatores foram mais relevantes.

## Interpretabilidade vs Explicabilidade

| Conceito | Definição |
|----------|-----------|
| **Interpretabilidade (intrínseca)** | Capacidade de um modelo ser compreendido diretamente por humanos sem necessidade de métodos auxiliares. Modelos intrinsecamente interpretáveis incluem árvores de decisão, regressão linear e GLMs. |
| **Explicabilidade (post-hoc)** | Conjunto de técnicas aplicadas **após** o treinamento para elucidar o comportamento de modelos que não são naturalmente interpretáveis (redes neurais, gradient boosting, ensembles). |

## Importância

- **Confiança:** Usuários e stakeholders precisam confiar nas decisões automatizadas.
- **Auditoria:** Reguladores exigem rastreabilidade de decisões algorítmicas.
- **Regulamentação:**
  - **EU AI Act:** Classifica sistemas de IA por risco; modelos de alto risco exigem documentação de explicabilidade.
  - **LGPD (Brasil):** Art. 20 garante ao titular o direito de solicitar revisão de decisões automatizadas.
  - **GDPR (Europa):** Direito à explicação sobre decisões automatizadas (Art. 22).
- **Fairness:** Identificar e corrigir vieses embutidos nos dados ou no modelo.
- **Segurança:** Detectar adversarial attacks, data poisoning e conceitos espúrios.
- **Diagnóstico:** Depurar erros, identificar overfitting e melhorar performance.

## Métodos Intrínsecos (Interpretáveis por Natureza)

- **Árvores de Decisão:** Estrutura hierárquica de regras if-then-else; completamente transparente.
- **Regressão Linear:** Pesos das features indicam contribuição direta (coeficientes).
- **Generalized Linear Models (GLM):** Extensão da regressão linear para diferentes distribuições.
- **Modelos Baseados em Regras:** Sistemas como RIPPER, OneR, rule lists.
- **Modelos Aditivos Generalizados (GAM):** Soma de funções suaves univariadas, mantendo interpretabilidade.
- **K-Nearest Neighbors (KNN):** Decisão baseada em exemplos vizinhos — intrinsecamente explicável por similaridade.

*Trade-off:* Modelos intrinsecamente interpretáveis geralmente sacrificam acurácia em datasets complexos.

## Métodos Post-Hoc

### LIME (Local Interpretable Model-agnostic Explanations)

*Ribeiro, Singh & Guestrin (2016)*

- **Funcionamento:** Aproxima o modelo global com um modelo simples (regressão linear) na vizinhança local de uma predição específica.
- **Características:** Model-agnostic (funciona com qualquer classificador), gera explicações locais.
- **Limitações:** Instabilidade entre execuções (diferentes amostragens podem gerar explicações distintas); definição arbitrária de vizinhança.

### SHAP (Shapley Additive Explanations)

*Lundberg & Lee (2017)*

- **Fundamentação:** Baseado em valores de Shapley da teoria dos jogos cooperativos.
- **Propriedades:** Único método que garante consistência, eficiência, simetria e dummy (propriedades desejáveis de atribuição).
- **Variações:** KernelSHAP (model-agnostic, lento), TreeSHAP (rápido para modelos baseados em árvores), DeepSHAP (para redes neurais).
- **Saída:** Gráfico de barras (feature importance global), summary plot (distribuição por classe), dependence plot (relação feature-predição), force plot (explicação local).

### Grad-CAM (Gradient-weighted Class Activation Mapping)

*Selvaraju et al. (2017)*

- **Domínio:** Visão computacional (CNNs).
- **Funcionamento:** Usa gradientes da saída em relação aos mapas de ativação da última camada convolucional para produzir um heatmap de relevância.
- **Saída:** Mapa de calor sobreposto à imagem original indicando quais regiões foram mais importantes para a decisão.
- **Variações:** Grad-CAM++, Score-CAM, Ablation-CAM.

### Integrated Gradients

*Sundararajan, Taly & Yan (2017)*

- **Funcionamento:** Calcula a integral do gradiente ao longo do caminho linear de uma linha de base (baseline, ex: imagem preta) até a entrada original.
- **Propriedades:** Satisfaz sensibilidade e invariância por implementação.
- **Aplicação:** Imagens, texto, modelos tabulares.

### Attention Visualization

- **Contexto:** Modelos Transformer (BERT, GPT, ViT).
- **Funcionamento:** Pesos de atenção indicam a importância relativa entre tokens em cada camada.
- **Ferramentas:** BertViz (Vig 2019), exBERT (Hoover 2020), attention rollout (Abnar & Zuidema 2020).
- **Limitações:** Atenção **não** é explicação por si só (Jain & Wallace 2019); pode ser manipulada.

### TCAV (Testing with Concept Activation Vectors)

*Kim et al. (2018)*

- **Funcionamento:** Testa se um conceito de alto nível (ex: "listrado", "médico") é importante para a predição treinando classificadores lineares em ativações intermediárias.
- **Vantagem:** Não requer rótulos para os conceitos; permite explicações em linguagem natural ("o modelo usou o conceito listrado para classificar zebra").
- **Limitação:** Requer definição externa dos conceitos e dados de exemplo.

### LRP (Layer-wise Relevance Propagation)

*Bach et al. (2015)*

- **Funcionamento:** Propaga a relevância da saída para a entrada através de regras de conservação locais.
- **Aplicação:** Redes neurais profundas em geral.

## Técnicas por Tipo de Modelo

### Modelos Tabulares

| Técnica | Descrição |
|---------|-----------|
| **LIME** | Explicações locais com modelo substituto linear |
| **SHAP** | Atribuição baseada em valores de Shapley |
| **PDP (Partial Dependence Plot)** | Efeito marginal de uma feature na predição |
| **ICE (Individual Conditional Expectation)** | PDP individualizado por instância |
| **Permutation Importance** | Queda na performance ao permutar uma feature |
| **ALE (Accumulated Local Effects)** | Alternativa ao PDP sem viés de correlação |

### Imagens

| Técnica | Descrição |
|---------|-----------|
| **Grad-CAM** | Heatmap na última camada convolucional |
| **Saliency Maps** | Magnitude do gradiente em relação a cada pixel |
| **Integrated Gradients** | Gradiente acumulado da baseline até a entrada |
| **LRP** | Propagação de relevância camada a camada |
| **Guided Backpropagation** | Gradientes com apenas fluxo positivo |
| **Occlusion Sensitivity** | Importância medida pela queda de confiança ao ocluir regiões |
| **RISE (Randomized Input Sampling)** | Amostragem aleatória de máscaras |

### Texto

| Técnica | Descrição |
|---------|-----------|
| **Attention Visualization** | Pesos de atenção entre tokens |
| **LIME** | Palavras mais influentes para a predição |
| **SHAP** | Atribuição a tokens individuais |
| **Erasure Search** | Remoção sistemática de tokens e medição do impacto |
| **Integrated Gradients** | Gradientes acumulados por token |
| **Contextual Decomposition** | Decomposição da contribuição de cada token |

### Grafos (GNNs)

| Técnica | Descrição |
|---------|-----------|
| **GNNExplainer (Ying et al. 2019)** | Subgrafo e subconjunto de features mais importantes |
| **GNN-LRP** | Propagação de relevância em GNNs |
| **PGExplainer** | Explicações paramétricas em subgrafos |
| **GraphMask** | Máscara de arestas para explicação |

## Global vs Local Explanations

| Dimensão | Local | Global |
|----------|-------|--------|
| **Escopo** | Uma única predição | Comportamento geral do modelo |
| **Exemplo** | "Este cliente foi negado porque renda < R$ 3000" | "Renda é a feature mais importante do modelo" |
| **Métodos** | LIME, SHAP (force plot) | SHAP summary, Permutation Importance, PDP |
| **Utilidade** | Depuração, contestação, auditoria individual | Compliance, documentação, entendimento geral |

## Faithfulness vs Comprehensibility

- **Faithfulness (Fidelidade):** Quão precisamente a explicação reflete o comportamento real do modelo.
  - Métricas: Infidelity (Yeh 2019), sufficiency, comprehensiveness.
  - Explicação pode ser fiel mas incompreensível.
- **Comprehensibility (Compreensibilidade):** Quão fácil é para um humano entender a explicação.
  - Explicação pode ser compreensível mas infiel (ex: árvore de decisão aproximando uma rede neural).
- **Trade-off fundamental:** Explicações mais fiéis tendem a ser mais complexas e vice-versa.

## Explainability vs Privacy

- **Trade-off:** Explicações detalhadas podem vazar informações sobre dados de treinamento.
  - Model inversion attacks: usar explicações para reconstruir dados de treino.
  - Membership inference: determinar se um exemplo estava no conjunto de treino.
- **Mitigações:**
  - Diferential privacy durante o treinamento.
  - Explicações agregadas (não individuais).
  - Limitar granularidade das explicações.

## Ferramentas

| Ferramenta | Framework | Destaque |
|------------|-----------|----------|
| **Captum** | PyTorch | Integrated Gradients, DeepLIFT, SmoothGrad, LRP |
| **Alibi** (Seldon) | Model-agnostic | Anchor, Counterfactuals, CEM, PDP, ALE |
| **Eli5** | Scikit-learn, XGBoost, Keras | Permutation Importance, LIME-like |
| **InterpretML** (Microsoft) | Multi-framework | Glassbox (EBM), Blackbox (SHAP, LIME) |
| **What-If Tool** (Google) | TensorFlow | Visualização interativa, fairness, contrafactuais |
| **Shapash** | Multi-framework | Dashboard interativo de explicações |
| **Dalex** (MI2) | R & Python | Conjunto unificado de explicações |
| **XAI Library** (IBM) | Multi-framework | Algoritmos clássicos de XAI |

## Explainability em LLMs

### Chain-of-Thought (CoT)
- Modelos geram raciocínio passo-a-passo antes da resposta final.
- *Wei et al. (2022)* — permite interpretar o raciocínio lógico.
- Limitação: modelo pode gerar raciocínio **incorreto** mas aparentemente coerente (post-hoc rationalization).

### Probing
- Classificadores supervisionados treinados em ativações intermediárias para detectar propriedades linguísticas.
- Ex: probing para POS tagging, relações sintáticas, informações factuais.

### Activation Steering
- Modificação direcionada de ativações internas durante a inferência para alterar comportamento.
- Técnicas: activation patching, representation engineering (RepE).

### Sparse Autoencoders (SAE)
- Decomposição de ativações em features esparsas monosemânticas.
- *Elhage et al. (2022), Bricken et al. (2023)* — base da mechanistic interpretability moderna.
- Ferramentas: SAELens, TransformerLens.

### Mechanistic Interpretability
- **Objetivo:** Engenharia reversa completa do modelo — descobrir circuitos neurais responsáveis por comportamentos específicos.
- **Circuitos:** "indirect object identification" (IOI), "greater-than", "docstring" em transformers.
- **Limitação:** Escala — extremamente trabalhoso; não escala para modelos > 7B parâmetros atualmente.

### Logit Lens
- Projetar ativações intermediárias no vocabulary space para ver predições parciais em cada camada.
- *nostalgebraist (2020)* — técnica simples mas reveladora.

## Pesquisadores-Chave

| Pesquisador(a) | Contribuição |
|----------------|--------------|
| **Cynthia Rudin** | Defensora de modelos interpretáveis por design; crítica ao uso de black-box em high-stakes (saúde, justiça) |
| **Been Kim** | TCAV; explicabilidade em redes profundas; interpretability no Google Brain |
| **Scott Lundberg** | SHAP; fundamentos teóricos de atribuição |
| **Marco Ribeiro** | LIME; Anchor explanations |
| **Finale Doshi-Velez** | Estruturas teóricas para interpretabilidade; avaliação de explicações |
| **Chris Olah** | Visualização de redes neurais; distill.pub; mechanistic interpretability |
| **Ramprasaath Selvaraju** | Grad-CAM |
| **Mukund Sundararajan** | Integrated Gradients |
| **David Bau** | Network dissection; intervenções causais em redes |

## Desafios

- **Modelos black-box:** Redes neurais profundas, ensembles e LLMs são intrinsecamente opacos.
- **Trade-off acurácia-explicabilidade:** Modelos mais acurados tendem a ser menos interpretáveis. *Rudin (2019)* argumenta que em high-stakes domains não há trade-off — modelos interpretáveis podem ser tão acurados quanto.
- **Explicações contraditórias:** Diferentes métodos XAI podem produzir explicações conflitantes para a mesma predição.
- **Explicações manipuláveis:** Adversarial attacks podem enganar sistemas XAI (Heo et al. 2019).
- **Avaliação de explicações:** Falta de ground truth para explicabilidade; métricas subjetivas.
- **Escala:** Explicar modelos com bilhões de parâmetros (LLMs) é computacionalmente caro.

## Conexões

- [[Machine-Learning-Fundamentos]] — base conceitual de ML
- [[Etica-em-IA]] — fairness, viés, transparência
- [[EU-AI-Act]] — regulamentação europeia
- [[LLM-Fine-Tuning]] — explicabilidade em modelos de linguagem
- [[MLOps]] — monitoramento e Governança de modelos
- [[Teoria-dos-Jogos]] — fundamento matemático do SHAP

---

*"Explainability is not a property of a model, but a property of a relationship between a model and a human." — Finale Doshi-Velez*

[[skills/README|← Voltar à Taxonomia de Skills]]
