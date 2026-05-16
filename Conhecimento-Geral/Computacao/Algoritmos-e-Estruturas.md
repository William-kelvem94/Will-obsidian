---
title: "Algoritmos e Estruturas de Dados"
date: 2026-05-16
area: "Computação e Programação"
tags: [computacao, algoritmos, estruturas-de-dados, python, programacao, grafos, dp, sorting]
aliases: ["Algorithms and Data Structures", "Estruturas de Dados e Algoritmos"]
---

# Algoritmos e Estruturas de Dados

> *"Algorithms + Data Structures = Programs"* — Niklaus Wirth (1976)

---

## 1. Análise Assintótica

### 1.1 Notação Big O

A **notação Big O** descreve o limite superior do crescimento de uma função:

$$O(g(n)) = \{f(n) \mid \exists c, n_0 > 0 \text{ tal que } 0 \leq f(n) \leq c \cdot g(n) \ \forall n \geq n_0\}$$

**Big Omega** ($\Omega$): limite inferior. **Big Theta** ($\Theta$): limite apertado.

| Classe | Nome | Exemplo |
|--------|------|---------|
| $O(1)$ | Constante | Acesso a array por índice |
| $O(\log n)$ | Logarítmico | Busca binária |
| $O(n)$ | Linear | Busca sequencial |
| $O(n \log n)$ | Linearítmico | Merge sort, quick sort (médio) |
| $O(n^2)$ | Quadrático | Bubble sort, insertion sort |
| $O(2^n)$ | Exponencial | Subset sum (força bruta) |
| $O(n!)$ | Fatorial | Permutações (TSP força bruta) |

```python
def constante(n):
    return n * (n + 1) // 2  # fórmula fechada — O(1)

def linear(n):
    total = 0
    for i in range(n):
        total += i  # O(n)
    return total

def quadratico(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i + j  # O(n^2)
    return total
```

### 1.2 Master Theorem

Para recorrências da forma $T(n) = aT(n/b) + f(n)$:

1. Se $f(n) = O(n^{\log_b a - \epsilon})$, então $T(n) = \Theta(n^{\log_b a})$
2. Se $f(n) = \Theta(n^{\log_b a})$, então $T(n) = \Theta(n^{\log_b a} \log n)$
3. Se $f(n) = \Omega(n^{\log_b a + \epsilon})$ e $af(n/b) \leq cf(n)$, então $T(n) = \Theta(f(n))$

**Exemplos**:
- Merge sort: $T(n) = 2T(n/2) + O(n)$ → $T(n) = \Theta(n \log n)$ (caso 2)
- Busca binária: $T(n) = T(n/2) + O(1)$ → $T(n) = O(\log n)$ (caso 2)
- Strassen: $T(n) = 7T(n/2) + O(n^2)$ → $T(n) = \Theta(n^{\log_2 7}) \approx O(n^{2.81})$ (caso 1)

---

## 2. Estruturas de Dados Lineares

### 2.1 Arrays (Listas em Python)

```python
arr = [1, 2, 3, 4, 5]
arr.append(6)        # Amortized O(1)
arr.insert(0, 0)     # O(n)
arr.pop()            # O(1)
arr.pop(0)           # O(n)
elemento = arr[2]    # O(1)  — acesso direto
```

### 2.2 Linked Lists

```python
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class LinkedList:
    def __init__(self):
        self.cabeca = None
        self._tamanho = 0

    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.cabeca
        self.cabeca = novo
        self._tamanho += 1

    def inserir_fim(self, valor):
        novo = No(valor)
        if not self.cabeca:
            self.cabeca = novo
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo
        self._tamanho += 1

    def buscar(self, valor):
        atual = self.cabeca
        pos = 0
        while atual:
            if atual.valor == valor:
                return pos
            atual = atual.proximo
            pos += 1
        return -1

    def remover(self, valor):
        if not self.cabeca:
            return False
        if self.cabeca.valor == valor:
            self.cabeca = self.cabeca.proximo
            self._tamanho -= 1
            return True
        atual = self.cabeca
        while atual.proximo:
            if atual.proximo.valor == valor:
                atual.proximo = atual.proximo.proximo
                self._tamanho -= 1
                return True
            atual = atual.proximo
        return False

    def __len__(self):
        return self._tamanho

    def __repr__(self):
        valores = []
        atual = self.cabeca
        while atual:
            valores.append(str(atual.valor))
            atual = atual.proximo
        return "[" + " → ".join(valores) + "]"

ll = LinkedList()
ll.inserir_inicio(3)
ll.inserir_inicio(2)
ll.inserir_inicio(1)
ll.inserir_fim(4)
print(f"Lista: {ll}")
print(f"Buscar 3: pos {ll.buscar(3)}")
ll.remover(2)
print(f"Após remover 2: {ll}")
```

### 2.3 Stacks e Queues

```python
from collections import deque

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

def avaliar_rpn(expressao):
    pilha = Stack()
    ops = {'+': lambda a, b: a + b, '-': lambda a, b: a - b,
           '*': lambda a, b: a * b, '/': lambda a, b: a / b}
    for token in expressao.split():
        if token in ops:
            b = pilha.pop()
            a = pilha.pop()
            pilha.push(ops[token](a, b))
        else:
            pilha.push(float(token))
    return pilha.pop()

print(f"RPN '3 4 + 2 *': {avaliar_rpn('3 4 + 2 *')}")

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        raise IndexError("dequeue from empty queue")

    def front(self):
        return self.items[0] if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

def simulador_fila_impressao(tarefas):
    fila = Queue()
    for tarefa in tarefas:
        fila.enqueue(tarefa)
        print(f"Enfileirado: {tarefa}")
    while not fila.is_empty():
        tarefa = fila.dequeue()
        print(f"Processando: {tarefa}")

simulador_fila_impressao(["Doc1.pdf", "Foto.jpg", "Planilha.xlsx"])
```

---

## 3. Árvores e Heap

### 3.1 Árvore Binária de Busca (BST)

```python
class NoBST:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class BST:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if not self.raiz:
            self.raiz = NoBST(chave)
        else:
            self._inserir(self.raiz, chave)

    def _inserir(self, no, chave):
        if chave < no.chave:
            if no.esquerda:
                self._inserir(no.esquerda, chave)
            else:
                no.esquerda = NoBST(chave)
        elif chave > no.chave:
            if no.direita:
                self._inserir(no.direita, chave)
            else:
                no.direita = NoBST(chave)

    def buscar(self, chave):
        return self._buscar(self.raiz, chave)

    def _buscar(self, no, chave):
        if not no or no.chave == chave:
            return no
        if chave < no.chave:
            return self._buscar(no.esquerda, chave)
        return self._buscar(no.direita, chave)

    def percurso_inorder(self):
        resultado = []
        self._inorder(self.raiz, resultado)
        return resultado

    def _inorder(self, no, resultado):
        if no:
            self._inorder(no.esquerda, resultado)
            resultado.append(no.chave)
            self._inorder(no.direita, resultado)

    def percurso_preorder(self):
        resultado = []
        self._preorder(self.raiz, resultado)
        return resultado

    def _preorder(self, no, resultado):
        if no:
            resultado.append(no.chave)
            self._preorder(no.esquerda, resultado)
            self._preorder(no.direita, resultado)

    def percurso_posorder(self):
        resultado = []
        self._posorder(self.raiz, resultado)
        return resultado

    def _posorder(self, no, resultado):
        if no:
            self._posorder(no.esquerda, resultado)
            self._posorder(no.direita, resultado)
            resultado.append(no.chave)

bst = BST()
for v in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    bst.inserir(v)

print(f"Inorder:   {bst.percurso_inorder()}")
print(f"Preorder:  {bst.percurso_preorder()}")
print(f"Posorder:  {bst.percurso_posorder()}")
print(f"Buscar 7: {'Encontrado' if bst.buscar(7) else 'Ausente'}")
```

### 3.2 Árvores Balanceadas (AVL)

```python
class NoAVL:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1

class AVL:
    def __init__(self):
        self.raiz = None

    def _altura(self, no):
        return no.altura if no else 0

    def _bf(self, no):
        return self._altura(no.esquerda) - self._altura(no.direita) if no else 0

    def _rot_dir(self, y):
        x = y.esquerda
        T2 = x.direita
        x.direita = y
        y.esquerda = T2
        y.altura = 1 + max(self._altura(y.esquerda), self._altura(y.direita))
        x.altura = 1 + max(self._altura(x.esquerda), self._altura(x.direita))
        return x

    def _rot_esq(self, x):
        y = x.direita
        T2 = y.esquerda
        y.esquerda = x
        x.direita = T2
        x.altura = 1 + max(self._altura(x.esquerda), self._altura(x.direita))
        y.altura = 1 + max(self._altura(y.esquerda), self._altura(y.direita))
        return y

    def inserir(self, chave):
        self.raiz = self._inserir(self.raiz, chave)

    def _inserir(self, no, chave):
        if not no:
            return NoAVL(chave)
        if chave < no.chave:
            no.esquerda = self._inserir(no.esquerda, chave)
        else:
            no.direita = self._inserir(no.direita, chave)
        no.altura = 1 + max(self._altura(no.esquerda), self._altura(no.direita))
        bf = self._bf(no)
        if bf > 1 and chave < no.esquerda.chave:
            return self._rot_dir(no)
        if bf < -1 and chave > no.direita.chave:
            return self._rot_esq(no)
        if bf > 1 and chave > no.esquerda.chave:
            no.esquerda = self._rot_esq(no.esquerda)
            return self._rot_dir(no)
        if bf < -1 and chave < no.direita.chave:
            no.direita = self._rot_dir(no.direita)
            return self._rot_esq(no)
        return no

    def inorder(self):
        r = []
        self._inorder(self.raiz, r)
        return r

    def _inorder(self, no, r):
        if no:
            self._inorder(no.esquerda, r)
            r.append(no.chave)
            self._inorder(no.direita, r)

avl = AVL()
for v in [10, 20, 30, 40, 50, 25]:
    avl.inserir(v)
print(f"AVL inorder: {avl.inorder()}")
```

### 3.3 Heap Binário (Priority Queue)

```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def _pai(self, i):
        return (i - 1) // 2

    def _fe(self, i):
        return 2 * i + 1

    def _fd(self, i):
        return 2 * i + 2

    def inserir(self, valor):
        self.heap.append(valor)
        self._subir(len(self.heap) - 1)

    def _subir(self, i):
        while i > 0 and self.heap[i] < self.heap[self._pai(i)]:
            self.heap[i], self.heap[self._pai(i)] = self.heap[self._pai(i)], self.heap[i]
            i = self._pai(i)

    def extrair_min(self):
        if not self.heap:
            raise IndexError("heap vazio")
        if len(self.heap) == 1:
            return self.heap.pop()
        minimo = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._descer(0)
        return minimo

    def _descer(self, i):
        menor = i
        esq = self._fe(i)
        dir = self._fd(i)
        if esq < len(self.heap) and self.heap[esq] < self.heap[menor]:
            menor = esq
        if dir < len(self.heap) and self.heap[dir] < self.heap[menor]:
            menor = dir
        if menor != i:
            self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
            self._descer(menor)

    @classmethod
    def heapify(cls, arr):
        h = cls()
        h.heap = arr[:]
        for i in range(len(arr) // 2 - 1, -1, -1):
            h._descer(i)
        return h

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)

heap = MinHeap()
for v in [5, 3, 8, 1, 9, 2]:
    heap.inserir(v)
print(f"Heap: {heap}")
print(f"Extraídos: {[heap.extrair_min() for _ in range(6)]}")

arr = [9, 5, 3, 7, 1, 8]
h2 = MinHeap.heapify(arr)
print(f"Heapify {arr}: {h2}")
```

---

## 4. Hash Tables

### 4.1 Implementação com Encadeamento

```python
class ParChaveValor:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None

class HashTable:
    def __init__(self, capacidade=16):
        self.capacidade = capacidade
        self.tabela = [None] * capacidade
        self._tamanho = 0

    def _hash(self, chave):
        if isinstance(chave, str):
            return sum(ord(c) * (31 ** i) for i, c in enumerate(chave)) % self.capacidade
        return hash(chave) % self.capacidade

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        if not self.tabela[indice]:
            self.tabela[indice] = ParChaveValor(chave, valor)
            self._tamanho += 1
        else:
            atual = self.tabela[indice]
            while atual:
                if atual.chave == chave:
                    atual.valor = valor
                    return
                if not atual.proximo:
                    atual.proximo = ParChaveValor(chave, valor)
                    self._tamanho += 1
                    return
                atual = atual.proximo
        self._redimensionar_se_necessario()

    def obter(self, chave):
        indice = self._hash(chave)
        atual = self.tabela[indice]
        while atual:
            if atual.chave == chave:
                return atual.valor
            atual = atual.proximo
        raise KeyError(chave)

    def remover(self, chave):
        indice = self._hash(chave)
        atual = self.tabela[indice]
        anterior = None
        while atual:
            if atual.chave == chave:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.tabela[indice] = atual.proximo
                self._tamanho -= 1
                return
            anterior = atual
            atual = atual.proximo
        raise KeyError(chave)

    def _redimensionar_se_necessario(self):
        if self._tamanho > self.capacidade * 0.75:
            antiga = self.tabela
            self.capacidade *= 2
            self.tabela = [None] * self.capacidade
            self._tamanho = 0
            for cabeca in antiga:
                atual = cabeca
                while atual:
                    self.inserir(atual.chave, atual.valor)
                    atual = atual.proximo

    def __contains__(self, chave):
        try:
            self.obter(chave)
            return True
        except KeyError:
            return False

    def __setitem__(self, chave, valor):
        self.inserir(chave, valor)

    def __getitem__(self, chave):
        return self.obter(chave)

    def __len__(self):
        return self._tamanho

ht = HashTable()
ht["nome"] = "João"
ht["idade"] = 30
ht["cidade"] = "São Paulo"
print(f"nome: {ht['nome']}, idade: {ht['idade']}")
ht["idade"] = 31
print(f"idade atualizada: {ht['idade']}")
print(f"'peso' in ht: {'peso' in ht}")
del ht["cidade"]
```

### 4.2 Cache LRU

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacidade):
        self.cache = OrderedDict()
        self.capacidade = capacidade

    def get(self, chave):
        if chave not in self.cache:
            return -1
        self.cache.move_to_end(chave)
        return self.cache[chave]

    def put(self, chave, valor):
        if chave in self.cache:
            self.cache.move_to_end(chave)
        self.cache[chave] = valor
        if len(self.cache) > self.capacidade:
            self.cache.popitem(last=False)

cache = LRUCache(3)
cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")
cache.get(1)
cache.put(4, "D")
print(f"LRU Cache: {list(cache.cache.items())}")
```

---

## 5. Algoritmos de Ordenação

### 5.1 Quick Sort

```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = _particionar(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def _particionar(arr, low, high):
    pivo = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr_qs = [38, 27, 43, 3, 9, 82, 10]
quick_sort(arr_qs)
print(f"Quick sort: {arr_qs}")
```

### 5.2 Merge Sort

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    esq = merge_sort(arr[:mid])
    dir = merge_sort(arr[mid:])
    return _merge(esq, dir)

def _merge(esq, dir):
    res = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            res.append(esq[i]); i += 1
        else:
            res.append(dir[j]); j += 1
    res.extend(esq[i:])
    res.extend(dir[j:])
    return res

arr_ms = [38, 27, 43, 3, 9, 82, 10]
print(f"Merge sort: {merge_sort(arr_ms)}")
```

### 5.3 Heap Sort

```python
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)

def _heapify(arr, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2
    if esq < n and arr[esq] > arr[maior]:
        maior = esq
    if dir < n and arr[dir] > arr[maior]:
        maior = dir
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        _heapify(arr, n, maior)

arr_hs = [38, 27, 43, 3, 9, 82, 10]
heap_sort(arr_hs)
print(f"Heap sort: {arr_hs}")
```

### 5.4 Comparação de Ordenação

| Algoritmo | Melhor | Médio | Pior | Memória | Estável |
|-----------|--------|-------|------|---------|---------|
| Quick sort | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | ❌ |
| Merge sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | ✅ |
| Heap sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | ❌ |
| Bubble sort | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ✅ |
| Counting sort | $O(n+k)$ | $O(n+k)$ | $O(n+k)$ | $O(k)$ | ✅ |

### 5.5 Ordenação Linear (Counting & Radix Sort)

```python
def counting_sort(arr, k):
    n = len(arr)
    count = [0] * (k + 1)
    output = [0] * n
    for v in arr:
        count[v] += 1
    for i in range(1, k + 1):
        count[i] += count[i - 1]
    for v in reversed(arr):
        output[count[v] - 1] = v
        count[v] -= 1
    return output

def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = _counting_sort_digit(arr, exp)
        exp *= 10
    return arr

def _counting_sort_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for v in arr:
        count[(v // exp) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for v in reversed(arr):
        dig = (v // exp) % 10
        output[count[dig] - 1] = v
        count[dig] -= 1
    return output

print(f"Counting sort: {counting_sort([4, 2, 2, 8, 3, 3, 1], 8)}")
print(f"Radix sort:   {radix_sort([170, 45, 75, 90, 802, 24, 2, 66])}")
```

---

## 6. Algoritmos de Busca

### 6.1 Busca Binária

```python
def busca_binaria(arr, alvo):
    esq, dir = 0, len(arr) - 1
    while esq <= dir:
        mid = (esq + dir) // 2
        if arr[mid] == alvo:
            return mid
        elif arr[mid] < alvo:
            esq = mid + 1
        else:
            dir = mid - 1
    return -1

def raiz_quadrada_inteira(n):
    esq, dir = 0, n
    while esq <= dir:
        mid = (esq + dir) // 2
        if mid * mid <= n:
            esq = mid + 1
        else:
            dir = mid - 1
    return dir

arr_ord = [1, 3, 5, 7, 9, 11, 13]
print(f"Busca 7: pos {busca_binaria(arr_ord, 7)}")
print(f"sqrt(50): {raiz_quadrada_inteira(50)}")
```

### 6.2 BFS e DFS em Grafos

```python
from collections import defaultdict, deque

class Grafo:
    def __init__(self, direcionado=False):
        self.adj = defaultdict(list)
        self.direcionado = direcionado

    def adicionar_aresta(self, u, v):
        self.adj[u].append(v)
        if not self.direcionado:
            self.adj[v].append(u)

    def bfs(self, inicio):
        visitados = {inicio}
        fila = deque([inicio])
        ordem = []
        while fila:
            v = fila.popleft()
            ordem.append(v)
            for viz in self.adj[v]:
                if viz not in visitados:
                    visitados.add(viz)
                    fila.append(viz)
        return ordem

    def dfs(self, inicio):
        visitados = set()
        ordem = []
        def _dfs(v):
            visitados.add(v)
            ordem.append(v)
            for viz in self.adj[v]:
                if viz not in visitados:
                    _dfs(viz)
        _dfs(inicio)
        return ordem

    def menor_distancia(self, u, v):
        if u == v:
            return 0
        visitados = {u}
        fila = deque([(u, 0)])
        while fila:
            vert, dist = fila.popleft()
            for viz in self.adj[vert]:
                if viz == v:
                    return dist + 1
                if viz not in visitados:
                    visitados.add(viz)
                    fila.append((viz, dist + 1))
        return -1

grafo = Grafo()
arestas = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8)]
for u, v in arestas:
    grafo.adicionar_aresta(u, v)

print(f"BFS(1): {grafo.bfs(1)}")
print(f"DFS(1): {grafo.dfs(1)}")
print(f"Dist 1→8: {grafo.menor_distancia(1, 8)}")
```

---

## 7. Algoritmos em Grafos

### 7.1 Dijkstra

```python
import heapq

def dijkstra(grafo, origem):
    distancias = {v: float('inf') for v in grafo}
    distancias[origem] = 0
    fila = [(0, origem)]
    visitados = set()
    while fila:
        dist_atual, u = heapq.heappop(fila)
        if u in visitados:
            continue
        visitados.add(u)
        for v, peso in grafo.get(u, []):
            if v in visitados:
                continue
            nova_dist = dist_atual + peso
            if nova_dist < distancias[v]:
                distancias[v] = nova_dist
                heapq.heappush(fila, (nova_dist, v))
    return distancias

def dijkstra_caminho(grafo, origem, destino):
    dist = {v: float('inf') for v in grafo}
    ant = {v: None for v in grafo}
    dist[origem] = 0
    fila = [(0, origem)]
    while fila:
        d, u = heapq.heappop(fila)
        if d > dist[u]:
            continue
        if u == destino:
            break
        for v, peso in grafo.get(u, []):
            nd = d + peso
            if nd < dist[v]:
                dist[v] = nd
                ant[v] = u
                heapq.heappush(fila, (nd, v))
    caminho = []
    v = destino
    while v is not None:
        caminho.append(v)
        v = ant[v]
    caminho.reverse()
    return caminho, dist[destino]

mapa = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 1), ('D', 5)],
    'C': [('D', 8), ('E', 10)],
    'D': [('E', 2)],
    'E': [],
}

print(f"Dijkstra (A): {dijkstra(mapa, 'A')}")
cam, d = dijkstra_caminho(mapa, 'A', 'E')
print(f"Caminho A→E: {cam}, distância: {d}")
```

### 7.2 Floyd-Warshall

```python
def floyd_warshall(grafo):
    vertices = list(grafo.keys())
    n = len(vertices)
    idx = {v: i for i, v in enumerate(vertices)}
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, vizinhos in grafo.items():
        for v, peso in vizinhos:
            dist[idx[u]][idx[v]] = peso
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return vertices, dist

vertices, dist = floyd_warshall(mapa)
print("Floyd-Warshall (A→E):", dist[0][4])
```

### 7.3 A* Search

```python
def a_star(grafo, inicio, objetivo, heuristica):
    fila = [(0 + heuristica(inicio, objetivo), 0, inicio, [inicio])]
    visitados = set()
    while fila:
        f, g, atual, caminho = heapq.heappop(fila)
        if atual == objetivo:
            return caminho, g
        if atual in visitados:
            continue
        visitados.add(atual)
        for vizinho, custo in grafo.get(atual, []):
            if vizinho not in visitados:
                ng = g + custo
                nh = heuristica(vizinho, objetivo)
                heapq.heappush(fila, (ng + nh, ng, vizinho, caminho + [vizinho]))
    return None, float('inf')

h = {'A': 6, 'B': 4, 'C': 4, 'D': 2, 'E': 0}
heuristic = lambda v, o: h.get(v, 0)

cam, custo = a_star(mapa, 'A', 'E', heuristic)
print(f"A* A→E: {cam}, custo: {custo}")
```

### 7.4 MST (Kruskal)

```python
class UnionFind:
    def __init__(self, n):
        self.pai = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.find(self.pai[x])
        return self.pai[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.pai[px] = py
        elif self.rank[px] > self.rank[py]:
            self.pai[py] = px
        else:
            self.pai[py] = px
            self.rank[px] += 1
        return True

def kruskal(vertices, arestas):
    arestas_ord = sorted(arestas, key=lambda x: x[2])
    uf = UnionFind(len(vertices))
    idx = {v: i for i, v in enumerate(vertices)}
    mst = []
    custo_total = 0
    for u, v, peso in arestas_ord:
        if uf.union(idx[u], idx[v]):
            mst.append((u, v, peso))
            custo_total += peso
    return mst, custo_total

vertices_mst = ['A', 'B', 'C', 'D', 'E']
arestas_mst = [
    ('A', 'B', 4), ('A', 'C', 2),
    ('B', 'C', 1), ('B', 'D', 5),
    ('C', 'D', 8), ('C', 'E', 10),
    ('D', 'E', 2),
]
mst, custo = kruskal(vertices_mst, arestas_mst)
print(f"MST (Kruskal): {mst}, custo: {custo}")
```

---

## 8. Paradigmas de Projeto

### 8.1 Divisão e Conquista

```python
def maior_subarray_sum(arr, esq, dir):
    if esq == dir:
        return arr[esq]
    mid = (esq + dir) // 2
    soma_esq = maior_subarray_sum(arr, esq, mid)
    soma_dir = maior_subarray_sum(arr, mid + 1, dir)
    soma_esq_max = float('-inf')
    soma_atual = 0
    for i in range(mid, esq - 1, -1):
        soma_atual += arr[i]
        soma_esq_max = max(soma_esq_max, soma_atual)
    soma_dir_max = float('-inf')
    soma_atual = 0
    for i in range(mid + 1, dir + 1):
        soma_atual += arr[i]
        soma_dir_max = max(soma_dir_max, soma_atual)
    return max(soma_esq, soma_dir, soma_esq_max + soma_dir_max)

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Maior subarray sum: {maior_subarray_sum(arr, 0, len(arr) - 1)}")
```

### 8.2 Programação Dinâmica

```python
def fib_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def fib_otimizado(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(f"Fib(10) DP: {fib_dp(10)}, Fib(10) O(1): {fib_otimizado(10)}")

def knapsack_01(pesos, valores, capacidade):
    n = len(pesos)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - pesos[i - 1]] + valores[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacidade]

def knapsack_otimizado(pesos, valores, capacidade):
    n = len(pesos)
    dp = [0] * (capacidade + 1)
    for i in range(n):
        for w in range(capacidade, pesos[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - pesos[i]] + valores[i])
    return dp[capacidade]

pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
print(f"Knapsack (cap=5): {knapsack_01(pesos, valores, 5)}")
print(f"Knapsack otimizado (cap=5): {knapsack_otimizado(pesos, valores, 5)}")

def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    seq = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            seq.append(s1[i - 1])
            i -= 1; j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return dp[m][n], ''.join(reversed(seq))

print(f"LCS('ABCBDAB', 'BDCAB'): {lcs('ABCBDAB', 'BDCAB')}")
```

### 8.3 Algoritmo Guloso

```python
def troco_guloso(moedas, valor):
    moedas_ord = sorted(moedas, reverse=True)
    resultado = {}
    resto = valor
    for moeda in moedas_ord:
        qtd = resto // moeda
        if qtd > 0:
            resultado[moeda] = qtd
            resto -= qtd * moeda
    return resultado, resto

print(f"Troco 47 (moedas BR): {troco_guloso([100, 50, 25, 10, 5, 1], 47)}")

def agendamento_intervalos(tarefas):
    tarefas_ord = sorted(tarefas, key=lambda t: t[1])
    selecionadas = []
    fim_atual = float('-inf')
    for inicio, fim in tarefas_ord:
        if inicio >= fim_atual:
            selecionadas.append((inicio, fim))
            fim_atual = fim
    return selecionadas

tarefas = [(1, 3), (2, 5), (3, 7), (1, 4), (5, 8), (6, 9)]
print(f"Agendamento máximo: {agendamento_intervalos(tarefas)}")
```

---

## 9. Paralelismo e Concorrência

### 9.1 Threading e Locks

```python
import threading
import time

contador = 0
lock = threading.Lock()

def incrementar(n):
    global contador
    for _ in range(n):
        with lock:
            contador += 1

threads = []
N = 100000
for _ in range(4):
    t = threading.Thread(target=incrementar, args=(N,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Contador (com lock): {contador} (esperado: {4 * N})")

contador2 = 0

def incrementar_sem_lock(n):
    global contador2
    for _ in range(n):
        contador2 += 1

threads2 = []
for _ in range(4):
    t = threading.Thread(target=incrementar_sem_lock, args=(N,))
    threads2.append(t)
    t.start()

for t in threads2:
    t.join()

print(f"Contador (sem lock): {contador2} (esperado: {4 * N})")
```

### 9.2 Thread Pools

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def tarefa_pesada(n):
    time.sleep(0.1)
    return n * n

with ThreadPoolExecutor(max_workers=4) as executor:
    futuros = [executor.submit(tarefa_pesada, i) for i in range(10)]
    resultados = [f.result() for f in as_completed(futuros)]

print(f"ThreadPool results: {sorted(resultados)}")
```

### 9.3 asyncio

```python
import asyncio

async def tarefa_async(n):
    await asyncio.sleep(0.1)
    return n * 2

async def main():
    tarefas = [tarefa_async(i) for i in range(5)]
    resultados = await asyncio.gather(*tarefas)
    print(f"asyncio results: {resultados}")

asyncio.run(main())
```

---

## 10. Glossário

| Termo | Definição |
|-------|-----------|
| **Big O** | Limite superior assintótico de uma função |
| **BST** | Árvore binária de busca; inserção, busca e remoção $O(h)$ |
| **DFS/BFS** | Busca em profundidade/largura em grafos |
| **Dijkstra** | Algoritmo de caminho mínimo para grafos com pesos positivos |
| **DP** | Programação dinâmica; resolve subproblemas sobrepostos |
| **Floyd-Warshall** | Caminho mínimo entre todos os pares $O(V^3)$ |
| **Guloso** | Paradigma que escolhe a melhor opção local a cada passo |
| **Hash Table** | Estrutura com tempo $O(1)$ médio para inserção/busca |
| **Heap** | Árvore binária completa com propriedade de heap (max/min) |
| **LCS** | Longest Common Subsequence; problema clássico de DP |
| **LRU** | Least Recently Used; política de substituição de cache |
| **MST** | Minimum Spanning Tree; conecta todos vértices com custo mínimo |
| **Race Condition** | Comportamento indeterminado devido a acesso concorrente sem sincronização |

---

## 11. Referências

### Livros Clássicos
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. & Stein, C. (2009). *Introduction to Algorithms* (3ª ed.). MIT Press.
- Sedgewick, R. & Wayne, K. (2011). *Algorithms* (4ª ed.). Addison-Wesley.
- Knuth, D. E. (1997). *The Art of Computer Programming* (Vol. 1–3). Addison-Wesley.
- Skiena, S. S. (2008). *The Algorithm Design Manual* (2ª ed.). Springer.
- Kleinberg, J. & Tardos, É. (2006). *Algorithm Design*. Addison-Wesley.

### Tópicos Específicos
- Dasgupta, S., Papadimitriou, C. H. & Vazirani, U. V. (2008). *Algorithms*. McGraw-Hill.
- Herlihy, M. & Shavit, N. (2012). *The Art of Multiprocessor Programming*. Morgan Kaufmann.

### Implementações e Prática
- Hetland, M. L. (2014). *Python Algorithms: Mastering Basic Algorithms in the Python Language* (2ª ed.). Apress.
- Bhargava, A. Y. (2016). *Grokking Algorithms*. Manning.

### Conexões com Outras Notas
- [[Conhecimento-Geral/Computacao/Ciencia-da-Computacao]] — complexidade computacional, P vs NP
- [[Conhecimento-Geral/Computacao/NLP-Fundamentos]] — algoritmos de busca e DP em NLP (Viterbi, CKY)
- [[Conhecimento-Geral/Matematica/Algebra-Linear-Essencial]] — matrizes, grafos como matrizes de adjacência
- [[Conhecimento-Geral/Matematica/Probabilidade-e-Estatistica]] — análise probabilística de algoritmos
- [[Conhecimento-Geral/Matematica/Teoria-da-Informacao]] — limites teóricos de compressão e ordenação
