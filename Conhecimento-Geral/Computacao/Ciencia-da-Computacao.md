---
title: "Ciência da Computação — Fundamentos Teóricos"
date: 2026-05-16
area: "Computação e Programação"
tags: [computacao, teoria, turing, chomsky, complexidade, p-vs-np, computabilidade]
aliases: ["Fundamentos da Computação", "Computer Science Theory"]
---

# Ciência da Computação — Fundamentos Teóricos

> *"We can only see a short distance ahead, but we can see plenty there that needs to be done."* — Alan Turing (1950)

---

## 1. História da Computação

### 1.1 Precursores Mecânicos

| Ano | Contribuição | Inventor |
|-----|-------------|----------|
| ~100 a.C. | Máquina de Anticítera (primeiro computador analógico) | Gregos antigos |
| 1642 | Pascaline (calculadora mecânica) | Blaise Pascal |
| 1804 | Tear programável (cartões perfurados) | Joseph Jacquard |
| 1822 | Máquina Diferencial | Charles Babbage |
| 1837 | Máquina Analítica (primeiro computador de propósito geral) | Charles Babbage & Ada Lovelace |
| 1843 | Primeiro algoritmo da história (para a Máquina Analítica) | Ada Lovelace |
| 1890 | Tabuladora de cartões perfurados (censo dos EUA) | Herman Hollerith |
| 1936 | Máquina de Turing (fundação teórica) | Alan Turing |
| 1937 | Computador baseado em relés (Model K) | George Stibitz |
| 1941 | Z3 (primeiro computador eletromecânico programável) | Konrad Zuse |
| 1945 | Arquitetura de von Neumann (EDVAC report) | John von Neumann |
| 1948 | Transistor (Bell Labs) | Shockley, Bardeen, Brattain |
| 1958 | Circuito integrado | Jack Kilby |

### 1.2 Alan Turing (1912–1954)

Alan Turing é considerado o pai da ciência da computação teórica e da inteligência artificial. Suas contribuições fundamentais:

- **Máquina de Turing** (1936): modelo abstrato de computação que define o que é computável
- **Tese de Church-Turing**: toda função computável é computável por uma Máquina de Turing
- **Problema da Parada** (Entscheidungsproblem): demonstrou que existem problemas que nenhum algoritmo pode resolver
- **Teste de Turing** (1950): "Can machines think?" — proposta de um teste comportamental para IA
- **Criptoanálise** (Bletchley Park, 1939–1945): quebra do código Enigma nazista

### 1.3 John von Neumann (1903–1957)

Von Neumann formalizou a **arquitetura de computador de programa armazenado** (stored-program), que ainda é a base da maioria dos computadores modernos. Também contribuiu para a teoria dos jogos, autômatos celulares e computação paralela.

### 1.4 Claude Shannon (1916–2001)

Fundou a **teoria da informação** com o artigo *"A Mathematical Theory of Communication"* (1948). Introduziu os conceitos de:
- Entropia da informação (bits)
- Capacidade de canal
- Códigos de correção de erros
- Aplicação da álgebra booleana a circuitos elétricos (sua tese de mestrado de 1937)

```python
import math

def entropia(probabilidades):
    """Calcula a entropia de Shannon em bits."""
    return -sum(p * math.log2(p) for p in probabilidades if p > 0)

# Exemplo: moeda justa vs. viciada
moeda_justa = [0.5, 0.5]
moeda_viciada = [0.9, 0.1]

print(f"Entropia (moeda justa): {entropia(moeda_justa):.2f} bits")      # 1.0
print(f"Entropia (moeda viciada): {entropia(moeda_viciada):.2f} bits")  # 0.47
```

---

## 2. Máquina de Turing e Computabilidade

### 2.1 Definição Formal

Uma **Máquina de Turing (MT)** é uma 7-tupla $M = (Q, \Sigma, \Gamma, \delta, q_0, q_{accept}, q_{reject})$ onde:

- $Q$: conjunto finito de estados
- $\Sigma$: alfabeto de entrada (não contém o símbolo branco $\_$)
- $\Gamma$: alfabeto da fita ($\Sigma \subset \Gamma$, $\_ \in \Gamma$)
- $\delta: Q \times \Gamma \to Q \times \Gamma \times \{L, R\}$: função de transição
- $q_0$: estado inicial
- $q_{accept}$: estado de aceitação
- $q_{reject}$: estado de rejeição ($q_{accept} \ne q_{reject}$)

```python
class TuringMachine:
    """Simulação simplificada de uma Máquina de Turing."""
    def __init__(self, fita_inicial, transicoes, estado_inicial='q0',
                 estado_aceita='accept', estado_rejeita='reject'):
        self.fita = list(fita_inicial) + ['_'] * 100
        self.cabeca = 0
        self.estado = estado_inicial
        self.transicoes = transicoes
        self.estado_aceita = estado_aceita
        self.estado_rejeita = estado_rejeita

    def passo(self):
        simbolo = self.fita[self.cabeca]
        chave = (self.estado, simbolo)
        if chave not in self.transicoes:
            return False
        novo_estado, novo_simbolo, direcao = self.transicoes[chave]
        self.fita[self.cabeca] = novo_simbolo
        self.estado = novo_estado
        self.cabeca += 1 if direcao == 'R' else -1
        if self.cabeca < 0:
            self.cabeca = 0
        return self.estado not in (self.estado_aceita, self.estado_rejeita)

    def executar(self, max_passos=1000):
        for _ in range(max_passos):
            if not self.passo():
                break
        return self.estado == self.estado_aceita

# Exemplo: MT que aceita strings da forma 0^n 1^n
transicoes = {
    ('q0', '0'): ('q1', 'X', 'R'),
    ('q0', 'Y'): ('q3', 'Y', 'R'),
    ('q1', '0'): ('q1', '0', 'R'),
    ('q1', 'Y'): ('q1', 'Y', 'R'),
    ('q1', '1'): ('q2', 'Y', 'L'),
    ('q2', 'Y'): ('q2', 'Y', 'L'),
    ('q2', '0'): ('q2', '0', 'L'),
    ('q2', 'X'): ('q0', 'X', 'R'),
    ('q3', 'Y'): ('q3', 'Y', 'R'),
    ('q3', '_'): ('accept', '_', 'R'),
}

mt = TuringMachine("0011", transicoes)
print(f"Aceita '0011'? {mt.executar()}")  # True
```

### 2.2 Tese de Church-Turing

A **Tese de Church-Turing** afirma que qualquer função que possa ser computada por um algoritmo pode ser computada por uma Máquina de Turing. Equivale dizer que MTs capturam a noção intuitiva de "computabilidade".

**Formulações equivalentes**:
- Cálculo Lambda (Church, 1936)
- Funções Recursivas (Kleene, Gödel)
- Máquina de Turing (Turing, 1936)
- Sistemas de Post (Post, 1936)
- Gramáticas irrestritas (Chomsky, 1956)

### 2.3 Problema da Parada (Halting Problem)

O **Problema da Parada** pergunta: existe um algoritmo $H$ que, dado a descrição de um programa $P$ e uma entrada $I$, decide se $P$ termina (para) quando executado com $I$?

Turing (1936) provou que **não existe tal algoritmo**.

**Prova por contradição**:
1. Suponha que existe $H(P, I)$ que retorna True se $P(I)$ para, False caso contrário.
2. Construa $D(P)$ que chama $H(P, P)$ e entra em loop se $H$ retorna True, ou para se $H$ retorna False.
3. Pergunte: o que $D(D)$ faz? Se $D(D)$ para, então $H(D, D)$ retorna True, mas $D$ entra em loop. Se $D(D)$ não para, $H(D, D)$ retorna False, mas $D$ para. Contradição.

```python
def problema_da_parada(programa, entrada):
    """Simulação conceitual — na prática, isso é indecidível."""
    raise NotImplementedError("O Problema da Parada é indecidível!")

# Exemplo de um problema que DEPENDE da parada
def collatz(n):
    """Conjectura de Collatz: será que isso sempre termina? Ninguém sabe."""
    while n != 1:
        n = 3 * n + 1 if n % 2 else n // 2
    return n  # Desconhece-se se termina para todo n
```

### 2.4 Problemas Indecidíveis Famosos

| Problema | Descrição | Provado por |
|----------|-----------|-------------|
| Halting Problem | Determinar se um programa para | Turing (1936) |
| Entscheidungsproblem | Determinar se uma fórmula lógica é válida | Church, Turing (1936) |
| Décimo Problema de Hilbert | Existência de soluções inteiras para equações diofantinas | Matiyasevich (1970) |
| Problema da Correspondência de Post | Combinar blocos com strings iguais | Post (1946) |
| Equivalência de programas | Dois programas computam a mesma função | Rice (1953) |

---

## 3. Arquitetura de von Neumann

### 3.1 Componentes

A arquitetura proposta por von Neumann (1945, *First Draft of a Report on the EDVAC*) possui quatro componentes principais:

```
┌─────────────────────────────────────────────────────┐
│                    MEMÓRIA                           │
│          (instruções + dados no mesmo espaço)         │
└────────────┬────────────────────────────┬────────────┘
             │                            │
             ▼                            ▼
┌──────────────────────┐    ┌──────────────────────────┐
│   UNIDADE DE CONTROLE │◄──►│   UNIDADE LÓGICO-        │
│   (UC)                 │    │   ARITMÉTICA (ULA)        │
│   • fetch-decode-execute│    │   • +, -, *, /            │
│   • PC, IR              │    │   • AND, OR, NOT          │
└──────────────────────┘    └──────────────────────────┘
             │                            │
             ▼                            ▼
┌─────────────────────────────────────────────────────┐
│                  ENTRADA/SAÍDA                        │
│               (teclado, tela, disco)                  │
└─────────────────────────────────────────────────────┘
```

### 3.2 Ciclo Fetch-Execute

```python
class SimuladorVonNeumann:
    """Simulação minimalista do ciclo fetch-execute."""

    def __init__(self, memoria=None):
        self.PC = 0  # Program Counter
        self.IR = 0  # Instruction Register
        self.AC = 0  # Accumulator
        self.memoria = memoria if memoria else [0] * 256

    def fetch(self):
        """Busca instrução da memória."""
        self.IR = self.memoria[self.PC]
        self.PC += 1

    def decode_execute(self):
        """Decodifica e executa a instrução."""
        opcode = self.IR >> 4
        operando = self.IR & 0x0F

        if opcode == 0x01:    # LOAD
            self.AC = self.memoria[operando]
        elif opcode == 0x02:  # STORE
            self.memoria[operando] = self.AC
        elif opcode == 0x03:  # ADD
            self.AC += self.memoria[operando]
        elif opcode == 0x04:  # SUB
            self.AC -= self.memoria[operando]
        elif opcode == 0x0F:  # HALT
            return False
        return True

    def executar(self):
        rodando = True
        while rodando:
            self.fetch()
            rodando = self.decode_execute()
```

### 3.3 Limitações (Von Neumann Bottleneck)

- **Gargalo de von Neumann**: barramento único entre CPU e memória limita a taxa de transferência de dados
- Instruções e dados compartilham o mesmo barramento, criando contenção
- Arquitetura **Harvard** separa memória de instruções e de dados para resolver parcialmente esse problema

---

## 4. Linguagens Formais e Hierarquia de Chomsky

### 4.1 A Hierarquia (Chomsky, 1956)

A hierarquia de Chomsky classifica as gramáticas formais em **quatro tipos** baseados nas restrições de suas regras de produção:

| Tipo | Nome | Regras $(\alpha \to \beta)$ | Autômato | Linguagem |
|------|------|------------------------------|----------|-----------|
| **Tipo 0** | Gramáticas irrestritas | $\alpha \in V^+, \beta \in V^*$ | Máquina de Turing | Recursivamente enumerável |
| **Tipo 1** | Sensíveis ao contexto | $\alpha A \beta \to \alpha \gamma \beta, \gamma \ne \varepsilon$ | Autômato linearmente limitado (LBA) | Sensível ao contexto |
| **Tipo 2** | Livres de contexto | $A \to \gamma$ | Autômato de pilha (PDA) | Livre de contexto |
| **Tipo 3** | Regulares | $A \to aB \mid a$ | Autômato finito (DFA/NFA) | Regular |

```python
import re
from abc import ABC, abstractmethod

class AutomatoFinito:
    """Autômato finito determinístico (DFA) — Tipo 3."""

    def __init__(self, estados, alfabeto, transicoes, inicial, finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes  # dict: (estado, simbolo) -> estado
        self.estado_atual = inicial
        self.inicial = inicial
        self.finais = set(finais)

    def processar(self, string):
        self.estado_atual = self.inicial
        for simbolo in string:
            chave = (self.estado_atual, simbolo)
            if chave not in self.transicoes:
                return False
            self.estado_atual = self.transicoes[chave]
        return self.estado_atual in self.finais

# DFA que aceita strings binárias terminadas em '01'
dfa = AutomatoFinito(
    estados={'q0', 'q1', 'q2'},
    alfabeto={'0', '1'},
    transicoes={
        ('q0', '0'): 'q1', ('q0', '1'): 'q0',
        ('q1', '0'): 'q1', ('q1', '1'): 'q2',
        ('q2', '0'): 'q1', ('q2', '1'): 'q0',
    },
    inicial='q0',
    finais=['q2']
)

testes = ['01', '101', '0001', '11', '0101']
for t in testes:
    print(f"Aceita '{t}'? {dfa.processar(t)}")
```

```python
class AutomatoDePilha:
    """Autômato de pilha (PDA) simplificado — Tipo 2."""

    def __init__(self, estados, alfabeto, alfabeto_pilha,
                 transicoes, inicial, pilha_inicial, finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.alfabeto_pilha = alfabeto_pilha
        self.transicoes = transicoes
        self.estado = inicial
        self.pilha = [pilha_inicial]
        self.finais = set(finais)

    def processar(self, string):
        for simbolo in string:
            topo = self.pilha[-1] if self.pilha else '_'
            chave = (self.estado, simbolo, topo)
            if chave not in self.transicoes:
                return False
            novo_estado, desempenhar, empilhar = self.transicoes[chave]
            self.estado = novo_estado
            if desempenhar:
                self.pilha.pop()
            if empilhar:
                self.pilha.append(empilhar)
        return self.estado in self.finais

# PDA para a^n b^n (linguagem livre de contexto)
pda = AutomatoDePilha(
    estados={'q0', 'q1'},
    alfabeto={'a', 'b'},
    alfabeto_pilha={'Z', 'A'},
    transicoes={
        ('q0', 'a', 'Z'): ('q0', False, 'A'),   # empilha A
        ('q0', 'a', 'A'): ('q0', False, 'A'),   # empilha mais A
        ('q0', 'b', 'A'): ('q1', True, None),   # desempilha A
        ('q1', 'b', 'A'): ('q1', True, None),   # desempilha mais A
    },
    inicial='q0',
    pilha_inicial='Z',
    finais=['q1']
)

print(f"Aceita 'aabb'? {pda.processar('aabb')}")  # True
print(f"Aceita 'aaabb'? {pda.processar('aaabb')}")  # False
```

### 4.2 Aplicações da Hierarquia de Chomsky

| Tipo | Aplicação | Exemplos |
|------|-----------|----------|
| Tipo 3 (Regular) | Tokenização, expressões regulares, analisadores léxicos | `re` em Python, `flex`, `grep` |
| Tipo 2 (LC) | Parsing sintático, linguagens de programação (quase todas), HTML | `yacc`, `ANTLR`, `lark` |
| Tipo 1 (SC) | Algumas linguagens naturais, verificação de tipos em Haskell | Context-sensitive constraints |
| Tipo 0 (Irrestrita) | Computação geral, transformações Turing-completas | Qualquer linguagem de programação |

### 4.3 Gramáticas Livres de Contexto

Uma **gramática livre de contexto (GLC)** é uma 4-tupla $G = (V, \Sigma, R, S)$:
- $V$: variáveis (não-terminais)
- $\Sigma$: terminais (disjunto de $V$)
- $R$: regras de produção $A \to \alpha$, onde $A \in V$, $\alpha \in (V \cup \Sigma)^*$
- $S$: variável inicial

**Exemplo**: GLC para expressões aritméticas simples

```
E → E + T | T
T → T * F | F  
F → (E) | num
```

```python
# Parsing de expressões aritméticas com lark (gramática LALR)
from lark import Lark, Transformer

gramatica = """
    ?expr: term
         | expr "+" term   -> add
         | expr "-" term   -> sub

    ?term: factor
         | term "*" factor -> mul
         | term "/" factor -> div

    ?factor: NUMBER        -> num
           | "(" expr ")"

    %import common.NUMBER
    %import common.WS
    %ignore WS
"""

class Avaliador(Transformer):
    def num(self, args):
        return float(args[0])
    def add(self, args):
        return args[0] + args[1]
    def sub(self, args):
        return args[0] - args[1]
    def mul(self, args):
        return args[0] * args[1]
    def div(self, args):
        return args[0] / args[1]

parser = Lark(gramatica, parser='lalr', transformer=Avaliador())
print(parser.parse("3 + 4 * (2 - 1)"))  # 7.0
```

---

## 5. Teoria da Computabilidade

### 5.1 Funções Recursivas

A classe das **funções recursivas** é a menor classe que contém:
- **Funções básicas**: zero ($Z(x) = 0$), sucessor ($S(x) = x+1$), projeções ($P_i^n(x_1,...,x_n) = x_i$)
- **Fechada sob**: composição, recursão primitiva, minimização ($\mu$-operator)

**Tese de Church-Turing (versão forte)**: As funções recursivas parciais coincidem exatamente com as funções computáveis por Máquina de Turing.

```python
def recursao_primitiva(base, passo):
    """Retorna função definida por recursão primitiva.
    f(0, x) = base(x)
    f(n+1, x) = passo(n, f(n, x), x)
    """
    def f(n, *x):
        if n == 0:
            return base(*x)
        return passo(n - 1, f(n - 1, *x), *x)
    return f

# Exemplo: fatorial por recursão primitiva
fat_base = lambda: 1
fat_passo = lambda n, acc: (n + 1) * acc
fatorial = recursao_primitiva(fat_base, fat_passo)

# Exemplo: Fibonacci
fib_base = lambda: 0
fib_base2 = lambda: 1  # precisamos de 2 casos base
def fib_rec(n, a, b):
    return a + b

# Implementação direta de Fibonacci (recursão primitiva não trivial)
def fibonacci(n, a=0, b=1):
    return a if n == 0 else fibonacci(n - 1, b, a + b)

print(f"fib(10) = {fibonacci(10)}")  # 55
```

### 5.2 Conjuntos Recursivos e RE

- **Recursivo** (decidível): existe uma MT que sempre para e aceita ou rejeita
- **Recursivamente Enumerável (RE)**: existe uma MT que aceita se a resposta for "sim" (pode loopar para "não")
- **co-RE**: complemento de um conjunto RE

**Relações**:
```
Recursivo = RE ∩ co-RE
Halting Problem ∈ RE \ Recursivo
Complemento do Halting ∈ co-RE \ Recursivo
```

### 5.3 Teorema de Rice

**Teorema de Rice**: Qualquer propriedade não trivial (diferente de "sempre vazio" ou "sempre todos") sobre a **função computada** por um programa é indecidível.

**Consequência**: Não existe algoritmo que decida, dado um programa, se ele:
- Termina para alguma entrada (não trivial)
- Calcula uma função total
- É equivalente a outro programa
- Nunca entra em loop

---

## 6. Complexidade Computacional e P vs NP

### 6.1 Classes de Complexidade

| Classe | Descrição | Exemplo |
|--------|-----------|---------|
| **P** | Problemas decidíveis em tempo polinomial por MT determinística | Ordenação, busca, caminho mínimo |
| **NP** | Problemas cuja solução pode ser **verificada** em tempo polinomial | SAT, clique, caixeiro viajante (decisão) |
| **NP-completo** | Mais difícil dentro de NP; qualquer problema NP reduz-se a ele | SAT (Cook-Levin), 3-SAT, clique, vertex cover |
| **NP-difícil** | Pelo menos tão difícil quanto qualquer problema NP (pode não estar em NP) | Caixeiro viajante (otimização), halting problem |
| **co-NP** | Complemento de problemas em NP | Tautologia (toda atribuição satisfaz) |
| **EXP** | Problemas decidíveis em tempo exponencial | GO (tabuleiro completo), xadrez (n posições) |
| **PSPACE** | Problemas decidíveis com espaço polinomial | QSAT, jogos determinísticos |

### 6.2 O Problema P vs NP

**Pergunta**: $P \stackrel{?}{=} NP$

Isto é: problemas cuja solução pode ser **verificada** rapidamente (NP) também podem ser **resolvidos** rapidamente (P)?

**Status**: Aberto (um dos 7 Problemas do Milênio do Clay Institute, prêmio de $1M)

**Consenso da comunidade**: acredita-se que $P \ne NP$ (pesquisa informal mostra ~90% dos pesquisadores concordam)

```python
# Exemplo: SAT (Satisfiability) — problema NP-completo clássico
# Usando brute-force para verificar (exponencial)

import itertools

def sat_bruteforce(clausulas, n_variaveis):
    """Resolve SAT por busca exaustiva — O(2^n)."""
    for atribuicao in itertools.product([False, True], repeat=n_variaveis):
        satisfaz = True
        for clausula in clausulas:
            # Clausula é uma lista de literais: (var_idx, is_negated)
            valor_clausula = False
            for var_idx, negado in clausula:
                valor = atribuicao[var_idx] ^ negado  # XOR: negado inverte
                valor_clausula = valor_clausula or valor
            if not valor_clausula:
                satisfaz = False
                break
        if satisfaz:
            return atribuicao
    return None

# Exemplo: (x1 ∨ ¬x2) ∧ (¬x1 ∨ x2) — SAT, solução: x1=True, x2=True
clausulas = [
    [(0, False), (1, True)],   # x1 ∨ ¬x2
    [(0, True), (1, False)],   # ¬x1 ∨ x2
]
sol = sat_bruteforce(clausulas, 2)
print(f"SAT? {sol is not None}, solução: {sol}")
```

### 6.3 Reduções Polinomiais

Uma **redução polinomial** $A \le_p B$ significa que o problema $A$ pode ser transformado em $B$ com custo polinomial. Se $B \in P$ e $A \le_p B$, então $A \in P$.

**Cook-Levin Theorem** (1971): SAT é NP-completo — todo problema em NP pode ser reduzido polinomialmente a SAT.

**Cadeia de reduções clássica**:
```
SAT → 3-SAT → Clique → Vertex Cover → Hamiltonian Cycle → TSP
```

### 6.4 Complexidade em Machine Learning

| Conceito | Classe | Descrição |
|----------|--------|-----------|
| PAC Learning | Probabilisticamente Aproximadamente Correto | Modelo de aprendizado com amostras |
| VC Dimension | Medida de capacidade | Complexidade de hipóteses |
| NP-hardness em ML | Treinar certos modelos (e.g., redes neurais com 3 neurônios) é NP-difícil | Teoria de aprendizado computacional |
| Agnositic Learning | Aprender a melhor hipótese em uma classe é NP-difícil em geral | Kearns et al. |

---

## 7. Aplicações para IA e ML

### 7.1 Conexões com Aprendizado

| Tópico da Computação | Aplicação em IA/ML |
|----------------------|--------------------|
| Máquina de Turing Universal | Base teórica para computação de funções de aprendizado |
| Problema da Parada | Impossibilidade de decidir convergência de algoritmos (geral) |
| Hierarquia de Chomsky | Gramáticas para parsing em NLP, limitações de modelos |
| Complexidade P vs NP | Treinamento de certos modelos é NP-difícil |
| No Free Lunch Theorem | Não existe algoritmo universalmente superior |
| VC Dimension | Generalização, overfitting, complexidade de Shattering |

### 7.2 Teoria da Informação e ML

```python
import numpy as np

def divergencia_kl(p, q):
    """Divergência Kullback-Leibler: D_KL(P || Q)."""
    p = np.array(p, dtype=float)
    q = np.array(q, dtype=float)
    return np.sum(p * np.log2(p / q))  # nats se usar np.log

def entropia_cruzada(p, q):
    """Cross-entropy: H(p, q) = H(p) + D_KL(p || q)."""
    return -np.sum(p * np.log2(q))

# Distribuições verdadeira (p) e prevista (q)
p = [0.7, 0.2, 0.1]
q = [0.6, 0.3, 0.1]

print(f"D_KL(P||Q) = {divergencia_kl(p, q):.4f} bits")
print(f"H(p,q) = {entropia_cruzada(p, q):.4f} bits")
# Cross-entropy é a função de perda padrão para classificação
```

### 7.3 Viés de Indutividade (Inductive Bias)

O **viés de indutividade** é o conjunto de suposições que um algoritmo de aprendizado usa para generalizar além dos dados de treinamento. Sem viés, o aprendizado é impossível (No Free Lunch).

```python
# Diferentes vieses produzem diferentes generalizações
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1.1, 3.8, 9.2, 16.5, 25.1])

# Viés: relação linear (inductive bias = linearidade)
linear = LinearRegression().fit(X, y)
print(f"Linear bias: pred(6) = {linear.predict([[6]])[0]:.2f}")

# Viés: árvore de decisão (inductive bias = segmentação axis-aligned)
tree = DecisionTreeRegressor(max_depth=2).fit(X, y)
print(f"Tree bias: pred(6) = {tree.predict([[6]])[0]:.2f}")
```

### 7.4 Máquinas de Turing e Redes Neurais

Redes neurais recorrentes (RNNs) com pesos racionais e ativações sigmoidais são **Turing-completas** (Siegelmann & Sontag, 1995). Transformers com atenção ilimitada também são Turing-completos (Pérez et al., 2019).

**Limitação prática**: na prática, recursos finitos (memória, tempo) impedem que modelos reais atinjam completude de Turing.

---

## 8. Glossário

| Termo | Definição |
|-------|-----------|
| **Autômato Finito (DFA/NFA)** | Modelo computacional com estados finitos e transições; reconhece linguagens regulares (Tipo 3) |
| **Autômato de Pilha (PDA)** | DFA + pilha; reconhece linguagens livres de contexto (Tipo 2) |
| **Co-NP** | Problemas cujo complemento está em NP |
| **Decidível** | Problema para o qual existe um algoritmo que sempre termina |
| **Entropia (Shannon)** | Medida de incerteza/informação: $H(X) = -\sum p(x) \log_2 p(x)$ |
| **Hierarquia de Chomsky** | Classificação de gramáticas em 4 tipos: regular, LC, sensível-ao-contexto, irrestrita |
| **Indecidível** | Problema para o qual não existe algoritmo (e.g., Halting Problem) |
| **Máquina de Turing Universal** | MT que pode simular qualquer outra MT |
| **NP-completo** | Subclasse de NP: todo problema em NP reduz-se a ele polinomialmente |
| **P vs NP** | Problema aberto: verificação rápida implica solução rápida? |
| **Recursivo** | Conjunto decidível por MT que sempre para |
| **Recursivamente Enumerável (RE)** | Conjunto aceito por MT (pode loopar para "não") |
| **Redução Polinomial** | Transformação de um problema em outro com custo polinomial |
| **Tese de Church-Turing** | Todo computável é computável por MT |
| **VC Dimension** | Medida de complexidade de uma classe de hipóteses |

---

## 9. Referências

### Artigos Fundacionais
- Turing, A. M. (1936). *On Computable Numbers, with an Application to the Entscheidungsproblem*. Proceedings of the London Mathematical Society, 2(42), 230–265.
- Turing, A. M. (1950). *Computing Machinery and Intelligence*. Mind, 59(236), 433–460.
- von Neumann, J. (1945). *First Draft of a Report on the EDVAC*. Moore School of Electrical Engineering.
- Shannon, C. E. (1948). *A Mathematical Theory of Communication*. Bell System Technical Journal, 27, 379–423, 623–656.
- Chomsky, N. (1956). *Three Models for the Description of Language*. IRE Transactions on Information Theory, 2(3), 113–124.
- Cook, S. A. (1971). *The Complexity of Theorem-Proving Procedures*. STOC '71, 151–158.
- Levin, L. (1973). *Universal Search Problems*. Problems of Information Transmission, 9(3), 265–266.
- Hopcroft, J. E. & Ullman, J. D. (1969). *Formal Languages and Their Relation to Automata*. Addison-Wesley.

### Livros-texto
- Sipser, M. (2012). *Introduction to the Theory of Computation* (3ª ed.). Cengage Learning.
- Arora, S. & Barak, B. (2009). *Computational Complexity: A Modern Approach*. Cambridge University Press.
- Hopcroft, J. E., Motwani, R. & Ullman, J. D. (2006). *Introduction to Automata Theory, Languages, and Computation* (3ª ed.). Addison-Wesley.
- Papadimitriou, C. H. (1994). *Computational Complexity*. Addison-Wesley.
- Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill. (Capítulo 7: VC Dimension, PAC Learning)

### Para IA/ML
- Russell, S. & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4ª ed.). Pearson.
- Goodfellow, I., Bengio, Y. & Courville, A. (2016). *Deep Learning*. MIT Press. (Capítulos 1, 4, 5, 6)
- Shalev-Shwartz, S. & Ben-David, S. (2014). *Understanding Machine Learning: From Theory to Algorithms*. Cambridge University Press.

### Conexões com Outras Notas
- [[Conhecimento-Geral/Computacao/NLP-Fundamentos]] — aplicações práticas de linguagens formais e gramáticas
- [[Conhecimento-Geral/Matematica/Teoria-da-Informacao]] — entropia, divergência KL, capacidade de canal
- [[Conhecimento-Geral/Matematica/Probabilidade-e-Estatistica]] — distribuições, inferência, MLE
- [[Conhecimento-Geral/Computacao/Algoritmos-e-Estruturas]] — implementações de algoritmos discutidos teoricamente
- [[Conhecimento-Geral/Linguistica/Linguistica-e-Semiotica]] — linguística estrutural, hierarquia de Chomsky aplicada
