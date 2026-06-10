---
tags: [skills, skills-eng, algorithms, data-structures, complexity, dynamic-programming]
updated: 2026-06-10
title: "Algoritmos e Estruturas de Dados Avancados"
date: 2026-05-16
---

# Algoritmos e Estruturas de Dados Avancados

Referencia completa para analise de complexidade, estruturas de dados avancadas, algoritmos de ordenacao, grafos, programacao dinamica e algoritmos de strings. Guia pratico com implementacoes em Python e TypeScript para treinamento do agente JARVIS.

## Analise de Complexidade

### Notacoes Assintoticas

| Notacao | Nome | Significado | Exemplo |
|---------|------|-------------|---------|
| O(g(n)) | Big O | Limite superior (pior caso) | Busca linear: O(n) |
| Omega(g(n)) | Big Omega | Limite inferior (melhor caso) | Busca linear: Omega(1) |
| Theta(g(n)) | Big Theta | Limite justo (caso exato) | Busca em array ordenado: Theta(log n) |

```python
# Big O: O(n) - pior caso cresce linearmente
def busca_linear(arr: list[int], target: int) -> int:
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1  # O(n) no pior caso

# Big Omega: Omega(1) - melhor caso constante
# Big Theta: Theta(n) - caso medio e pior sao lineares
```

```typescript
// Big O: O(n^2) - pior caso quadratico
function bubbleSort(arr: number[]): number[] {
  const n = arr.length;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
      }
    }
  }
  return arr;
}
```

### Classes de Complexidade Comuns

| Classe | Nome | Exemplo Tipico | Escala (n=1000) |
|--------|------|----------------|-----------------|
| O(1) | Constante | Acesso a array por indice | 1 operacao |
| O(log n) | Logaritmica | Busca binaria | ~10 operacoes |
| O(n) | Linear | Iteracao simples | 1000 operacoes |
| O(n log n) | Linearitmica | Merge Sort, Quick Sort medio | ~10000 operacoes |
| O(n^2) | Quadratica | Bubble Sort, dois loops aninhados | 1.000.000 operacoes |
| O(2^n) | Exponencial | Forca bruta em subconjuntos | 10^301 operacoes |
| O(n!) | Fatorial | Permutacoes | Impossivel para n>20 |

```python
# O(log n) - Busca binaria
def busca_binaria(arr: list[int], target: int) -> int:
    esq, dir = 0, len(arr) - 1
    while esq <= dir:
        meio = (esq + dir) // 2
        if arr[meio] == target:
            return meio
        elif arr[meio] < target:
            esq = meio + 1
        else:
            dir = meio - 1
    return -1
```

```typescript
// O(log n) - Busca binaria em TypeScript
function buscaBinaria(arr: number[], target: number): number {
  let esq = 0, dir = arr.length - 1;
  while (esq <= dir) {
    const meio = Math.floor((esq + dir) / 2);
    if (arr[meio] === target) return meio;
    if (arr[meio] < target) esq = meio + 1;
    else dir = meio - 1;
  }
  return -1;
}
```

### Analise Amortizada

Analise amortizada calcula o custo medio por operacao em uma sequencia, mesmo que operacoes individuais sejam caras.

```python
# Dynamic Array (list do Python) - Amortized O(1) append
class ArrayDinamico:
    def __init__(self):
        self._capacidade = 1
        self._tamanho = 0
        self._dados = [None] * self._capacidade

    def append(self, valor):
        if self._tamanho == self._capacidade:
            self._redimensionar(2 * self._capacidade)  # O(n)
        self._dados[self._tamanho] = valor
        self._tamanho += 1

    def _redimensionar(self, nova_capacidade):
        novos_dados = [None] * nova_capacidade
        for i in range(self._tamanho):
            novos_dados[i] = self._dados[i]
        self._dados = novos_dados
        self._capacidade = nova_capacidade
    # Custo amortizado: O(1) por append
    # Prova: n appends custam no maximo 2n operacoes => O(1) amortizado
```

```typescript
// Dynamic Array em TypeScript - Amortized O(1) push
class ArrayDinamico<T> {
  private dados: (T | null)[];
  private tamanho: number;
  private capacidade: number;

  constructor() {
    this.capacidade = 1;
    this.tamanho = 0;
    this.dados = new Array(this.capacidade);
  }

  push(valor: T): void {
    if (this.tamanho === this.capacidade) {
      this.redimensionar(2 * this.capacidade);
    }
    this.dados[this.tamanho++] = valor;
  }

  private redimensionar(novaCapacidade: number): void {
    const novosDados = new Array(novaCapacidade);
    for (let i = 0; i < this.tamanho; i++) {
      novosDados[i] = this.dados[i];
    }
    this.dados = novosDados;
    this.capacidade = novaCapacidade;
  }
}
```

### Trade-off Tempo vs Espaco

| Tecnica | Tempo | Espaco | Quando Usar |
|---------|-------|--------|-------------|
| Memoization | O(1) lookup | O(n) memoria | Subproblemas repetidos |
| Hash table | O(1) media | O(n) memoria | Busca rapida por chave |
| Array ordenado + busca binaria | O(log n) | O(1) extra | Buscas frequentes, poucas insercoes |
| Bloom filter | O(k) hashing | O(m) bits | Teste de pertinencia aproximado |

## Estruturas de Dados

### Listas Ligadas

```
Singly Linked List:
[Head] -> [A|next] -> [B|next] -> [C|next] -> null

Doubly Linked List:
null <- [A|prev|next] <-> [B|prev|next] <-> [C|prev|next] -> null

Circular Linked List:
[Head] -> [A|next] -> [B|next] -> [C|next] --+
  ^------------------------------------------+
```

```python
class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class ListaLigada:
    def __init__(self):
        self.cabeca = None

    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.prox = self.cabeca
        self.cabeca = novo  # O(1)

    def inserir_fim(self, valor):
        novo = No(valor)
        if not self.cabeca:
            self.cabeca = novo
            return
        atual = self.cabeca
        while atual.prox:
            atual = atual.prox
        atual.prox = novo  # O(n)

    def remover(self, valor):
        if not self.cabeca:
            return
        if self.cabeca.valor == valor:
            self.cabeca = self.cabeca.prox
            return
        atual = self.cabeca
        while atual.prox and atual.prox.valor != valor:
            atual = atual.prox
        if atual.prox:
            atual.prox = atual.prox.prox  # O(n)
```

```typescript
class No<T> {
  valor: T;
  prox: No<T> | null;
  constructor(valor: T) {
    this.valor = valor;
    this.prox = null;
  }
}

class ListaLigada<T> {
  private cabeca: No<T> | null = null;

  inserirInicio(valor: T): void {
    const novo = new No(valor);
    novo.prox = this.cabeca;
    this.cabeca = novo;
  }

  buscar(valor: T): boolean {
    let atual = this.cabeca;
    while (atual) {
      if (atual.valor === valor) return true;
      atual = atual.prox;
    }
    return false;
  }
}
```

### Pilhas e Filas

```
Stack (LIFO):          Queue (FIFO):
|   E   |  <- top      [A] [B] [C] [D] <- enqueue
|   D   |              ^               ^
|   C   |            dequeue          rear
|   B   |
|   A   |  <- bottom
```

```python
# Pilha (Stack) - Python usa list nativamente
class Pilha:
    def __init__(self):
        self._itens = []

    def push(self, item):
        self._itens.append(item)  # O(1)

    def pop(self):
        if self.esta_vazia():
            raise IndexError("Pilha vazia")
        return self._itens.pop()  # O(1)

    def topo(self):
        return self._itens[-1] if not self.esta_vazia() else None

    def esta_vazia(self):
        return len(self._itens) == 0

# Aplicacao: validacao de parenteses
def parenteses_balanceados(s: str) -> bool:
    pilha = Pilha()
    mapa = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '({[':
            pilha.push(char)
        elif char in ')}]':
            if pilha.esta_vazia() or pilha.pop() != mapa[char]:
                return False
    return pilha.esta_vazia()
```

```typescript
// Fila (Queue) com duas pilhas
class Fila<T> {
  private entrada: T[] = [];
  private saida: T[] = [];

  enqueue(item: T): void {
    this.entrada.push(item);
  }

  dequeue(): T | undefined {
    if (this.saida.length === 0) {
      while (this.entrada.length > 0) {
        this.saida.push(this.entrada.pop()!);
      }
    }
    return this.saida.pop();
  }

  frente(): T | undefined {
    if (this.saida.length === 0) {
      while (this.entrada.length > 0) {
        this.saida.push(this.entrada.pop()!);
      }
    }
    return this.saida[this.saida.length - 1];
  }
}
```

### Tabelas Hash

```
Hash Table com Chaining:
Index 0: null
Index 1: ["chave1", valor] -> ["chave4", valor] -> null
Index 2: ["chave2", valor] -> null
Index 3: null

Open Addressing (Linear Probing):
Index 0: null
Index 1: ["chave1", valor]
Index 2: ["chave2", valor]
Index 3: ["chave4", valor]  (colidiu com 1, probing ate 3)
```

```python
class TabelaHash:
    def __init__(self, tamanho=16):
        self._tamanho = tamanho
        self._buckets: list[list[tuple]] = [[] for _ in range(tamanho)]
        self._count = 0

    def _hash(self, chave: str) -> int:
        return hash(chave) % self._tamanho

    def put(self, chave: str, valor):
        idx = self._hash(chave)
        for i, (k, v) in enumerate(self._buckets[idx]):
            if k == chave:
                self._buckets[idx][i] = (chave, valor)
                return
        self._buckets[idx].append((chave, valor))
        self._count += 1
        if self._count / self._tamanho > 0.75:
            self._redimensionar()

    def get(self, chave: str):
        idx = self._hash(chave)
        for k, v in self._buckets[idx]:
            if k == chave:
                return v
        raise KeyError(chave)
    # Complexidade: O(1) media, O(n) pior caso (todas no mesmo bucket)
```

```typescript
// Tabela Hash com Open Addressing (Linear Probing)
class TabelaHash<T> {
  private buckets: (string | null)[];
  private valores: (T | null)[];
  private tamanho: number;
  private count: number;

  constructor(tamanho = 16) {
    this.tamanho = tamanho;
    this.count = 0;
    this.buckets = new Array(tamanho).fill(null);
    this.valores = new Array(tamanho).fill(null);
  }

  private hash(chave: string): number {
    let h = 0;
    for (let i = 0; i < chave.length; i++) {
      h = ((h << 5) - h + chave.charCodeAt(i)) | 0;
    }
    return Math.abs(h) % this.tamanho;
  }

  put(chave: string, valor: T): void {
    if (this.count / this.tamanho > 0.75) this.redimensionar();
    let idx = this.hash(chave);
    while (this.buckets[idx] !== null && this.buckets[idx] !== chave) {
      idx = (idx + 1) % this.tamanho;
    }
    if (this.buckets[idx] === null) this.count++;
    this.buckets[idx] = chave;
    this.valores[idx] = valor;
  }

  get(chave: string): T | undefined {
    let idx = this.hash(chave);
    while (this.buckets[idx] !== null) {
      if (this.buckets[idx] === chave) return this.valores[idx]!;
      idx = (idx + 1) % this.tamanho;
    }
    return undefined;
  }
}
```

### Arvores

```
Arvore Binaria de Busca (BST):
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13

AVL Tree (balanceada, fator de altura <= 1):
        8
       / \
      4   12
     / \  / \
    2  6 10  14
```

```python
class NoBST:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir_rec(self.raiz, valor)

    def _inserir_rec(self, no, valor):
        if no is None:
            return NoBST(valor)
        if valor < no.valor:
            no.esq = self._inserir_rec(no.esq, valor)
        elif valor > no.valor:
            no.dir = self._inserir_rec(no.dir, valor)
        return no

    def buscar(self, valor) -> bool:
        return self._buscar_rec(self.raiz, valor)

    def _buscar_rec(self, no, valor) -> bool:
        if no is None:
            return False
        if valor == no.valor:
            return True
        return self._buscar_rec(no.esq, valor) if valor < no.valor \
            else self._buscar_rec(no.dir, valor)
    # Inserir/Buscar: O(h) onde h e altura. BST: O(log n) medio, O(n) pior
```

```typescript
// AVL Tree - auto-balanceada
class NoAVL {
  valor: number;
  esq: NoAVL | null = null;
  dir: NoAVL | null = null;
  altura: number = 1;
  constructor(valor: number) { this.valor = valor; }
}

class ArvoreAVL {
  private raiz: NoAVL | null = null;

  private altura(no: NoAVL | null): number {
    return no ? no.altura : 0;
  }

  private fatorBalanceamento(no: NoAVL | null): number {
    return no ? this.altura(no.esq) - this.altura(no.dir) : 0;
  }

  private rotacaoDireita(y: NoAVL): NoAVL {
    const x = y.esq!;
    const T2 = x.dir;
    x.dir = y;
    y.esq = T2;
    y.altura = 1 + Math.max(this.altura(y.esq), this.altura(y.dir));
    x.altura = 1 + Math.max(this.altura(x.esq), this.altura(x.dir));
    return x;
  }

  private rotacaoEsquerda(x: NoAVL): NoAVL {
    const y = x.dir!;
    const T2 = y.esq;
    y.esq = x;
    x.dir = T2;
    x.altura = 1 + Math.max(this.altura(x.esq), this.altura(x.dir));
    y.altura = 1 + Math.max(this.altura(y.esq), this.altura(y.dir));
    return y;
  }

  inserir(valor: number): void {
    this.raiz = this._inserirRec(this.raiz, valor);
  }

  private _inserirRec(no: NoAVL | null, valor: number): NoAVL {
    if (!no) return new NoAVL(valor);
    if (valor < no.valor) no.esq = this._inserirRec(no.esq, valor);
    else if (valor > no.valor) no.dir = this._inserirRec(no.dir, valor);
    else return no;

    no.altura = 1 + Math.max(this.altura(no.esq), this.altura(no.dir));
    const fb = this.fatorBalanceamento(no);

    if (fb > 1 && valor < no.esq!.valor) return this.rotacaoDireita(no);
    if (fb < -1 && valor > no.dir!.valor) return this.rotacaoEsquerda(no);
    if (fb > 1 && valor > no.esq!.valor) {
      no.esq = this.rotacaoEsquerda(no.esq!);
      return this.rotacaoDireita(no);
    }
    if (fb < -1 && valor < no.dir!.valor) {
      no.dir = this.rotacaoDireita(no.dir!);
      return this.rotacaoEsquerda(no);
    }
    return no;
  }
  // AVL: O(log n) garantido para insercao/busca/remocao
}
```

### Heaps (Min-Heap / Max-Heap)

```
Min-Heap:              Max-Heap:
       2                     10
      / \                   /  \
     3   5                 8    6
    / \ / \               / \  /
   4  7 8  6             3   4 5
Array: [2,3,5,4,7,8,6]   Array: [10,8,6,3,4,5]
```

```python
import heapq

# Python usa heapq para min-heap
def heap_demo():
    heap = []
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 2)
    heapq.heappush(heap, 8)
    print(heapq.heappop(heap))  # 2 (menor elemento)

    # Max-heap: negar valores
    max_heap = []
    heapq.heappush(max_heap, -5)
    heapq.heappush(max_heap, -2)
    heapq.heappush(max_heap, -8)
    print(-heapq.heappop(max_heap))  # 8 (maior elemento)

# Heap Sort
def heap_sort(arr: list[int]) -> list[int]:
    heapq.heapify(arr)  # O(n)
    return [heapq.heappop(arr) for _ in range(len(arr))]  # O(n log n)
```

```typescript
// Min-Heap em TypeScript
class MinHeap {
  private heap: number[] = [];

  private pai(i: number): number { return Math.floor((i - 1) / 2); }
  private esq(i: number): number { return 2 * i + 1; }
  private dir(i: number): number { return 2 * i + 2; }

  push(val: number): void {
    this.heap.push(val);
    this.borbulharCima(this.heap.length - 1);
  }

  pop(): number | undefined {
    if (this.heap.length === 0) return undefined;
    const topo = this.heap[0];
    const ultimo = this.heap.pop()!;
    if (this.heap.length > 0) {
      this.heap[0] = ultimo;
      this.borbulharBaixo(0);
    }
    return topo;
  }

  private borbulharCima(i: number): void {
    while (i > 0 && this.heap[this.pai(i)] > this.heap[i]) {
      [this.heap[this.pai(i)], this.heap[i]] = [this.heap[i], this.heap[this.pai(i)]];
      i = this.pai(i);
    }
  }

  private borbulharBaixo(i: number): void {
    const n = this.heap.length;
    while (true) {
      let menor = i;
      const e = this.esq(i), d = this.dir(i);
      if (e < n && this.heap[e] < this.heap[menor]) menor = e;
      if (d < n && this.heap[d] < this.heap[menor]) menor = d;
      if (menor === i) break;
      [this.heap[menor], this.heap[i]] = [this.heap[i], this.heap[menor]];
      i = menor;
    }
  }
}
```

### Grafos

```
Adjacency List:          Adjacency Matrix:
A: [B, C]                |   A  B  C  D
B: [A, D]                A | 0  1  1  0
C: [A, D]                B | 1  0  0  1
D: [B, C]                C | 1  0  0  1
                         D | 0  1  1  0
```

```python
from collections import deque, defaultdict

class Grafo:
    def __init__(self):
        self.adj = defaultdict(list)

    def adicionar_aresta(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # nao-direcionado

    def bfs(self, inicio):
        visitados = {inicio}
        fila = deque([inicio])
        ordem = []
        while fila:
            no = fila.popleft()
            ordem.append(no)
            for vizinho in self.adj[no]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)
        return ordem

    def dfs(self, inicio, visitados=None):
        if visitados is None:
            visitados = set()
        visitados.add(inicio)
        for vizinho in self.adj[inicio]:
            if vizinho not in visitados:
                self.dfs(vizinho, visitados)
        return visitados
```

```typescript
// Grafo com adjacency list em TypeScript
class Grafo<T> {
  private adj: Map<T, T[]> = new Map();

  adicionarAresta(u: T, v: T, direcionado = false): void {
    if (!this.adj.has(u)) this.adj.set(u, []);
    if (!this.adj.has(v)) this.adj.set(v, []);
    this.adj.get(u)!.push(v);
    if (!direcionado) this.adj.get(v)!.push(u);
  }

  bfs(inicio: T): T[] {
    const visitados = new Set<T>([inicio]);
    const fila: T[] = [inicio];
    const ordem: T[] = [];
    while (fila.length > 0) {
      const no = fila.shift()!;
      ordem.push(no);
      for (const viz of this.adj.get(no) || []) {
        if (!visitados.has(viz)) {
          visitados.add(viz);
          fila.push(viz);
        }
      }
    }
    return ordem;
  }
}
```

### Tries (Arvore de Prefixos)

```
Trie para: "cat", "car", "cart"
       root
        |
        c
        |
        a
       / \
      t   r
           \
            t
```

```python
class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.fim_palavra = False

class Trie:
    def __init__(self):
        self.raiz = NoTrie()

    def inserir(self, palavra: str):
        no = self.raiz
        for char in palavra:
            if char not in no.filhos:
                no.filhos[char] = NoTrie()
            no = no.filhos[char]
        no.fim_palavra = True

    def buscar(self, palavra: str) -> bool:
        no = self.raiz
        for char in palavra:
            if char not in no.filhos:
                return False
            no = no.filhos[char]
        return no.fim_palavra

    def iniciar_com(self, prefixo: str) -> bool:
        no = self.raiz
        for char in prefixo:
            if char not in no.filhos:
                return False
            no = no.filhos[char]
        return True
    # Inserir/Buscar: O(m) onde m e comprimento da palavra
```

```typescript
// Trie com autocomplete
class TrieNode {
  filhos: Map<string, TrieNode> = new Map();
  fimPalavra = false;
}

class Trie {
  private raiz = new TrieNode();

  inserir(palavra: string): void {
    let no = this.raiz;
    for (const char of palavra) {
      if (!no.filhos.has(char)) no.filhos.set(char, new TrieNode());
      no = no.filhos.get(char)!;
    }
    no.fimPalavra = true;
  }

  autocomplete(prefixo: string): string[] {
    let no = this.raiz;
    for (const char of prefixo) {
      if (!no.filhos.has(char)) return [];
      no = no.filhos.get(char)!;
    }
    const resultados: string[] = [];
    this._coletar(no, prefixo, resultados);
    return resultados;
  }

  private _coletar(no: TrieNode, prefixo: string, resultados: string[]): void {
    if (no.fimPalavra) resultados.push(prefixo);
    for (const [char, filho] of no.filhos) {
      this._coletar(filho, prefixo + char, resultados);
    }
  }
}
```

### Bloom Filter

```python
import hashlib

class BloomFilter:
    def __init__(self, tamanho=1000, num_hashes=3):
        self.tamanho = tamanho
        self.num_hashes = num_hashes
        self.bit_array = [False] * tamanho

    def _hashes(self, item: str) -> list[int]:
        hashes = []
        for i in range(self.num_hashes):
            h = hashlib.sha256(f"{item}{i}".encode()).hexdigest()
            hashes.append(int(h, 16) % self.tamanho)
        return hashes

    def adicionar(self, item: str):
        for h in self._hashes(item):
            self.bit_array[h] = True

    def contem(self, item: str) -> bool:
        return all(self.bit_array[h] for h in self._hashes(item))
    # O(k) para k funcoes hash. Falsos positivos possiveis, falsos negativos impossiveis
```

## Algoritmos de Ordenacao

### Comparacao de Algoritmos

| Algoritmo | Melhor | Medio | Pior | Espaco | Estavel | In-place |
|-----------|--------|-------|------|--------|---------|----------|
| Quick Sort | O(n log n) | O(n log n) | O(n^2) | O(log n) | Nao | Sim |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Sim | Nao |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | Nao | Sim |
| Tim Sort | O(n) | O(n log n) | O(n log n) | O(n) | Sim | Nao |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Sim | Nao |
| Radix Sort | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n+k) | Sim | Nao |
| Bubble Sort | O(n) | O(n^2) | O(n^2) | O(1) | Sim | Sim |

### Quick Sort

```python
def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    pivô = arr[len(arr) // 2]
    esquerda = [x for x in arr if x < pivô]
    meio = [x for x in arr if x == pivô]
    direita = [x for x in arr if x > pivô]
    return quick_sort(esquerda) + meio + quick_sort(direita)

# In-place Quick Sort
def quick_sort_inplace(arr: list[int], baixo=0, alto=None) -> list[int]:
    if alto is None:
        alto = len(arr) - 1
    if baixo < alto:
        pi = particao(arr, baixo, alto)
        quick_sort_inplace(arr, baixo, pi - 1)
        quick_sort_inplace(arr, pi + 1, alto)
    return arr

def particao(arr, baixo, alto):
    pivô = arr[alto]
    i = baixo - 1
    for j in range(baixo, alto):
        if arr[j] <= pivô:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1
```

```typescript
// Merge Sort em TypeScript
function mergeSort(arr: number[]): number[] {
  if (arr.length <= 1) return arr;
  const meio = Math.floor(arr.length / 2);
  const esquerda = mergeSort(arr.slice(0, meio));
  const direita = mergeSort(arr.slice(meio));
  return merge(esquerda, direita);
}

function merge(esq: number[], dir: number[]): number[] {
  const resultado: number[] = [];
  let i = 0, j = 0;
  while (i < esq.length && j < dir.length) {
    if (esq[i] <= dir[j]) resultado.push(esq[i++]);
    else resultado.push(dir[j++]);
  }
  return [...resultado, ...esq.slice(i), ...dir.slice(j)];
}
```

### Counting Sort (Nao-baseado em comparacao)

```python
def counting_sort(arr: list[int]) -> list[int]:
    if not arr:
        return arr
    max_val = max(arr)
    min_val = min(arr)
    intervalo = max_val - min_val + 1
    contagem = [0] * intervalo
    for num in arr:
        contagem[num - min_val] += 1
    resultado = []
    for i, c in enumerate(contagem):
        resultado.extend([i + min_val] * c)
    return resultado
    # O(n + k) onde k e o intervalo de valores
```

## Algoritmos de Grafos

### Dijkstra (Caminho Mais Curto)

```python
import heapq

def dijkstra(grafo: dict, inicio: str) -> dict[str, float]:
    distancias = {no: float('inf') for no in grafo}
    distancias[inicio] = 0
    fila = [(0, inicio)]
    visitados = set()

    while fila:
        dist_atual, no_atual = heapq.heappop(fila)
        if no_atual in visitados:
            continue
        visitados.add(no_atual)

        for vizinho, peso in grafo[no_atual].items():
            nova_dist = dist_atual + peso
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                heapq.heappush(fila, (nova_dist, vizinho))

    return distancias
    # O((V + E) log V) com heap binario
```

```typescript
// Bellman-Ford (suporta pesos negativos)
function bellmanFord(
  grafo: Map<string, Map<string, number>>,
  inicio: string
): Map<string, number> | null {
  const nos = Array.from(grafo.keys());
  const dist: Map<string, number> = new Map();
  for (const no of nos) dist.set(no, Infinity);
  dist.set(inicio, 0);

  for (let i = 0; i < nos.length - 1; i++) {
    for (const u of nos) {
      for (const [v, peso] of grafo.get(u) || []) {
        if (dist.get(u)! + peso < dist.get(v)!) {
          dist.set(v, dist.get(u)! + peso);
        }
      }
    }
  }

  // Verificar ciclo negativo
  for (const u of nos) {
    for (const [v, peso] of grafo.get(u) || []) {
      if (dist.get(u)! + peso < dist.get(v)!) {
        return null; // ciclo negativo detectado
      }
    }
  }
  return dist;
}
```

### Kruskal - Minimum Spanning Tree

```python
class UnionFind:
    def __init__(self, n):
        self.pai = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.find(self.pai[x])  # path compression
        return self.pai[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.pai[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

def kruskal(arestas: list[tuple[int, int, int]], n: int) -> list[tuple[int, int, int]]:
    arestas.sort(key=lambda x: x[2])  # ordenar por peso
    uf = UnionFind(n)
    mst = []
    for u, v, peso in arestas:
        if uf.union(u, v):
            mst.append((u, v, peso))
            if len(mst) == n - 1:
                break
    return mst
    # O(E log E) para ordenacao das arestas
```

### Ordenacao Topologica

```python
from collections import deque

def ordenacao_topologica(grafo: dict) -> list:
    grau_entrada = {no: 0 for no in grafo}
    for no in grafo:
        for vizinho in grafo[no]:
            grau_entrada[vizinho] += 1

    fila = deque([no for no in grafo if grau_entrada[no] == 0])
    ordem = []

    while fila:
        no = fila.popleft()
        ordem.append(no)
        for vizinho in grafo[no]:
            grau_entrada[vizinho] -= 1
            if grau_entrada[vizinho] == 0:
                fila.append(vizinho)

    if len(ordem) != len(grafo):
        raise ValueError("Grafo contem ciclo - ordenacao topologica impossivel")
    return ordem
    # O(V + E) - Kahn's algorithm
```

## Programacao Dinamica

### Memoization vs Tabulacao

```
Memoization (Top-Down):        Tabulacao (Bottom-Up):
fib(5)                         dp[0]=0, dp[1]=1
├── fib(4)                     dp[2] = dp[1]+dp[0] = 1
│   ├── fib(3)                 dp[3] = dp[2]+dp[1] = 2
│   │   ├── fib(2)             dp[4] = dp[3]+dp[2] = 3
│   │   │   ├── fib(1) -> 1    dp[5] = dp[4]+dp[3] = 5
│   │   │   └── fib(0) -> 0
│   │   └── fib(1) -> 1 (cache)
│   └── fib(2) -> 1 (cache)
└── fib(3) -> 2 (cache)
```

```python
# Fibonacci - Memoization
def fib_memo(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# Fibonacci - Tabulacao
def fib_tab(n: int) -> int:
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Fibonacci - Otimizacao de espaco O(1)
def fib_opt(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### Mochila 0/1 (Knapsack)

```python
def mochila(pesos: list[int], valores: list[int], capacidade: int) -> int:
    n = len(pesos)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], valores[i - 1] + dp[i - 1][w - pesos[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidade]
    # O(n * capacidade) tempo, O(n * capacidade) espaco
```

```typescript
// Longest Common Subsequence (LCS)
function lcs(s1: string, s2: string): number {
  const m = s1.length, n = s2.length;
  const dp: number[][] = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (s1[i - 1] === s2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
      } else {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }
  return dp[m][n];
}
```

### Distancia de Edicao (Levenshtein)

```python
def distancia_edicao(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # delecao
                                   dp[i][j - 1],      # insercao
                                   dp[i - 1][j - 1])  # substituicao
    return dp[m][n]
```

## Algoritmos Gananciosos (Greedy)

### Selecao de Atividades

```python
def selecao_atividades(inicios: list[int], fins: list[int]) -> list[int]:
    atividades = sorted(zip(inicios, fins), key=lambda x: x[1])
    selecionadas = [0]
    ultimo_fim = atividades[0][1]

    for i in range(1, len(atividades)):
        if atividades[i][0] >= ultimo_fim:
            selecionadas.append(i)
            ultimo_fim = atividades[i][1]
    return selecionadas
    # Funciona porque: subestrutura otima + propriedade de escolha gananciosa
```

```typescript
// Interval Scheduling Maximization
interface Intervalo { inicio: number; fim: number; id: string; }

function maxIntervalos(intervalos: Intervalo[]): Intervalo[] {
  intervalos.sort((a, b) => a.fim - b.fim);
  const resultado: Intervalo[] = [];
  let ultimoFim = -Infinity;

  for (const intervalo of intervalos) {
    if (intervalo.inicio >= ultimoFim) {
      resultado.push(intervalo);
      ultimoFim = intervalo.fim;
    }
  }
  return resultado;
}
```

## Algoritmos de Strings

### KMP (Knuth-Morris-Pratt)

```python
def kmp_build_table(padrao: str) -> list[int]:
    m = len(padrao)
    tabela = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and padrao[i] != padrao[j]:
            j = tabela[j - 1]
        if padrao[i] == padrao[j]:
            j += 1
        tabela[i] = j
    return tabela

def kmp_search(texto: str, padrao: str) -> list[int]:
    if not padrao:
        return []
    tabela = kmp_build_table(padrao)
    posicoes = []
    j = 0
    for i in range(len(texto)):
        while j > 0 and texto[i] != padrao[j]:
            j = tabela[j - 1]
        if texto[i] == padrao[j]:
            j += 1
        if j == len(padrao):
            posicoes.append(i - len(padrao) + 1)
            j = tabela[j - 1]
    return posicoes
    # O(n + m) tempo, O(m) espaco
```

### Rabin-Karp (Rolling Hash)

```python
def rabin_karp(texto: str, padrao: str, primo=10**9 + 7, base=256) -> list[int]:
    n, m = len(texto), len(padrao)
    if m > n:
        return []

    hash_padrao = 0
    hash_texto = 0
    h = pow(base, m - 1, primo)

    for i in range(m):
        hash_padrao = (hash_padrao * base + ord(padrao[i])) % primo
        hash_texto = (hash_texto * base + ord(texto[i])) % primo

    posicoes = []
    for i in range(n - m + 1):
        if hash_padrao == hash_texto:
            if texto[i:i + m] == padrao:  # verificacao para evitar colisoes
                posicoes.append(i)
        if i < n - m:
            hash_texto = ((hash_texto - ord(texto[i]) * h) * base + ord(texto[i + m])) % primo
            hash_texto = (hash_texto + primo) % primo
    return posicoes
```

## Arvore de Decisao: Qual Estrutura Usar?

```
Precisa de busca rapida por chave?
├── Sim -> Hash Table (O(1) media)
│   └── Precisa de ordenacao? -> Tree Map / BST (O(log n))
└── Nao -> Continue...

Precisa de ordenacao automatica?
├── Sim -> AVL/Red-Black Tree (O(log n))
└── Nao -> Continue...

Precisa de acesso por indice?
├── Sim -> Array/Dynamic Array (O(1))
└── Nao -> Continue...

Precisa de insercoes/remocoes frequentes no meio?
├── Sim -> Linked List (O(1) com referencia)
└── Nao -> Array

Precisa de min/max frequente?
├── Sim -> Heap (O(1) peek, O(log n) insert/delete)
└── Nao -> Array ordenado + busca binaria

Precisa de busca por prefixo?
├── Sim -> Trie (O(m) onde m = tamanho do prefixo)
└── Nao -> Hash Set

Precisa de teste de pertinencia com pouca memoria?
├── Sim -> Bloom Filter (O(k), espaco fixo)
└── Nao -> Hash Set
```

## Implementacoes Built-in

### Python

| Estrutura | Classe Python | Operacoes Principais |
|-----------|--------------|---------------------|
| Array dinamico | `list` | append O(1), pop O(1), insert O(n) |
| Deque | `collections.deque` | append/appendleft/pop/popleft O(1) |
| Hash table | `dict`, `set` | get/set/delete O(1) media |
| Heap | `heapq` | push/pop O(log n), heapify O(n) |
| Counter | `collections.Counter` | contagem de elementos O(n) |
| Default dict | `collections.defaultdict` | dict com valor padrao |
| Named tuple | `collections.namedtuple` | tupla com campos nomeados |
| Ordered dict | `dict` (Python 3.7+) | dict que preserva ordem |

### TypeScript/JavaScript

| Estrutura | Classe/Modo | Operacoes Principais |
|-----------|------------|---------------------|
| Array | `Array<T>` | push/pop O(1), shift/unshift O(n), splice O(n) |
| Map | `Map<K, V>` | get/set/delete O(1), iteracao por ordem de insercao |
| Set | `Set<T>` | add/has/delete O(1) |
| WeakMap | `WeakMap<object, V>` | chaves sao objetos, GC-friendly |
| PriorityQueue | Nao nativo - usar biblioteca ou implementar |

## Referencias Cruzadas

- [[backend]] - Aplicacao de estruturas de dados em sistemas backend
- [[performance]] - Benchmarks e otimizacao de algoritmos
- [[data-engineering/INDEX]] - Estruturas de dados para processamento de dados em larga escala
- [[database]] - B-Trees e estruturas de indexacao
- [[frontend]] - Estruturas de dados para manipulacao de DOM e estado
