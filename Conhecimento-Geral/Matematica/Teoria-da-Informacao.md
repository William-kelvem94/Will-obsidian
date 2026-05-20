---
title: "Teoria da Informação"
date: 2026-05-16
area: "Matemática para IA"
tags:
  [
    conhecimento,
    conceito,
    matematica,
    informacao,
    entropia,
    shannon,
    compressao,
    codificacao,
  ]
related:
  [
    "Conhecimento-Geral/Matematica/Probabilidade-e-Estatistica",
    "Conhecimento-Geral/Matematica/Algebra-Linear-Essencial",
    "Conhecimento-Geral/Matematica/Calculo-e-Otimizacao",
    "Conhecimento-Geral/Psicologia/Vieses-em-LLMs",
    "Conhecimento-Geral/Neurociencia/Sistemas-de-Memoria",
  ]
aliases:
  [
    "Informação",
    "Entropia",
    "Teoria de Shannon",
    "Codificação de Fonte",
    "Informação Mútua",
  ]
---

# Teoria da Informação

## Visão Geral

A teoria da informação, fundada por Claude Shannon em seu artigo seminal de 1948 *"A Mathematical Theory of Communication"*, estabelece limites fundamentais sobre compressão, armazenamento e comunicação de dados. Em inteligência artificial, seus conceitos são ubíquos: entropia cruzada é a função de perda padrão para classificação e modelagem de linguagem; divergência KL regulariza autoencoders variacionais (VAEs); informação mútua guia seleção de features e aprendizado de representações; e o princípio da informação bottleneck explica o aprendizado profundo.

Este documento desenvolve desde a entropia de Shannon e a divergência KL até tópicos avançados como capacidade de canal, teoria taxa-distorção e o método do information bottleneck, conectando a teoria às aplicações modernas em IA.

---

## Entropia de Shannon

### Motivação e Definição

Suponha que observamos amostras de uma distribuição $p(x)$. Quanta "informação" recebemos ao observar um evento $x$?

**Requisitos intuitivos para uma medida de informação** $I(x)$:

1. $I(x)$ deve depender apenas de $p(x)$
2. $I(x) \geq 0$ (informação não-negativa)
3. Se $p(x) = 1$, então $I(x) = 0$ (evento certo não surpreende)
4. Se $p(x)$ é pequeno, $I(x)$ é grande (evento raro surpreende mais)
5. **Aditividade**: $I(x, y) = I(x) + I(y)$ para eventos independentes

O requisito (5) força $I$ a ser logarítmica:

$$
I(x) = \log \frac{1}{p(x)} = -\log p(x)
$$

A **entropia** de Shannon é o valor esperado da informação:

$$
H(p) = \mathbb{E}_{x \sim p}[-\log p(x)] = -\sum_{x \in \mathcal{X}} p(x) \log p(x)
$$

Para distribuições contínuas (entropia diferencial):

$$
H(p) = -\int_{\mathcal{X}} p(x) \log p(x) \, dx
$$

**Unidades**: log base 2 → bits; log base $e$ (natural) → nats; log base 10 → dits (hartleys).

### Interpretações da Entropia

1. **Incerteza média**: quanta incerteza existe sobre o valor de $X$
2. **Surpresa média**: quão surpreendente é $X$ em média
3. **Comprimento de código ótimo**: número mínimo de bits necessário para codificar amostras de $p$

### Entropia de Distribuições Comuns

- Bernoulli($p$): $H(p) = -p \log p - (1-p) \log(1-p)$ (≤ 1 bit, máximo em $p = 0.5$)
- Uniforme($N$): $H = \log N$ (máxima entropia para suporte finito)
- Normal($\mu, \sigma^2$): $H = \frac{1}{2} \log(2\pi e \sigma^2)$

### Derivação: Entropia como Medida de Informação

Shannon derivou a entropia axiomática e também mostrou que ela é o único funcional (a menos de constante multiplicativa) que satisfaz:

1. Continuidade em $p$
2. Máximo para distribuição uniforme
3. **Decomposição de grupo**: $H(p_1, \ldots, p_n) = H(p_1 + p_2, p_3, \ldots, p_n) + (p_1 + p_2) H\left(\frac{p_1}{p_1+p_2}, \frac{p_2}{p_1+p_2}\right)$

### Exemplo: Entropia de Bernoulli

```python
import numpy as np
import matplotlib.pyplot as plt

def entropy(p):
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return -(p * np.log2(p) + (1 - p) * np.log2(1 - p))

ps = np.linspace(0, 1, 200)
H = entropy(ps)

plt.figure(figsize=(8, 4))
plt.plot(ps, H, 'b-', linewidth=2)
plt.axvline(0.5, color='r', linestyle='--', alpha=0.5, label='p=0.5 (máx = 1 bit)')
plt.axhline(1, color='r', linestyle=':', alpha=0.5)
plt.xlabel('p (probabilidade de cara)')
plt.ylabel('Entropia H(p) [bits]')
plt.title('Entropia da Distribuição Bernoulli')
plt.legend(); plt.grid()
plt.show()
```

---

## Entropia Conjunta e Condicional

### Entropia Conjunta

A entropia de duas variáveis aleatórias $(X, Y)$ com distribuição conjunta $p(x, y)$:

$$
H(X, Y) = -\sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p(x, y) \log p(x, y)
$$

Propriedade: $H(X, Y) \leq H(X) + H(Y)$ com igualdade se $X$ e $Y$ são independentes.

### Entropia Condicional

A entropia de $Y$ dado que conhecemos $X$:

$$
H(Y \mid X) = -\sum_{x, y} p(x, y) \log p(y \mid x) = \mathbb{E}_x[H(Y \mid X = x)]
$$

**Regra da cadeia para entropia**:

$$
H(X, Y) = H(X) + H(Y \mid X) = H(Y) + H(X \mid Y)
$$

Generalizando para $n$ variáveis:

$$
H(X_1, X_2, \ldots, X_n) = \sum_{i=1}^n H(X_i \mid X_1, \ldots, X_{i-1})
$$

Esta regra da cadeia é a base da modelagem autoregressiva em LLMs (GPT, LLaMA): cada token é previsto condicionado aos tokens anteriores.

### Exemplo: Entropia Conjunta e Condicional

```python
import numpy as np

# Distribuição conjunta simples
p_xy = np.array([[0.3, 0.1],
                 [0.1, 0.5]])

# Marginais
p_x = p_xy.sum(axis=1)
p_y = p_xy.sum(axis=0)

# Entropia conjunta
H_xy = -np.sum(p_xy * np.log2(p_xy + 1e-12))
print(f"H(X, Y) = {H_xy:.3f} bits")

# Entropias individuais
H_x = -np.sum(p_x * np.log2(p_x + 1e-12))
H_y = -np.sum(p_y * np.log2(p_y + 1e-12))
print(f"H(X) = {H_x:.3f} bits")
print(f"H(Y) = {H_y:.3f} bits")

# Entropia condicional: H(Y|X) = H(X,Y) - H(X)
H_y_given_x = H_xy - H_x
print(f"H(Y|X) = {H_y_given_x:.3f} bits")

# Verificação: H(Y|X) <= H(Y)
print(f"H(Y|X) <= H(Y)? {H_y_given_x <= H_y}")
```

---

## Divergência KL (Kullback-Leibler)

### Definição e Intuição

A divergência KL (ou entropia relativa) mede a "distância" entre duas distribuições de probabilidade $p$ e $q$:

$$
D_{\text{KL}}(p \| q) = \sum_{x \in \mathcal{X}} p(x) \log \frac{p(x)}{q(x)} = \mathbb{E}_{x \sim p}\left[\log \frac{p(x)}{q(x)}\right]
$$

**Interpretações**:

1. **Custo de codificação**: bits extras necessários para codificar dados de $p$ usando um código ótimo para $q$
2. **Surpresa relativa**: quão mais surpreendentes são amostras de $p$ quando medidas contra $q$
3. **Informação discriminante**: quanta informação ganhamos ao usar $p$ em vez de $q$

### Propriedades

1. **Não-negatividade**: $D_{\text{KL}}(p \| q) \geq 0$, com igualdade se e somente se $p = q$ q.s.
2. **Não-simetria**: $D_{\text{KL}}(p \| q) \neq D_{\text{KL}}(q \| p)$ em geral — não é uma métrica
3. **Convexidade**: $D_{\text{KL}}(p \| q)$ é convexa em $(p, q)$

### Desigualdade de Gibbs

Aplicando a desigualdade de Jensen ao logaritmo:

$$
D_{\text{KL}}(p \| q) \geq 0
$$

**Prova**: $\log$ é côncavo, então $-\sum p \log \frac{q}{p} \geq -\log \sum p \frac{q}{p} = -\log 1 = 0$.

### Divergência KL em ML

1. **VAEs**: o termo de regularização é $D_{\text{KL}}(q_\phi(\mathbf{z} \mid \mathbf{x}) \| p(\mathbf{z}))$
2. **Policy gradients**: $D_{\text{KL}}(\pi_{\text{old}} \| \pi_{\text{new}})$ em TRPO/P PO
3. **Knowledge distillation**: $D_{\text{KL}}(p_{\text{teacher}} \| p_{\text{student}})$
4. **Variational inference**: minimizar $D_{\text{KL}}(q(\theta) \| p(\theta \mid \mathcal{D}))$
5. **Information bottleneck**: $D_{\text{KL}}(p(\mathbf{z} \mid \mathbf{x}) \| r(\mathbf{z}))$

### Exemplo: Divergência KL entre Gaussianas

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def kl_divergence_gaussian(mu_p, sigma_p, mu_q, sigma_q):
    """KL(p || q) para duas Gaussianas univariadas"""
    return (np.log(sigma_q / sigma_p) + 
            (sigma_p**2 + (mu_p - mu_q)**2) / (2 * sigma_q**2) - 0.5)

# Duas Gaussianas
mu_p, sigma_p = 0, 1
mu_q, sigma_q = 1, 0.8

x = np.linspace(-4, 4, 500)
p = stats.norm.pdf(x, mu_p, sigma_p)
q = stats.norm.pdf(x, mu_q, sigma_q)

kl_pq = kl_divergence_gaussian(mu_p, sigma_p, mu_q, sigma_q)
kl_qp = kl_divergence_gaussian(mu_q, sigma_q, mu_p, sigma_p)

plt.figure(figsize=(10, 5))
plt.plot(x, p, 'b-', label=f'p ~ N({mu_p}, {sigma_p}²)')
plt.plot(x, q, 'r-', label=f'q ~ N({mu_q}, {sigma_q}²)')
plt.fill_between(x, p, np.zeros_like(x), alpha=0.1, color='b')
plt.fill_between(x, q, np.zeros_like(x), alpha=0.1, color='r')
plt.title(f'KL(p||q) = {kl_pq:.3f} nats,  KL(q||p) = {kl_qp:.3f} nats')
plt.xlabel('x'); plt.ylabel('Densidade')
plt.legend(); plt.grid()
plt.show()
```

---

## Entropia Cruzada (Cross-Entropy)

### Definição

A entropia cruzada entre $p$ (verdadeira) e $q$ (modelo) é:

$$
H(p, q) = -\sum_{x \in \mathcal{X}} p(x) \log q(x) = H(p) + D_{\text{KL}}(p \| q)
$$

**Relação fundamental**: minimizar entropia cruzada equivale a minimizar divergência KL (pois $H(p)$ é constante).

$$
\arg\min_q H(p, q) = \arg\min_q D_{\text{KL}}(p \| q)
$$

### Entropia Cruzada como Função de Perda

Em classificação, $p$ é a distribuição one-hot dos rótulos verdadeiros e $q$ é a saída softmax do modelo:

$$
\mathcal{L}_{\text{CE}} = -\sum_{i=1}^n \sum_{k=1}^K y_{ik} \log \hat{y}_{ik}
$$

Para um único exemplo com classe verdadeira $c$: $\mathcal{L}_{\text{CE}} = -\log \hat{y}_c$

### Entropia Cruzada em LLMs

Modelos de linguagem autoregressivos (GPT, LLaMA, Claude) minimizam a entropia cruzada sobre tokens:

$$
\mathcal{L} = -\frac{1}{T} \sum_{t=1}^T \log p_\theta(x_t \mid x_{<t})
$$

A **perplexidade** (perplexity) é:

$$
\text{PPL} = \exp\left(-\frac{1}{T} \sum_{t=1}^T \log p_\theta(x_t \mid x_{<t})\right) = 2^{H(p, q)}
$$

Menor perplexidade = melhor modelo.

### Exemplo: Cross-Entropy vs MSE

```python
import numpy as np
import matplotlib.pyplot as plt

# Comparação: cross-entropy vs MSE para classificação binária
y_true = 1  # classe verdadeira

def cross_entropy_loss(y_pred):
    return -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

def mse_loss(y_pred):
    return (y_true - y_pred)**2

preds = np.linspace(0.001, 0.999, 200)
ce = cross_entropy_loss(preds)
mse = mse_loss(preds)

plt.figure(figsize=(10, 4))
plt.plot(preds, ce, 'r-', label='Cross-Entropy')
plt.plot(preds, mse, 'b-', label='MSE')
plt.axvline(y_true, color='k', linestyle='--', alpha=0.5, label='Valor verdadeiro')
plt.xlabel('Predição'); plt.ylabel('Perda')
plt.legend(); plt.grid()
plt.title('Cross-Entropy vs MSE para Classificação Binária')
plt.show()

# Note: cross-entropy penaliza muito mais predições confiantes e erradas
```

---

## Informação Mútua

### Definição

A informação mútua $I(X; Y)$ mede a quantidade de informação que uma variável contém sobre a outra:

$$
I(X; Y) = D_{\text{KL}}(p(x, y) \| p(x)p(y)) = \sum_{x, y} p(x, y) \log \frac{p(x, y)}{p(x)p(y)}
$$

### Relações Fundamentais

$$
I(X; Y) = H(X) - H(X \mid Y) = H(Y) - H(Y \mid X)
$$
$$
I(X; Y) = H(X) + H(Y) - H(X, Y)
$$
$$
I(X; Y) = I(Y; X) \quad \text{(simétrica)}
$$
$$
I(X; Y) \geq 0 \quad \text{com igualdade se } X \perp Y
$$

### Diagrama de Venn da Informação

```
        H(X)          H(Y)
    ┌────────┐  ┌────────┐
    │        │  │        │
    │ H(X|Y) │ I│ H(Y|X) │
    │        │  │        │
    └────────┘  └────────┘
        H(X, Y)
```

### Aplicações em ML

1. **Seleção de features**: escolher features com máxima $I(\text{feature}; \text{target})$
2. **Aprendizado de representações**: maximizar $I(\mathbf{z}; \mathbf{y})$ enquanto minimiza $I(\mathbf{z}; \mathbf{x})$ (information bottleneck)
3. **Mutual Information Neural Estimation (MINE)**: estimar $I(X; Y)$ com redes neurais
4. **InfoGAN**: maximizar informação mútua entre variáveis latentes e saídas
5. **Deep InfoMax (DIM)**: maximizar $I(\text{representação}; \text{entrada})$ para aprendizado não-supervisionado

### Exemplo: Informação Mútua

```python
import numpy as np
from sklearn.feature_selection import mutual_info_classif
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

# Dados sintéticos com features relevantes e irrelevantes
X, y = make_classification(n_samples=1000, n_features=10, n_informative=3,
                           n_redundant=2, n_repeated=0, random_state=42)

# Informação mútua entre cada feature e o target
mi = mutual_info_classif(X, y)
feature_names = [f'F{i}' for i in range(10)]

plt.figure(figsize=(10, 4))
bars = plt.bar(feature_names, mi)
for i, (bar_, val) in enumerate(zip(bars, mi)):
    if val > 0.1:
        bar_.set_color('green')
    else:
        bar_.set_color('red')
plt.axhline(0.1, color='gray', linestyle='--', alpha=0.7, label='Limiar')
plt.xlabel('Feature'); plt.ylabel('Informação Mútua (nats)')
plt.title('Seleção de Features via Informação Mútua')
plt.legend()
plt.show()

print("Features mais relevantes:")
for idx in np.argsort(mi)[::-1][:5]:
    print(f"  F{idx}: MI = {mi[idx]:.4f}")
```

---

## Information Bottleneck (Tishby et al., 1999)

### Princípio

O **Information Bottleneck** (IB) busca um equilíbrio entre compressão e preservação de informação relevante. Dada a entrada $X$ e o target $Y$, queremos encontrar uma representação $Z$ que:

1. Seja **compressiva**: minimize $I(X; Z)$
2. Seja **preditiva**: maximize $I(Z; Y)$

**Problema de otimização**:

$$
\min_{p(z \mid x)} I(X; Z) - \beta I(Z; Y)
$$

onde $\beta \geq 0$ controla o trade-off entre compressão e predição.

### Solução

A solução ótima satisfaz a equação auto-consistente:

$$
p(z \mid x) = \frac{p(z)}{Z(x, \beta)} \exp\left(-\beta D_{\text{KL}}(p(y \mid x) \| p(y \mid z))\right)
$$

### IB em Deep Learning

Tishby & Schwartz-Ziv (2017) propuseram que o aprendizado profundo passa por duas fases:

1. **Fase de fitting**: $I(X; Z)$ e $I(Z; Y)$ aumentam juntos (a rede aprende a representação)
2. **Fase de compressão**: $I(X; Z)$ diminui enquanto $I(Z; Y)$ continua aumentando (a rede descarta informação irrelevante)

Embora este quadro seja contestado para ativações ReLU (Saxe et al., 2018), ele oferece uma lente informacional poderosa para entender o que redes profundas aprendem.

### VIB — Variational Information Bottleneck

Alemi et al. (2017) introduziram o **VIB**, que aproxima o IB com inferência variacional:

$$
\mathcal{L}_{\text{VIB}} = \mathbb{E}_{p(\mathbf{x}, \mathbf{y})} \left[ \mathbb{E}_{q(\mathbf{z} \mid \mathbf{x})}[-\log p(\mathbf{y} \mid \mathbf{z})] + \beta \, D_{\text{KL}}(q(\mathbf{z} \mid \mathbf{x}) \| r(\mathbf{z})) \right]
$$

O primeiro termo é a perda preditiva, o segundo é o custo de compressão (KL com o prior $r(\mathbf{z})$). Note a semelhança com o ELBO dos VAEs!

### Exemplo: Information Bottleneck

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Simulação do trade-off IB para uma variável Gaussiana
# X ~ N(0, 1), Y = X + noise, Z = compressão de X

def ib_tradeoff(beta, sigma_z=0.5):
    """
    Modelo linear Gaussiano:
    X ~ N(0, 1)
    Y = X + eps, eps ~ N(0, sigma_y^2)
    Z = X + eta, eta ~ N(0, sigma_z^2)
    
    I(X; Z) = 0.5 * log(1 + 1/sigma_z^2) 
    I(Z; Y) = 0.5 * log(1 + 1/(1 + sigma_z^2))
    """
    I_xz = 0.5 * np.log(1 + 1/sigma_z**2)
    I_zy = 0.5 * np.log(1 + 1/(1 + sigma_z**2))
    return I_xz, I_zy

# Varrendo beta (via sigma_z)
sigmas = np.logspace(-1, 1, 50)
I_xz_vals = []
I_zy_vals = []

for sigma_z in sigmas:
    I_xz, I_zy = ib_tradeoff(1.0, sigma_z)
    I_xz_vals.append(I_xz)
    I_zy_vals.append(I_zy)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(I_xz_vals, I_zy_vals, 'b-', linewidth=2)
plt.xlabel('I(X; Z) [nats]')
plt.ylabel('I(Z; Y) [nats]')
plt.title('Curva Information Bottleneck')
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(sigmas, I_xz_vals, 'r-', label='I(X; Z)')
plt.plot(sigmas, I_zy_vals, 'g-', label='I(Z; Y)')
plt.xscale('log')
plt.xlabel('σ_z (ruído de compressão)')
plt.ylabel('Informação [nats]')
plt.legend(); plt.grid()
plt.title('Trade-off: Compressão vs Predição')
plt.tight_layout()
plt.show()
```

---

## Capacidade de Canal

### Definição

Um **canal de comunicação** é caracterizado pela probabilidade condicional $p(y \mid x)$ de receber $y$ dado que $x$ foi enviado.

A **capacidade de canal** $C$ é a máxima informação mútua entre entrada e saída:

$$
C = \max_{p(x)} I(X; Y)
$$

### Exemplo: Canal Binário Simétrico (BSC)

Para um canal que inverte bits com probabilidade $\epsilon$:

$$
C = 1 - H_b(\epsilon) = 1 + \epsilon \log_2 \epsilon + (1 - \epsilon) \log_2 (1 - \epsilon)
$$

onde $H_b(\epsilon)$ é a entropia binária.

Se $\epsilon = 0$ (canal perfeito): $C = 1$ bit/uso
Se $\epsilon = 0.5$: $C = 0$ (canal inútil)

### Exemplo: Canal Gaussiano (AWGN)

Para $Y = X + N$ com $N \sim \mathcal{N}(0, \sigma^2)$ e potência $P = \mathbb{E}[X^2]$:

$$
C = \frac{1}{2} \log_2\left(1 + \frac{P}{\sigma^2}\right) \quad \text{bits/uso}
$$

Esta é a famosa **fórmula de Shannon-Hartley** para capacidade de canais com ruído Gaussiano branco aditivo.

### Teorema da Codificação de Canal (Shannon, 1948)

Para qualquer taxa $R < C$, existe um código que permite comunicação com probabilidade de erro arbitrariamente pequena. Para $R > C$, comunicação confiável é impossível.

Este teorema fundamental separa o possível do impossível em comunicação — e a transição é nítida.

### Exemplo: Capacidade de Canal

```python
import numpy as np
import matplotlib.pyplot as plt

def bsc_capacity(epsilon):
    """Capacidade do canal binário simétrico"""
    H = -(epsilon * np.log2(epsilon + 1e-12) + 
          (1 - epsilon) * np.log2(1 - epsilon + 1e-12))
    return 1 - H

def awgn_capacity(snr_db):
    """Capacidade do canal AWGN (Shannon-Hartley)"""
    snr_linear = 10**(snr_db / 10)
    return 0.5 * np.log2(1 + snr_linear)

epsilons = np.linspace(0, 1, 200)
C_bsc = bsc_capacity(epsilons)

snr_db = np.linspace(-20, 30, 200)
C_awgn = awgn_capacity(snr_db)

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(epsilons, C_bsc, 'b-')
plt.xlabel('ε (probabilidade de erro)')
plt.ylabel('C [bits/uso]')
plt.title('Capacidade: Canal Binário Simétrico')
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(snr_db, C_awgn, 'r-')
plt.xlabel('SNR [dB]')
plt.ylabel('C [bits/uso]')
plt.title('Capacidade: Canal AWGN (Shannon-Hartley)')
plt.grid()
plt.tight_layout()
plt.show()
```

---

## Teorema da Codificação de Fonte (Source Coding Theorem)

### Compressão Sem Perdas

Para uma fonte $X \sim p(x)$, o número mínimo de bits necessário para codificar $X$ sem perdas é:

$$
H(X) \leq \text{comprimento médio do código} < H(X) + 1
$$

Códigos de Huffman e codificação aritmética atingem este limite arbitrariamente próximo.

### Compressão com Perdas (Rate-Distortion)

Quando permitimos distorção $D$, a **função taxa-distorção** $R(D)$ dá a menor taxa possível para uma dada distorção máxima:

$$
R(D) = \min_{p(\hat{x} \mid x): \mathbb{E}[d(x, \hat{x})] \leq D} I(X; \hat{X})
$$

### Taxa-Distorção para Fonte Gaussiana

Para $X \sim \mathcal{N}(0, \sigma^2)$ e distorção quadrática $d(x, \hat{x}) = (x - \hat{x})^2$:

$$
R(D) = \begin{cases}
\frac{1}{2} \log_2 \frac{\sigma^2}{D}, & 0 \leq D \leq \sigma^2 \\
0, & D > \sigma^2
\end{cases}
$$

### Exemplo: Taxa-Distorção

```python
import numpy as np
import matplotlib.pyplot as plt

def rate_distortion_gaussian(sigma2, D):
    """Função taxa-distorção para fonte Gaussiana com MSE"""
    D = np.clip(D, 1e-10, sigma2)
    return 0.5 * np.log2(sigma2 / D)

sigma2 = 1.0
D_vals = np.logspace(-3, 0.5, 200)
R_vals = rate_distortion_gaussian(sigma2, D_vals)

plt.figure(figsize=(8, 4))
plt.plot(D_vals, R_vals, 'b-', linewidth=2)
plt.axvline(sigma2, color='r', linestyle='--', alpha=0.7)
plt.xlabel('Distorção D (MSE)')
plt.ylabel('Taxa R(D) [bits]')
plt.title(f'Taxa-Distorção: Fonte Gaussiana (σ² = {sigma2})')
plt.grid()
plt.show()
```

---

## Aplicações em Inteligência Artificial

### Entropia Cruzada em LLMs

Modelos de linguagem como GPT-4 são treinados para minimizar a entropia cruzada sobre tokens:

$$
\mathcal{L} = -\frac{1}{T} \sum_{t=1}^T \log p_\theta(x_t \mid x_{<t})
$$

A **perplexidade** é:

$$
\text{PPL} = \exp\left(\mathcal{L}\right)
$$

Um modelo com perplexidade $PPL$ é tão "surpreso" quanto um modelo uniforme sobre $PPL$ tokens.

### Information Gain em Árvores de Decisão

Algoritmos como ID3, C4.5 e CART usam **ganho de informação** para selecionar splits:

$$
\text{IG}(X, Y) = H(Y) - H(Y \mid X) = I(Y; X)
$$

O split que maximiza $I(\text{feature}; \text{target})$ é escolhido.

### Variational Autoencoders (VAEs)

O ELBO dos VAEs é:

$$
\log p(\mathbf{x}) \geq \mathbb{E}_{q(\mathbf{z} \mid \mathbf{x})}[\log p(\mathbf{x} \mid \mathbf{z})] - D_{\text{KL}}(q(\mathbf{z} \mid \mathbf{x}) \| p(\mathbf{z}))
$$

Reconhecemos aqui:
- $\mathbb{E}[\log p(\mathbf{x} \mid \mathbf{z})]$: reconstrução (negativo da entropia cruzada)
- $D_{\text{KL}}(q \| p)$: regularização (informação bottleneck)

### InfoGAN

InfoGAN maximiza:

$$
\max_{G, Q} V(D, G) - \lambda I(\mathbf{c}; G(\mathbf{z}, \mathbf{c}))
$$

onde $I(\mathbf{c}; \mathbf{x})$ é a informação mútua entre o código latente $\mathbf{c}$ e a saída gerada.

### Normalizing Flows

Flows transformam uma distribuição simples $p(\mathbf{z})$ em uma complexa $p(\mathbf{x})$ através de transformações invertíveis:

$$
\log p(\mathbf{x}) = \log p(\mathbf{z}) - \log \left|\det \frac{\partial f}{\partial \mathbf{z}}\right|
$$

O determinante do Jacobiano mede a "mudança de volume" — um conceito diretamente ligado à entropia e codificação.

### Exemplo: Implementação de um Codificador Simples

```python
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def huffman_encode(data):
    """Codificação de Huffman simplificada"""
    freq = Counter(data)
    total = len(data)
    # Entropia
    entropy = -sum((c/total) * np.log2(c/total) for c in freq.values())
    # Comprimento médio do código (ótimo para símbolos equiprováveis)
    # Na prática, Huffman dá comprimento ~ H + 1
    return entropy

# Comparar entropia de diferentes textos
textos = {
    "Português": "a casa é amarela e a rua é clara",
    "Inglês": "the house is yellow and the street is bright",
    "Aleatório": "xkz ptq mnv lwrf hjq dsp kx"
}

for nome, texto in textos.items():
    texto = texto.replace(" ", "").lower()
    h = huffman_encode(texto)
    print(f"{nome}: {len(texto)} chars, H ≈ {h:.3f} bits/char")
```

---

## Conceitos Avançados

### Desigualdade de Processamento de Dados (DPI)

Para uma cadeia de Markov $X \to Y \to Z$:

$$
I(X; Z) \leq I(X; Y)
$$

Processar dados não aumenta informação — apenas pode descartá-la. Isto é fundamental em deep learning: cada camada pode apenas diminuir (ou manter) a informação sobre a entrada.

### Entropia de von Neumann (Mecânica Quântica)

A generalização quântica da entropia de Shannon para matrizes densidade $\rho$:

$$
S(\rho) = -\text{tr}(\rho \log \rho)
$$

Usada em computação quântica e em certos modelos de representações neurais.

### Entropia de Rényi

Generalização paramétrica da entropia:

$$
H_\alpha(p) = \frac{1}{1-\alpha} \log \sum_{i=1}^n p_i^\alpha
$$

No limite $\alpha \to 1$, $H_\alpha \to H$ (entropia de Shannon). Para $\alpha = \infty$, $H_\infty = -\log \max_i p_i$ (entropia min).

### Divergência de Jensen-Shannon

Uma versão simetrizada da divergência KL:

$$
D_{\text{JS}}(p \| q) = \frac{1}{2} D_{\text{KL}}\left(p \,\Big\|\, \frac{p+q}{2}\right) + \frac{1}{2} D_{\text{KL}}\left(q \,\Big\|\, \frac{p+q}{2}\right)
$$

$0 \leq D_{\text{JS}} \leq \log 2$, e $\sqrt{D_{\text{JS}}}$ é uma métrica verdadeira. Usada em GANs (no critério de discriminação original).

### Máxima Entropia (MaxEnt)

O princípio da máxima entropia: entre todas as distribuições consistentes com as observações, escolha aquela de máxima entropia. Isto produz a distribuição **menos tendenciosa** que satisfaz as restrições.

**Exemplo**: Sob restrição de média $\mu$ e variância $\sigma^2$, a distribuição de máxima entropia é $\mathcal{N}(\mu, \sigma^2)$.

### Exemplo: Máxima Entropia

```python
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Restrições: valores em {1, 2, 3, 4, 5, 6}, média = 4
support = np.array([1, 2, 3, 4, 5, 6])
target_mean = 4.0

def neg_entropy(p):
    p = np.clip(p, 1e-12, 1)
    return np.sum(p * np.log(p))

cons = [
    {'type': 'eq', 'fun': lambda p: np.sum(p) - 1},
    {'type': 'eq', 'fun': lambda p: np.sum(p * support) - target_mean}
]
bounds = [(0, 1) for _ in support]

result = minimize(neg_entropy, x0=np.ones(6)/6, bounds=bounds, constraints=cons)
p_maxent = result.x

# Comparar com distribuição uniforme
p_uniform = np.ones(6) / 6

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.bar(support, p_uniform)
plt.title(f'Uniforme: H = {-neg_entropy(p_uniform):.3f} nats')

plt.subplot(1, 2, 2)
plt.bar(support, p_maxent)
plt.title(f'MaxEnt (média={target_mean}): H = {-neg_entropy(p_maxent):.3f} nats')
plt.tight_layout()
plt.show()
```

---

## Aplicações em Processamento de Linguagem Natural

### Surpresa e Informação em Texto

A teoria da informação oferece métricas naturais para análise de linguagem:

- **Surpresa de um token**: $-\log p(x_t \mid x_{<t})$ — surpreendência de cada palavra
- **Taxa de informação**: entropia por token (caracteriza eficiência linguística)
- **Redundância linguística**: $1 - \frac{H(\text{texto})}{\log |\text{vocabulário}|}$

### Tokenização e Subword Units

BPE (Byte-Pair Encoding), WordPiece e Unigram Language Model tokenizam texto em subwords. A escolha da tokenização afeta $H(\text{tokens})$ e, consequentemente, a eficiência de modelos de linguagem.

### Information-Theoretic Interpretability

Métodos como **logit lens** e **activation patching** usam informação mútua para entender o que cada camada de um transformer representa.

### Exemplo: Entropia de um Modelo de Linguagem

```python
import numpy as np

# Simulando saídas de um modelo de linguagem
# Probabilidades para o próximo token em um contexto dado
vocab_size = 1000  # vocabulário pequeno
probs = np.random.dirichlet(np.ones(vocab_size) * 0.1)  # distribuição esparsa

# Entropia da distribuição
H = -np.sum(probs * np.log2(probs))
perplexity = 2**H

print(f"Entropia da distribuição: {H:.3f} bits")
print(f"Perplexidade: {perplexity:.3f}")
print(f"Interpretação: modelo tão incerto quanto um uniforme sobre ~{perplexity:.0f} tokens")

# Distribuição mais concentrada
probs_sharp = np.random.dirichlet(np.ones(vocab_size) * 10)
H_sharp = -np.sum(probs_sharp * np.log2(probs_sharp))
print(f"\nDistribuição mais sharp:")
print(f"Entropia: {H_sharp:.3f} bits, Perplexidade: {2**H_sharp:.3f}")
```

---

## Referências

### Livros

1. **Shannon, C. E. & Weaver, W.** (1949). *The Mathematical Theory of Communication*. University of Illinois Press. — O texto original que fundou a teoria da informação.

2. **Cover, T. M. & Thomas, J. A.** (2006). *Elements of Information Theory*. 2nd ed. Wiley-Interscience. — A referência definitiva, cobrindo todos os aspectos teóricos com clareza e profundidade.

3. **MacKay, D. J. C.** (2003). *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press. — Conecta teoria da informação com inferência bayesiana e aprendizado de máquina. Disponível gratuitamente online.

4. **Bishop, C. M.** (2006). *Pattern Recognition and Machine Learning*. Springer. — Capítulos 1 (entropia) e 10 (inferência variacional) cobrem aplicações em ML.

5. **Murphy, K. P.** (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press. — Cobertura moderna de teoria da informação para ML.

### Artigos Seminais

6. **Shannon, C. E.** (1948). "A Mathematical Theory of Communication". *Bell System Technical Journal*, 27(3): 379-423, 623-656. — O artigo que criou o campo.

7. **Tishby, N., Pereira, F. C. & Bialek, W.** (1999). "The information bottleneck method". *37th Allerton Conference on Communication, Control, and Computing*. — Formulação do information bottleneck.

8. **Tishby, N. & Schwartz-Ziv, N.** (2017). "Opening the Black Box of Deep Neural Networks via Information". *arXiv:1703.00810*. — Aplicação do IB para entender deep learning.

9. **Alemi, A. A. et al.** (2017). "Deep Variational Information Bottleneck". *ICLR*. — VIB, unindo IB com inferência variacional.

10. **Belghazi, M. I. et al.** (2018). "Mutual Information Neural Estimation". *ICML*. — MINE, estimação de mi com redes neurais.

11. **Hjelm, R. D. et al.** (2019). "Learning Deep Representations by Mutual Information Estimation and Maximization". *ICLR*. — Deep InfoMax.

### Recursos Online

12. **3Blue1Brown** (2022). "Information Theory" — Série de vídeos que constrói a teoria da informação intuitivamente a partir de primeiros princípios.

13. **Stanford EE376A**: Information Theory (Cover & Thomas) — Curso completo disponível online.

14. **Visual Information Theory** (colah.github.io) — Artigo visual sobre entropia, divergência KL e informação mútua, com excelentes diagramas.

15. **The Information Bottleneck Method** (Tishby) — Palestras e tutoriais disponíveis no YouTube.

16. **J. V. Stone** (2015). *Information Theory: A Tutorial Introduction*. — Livro introdutório acessível com exemplos práticos.

[[Conhecimento-Geral/Matematica/INDEX|← Voltar ao índice de Matemática]]
