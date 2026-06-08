---
title: "Álgebra Linear Essencial"
date: 2026-05-16
area: "Matemática para IA"
tags: [conhecimento, conceito, matematica, algebra-linear, vetores, matrizes, SVD, PCA]
related:
  [
    "04-Conhecimentos/07-Humanidades/Matematica/Calculo-e-Otimizacao",
    "04-Conhecimentos/07-Humanidades/Matematica/Teoria-da-Informacao",
    "04-Conhecimentos/07-Humanidades/Matematica/Probabilidade-e-Estatistica",
    "04-Conhecimentos/07-Humanidades/Neurociencia/Redes-Neurais-Biologicas",
  ]
aliases: ["Vetores e Matrizes", "Decomposição Espectral", "Autovalores", "SVD"]
---

# Álgebra Linear Essencial

## Visão Geral

A álgebra linear é a linguagem matemática fundamental do aprendizado de máquina, processamento de sinais, computação gráfica e inteligência artificial. Toda a arquitetura de redes neurais — desde a camada densa mais simples até o mecanismo de atenção de transformers — é expressa em operações vetoriais e matriciais. Sem álgebra linear, não existiriam embeddings, convoluções, PCA, SVD ou qualquer dos métodos centrais de IA moderna.

Este documento cobre desde os fundamentos de vetores e matrizes até tópicos avançados como decomposição em valores singulares (SVD), análise de componentes principais (PCA) e cálculo matricial, sempre conectando a teoria a aplicações práticas em inteligência artificial.

---

## Vetores

### Definição e Notação

Um vetor $\mathbf{v} \in \mathbb{R}^n$ é uma tupla ordenada de $n$ números reais:

$$
\mathbf{v} = \begin{bmatrix} v_1 & v_2 & \cdots & v_n \end{bmatrix}^\top
$$

Em aprendizado de máquina, vetores representam:
- **Embeddings de palavras**: $\mathbf{w} \in \mathbb{R}^{300}$ (GloVe, word2vec)
- **Features de observações**: $\mathbf{x} \in \mathbb{R}^d$ em uma matriz de design $X \in \mathbb{R}^{m \times d}$
- **Ativações de camadas ocultas**: $\mathbf{a}^{(\ell)} \in \mathbb{R}^{d_\ell}$
- **Gradientes**: $\nabla_\theta \mathcal{L} \in \mathbb{R}^p$

### Produto Interno (Dot Product)

O produto interno entre dois vetores $\mathbf{a}, \mathbf{b} \in \mathbb{R}^n$ é definido como:

$$
\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^n a_i b_i = \mathbf{a}^\top \mathbf{b}
$$

Interpretações fundamentais:

1. **Similaridade cosseno**: $\cos \theta = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}$ — usada em sistemas de recomendação e recuperação de informação.

2. **Projeção**: A projeção escalar de $\mathbf{a}$ sobre $\mathbf{b}$ é $\frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{b}\|}$.

3. **Atenção (Attention)**: No mecanismo de atenção escalada por produto interno (dot-product attention), a similaridade entre query $\mathbf{q}$ e key $\mathbf{k}$ é:

$$
\text{score}(\mathbf{q}, \mathbf{k}) = \mathbf{q}^\top \mathbf{k}
$$

### Norma

A norma Euclidiana ($\ell_2$) mede o comprimento de um vetor:

$$
\|\mathbf{v}\|_2 = \sqrt{\sum_{i=1}^n v_i^2} = \sqrt{\mathbf{v}^\top \mathbf{v}}
$$

Outras normas importantes:

- **Norma $\ell_1$**: $\|\mathbf{v}\|_1 = \sum_{i=1}^n |v_i|$ — usada em regularização Lasso (L1).
- **Norma $\ell_\infty$**: $\|\mathbf{v}\|_\infty = \max_i |v_i|$
- **Norma $\ell_p$**: $\|\mathbf{v}\|_p = \left(\sum_{i=1}^n |v_i|^p\right)^{1/p}$

### Independência Linear e Span

Um conjunto de vetores $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$ é **linearmente independente** se a única solução para:

$$
c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \cdots + c_k \mathbf{v}_k = \mathbf{0}
$$

é $c_1 = c_2 = \cdots = c_k = 0$.

O **span** de um conjunto de vetores é o subespaço de todas as combinações lineares possíveis. Se os vetores são linearmente independentes e seu span é $\mathbb{R}^n$, eles formam uma **base** de $\mathbb{R}^n$.

### Base e Dimensão

Uma base $\mathcal{B} = \{\mathbf{e}_1, \ldots, \mathbf{e}_n\}$ de $\mathbb{R}^n$ é um conjunto linearmente independente que gera todo o espaço. Qualquer vetor $\mathbf{v} \in \mathbb{R}^n$ pode ser escrito de forma única como combinação linear dos vetores da base.

A **base canônica** de $\mathbb{R}^n$ é $\{\mathbf{e}_1, \ldots, \mathbf{e}_n\}$ onde $\mathbf{e}_i$ tem 1 na posição $i$ e 0 nas demais.

Em processamento de linguagem natural, a escolha da base é crucial: a base de um embedding space pode não ser ortogonal, e técnicas como orthogonalization de representações (e.g., IPM, orthogonal projection) melhoram a qualidade dos embeddings.

### Ortogonalidade e Ortonormalidade

Vetores $\mathbf{a}$ e $\mathbf{b}$ são **ortogonais** se $\mathbf{a}^\top \mathbf{b} = 0$. Um conjunto ortonormal satisfaz:

$$
\mathbf{v}_i^\top \mathbf{v}_j = \delta_{ij} = \begin{cases} 1 & \text{se } i = j \\ 0 & \text{caso contrário} \end{cases}
$$

Matrizes com colunas ortonormais têm a propriedade $Q^\top Q = I$, fundamentais na decomposição QR e em SVD.

### Exemplo NumPy: Operações com Vetores

```python
import numpy as np

a = np.array([2.0, 3.0, 5.0])
b = np.array([1.0, 0.0, -1.0])

# Produto interno
dot = np.dot(a, b)

# Norma L2
norm_a = np.linalg.norm(a)

# Similaridade cosseno
cos_sim = dot / (norm_a * np.linalg.norm(b))

# Projeção de a sobre b
proj = (dot / np.dot(b, b)) * b

# Verificação de ortogonalidade
if np.abs(dot) < 1e-10:
    print("Vetores ortogonais")
```

---

## Matrizes

### Definição e Operações

Uma matriz $\mathbf{A} \in \mathbb{R}^{m \times n}$ é um arranjo retangular de números com $m$ linhas e $n$ colunas:

$$
\mathbf{A} = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
$$

**Operações básicas:**

1. **Adição**: $(\mathbf{A} + \mathbf{B})_{ij} = a_{ij} + b_{ij}$
2. **Multiplicação escalar**: $(c\mathbf{A})_{ij} = c \cdot a_{ij}$
3. **Transposição**: $(\mathbf{A}^\top)_{ij} = a_{ji}$
4. **Multiplicação matricial**: $(\mathbf{A}\mathbf{B})_{ij} = \sum_{k=1}^n a_{ik} b_{kj}$

A multiplicação de matrizes é a operação central em redes neurais. Uma camada densa (fully connected) com ativação $\sigma$ realiza:

$$
\mathbf{h} = \sigma(\mathbf{W}\mathbf{x} + \mathbf{b})
$$

onde $\mathbf{W} \in \mathbb{R}^{d_\text{out} \times d_\text{in}}$ é a matriz de pesos.

### Rank

O **rank** de uma matriz $\mathbf{A}$ é o número máximo de linhas (ou colunas) linearmente independentes. Propriedades:

- $\text{rank}(\mathbf{A}) \leq \min(m, n)$
- $\text{rank}(\mathbf{A}) = \text{rank}(\mathbf{A}^\top)$
- $\text{rank}(\mathbf{A}\mathbf{B}) \leq \min(\text{rank}(\mathbf{A}), \text{rank}(\mathbf{B}))$

Um posto baixo indica redundância — explorada em compressão de modelos (low-rank factorization) e em sistemas de recomendação (matrix completion).

### Inversa

Uma matriz quadrada $\mathbf{A} \in \mathbb{R}^{n \times n}$ é **invertível** se existe $\mathbf{A}^{-1}$ tal que:

$$
\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}_n
$$

Condições equivalentes para invertibilidade:
- $\det(\mathbf{A}) \neq 0$
- $\text{rank}(\mathbf{A}) = n$
- Todos os autovalores são não-nulos
- As colunas (ou linhas) são linearmente independentes

A inversa aparece na solução de mínimos quadrados: $\mathbf{w} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$.

### Determinante

O determinante $\det(\mathbf{A})$ é uma função escalar que mede o fator de escala volumétrica da transformação linear representada por $\mathbf{A}$.

Propriedades:
- $\det(\mathbf{A}\mathbf{B}) = \det(\mathbf{A})\det(\mathbf{B})$
- $\det(\mathbf{A}^\top) = \det(\mathbf{A})$
- $\det(c\mathbf{A}) = c^n\det(\mathbf{A})$ para $\mathbf{A} \in \mathbb{R}^{n \times n}$

Em aprendizado de máquina, o determinante aparece no cálculo de entropia diferencial de distribuições normais multivariadas e em normalizing flows.

### Traço

O traço $\text{tr}(\mathbf{A}) = \sum_{i=1}^n a_{ii}$ possui a propriedade cíclica:

$$
\text{tr}(\mathbf{A}\mathbf{B}\mathbf{C}) = \text{tr}(\mathbf{C}\mathbf{A}\mathbf{B}) = \text{tr}(\mathbf{B}\mathbf{C}\mathbf{A})
$$

O traço do produto de duas matrizes define o produto interno de Frobenius.

### Norma de Frobenius

A norma de Frobenius de uma matriz é a norma $\ell_2$ do vetor achatado:

$$
\|\mathbf{A}\|_F = \sqrt{\sum_{i=1}^m \sum_{j=1}^n a_{ij}^2} = \sqrt{\text{tr}(\mathbf{A}^\top\mathbf{A})}
$$

### Matrizes Especiais

- **Simétrica**: $\mathbf{A} = \mathbf{A}^\top$ (autovalores reais, diagonalizável por base ortogonal)
- **Ortogonal**: $\mathbf{Q}^\top\mathbf{Q} = \mathbf{Q}\mathbf{Q}^\top = \mathbf{I}$ (preserva normas)
- **Positiva-definida**: $\mathbf{x}^\top\mathbf{A}\mathbf{x} > 0$ para todo $\mathbf{x} \neq \mathbf{0}$ (autovalores positivos)
- **Diagonal**: $a_{ij} = 0$ para $i \neq j$ (operações eficientes)
- **Estocástica**: colunas somam a 1 (usada em PageRank e cadeias de Markov)

### Exemplo NumPy: Operações Matriciais

```python
import numpy as np

# Criação
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Multiplicação
C = A @ B

# Transposição
A_T = A.T

# Inversa
A_inv = np.linalg.inv(A)

# Determinante
det_A = np.linalg.det(A)

# Rank
rank_A = np.linalg.matrix_rank(A)

# Norma de Frobenius
frob_norm = np.linalg.norm(A, 'fro')

# Autovalores e autovetores
eigvals, eigvecs = np.linalg.eig(A)

# Produto de Kronecker (usado em GPUs e paralelização)
K = np.kron(A, B)
```

---

## Transformações Lineares

### Definição

Uma transformação $T: \mathbb{R}^n \to \mathbb{R}^m$ é **linear** se:

1. $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ (aditividade)
2. $T(c\mathbf{u}) = c\,T(\mathbf{u})$ (homogeneidade)

Toda transformação linear pode ser representada por uma matriz $\mathbf{A} \in \mathbb{R}^{m \times n}$ tal que $T(\mathbf{v}) = \mathbf{A}\mathbf{v}$.

### Composição e Inversão

A composição de transformações corresponde à multiplicação de matrizes:

$$
(T_2 \circ T_1)(\mathbf{v}) = \mathbf{A}_2(\mathbf{A}_1\mathbf{v}) = (\mathbf{A}_2\mathbf{A}_1)\mathbf{v}
$$

### Núcleo e Imagem

- **Núcleo (kernel)**: $\ker(T) = \{\mathbf{v} \in \mathbb{R}^n : T(\mathbf{v}) = \mathbf{0}\}$
- **Imagem**: $\text{Im}(T) = \{T(\mathbf{v}) : \mathbf{v} \in \mathbb{R}^n\}$

Teorema do Núcleo e da Imagem (rank-nullity):

$$
\dim(\ker(T)) + \dim(\text{Im}(T)) = n
$$

Em redes neurais, as camadas sucessivas aplicam transformações lineares seguidas de não-linearidades. A composição de transformações lineares sem ativações não-lineares seria simplesmente uma única transformação linear.

### Mudança de Base

Se $\mathbf{v}$ é representado na base $\mathcal{B}$ como $[\mathbf{v}]_\mathcal{B}$, e queremos representá-lo na base $\mathcal{C}$, a matriz de mudança de base $\mathbf{P}_{\mathcal{C} \leftarrow \mathcal{B}}$ satisfaz:

$$
[\mathbf{v}]_\mathcal{C} = \mathbf{P}_{\mathcal{C} \leftarrow \mathcal{B}} [\mathbf{v}]_\mathcal{B}
$$

Em processamento de linguagem natural, mudanças de base correspondem a transformar embeddings de um espaço semântico para outro.

### Exemplo: Transformações em Imagens

```python
import numpy as np
import matplotlib.pyplot as plt

# Pontos de um quadrado unitário
points = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]).T

# Matriz de rotação (45 graus)
theta = np.pi / 4
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])

# Matriz de cisalhamento (shear)
S = np.array([[1, 0.5], [0, 1]])

# Aplicar transformações
rotated = R @ points
sheared = S @ points

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(points[0], points[1], 'b-', label='Original')
plt.plot(rotated[0], rotated[1], 'r-', label='Rotacionado')
plt.axis('equal'); plt.legend(); plt.title('Rotação')

plt.subplot(1, 2, 2)
plt.plot(points[0], points[1], 'b-', label='Original')
plt.plot(sheared[0], sheared[1], 'g-', label='Shear')
plt.axis('equal'); plt.legend(); plt.title('Cisalhamento')
plt.show()
```

---

## Autovalores e Autovetores

### Definição e Derivação

Para uma matriz quadrada $\mathbf{A} \in \mathbb{R}^{n \times n}$, um **autovetor** $\mathbf{v} \neq \mathbf{0}$ e seu **autovalor** associado $\lambda$ satisfazem:

$$
\mathbf{A}\mathbf{v} = \lambda \mathbf{v}
$$

Intuitivamente, $\mathbf{v}$ é uma direção que, quando transformada por $\mathbf{A}$, mantém sua direção (apenas é escalada por $\lambda$).

**Derivação**:

Reescrevendo:

$$
\mathbf{A}\mathbf{v} - \lambda \mathbf{v} = \mathbf{0} \implies (\mathbf{A} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0}
$$

Para que exista $\mathbf{v} \neq \mathbf{0}$ solução, a matriz $\mathbf{A} - \lambda\mathbf{I}$ deve ser singular:

$$
\det(\mathbf{A} - \lambda\mathbf{I}) = 0
$$

Esta é a **equação característica**, um polinômio de grau $n$ em $\lambda$ cujas raízes são os autovalores.

### Interpretação Geométrica

- **Autovalor positivo**: expansão na direção do autovetor
- **Autovalor negativo**: reversão de direção + expansão
- **Autovalor zero**: a direção é mapeada ao núcleo (informação perdida)
- **Autovalor complexo**: rotação no plano correspondente

### Propriedades

- $\text{tr}(\mathbf{A}) = \sum_{i=1}^n \lambda_i$
- $\det(\mathbf{A}) = \prod_{i=1}^n \lambda_i$
- $\text{rank}(\mathbf{A})$ = número de autovalores não-nulos
- Se $\mathbf{A}$ é simétrica, todos os autovalores são reais e os autovetores são ortogonais.

### Decomposição Espectral

Para matrizes simétricas reais, a decomposição espectral é:

$$
\mathbf{A} = \mathbf{Q}\mathbf{\Lambda}\mathbf{Q}^\top = \sum_{i=1}^n \lambda_i \mathbf{q}_i \mathbf{q}_i^\top
$$

onde $\mathbf{Q}$ é ortogonal (colunas = autovetores) e $\mathbf{\Lambda} = \text{diag}(\lambda_1, \ldots, \lambda_n)$.

### Aplicação: PageRank

O PageRank do Google resolve o problema de autovetor dominante:

$$
\mathbf{r} = d\mathbf{M}\mathbf{r} + \frac{1-d}{n}\mathbf{1}
$$

onde $\mathbf{r}$ é o vetor de relevância (PageRank), $\mathbf{M}$ é a matriz de transição e $d$ é o fator de amortecimento (tipicamente 0.85). A solução $\mathbf{r}$ é o autovetor associado ao autovalor dominante de uma matriz modificada.

### Exemplo: Autovalores e Autovetores em NumPy

```python
import numpy as np
import matplotlib.pyplot as plt

# Matriz simétrica (garante autovalores reais)
A = np.array([[3, 1], [1, 2]])
eigvals, eigvecs = np.linalg.eigh(A)

print(f"Autovalores: {eigvals}")
print(f"Autovetores:\n{eigvecs}")

# Verificação
v = eigvecs[:, 0]
lmbda = eigvals[0]
print(f"A v = {A @ v}")
print(f"lambda v = {lmbda * v}")

# Visualização: transformação de um círculo
theta = np.linspace(0, 2*np.pi, 100)
circle = np.array([np.cos(theta), np.sin(theta)])
transformed = A @ circle

plt.figure(figsize=(6, 6))
plt.plot(circle[0], circle[1], 'b--', label='Círculo unitário')
plt.plot(transformed[0], transformed[1], 'r-', label='Transformado')

# Direções dos autovetores
for i in range(2):
    v = eigvecs[:, i] * eigvals[i]
    plt.arrow(0, 0, v[0], v[1], head_width=0.2, 
              color='g' if i == 0 else 'm')

plt.axis('equal'); plt.legend(); plt.grid()
plt.title('Efeito da Matriz nos Autovetores')
plt.show()
```

---

## Decomposição em Valores Singulares (SVD)

### Teorema

Toda matriz $\mathbf{A} \in \mathbb{R}^{m \times n}$ pode ser decomposta como:

$$
\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^\top
$$

onde:
- $\mathbf{U} \in \mathbb{R}^{m \times m}$: matriz ortogonal de **vetores singulares à esquerda**
- $\mathbf{\Sigma} \in \mathbb{R}^{m \times n}$: matriz diagonal com **valores singulares** $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_k \geq 0$
- $\mathbf{V} \in \mathbb{R}^{n \times n}$: matriz ortogonal de **vetores singulares à direita**

### Relação com Autodecomposição

Os vetores singulares e valores singulares relacionam-se com as autodecomposições de $\mathbf{A}^\top\mathbf{A}$ e $\mathbf{A}\mathbf{A}^\top$:

- $\mathbf{A}^\top\mathbf{A} = \mathbf{V}\mathbf{\Sigma}^\top\mathbf{\Sigma}\mathbf{V}^\top$ (autovetores = $\mathbf{V}$, autovalores = $\sigma_i^2$)
- $\mathbf{A}\mathbf{A}^\top = \mathbf{U}\mathbf{\Sigma}\mathbf{\Sigma}^\top\mathbf{U}^\top$ (autovetores = $\mathbf{U}$, autovalores = $\sigma_i^2$)

### SVD Reduzido (Truncado)

Na prática computacional, usa-se a SVD truncada:

$$
\mathbf{A} \approx \mathbf{U}_k \mathbf{\Sigma}_k \mathbf{V}_k^\top
$$

onde apenas os $k$ maiores valores singulares são retidos. Isto dá a melhor aproximação de posto $k$ no sentido da norma de Frobenius (Teorema de Eckart-Young).

### Aplicações da SVD

1. **Compressão de imagens**: reter apenas os $k$ maiores $\sigma_i$ reduz drasticamente o armazenamento.

2. **Sistemas de recomendação**: SVD na matriz usuário-item (Netflix Prize, FunkSVD) preenche entradas faltantes e captura fatores latentes.

3. **Processamento de linguagem natural**: SVD sobre matrizes de co-ocorrência (GloVe) produz embeddings densos.

4. **Pseudoinversa**: $\mathbf{A}^+ = \mathbf{V}\mathbf{\Sigma}^+\mathbf{U}^\top$ — solução de mínimos quadrados mesmo para matrizes singulares.

5. **Decomposição de peso de redes neurais**: SVD de camadas completamente conectadas permite substituir uma camada grande por duas menores (compressão de modelo).

### Exemplo: SVD para Compressão de Imagens

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

# Carregar imagem (em escala de cinza)
img = plt.imread('caminho/para/imagem.png')
if img.ndim == 3:
    img = np.mean(img, axis=2)  # converter para cinza

# SVD
U, S, Vt = np.linalg.svd(img, full_matrices=False)

# Reconstruções com k componentes
ks = [5, 20, 50, 100, 200]
plt.figure(figsize=(15, 4))

for i, k in enumerate(ks):
    reconstruction = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
    plt.subplot(1, len(ks), i+1)
    plt.imshow(reconstruction, cmap='gray')
    plt.title(f'k = {k}')
    plt.axis('off')

plt.tight_layout()
plt.show()

# Razão de compressão
original = img.shape[0] * img.shape[1]
compressed = img.shape[0]*k + k + k*img.shape[1]
print(f"Original: {original} -> Compressed (k={k}): {compressed}")
print(f"Taxa: {compressed/original:.2%}")
```

---

## PCA — Análise de Componentes Principais

### Derivação a partir do SVD

PCA encontra as direções de máxima variância nos dados. Seja $\mathbf{X} \in \mathbb{R}^{m \times n}$ a matriz de dados centralizada (cada coluna tem média zero).

**Abordagem 1: Maximização da variância**

Queremos encontrar $\mathbf{w}_1$ com $\|\mathbf{w}_1\| = 1$ que maximize $\text{Var}(\mathbf{X}\mathbf{w}_1) = \mathbf{w}_1^\top \mathbf{X}^\top\mathbf{X}\mathbf{w}_1$. Este é o autovetor dominante de $\mathbf{X}^\top\mathbf{X}$, ou equivalentemente, o primeiro vetor singular direito de $\mathbf{X}$.

**Abordagem 2: Minimização do erro de reconstrução**

PCA também pode ser derivado como a projeção que minimiza o erro de reconstrução quadrático médio.

**Algoritmo PCA via SVD**:

1. Centralizar os dados: $\tilde{\mathbf{X}} = \mathbf{X} - \boldsymbol{\mu}$
2. Computar SVD: $\tilde{\mathbf{X}} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^\top$
3. Componentes principais: $\mathbf{Z} = \tilde{\mathbf{X}}\mathbf{V}_k = \mathbf{U}_k\mathbf{\Sigma}_k$
4. Projeção: os PCs são $\mathbf{V}_k$

### Variância Explicada

A proporção de variância explicada pelos $k$ primeiros componentes é:

$$
\frac{\sum_{i=1}^k \sigma_i^2}{\sum_{i=1}^n \sigma_i^2}
$$

### Aplicações

1. **Redução de dimensionalidade**: projetar dados de alta dimensão em 2D/3D para visualização.
2. **Pré-processamento**: remover ruído descartando componentes de baixa variância.
3. **Whitening**: PCA whitening transforma dados para ter covariância identidade.

### Exemplo: PCA em NumPy

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

# Dados: dígitos manuscritos (8x8 pixels -> 64 dimensões)
digits = load_digits()
X = digits.data  # (1797, 64)
y = digits.target

# Centralizar
X_centered = X - np.mean(X, axis=0)

# SVD
U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)

# Projetar em 2D
X_pca = X_centered @ Vt[:2, :].T

# Variância explicada
var_explained = (S**2) / np.sum(S**2)
cumulative = np.cumsum(var_explained)

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='tab10', alpha=0.7)
plt.colorbar(scatter)
plt.xlabel('PC1'); plt.ylabel('PC2')
plt.title('PCA dos Dígitos')

plt.subplot(1, 2, 2)
plt.bar(range(1, 11), var_explained[:10], alpha=0.6, label='Individual')
plt.plot(range(1, 11), cumulative[:10], 'r-o', label='Cumulativa')
plt.xlabel('Componente'); plt.ylabel('Variância Explicada')
plt.legend(); plt.title('Variância Explicada')
plt.tight_layout()
plt.show()
```

---

## Cálculo Matricial

### Gradientes Vetoriais

Seja $f: \mathbb{R}^n \to \mathbb{R}$ uma função escalar de um vetor $\mathbf{x}$. O gradiente é:

$$
\nabla_{\mathbf{x}} f = \begin{bmatrix} \frac{\partial f}{\partial x_1} & \frac{\partial f}{\partial x_2} & \cdots & \frac{\partial f}{\partial x_n} \end{bmatrix}^\top
$$

**Identidades importantes:**

1. $\nabla_{\mathbf{x}} (\mathbf{a}^\top \mathbf{x}) = \mathbf{a}$
2. $\nabla_{\mathbf{x}} (\mathbf{x}^\top \mathbf{A} \mathbf{x}) = (\mathbf{A} + \mathbf{A}^\top)\mathbf{x}$
3. $\nabla_{\mathbf{x}} \|\mathbf{A}\mathbf{x} - \mathbf{b}\|^2 = 2\mathbf{A}^\top(\mathbf{A}\mathbf{x} - \mathbf{b})$

### Jacobiana

Para $f: \mathbb{R}^n \to \mathbb{R}^m$, a matriz Jacobiana $\mathbf{J}_f \in \mathbb{R}^{m \times n}$ tem entradas:

$$
(\mathbf{J}_f)_{ij} = \frac{\partial f_i}{\partial x_j}
$$

A Jacobiana da transformação de uma camada de rede neural $\mathbf{h} = \mathbf{W}\mathbf{x} + \mathbf{b}$ é $\mathbf{W}$.

### Hessiana

Para $f: \mathbb{R}^n \to \mathbb{R}$, a matriz Hessiana $\mathbf{H}_f \in \mathbb{R}^{n \times n}$ contém as segundas derivadas:

$$
(\mathbf{H}_f)_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}
$$

A Hessiana determina a curvatura local da função de perda e é usada em métodos de otimização de segunda ordem (Newton, quasi-Newton).

### Gradientes em Redes Neurais

A retropropagação (backpropagation) calcula gradientes de forma eficiente usando a regra da cadeia:

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(\ell)}} = 
\frac{\partial \mathcal{L}}{\partial \mathbf{h}^{(L)}} \cdot
\frac{\partial \mathbf{h}^{(L)}}{\partial \mathbf{h}^{(L-1)}} \cdots
\frac{\partial \mathbf{h}^{(\ell+1)}}{\partial \mathbf{h}^{(\ell)}} \cdot
\frac{\partial \mathbf{h}^{(\ell)}}{\partial \mathbf{W}^{(\ell)}}
$$

Na prática, cada termo $\frac{\partial \mathbf{h}^{(k+1)}}{\partial \mathbf{h}^{(k)}}$ é uma matriz Jacobiana que propaga o erro para trás.

### Exemplo: Cálculo de Gradiente Manual

```python
import numpy as np

# Função: f(x) = x^T A x + b^T x + c
A = np.array([[2, 1], [1, 3]])
b = np.array([1, 2])
c = 0.5

def f(x):
    return x.T @ A @ x + b.T @ x + c

def grad_f(x):
    return (A + A.T) @ x + b

def hessian_f(x):
    return A + A.T  # constante (quadrática)

x0 = np.array([1.0, 1.0])
print(f"f(x0) = {f(x0)}")
print(f"∇f(x0) = {grad_f(x0)}")
print(f"Hf(x0) = \n{hessian_f(x0)}")
```

---

## Aplicações em Machine Learning e IA

### Embeddings de Palavras (GloVe)

O GloVe (Global Vectors for Word Representation) constrói embeddings fatorando a matriz de co-ocorrência $\mathbf{M}$, onde $M_{ij}$ é o número de vezes que a palavra $i$ aparece no contexto da palavra $j$. A decomposição é:

$$
\log M_{ij} = \mathbf{w}_i^\top \tilde{\mathbf{w}}_j + b_i + \tilde{b}_j
$$

O objetivo é encontrar $\mathbf{W}, \tilde{\mathbf{W}}$ que minimizam:

$$
\mathcal{L} = \sum_{i,j} f(M_{ij}) (\mathbf{w}_i^\top \tilde{\mathbf{w}}_j + b_i + \tilde{b}_j - \log M_{ij})^2
$$

Este é essencialmente um problema de fatoração de matrizes com ponderação, intimamente relacionado à SVD.

### Mecanismo de Atenção (Attention)

A atenção escalada por produto interno (dot-product attention) no paper "Attention Is All You Need" (Vaswani et al., 2017) usa álgebra linear:

$$
\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}}\right)\mathbf{V}
$$

onde $\mathbf{Q}, \mathbf{K}, \mathbf{V} \in \mathbb{R}^{n \times d_k}$ são as matrizes de queries, keys e values.

A multiplicação $\mathbf{Q}\mathbf{K}^\top$ calcula todas as similaridades entre pares de tokens. O softmax normaliza as linhas. A multiplicação por $\mathbf{V}$ combina os values ponderados pela atenção.

Em transformers de múltiplas cabeças (multi-head attention), múltiplas transformações lineares paralelas capturam diferentes aspectos das relações entre tokens:

$$
\text{MultiHead}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{Concat}(\text{head}_1, \ldots, \text{head}_h)\mathbf{W}^O
$$

onde $\text{head}_i = \text{Attention}(\mathbf{Q}\mathbf{W}_i^Q, \mathbf{K}\mathbf{W}_i^K, \mathbf{V}\mathbf{W}_i^V)$.

### Exemplo: Atenção Simples

```python
import numpy as np

def scaled_dot_product_attention(Q, K, V):
    """
    Q, K, V: (n_seq, d_k)
    Retorna: (n_seq, d_v)
    """
    d_k = K.shape[-1]
    scores = Q @ K.T / np.sqrt(d_k)  # (n_seq, n_seq)
    weights = np.exp(scores) / np.sum(np.exp(scores), axis=-1, keepdims=True)
    return weights @ V  # (n_seq, d_v)

# Exemplo: 4 tokens, dimensão 8
n_seq, d_k, d_v = 4, 8, 8
Q = np.random.randn(n_seq, d_k)
K = np.random.randn(n_seq, d_k)
V = np.random.randn(n_seq, d_v)

output = scaled_dot_product_attention(Q, K, V)
print(f"Output shape: {output.shape}")

# Matriz de atenção
d_k = K.shape[-1]
scores = Q @ K.T / np.sqrt(d_k)
weights = np.exp(scores) / np.sum(np.exp(scores), axis=-1, keepdims=True)
print("Matriz de pesos de atenção:")
print(np.round(weights, 3))
```

### Fatoração de Matrizes em Sistemas de Recomendação

Sistemas de recomendação como o do Netflix Prize usam fatoração de matrizes:

$$
\mathbf{R} \approx \mathbf{P}\mathbf{Q}^\top
$$

onde $\mathbf{R} \in \mathbb{R}^{m \times n}$ é a matriz usuário-item (parcialmente observada), $\mathbf{P} \in \mathbb{R}^{m \times k}$ contém os fatores latentes dos usuários, e $\mathbf{Q} \in \mathbb{R}^{n \times k}$ contém os fatores latentes dos itens.

A otimização tipicamente minimiza o erro quadrático sobre as entradas observadas com regularização:

$$
\min_{\mathbf{P}, \mathbf{Q}} \sum_{(i,j) \in \Omega} (r_{ij} - \mathbf{p}_i^\top \mathbf{q}_j)^2 + \lambda(\|\mathbf{P}\|_F^2 + \|\mathbf{Q}\|_F^2)
$$

### Decomposição de Pesos para Compressão

Uma camada totalmente conectada $\mathbf{y} = \mathbf{W}\mathbf{x}$ com $\mathbf{W} \in \mathbb{R}^{m \times n}$ pode ser decomposta via SVD:

$$
\mathbf{W} = \mathbf{U}_k \mathbf{\Sigma}_k \mathbf{V}_k^\top
$$

Substituindo por duas camadas:
1. $\mathbf{z} = \mathbf{V}_k^\top \mathbf{x}$ (redução de $n$ para $k$)
2. $\mathbf{y} = \mathbf{U}_k \mathbf{\Sigma}_k \mathbf{z}$ (expansão de $k$ para $m$)

Se $k \ll \min(m, n)$, o número de parâmetros cai de $mn$ para $k(m + n)$, uma economia significativa.

### Representações de Grupos e Simetrias

A álgebra linear também fundamenta a teoria de representações de grupos, usada em redes neurais equivariantes (GCNs, redes de grupo). A simetria de uma permutação, rotação ou translação pode ser representada como uma ação de grupo em espaços vetoriais.

---

## Decomposições Matriciais Avançadas

### Decomposição LU

$$
\mathbf{A} = \mathbf{L}\mathbf{U}
$$

onde $\mathbf{L}$ é triangular inferior e $\mathbf{U}$ é triangular superior. Usada para resolver sistemas lineares com complexidade $O(n^3)$ no pior caso.

### Decomposição de Cholesky

Para matrizes simétricas positivas-definidas:

$$
\mathbf{A} = \mathbf{L}\mathbf{L}^\top
$$

onde $\mathbf{L}$ é triangular inferior. Mais eficiente que LU ($O(n^3/3)$). Usada em amostragem de Gaussianas multivariadas e em otimização (Gauss-Newton).

### Decomposição QR

$$
\mathbf{A} = \mathbf{Q}\mathbf{R}
$$

onde $\mathbf{Q}$ é ortogonal e $\mathbf{R}$ é triangular superior. Mais estável numericamente que LU para resolver sistemas lineares.

### Exemplo: Decomposições em NumPy

```python
import numpy as np

A = np.array([[2, 1, 1], [4, 3, 3], [8, 7, 9]])

# LU
P, L, U = scipy.linalg.lu(A)
print(f"L:\n{L}\nU:\n{U}")

# Cholesky (matriz positiva definida)
A_pd = np.array([[4, 2], [2, 3]])
L = np.linalg.cholesky(A_pd)
print(f"Cholesky: \n{L}\n{L @ L.T}")

# QR
Q, R = np.linalg.qr(A)
print(f"Q:\n{Q}\nR:\n{R}")
```

---

## Exemplo Integrado: Regressão Linear via Álgebra Linear

A regressão linear resolve $\mathbf{X}\mathbf{w} \approx \mathbf{y}$ no sentido dos mínimos quadrados.

**Solução de equações normais**:

$$
\mathbf{w} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}
$$

**Solução via SVD**:

$$
\mathbf{w} = \mathbf{V}\mathbf{\Sigma}^+\mathbf{U}^\top\mathbf{y}
$$

A solução via SVD é numericamente mais estável, especialmente quando $\mathbf{X}^\top\mathbf{X}$ é mal-condicionada.

```python
import numpy as np

# Gerar dados sintéticos
np.random.seed(42)
n, p = 100, 5
X = np.random.randn(n, p)
w_true = np.array([1.5, -2.0, 0.5, 3.0, -1.0])
y = X @ w_true + 0.1 * np.random.randn(n)

# Solução via equações normais
w_ols = np.linalg.inv(X.T @ X) @ X.T @ y

# Solução via SVD
U, S, Vt = np.linalg.svd(X, full_matrices=False)
S_inv = np.diag(1.0 / S)
w_svd = Vt.T @ S_inv @ U.T @ y

# Solução via NumPy (LAPACK)
w_lstsq, *_ = np.linalg.lstsq(X, y, rcond=None)

print(f"Verdadeiro:    {w_true}")
print(f"Equações normais: {w_ols.round(4)}")
print(f"SVD:           {w_svd.round(4)}")
print(f"NumPy lstsq:   {w_lstsq.round(4)}")

# Número de condição
cond_number = np.linalg.cond(X.T @ X)
print(f"Número de condição: {cond_number:.2f}")
```

---

## Referências

### Livros

1. **Strang, G.** (2016). *Introduction to Linear Algebra*. 5th ed. Wellesley-Cambridge Press. — O clássico moderno, com ênfase em aplicações e SVD.

2. **Trefethen, L. N. & Bau III, D.** (1997). *Numerical Linear Algebra*. SIAM. — Referência definitiva em álgebra linear numérica e SVD.

3. **Boyd, S. & Vandenberghe, L.** (2018). *Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares*. Cambridge University Press. — Foco em aplicações de engenharia e ML.

4. **Goodfellow, I., Bengio, Y. & Courville, A.** (2016). *Deep Learning*. MIT Press. — Capítulos 2-5 cobrem álgebra linear, probabilidade e cálculo para deep learning.

5. **Murphy, K. P.** (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press. — Cobre álgebra linear no contexto de modelos probabilísticos.

### Artigos Clássicos

6. **Eckart, C. & Young, G.** (1936). "The approximation of one matrix by another of lower rank". *Psychometrika*, 1(3): 211-218. — Teorema fundamental da aproximação de posto baixo.

7. **Penrose, R.** (1955). "A generalized inverse for matrices". *Mathematical Proceedings of the Cambridge Philosophical Society*, 51(3): 406-413. — A pseudoinversa.

8. **Vaswani, A. et al.** (2017). "Attention Is All You Need". *NeurIPS*. — Mecanismo de atenção baseado em produto interno.

9. **Pennington, J., Socher, R. & Manning, C.** (2014). "GloVe: Global Vectors for Word Representation". *EMNLP*. — Embeddings via fatoração de matriz de co-ocorrência.

10. **Jolliffe, I. T.** (2002). *Principal Component Analysis*. 2nd ed. Springer. — Referência completa sobre PCA.

### Recursos Online

11. MIT OpenCourseWare: *Linear Algebra* (Gilbert Strang) — [https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)

12. **3Blue1Brown** (2016). "Essence of Linear Algebra" — Série de vídeos que oferece intuição geométrica profunda sobre todos os conceitos centrais.

13. **Stanford CS229**: Linear Algebra Review and Reference — Notas técnicas de revisão de álgebra linear para aprendizado de máquina.

[[04-Conhecimentos/07-Humanidades/Matematica/INDEX|← Voltar ao índice de Matemática]]
