---
title: "Cálculo e Otimização"
date: 2026-05-16
area: "Matemática para IA"
tags:
  [
    conhecimento,
    conceito,
    matematica,
    calculo,
    otimizacao,
    gradiente,
    backpropagation,
  ]
related:
  [
    "Conhecimento-Geral/Matematica/Algebra-Linear-Essencial",
    "Conhecimento-Geral/Matematica/Teoria-da-Informacao",
    "Conhecimento-Geral/Matematica/Probabilidade-e-Estatistica",
    "Conhecimento-Geral/Neurociencia/Redes-Neurais-Biologicas",
  ]
aliases: ["Gradiente e Perda", "Cálculo Diferencial", "Otimização Numérica"]
---

# Cálculo e Otimização

## Visão Geral

O cálculo diferencial é a matemática da mudança. Em inteligência artificial, ele fornece as ferramentas para ajustar parâmetros de modelos iterativamente, minimizando funções de perda que medem o quão longe as previsões estão dos dados reais. Sem cálculo, não haveria backpropagation, gradiente descendente, Adam, ou qualquer dos algoritmos de otimização que tornam o aprendizado profundo possível.

Este documento desenvolve desde os fundamentos de derivadas e gradientes até tópicos avançados como otimização convexa, multiplicadores de Lagrange, diferenciação automática e algoritmos de otimização de segunda ordem, sempre conectando a teoria matemática às aplicações práticas em aprendizado de máquina.

---

## Derivadas

### Definição Fundamental

A derivada de uma função $f: \mathbb{R} \to \mathbb{R}$ no ponto $x$ é definida pelo limite:

$$
f'(x) = \frac{df}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
$$

Geometricamente, $f'(x)$ é a inclinação da reta tangente ao gráfico de $f$ no ponto $(x, f(x))$. Em aprendizado de máquina, a derivada indica a direção e magnitude da mudança na função de perda quando um parâmetro é alterado.

### Regras de Diferenciação

**Regra da constante**: $\frac{d}{dx}[c] = 0$

**Regra da potência**: $\frac{d}{dx}[x^n] = n x^{n-1}$

**Regra do produto**: $\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)$

**Regra do quociente**: $\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$

**Regra da cadeia**: $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$

A regra da cadeia é a ferramenta mais importante para aprendizado profundo, pois permite propagar gradientes através de composições de funções — a essência do backpropagation.

### Derivadas de Funções Comuns em ML

- $\frac{d}{dx}[e^x] = e^x$
- $\frac{d}{dx}[\ln x] = \frac{1}{x}$
- $\frac{d}{dx}[\sigma(x)] = \sigma(x)(1 - \sigma(x))$ onde $\sigma(x) = \frac{1}{1 + e^{-x}}$ (sigmoide)
- $\frac{d}{dx}[\tanh(x)] = 1 - \tanh^2(x)$
- $\frac{d}{dx}[\text{ReLU}(x)] = \begin{cases} 1 & x > 0 \\ 0 & x < 0 \end{cases}$
- $\frac{d}{dx}[\text{softmax}_i(\mathbf{x})] = \text{softmax}_i(\mathbf{x})(\delta_{ij} - \text{softmax}_j(\mathbf{x}))$

### Derivadas Parciais

Para $f: \mathbb{R}^n \to \mathbb{R}$, a derivada parcial em relação a $x_i$ é:

$$
\frac{\partial f}{\partial x_i} = \lim_{h \to 0} \frac{f(x_1, \ldots, x_i + h, \ldots, x_n) - f(x_1, \ldots, x_n)}{h}
$$

### Gradiente

O gradiente $\nabla f$ é o vetor de todas as derivadas parciais:

$$
\nabla f(\mathbf{x}) = \begin{bmatrix} \frac{\partial f}{\partial x_1} & \frac{\partial f}{\partial x_2} & \cdots & \frac{\partial f}{\partial x_n} \end{bmatrix}^\top
$$

O gradiente aponta na direção de maior aumento de $f$. O **gradiente descendente** move-se na direção oposta ($-\nabla f$) para minimizar $f$.

### Jacobiana

Para uma função vetorial $f: \mathbb{R}^n \to \mathbb{R}^m$, a matriz Jacobiana $\mathbf{J}_f \in \mathbb{R}^{m \times n}$ é:

$$
\mathbf{J}_f = \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\
\vdots & \ddots & \vdots \\
\frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix}
$$

A Jacobiana da transformação de uma camada de rede neural $f(\mathbf{x}) = \sigma(\mathbf{W}\mathbf{x} + \mathbf{b})$ é:

$$
\mathbf{J}_f = \text{diag}(\sigma'(\mathbf{W}\mathbf{x} + \mathbf{b})) \cdot \mathbf{W}
$$

### Hessiana

Para $f: \mathbb{R}^n \to \mathbb{R}$, a Hessiana $\mathbf{H}_f \in \mathbb{R}^{n \times n}$ contém as derivadas de segunda ordem:

$$
\mathbf{H}_f = \begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}
$$

A Hessiana é simétrica se as derivadas mistas são contínuas (Teorema de Clairaut/Schwarz). Ela descreve a curvatura local da função:

- Se $\mathbf{H}_f$ é positiva definida: mínimo local
- Se $\mathbf{H}_f$ é negativa definida: máximo local
- Se $\mathbf{H}_f$ tem autovalores positivos e negativos: ponto de sela

### Exemplo: Gradiente e Hessiana

```python
import numpy as np

def rosenbrock(x, y, a=1, b=100):
    """Função de Rosenbrock (minimização clássica)"""
    return (a - x)**2 + b * (y - x**2)**2

def grad_rosenbrock(x, y, a=1, b=100):
    dx = -2*(a - x) - 4*b*x*(y - x**2)
    dy = 2*b*(y - x**2)
    return np.array([dx, dy])

def hess_rosenbrock(x, y, a=1, b=100):
    dxx = 2 - 4*b*y + 12*b*x**2
    dxy = -4*b*x
    dyx = -4*b*x
    dyy = 2*b
    return np.array([[dxx, dxy], [dyx, dyy]])

# Ponto de avaliação
x0, y0 = 0.5, 0.5
g = grad_rosenbrock(x0, y0)
H = hess_rosenbrock(x0, y0)
print(f"Gradiente: {g}")
print(f"Hessiana:\n{H}")
print(f"Autovalores da Hessiana: {np.linalg.eigvals(H)}")
```

---

## Série de Taylor

### Expansão Escalar

Para $f: \mathbb{R} \to \mathbb{R}$ infinitamente diferenciável:

$$
f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(x - a)^n
$$

A aproximação de primeira ordem: $f(x) \approx f(a) + f'(a)(x - a)$

A aproximação de segunda ordem: $f(x) \approx f(a) + f'(a)(x - a) + \frac{1}{2}f''(a)(x - a)^2$

### Expansão Multivariada

Para $f: \mathbb{R}^n \to \mathbb{R}$:

$$
f(\mathbf{x} + \Delta\mathbf{x}) \approx f(\mathbf{x}) + \nabla f(\mathbf{x})^\top \Delta\mathbf{x} + \frac{1}{2} \Delta\mathbf{x}^\top \mathbf{H}_f(\mathbf{x}) \Delta\mathbf{x}
$$

A aproximação de primeira ordem fundamenta o gradiente descendente. A aproximação de segunda ordem fundamenta o método de Newton.

### Exemplo: Aproximação de Taylor

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) * np.sin(2*x)

def df(x):
    return np.exp(x) * (np.sin(2*x) + 2*np.cos(2*x))

def d2f(x):
    return np.exp(x) * (4*np.cos(2*x) - 3*np.sin(2*x))

x0 = 0.5
xs = np.linspace(-1, 2, 100)

taylor1 = f(x0) + df(x0) * (xs - x0)
taylor2 = f(x0) + df(x0)*(xs - x0) + 0.5*d2f(x0)*(xs - x0)**2

plt.figure(figsize=(10, 5))
plt.plot(xs, f(xs), 'k-', label='f(x)')
plt.plot(xs, taylor1, 'r--', label='Taylor 1ª ordem')
plt.plot(xs, taylor2, 'b--', label='Taylor 2ª ordem')
plt.axvline(x0, color='gray', linestyle=':')
plt.legend(); plt.grid(); plt.title('Aproximações de Taylor')
plt.show()
```

---

## Regra da Cadeia Vetorial

### Formulação Geral

Seja $f: \mathbb{R}^m \to \mathbb{R}$ e $g: \mathbb{R}^n \to \mathbb{R}^m$, com $h(\mathbf{x}) = f(g(\mathbf{x}))$. Então:

$$
\nabla h(\mathbf{x}) = \mathbf{J}_g(\mathbf{x})^\top \nabla f(g(\mathbf{x}))
$$

Em notação de componentes:

$$
\frac{\partial h}{\partial x_i} = \sum_{j=1}^m \frac{\partial f}{\partial g_j} \cdot \frac{\partial g_j}{\partial x_i}
$$

Esta é a base matemática do backpropagation: cada camada da rede aplica a regra da cadeia para computar gradientes dos pesos.

### Propagação em Redes Neurais

Para uma rede com $L$ camadas:

$$
\mathbf{h}^{(1)} = f_1(\mathbf{x}, \mathbf{W}^{(1)})
$$
$$
\mathbf{h}^{(2)} = f_2(\mathbf{h}^{(1)}, \mathbf{W}^{(2)})
$$
$$
\vdots
$$
$$
\hat{\mathbf{y}} = f_L(\mathbf{h}^{(L-1)}, \mathbf{W}^{(L)})
$$
$$
\mathcal{L} = \ell(\hat{\mathbf{y}}, \mathbf{y})
$$

O gradiente em relação aos pesos da camada $\ell$ é:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(\ell)}} = 
\frac{\partial \mathcal{L}}{\partial \hat{\mathbf{y}}} \cdot
\frac{\partial \hat{\mathbf{y}}}{\partial \mathbf{h}^{(L-1)}} \cdots
\frac{\partial \mathbf{h}^{(\ell+1)}}{\partial \mathbf{h}^{(\ell)}} \cdot
\frac{\partial \mathbf{h}^{(\ell)}}{\partial \mathbf{W}^{(\ell)}}
$$

Cada termo $\frac{\partial \mathbf{h}^{(k+1)}}{\partial \mathbf{h}^{(k)}}$ é a Jacobiana da camada $k+1$ em relação à sua entrada.

### Exemplo: Regra da Cadeia

```python
import numpy as np

# Funções simples para demonstrar a regra da cadeia
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_grad(x):
    s = sigmoid(x)
    return s * (1 - s)

def linear(x, W, b):
    return W @ x + b

# Forward pass simples
x = np.array([1.0, 2.0])
W = np.array([[0.5, -0.3], [0.2, 0.8]])
b = np.array([0.1, -0.1])

z = linear(x, W, b)  # pré-ativação
a = sigmoid(z)       # ativação

# Gradiente local: d_a / d_z = sigmoid'(z)
dz = sigmoid_grad(z)
print(f"d_a/d_z = {dz}")

# Gradiente em relação a W: d_a/d_W = dz/dW * d_a/dz
# dz/dW = x^T (para cada saída)
dW = np.outer(dz, x)  # Gradiente para pesos
print(f"d_a/d_W:\n{dW}")
```

---

## Gradiente Descendente e Variantes

### Gradiente Descendente Batch

O algoritmo mais fundamental de otimização em ML:

$$
\theta_{t+1} = \theta_t - \eta \nabla_\theta \mathcal{L}(\theta_t)
$$

onde $\eta$ é a taxa de aprendizado (learning rate).

**Algoritmo**:

1. Computar $\nabla_\theta \mathcal{L}(\theta_t)$ sobre todo o dataset
2. Atualizar $\theta_{t+1} = \theta_t - \eta \nabla_\theta \mathcal{L}(\theta_t)$
3. Repetir até convergência

### Gradiente Descendente Estocástico (SGD)

Usa um único exemplo por atualização:

$$
\theta_{t+1} = \theta_t - \eta \nabla_\theta \ell(\mathbf{x}_i, y_i; \theta_t)
$$

- **Vantagem**: atualizações muito rápidas, escapa de mínimos locais rasos
- **Desvantagem**: alta variância no gradiente, convergência ruidosa

### Mini-Batch SGD

Compromisso entre batch e estocástico: usa um subconjunto (mini-batch) de $m$ exemplos:

$$
\theta_{t+1} = \theta_t - \eta \frac{1}{m} \sum_{i=1}^m \nabla_\theta \ell(\mathbf{x}_i, y_i; \theta_t)
$$

É a variante mais usada na prática. Tamanhos típicos de mini-batch: 32, 64, 128, 256.

### Momentum

O momentum acelera o SGD acumulando um vetor de velocidade:

$$
\mathbf{v}_{t+1} = \beta \mathbf{v}_t + \eta \nabla_\theta \mathcal{L}(\theta_t)
$$
$$
\theta_{t+1} = \theta_t - \mathbf{v}_{t+1}
$$

onde $\beta \in [0, 1)$ controla o decaimento do momentum (tipicamente 0.9). Isto suaviza a trajetória e acelera a convergência em direções consistentes.

### Nesterov Momentum

Uma variante que olha "adiante" calculando o gradiente na posição aproximada futura:

$$
\mathbf{v}_{t+1} = \beta \mathbf{v}_t + \eta \nabla_\theta \mathcal{L}(\theta_t - \beta \mathbf{v}_t)
$$
$$
\theta_{t+1} = \theta_t - \mathbf{v}_{t+1}
$$

Nesterov geralmente converge mais rápido que o momentum padrão.

### Adam (Adaptive Moment Estimation)

Adam combina momentum com taxas de aprendizado adaptativas por parâmetro:

$$
\mathbf{m}_t = \beta_1 \mathbf{m}_{t-1} + (1 - \beta_1) \nabla_\theta \mathcal{L}(\theta_t)
$$
$$
\mathbf{v}_t = \beta_2 \mathbf{v}_{t-1} + (1 - \beta_2) (\nabla_\theta \mathcal{L}(\theta_t))^2
$$
$$
\hat{\mathbf{m}}_t = \frac{\mathbf{m}_t}{1 - \beta_1^t}, \quad
\hat{\mathbf{v}}_t = \frac{\mathbf{v}_t}{1 - \beta_2^t}
$$
$$
\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{\hat{\mathbf{v}}_t} + \epsilon} \hat{\mathbf{m}}_t
$$

Hiperparâmetros padrão: $\eta = 0.001$, $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\epsilon = 10^{-8}$.

Adam é o otimizador padrão para a maioria das arquiteturas de deep learning, desde CNNs até transformers.

### Exemplo: SGD e Adam

```python
import numpy as np
import matplotlib.pyplot as plt

# Função objetivo: f(x, y) = x^2 + 10*y^2 (vale elíptico)
def f(x, y):
    return x**2 + 10*y**2

def grad_f(x, y):
    return np.array([2*x, 20*y])

def sgd(x0, y0, lr=0.1, n_iters=50):
    path = [(x0, y0)]
    x, y = x0, y0
    for _ in range(n_iters):
        g = grad_f(x, y)
        x -= lr * g[0]
        y -= lr * g[1]
        path.append((x, y))
    return path

def adam(x0, y0, lr=0.1, beta1=0.9, beta2=0.999, eps=1e-8, n_iters=50):
    path = [(x0, y0)]
    x, y = x0, y0
    mx, my = 0, 0
    vx, vy = 0, 0
    for t in range(1, n_iters + 1):
        gx, gy = grad_f(x, y)
        mx = beta1 * mx + (1 - beta1) * gx
        my = beta1 * my + (1 - beta1) * gy
        vx = beta2 * vx + (1 - beta2) * gx**2
        vy = beta2 * vy + (1 - beta2) * gy**2
        m_hat_x = mx / (1 - beta1**t)
        m_hat_y = my / (1 - beta1**t)
        v_hat_x = vx / (1 - beta2**t)
        v_hat_y = vy / (1 - beta2**t)
        x -= lr * m_hat_x / (np.sqrt(v_hat_x) + eps)
        y -= lr * m_hat_y / (np.sqrt(v_hat_y) + eps)
        path.append((x, y))
    return path

x0, y0 = 2.0, 1.5
path_sgd = sgd(x0, y0, lr=0.05)
path_adam = adam(x0, y0, lr=0.1)

xs = np.linspace(-2.5, 2.5, 100)
ys = np.linspace(-1.5, 1.5, 100)
X, Y = np.meshgrid(xs, ys)
Z = f(X, Y)

plt.figure(figsize=(12, 5))
for i, (path, name) in enumerate([(path_sgd, 'SGD'), (path_adam, 'Adam')]):
    plt.subplot(1, 2, i+1)
    plt.contour(X, Y, Z, levels=20, alpha=0.6)
    path_arr = np.array(path)
    plt.plot(path_arr[:, 0], path_arr[:, 1], 'r.-', markersize=4)
    plt.plot(path_arr[0, 0], path_arr[0, 1], 'go', label='Início')
    plt.plot(path_arr[-1, 0], path_arr[-1, 1], 'ro', label='Fim')
    plt.xlabel('x'); plt.ylabel('y')
    plt.title(name); plt.legend()
plt.tight_layout()
plt.show()
```

---

## Convexidade e Otimização Convexa

### Definição

Um conjunto $\mathcal{C}$ é convexo se para quaisquer $\mathbf{x}, \mathbf{y} \in \mathcal{C}$ e $\lambda \in [0, 1]$:

$$
\lambda \mathbf{x} + (1 - \lambda) \mathbf{y} \in \mathcal{C}
$$

Uma função $f$ é **convexa** se seu domínio é convexo e:

$$
f(\lambda \mathbf{x} + (1 - \lambda) \mathbf{y}) \leq \lambda f(\mathbf{x}) + (1 - \lambda) f(\mathbf{y})
$$

### Caracterizações de Convexidade

1. **Gradiente**: $f(\mathbf{y}) \geq f(\mathbf{x}) + \nabla f(\mathbf{x})^\top (\mathbf{y} - \mathbf{x})$
2. **Hessiana**: $\mathbf{H}_f(\mathbf{x}) \succeq 0$ (positiva semidefinida)

### Importância em ML

- Funções convexas têm **um único mínimo global** — qualquer mínimo local é global.
- Problemas de otimização convexa podem ser resolvidos eficientemente e com garantias.
- A regressão linear, regressão logística e SVM com kernel linear são problemas convexos.
- Redes neurais profundas são **não-convexas** — têm múltiplos mínimos locais e pontos de sela.

### Otimização Não-Convexa

A maioria dos problemas em deep learning é não-convexa. Na prática:

- Mínimos locais "rasos" são raros em altas dimensões
- A maioria dos pontos críticos são pontos de sela, não mínimos
- SGD e Adam escapam naturalmente de pontos de sela devido ao ruído estocástico
- A qualidade do mínimo encontrado depende da arquitetura, inicialização e regularização

### Exemplo: Convexidade Visualizada

```python
import numpy as np
import matplotlib.pyplot as plt

# Função convexa: f(x) = x^2
# Função não-convexa: g(x) = x^3 - 3x

x = np.linspace(-3, 3, 100)
f = x**2
g = x**3 - 3*x

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(x, f, 'b-')
plt.title('Convexa: $f(x) = x^2$')
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(x, g, 'r-')
plt.title('Não-convexa: $g(x) = x^3 - 3x$')
plt.grid()
plt.tight_layout()
plt.show()
```

---

## Multiplicadores de Lagrange

### Otimização com Restrições de Igualdade

Para minimizar $f(\mathbf{x})$ sujeito a $g(\mathbf{x}) = 0$, definimos o Lagrangiano:

$$
\mathcal{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) + \lambda g(\mathbf{x})
$$

O ponto ótimo satisfaz as condições de KKT (Karush-Kuhn-Tucker):

$$
\nabla_\mathbf{x} \mathcal{L}(\mathbf{x}^*, \lambda^*) = \nabla f(\mathbf{x}^*) + \lambda^* \nabla g(\mathbf{x}^*) = \mathbf{0}
$$
$$
g(\mathbf{x}^*) = 0
$$

### Otimização com Restrições de Desigualdade

Para $f(\mathbf{x})$ sujeito a $g_i(\mathbf{x}) \leq 0$ e $h_j(\mathbf{x}) = 0$:

$$
\mathcal{L}(\mathbf{x}, \boldsymbol{\lambda}, \boldsymbol{\mu}) = f(\mathbf{x}) + \sum_i \lambda_i g_i(\mathbf{x}) + \sum_j \mu_j h_j(\mathbf{x})
$$

Condições KKT completas:
1. $\nabla \mathcal{L} = 0$ (estacionariedade)
2. $g_i(\mathbf{x}^*) \leq 0$, $h_j(\mathbf{x}^*) = 0$ (factibilidade primal)
3. $\lambda_i \geq 0$ (factibilidade dual)
4. $\lambda_i g_i(\mathbf{x}^*) = 0$ (complementaridade)

### Derivação do SVM

A Support Vector Machine (SVM) busca maximizar a margem entre classes. O problema primal é:

$$
\min_{\mathbf{w}, b} \frac{1}{2} \|\mathbf{w}\|^2 \quad \text{sujeito a} \quad y_i(\mathbf{w}^\top \mathbf{x}_i + b) \geq 1, \ \forall i
$$

O Lagrangiano:

$$
\mathcal{L}(\mathbf{w}, b, \boldsymbol{\alpha}) = \frac{1}{2} \|\mathbf{w}\|^2 - \sum_{i=1}^m \alpha_i [y_i(\mathbf{w}^\top \mathbf{x}_i + b) - 1]
$$

Derivando em relação a $\mathbf{w}$ e $b$:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{w}} = \mathbf{w} - \sum_i \alpha_i y_i \mathbf{x}_i = \mathbf{0} \implies \mathbf{w} = \sum_i \alpha_i y_i \mathbf{x}_i
$$
$$
\frac{\partial \mathcal{L}}{\partial b} = -\sum_i \alpha_i y_i = 0 \implies \sum_i \alpha_i y_i = 0
$$

Substituindo no Lagrangiano, obtemos o problema dual:

$$
\max_\boldsymbol{\alpha} \sum_i \alpha_i - \frac{1}{2} \sum_i \sum_j \alpha_i \alpha_j y_i y_j \mathbf{x}_i^\top \mathbf{x}_j
$$

sujeito a $\alpha_i \geq 0$ e $\sum_i \alpha_i y_i = 0$.

### Exemplo: Otimização com Restrição

```python
import numpy as np
from scipy.optimize import minimize

# Minimizar f(x,y) = x^2 + y^2  sujeito a  x + y = 1
def f(x):
    return x[0]**2 + x[1]**2

def constraint_eq(x):
    return x[0] + x[1] - 1  # = 0

cons = {'type': 'eq', 'fun': constraint_eq}
result = minimize(f, x0=[2, 2], constraints=cons, method='SLSQP')
print(f"Solução: x = {result.x}")
print(f"f(x) = {result.fun}")

# Solução analítica: Lagrange multipliers
# L = x^2 + y^2 + lambda*(x + y - 1)
# dL/dx = 2x + lambda = 0 -> x = -lambda/2
# dL/dy = 2y + lambda = 0 -> y = -lambda/2
# x + y = 1 -> -lambda = 1 -> lambda = -1
# x = 0.5, y = 0.5
print(f"Solução analítica: x = 0.5, y = 0.5")
```

---

## Otimização de Segunda Ordem

### Método de Newton

Usa a expansão de Taylor de segunda ordem para encontrar o mínimo:

$$
\theta_{t+1} = \theta_t - \mathbf{H}_\mathcal{L}(\theta_t)^{-1} \nabla_\mathcal{L}(\theta_t)
$$

**Vantagens**:
- Convergência quadrática perto do ótimo
- Não requer ajuste de learning rate
- Invariante a transformações lineares dos parâmetros

**Desvantagens**:
- Computar a Hessiana é $O(n^2)$ em memória e $O(n^3)$ para inverter
- Hessiana pode não ser positiva definida longe do mínimo
- Inviável para redes com milhões de parâmetros

### BFGS e L-BFGS

BFGS (Broyden-Fletcher-Goldfarb-Shanno) é um método quasi-Newton que aproxima a Hessiana (ou sua inversa) iterativamente sem computá-la explicitamente:

$$
\mathbf{B}_{t+1} = \mathbf{B}_t + \frac{\mathbf{y}_t \mathbf{y}_t^\top}{\mathbf{y}_t^\top \mathbf{s}_t} - \frac{\mathbf{B}_t \mathbf{s}_t \mathbf{s}_t^\top \mathbf{B}_t^\top}{\mathbf{s}_t^\top \mathbf{B}_t \mathbf{s}_t}
$$

onde $\mathbf{s}_t = \theta_{t+1} - \theta_t$ e $\mathbf{y}_t = \nabla f(\theta_{t+1}) - \nabla f(\theta_t)$.

L-BFGS (Limited-memory BFGS) armazena apenas os últimos $m$ vetores $\mathbf{s}$ e $\mathbf{y}$, reduzindo a memória para $O(mn)$.

### Gauss-Newton

Para problemas de mínimos quadrados não-lineares:

$$
\min_\theta \sum_{i=1}^m r_i(\theta)^2 = \|\mathbf{r}(\theta)\|^2
$$

O método de Gauss-Newton aproxima a Hessiana como $\mathbf{J}_r^\top \mathbf{J}_r$, ignorando termos de segunda ordem:

$$
\theta_{t+1} = \theta_t - (\mathbf{J}_r^\top \mathbf{J}_r)^{-1} \mathbf{J}_r^\top \mathbf{r}(\theta_t)
$$

É a base do algoritmo Levenberg-Marquardt.

### Exemplo: Newton vs SGD

```python
import numpy as np
import matplotlib.pyplot as plt

# Função quadrática simples
def f(x):
    return x[0]**2 + 5*x[1]**2

def grad(x):
    return np.array([2*x[0], 10*x[1]])

def hess(x):
    return np.array([[2, 0], [0, 10]])

# SGD
x_sgd = np.array([3.0, 2.0])
path_sgd = [x_sgd.copy()]
lr = 0.1
for _ in range(30):
    x_sgd -= lr * grad(x_sgd)
    path_sgd.append(x_sgd.copy())

# Newton
x_newton = np.array([3.0, 2.0])
path_newton = [x_newton.copy()]
for _ in range(5):
    x_newton -= np.linalg.solve(hess(x_newton), grad(x_newton))
    path_newton.append(x_newton.copy())

path_sgd = np.array(path_sgd)
path_newton = np.array(path_newton)

# Plot
xs, ys = np.meshgrid(np.linspace(-3, 3, 50), np.linspace(-2, 2, 50))
Z = f([xs, ys])

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.contour(xs, ys, Z, levels=20)
plt.plot(path_sgd[:, 0], path_sgd[:, 1], 'r.-')
plt.title(f'SGD ({len(path_sgd)} iterações)')

plt.subplot(1, 2, 2)
plt.contour(xs, ys, Z, levels=20)
plt.plot(path_newton[:, 0], path_newton[:, 1], 'b.-')
plt.title(f'Newton ({len(path_newton)} iterações)')
plt.tight_layout()
plt.show()
```

---

## Diferenciação Automática (Autodiff)

### Diferenciação Simbólica vs Numérica vs Automática

- **Simbólica**: manipula expressões algébricas (exatas, mas pode explodir)
- **Numérica**: diferenças finitas $f'(x) \approx \frac{f(x+h) - f(x)}{h}$ (simples, mas instável)
- **Automática**: decompõe a função em operações elementares e aplica a regra da cadeia (exata e eficiente)

### Modo Forward (Forward Mode)

Computa a derivada junto com o valor da função, propagando uma "dual number" $(f(x), f'(x))$ através de cada operação.

Para uma operação $z = g(x, y)$:

$$
\dot{z} = \frac{\partial g}{\partial x} \dot{x} + \frac{\partial g}{\partial y} \dot{y}
$$

**Custo**: $O(n)$ para computar $n$ derivadas parciais.

### Modo Reverse (Reverse Mode) — Backpropagation

Computa o valor primeiro (forward pass), depois propaga gradientes de trás para frente (backward pass):

1. **Forward pass**: computa valores intermediários
2. **Backward pass**: computa $\bar{v}_i = \frac{\partial \mathcal{L}}{\partial v_i}$ usando a regra da cadeia reversa

**Custo**: $O(1)$ para gradiente de uma função escalar (comparado a $O(n)$ do forward mode).

Toda biblioteca moderna de deep learning (TensorFlow, PyTorch, JAX) implementa diferenciação automática em modo reverso.

### Exemplo: Diferenciação Automática Manual

```python
import numpy as np

def autodiff_manual(x):
    """
    f(x) = (sin(x) + 3) * exp(x^2)
    Computa f(x) e f'(x) via modo forward.
    """
    # Forward pass
    a = np.sin(x)       # a = sin(x)
    da = np.cos(x)      # da/dx = cos(x)
    
    b = a + 3           # b = a + 3
    db = da             # db/dx = da/dx
    
    c = x**2            # c = x^2
    dc = 2*x            # dc/dx = 2x
    
    d = np.exp(c)       # d = exp(c)
    dd = d * dc         # dd/dx = exp(c) * dc/dx
    
    y = b * d           # y = b * d
    dy = db * d + b * dd  # dy/dx = db/dx * d + b * dd/dx
    
    return y, dy

x = 1.0
y, dy = autodiff_manual(x)
print(f"f({x}) = {y:.4f}")
print(f"f'({x}) = {dy:.4f}")

# Verificação numérica
h = 1e-8
y_num = (np.sin(x+h) + 3) * np.exp((x+h)**2)
y_num2 = (np.sin(x-h) + 3) * np.exp((x-h)**2)
dy_num = (y_num - y_num2) / (2*h)
print(f"f'({x}) numérico = {dy_num:.4f}")
print(f"Erro: {abs(dy - dy_num):.2e}")
```

---

## Backpropagation — Derivação Completa

### Rede de 2 Camadas

Seja uma rede neural com:
- Entrada: $\mathbf{x} \in \mathbb{R}^d$
- Camada oculta: $\mathbf{z} = \mathbf{W}^{(1)}\mathbf{x} + \mathbf{b}^{(1)}$, $\mathbf{a} = \sigma(\mathbf{z})$
- Saída: $\hat{y} = \mathbf{w}^{(2)\top} \mathbf{a} + b^{(2)}$
- Perda MSE: $\mathcal{L} = \frac{1}{2}(y - \hat{y})^2$

### Forward Pass

1. $\mathbf{z} = \mathbf{W}^{(1)}\mathbf{x} + \mathbf{b}^{(1)}$
2. $\mathbf{a} = \sigma(\mathbf{z})$
3. $\hat{y} = \mathbf{w}^{(2)\top} \mathbf{a} + b^{(2)}$
4. $\mathcal{L} = \frac{1}{2}(y - \hat{y})^2$

### Backward Pass

Computamos gradientes da saída para a entrada:

**Camada de saída**:

$$
\frac{\partial \mathcal{L}}{\partial \hat{y}} = \hat{y} - y
$$

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{w}^{(2)}} = \frac{\partial \mathcal{L}}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial \mathbf{w}^{(2)}} = (\hat{y} - y) \cdot \mathbf{a}
$$

$$
\frac{\partial \mathcal{L}}{\partial b^{(2)}} = \hat{y} - y
$$

**Camada oculta**:

O erro propagado para a camada oculta:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{a}} = \frac{\partial \mathcal{L}}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial \mathbf{a}} = (\hat{y} - y) \cdot \mathbf{w}^{(2)}
$$

Usando a ativação sigmoide $\sigma'(z) = \sigma(z)(1 - \sigma(z))$:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{z}} = \frac{\partial \mathcal{L}}{\partial \mathbf{a}} \odot \sigma'(\mathbf{z})
$$

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(1)}} = \frac{\partial \mathcal{L}}{\partial \mathbf{z}} \cdot \mathbf{x}^\top
$$

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{b}^{(1)}} = \frac{\partial \mathcal{L}}{\partial \mathbf{z}}
$$

### Exemplo: Backpropagation Completo

```python
import numpy as np
import matplotlib.pyplot as plt

# Dados sintéticos: XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Parâmetros
d_in, d_hidden, d_out = 2, 4, 1
lr = 1.0

np.random.seed(42)
W1 = np.random.randn(d_in, d_hidden) * 0.5
b1 = np.zeros((1, d_hidden))
W2 = np.random.randn(d_hidden, d_out) * 0.5
b2 = np.zeros((1, d_out))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_grad(x):
    s = sigmoid(x)
    return s * (1 - s)

losses = []
for epoch in range(5000):
    # Forward
    z1 = X @ W1 + b1
    a1 = sigmoid(z1)
    z2 = a1 @ W2 + b2
    y_pred = sigmoid(z2)
    
    loss = np.mean((y - y_pred)**2)
    losses.append(loss)
    
    # Backward (saída)
    dy = (y_pred - y) * sigmoid_grad(z2)  # (4, 1)
    
    dW2 = a1.T @ dy  # (hidden, 1)
    db2 = np.sum(dy, axis=0, keepdims=True)
    
    # Backward (oculta)
    da1 = dy @ W2.T  # (4, hidden)
    dz1 = da1 * sigmoid_grad(z1)
    
    dW1 = X.T @ dz1
    db1 = np.sum(dz1, axis=0, keepdims=True)
    
    # Atualização
    W2 -= lr * dW2
    b2 -= lr * db2
    W1 -= lr * dW1
    b1 -= lr * db1

plt.plot(losses)
plt.xlabel('Época'); plt.ylabel('MSE')
plt.title('Treinamento via Backpropagation')
plt.yscale('log')
plt.grid()
plt.show()

# Teste
z1 = X @ W1 + b1
a1 = sigmoid(z1)
z2 = a1 @ W2 + b2
y_pred = sigmoid(z2)
print("Previsões XOR:")
print(np.round(y_pred, 3))
```

---

## Taxa de Aprendizado e Scheduling

### Learning Rate Schedules

**Step decay**: reduz a taxa por um fator $\gamma$ a cada $k$ épocas:

$$
\eta_t = \eta_0 \cdot \gamma^{\lfloor t/k \rfloor}
$$

**Exponential decay**: $\eta_t = \eta_0 \cdot e^{-kt}$

**Cosine annealing**: $\eta_t = \eta_{\min} + \frac{1}{2}(\eta_{\max} - \eta_{\min})(1 + \cos(\frac{t}{T}\pi))$

**Warmup**: aumenta linearmente de 0 a $\eta_{\max}$ nas primeiras $w$ iterações, depois decai.

### Taxa de Aprendizado Adaptativa

**AdaGrad**: acumula gradientes ao quadrado e adapta por parâmetro:

$$
\theta_{t+1, i} = \theta_{t, i} - \frac{\eta}{\sqrt{G_{t, ii} + \epsilon}} g_{t, i}
$$

**RMSProp**: usa média móvel dos gradientes ao quadrado:

$$
\mathbb{E}[g^2]_t = \beta \mathbb{E}[g^2]_{t-1} + (1 - \beta)g_t^2
$$
$$
\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{\mathbb{E}[g^2]_t + \epsilon}} g_t
$$

---

## Regularização e Otimização

### Weight Decay (Regularização L2)

Adiciona penalidade aos parâmetros:

$$
\tilde{\mathcal{L}}(\theta) = \mathcal{L}(\theta) + \frac{\lambda}{2} \|\theta\|^2
$$

O gradiente com weight decay torna-se:

$$
\nabla \tilde{\mathcal{L}} = \nabla \mathcal{L} + \lambda \theta
$$

Na prática, muitos otimizadores implementam weight decay de forma desacoplada do gradiente da perda (AdamW).

### Early Stopping

Monitora a perda de validação e interrompe o treinamento quando ela para de melhorar. Isto equivale a uma regularização implícita.

### Dropout

Durante o treinamento, neurônios são "dropados" (zerados) com probabilidade $p$. Isto força a rede a aprender representações redundantes e funciona como uma forma de ensemble (aproximadamente).

### Batch Normalization

Normaliza a saída de cada camada:

$$
\hat{\mathbf{z}} = \frac{\mathbf{z} - \mu_\mathcal{B}}{\sqrt{\sigma^2_\mathcal{B} + \epsilon}}
$$
$$
\mathbf{y} = \gamma \hat{\mathbf{z}} + \beta
$$

BatchNorm suaviza a paisagem de otimização, permitindo taxas de aprendizado maiores.

---

## Algoritmos de Otimização em ML

### Otimização de Hiperparâmetros

**Grid Search**: busca exaustiva sobre valores pré-definidos.
**Random Search**: amostra valores aleatórios — surpreendentemente mais eficiente que grid search (Bergstra & Bengio, 2012).
**Bayesian Optimization**: modela a função objetivo como um processo Gaussiano e usa aquisição para selecionar o próximo ponto.

### Exemplo: Otimização de Hiperparâmetros

```python
import numpy as np
from scipy.optimize import minimize

# Simulando uma função de validação cara
def validation_loss(learning_rate, hidden_size, weight_decay):
    """Função sintética que simula perda de validação"""
    return (learning_rate - 0.01)**2 * 100 + \
           (hidden_size - 128)**2 * 1e-4 + \
           (weight_decay - 0.001)**2 * 1e6 + \
           np.random.randn() * 0.01

# Random search
best_loss = float('inf')
best_params = None
for _ in range(100):
    lr = 10**np.random.uniform(-4, -1)   # log-uniform
    hs = int(2**np.random.uniform(5, 9))  # potências de 2
    wd = 10**np.random.uniform(-5, -2)    # log-uniform
    loss = validation_loss(lr, hs, wd)
    if loss < best_loss:
        best_loss = loss
        best_params = (lr, hs, wd)

print(f"Melhor: lr={best_params[0]:.4f}, "
      f"hs={best_params[1]}, wd={best_params[2]:.5f}, "
      f"loss={best_loss:.4f}")
```

---

## Otimização Convexa Avançada

### Dualidade

Para cada problema de otimização primal, existe um problema dual. A diferença entre o valor ótimo primal e dual é o **gap de dualidade**. Para problemas convexos com certas qualificações de restrição, o gap é zero (dualidade forte).

**Lagrangiano**: $\mathcal{L}(\mathbf{x}, \boldsymbol{\lambda}) = f(\mathbf{x}) + \sum_i \lambda_i g_i(\mathbf{x})$

**Função dual**: $g(\boldsymbol{\lambda}) = \inf_\mathbf{x} \mathcal{L}(\mathbf{x}, \boldsymbol{\lambda})$

**Problema dual**: $\max_{\boldsymbol{\lambda} \geq 0} g(\boldsymbol{\lambda})$

### Programação Quadrática (QP)

Minimizar função quadrática convexa sujeita a restrições lineares é um dos problemas mais importantes em ML:

$$
\min_{\mathbf{x}} \frac{1}{2} \mathbf{x}^\top \mathbf{Q} \mathbf{x} + \mathbf{c}^\top \mathbf{x}
$$
$$
\text{s.a. } \mathbf{A}\mathbf{x} \leq \mathbf{b}, \ \mathbf{A}_{\text{eq}}\mathbf{x} = \mathbf{b}_{\text{eq}}
$$

SVMs e regressão ridge são exemplos de problemas QP.

### Programação Semi-Definida (SDP)

Minimiza uma função linear sujeita a restrições de que uma combinação linear de matrizes seja positiva semidefinida. Usada em **kernel learning** e **dimensionality reduction**.

### Exemplo: Programação Quadrática

```python
import numpy as np
from scipy.optimize import minimize

# SVM via otimização: problema dual
X = np.array([[0, 0], [1, 1], [1, 0], [0, 1]])
y = np.array([-1, 1, 1, -1])

# Kernel linear: K(x_i, x_j) = x_i^T x_j
def kernel(xi, xj):
    return np.dot(xi, xj)

m = len(y)
# Função dual: max sum(alpha) - 0.5 * sum_i sum_j alpha_i alpha_j y_i y_j K(x_i, x_j)
def dual_objective(alpha):
    alpha = alpha.reshape(-1, 1)
    K_mat = np.array([[kernel(X[i], X[j]) for j in range(m)] for i in range(m)])
    quad = (y.reshape(-1, 1) * alpha).T @ K_mat @ (y.reshape(-1, 1) * alpha)
    return -(alpha.sum() - 0.5 * quad.item())  # negativa para minimizar

# Restrição: sum(alpha_i * y_i) = 0, alpha_i >= 0
cons = {'type': 'eq', 'fun': lambda a: np.dot(a, y)}
bounds = [(0, None) for _ in range(m)]

alpha0 = np.zeros(m)
result = minimize(dual_objective, alpha0, bounds=bounds, constraints=cons, method='SLSQP')
alpha = result.x

# Vetor de pesos: w = sum(alpha_i * y_i * x_i)
w = np.sum([alpha[i] * y[i] * X[i] for i in range(m)], axis=0)
print(f"Vetor de pesos: {w}")
print(f"Vetores de suporte (alpha > 1e-6): {np.where(alpha > 1e-6)[0]}")
```

---

## Aplicações em IA Moderna

### LLMs e Otimização em Larga Escala

O treinamento de Large Language Models (LLMs) como GPT-4, Llama e Claude envolve:

- **Otimizador**: AdamW (Adam + weight decay desacoplado)
- **Schedule**: cosine decay com warmup linear (tipicamente 2000 passos de warmup)
- **Batch size**: centenas de milhares a milhões de tokens
- **Paralelismo**: data parallelism, model parallelism, pipeline parallelism
- **Mixed precision**: FP16/BF16 para reduzir memória e acelerar
- **Gradient accumulation**: simular batches grandes com memória limitada
- **Gradient clipping**: limitar a norma do gradiente a $\tau$ (tipicamente 1.0)

### Loss Landscape e Generalização

Estudos modernos mostram que:
- A paisagem de perda (loss landscape) de redes profundas tem estrutura rica • Mínimos largos (flat minima) generalizam melhor que mínimos agudos (sharp minima) — conjectura apoiada por evidências experimentais (Keskar et al., 2016)
- Técnicas como **stochastic weight averaging (SWA)** encontram soluções mais planas
- O ruído intrínseco do SGD atua como regularizador implícito
- A **profundidade** da rede adiciona não-convexidade, mas também capacidade representacional

### Normalização da Taxa de Aprendizado (Learning Rate Scaling)

**Linear scaling rule**: quando o batch size é multiplicado por $k$, a learning rate pode ser multiplicada por $k$ (para SGD):

$$
\eta_k = k \cdot \eta_{\text{base}}
$$

**Square root scaling**: para Adam e métodos adaptativos, escalar por $\sqrt{k}$ é mais seguro.

---

## Referências

### Livros

1. **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — A bíblia da otimização convexa, disponível gratuitamente online.

2. **Nocedal, J. & Wright, S. J.** (2006). *Numerical Optimization*. 2nd ed. Springer. — Referência completa em otimização numérica, incluindo métodos quasi-Newton.

3. **Goodfellow, I., Bengio, Y. & Courville, A.** (2016). *Deep Learning*. MIT Press. — Capítulos 6-8 cobrem backpropagation e otimização para deep learning.

4. **Ruder, S.** (2016). "An overview of gradient descent optimization algorithms". *arXiv:1609.04747*. — Levantamento abrangente de otimizadores.

5. **Murphy, K. P.** (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press. — Cobre otimização no contexto de inferência probabilística.

### Artigos Clássicos

6. **Rumelhart, D. E., Hinton, G. E. & Williams, R. J.** (1986). "Learning representations by back-propagating errors". *Nature*, 323: 533-536. — O artigo seminal do backpropagation.

7. **Kingma, D. P. & Ba, J.** (2015). "Adam: A Method for Stochastic Optimization". *ICLR*. — O otimizador Adam.

8. **Loshchilov, I. & Hutter, F.** (2019). "Decoupled Weight Decay Regularization". *ICLR*. — AdamW.

9. **Sutskever, I. et al.** (2013). "On the importance of initialization and momentum in deep learning". *ICML*. — Momentum e inicialização.

10. **Pascanu, R., Mikolov, T. & Bengio, Y.** (2013). "On the difficulty of training recurrent neural networks". *ICML*. — Gradient clipping e vanishing gradients.

11. **Bergstra, J. & Bengio, Y.** (2012). "Random Search for Hyper-Parameter Optimization". *JMLR*, 13: 281-305. — Random search para otimização de hiperparâmetros.

### Recursos Online

12. **CS229 Lecture Notes**: "Gradient Descent" — Stanford, Andrew Ng.

13. **CS231n**: "Optimization Notes" — Stanford, Fei-Fei Li & Andrej Karpathy.

14. ** distill.pub ** — Artigos visualmente ricos sobre otimização e backpropagation.

15. **3Blue1Brown** (2017). "Backpropagation Calculus" — Série de vídeos com intuição geométrica do backpropagation.

16. **PyTorch Docs**: `torch.optim` — Documentação dos otimizadores implementados.

[[Conhecimento-Geral/Matematica/INDEX|← Voltar ao índice de Matemática]]
