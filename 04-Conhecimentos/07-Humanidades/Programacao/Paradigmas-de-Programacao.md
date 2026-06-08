---
title: "Paradigmas de Programação"
date: 2026-05-16
area: "Programação e Engenharia de Software"
tags: [conhecimento, programacao, paradigmas, oop, funcional]
related: ["04-Conhecimentos/07-Humanidades/Computacao/Ciencia-da-Computacao"]
aliases: ["Programming Paradigms", "OOP", "Functional Programming"]
---

# Paradigmas de Programação

Paradigmas de programação são estilos fundamentais de se escrever código, cada um com sua própria forma de modelar problemas, estruturar dados e organizar fluxos de controle. Compreender múltiplos paradigmas é essencial para escolher a ferramenta certa para cada problema.

## 1. Programação Imperativa vs Declarativa

A divisão mais fundamental entre paradigmas está em **como** o código descreve a solução.

### Programação Imperativa

O programador descreve **passo a passo** como o computador deve executar a tarefa. Foco no **fluxo de controle** e **mutação de estado**.

```python
# Imperativo: como fazer
def soma_pares(numeros):
    resultado = 0
    for i in range(len(numeros)):
        if numeros[i] % 2 == 0:
            resultado += numeros[i]
    return resultado
```

```typescript
// Imperativo: como fazer
function somaPares(numeros: number[]): number {
  let resultado = 0;
  for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] % 2 === 0) {
      resultado += numeros[i];
    }
  }
  return resultado;
}
```

### Programação Declarativa

O programador descreve **o que** deve ser feito, e a execução fica a cargo da linguagem/framework. Foco no **resultado desejado**.

```python
# Declarativa: o que fazer
def soma_pares(numeros):
    return sum(n for n in numeros if n % 2 == 0)
```

```typescript
// Declarativa: o que fazer
const somaPares = (numeros: number[]): number =>
  numeros.filter(n => n % 2 === 0).reduce((a, b) => a + b, 0);
```

SQL é o exemplo clássico de linguagem declarativa: você diz *o que* quer (`SELECT * FROM usuarios WHERE ativo = 1`), não *como* o banco deve buscar.

| Característica | Imperativo | Declarativo |
|---|---|---|
| Controle | Explícito (loops, condicionais) | Implícito (abstraído) |
| Estado | Mutável frequentemente | Imutável ou gerenciado |
| Legibilidade | Passo a passo detalhado | Intenção clara |
| Performance | Controle fino | Otimizado pelo runtime |

---

## 2. Programação Orientada a Objetos (OOP)

Paradigma baseado no conceito de **objetos** que combinam **dados** (atributos) e **comportamento** (métodos). Popularizada por linguagens como Smalltalk, Java, C++ e posteriormente Python e TypeScript.

**Referência:** Gamma, Helm, Johnson, Vlissides. *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley, 1994. (GoF)

### 2.1 Encapsulamento

Protege os dados internos de um objeto, expondo apenas uma interface controlada.

```python
class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self._titular = titular
        self.__saldo = saldo_inicial  # Privado por name mangling

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        self.__saldo += valor

    def sacar(self, valor: float) -> bool:
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False

    @property
    def saldo(self) -> float:
        return self.__saldo
```

```typescript
class ContaBancaria {
  private _saldo: number;

  constructor(
    private readonly _titular: string,
    saldoInicial: number = 0
  ) {
    this._saldo = saldoInicial;
  }

  depositar(valor: number): void {
    if (valor <= 0) throw new Error("Valor deve ser positivo");
    this._saldo += valor;
  }

  sacar(valor: number): boolean {
    if (valor > 0 && valor <= this._saldo) {
      this._saldo -= valor;
      return true;
    }
    return false;
  }

  get saldo(): number {
    return this._saldo;
  }
}
```

### 2.2 Herança

Permite que uma classe derive de outra, reutilizando e estendendo comportamento.

```python
class Animal:
    def __init__(self, nome: str):
        self.nome = nome

    def emitir_som(self) -> str:
        return "..."

class Cachorro(Animal):
    def emitir_som(self) -> str:
        return "Au au!"

class Gato(Animal):
    def emitir_som(self) -> str:
        return "Miau!"
```

```typescript
abstract class Animal {
  constructor(protected readonly nome: string) {}

  abstract emitirSom(): string;
}

class Cachorro extends Animal {
  emitirSom(): string {
    return "Au au!";
  }
}

class Gato extends Animal {
  emitirSom(): string {
    return "Miau!";
  }
}
```

**Cuidado:** Herança excessiva leva ao *Fragile Base Class Problem*. Prefira **composição** sobre herança (GoF).

### 2.3 Polimorfismo

Capacidade de objetos de diferentes classes responderem à mesma mensagem de formas distintas.

```python
def fazer_som(animal: Animal) -> None:
    print(animal.emitir_som())

fazer_som(Cachorro("Rex"))  # Au au!
fazer_som(Gato("Mimi"))     # Miau!
```

```typescript
function fazerSom(animal: Animal): void {
  console.log(animal.emitirSom());
}
```

### 2.4 Composição

Montar objetos complexos combinando objetos mais simples. Prefira composição à herança (GoF, Item 18 de *Effective Java*).

```python
class Motor:
    def ligar(self) -> str:
        return "Motor ligado"

class Carro:
    def __init__(self):
        self._motor = Motor()  # Composição

    def ligar(self) -> str:
        return self._motor.ligar()
```

```typescript
class Motor {
  ligar(): string {
    return "Motor ligado";
  }
}

class Carro {
  private readonly motor = new Motor();

  ligar(): string {
    return this.motor.ligar();
  }
}
```

### 2.5 SOLID em OOP (visão geral)

| Princípio | Significado |
|---|---|
| **S**ingle Responsibility | Uma classe, uma razão para mudar |
| **O**pen/Closed | Aberta para extensão, fechada para modificação |
| **L**iskov Substitution | Subtipos devem substituir seus tipos base |
| **I**nterface Segregation | Interfaces específicas > interface genérica |
| **D**ependency Inversion | Dependa de abstrações, não de concreções |

Detalhado em [[04-Conhecimentos/07-Humanidades/Programacao/Arquitetura-de-Software]].

---

## 3. Programação Funcional

Paradigma baseado em **funções matemáticas** e **imutabilidade**. Evita estado compartilhado e efeitos colaterais. Inspirado no cálculo lambda (Alonzo Church, 1930s).

**Referência:** Bird, Richard. *Thinking Functionally with Haskell*. Cambridge University Press, 2014.

### 3.1 Imutabilidade

Dados nunca são modificados após criados; operações produzem novos dados.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Pedido:
    itens: tuple[str, ...]
    total: float

    def adicionar_item(self, item: str, preco: float) -> "Pedido":
        return Pedido(
            itens=self.itens + (item,),
            total=self.total + preco
        )
```

```typescript
interface Pedido {
  readonly itens: readonly string[];
  readonly total: number;
}

function adicionarItem(pedido: Pedido, item: string, preco: number): Pedido {
  return {
    itens: [...pedido.itens, item],
    total: pedido.total + preco,
  };
}
```

### 3.2 Funções Puras

Uma função pura: (1) dado o mesmo input, retorna sempre o mesmo output; (2) não causa efeitos colaterais.

```python
# Pura
def somar(a: int, b: int) -> int:
    return a + b

# Impura (efeito colateral: I/O)
def logar_soma(a: int, b: int) -> int:
    resultado = a + b
    print(f"Soma: {resultado}")  # Side effect!
    return resultado

# Impura (mutação de estado global)
contador = 0
def incrementar() -> int:
    global contador
    contador += 1
    return contador
```

```typescript
// Pura
function somar(a: number, b: number): number {
  return a + b;
}

// Impura
let contador = 0;
function incrementar(): number {
  return ++contador;
}
```

### 3.3 Funções de Alta Ordem (Higher-Order Functions)

Funções que recebem ou retornam outras funções.

```python
def aplicar_tres_vezes(funcao, valor):
    return funcao(funcao(funcao(valor)))

resultado = aplicar_tres_vezes(lambda x: x * 2, 1)  # 8
```

```typescript
function aplicarTresVezes<T>(fn: (x: T) => T, valor: T): T {
  return fn(fn(fn(valor)));
}

const resultado = aplicarTresVezes((x: number) => x * 2, 1); // 8
```

### 3.4 Currying

Transformar uma função de múltiplos argumentos em uma sequência de funções de um argumento.

```python
from functools import partial

def somar(a: int, b: int) -> int:
    return a + b

somar_curried = lambda a: lambda b: a + b
somar_5 = somar_curried(5)
print(somar_5(3))  # 8

# Versão com partial
def somar(a: int, b: int, c: int) -> int:
    return a + b + c

somar_1_2 = partial(somar, 1, 2)
print(somar_1_2(3))  # 6
```

```typescript
// Currying manual
const somar = (a: number) => (b: number) => a + b;
const somar5 = somar(5);
console.log(somar5(3)); // 8

// Curry genérico (versão simplificada)
function curry<T extends unknown[], R>(
  fn: (...args: T) => R
): (...args: Partial<T>) => any {
  return (...args: any[]) =>
    args.length >= fn.length
      ? fn(...(args as T))
      : curry(fn.bind(null, ...args));
}
```

### 3.5 Functors e Monads

**Functor:** Um tipo que implementa `map` (ou `fmap`), permitindo aplicar uma função ao valor encapsulado.

```python
from typing import TypeVar, Generic, Callable

A = TypeVar("A")
B = TypeVar("B")

class Maybe(Generic[A]):
    def __init__(self, valor: A | None):
        self._valor = valor

    def map(self, fn: Callable[[A], B]) -> "Maybe[B]":
        if self._valor is None:
            return Maybe(None)
        return Maybe(fn(self._valor))

    def bind(self, fn: Callable[[A], "Maybe[B]"]) -> "Maybe[B]":
        if self._valor is None:
            return Maybe(None)
        return fn(self._valor)

    def get_or_else(self, default: B) -> A | B:
        return self._valor if self._valor is not None else default

# Uso
Maybe(10).map(lambda x: x * 2).get_or_else(0)  # 20
Maybe(None).map(lambda x: x * 2).get_or_else(0)  # 0
```

```typescript
type Maybe<T> = { kind: "some"; value: T } | { kind: "none" };

function map<T, U>(maybe: Maybe<T>, fn: (x: T) => U): Maybe<U> {
  switch (maybe.kind) {
    case "some":
      return { kind: "some", value: fn(maybe.value) };
    case "none":
      return { kind: "none" };
  }
}

function bind<T, U>(maybe: Maybe<T>, fn: (x: T) => Maybe<U>): Maybe<U> {
  switch (maybe.kind) {
    case "some":
      return fn(maybe.value);
    case "none":
      return { kind: "none" };
  }
}

function of<T>(value: T): Maybe<T> {
  return { kind: "some", value };
}

const result = map(of(10), (x) => x * 2); // { kind: "some", value: 20 }
```

**Monad:** Um functor que implementa `bind` (ou `flatMap`, `>>=`), permitindo composição de operações monádicas. Exemplos clássicos: `Maybe` (option), `Either`, `Promise`/`Task`, `List`.

```python
from typing import TypeVar, Generic, Callable

E = TypeVar("E")
A = TypeVar("A")
B = TypeVar("B")

class Either(Generic[E, A]):
    """Monad Either: Left (erro) ou Right (sucesso)."""

    def __init__(self, is_left: bool, erro: E | None, valor: A | None):
        self._is_left = is_left
        self._erro = erro
        self._valor = valor

    @classmethod
    def success(cls, valor: A) -> "Either[E, A]":
        return cls(False, None, valor)

    @classmethod
    def failure(cls, erro: E) -> "Either[E, A]":
        return cls(True, erro, None)

    def map(self, fn: Callable[[A], B]) -> "Either[E, B]":
        if self._is_left:
            return Either.failure(self._erro)
        return Either.success(fn(self._valor))

    def bind(self, fn: Callable[[A], "Either[E, B]"]) -> "Either[E, B]":
        if self._is_left:
            return Either.failure(self._erro)
        return fn(self._valor)

    def __repr__(self) -> str:
        if self._is_left:
            return f"Left({self._erro})"
        return f"Right({self._valor})"

# Pipeline monádico
def dividir(a: float, b: float) -> Either[str, float]:
    if b == 0:
        return Either.failure("Divisão por zero")
    return Either.success(a / b)

def raiz_quadrada(x: float) -> Either[str, float]:
    if x < 0:
        return Either.failure("Raiz de número negativo")
    return Either.success(x ** 0.5)

resultado = (
    Either.success(16)
    .bind(lambda x: dividir(x, 2))
    .bind(lambda x: raiz_quadrada(x))
)
print(resultado)  # Right(2.828...)
```

```typescript
type Either<E, A> =
  | { kind: "left"; error: E }
  | { kind: "right"; value: A };

function success<E, A>(value: A): Either<E, A> {
  return { kind: "right", value };
}

function failure<E, A>(error: E): Either<E, A> {
  return { kind: "left", error };
}

function bind<E, A, B>(
  either: Either<E, A>,
  fn: (x: A) => Either<E, B>
): Either<E, B> {
  switch (either.kind) {
    case "left":
      return either as unknown as Either<E, B>;
    case "right":
      return fn(either.value);
  }
}

function dividir(a: number, b: number): Either<string, number> {
  return b === 0
    ? failure("Divisão por zero")
    : success(a / b);
}

function raizQuadrada(x: number): Either<string, number> {
  return x < 0
    ? failure("Raiz de número negativo")
    : success(Math.sqrt(x));
}

const resultado = bind(
  bind(success(16), (x) => dividir(x, 2)),
  (x) => raizQuadrada(x)
); // { kind: "right", value: 2.828... }
```

### 3.6 Pattern Matching

Poderoso recurso funcional para desestruturar e ramificar baseado em tipos/estruturas.

```python
# Python 3.10+ match/case (structural pattern matching)
from typing import Union

Forma = Union[tuple[str, float], tuple[str, float, float]]

def area(forma: Forma) -> float:
    match forma:
        case ("circulo", raio):
            return 3.14159 * raio ** 2
        case ("retangulo", largura, altura):
            return largura * altura
        case _:
            raise ValueError("Forma desconhecida")

print(area(("circulo", 5.0)))       # 78.53975
print(area(("retangulo", 3.0, 4.0))) # 12.0
```

```typescript
type Forma =
  | { tipo: "circulo"; raio: number }
  | { tipo: "retangulo"; largura: number; altura: number };

function area(forma: Forma): number {
  switch (forma.tipo) {
    case "circulo":
      return Math.PI * forma.raio ** 2;
    case "retangulo":
      return forma.largura * forma.altura;
  }
}
```

---

## 4. Programação Procedural

Paradigma que organiza o código em **procedimentos** (funções/sub-rotinas). É uma evolução da programação linear, focada em **decomposição funcional**. Linguagens típicas: C, Pascal, COBOL.

Embora considerado mais "primitivo" que OOP, o paradigma procedural ainda é extremamente relevante em sistemas embarcados, kernels e algoritmos de alto desempenho.

```c
// C: Exemplo procedural
#include <stdio.h>

int fatorial(int n) {
    if (n <= 1) return 1;
    return n * fatorial(n - 1);
}

int main() {
    int n = 5;
    printf("Fatorial de %d = %d\n", n, fatorial(n));
    return 0;
}
```

```python
# Python procedural style
def fatorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

def main() -> None:
    n = 5
    print(f"Fatorial de {n} = {fatorial(n)}")

if __name__ == "__main__":
    main()
```

```typescript
// TypeScript procedural (evitando classes)
function fatorial(n: number): number {
  if (n <= 1) return 1;
  return n * fatorial(n - 1);
}

function main(): void {
  const n = 5;
  console.log(`Fatorial de ${n} = ${fatorial(n)}`);
}

main();
```

---

## 5. Programação Lógica

Paradigma baseado em **lógica formal** e **inferência**. O programador define fatos e regras, e o motor de inferência deriva conclusões. Linguagem principal: Prolog.

**Referência:** Clocksin, William F.; Mellish, Christopher S. *Programming in Prolog*. Springer, 2003.

```prolog
% Fatos
humano(socrates).
humano(platao).
mortal(X) :- humano(X).

% Consulta: mortal(socrates). -> true
% Consulta: mortal(zeus). -> false

% Listas e recursão
membro(X, [X|_]).
membro(X, [_|T]) :- membro(X, T).

% Consulta: membro(3, [1,2,3,4]). -> true
```

```python
# Simulação de programação lógica em Python
class BaseConhecimento:
    def __init__(self):
        self.fatos = set()
        self.regras = []

    def adicionar_fato(self, fato: tuple):
        self.fatos.add(fato)

    def adicionar_regra(self, consequencia, antecedentes):
        self.regras.append((consequencia, antecedentes))

    def consultar(self, objetivo, bindings=None) -> list[dict]:
        if bindings is None:
            bindings = {}

        # Verificar fatos
        for fato in self.fatos:
            unificador = self._unificar(objetivo, fato, bindings)
            if unificador is not None:
                return [unificador]

        # Verificar regras
        for consequencia, antecedentes in self.regras:
            unificador = self._unificar(objetivo, consequencia, bindings)
            if unificador is not None:
                resultados = [[]]
                for ant in antecedentes:
                    novos = []
                    for res in resultados:
                        for sol in self.consultar(ant, {**bindings, **res}):
                            novos.append({**res, **sol})
                    resultados = novos
                if resultados:
                    return resultados
        return []

    def _unificar(self, a, b, bindings):
        # Simplificação: verifica igualdade
        if a == b:
            return bindings
        return None

# Uso
bc = BaseConhecimento()
bc.adicionar_fato(("humano", "socrates"))
bc.adicionar_regra(("mortal", "X"), [("humano", "X")])

print(bc.consultar(("mortal", "socrates")))  # [{}]
```

---

## 6. Programação Concorrente

Paradigma que lida com múltiplas unidades de execução simultâneas. Dois modelos principais:

### 6.1 Actor Model

Atores são unidades fundamentais de computação que se comunicam exclusivamente via **mensagens assíncronas**. Cada ator tem um mailbox e processa uma mensagem por vez. Popularizado por Erlang/OTP e Akka.

**Referência:** Hewitt, Carl; Bishop, Peter; Steiger, Richard. "A Universal Modular ACTOR Formalism for Artificial Intelligence". IJCAI, 1973.

```python
# Actor Model simplificado em Python
from dataclasses import dataclass
from queue import Queue
from typing import Protocol

@dataclass
class Mensagem:
    tipo: str
    dados: dict

class Ator(Protocol):
    def receber(self, msg: Mensagem) -> None: ...

class Mailbox:
    def __init__(self):
        self._fila: Queue[Mensagem] = Queue()

    def enviar(self, msg: Mensagem):
        self._fila.put(msg)

    def processar(self, ator: Ator):
        while not self._fila.empty():
            msg = self._fila.get()
            ator.receber(msg)

class ContadorAtor:
    def __init__(self):
        self._contagem = 0
        self._mailbox = Mailbox()

    @property
    def mailbox(self) -> Mailbox:
        return self._mailbox

    def receber(self, msg: Mensagem) -> None:
        if msg.tipo == "incrementar":
            self._contagem += msg.dados.get("valor", 1)
        elif msg.tipo == "consultar":
            print(f"Contagem atual: {self._contagem}")

ator = ContadorAtor()
ator.mailbox.enviar(Mensagem("incrementar", {"valor": 5}))
ator.mailbox.enviar(Mensagem("consultar", {}))
ator.mailbox.processar(ator)  # Contagem atual: 5
```

```typescript
// Actor Model simplificado em TypeScript
interface Mensagem {
  tipo: string;
  dados: Record<string, unknown>;
}

class Mailbox {
  private fila: Mensagem[] = [];

  enviar(msg: Mensagem): void {
    this.fila.push(msg);
  }

  processar(ator: Ator): void {
    while (this.fila.length > 0) {
      const msg = this.fila.shift()!;
      ator.receber(msg);
    }
  }
}

abstract class Ator {
  protected mailbox = new Mailbox();

  abstract receber(msg: Mensagem): void;

  getMailbox(): Mailbox {
    return this.mailbox;
  }
}

class ContadorAtor extends Ator {
  private contagem = 0;

  receber(msg: Mensagem): void {
    switch (msg.tipo) {
      case "incrementar":
        this.contagem += (msg.dados.valor as number) ?? 1;
        break;
      case "consultar":
        console.log(`Contagem atual: ${this.contagem}`);
        break;
    }
  }
}

const ator = new ContadorAtor();
ator.getMailbox().enviar({ tipo: "incrementar", dados: { valor: 5 } });
ator.getMailbox().enviar({ tipo: "consultar", dados: {} });
ator.getMailbox().processar(ator); // Contagem atual: 5
```

### 6.2 CSP (Communicating Sequential Processes)

Modelo onde processos concorrentes se comunicam via **canais** com operações de send/receive bloqueantes. Popularizado por Go (goroutines + channels) e Clojure (core.async).

**Referência:** Hoare, C. A. R. "Communicating Sequential Processes". Communications of the ACM, 1978.

```python
# CSP-style com asyncio + queues
import asyncio

async def produtor(channel: asyncio.Queue[int]):
    for i in range(5):
        await channel.put(i)
        print(f"Produziu: {i}")
        await asyncio.sleep(0.1)
    await channel.put(None)  # Sinal de fim

async consumidor(channel: asyncio.Queue[int | None]):
    while True:
        item = await channel.get()
        if item is None:
            break
        print(f"Consumiu: {item}")
        channel.task_done()

async def main():
    channel: asyncio.Queue[int | None] = asyncio.Queue()
    await asyncio.gather(
        produtor(channel),
        consumidor(channel)
    )

asyncio.run(main())
```

```typescript
// CSP-style com promises e canais
class Channel<T> {
  private fila: T[] = [];
  private waiters: ((value: T) => void)[] = [];

  async send(value: T): Promise<void> {
    if (this.waiters.length > 0) {
      const waiter = this.waiters.shift()!;
      waiter(value);
    } else {
      this.fila.push(value);
    }
  }

  async receive(): Promise<T> {
    if (this.fila.length > 0) {
      return this.fila.shift()!;
    }
    return new Promise((resolve) => {
      this.waiters.push(resolve);
    });
  }
}

async function produtor(channel: Channel<number | null>) {
  for (let i = 0; i < 5; i++) {
    await channel.send(i);
    console.log(`Produziu: ${i}`);
  }
  await channel.send(null);
}

async function consumidor(channel: Channel<number | null>) {
  while (true) {
    const item = await channel.receive();
    if (item === null) break;
    console.log(`Consumiu: ${item}`);
  }
}

async function main() {
  const channel = new Channel<number | null>();
  await Promise.all([produtor(channel), consumidor(channel)]);
}
```

---

## 7. Programação Concorrente: Threads e Locks

Modelo clássico de concorrência com **memória compartilhada** e **sincronização** via locks, semáforos e monitores.

```python
import threading
import time

class ContadorCompartilhado:
    def __init__(self):
        self._valor = 0
        self._lock = threading.Lock()

    def incrementar(self):
        with self._lock:
            atual = self._valor
            time.sleep(0.001)  # Simula trabalho
            self._valor = atual + 1

    @property
    def valor(self) -> int:
        return self._valor

contador = ContadorCompartilhado()
threads = [threading.Thread(target=contador.incrementar) for _ in range(10)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(contador.valor)  # 10 (graças ao lock)
```

```typescript
// No Node.js, threads são Worker Threads
import { Worker, isMainThread, parentPort, workerData } from "worker_threads";

if (isMainThread) {
  const workers: Worker[] = [];
  for (let i = 0; i < 10; i++) {
    const worker = new Worker(__filename, { workerData: { id: i } });
    workers.push(worker);
  }
} else {
  // Worker executa trabalho isolado (memória não compartilhada)
  console.log(`Worker ${workerData.id} executando`);
}
```

---

## 8. Comparação e Trade-offs

| Paradigma | Pontos Fortes | Pontos Fracos | Quando Usar |
|---|---|---|---|
| **Imperativo** | Performance, controle fino, previsível | Verboso, difícil de paralelizar | Sistemas embarcados, kernels, jogos |
| **Declarativo** | Expressivo, conciso, fácil de entender | Performance pode ser opaca | Queries SQL, pipelines de dados, HTML/CSS |
| **OOP** | Modelagem do mundo real, encapsulamento, reuso | Complexidade acidental, acoplamento | Sistemas empresariais, GUIs, jogos |
| **Funcional** | Imutabilidade, testabilidade, paralelismo | Curva de aprendizado, performance em alguns casos | Processamento de dados, sistemas concorrentes, análise |
| **Lógico** | Inferência automática, elegante | Escalabilidade, problemas práticos | Sistemas especialistas, busca, linguística |
| **Procedural** | Simples, eficiente, previsível | Dificuldade em sistemas grandes | Scripts, algoritmos, sistemas de baixo nível |
| **Concorrente (Actors)** | Isolamento, tolerância a falhas | Debugging complexo | Sistemas distribuídos, telco, IoT |
| **Concorrente (CSP)** | Sincronização elegante | Deadlock potencial | Pipelines, workers |

### 8.1 Paradigmas não são mutuamente exclusivos

Linguagens modernas são **multiparadigma**:

- **Python**: OOP + funcional + procedural
- **TypeScript**: OOP + funcional (com tipagem)
- **Scala**: OOP + funcional (puro no JVM)
- **Kotlin**: OOP + funcional
- **Rust**: procedural + funcional + concorrente segura
- **Go**: procedural + CSP

```python
# Python multiparadigma
from dataclasses import dataclass
from typing import Callable

# OOP
@dataclass
class Transacao:
    valor: float
    tipo: str

# Funcional
def aplicar_taxa(transacao: Transacao) -> Transacao:
    return Transacao(
        valor=transacao.valor * 1.1,
        tipo=transacao.tipo
    )

# Pipeline funcional + OOP
transacoes = [Transacao(100, "credito"), Transacao(200, "debito")]
taxadas = list(map(aplicar_taxa, transacoes))
```

```typescript
// TypeScript multiparadigma
interface Transacao {
  valor: number;
  tipo: "credito" | "debito";
}

// Funcional
const aplicarTaxa = (t: Transacao): Transacao => ({
  ...t,
  valor: t.valor * 1.1,
});

// Pipeline
const transacoes: Transacao[] = [
  { valor: 100, tipo: "credito" },
  { valor: 200, tipo: "debito" },
];
const taxadas = transacoes.map(aplicarTaxa);
```

---

## 9. Referências Bibliográficas

- Gamma, E.; Helm, R.; Johnson, R.; Vlissides, J. *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley, 1994.
- Martin, R. C. *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall, 2017.
- Bird, R. *Thinking Functionally with Haskell*. Cambridge University Press, 2014.
- Clocksin, W. F.; Mellish, C. S. *Programming in Prolog*. Springer, 2003.
- Hewitt, C.; Bishop, P.; Steiger, R. "A Universal Modular ACTOR Formalism for Artificial Intelligence". IJCAI, 1973.
- Hoare, C. A. R. "Communicating Sequential Processes". Communications of the ACM, 1978.
- Evans, E. *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley, 2003.
- Armstrong, J. *Programming Erlang: Software for a Concurrent World*. Pragmatic Bookshelf, 2007.

## Ver Também

- [[04-Conhecimentos/07-Humanidades/Computacao/Ciencia-da-Computacao]]
- [[04-Conhecimentos/07-Humanidades/Programacao/Arquitetura-de-Software]]
- [[04-Conhecimentos/07-Humanidades/Programacao/Design-Patterns]]
- [[05-Skills/skills/02-software-engineering/advanced-backend-architecture]]
