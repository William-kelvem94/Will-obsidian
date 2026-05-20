---
title: "Python — Cheat Sheet"
description: "Guia de referência rápida para Python — sintaxe, bibliotecas, boas práticas e padrões"
tags: [cheatsheet, python, linguagem, scripting]
updated: 2026-05-16
date: 2026-05-16
---

# Python — Cheat Sheet

Referência completa para desenvolvimento Python: setup, sintaxe essencial, biblioteca padrão, pacotes populares e padrões avançados.

---

## 📋 Sumário

- [🔧 Ambiente e Setup](#-ambiente-e-setup)
- [📝 Sintaxe Essencial](#-sintaxe-essencial)
- [🧩 Comprehensions](#-comprehensions)
- [⚡ Generators](#-generators)
- [🎀 Decorators](#-decorators)
- [📚 Biblioteca Padrão](#-biblioteca-padrão)
- [📦 Pacotes Populares](#-pacotes-populares)
- [⏳ Async / Await](#-async--await)
- [🧪 Testes](#-testes)
- [📦 Empacotamento](#-empacotamento)
- [⚡ Performance](#-performance)
- [⚠️ Pitfalls Comuns](#-pitfalls-comuns)
- [🐛 Troubleshooting](#-troubleshooting)
- [🔗 Relacionados](#-relacionados)

---

## 🔧 Ambiente e Setup

### venv (nativo)

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar (Linux/Mac)
source .venv/bin/activate

# Ativar (Windows)
.venv\Scripts\activate

# Desativar
deactivate

# Instalar pacotes
pip install -r requirements.txt
pip list                          # Lista pacotes
pip freeze > requirements.txt     # Congela dependências
```

### pyenv (gerenciar versões)

```bash
# Instalar (Linux/Mac)
curl https://pyenv.run | bash

# Instalar versão
pyenv install 3.12.3
pyenv install 3.11.9

# Listar versões
pyenv versions

# Definir versão
pyenv global 3.12.3
pyenv local 3.11.9               # Por projeto (.python-version)
pyenv shell 3.10.14              # Temporário

# Virtualenv com pyenv
pyenv virtualenv 3.12.3 meu-projeto
pyenv activate meu-projeto
```

### conda (ciência de dados)

```bash
# Criar ambiente
conda create -n ml-env python=3.12
conda activate ml-env

# Instalar
conda install numpy pandas scikit-learn
conda install -c conda-forge jupyterlab

# Exportar
conda env export > environment.yml
conda env create -f environment.yml
```

### pyproject.toml moderno

```toml
[project]
name = "meu-projeto"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "httpx>=0.27",
    "pydantic>=2.0",
    "typer>=0.9",
]

[project.optional-dependencies]
dev = ["pytest>=8", "mypy>=1.0", "ruff>=0.3"]
test = ["pytest>=8", "pytest-cov>=4"]
```

---

## 📝 Sintaxe Essencial

### Tipos de Dados

```python
# Básicos
int: int = 42
float: float = 3.14
str: str = "hello"
bool: bool = True
NoneType: None = None

# Coleções
list: list[int] = [1, 2, 3]
tuple: tuple[int, str] = (1, "a")
dict: dict[str, int] = {"a": 1}
set: set[int] = {1, 2, 3}
frozenset: frozenset[int] = frozenset([1, 2])

# type: ignore
from typing import Optional, Union, Any, Literal

Optional[str]         # str | None
Union[int, str]       # int | str (Python 3.10+: int | str)
Any                   # qualquer tipo
Literal["a", "b"]     # valor literal
```

### Controle de Fluxo

```python
# If/elif/else
if x > 0:
    print("positivo")
elif x == 0:
    print("zero")
else:
    print("negativo")

# Operador ternário
status = "maior" if age >= 18 else "menor"

# Match (Python 3.10+)
match status_code:
    case 200:
        print("OK")
    case 201 | 204:
        print("criado/sem conteúdo")
    case 400:
        print("bad request")
    case _:
        print("outro")

# For
for item in items:
    print(item)

for i, item in enumerate(items, start=1):
    print(f"{i}: {item}")

for k, v in dict.items():
    print(k, v)

# While
while count > 0:
    count -= 1
```

### Funções

```python
# Parâmetros
def func(a: int, b: str = "default", *args: int, **kwargs: Any) -> bool:
    return True

# Positional-only / Keyword-only (Python 3.8+)
def func(a: int, b: int, /, c: int, *, d: int) -> None:
    pass

# a, b: positional-only
# c: positional ou keyword
# d: keyword-only

# Docstrings
def soma(a: int, b: int) -> int:
    """Soma dois números."""
    return a + b

# Lambda
squared = list(map(lambda x: x**2, [1, 2, 3]))
sorted_by_key = sorted(items, key=lambda x: x["name"])
```

### Tratamento de Erros

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("divisão por zero")
except (ValueError, TypeError) as e:
    print(f"erro: {e}")
else:
    print("sem exceções")
finally:
    print("sempre executa")

# Raise
raise ValueError("mensagem")
raise NotImplementedError("método deve ser implementado")

# Context manager customizado
class ManagedFile:
    def __enter__(self):
        self.file = open("file.txt", "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# with
with open("file.txt") as f:
    content = f.read()
```

---

## 🧩 Comprehensions

```python
# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]

# Dict comprehension
square_map = {x: x**2 for x in range(5)}
filtered = {k: v for k, v in dict.items() if v > 10}

# Set comprehension
unique_squares = {x**2 for x in [1, 1, 2, 2, 3]}

# Nested comprehension (matriz)
matrix = [[i * j for j in range(3)] for i in range(3)]

# Com condicional ternário
parsed = [int(x) if x.isdigit() else 0 for x in items]
```

---

## ⚡ Generators

```python
# Generator function
def fibonacci(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

# Generator expression
squares = (x**2 for x in range(10))

# Pipeline com generators
def read_lines(filepath: str):
    with open(filepath) as f:
        yield from f

def strip_lines(lines):
    for line in lines:
        yield line.strip()

def non_empty(lines):
    for line in lines:
        if line:
            yield line

lines = non_empty(strip_lines(read_lines("data.txt")))

# yield from (delegação)
def chain(*iterables):
    for it in iterables:
        yield from it

# Infinito
def count(start: int = 0, step: int = 1):
    while True:
        yield start
        start += step
```

---

## 🎀 Decorators

```python
from functools import wraps
import time
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

# Decorator básico
def log(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"chamando {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def hello(name: str) -> str:
    return f"olá, {name}"

# Decorator com argumentos
def retry(max_attempts: int = 3, delay: float = 1.0):
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
            raise  # unreachable
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def fetch_data(url: str) -> dict:
    ...

# Decorator de classe
def singleton(cls):
    instances = {}
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    ...
```

---

## 📚 Biblioteca Padrão

### pathlib (manipulação de caminhos)

```python
from pathlib import Path

base = Path("repo/python")
base.exists()                       # True
base.is_dir()                       # True
base.is_file()                      # False

# Ler/Escrever
content = (base / "main.py").read_text()
(base / "output.json").write_text('{"key": "value"}')

# Iterar
for file in base.glob("**/*.py"):
    print(file)

# Caminhos
Path.home()                         # /home/user
Path.cwd()                          # /current/working/dir
base.parent                         # repo
base.name                           # python
base.stem                           # python (sem extensão)
base.suffix                         # "" (diretório)

# Criar/Deletar
(base / "nova-pasta").mkdir(parents=True, exist_ok=True)
(base / "arquivo.txt").touch()
(base / "arquivo.txt").unlink()     # Deletar
```

### itertools (iteradores)

```python
from itertools import (
    chain, cycle, count, repeat,
    product, permutations, combinations,
    groupby, islice, batched,
)

# chain: concatenar iteráveis
list(chain([1, 2], [3, 4]))        # [1, 2, 3, 4]

# cycle: loop infinito
for item in cycle(["A", "B", "C"]):
    ...

# count: contador infinito
for i in count(start=10, step=2):
    ...

# product: produto cartesiano
list(product("AB", "12"))           # [('A','1'),('A','2'),('B','1'),('B','2')]

# permutations / combinations
list(permutations("ABC", 2))        # Todas ordenações de 2
list(combinations("ABC", 2))        # Todos subsets de 2

# groupby (ordenado!)
for key, group in groupby(sorted(data, key=key_func), key=key_func):
    print(key, list(group))

# batched (Python 3.12+)
for batch in batched(range(10), 3):
    print(batch)                    # (0,1,2), (3,4,5), (6,7,8), (9,)

# islice: fatiar iterável
first_5 = islice(iterator, 5)
```

### collections (estruturas de dados)

```python
from collections import defaultdict, Counter, deque, OrderedDict, ChainMap

# defaultdict: valor padrão
counter = defaultdict(int)
counter["a"] += 1                   # não levanta KeyError

grouped = defaultdict(list)
grouped["key"].append(item)

# Counter: contar elementos
freq = Counter("abracadabra")
freq.most_common(3)                 # [('a', 5), ('b', 3), ('r', 2)]

# deque: fila dupla
queue = deque(["a", "b", "c"])
queue.append("d")
queue.appendleft("z")
queue.popleft()                     # 'z'
queue.pop()                         # 'd'

# OrderedDict (preserva ordem de inserção - Python 3.7+ dict já preserva)
od = OrderedDict()
od.move_to_end("key")               # Move para o final

# ChainMap: múltiplos dicionários como um
combined = ChainMap(dict1, dict2)   # dict1 tem prioridade
```

### typing (type hints)

```python
from typing import (
    Optional, Union, Any, Literal,
    TypeVar, Generic, Protocol,
    TypedDict, NamedTuple,
    overload, assert_never,
    Self,  # Python 3.11+
)

T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)

# Generic
class Stack(Generic[T]):
    def push(self, item: T) -> None: ...
    def pop(self) -> T: ...

# Protocol (duck typing estático)
class Drawable(Protocol):
    def draw(self) -> None: ...

def render(obj: Drawable) -> None:
    obj.draw()  # Aceita qualquer objeto com método draw

# TypedDict
class User(TypedDict):
    id: int
    name: str
    email: str

user: User = {"id": 1, "name": "Alice", "email": "a@b.com"}

# NamedTuple
class Point(NamedTuple):
    x: float
    y: float

p = Point(1.0, 2.0)
print(p.x, p.y)                     # Acesso por atributo

# overload (assinaturas múltiplas)
@overload
def process(value: int) -> int: ...
@overload
def process(value: str) -> str: ...
def process(value: int | str) -> int | str:
    return value  # implementação real

# Self (Python 3.11+)
class Builder:
    def set_name(self, name: str) -> Self:
        self.name = name
        return self
```

### dataclasses

```python
from dataclasses import dataclass, field, asdict

@dataclass(frozen=True, order=True)
class Pessoa:
    nome: str
    idade: int = field(compare=False)
    tags: list[str] = field(default_factory=list, repr=False)

p1 = Pessoa("Alice", 30)
p2 = Pessoa("Bob", 25)
print(p1 > p2)                      # True (compara nome)

# asdict / astuple
data = asdict(p1)                   # {"nome": "Alice", "idade": 30}

# Init-only variáveis
@dataclass
class Cliente:
    nome: str
    email: str
    _id: int = field(init=False)

    def __post_init__(self):
        self._id = hash(self.email)

# Suporte a slots (Python 3.10+)
@dataclass(slots=True)
class Config:
    host: str = "localhost"
    port: int = 8080
```

---

## 📦 Pacotes Populares

### requests / httpx

```python
import httpx  # moderno, async, HTTP/2

# GET síncrono
response = httpx.get("https://api.github.com", params={"page": 1})
response.status_code               # 200
response.json()                    # dict
response.headers["Content-Type"]

# POST
response = httpx.post(
    "https://api.example.com/login",
    json={"user": "admin", "pass": "secret"},
    headers={"Authorization": "Bearer token"},
    timeout=30.0,
)

# Async
async def fetch(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.json()

# Retry + error handling
from httpx import HTTPStatusError, RequestError

try:
    resp = httpx.get(url, timeout=10)
    resp.raise_for_status()
except HTTPStatusError as e:
    print(f"HTTP {e.response.status_code}")
except RequestError as e:
    print(f"Erro de conexão: {e}")
```

### pydantic (validação)

```python
from pydantic import BaseModel, Field, EmailStr, HttpUrl, model_validator
from datetime import datetime

class User(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    url: HttpUrl | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    tags: list[str] = []

    @model_validator(mode="after")
    def check_name_not_in_tags(self) -> "User":
        if self.name in self.tags:
            raise ValueError("name cannot be in tags")
        return self

# Uso
user = User(id=1, name="Alice", email="a@b.com")
print(user.model_dump())            # dict
print(user.model_dump_json())       # JSON string

# Config
class Settings(BaseModel):
    db_url: str = Field(alias="DATABASE_URL")
    debug: bool = False

    model_config = {"env_file": ".env", "extra": "forbid"}

settings = Settings()  # Lê de .env automaticamente
```

### click / typer (CLIs)

```python
# Typer (moderno, baseado em type hints)
import typer

app = typer.Typer()

@app.command()
def hello(name: str, count: int = 1, upper: bool = False):
    """Diz olá para NAME, COUNT vezes."""
    msg = name.upper() if upper else name
    for _ in range(count):
        print(f"Olá {msg}!")

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Adeus {name}")
    else:
        print(f"Falou {name}!")

if __name__ == "__main__":
    app()

# click (clássico)
import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument("name")
@click.option("--count", default=1, help="Número de vezes")
def greet(name: str, count: int):
    for _ in range(count):
        click.echo(f"Olá {name}!")
```

---

## ⏳ Async / Await

```python
import asyncio
import httpx

# Corotina básica
async def fetch(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        return resp.json()

# Executar
result = asyncio.run(fetch("https://api.github.com"))

# Concorrência com gather
async def fetch_all(urls: list[str]) -> list[dict]:
    async with httpx.AsyncClient() as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        return [r.json() for r in responses if not isinstance(r, Exception)]

# Semáforo (limitar concorrência)
sem = asyncio.Semaphore(10)

async def fetch_with_limit(url: str) -> dict:
    async with sem:
        return await fetch(url)

# Timeout
async def fetch_with_timeout(url: str) -> dict:
    try:
        async with asyncio.timeout(5.0):
            return await fetch(url)
    except asyncio.TimeoutError:
        return {"error": "timeout"}

# Async generator
async def stream_lines(url: str):
    async with httpx.AsyncClient() as client:
        async with client.stream("GET", url) as resp:
            async for line in resp.aiter_lines():
                yield line.strip()

# TaskGroup (Python 3.11+)
async def process_all(urls: list[str]) -> list[dict]:
    results = []
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(fetch(url)) for url in urls]
    return [t.result() for t in tasks]
```

---

## 🧪 Testes

### pytest

```python
# test_calculator.py
import pytest
from calculator import add, divide

# Teste simples
def test_add():
    assert add(2, 3) == 5

# Teste com parametrização
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add_params(a: int, b: int, expected: int):
    assert add(a, b) == expected

# Fixtures
@pytest.fixture
def db_connection():
    conn = create_test_db()
    yield conn
    conn.close()

def test_query(db_connection):
    result = db_connection.query("SELECT 1")
    assert result == 1

# Fixture com escopo
@pytest.fixture(scope="session")
def settings():
    return load_test_settings()

# Mock
from unittest.mock import Mock, patch

def test_external_api():
    with patch("myapp.api.client.get") as mock_get:
        mock_get.return_value.json.return_value = {"status": "ok"}
        result = call_api()
        assert result["status"] == "ok"

# Pytest fixtures built-in
def test_tmp_path(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("hello")
    assert file.read_text() == "hello"

# Fixture com yield (teardown)
@pytest.fixture
def resource():
    print("setup")
    yield "resource"
    print("teardown")

# Conftest.py (fixtures compartilhadas)
# tests/conftest.py
@pytest.fixture
def client():
    from myapp import app
    return app.test_client()

# Rodar testes
# pytest
# pytest -v
# pytest -x  (para no primeiro erro)
# pytest --cov=src --cov-report=term-missing
# pytest -k "test_login"  (filtra por nome)
```

---

## 📦 Empacotamento

### pyproject.toml (moderno)

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "meu-pacote"
version = "0.1.0"
description = "Descrição do pacote"
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.11"
authors = [
    {name = "Seu Nome", email = "email@example.com"},
]
dependencies = [
    "httpx>=0.27",
]

[project.optional-dependencies]
dev = [
    "pytest>=8",
    "mypy>=1.0",
    "ruff>=0.3",
]

[project.urls]
Repository = "https://github.com/usuario/meu-pacote"

[tool.pytest.ini_options]
testpaths = ["tests"]
```

### Script de entrada

```python
# src/meu_pacote/__init__.py
from .main import hello

__all__ = ["hello"]
__version__ = "0.1.0"

# src/meu_pacote/__main__.py (suporta python -m meu_pacote)
from .cli import app

if __name__ == "__main__":
    app()
```

### Instalação em modo editable

```bash
pip install -e .                    # Com pyproject.toml
pip install -e ".[dev]"             # Com dependências dev
```

---

## ⚡ Performance

### Profiling

```python
# timeit (micro-benchmarks)
import timeit

timeit.timeit("sum(range(100))", number=10000)

# cProfile (macro)
python -m cProfile -s cumulative meu_script.py

# snakeviz (visualização)
# pip install snakeviz
# python -m cProfile -o output.prof meu_script.py
# snakeviz output.prof

# py-spy (sampling profiler, sem modificar código)
# py-spy record -o profile.svg -- python meu_script.py

# timing manual
from time import perf_counter

start = perf_counter()
result = expensive_function()
elapsed = perf_counter() - start
print(f"levou {elapsed:.3f}s")
```

### __slots__

```python
# Reduz overhead de memória (~50% menos)
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

# Sem __dict__
# p.__dict__  # AttributeError!

# Quando usar:
# - Milhares/milhões de instâncias
# - Atributos conhecidos em tempo de design
```

### Caching

```python
from functools import lru_cache, cache

# LRU Cache (tamanho limitado)
@lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Cache sem limite (Python 3.9+)
@cache
def expensive_query(user_id: int) -> dict:
    ...

# Cache com TTL customizado
from functools import wraps
import time

def ttl_cache(seconds: int = 60):
    def decorator(func):
        cache_data = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(kwargs.items()))
            if key in cache_data:
                result, timestamp = cache_data[key]
                if time.time() - timestamp < seconds:
                    return result
            result = func(*args, **kwargs)
            cache_data[key] = (result, time.time())
            return result
        return wrapper
    return decorator
```

### Outras Dicas

```python
# Use join ao invés de +
words = ["hello", "world"]
text = " ".join(words)              # rápido
# text = ""
# for w in words: text += w         # lento (O(n²))

# Compreensões > loops
squares = [x**2 for x in range(1000)]  # 2x mais rápido
# squares = []
# for x in range(1000):
#     squares.append(x**2)

# Use map/filter com funções built-in
nums = list(map(int, strings))

# Variáveis locais são mais rápidas que globais
def fast():
    local_sum = sum                    # lookup único
    return local_sum(range(1000))

# Use deque para filas, não list (pop(0) é O(n))
from collections import deque
```

---

## ⚠️ Pitfalls Comuns

```python
# 1. Mutabilidade como padrão
def add_item(item, lst=[]):         # ERRO! lista é mutável
    lst.append(item)
    return lst

# Correto
def add_item(item, lst=None):
    lst = lst or []
    lst.append(item)
    return lst

# 2. Cópia vs Referência
a = [1, 2, 3]
b = a                               # Referência, não cópia!
b.append(4)
print(a)  # [1, 2, 3, 4]

# Correto
b = a.copy()
b = a[:]

# 3. Chaves de dicionário mutáveis
# bad = {[1, 2]: "value"}           # TypeError: unhashable type
# Correto: use tuple como chave
good = {(1, 2): "value"}

# 4. Closures e variáveis de loop
funcs = [lambda: i for i in range(5)]
print([f() for f in funcs])         # [4, 4, 4, 4, 4]

# Correto
funcs = [lambda i=i: i for i in range(5)]
print([f() for f in funcs])         # [0, 1, 2, 3, 4]

# 5. float inexato
print(0.1 + 0.2)                    # 0.30000000000000004

# Correto: Decimal
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))  # 0.3

# 6. Shadow de built-ins
# list = [1, 2]                     # ERRO: sobrescreve list()
# Correto: nunca use nomes de built-ins como variáveis

# 7. is vs == para strings
# is compara identidade, não igualdade!
a = "hello"
b = "".join(["h", "e", "l", "l", "o"])
print(a is b)                       # Pode ser False!
print(a == b)                       # Sempre True

# 8. Modificar lista durante iteração
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)          # Pula elementos!

# Correto
items[:] = [x for x in items if x % 2 != 0]
```

---

## 🐛 Troubleshooting

### Issue: ModuleNotFoundError

```bash
# Causa: pacote não instalado ou ambiente errado

# Verificar ambiente ativo
which python
which pip
pip list | grep pacote

# Soluções
pip install pacote
pip install -e .                    # Pacote local
python -m pip install pacote        # Garante pip correto

# Verificar PYTHONPATH
echo $PYTHONPATH
export PYTHONPATH="$PWD/src:$PYTHONPATH"
```

### Issue: Erro de import circular

```python
# a.py -> import b.py -> import a.py (ciclo)

# Solução 1: import tardio (dentro da função)
def get_b():
    from b import B
    return B()

# Solução 2: reestruturar
# Mover interface compartilhada para um terceiro módulo

# Solução 3: usar TYPE_CHECKING para type hints
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from b import B
```

### Issue: MemoryError (vazamento de memória)

```bash
# Rastrear com tracemalloc
python -X tracemalloc meu_script.py
```

```python
import tracemalloc

tracemalloc.start()
# ... código ...
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")

for stat in top_stats[:10]:
    print(stat)
```

### Issue: Erro de encoding (UnicodeDecodeError)

```python
# Ao ler arquivos
with open("file.txt", encoding="utf-8") as f:
    content = f.read()

# Detectar encoding
import chardet
with open("file.txt", "rb") as f:
    raw = f.read()
    result = chardet.detect(raw)
    encoding = result["encoding"]

with open("file.txt", encoding=encoding) as f:
    content = f.read()
```

### Issue: Performance lenta

```bash
# Identificar gargalos
python -m cProfile -s cumulative script.py | head -20

# Verificar se há loops lentos
# Use @lru_cache para funções chamadas repetidamente
# Use arrays numpy para operações numéricas
# Considere PyPy como alternativa ao CPython
```

---

## 🔗 Relacionados

- [Python Docs](https://docs.python.org/3/)
- [Python Package Index (PyPI)](https://pypi.org/)
- [[skills/02-software-engineering/backend|Backend Skills]]
- [[JARVIS/04-Engineering/Wiki/CheatSheets/Docker|Docker Cheat Sheet]]
- [[JARVIS/04-Engineering/Wiki/CheatSheets/FastAPI|FastAPI Cheat Sheet]]

[[JARVIS/README|← Voltar ao Command Center]]
