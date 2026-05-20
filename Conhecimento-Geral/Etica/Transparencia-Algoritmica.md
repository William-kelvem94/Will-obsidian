---
title: "Transparência Algorítmica"
area: "Ética"
related: ["Explainable AI", "Responsabilidade", "Deontologia", "Interpretabilidade"]
embeddings_model: "all-MiniLM-L6-v2"
tags: [conhecimento, conceito, etica, transparencia, xai, lime, shap, explicabilidade]
updated: 2026-05-16
---

# Transparência Algorítmica

## Visão Geral

Transparência algorítmica refere-se ao princípio e à prática de tornar sistemas de inteligência artificial compreensíveis, auditáveis e explicáveis para seres humanos. Em sua formulação mais forte, a transparência exige que para qualquer decisão tomada por um sistema automatizado, seja possível fornecer uma **explicação inteligível** dos fatores que levaram àquela decisão.

O campo é governado por duas tensões fundamentais:

1. **Precisão vs. Interpretabilidade**: Modelos mais precisos tendem a ser menos interpretáveis, enquanto modelos interpretáveis tendem a ser menos precisos.
2. **Privacidade vs. Transparência**: Explicações detalhadas podem expor informações sensíveis sobre o modelo ou os dados de treinamento.

### Dimensões da Transparência

| Dimensão | Descrição | Exemplo |
|----------|-----------|---------|
| Transparência de design | Arquitetura documentada | Publicação de whitepapers |
| Transparência de processo | Dados e treinamento auditáveis | Proveniência de dados |
| Transparência de decisão | Explicação por decisão | LIME para cada predição |
| Transparência pós-hoc | Análise após treinamento | SHAP values |
| Transparência sistêmica | Impacto sociotécnico | Auditoria de viés |

## O Problema da Caixa-Preta

### Definição

O "black box problem" em IA refere-se à incapacidade de inspecionar internamente o processo de tomada de decisão de modelos complexos. Uma rede neural com milhões de parâmetros aprende representações que não são diretamente interpretáveis por humanos.

**Causas do problema:**
- **Alta dimensionalidade**: Milhares/milhões de features internas
- **Não-linearidade**: Interações complexas entre parâmetros
- **Representações latentes**: Features aprendidas não correspondem a conceitos humanos
- **Emergência**: Comportamento complexo surge de componentes simples

```python
import numpy as np

class BlackBoxModel:
    def __init__(self):
        np.random.seed(42)
        self.W1 = np.random.randn(100, 256) * 0.01
        self.b1 = np.zeros(256)
        self.W2 = np.random.randn(256, 128) * 0.01
        self.b2 = np.zeros(128)
        self.W3 = np.random.randn(128, 1) * 0.01
        self.b3 = np.zeros(1)
    
    def predict(self, x):
        h1 = np.maximum(0, np.dot(x, self.W1) + self.b1)
        h2 = np.maximum(0, np.dot(h1, self.W2) + self.b2)
        output = np.dot(h2, self.W3) + self.b3
        return output.squeeze()
    
    def internals(self, x):
        h1 = np.maximum(0, np.dot(x, self.W1) + self.b1)
        h2 = np.maximum(0, np.dot(h1, self.W2) + self.b2)
        return {
            'layer_1_stats': {'mean': h1.mean(), 'std': h1.std(), 'sparsity': (h1 == 0).mean()},
            'layer_2_stats': {'mean': h2.mean(), 'std': h2.std(), 'sparsity': (h2 == 0).mean()},
            'note': 'Representacoes sem correspondencia com conceitos humanos'
        }
```

### Por que a Caixa-Preta é Problemática?

1. **Viés e discriminação**: Sem transparência, vieses permanecem ocultos (COMPAS, Amazon hiring).
2. **Responsabilidade**: Não podemos atribuir responsabilidade por decisões que não entendemos.
3. **Segurança**: Vulnerabilidades adversariais não são detectáveis.
4. **Confiança**: Usuários não confiam em sistemas que não entendem.
5. **Regulação**: Leis como GDPR exigem explicações.

## Interpretabilidade vs. Explicabilidade

### Distinção Conceitual

| Propriedade | Interpretabilidade | Explicabilidade |
|-------------|-------------------|-----------------|
| Definição | Grau em que um humano entende o funcionamento do modelo | Grau em que decisões específicas podem ser justificadas |
| Escopo | Global (modelo inteiro) | Local (decisão individual) |
| Métodos | Árvores de decisão, regressão linear | LIME, SHAP, GradCAM |
| Momento | Antes do treinamento (intrínseca) | Após treinamento (pós-hoc) |
| Requisito | Modelo simples o suficiente | Método de aproximação |

**Interpretabilidade intrínseca**: O modelo é compreensível por si só (regressão linear, árvores rasas).

**Explicabilidade pós-hoc**: O modelo é complexo, mas geramos explicações externas (SHAP para redes neurais).

```python
class InterpretabilityFramework:
    def __init__(self):
        self.methods = {'intrinsic': [], 'post_hoc': []}
    
    def classify_method(self, method):
        if method['type'] == 'intrinsic':
            return {
                'category': 'Interpretabilidade intrinseca',
                'description': 'Modelo compreensivel por si so',
                'advantage': 'Explicacao fiel ao modelo',
                'disadvantage': 'Pode sacrificar precisao'
            }
        elif method['type'] == 'post_hoc':
            return {
                'category': 'Explicabilidade pos-hoc',
                'description': 'Explicacao gerada apos treinamento',
                'advantage': 'Funciona com qualquer modelo',
                'disadvantage': 'Apenas aproximacao do comportamento'
            }
    
    def tradeoff_analysis(self, task_requirements):
        if task_requirements.get('need_high_stakes_explanation'):
            return 'Preferir interpretabilidade intrinseca (ex: saude, justica)'
        elif task_requirements.get('need_high_accuracy'):
            return 'Preferir modelo complexo com explicacoes pos-hoc'
        return 'Equilibrio entre ambos'
```

## Métodos Principais de Explicabilidade

### 1. LIME (Local Interpretable Model-agnostic Explanations)

Proposto por Ribeiro, Singh & Guestrin (2016), o LIME aproxima localmente o modelo complexo $f$ por um modelo interpretável $g$ na vizinhança de uma predição específica.

**Formulação:**

$$
\xi(x) = \arg\min_{g \in \mathcal{G}} \mathcal{L}(f, g, \pi_x) + \Omega(g)
$$

Onde $f$ é o modelo original, $g$ o modelo interpretável, $\pi_x$ a medida de proximidade em torno de $x$, e $\Omega(g)$ penaliza a complexidade de $g$.

**Algoritmo:**
1. Selecione a instância $x$ a ser explicada
2. Gere perturbações $z$ em torno de $x$
3. Obtenha predições $f(z)$ para cada perturbação
4. Pese as perturbações pela proximidade a $x$
5. Treine modelo $g$ nos dados perturbados ponderados
6. Retorne coeficientes de $g$ como explicação

```python
import numpy as np
from sklearn.linear_model import Ridge

class LIMEExplainer:
    def __init__(self, feature_names, categorical_features=None, kernel_width=0.75):
        self.feature_names = feature_names
        self.categorical_features = categorical_features or []
        self.kernel_width = kernel_width
    
    def explain_instance(self, model, instance, num_features=5, num_samples=5000):
        n_features = len(instance)
        
        # 1. Gerar perturbacoes
        perturbations = self._generate_perturbations(instance, num_samples)
        
        # 2. Obter predicoes do modelo original
        predictions = model.predict(perturbations)
        
        # 3. Calcular similaridade com a instancia original
        distances = self._compute_distances(instance, perturbations)
        weights = np.exp(-distances / (self.kernel_width ** 2))
        
        # 4. Treinar modelo interpretavel ponderado
        local_model = Ridge(alpha=1.0)
        local_model.fit(perturbations, predictions, sample_weight=weights)
        
        # 5. Extrair features mais importantes
        coefs = local_model.coef_
        feature_importance = [
            (self.feature_names[i], coefs[i])
            for i in range(n_features)
        ]
        feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)
        
        return {
            'feature_importance': feature_importance[:num_features],
            'original_prediction': model.predict([instance])[0],
            'local_model_r2': local_model.score(perturbations, predictions, sample_weight=weights)
        }
    
    def _generate_perturbations(self, instance, n):
        n_features = len(instance)
        perturbations = np.zeros((n, n_features))
        for i in range(n_features):
            if i in self.categorical_features:
                perturbations[:, i] = np.random.binomial(1, instance[i], n)
            else:
                mean = instance[i]
                std = max(0.1, abs(mean) * 0.2)
                perturbations[:, i] = np.random.normal(mean, std, n)
        return perturbations
    
    def _compute_distances(self, instance, perturbations):
        return np.array([np.linalg.norm(instance - p) for p in perturbations])
```

### 2. SHAP (SHapley Additive exPlanations)

Proposto por Lundberg & Lee (2017), o SHAP usa valores de Shapley da teoria dos jogos cooperativos para atribuir importância a cada feature.

**Valor de Shapley:**

$$
\phi_i = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!(|N|-|S|-1)!}{|N|!} [f(S \cup \{i\}) - f(S)]
$$

O valor $\phi_i$ é a contribuição marginal média da feature $i$ sobre todas as possíveis coalizões $S$ de features.

**Propriedades desejáveis:**
1. **Eficiência**: $\sum_i \phi_i = f(x) - \mathbb{E}[f(X)]$
2. **Simetria**: Se $i$ e $j$ contribuem igualmente, $\phi_i = \phi_j$
3. **Dummy**: Se $i$ nunca contribui, $\phi_i = 0$
4. **Aditividade**: Para modelos somados, valores de Shapley se somam

```python
import itertools
import numpy as np

class SHAPExplainer:
    def __init__(self, model, feature_names):
        self.model = model
        self.feature_names = feature_names
        self.n_features = len(feature_names)
    
    def shap_values(self, instance, background_data=None):
        if background_data is None:
            expected_value = 0.5
        else:
            expected_value = np.mean(self.model.predict(background_data))
        
        n = self.n_features
        shap_values = np.zeros(n)
        features = list(range(n))
        
        for i in range(n):
            shap_i = 0
            other_features = [f for f in features if f != i]
            
            for r in range(n):
                for subset in itertools.combinations(other_features, r):
                    s = set(subset)
                    s_size = len(s)
                    
                    x_without = self._mask_features(instance, s)
                    val_without = self.model.predict([x_without])[0]
                    
                    s_with_i = s | {i}
                    x_with = self._mask_features(instance, s_with_i)
                    val_with = self.model.predict([x_with])[0]
                    
                    marginal = val_with - val_without
                    weight = (np.math.factorial(s_size) *
                             np.math.factorial(n - s_size - 1)) / np.math.factorial(n)
                    shap_i += weight * marginal
            
            shap_values[i] = shap_i
        
        feature_importance = list(zip(self.feature_names, shap_values))
        feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)
        
        return {
            'expected_value': expected_value,
            'shap_values': shap_values,
            'feature_importance': feature_importance,
            'prediction': self.model.predict([instance])[0]
        }
    
    def _mask_features(self, instance, feature_set):
        masked = instance.copy()
        reference = np.mean(instance)
        for f in range(self.n_features):
            if f not in feature_set:
                masked[f] = reference
        return masked
    
    def summary_plot(self, X, max_features=10):
        all_shap = np.array([self.shap_values(x)['shap_values'] for x in X])
        mean_abs_shap = np.mean(np.abs(all_shap), axis=0)
        features_sorted = sorted(
            zip(self.feature_names, mean_abs_shap),
            key=lambda x: x[1], reverse=True
        )[:max_features]
        return {'global_feature_importance': features_sorted}
```

### 3. GradCAM (Gradient-weighted Class Activation Mapping)

Selvaraju et al. (2017) propuseram o GradCAM para visualizar quais regiões de uma imagem são relevantes para a decisão de uma CNN.

**Procedimento:**
1. Calcule o gradiente da classe alvo $y^c$ nos mapas de ativação $A^k$
2. Pondere os mapas pelos gradientes médios: $\alpha_k^c = \frac{1}{Z} \sum_i \sum_j \frac{\partial y^c}{\partial A_{ij}^k}$
3. Compute o mapa de calor: $L_{GradCAM}^c = ReLU(\sum_k \alpha_k^c A^k)$

```python
import numpy as np

class GradCAMExplainer:
    def __init__(self, model, target_layer):
        self.model = model
        self.target_layer = target_layer
        self.gradients = None
        self.activations = None
    
    def generate_heatmap(self, image, class_idx=None):
        # Forward pass (simplificado)
        output = self.model(image)
        if class_idx is None:
            class_idx = output.argmax()
        
        # Simulacao de gradientes e mapa de calor
        h, w = image.shape[2:] if len(image.shape) == 4 else (224, 224)
        cam = np.random.rand(h // 8, w // 8) * 0.3
        cam[h//4:3*h//4, w//4:3*w//4] += 0.5
        cam = np.maximum(cam, 0)
        cam = (cam - cam.min()) / (cam.max() - cam.min() + 1e-8)
        
        return {
            'heatmap': cam,
            'class_idx': class_idx,
            'heatmap_shape': cam.shape,
            'most_active_region': np.unravel_index(cam.argmax(), cam.shape)
        }
```

### 4. Outros Métodos

| Método | Tipo | Descrição |
|--------|------|-----------|
| **Anchors** (Ribeiro et al., 2018) | Regras | Regras "se-então" que garantem predição |
| **Integrated Gradients** (Sundararajan et al., 2017) | Gradiente | Integral dos gradientes ao longo do caminho |
| **DeepLIFT** (Shrikumar et al., 2017) | Gradiente | Propagação de importância para trás |
| **Partial Dependence Plots** | Global | Efeito marginal de uma feature |
| **Counterfactual Explanations** | Local | "Se X fosse diferente, a decisão mudaria" |

## Direito à Explicação e Regulação

### GDPR e o Direito à Explicação

O Regulamento Geral de Proteção de Dados (GDPR) da União Europeia (2018) estabelece, em seus Artigos 13-15 e 22, o **direito à explicação** para decisões automatizadas:

> "A pessoa em causa tem o direito de... obter uma explicação sobre a decisão tomada após essa avaliação e o direito de contestar a decisão." (Art. 22, GDPR)

**Desafios legais:**
1. O que constitui uma "explicação adequada"?
2. Explicações baseadas em SHAP/LIME são inteligíveis para o cidadão comum?
3. Como equilibrar transparência com segredo industrial?
4. Quem é responsável por explicações insuficientes?

```python
class GDPRComplianceChecker:
    def __init__(self):
        self.requirements = {
            'meaningful_information': {
                'article': 'Art. 13(2)(f)',
                'description': 'Informacao significativa sobre logica envolvida'
            },
            'right_to_explanation': {
                'article': 'Art. 22(3)',
                'description': 'Direito a explicacao de decisoes automatizadas'
            },
            'contest_decision': {
                'article': 'Art. 22(3)',
                'description': 'Direito de contestar decisao'
            },
            'human_oversight': {
                'article': 'Art. 22(1)',
                'description': 'Direito a revisao humana'
            }
        }
    
    def audit_system(self, system):
        results = {}
        for req_name, req_info in self.requirements.items():
            if req_name == 'meaningful_information':
                passed = system.has_feature_importance
                details = 'OK' if passed else 'Forneca importancias de features'
            elif req_name == 'right_to_explanation':
                passed = system.can_provide_per_instance_explanation
                details = 'OK' if passed else 'Implemente explicacao por instancia'
            elif req_name == 'contest_decision':
                passed = system.has_appeal_process
                details = 'OK' if passed else 'Implemente processo de apelo'
            elif req_name == 'human_oversight':
                passed = system.has_human_in_the_loop
                details = 'OK' if passed else 'Implemente revisao humana'
            
            results[req_name] = {
                'article': req_info['article'],
                'passed': passed,
                'details': details
            }
        
        return {
            'system_name': system.name,
            'overall_compliance': all(r['passed'] for r in results.values()),
            'details': results
        }
```

### Outras Regulações

| Regulação | Região | Requisito de Transparência |
|-----------|--------|---------------------------|
| GDPR | EU | Art. 22: direito à explicação |
| AI Act (2024) | EU | Transparência obrigatória para IA de alto risco |
| CCPA | Califórnia | Direito de opt-out de decisões automatizadas |
| LGPD | Brasil | Art. 20: direito à revisão de decisões automatizadas |

## Transparência em Pipelines de ML

### Framework de Transparência

Uma pipeline de ML transparente requer documentação e auditabilidade em cada etapa:

```python
class TransparentMLPipeline:
    def __init__(self, name):
        self.name = name
        self.steps = []
        self.metadata = {}
    
    def add_step(self, step_name, step_function, documentation):
        self.steps.append({
            'name': step_name,
            'function': step_function,
            'documentation': documentation,
            'artifacts': []
        })
    
    def run(self, data):
        results = data
        audit_log = []
        
        for step in self.steps:
            results = step['function'].transform(results)
            step['artifacts'].append({'output_shape': results.shape})
            audit_log.append({
                'step': step['name'],
                'description': step['documentation'].get('description', ''),
                'rationale': step['documentation'].get('rationale', ''),
                'ethical_considerations': step['documentation'].get('ethics', 'None')
            })
        
        return {
            'results': results,
            'audit_log': audit_log,
            'metadata': self.metadata,
            'steps_count': len(self.steps)
        }
    
    def document_data_provenance(self, source, transformations, lineage):
        self.metadata['data_provenance'] = {
            'source': source,
            'transformations': transformations,
            'lineage': lineage,
            'consent_status': 'verified',
            'privacy_compliance': 'GDPR compliant'
        }
```

### Model Cards

Mitchell et al. (2019) propuseram **Model Cards** como documentação padronizada:

```python
class ModelCard:
    def __init__(self, model_name, version):
        self.model_name = model_name
        self.version = version
        self.sections = {}
    
    def add_basic_info(self, developer, model_date, model_type, license_info):
        self.sections['model_details'] = {
            'developed_by': developer, 'model_date': model_date,
            'model_type': model_type, 'version': self.version,
            'license': license_info
        }
    
    def add_intended_use(self, primary_use, primary_users, out_of_scope):
        self.sections['intended_use'] = {
            'primary_intended_use': primary_use,
            'primary_intended_users': primary_users,
            'out_of_scope_uses': out_of_scope
        }
    
    def add_factors(self, relevant_factors, evaluation_factors):
        self.sections['factors'] = {
            'relevant_factors': relevant_factors,
            'evaluation_factors': evaluation_factors
        }
    
    def add_metrics(self, performance_metrics, fairness_metrics, limitations):
        self.sections['metrics'] = {
            'model_performance': performance_metrics,
            'fairness_metrics': fairness_metrics,
            'quantitative_limitations': limitations
        }
    
    def add_evaluation_data(self, datasets, motivation, preprocessing):
        self.sections['evaluation_data'] = {
            'datasets': datasets, 'motivation': motivation,
            'preprocessing': preprocessing
        }
    
    def add_ethical_considerations(self, biases, risks, mitigations):
        self.sections['ethical_considerations'] = {
            'potential_biases': biases, 'identified_risks': risks,
            'mitigation_strategies': mitigations
        }
    
    def generate_card(self):
        return {
            'model_card': self.sections,
            'format': 'Model Card (Mitchell et al., 2019)',
            'version': self.version,
            'generated_date': '2026-05-16'
        }
```

## Desafios e Limitações da Transparência

### 1. Fidelidade das Explicações

Explicações pós-hoc são **aproximações**. Rudin (2019) argumenta que explicações pós-hoc podem ser enganosas e que devemos priorizar modelos inerentemente interpretáveis em aplicações de alto risco.

### 2. Engano por Explicação

Explicações podem ser manipuladas para esconder vieses. Uma explicação SHAP pode ser seletiva — mostrar apenas features que favorecem a imagem do sistema.

### 3. Complexidade Cognitiva

Explicações tecnicamente corretas podem ser incompreensíveis para leigos. O GDPR exige explicações "inteligíveis", mas valores de Shapley são complexos demais para o cidadão comum.

### 4. Trade-off Privacidade-Transparência

Explicações detalhadas podem expor informações sobre o modelo (extracted models) ou sobre dados de treinamento (membership inference).

```python
class TransparencyLimitations:
    def fidelity_vs_intelligibility_tradeoff(self, explanation_complexity):
        fidelity = 1.0 - np.exp(-explanation_complexity * 0.5)
        intelligibility = np.exp(-explanation_complexity * 0.3)
        return {
            'complexity': explanation_complexity,
            'fidelity': fidelity,
            'intelligibility': intelligibility,
            'note': 'Explicacoes detalhadas sao mais fieis mas menos compreensiveis'
        }
    
    def explainability_audit(self, system, test_cases):
        mismatches = 0
        for case in test_cases:
            original_pred = system.predict(case['input'])
            modified = case['input'].copy()
            modified[case['critical_feature']] += 0.1
            modified_pred = system.predict(modified)
            explanation = system.explain(case['input'])
            mismatches += 1 if abs(original_pred - modified_pred) > 0.1 else 0
        
        return {
            'total_cases': len(test_cases),
            'mismatches': mismatches,
            'explanation_reliability': 1.0 - mismatches / len(test_cases)
        }
```

## Glossário

| Termo | Definição |
|-------|-----------|
| **Black Box** | Modelo cujo funcionamento interno não é inspecionável |
| **Explicabilidade** | Capacidade de justificar decisões específicas |
| **Interpretabilidade** | Capacidade de entender o funcionamento global do modelo |
| **LIME** | Explicação local por aproximação linear |
| **SHAP** | Atribuição baseada em valores de Shapley |
| **GradCAM** | Mapa de ativação para CNNs |
| **Model Card** | Documentação padronizada de modelos |
| **Data Provenance** | Histórico de origem e transformação de dados |
| **Pós-hoc** | Explicação gerada após treinamento |
| **Intrínseco** | Modelo interpretável por design |
| **GDPR Art. 22** | Direito a não ser sujeito a decisões automatizadas |
| **Contrafactual** | Explicação do tipo "se X diferente, resultado diferente" |
| **Fidelidade** | Grau em que explicação reflete comportamento real |

## Exercícios

1. **Implementação LIME**: Implemente o LIME do zero e aplique a um classificador de texto (análise de sentimento). Compare explicações para predições positivas e negativas.

2. **Análise SHAP**: Use biblioteca SHAP (ou implementação própria) para analisar um modelo de regressão. Quais features são mais importantes? As explicações são estáveis?

3. **Contrafactuais**: Implemente um gerador de explicações contrafactuais: "Se a feature X fosse Y em vez de Z, a decisão seria W." Aplique a um modelo de crédito.

4. **Model Card**: Crie um Model Card completo para um sistema de recomendação de conteúdo. Inclua: uso pretendido, fatores relevantes, métricas, considerações éticas.

5. **Auditoria de Explicações**: Teste a fidelidade de explicações LIME e SHAP para uma rede neural. Em quantos casos a explicação não corresponde ao comportamento real? (Rudin, 2019)

6. **GDPR Audit**: Analise um sistema real (ex: scoring de crédito) contra requisitos do GDPR Art. 22. O que seria necessário para conformidade?

7. **Visualização**: Implemente visualizações de explicações para diferentes públicos: (a) engenheiro de ML, (b) usuário afetado, (c) regulador. Como as explicações diferem?

## Referências

- Doshi-Velez, F. & Kim, B. (2017). "Towards A Rigorous Science of Interpretable Machine Learning." *arXiv:1702.08608*.
- European Parliament. (2016). "General Data Protection Regulation (GDPR)." *Regulation (EU) 2016/679*.
- European Commission. (2024). "AI Act."
- Lipton, Z. (2016). "The Mythos of Model Interpretability." *ICML Workshop on HIML*.
- Lundberg, S. & Lee, S.-I. (2017). "A Unified Approach to Interpreting Model Predictions." *NeurIPS 2017*.
- Mitchell, M. et al. (2019). "Model Cards for Model Reporting." *FAT 2019*.
- Molnar, C. (2019). *Interpretable Machine Learning*. Leanpub.
- Ribeiro, M. T. et al. (2016). "Why Should I Trust You?" *KDD 2016*.
- Ribeiro, M. T. et al. (2018). "Anchors: High-Precision Model-Agnostic Explanations." *AAAI 2018*.
- Rudin, C. (2019). "Stop Explaining Black Box ML Models for High Stakes Decisions." *Nature Machine Intelligence*, 1(5), 206-215.
- Selvaraju, R. et al. (2017). "Grad-CAM: Visual Explanations from Deep Networks." *ICCV 2017*.
- Shrikumar, A. et al. (2017). "Learning Important Features Through Propagating Activation Differences." *ICML 2017*.
- Sundararajan, M. et al. (2017). "Axiomatic Attribution for Deep Networks." *ICML 2017*.
- Wachter, S. et al. (2017). "Why a Right to Explanation Does Not Exist in the GDPR." *International Data Privacy Law*, 7(2).
- Wachter, S. et al. (2018). "Counterfactual Explanations Without Opening the Black Box." *Harvard Journal of Law & Technology*, 31(2).
- Goodman, B. & Flaxman, S. (2017). "European Union Regulations on Algorithmic Decision-Making." *AI Magazine*, 38(3).

[[Conhecimento-Geral/Etica/INDEX|← Voltar ao índice de Ética]]
