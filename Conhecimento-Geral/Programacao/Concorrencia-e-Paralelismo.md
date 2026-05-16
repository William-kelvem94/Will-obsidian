---
title: "Concorrência e Paralelismo"
date: 2026-05-16
area: "Programação e Engenharia de Software"
tags: [conhecimento, programacao, concorrencia, paralelismo, async, threads]
related: ["Conhecimento-Geral/Programacao/Performance-e-Otimizacao"]
aliases: ["Concurrency", "Parallelism", "Async", "Multithreading"]
---

## Visão Geral

**Concorrência** é a composição de tarefas que podem progredir de forma independente (lógica). **Paralelismo** é a execução simultânea de múltiplas tarefas (física). Concorrência permite estruturar problemas; paralelismo permite acelerá-los.

```
Concorrência:  |A|A|B|A|B|B|C|  (interleaving)
Paralelismo:   |A|A|A|          (simultâneo)
               |B|B|B|
               |C|C|C|
```

## Threads vs Processes vs Async

```python
import threading
import multiprocessing
import asyncio
import time

# Thread — concorrência, compartilha memória (GIL limita CPU)
def tarefa_thread(nome):
    for i in range(3):
        print(f"Thread {nome}: {i}")
        time.sleep(0.1)

threads = [threading.Thread(target=tarefa_thread, args=(f"T{i}",)) for i in range(3)]
[t.start() for t in threads]
[t.join() for t in threads]

# Process — paralelismo real, memória separada
def tarefa_processo(nome):
    return sum(i * i for i in range(10_000_000))

with multiprocessing.Pool(4) as pool:
    resultados = pool.map(tarefa_processo, range(4))

# Async — concorrência cooperativa (single-thread)
async def tarefa_async(nome):
    for i in range(3):
        print(f"Async {nome}: {i}")
        await asyncio.sleep(0.1)  # cede controle

async def main():
    await asyncio.gather(
        tarefa_async("A"), tarefa_async("B"), tarefa_async("C")
    )

asyncio.run(main())
```

| Característica | Thread | Process | Async |
|---------------|--------|---------|-------|
| Espaço de memória | Compartilhado | Isolado | Compartilhado |
| GIL | Limitado (CPU) | Não afeta | Não afeta |
| Criação | Leve | Pesado | Leve |
| Comunicação | Shared state | Queue/Pipe | Objetos compartilhados |
| Ideal para | I/O bound | CPU bound | I/O bound |
| Overhead | ~50μs/thread | ~500μs/process | ~μs/task |

## GIL (Python)

O Global Interpreter Lock impede que múltiplas threads executem bytecode Python simultaneamente.

```python
import sys
import threading
import time

# GIL ativo — CPU bound não escala com threads
def cpu_intensivo():
    total = 0
    for _ in range(50_000_000):
        total += 1
    return total

# Com threads — NÃO acelera (GIL serializa)
inicio = time.time()
threads = [threading.Thread(target=cpu_intensivo) for _ in range(4)]
[t.start() for t in threads]
[t.join() for t in threads]
print(f"Threads: {time.time() - inicio:.2f}s")  # ~mesmo que serial

# Com multiprocessing — acelera (cada processo tem seu GIL)
with multiprocessing.Pool(4) as pool:
    pool.map(cpu_intensivo, [()]*4)
print(f"Multiprocessing: {time.time() - inicio_real}:.2f}s")

# Alternativas ao GIL:
# - multiprocessing (memória separada)
# - C extensions (numpy, cython) — liberam GIL
# - PyPy — STM (Software Transactional Memory, experimental)
# - Python sem GIL (PEP 703, Python 3.13+ experimental)
```

### Liberando o GIL com C Extensions

```python
# NumPy libera o GIL durante operações pesadas
import numpy as np

def operacao_pesada():
    a = np.random.rand(1000, 1000)
    b = np.random.rand(1000, 1000)
    return np.dot(a, b)  # GIL liberado durante execução C
```

## Event Loop (Node.js)

Node.js usa um event loop single-thread para I/O não-bloqueante.

```javascript
// Event loop phases (libuv):
// 1. timers (setTimeout, setInterval)
// 2. pending callbacks (I/O)
// 3. idle, prepare
// 4. poll (coleta novos eventos I/O)
// 5. check (setImmediate)
// 6. close callbacks

// ❌ Bloqueia event loop
function bloquear() {
    const fim = Date.now() + 5000;
    while (Date.now() < fim) {}  // CPU bound no event loop
}

// ✅ I/O assíncrono
const fs = require('fs/promises');
async function lerArquivos() {
    const [a, b] = await Promise.all([
        fs.readFile('a.txt', 'utf8'),
        fs.readFile('b.txt', 'utf8'),
    ]);
    return a + b;
}

// ✅ Worker threads para CPU bound
const { Worker } = require('worker_threads');

function calcularNoWorker(dados) {
    return new Promise((resolve, reject) => {
        const worker = new Worker('./worker.js', { workerData: dados });
        worker.on('message', resolve);
        worker.on('error', reject);
    });
}
```

### Virtual Threads (Java)

```java
// Java 21+ — Virtual Threads (Project Loom)
// Threads ultra-leves gerenciadas pela JVM

import java.util.concurrent.*;

public class VirtualThreadExample {
    public static void main(String[] args) throws Exception {
        // Criar 10000 virtual threads (impossível com platform threads)
        try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
            for (int i = 0; i < 10000; i++) {
                int taskId = i;
                executor.submit(() -> {
                    try {
                        Thread.sleep(100);  // não bloqueia thread OS
                        System.out.println("Task " + taskId + " completada");
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                    }
                });
            }
        }

        // Structured concurrency
        try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
            Future<String> user = scope.fork(() -> fetchUser());
            Future<String> orders = scope.fork(() -> fetchOrders());
            scope.join();
            scope.throwIfFailed();

            return user.resultNow() + orders.resultNow();
        }
    }
}
```

## async/await Patterns

### Python

```python
import asyncio
import aiohttp
from asyncio import Semaphore

# Controle de concorrência com semáforo
sem = Semaphore(10)  # max 10 conexões simultâneas

async def fetch_com_limite(session, url):
    async with sem:
        async with session.get(url) as response:
            return await response.json()

async def main():
    urls = [f"https://api.exemplo.com/page/{i}" for i in range(100)]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_com_limite(session, url) for url in urls]
        resultados = await asyncio.gather(*tasks, return_exceptions=True)

    # Tratar erros
    sucessos = [r for r in resultados if not isinstance(r, Exception)]
    erros = [r for r in resultados if isinstance(r, Exception)]
    print(f"{len(sucessos)} sucessos, {len(erros)} erros")

# Timeout
async def fetch_com_timeout(session, url):
    try:
        async with asyncio.timeout(5):
            async with session.get(url) as response:
                return await response.json()
    except asyncio.TimeoutError:
        return {"error": "timeout", "url": url}

asyncio.run(main())
```

### TypeScript

```typescript
// TypeScript — async patterns
async function fetchWithRetry<T>(
    fn: () => Promise<T>,
    retries: number = 3,
    delay: number = 1000
): Promise<T> {
    for (let i = 0; i < retries; i++) {
        try {
            return await fn();
        } catch (error) {
            if (i === retries - 1) throw error;
            await new Promise(r => setTimeout(r, delay * Math.pow(2, i)));
        }
    }
    throw new Error('Unreachable');
}

// Promise.allSettled — executa todas, coleta erros sem abortar
const results = await Promise.allSettled(
    urls.map(url => fetch(url))
);

const successes = results.filter(r => r.status === 'fulfilled');
const errors = results.filter(r => r.status === 'rejected');

// AbortController — cancelamento
const controller = new AbortController();
const timeout = setTimeout(() => controller.abort(), 5000);

try {
    const response = await fetch(url, { signal: controller.signal });
} catch (err) {
    if (err instanceof DOMException && err.name === 'AbortError') {
        console.log('Request cancelada por timeout');
    }
} finally {
    clearTimeout(timeout);
}
```

## Locks, Mutexes, Semaphores

### Race Conditions

```python
import threading

# ❌ Race condition — resultado imprevisível
contador = 0

def incrementar():
    global contador
    for _ in range(100000):
        temp = contador      # READ
        temp += 1            # MODIFY
        contador = temp      # WRITE

threads = [threading.Thread(target=incrementar) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]
print(f"Esperado: 1_000_000, Obtido: {contador}")  # MUITO menor
```

### Lock (Mutex)

```python
import threading

# ✅ Lock — exclusão mútua
lock = threading.Lock()
contador = 0

def incrementar_seguro():
    global contador
    for _ in range(100000):
        with lock:  # acquire/release automático
            contador += 1

# RLock — reentrante (mesma thread pode adquirir múltiplas vezes)
rlock = threading.RLock()

def recursiva(n):
    with rlock:
        if n > 0:
            recursiva(n - 1)  # mesma thread, RLock permite
```

### Deadlocks

```python
import threading
import time

# ❌ Deadlock — duas threads esperam recursos do outro
lock_a = threading.Lock()
lock_b = threading.Lock()

def thread_1():
    with lock_a:
        time.sleep(0.1)
        with lock_b:  # Espera lock_b que thread_2 segura
            pass

def thread_2():
    with lock_b:
        time.sleep(0.1)
        with lock_a:  # Espera lock_a que thread_1 segura
            pass

# ✅ Prevenção: lock ordering (sempre adquirir na mesma ordem)
def thread_1_segura():
    with lock_a:
        time.sleep(0.1)
        with lock_b:
            pass

def thread_2_segura():
    with lock_a:  # mesma ordem!
        time.sleep(0.1)
        with lock_b:
            pass

# Uso de timeout para detectar deadlock
def adquirir_com_timeout(lock, timeout=5):
    if lock.acquire(timeout=timeout):
        try:
            return True
        finally:
            lock.release()
    else:
        raise TimeoutError("Deadlock detectado!")
```

### Semaphore

```python
import threading
import time

# Semaphore — controla acesso a recurso com capacidade limitada
pool = threading.Semaphore(3)  # máximo 3 conexões simultâneas

def processar_com_recurso(id):
    with pool:
        print(f"Processando {id}...")
        time.sleep(1)
        print(f"Finalizado {id}")

threads = [threading.Thread(target=processar_com_recurso, args=(i,))
           for i in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

# BoundedSemaphore — verifica se mais releases que acquires foram feitos
pool_seguro = threading.BoundedSemaphore(3)

# Condition — sinalização entre threads
cond = threading.Condition()
buffer = []
MAX = 5

def produtor():
    for i in range(10):
        with cond:
            while len(buffer) >= MAX:
                cond.wait()  # aguarda consumidor liberar espaço
            buffer.append(i)
            cond.notify()   # acorda consumidor

def consumidor():
    for _ in range(10):
        with cond:
            while not buffer:
                cond.wait()  # aguarda produtor adicionar
            item = buffer.pop(0)
            cond.notify()    # acorda produtor
```

## Actor Model

Cada **ator** é uma entidade independente com estado privado, que se comunica via mensagens assíncronas.

### Erlang/Elixir

```elixir
# Elixir — Actor Model nativo (BEAM VM)
defmodule Counter do
  use GenServer

  # API
  def start_link(initial) do
    GenServer.start_link(__MODULE__, initial, name: __MODULE__)
  end

  def increment do
    GenServer.cast(__MODULE__, :increment)
  end

  def get do
    GenServer.call(__MODULE__, :get)
  end

  # Callbacks
  def init(initial), do: {:ok, initial}

  def handle_cast(:increment, state) do
    {:noreply, state + 1}
  end

  def handle_call(:get, _from, state) do
    {:reply, state, state}
  end
end

# Uso — milhões de atores simultâneos
Counter.start_link(0)
Counter.increment()
Counter.get()  #=> 1
```

### Akka (Java/Scala)

```java
// Akka — Actor Model para JVM
import akka.actor.AbstractActor;
import akka.actor.ActorRef;
import akka.actor.ActorSystem;
import akka.actor.Props;

public class BankAccount extends AbstractActor {
    private int balance = 0;

    @Override
    public Receive createReceive() {
        return receiveBuilder()
            .match(Deposit.class, this::onDeposit)
            .match(Withdraw.class, this::onWithdraw)
            .match(GetBalance.class, this::onGetBalance)
            .build();
    }

    private void onDeposit(Deposit d) {
        balance += d.amount;
    }

    private void onWithdraw(Withdraw w) {
        if (balance >= w.amount) {
            balance -= w.amount;
            sender().tell(new WithdrawSuccess(), self());
        } else {
            sender().tell(new InsufficientFunds(), self());
        }
    }

    private void onGetBalance(GetBalance g) {
        sender().tell(balance, self());
    }

    // Mensagens imutáveis
    record Deposit(int amount) {}
    record Withdraw(int amount) {}
    record GetBalance() {}
    record WithdrawSuccess() {}
    record InsufficientFunds() {}
}

// Uso
ActorSystem system = ActorSystem.create("bank");
ActorRef account = system.actorOf(Props.create(BankAccount.class));
account.tell(new BankAccount.Deposit(100), ActorRef.noSender());
```

## Multiprocessing em Python

```python
import multiprocessing as mp
from multiprocessing import Queue, Pipe, Array, Value
import time

# Pool — map/reduce paralelo
def processar_chunk(dados):
    return sum(x * x for x in dados)

if __name__ == "__main__":
    dados = list(range(10_000_000))
    chunk_size = len(dados) // 4
    chunks = [dados[i:i+chunk_size] for i in range(0, len(dados), chunk_size)]

    with mp.Pool(4) as pool:
        resultados = pool.map(processar_chunk, chunks)

    total = sum(resultados)
    print(f"Resultado: {total}")

    # Shared memory — Array, Value
    contador = mp.Value('i', 0)
    lock = mp.Lock()

    def incrementar(c, l):
        with l:
            c.value += 1

    processes = [mp.Process(target=incrementar, args=(contador, lock))
                 for _ in range(10)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    print(contador.value)  # 10

    # Queue — comunicação entre processos
    q = mp.Queue()

    def producer(q):
        for i in range(5):
            q.put(i)
        q.put(None)  # sentinel

    p = mp.Process(target=producer, args=(q,))
    p.start()
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Recebido: {item}")
    p.join()
```

## Worker Threads (Node.js)

```javascript
// worker.js
const { parentPort, workerData } = require('worker_threads');

// CPU intensivo no worker
function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

const result = fibonacci(workerData.n);
parentPort.postMessage(result);

// main.js
const { Worker } = require('worker_threads');
const { cpus } = require('os');

function paralelizar(tarefas) {
    const numWorkers = cpus().length;
    const workers = [];
    const resultados = [];

    return new Promise((resolve, reject) => {
        tarefas.forEach((tarefa, i) => {
            const worker = new Worker('./worker.js', { workerData: tarefa });
            workers.push(worker);

            worker.on('message', (resultado) => {
                resultados[i] = resultado;
                if (resultados.length === tarefas.length) {
                    resolve(resultados);
                }
            });
            worker.on('error', reject);
        });
    });
}

// Web Workers (Browser)
// main.js
const worker = new Worker('worker.js');
worker.postMessage({ n: 42 });
worker.onmessage = (event) => {
    console.log('Resultado:', event.data);
};
worker.onerror = (error) => {
    console.error('Erro no worker:', error);
};

// worker.js (browser)
self.onmessage = (event) => {
    const { n } = event.data;
    const result = fibonacci(n);
    self.postMessage(result);
};
```

## Parallelism em Data Processing

### MapReduce

```python
# MapReduce simplificado com multiprocessing
from collections import defaultdict
import multiprocessing as mp

def map_function(texto):
    palavras = texto.lower().split()
    return [(palavra, 1) for palavra in palavras]

def reduce_function(items):
    palavra, contagens = items
    return (palavra, sum(contagens))

def word_count_mapreduce(documentos):
    # Map paralelo
    with mp.Pool() as pool:
        mapped = pool.map(map_function, documentos)

    # Shuffle (agrupar por chave)
    shuffling = defaultdict(list)
    for m in mapped:
        for palavra, count in m:
            shuffling[palavra].append(count)

    # Reduce
    with mp.Pool() as pool:
        result = pool.map(reduce_function, shuffling.items())

    return dict(result)
```

### Apache Spark

```python
# PySpark — processamento distribuído
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, window, avg

spark = SparkSession.builder \
    .appName("Analise") \
    .config("spark.executor.memory", "4g") \
    .getOrCreate()

# Transformações lazy
df = spark.read.parquet("s3://dados/vendas.parquet")

resultados = (
    df
    .filter(col("valor") > 0)
    .groupBy("produto_id")
    .agg(
        avg("valor").alias("media"),
        avg("quantidade").alias("media_qtd")
    )
    .orderBy(col("media").desc())
)

# Ação — executa o DAG
resultados.show(10)

# Particionamento otimizado
df.repartition(200, "produto_id") \
  .write \
  .partitionBy("data") \
  .parquet("s3://dados/otimizado/")
```

## Concurrency Patterns

### Fan-Out (distribuir tarefas)

```python
import asyncio

async def worker(id, queue, results):
    while True:
        item = await queue.get()
        if item is None:
            break
        result = await processar(item)
        await results.put(result)
    queue.task_done()

async def fan_out(num_workers, items):
    queue = asyncio.Queue()
    results = asyncio.Queue()

    # Enfileirar itens
    for item in items:
        await queue.put(item)

    # Workers
    workers = [
        asyncio.create_task(worker(i, queue, results))
        for i in range(num_workers)
    ]

    # Sentinels
    for _ in range(num_workers):
        await queue.put(None)

    await asyncio.gather(*workers)

    # Coletar resultados
    output = []
    while not results.empty():
        output.append(await results.get())
    return output
```

### Fan-In (coletar resultados)

```python
async def fan_in(sources):
    """Combina múltiplos streams em um único"""
    queue = asyncio.Queue()

    async def collect(source_id, stream):
        async for item in stream:
            await queue.put((source_id, item))

    collectors = [
        asyncio.create_task(collect(i, source))
        for i, source in enumerate(sources)
    ]

    async def waiter():
        await asyncio.gather(*collectors)
        await queue.put(None)  # sentinel

    asyncio.create_task(waiter())

    while True:
        item = await queue.get()
        if item is None:
            break
        yield item
```

### Pipeline

```python
import asyncio

async def pipeline():
    """Pipeline de processamento com 3 estágios"""
    queue1 = asyncio.Queue()
    queue2 = asyncio.Queue()

    async def stage1():
        for i in range(100):
            await queue1.put(f"dado_{i}")
        await queue1.put(None)

    async def stage2():
        while True:
            item = await queue1.get()
            if item is None:
                await queue2.put(None)
                break
            # Processamento intermediário
            processed = item.upper()
            await queue2.put(processed)

    async def stage3():
        while True:
            item = await queue2.get()
            if item is None:
                break
            print(f"Output: {item}")

    await asyncio.gather(stage1(), stage2(), stage3())
```

### Pub/Sub

```python
import asyncio
from collections import defaultdict

class EventBus:
    def __init__(self):
        self.subscribers = defaultdict(list)

    def subscribe(self, event_type, callback):
        self.subscribers[event_type].append(callback)

    async def publish(self, event_type, data):
        if event_type not in self.subscribers:
            return
        tasks = [
            asyncio.create_task(cb(data))
            for cb in self.subscribers[event_type]
        ]
        await asyncio.gather(*tasks, return_exceptions=True)

# Uso
bus = EventBus()

async def log_event(data):
    print(f"Log: {data}")

async def notify_event(data):
    print(f"Notify: {data}")

bus.subscribe("pedido.criado", log_event)
bus.subscribe("pedido.criado", notify_event)

await bus.publish("pedido.criado", {"id": 123, "total": 450.0})
```

### Worker Pool

```python
import asyncio
from asyncio import Queue

class WorkerPool:
    def __init__(self, num_workers, process_func):
        self.queue = Queue()
        self.process_func = process_func
        self.workers = [
            asyncio.create_task(self._worker(i))
            for i in range(num_workers)
        ]

    async def _worker(self, worker_id):
        while True:
            item = await self.queue.get()
            if item is None:
                self.queue.task_done()
                break
            try:
                await self.process_func(worker_id, item)
            except Exception as e:
                print(f"Worker {worker_id} error: {e}")
            finally:
                self.queue.task_done()

    async def submit(self, item):
        await self.queue.put(item)

    async def shutdown(self):
        for _ in range(len(self.workers)):
            await self.queue.put(None)
        await asyncio.gather(*self.workers)
```

## Ferramentas e Monitoramento

```bash
# Monitoramento de threads
ps -eLf | grep python  # ver threads
htop -H                 # threads individuais

# strace — syscalls (identificar bloqueios)
strace -p 12345 -f -c

# Python threading debug
python -c "import threading; print(threading.enumerate())"

# asyncio debug
PYTHONASYNCIODEBUG=1 python script.py
```

## Anti-patterns

```python
# ❌ Shared state sem locks
# ✅ Message passing ou locks explícitos

# ❌ Thread per request (C10K problem)
# ✅ Event loop (async) ou thread pool

# ❌ Bloquear event loop com CPU
# ✅ Executar CPU bound em process pool separado

# ❌ Fire-and-forget sem tratamento de erro
# ✅ Sempre tratar exceções em tasks concorrentes

# ❌ Starvation — prioridade baixa nunca executa
# ✅ Usar filas justas (FIFO) ou scheduling adequado
```

## Referências

- **"Concurrency in Go"** — Katherine Cox-Buday (2017). Padrões de concorrência em Go.
- **"Programming Erlang"** — Joe Armstrong (2013). Actor Model e tolerância a falhas.
- **"Java Concurrency in Practice"** — Brian Goetz et al. (2006). O livro definitivo sobre concorrência em Java.
- **"Python Concurrency with asyncio"** — Matthew Fowler (2022). Async/await em Python na prática.
- **"C++ Concurrency in Action"** — Anthony Williams (2019). Concorrência e paralelismo em C++.
- **"Seven Concurrency Models in Seven Weeks"** — Paul Butcher (2014). Visão comparativa de modelos de concorrência.
- **"The Art of Multiprocessor Programming"** — Maurice Herlihy, Nir Shavit (2021). Fundamentos teóricos de concorrência.
- **PEP 703 — CPython sem GIL** — https://peps.python.org/pep-0703/
- **libuv (Node.js event loop)** — https://libuv.org/
- **Akka Framework** — https://akka.io/
- **Project Loom (Java Virtual Threads)** — https://openjdk.org/projects/loom/
- **"Understanding the Node.js Event Loop"** — https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick
