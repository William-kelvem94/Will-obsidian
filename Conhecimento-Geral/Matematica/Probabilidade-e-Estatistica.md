---
title: "Probabilidade e Estatística"
date: 2026-05-16
area: "Matemática para IA"
tags:
  [
    conhecimento,
    conceito,
    matematica,
    probabilidade,
    estatistica,
    bayes,
    inferencia,
  ]
related:
  [
    "Conhecimento-Geral/Matematica/Teoria-da-Informacao",
    "Conhecimento-Geral/Matematica/Calculo-e-Otimizacao",
    "Conhecimento-Geral/Matematica/Algebra-Linear-Essencial",
    "Conhecimento-Geral/Neurociencia/Sistemas-de-Memoria",
  ]
aliases: ["Probabilidade", "Inferência Estatística", "Teoria da Probabilidade"]
---

# Probabilidade e Estatística

## Visão Geral

Probabilidade e estatística fornecem a estrutura matemática para lidar com incerteza, variabilidade e tomada de decisão sob informação incompleta. Em inteligência artificial, estas ferramentas são onipresentes: modelos generativos amostram de distribuições de probabilidade, classificadores produzem distribuições sobre classes, algoritmos de inferência bayesiana atualizam crenças com novos dados, e funções de perda como entropia cruzada têm raízes profundas na teoria da probabilidade.

Este documento desenvolve desde os axiomas fundamentais de Kolmogorov até tópicos avançados como estimação de máxima verossimilhança, inferência bayesiana, testes de hipóteses e regressão vista por lentes probabilísticas, sempre conectando a teoria matemática a aplicações práticas em aprendizado de máquina.

---

## Fundamentos da Probabilidade

### Espaço Amostral e Eventos

Um **experimento aleatório** é um processo cujo resultado não pode ser previsto com certeza. O **espaço amostral** $\Omega$ é o conjunto de todos os resultados possíveis. Um **evento** $E \subseteq \Omega$ é um subconjunto do espaço amostral.

**Exemplo**: No lançamento de um dado, $\Omega = \{1, 2, 3, 4, 5, 6\}$. O evento "número par" é $E = \{2, 4, 6\}$.

### Axiomas de Kolmogorov (1933)

Uma **medida de probabilidade** $\mathbb{P}$ é uma função $\mathbb{P}: \mathcal{F} \to [0, 1]$ (onde $\mathcal{F}$ é uma $\sigma$-álgebra de subconjuntos de $\Omega$) que satisfaz:

1. **Não-negatividade**: $\mathbb{P}(E) \geq 0$ para todo $E \in \mathcal{F}$
2. **Normalização**: $\mathbb{P}(\Omega) = 1$
3. **Aditividade enumerável**: Para eventos mutuamente exclusivos $E_1, E_2, \ldots$,

$$
\mathbb{P}\left(\bigcup_{i=1}^\infty E_i\right) = \sum_{i=1}^\infty \mathbb{P}(E_i)
$$

### Consequências dos Axiomas

- $\mathbb{P}(\emptyset) = 0$
- $\mathbb{P}(E^c) = 1 - \mathbb{P}(E)$
- $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$
- Se $A \subseteq B$, então $\mathbb{P}(A) \leq \mathbb{P}(B)$

### Exemplo: Espaço Amostral em Python

```python
import numpy as np

# Simulação Monte Carlo
n_simulacoes = 100000

# Espaço amostral: 3 lançamentos de moeda
# Evento: pelo menos 2 caras
lancamentos = np.random.randint(0, 2, (n_simulacoes, 3))  # 0=cara, 1=coroa
pelo_menos_2_caras = np.sum(lancamentos, axis=1) <= 1  # <=1 coroa = >=2 caras
prob_empirica = np.mean(pelo_menos_2_caras)
prob_teorica = 4 / 8  # {CCC, CCK, CKC, KCC} de 8 possíveis
print(f"Probabilidade empírica: {prob_empirica:.4f}")
print(f"Probabilidade teórica:  {prob_teorica:.4f}")
```

---

## Probabilidade Condicional e Independência

### Definição

A probabilidade condicional de $A$ dado $B$ é:

$$
\mathbb{P}(A \mid B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}, \quad \text{se } \mathbb{P}(B) > 0
$$

**Interpretação**: a fração de vezes que $A$ ocorre entre os resultados em que $B$ ocorre.

### Independência

Dois eventos $A$ e $B$ são **independentes** se:

$$
\mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B)
$$

Equivalentemente, $\mathbb{P}(A \mid B) = \mathbb{P}(A)$ e $\mathbb{P}(B \mid A) = \mathbb{P}(B)$.

### Regra do Produto e Probabilidade Total

**Regra do produto** (caso geral):

$$
\mathbb{P}(A_1 \cap A_2 \cap \cdots \cap A_n) = \mathbb{P}(A_1) \cdot \mathbb{P}(A_2 \mid A_1) \cdot \mathbb{P}(A_3 \mid A_1 \cap A_2) \cdots
$$

**Lei da probabilidade total**: Se $\{B_i\}$ é uma partição de $\Omega$, então:

$$
\mathbb{P}(A) = \sum_i \mathbb{P}(A \mid B_i) \mathbb{P}(B_i)
$$

### Teorema de Bayes

Derivado diretamente da definição de probabilidade condicional:

$$
\mathbb{P}(B_i \mid A) = \frac{\mathbb{P}(A \mid B_i) \mathbb{P}(B_i)}{\mathbb{P}(A)} = \frac{\mathbb{P}(A \mid B_i) \mathbb{P}(B_i)}{\sum_j \mathbb{P}(A \mid B_j) \mathbb{P}(B_j)}
$$

**Interpretação**:

$$
\text{Posterior} = \frac{\text{Verossimilhança} \times \text{Prior}}{\text{Evidência}}
$$

O Teorema de Bayes é o mecanismo fundamental de atualização de crenças à luz de evidências. Em aprendizado de máquina, ele fundamenta:

- **Classificadores Naive Bayes**
- **Modelos generativos profundos** (VAEs, normalizing flows)
- **Aprendizado Bayesiano por redes neurais** (BNN)
- **Inferência variacional**

### Exemplo: Diagnóstico Médico com Bayes

```python
import numpy as np

# Problema: teste para doença rara
# Prevalência: 1% da população tem a doença
# Sensibilidade (P(+|doente)): 99%
# Especificidade (P(-|sadio)): 95%

p_doenca = 0.01
p_pos_dado_doente = 0.99
p_neg_dado_sadio = 0.95
p_pos_dado_sadio = 1 - p_neg_dado_sadio

# Teorema de Bayes
p_doente_dado_pos = (p_pos_dado_doente * p_doenca) / (
    p_pos_dado_doente * p_doenca + p_pos_dado_sadio * (1 - p_doenca)
)

print(f"P(doente | positivo) = {p_doente_dado_pos:.4f}")
# Resultado: ~16.6% — contra-intuitivo, mas correto!
# Isto se deve à baixa prevalência (1%)

# Simulação Monte Carlo
n = 1000000
doentes = np.random.rand(n) < p_doenca
testes = np.zeros(n, dtype=bool)
testes[doentes] = np.random.rand(np.sum(doentes)) < p_pos_dado_doente
testes[~doentes] = np.random.rand(np.sum(~doentes)) < p_pos_dado_sadio

positivos = testes.sum()
positivos_doentes = np.sum(doentes & testes)
print(f"Monte Carlo: P(doente | positivo) = {positivos_doentes / positivos:.4f}")
```

---

## Variáveis Aleatórias

### Definição

Uma **variável aleatória** $X$ é uma função $X: \Omega \to \mathbb{R}$ que associa um valor numérico a cada resultado do espaço amostral.

### Variáveis Aleatórias Discretas

Uma variável aleatória é **discreta** se assume valores em um conjunto enumerável. Sua função de massa de probabilidade (PMF) é:

$$
p_X(x) = \mathbb{P}(X = x)
$$

Propriedades: $p_X(x) \geq 0$ e $\sum_x p_X(x) = 1$.

A **função de distribuição acumulada (CDF)** é:

$$
F_X(x) = \mathbb{P}(X \leq x) = \sum_{t \leq x} p_X(t)
$$

### Variáveis Aleatórias Contínuas

Uma variável aleatória é **contínua** se existe uma função $f_X(x) \geq 0$ (densidade de probabilidade, PDF) tal que:

$$
\mathbb{P}(a \leq X \leq b) = \int_a^b f_X(x) \, dx
$$

A CDF para contínuas é:

$$
F_X(x) = \mathbb{P}(X \leq x) = \int_{-\infty}^x f_X(t) \, dt
$$

Note que $\mathbb{P}(X = x) = 0$ para variáveis contínuas — a probabilidade está na área sob a PDF, não em pontos individuais.

### Valor Esperado e Momentos

**Valor esperado** (média):

- Discreta: $\mathbb{E}[X] = \sum_x x \cdot p_X(x)$
- Contínua: $\mathbb{E}[X] = \int_{-\infty}^\infty x \cdot f_X(x) \, dx$

**Variância**:

$$
\text{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2
$$

**Desvio padrão**: $\sigma_X = \sqrt{\text{Var}(X)}$

**Momentos centrados**: $\mu_k = \mathbb{E}[(X - \mu)^k]$

- $\mu_2$: variância (dispersão)
- $\mu_3$: assimetria (skewness)
- $\mu_4$: curtose (achatamento)

### Exemplo: PDF, CDF e Momentos

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Distribuição Normal N(0, 1)
x = np.linspace(-4, 4, 200)
pdf = stats.norm.pdf(x, loc=0, scale=1)
cdf = stats.norm.cdf(x, loc=0, scale=1)

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.plot(x, pdf, 'b-'); plt.title('PDF'); plt.grid()

plt.subplot(1, 3, 2)
plt.plot(x, cdf, 'r-'); plt.title('CDF'); plt.grid()

# Amostragem e histograma
samples = np.random.randn(10000)
plt.subplot(1, 3, 3)
plt.hist(samples, bins=50, density=True, alpha=0.6, label='Amostras')
plt.plot(x, pdf, 'b-', label='PDF teórica')
plt.title('Histograma vs PDF'); plt.legend(); plt.grid()

plt.tight_layout()
plt.show()

print(f"Média amostral: {np.mean(samples):.4f}")
print(f"Variância amostral: {np.var(samples):.4f}")
print(f"Assimetria: {stats.skew(samples):.4f}")
print(f"Curtose: {stats.kurtosis(samples):.4f}")
```

---

## Distribuições de Probabilidade

### Distribuições Discretas

#### Bernoulli $\text{Ber}(p)$

Modela um único ensaio binário (cara/coroa, sucesso/fracasso):

$$
p_X(x) = p^x (1-p)^{1-x}, \quad x \in \{0, 1\}
$$

- $\mathbb{E}[X] = p$
- $\text{Var}(X) = p(1-p)$

**Em ML**: saída de classificação binária (regressão logística).

#### Binomial $\text{Bin}(n, p)$

Soma de $n$ Bernoulli i.i.d.:

$$
p_X(k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n
$$

- $\mathbb{E}[X] = np$
- $\text{Var}(X) = np(1-p)$

#### Poisson $\text{Poi}(\lambda)$

Modela o número de eventos em um intervalo fixo:

$$
p_X(k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \ldots
$$

- $\mathbb{E}[X] = \text{Var}(X) = \lambda$

**Em ML**: modelagem de contagens (ocorrência de palavras, cliques).

#### Categorial (Multinoulli)

Generalização da Bernoulli para $K$ categorias:

$$
p_X(\mathbf{x}) = \prod_{k=1}^K \pi_k^{x_k}, \quad \mathbf{x} \in \{0, 1\}^K, \sum_k x_k = 1
$$

**Em ML**: saída de classificadores multiclasse (softmax).

### Distribuições Contínuas

#### Uniforme $\text{Unif}(a, b)$

$$
f_X(x) = \frac{1}{b-a}, \quad a \leq x \leq b
$$

- $\mathbb{E}[X] = \frac{a+b}{2}$
- $\text{Var}(X) = \frac{(b-a)^2}{12}$

#### Normal (Gaussiana) $\mathcal{N}(\mu, \sigma^2)$

A distribuição mais importante em estatística:

$$
f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$

- $\mathbb{E}[X] = \mu$
- $\text{Var}(X) = \sigma^2$

**Por que tão importante?**
1. **Teorema Central do Limite**: a soma de muitas variáveis i.i.d. tende à Normal
2. **Máxima entropia**: entre distribuições com média e variância fixas, a Normal tem máxima entropia
3. **Conveniência analítica**: conjugada com sigo mesma em inferência bayesiana
4. **Ruído de observação**: modelo natural para erros de medição

#### Gaussiana Multivariada $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$

$$
f_X(\mathbf{x}) = \frac{1}{(2\pi)^{d/2} |\boldsymbol{\Sigma}|^{1/2}} \exp\left(-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu})\right)
$$

**Em ML**: modelos de mistura gaussiana (GMM), VAEs, processos Gaussianos, normalizing flows, embeddings de palavras (representações latentes Gaussianas).

#### Beta $\text{Beta}(\alpha, \beta)$

Distribuição sobre probabilidades:

$$
f_X(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha, \beta)}, \quad 0 \leq x \leq 1
$$

onde $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$.

- $\mathbb{E}[X] = \frac{\alpha}{\alpha + \beta}$
- $\text{Var}(X) = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$

**Em ML**: prior conjugada para Bernoulli, aprendizado de probabilidades (bandit problems, A/B testing), parâmetros de redes neurais Bayesianas com saída probabilística.

#### Dirichlet $\text{Dir}(\boldsymbol{\alpha})$

Generalização da Beta para $K$ dimensões — distribuição sobre vetores de probabilidade:

$$
f_X(\mathbf{x}) = \frac{\Gamma(\sum \alpha_k)}{\prod \Gamma(\alpha_k)} \prod_{k=1}^K x_k^{\alpha_k - 1}, \quad \sum_k x_k = 1
$$

**Em ML**: prior conjugada para Categorial, modelagem de tópicos (LDA), misturas, parâmetros de atenção em transformers, aprendizado de distribuições de classes.

#### Exponencial $\text{Exp}(\lambda)$

Modela tempo entre eventos em um processo Poisson:

$$
f_X(x) = \lambda e^{-\lambda x}, \quad x \geq 0
$$

**Propriedade sem memória**: $\mathbb{P}(X > s + t \mid X > t) = \mathbb{P}(X > s)$

### Exemplo: Visualização de Distribuições

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.linspace(-4, 8, 500)

plt.figure(figsize=(14, 6))

# Discretas
plt.subplot(2, 3, 1)
k = np.arange(0, 11)
pmf = stats.binom.pmf(k, n=10, p=0.5)
plt.stem(k, pmf); plt.title('Binomial(10, 0.5)')

plt.subplot(2, 3, 2)
k = np.arange(0, 11)
pmf = stats.poisson.pmf(k, mu=3)
plt.stem(k, pmf); plt.title('Poisson(3)')

# Contínuas
plt.subplot(2, 3, 3)
for sigma in [0.5, 1, 2]:
    plt.plot(x, stats.norm.pdf(x, loc=0, scale=sigma), label=f'σ={sigma}')
plt.title('Normal'); plt.legend()

plt.subplot(2, 3, 4)
for (a, b) in [(0.5, 0.5), (2, 5), (5, 1)]:
    plt.plot(np.linspace(0, 1, 200), stats.beta.pdf(np.linspace(0, 1, 200), a, b),
             label=f'α={a}, β={b}')
plt.title('Beta'); plt.legend()

plt.subplot(2, 3, 5)
plt.plot(x[x>=0], stats.expon.pdf(x[x>=0], scale=1), label='λ=1')
plt.plot(x[x>=0], stats.expon.pdf(x[x>=0], scale=0.5), label='λ=0.5')
plt.title('Exponencial'); plt.legend()

plt.tight_layout()
plt.show()
```

---

## Teoremas Limite Fundamentais

### Lei dos Grandes Números (LLN)

Sejam $X_1, X_2, \ldots$ variáveis i.i.d. com $\mathbb{E}[X_i] = \mu$. A média amostral converge para a média verdadeira:

$$
\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i \xrightarrow{p} \mu \quad \text{(lei fraca)}
$$

$$
\bar{X}_n \xrightarrow{a.s.} \mu \quad \text{(lei forte)}
$$

Intuitivamente, com mais dados, a incerteza sobre a média diminui.

### Teorema Central do Limite (CLT)

Sejam $X_1, X_2, \ldots, X_n$ variáveis i.i.d. com $\mathbb{E}[X_i] = \mu$ e $\text{Var}(X_i) = \sigma^2 < \infty$. Então:

$$
\sqrt{n}(\bar{X}_n - \mu) \xrightarrow{d} \mathcal{N}(0, \sigma^2)
$$

Equivalentemente:

$$
\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)
$$

O CLT é a razão pela qual a distribuição Normal aparece tão frequentemente — ela é a distribuição limite de somas de variáveis aleatórias, independentemente de suas distribuições individuais.

**Importância em ML**:
- Justifica o uso de erro padrão e intervalos de confiança
- Fundamenta a convergência de estimadores MLE
- Explica porque médias de predições (ensemble methods) tendem a ser Normais
- Base da inferência em experimentos (A/B testing)

### Exemplo: CLT Visualizado

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# População: distribuição Exponencial (muito não-normal)
pop = stats.expon(scale=1)

# Amostrar médias de n amostras
n = 30
n_repeticoes = 10000
medias = np.array([np.mean(pop.rvs(n)) for _ in range(n_repeticoes)])

# Teórico: N(média, std/sqrt(n))
x = np.linspace(0.5, 1.5, 200)
mu = 1.0
sigma = 1.0 / np.sqrt(n)
pdf = stats.norm.pdf(x, loc=mu, scale=sigma)

plt.figure(figsize=(10, 5))
plt.hist(medias, bins=50, density=True, alpha=0.6, label='Médias amostrais')
plt.plot(x, pdf, 'r-', linewidth=2, label='Normal aproximante')
plt.axvline(mu, color='k', linestyle='--', label='Média verdadeira')
plt.title(f'CLT: Médias de {n} Exponenciais')
plt.legend(); plt.grid()
plt.show()
```

---

## Estimação de Máxima Verossimilhança (MLE)

### Definição

Seja $\{x_1, \ldots, x_n\}$ uma amostra i.i.d. de $p(x \mid \theta)$. A **função de verossimilhança** é:

$$
\mathcal{L}(\theta) = p(x_1, \ldots, x_n \mid \theta) = \prod_{i=1}^n p(x_i \mid \theta)
$$

O **estimador de máxima verossimilhança** (MLE) é:

$$
\hat{\theta}_{\text{MLE}} = \arg\max_\theta \mathcal{L}(\theta) = \arg\max_\theta \sum_{i=1}^n \log p(x_i \mid \theta)
$$

Na prática, maximiza-se o **log-verossimilhança** $\ell(\theta) = \sum_i \log p(x_i \mid \theta)$, que é equivalente e numericamente mais estável.

### MLE para a Distribuição Normal

Para $x_i \sim \mathcal{N}(\mu, \sigma^2)$ i.i.d.:

$$
\ell(\mu, \sigma^2) = -\frac{n}{2} \log(2\pi\sigma^2) - \frac{1}{2\sigma^2} \sum_{i=1}^n (x_i - \mu)^2
$$

Maximizando em relação a $\mu$ e $\sigma^2$:

$$
\frac{\partial \ell}{\partial \mu} = \frac{1}{\sigma^2} \sum_{i=1}^n (x_i - \mu) = 0 \implies \hat{\mu}_{\text{MLE}} = \frac{1}{n} \sum_{i=1}^n x_i
$$

$$
\frac{\partial \ell}{\partial \sigma^2} = -\frac{n}{2\sigma^2} + \frac{1}{2\sigma^4} \sum_{i=1}^n (x_i - \mu)^2 = 0 \implies \hat{\sigma}^2_{\text{MLE}} = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2
$$

Note que o MLE para $\sigma^2$ é **viesado** (tende a subestimar), mas é consistente (converge para o valor verdadeiro quando $n \to \infty$).

### Propriedades do MLE

- **Consistência**: $\hat{\theta}_{\text{MLE}} \xrightarrow{p} \theta^*$ (converge para o valor verdadeiro)
- **Eficiência assimptótica**: atinge o limite inferior de Cramér-Rao
- **Normalidade assimptótica**: $\sqrt{n}(\hat{\theta}_{\text{MLE}} - \theta) \xrightarrow{d} \mathcal{N}(0, \mathcal{I}(\theta)^{-1})$
- **Invarância**: se $\hat{\theta}$ é MLE de $\theta$, então $g(\hat{\theta})$ é MLE de $g(\theta)$

O MLE é o princípio de estimação mais usado em ML: minimizar MSE, entropia cruzada e outras perdas corresponde a MLE sob diferentes distribuições assumidas.

### MLE para Regressão Linear

No modelo $y_i = \mathbf{w}^\top \mathbf{x}_i + \epsilon_i$ com $\epsilon_i \sim \mathcal{N}(0, \sigma^2)$:

$$
p(y_i \mid \mathbf{x}_i, \mathbf{w}, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(y_i - \mathbf{w}^\top \mathbf{x}_i)^2}{2\sigma^2}\right)
$$

Minimizar o erro quadrático médio (MSE) é equivalente a MLE com ruído Gaussiano.

### Exemplo: MLE

```python
import numpy as np
from scipy.optimize import minimize
from scipy import stats
import matplotlib.pyplot as plt

# Gerar dados de uma Poisson
np.random.seed(42)
lambda_true = 3.5
n = 100
data = stats.poisson.rvs(lambda_true, size=n)

# MLE: lambda = média amostral
lambda_mle = np.mean(data)
print(f"λ verdadeiro: {lambda_true}")
print(f"λ MLE: {lambda_mle:.3f}")

# MLE via otimização numérica (para verificação)
def neg_log_likelihood(lmbda, data):
    return -np.sum(stats.poisson.logpmf(data, lmbda))

result = minimize(neg_log_likelihood, x0=[1], args=(data,), method='L-BFGS-B', bounds=[(1e-5, None)])
print(f"λ MLE (otimização): {result.x[0]:.3f}")

# Distribuição assimptótica do MLE
# sqrt(n)(lambda_hat - lambda) ~ N(0, lambda)
se = np.sqrt(lambda_mle / n)
print(f"Erro padrão: {se:.4f}")

# Histograma da amostra
x = np.arange(0, 10)
plt.bar(x, np.bincount(data, minlength=11)[:10] / n, alpha=0.6, label='Dados')
plt.plot(x, stats.poisson.pmf(x, lambda_mle), 'ro-', label=f'Poisson({lambda_mle:.2f})')
plt.title('MLE para Poisson')
plt.legend(); plt.grid()
plt.show()
```

---

## Inferência Bayesiana

### Estrutura Conceitual

A inferência bayesiana trata parâmetros como variáveis aleatórias com distribuições que representam incerteza:

$$
p(\theta \mid \mathcal{D}) = \frac{p(\mathcal{D} \mid \theta) \, p(\theta)}{p(\mathcal{D})}
$$

- **Prior** $p(\theta)$: crença inicial sobre $\theta$ antes de ver os dados
- **Verossimilhança** $p(\mathcal{D} \mid \theta)$: quão prováveis são os dados dado $\theta$
- **Evidência** $p(\mathcal{D}) = \int p(\mathcal{D} \mid \theta) p(\theta) \, d\theta$: constante de normalização
- **Posterior** $p(\theta \mid \mathcal{D})$: crença atualizada após ver os dados

### Priors Conjugados

Um prior é **conjugado** à verossimilhança se o posterior pertence à mesma família do prior.

| Verossimilhança | Prior Conjugado | Posterior |
|:---|:---|:---|
| Bernoulli(p) | Beta($\alpha$, $\beta$) | Beta($\alpha + \sum x_i$, $\beta + n - \sum x_i$) |
| Poisson($\lambda$) | Gamma($a$, $b$) | Gamma($a + \sum x_i$, $b + n$) |
| Normal($\mu$, $\sigma^2$) ($\sigma^2$ conhecida) | Normal($\mu_0$, $\sigma_0^2$) | Normal $\left(\frac{\mu_0/\sigma_0^2 + \sum x_i/\sigma^2}{1/\sigma_0^2 + n/\sigma^2}, \frac{1}{1/\sigma_0^2 + n/\sigma^2}\right)$ |
| Categorial($\boldsymbol{\pi}$) | Dirichlet($\boldsymbol{\alpha}$) | Dirichlet($\boldsymbol{\alpha} + \mathbf{n}$) |

### Predição Bayesiana

A distribuição preditiva para um novo ponto $\tilde{x}$ é:

$$
p(\tilde{x} \mid \mathcal{D}) = \int p(\tilde{x} \mid \theta) p(\theta \mid \mathcal{D}) \, d\theta
$$

Isto propaga automaticamente a incerteza sobre $\theta$ para as previsões.

### MLE vs MAP vs Bayes Pleno

- **MLE**: $\hat{\theta} = \arg\max_\theta p(\mathcal{D} \mid \theta)$ (apenas dados)
- **MAP**: $\hat{\theta} = \arg\max_\theta p(\theta \mid \mathcal{D}) = \arg\max_\theta [\log p(\mathcal{D} \mid \theta) + \log p(\theta)]$ (regularização implícita)
- **Bayes pleno**: usa toda a distribuição posterior $p(\theta \mid \mathcal{D})$ (incerteza total)

### Exemplo: Bernoulli com Prior Beta

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Dados: 6 caras em 10 lançamentos
n_caras, n_total = 6, 10

# Prior: Beta(2, 2) — ligeira crença de que a moeda é justa
alpha_prior, beta_prior = 2, 2

# Posterior: Beta(alpha + n_caras, beta + n_total - n_caras)
alpha_post = alpha_prior + n_caras
beta_post = beta_prior + n_total - n_caras

# MLE e MAP
p_mle = n_caras / n_total
p_map = (n_caras + alpha_prior - 1) / (n_total + alpha_prior + beta_prior - 2)
print(f"MLE:  {p_mle:.3f}")
print(f"MAP:  {p_map:.3f}")

# Visualização
theta = np.linspace(0, 1, 200)
prior = stats.beta.pdf(theta, alpha_prior, beta_prior)
likelihood = stats.binom.pmf(n_caras, n_total, theta)
posterior = stats.beta.pdf(theta, alpha_post, beta_post)

plt.figure(figsize=(10, 5))
plt.plot(theta, prior, 'g--', label=f'Prior Beta({alpha_prior},{beta_prior})')
plt.plot(theta, likelihood / np.trapz(likelihood, theta), 'b:', 
         label='Verossimilhança (normalizada)')
plt.plot(theta, posterior, 'r-', label=f'Posterior Beta({alpha_post},{beta_post})')
plt.axvline(p_mle, color='b', linestyle=':', alpha=0.7, label=f'MLE={p_mle:.3f}')
plt.axvline(p_map, color='r', linestyle=':', alpha=0.7, label=f'MAP={p_map:.3f}')
plt.xlabel('p (probabilidade de cara)')
plt.ylabel('Densidade')
plt.legend(); plt.grid()
plt.title('Inferência Bayesiana: Bernoulli + Beta')
plt.show()

# Intervalo de credibilidade (95%)
ci = stats.beta.interval(0.95, alpha_post, beta_post)
print(f"Intervalo de credibilidade 95%: [{ci[0]:.3f}, {ci[1]:.3f}]")
```

---

## Testes de Hipóteses

### Estrutura Básica

1. Definir $H_0$ (hipótese nula) e $H_1$ (hipótese alternativa)
2. Escolher uma **estatística de teste** $T(X)$
3. Calcular o **p-valor**: $\mathbb{P}(T \geq t_{\text{obs}} \mid H_0)$
4. Rejeitar $H_0$ se p-valor $< \alpha$ (nível de significância)

### Erros Tipo I e Tipo II

| Decisão | $H_0$ verdadeira | $H_1$ verdadeira |
|:---|:---|:---|
| Não rejeitar $H_0$ | ✅ Decisão correta | ❌ Erro Tipo II ($\beta$) |
| Rejeitar $H_0$ | ❌ Erro Tipo I ($\alpha$) | ✅ Decisão correta |

- **Nível de significância** $\alpha = \mathbb{P}(\text{Erro Tipo I})$ (tipicamente 0.05 ou 0.01)
- **Poder** $1 - \beta = \mathbb{P}(\text{rejeitar } H_0 \mid H_1 \text{ verdadeira})$

### p-valores

O p-valor é a probabilidade de observar uma estatística tão ou mais extrema que a observada, assumindo $H_0$ verdadeira.

**Interpretação correta**: p-valor não é a probabilidade de $H_0$ ser verdadeira. É a probabilidade dos dados sob $H_0$.

**Críticas ao p-valor**:
- Depende fortemente do tamanho amostral (amostras grandes sempre dão p-valores pequenos)
- Não mede magnitude do efeito
- Facilmente mal interpretado
- Alternativas: intervalos de confiança, fatores de Bayes, estimativas de efeito

### Intervalos de Confiança

Um intervalo de confiança de $1-\alpha$ para $\theta$ é um intervalo $[L(X), U(X)]$ tal que:

$$
\mathbb{P}(L(X) \leq \theta \leq U(X)) = 1 - \alpha
$$

**Interpretação**: se repetíssemos o experimento muitas vezes, $1-\alpha$ dos intervalos conteriam o verdadeiro parâmetro.

### Exemplo: Teste t e Intervalo de Confiança

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Dois grupos
np.random.seed(42)
grupo_a = stats.norm.rvs(loc=100, scale=15, size=50)
grupo_b = stats.norm.rvs(loc=108, scale=15, size=50)

# Teste t (duas amostras independentes)
t_stat, p_valor = stats.ttest_ind(grupo_a, grupo_b)
print(f"Estatística t: {t_stat:.4f}")
print(f"p-valor: {p_valor:.4f}")
print(f"Diferença significativa (α=0.05)? {'Sim' if p_valor < 0.05 else 'Não'}")

# Intervalo de confiança para a diferença das médias
diferenca = np.mean(grupo_b) - np.mean(grupo_a)
se = np.sqrt(np.var(grupo_a, ddof=1)/50 + np.var(grupo_b, ddof=1)/50)
gl = 98  # aproximação de Welch
ci = diferenca + stats.t.ppf([0.025, 0.975], gl) * se
print(f"Diferença das médias: {diferenca:.2f}")
print(f"IC 95%: [{ci[0]:.2f}, {ci[1]:.2f}]")

# Visualização
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.hist(grupo_a, alpha=0.5, label='Grupo A', bins=12)
plt.hist(grupo_b, alpha=0.5, label='Grupo B', bins=12)
plt.legend(); plt.title('Distribuições dos Grupos')

plt.subplot(1, 2, 2)
plt.errorbar([1, 2], [np.mean(grupo_a), np.mean(grupo_b)],
             yerr=[stats.sem(grupo_a), stats.sem(grupo_b)], 
             fmt='o', capsize=5, markersize=10)
plt.xticks([1, 2], ['Grupo A', 'Grupo B'])
plt.title('Médias ± Erro Padrão')
plt.grid()
plt.tight_layout()
plt.show()
```

---

## Regressão: Perspectiva Probabilística

### Regressão Linear

O modelo de regressão linear assume:

$$
y_i = \mathbf{w}^\top \mathbf{x}_i + \epsilon_i, \quad \epsilon_i \sim \mathcal{N}(0, \sigma^2)
$$

A verossimilhança:

$$
p(\mathbf{y} \mid \mathbf{X}, \mathbf{w}, \sigma^2) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(y_i - \mathbf{w}^\top \mathbf{x}_i)^2}{2\sigma^2}\right)
$$

Maximizar o log da verossimilhança equivale a minimizar o MSE.

#### Regularização como Prior

- **Ridge (L2)**: $\mathbf{w} \sim \mathcal{N}(0, \lambda^{-1}\mathbf{I})$ — prior Gaussiano → MAP = minimizar MSE + $\lambda \|\mathbf{w}\|^2$
- **Lasso (L1)**: $\mathbf{w} \sim \text{Laplace}(0, \lambda^{-1})$ — prior Laplaceano → MAP = minimizar MSE + $\lambda \|\mathbf{w}\|_1$

### Regressão Logística

Para classificação binária, modelamos:

$$
p(y = 1 \mid \mathbf{x}, \mathbf{w}) = \sigma(\mathbf{w}^\top \mathbf{x}) = \frac{1}{1 + e^{-\mathbf{w}^\top \mathbf{x}}}
$$

A verossimilhança:

$$
p(\mathbf{y} \mid \mathbf{X}, \mathbf{w}) = \prod_{i=1}^n \sigma(\mathbf{w}^\top \mathbf{x}_i)^{y_i} (1 - \sigma(\mathbf{w}^\top \mathbf{x}_i))^{1-y_i}
$$

O negativo do log-verossimilhança é a **entropia cruzada binária**:

$$
\mathcal{L}(\mathbf{w}) = -\sum_{i=1}^n \left[ y_i \log \sigma(\mathbf{w}^\top \mathbf{x}_i) + (1 - y_i) \log(1 - \sigma(\mathbf{w}^\top \mathbf{x}_i)) \right]
$$

### Regressão Linear Bayesiana

Em vez de estimar $\mathbf{w}$ pontualmente, colocamos um prior $p(\mathbf{w})$ e computamos a posterior:

$$
p(\mathbf{w} \mid \mathbf{X}, \mathbf{y}) \propto p(\mathbf{y} \mid \mathbf{X}, \mathbf{w}) \, p(\mathbf{w})
$$

Com prior Gaussiano $\mathbf{w} \sim \mathcal{N}(\mathbf{0}, \boldsymbol{\Sigma}_p)$, a posterior é:

$$
p(\mathbf{w} \mid \mathbf{X}, \mathbf{y}) = \mathcal{N}\left(\frac{1}{\sigma^2}\mathbf{A}^{-1}\mathbf{X}^\top\mathbf{y}, \mathbf{A}^{-1}\right)
$$

onde $\mathbf{A} = \frac{1}{\sigma^2}\mathbf{X}^\top\mathbf{X} + \boldsymbol{\Sigma}_p^{-1}$.

A predição para um novo ponto $\mathbf{x}_*$ integra sobre a incerteza em $\mathbf{w}$:

$$
p(y_* \mid \mathbf{x}_*, \mathbf{X}, \mathbf{y}) = \mathcal{N}\left(\frac{1}{\sigma^2}\mathbf{x}_*^\top \mathbf{A}^{-1} \mathbf{X}^\top \mathbf{y}, \ \mathbf{x}_*^\top \mathbf{A}^{-1} \mathbf{x}_* + \sigma^2\right)
$$

### Exemplo: Regressão Bayesiana

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Dados sintéticos
np.random.seed(42)
X = np.linspace(-3, 3, 20)
w_true = [1.5, -0.8]
y = w_true[0] + w_true[1] * X + 0.3 * np.random.randn(20)

X_design = np.column_stack([np.ones_like(X), X])

# Regressão linear (MLE)
w_mle = np.linalg.inv(X_design.T @ X_design) @ X_design.T @ y

# Regressão bayesiana
sigma2 = 0.3**2  # variância do ruído (suposta conhecida)
Sigma_p = np.eye(2) * 5  # prior amplo

A = X_design.T @ X_design / sigma2 + np.linalg.inv(Sigma_p)
mu_post = np.linalg.solve(A, X_design.T @ y / sigma2)
Sigma_post = np.linalg.inv(A)

# Predições
X_test = np.linspace(-4, 4, 200)
X_test_design = np.column_stack([np.ones_like(X_test), X_test])

mu_pred = X_test_design @ mu_post
var_pred = np.sum(X_test_design @ Sigma_post * X_test_design, axis=1) + sigma2
std_pred = np.sqrt(var_pred)

# Plot
plt.figure(figsize=(10, 5))
plt.scatter(X, y, alpha=0.7, label='Dados')
plt.plot(X_test, X_test_design @ w_mle, 'g--', label='MLE')
plt.plot(X_test, mu_pred, 'r-', label='Média posterior')
plt.fill_between(X_test, mu_pred - 2*std_pred, mu_pred + 2*std_pred,
                 color='r', alpha=0.15, label='IC 95%')
plt.xlabel('x'); plt.ylabel('y')
plt.legend(); plt.grid()
plt.title('Regressão Linear Bayesiana')
plt.show()

print(f"w MLE: {w_mle}")
print(f"w posterior (média): {mu_post}")
print(f"w posterior (desvio): {np.sqrt(np.diag(Sigma_post))}")
```

---

## Modelos Probabilísticos em IA

### Modelos de Mistura Gaussiana (GMM)

Cada ponto é gerado por uma das $K$ componentes Gaussianas:

$$
p(\mathbf{x}) = \sum_{k=1}^K \pi_k \, \mathcal{N}(\mathbf{x} \mid \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)
$$

com $\sum_{k=1}^K \pi_k = 1$ e $\pi_k \geq 0$.

O **algoritmo EM** (Expectation-Maximization) estima os parâmetros iterativamente:

**E-step**: $\gamma_{ik} = \mathbb{P}(z_i = k \mid \mathbf{x}_i, \theta) = \frac{\pi_k \mathcal{N}(\mathbf{x}_i \mid \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)}{\sum_j \pi_j \mathcal{N}(\mathbf{x}_i \mid \boldsymbol{\mu}_j, \boldsymbol{\Sigma}_j)}$

**M-step**: atualizar $\pi_k = \frac{\sum_i \gamma_{ik}}{n}$, $\boldsymbol{\mu}_k = \frac{\sum_i \gamma_{ik} \mathbf{x}_i}{\sum_i \gamma_{ik}}$, etc.

### Variational Autoencoders (VAEs)

VAEs modelam a distribuição marginal $p(\mathbf{x})$ através de variáveis latentes $\mathbf{z}$:

$$
p(\mathbf{x}) = \int p(\mathbf{x} \mid \mathbf{z}) \, p(\mathbf{z}) \, d\mathbf{z}
$$

O **Evidence Lower Bound (ELBO)** é:

$$
\log p(\mathbf{x}) \geq \mathbb{E}_{q(\mathbf{z} \mid \mathbf{x})}[\log p(\mathbf{x} \mid \mathbf{z})] - D_{\text{KL}}(q(\mathbf{z} \mid \mathbf{x}) \| p(\mathbf{z}))
$$

O primeiro termo é a **reconstrução**, o segundo é a **regularização** (divergência KL entre o posterior aproximado $q$ e o prior $p(\mathbf{z})$).

### Processos Gaussianos (GP)

Um GP define uma distribuição sobre funções. Qualquer conjunto finito de pontos tem distribuição Gaussiana conjunta:

$$
f(\mathbf{x}) \sim \mathcal{GP}(m(\mathbf{x}), k(\mathbf{x}, \mathbf{x}'))
$$

onde $m$ é a função média e $k$ é a função de covariância (kernel).

**Predição**:

$$
f(\mathbf{x}_*) \mid \mathbf{X}, \mathbf{y} \sim \mathcal{N}(\boldsymbol{\mu}_*, \boldsymbol{\Sigma}_*)
$$

com:

$$
\boldsymbol{\mu}_* = \mathbf{k}_*^\top (\mathbf{K} + \sigma^2\mathbf{I})^{-1} \mathbf{y}
$$
$$
\boldsymbol{\Sigma}_* = k(\mathbf{x}_*, \mathbf{x}_*) - \mathbf{k}_*^\top (\mathbf{K} + \sigma^2\mathbf{I})^{-1} \mathbf{k}_*
$$

### Exemplo: GMM com EM

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Gerar dados de duas Gaussianas
np.random.seed(42)
n1, n2 = 200, 150
X1 = np.random.randn(n1, 2) + np.array([-2, -2])
X2 = np.random.randn(n2, 2) + np.array([2, 2])
X = np.vstack([X1, X2])
n = len(X)
K = 2

# Inicialização
pi = np.ones(K) / K
mu = np.array([[-1, -1], [1, 1]], dtype=float)
Sigma = np.array([np.eye(2), np.eye(2)])

for iteration in range(50):
    # E-step
    gamma = np.zeros((n, K))
    for k in range(K):
        gamma[:, k] = pi[k] * stats.multivariate_normal.pdf(X, mu[k], Sigma[k])
    gamma /= gamma.sum(axis=1, keepdims=True)
    
    # M-step
    Nk = gamma.sum(axis=0)
    pi = Nk / n
    for k in range(K):
        mu[k] = (gamma[:, k:k+1] * X).sum(axis=0) / Nk[k]
        diff = X - mu[k]
        Sigma[k] = (gamma[:, k:k+1] * diff).T @ diff / Nk[k]

# Visualização
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=gamma[:, 0], cmap='viridis', alpha=0.6)
for k in range(K):
    plt.scatter(mu[k, 0], mu[k, 1], c='r', marker='x', s=200, linewidths=3)
plt.title('GMM: Responsabilidades (cores) e Centros (X)')
plt.colorbar(label='P(Componente 1)')
plt.axis('equal'); plt.grid()
plt.show()
```

---

## Conceitos Avançados em Probabilidade

### Correlação e Covariância

Para duas variáveis aleatórias $X$ e $Y$:

$$
\text{Cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}[X])(Y - \mathbb{E}[Y])]
$$

$$
\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} \in [-1, 1]
$$

**Correlação não implica causalidade** — uma das lições mais importantes em estatística.

### Desigualdades Probabilísticas

**Desigualdade de Markov**: $\mathbb{P}(X \geq t) \leq \frac{\mathbb{E}[X]}{t}$ para $X \geq 0$

**Desigualdade de Chebyshev**: $\mathbb{P}(|X - \mu| \geq t) \leq \frac{\sigma^2}{t^2}$

**Desigualdade de Hoeffding**: Para $X_i \in [a_i, b_i]$ independentes:

$$
\mathbb{P}\left(\left|\frac{1}{n}\sum_i X_i - \mathbb{E}[X]\right| \geq t\right) \leq 2\exp\left(-\frac{2n^2 t^2}{\sum_i (b_i - a_i)^2}\right)
$$

Estas desigualdades fundamentam **limites de generalização** em aprendizado de máquina.

### Teoria da Informação (conexão)

- **Entropia**: $H(X) = -\sum_x p(x) \log p(x)$ — incerteza de $X$
- **Entropia cruzada**: $H(p, q) = -\sum_x p(x) \log q(x)$ — perda em classificação
- **Divergência KL**: $D_{\text{KL}}(p \| q) = \sum_x p(x) \log \frac{p(x)}{q(x)}$ — distância entre distribuições
- **Informação mútua**: $I(X; Y) = H(X) - H(X \mid Y) = D_{\text{KL}}(p(x,y) \| p(x)p(y))$

Veja [[Conhecimento-Geral/Matematica/Teoria-da-Informacao|Teoria da Informação]] para tratamento completo.

---

## Referências

### Livros

1. **Casella, G. & Berger, R. L.** (2002). *Statistical Inference*. 2nd ed. Duxbury. — Referência clássica em inferência estatística, com rigor matemático completo.

2. **Hastie, T., Tibshirani, R. & Friedman, J.** (2009). *The Elements of Statistical Learning*. 2nd ed. Springer. — Ponte entre estatística e aprendizado de máquina.

3. **Murphy, K. P.** (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press. — Tratamento probabilístico unificado de ML.

4. **Bishop, C. M.** (2006). *Pattern Recognition and Machine Learning*. Springer. — Capítulos 1-3 cobrem probabilidade no contexto de reconhecimento de padrões.

5. **Gelman, A. et al.** (2013). *Bayesian Data Analysis*. 3rd ed. CRC Press. — O livro-texto definitivo em análise bayesiana.

6. **Wasserman, L.** (2004). *All of Statistics*. Springer. — Cobertura concisa e rigorosa da estatística para cientistas da computação.

### Artigos Clássicos

7. **Kolmogorov, A. N.** (1933). *Grundbegriffe der Wahrscheinlichkeitsrechnung*. — Axiomatização da probabilidade.

8. **Demspter, A. P., Laird, N. M. & Rubin, D. B.** (1977). "Maximum likelihood from incomplete data via the EM algorithm". *Journal of the Royal Statistical Society*, 39(1): 1-38. — O algoritmo EM.

9. **Kingma, D. P. & Welling, M.** (2014). "Auto-Encoding Variational Bayes". *ICLR*. — VAEs e o ELBO.

10. **Blei, D. M., Kucukelbir, A. & McAuliffe, J. D.** (2017). "Variational Inference: A Review for Statisticians". *JASA*, 112(518): 859-877.

11. **Efron, B.** (1979). "Bootstrap methods: another look at the jackknife". *The Annals of Statistics*, 7(1): 1-26. — O bootstrap.

12. **Benjamin, D. J. et al.** (2018). "Redefine statistical significance". *Nature Human Behaviour*, 2: 6-10. — Crítica ao uso do p-valor.

### Recursos Online

13. **Stanford CS229**: Probability Theory Review — Notas de revisão de probabilidade para ML.

14. **3Blue1Brown** (2019). "Bayes theorem" — Visualização intuitiva do Teorema de Bayes.

15. **StatQuest with Josh Starmer** — Série de vídeos que explica estatística e ML com clareza excepcional.

16. **Probabilistic Programming & Bayesian Methods for Hackers** (Davidson-Pilon) — Livro online gratuito sobre inferência bayesiana com PyMC3.

[[Conhecimento-Geral/Matematica/INDEX|← Voltar ao índice de Matemática]]
