---
title: "Testes de Software"
date: 2026-05-16
area: "Programação e Engenharia de Software"
tags: [conhecimento, programacao, testes, tdd, pytest, testing]
related: ["04-Conhecimentos/07-Humanidades/Programacao/DevOps-e-Infra"]
aliases: ["Software Testing", "TDD", "Test Automation"]
---

## Visão Geral

Testes de software são a principal ferramenta para garantir que o código se comporta conforme esperado. Uma boa estratégia de testes reduz bugs, facilita refatorações e documenta o comportamento do sistema.

## Pirâmide de Testes

Proposta por Mike Cohn em *Succeeding with Agile*, a pirâmide define a proporção ideal entre tipos de teste:

```
        /\
       /e2e\
      /------\
     /integra-\
    /--------- \
   /  unitário  \
  /---------------\
 /    (base ampla) \
/-------------------\
```

| Camada | Velocidade | Cobertura | Quantidade |
|--------|-----------|-----------|------------|
| Unitário | ms | Função/classe isolada | ~70% |
| Integração | ms-s | Módulos combinados | ~20% |
| E2E | s-min | Fluxo completo | ~10% |

```python
# Teste unitário — isolado com mock
from unittest.mock import Mock

def test_calcula_total():
    repo = Mock()
    repo.buscar_preco.return_value = 10.0
    servico = CarrinhoServico(repo)

    total = servico.calcular_total([{"produto_id": 1, "qtd": 3}])

    assert total == 30.0
    repo.buscar_preco.assert_called_once_with(1)
```

## TDD (Test-Driven Development)

Ciclo **Red-Green-Refactor** proposto por Kent Beck em *Test-Driven Development: By Example*:

1. **Red** — Escreva um teste que falha
2. **Green** — Escreva o mínimo de código para passar
3. **Refactor** — Melhore o código mantendo testes verdes

```python
# Ciclo TDD — calculadora de frete

# Passo 1: RED — testa funcionalidade que ainda não existe
def test_frete_gratis_acima_de_100():
    resultado = calcular_frete(valor_total=150)
    assert resultado == 0.0

def test_frete_10_percent_abaixo_de_100():
    resultado = calcular_frete(valor_total=50)
    assert resultado == 5.0  # 10% de 50

# Passo 2: GREEN — implementação mínima
def calcular_frete(valor_total: float) -> float:
    if valor_total >= 100:
        return 0.0
    return valor_total * 0.1

# Passo 3: REFACTOR — extrair constantes, melhorar legibilidade
TAXA_FRETE = 0.1
VALOR_MINIMO_FRETE_GRATIS = 100.0

def calcular_frete(valor_total: float) -> float:
    if valor_total >= VALOR_MINIMO_FRETE_GRATIS:
        return 0.0
    return valor_total * TAXA_FRETE
```

```typescript
// TDD em TypeScript com Vitest

// __tests__/pedido.test.ts
import { describe, it, expect } from 'vitest';

describe('Pedido.calcularDesconto', () => {
    it('retorna 10% para cliente VIP', () => {
        const pedido = new Pedido({ clienteTipo: 'VIP', total: 200 });
        expect(pedido.calcularDesconto()).toBe(20);
    });

    it('retorna 0 para cliente comum', () => {
        const pedido = new Pedido({ clienteTipo: 'COMUM', total: 200 });
        expect(pedido.calcularDesconto()).toBe(0);
    });
});
```

## Mocking, Stubs e Fakes

Técnicas para isolar a unidade sob teste substituindo dependências:

| Técnica | Descrição |
|---------|-----------|
| **Stub** | Retorna valores fixos |
| **Mock** | Verifica interações (quantas vezes foi chamado, com quais args) |
| **Fake** | Implementação leve funcional (ex: banco em memória) |
| **Spy** | Wrapper que registra chamadas no objeto real |

```python
# unittest.mock
from unittest.mock import patch, MagicMock
import requests

def buscar_usuario(api: str, user_id: int) -> dict:
    resp = requests.get(f"{api}/users/{user_id}")
    resp.raise_for_status()
    return resp.json()

# Mock de requests.get
@patch("requests.get")
def test_buscar_usuario(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"id": 1, "nome": "João"}

    resultado = buscar_usuario("https://api.exemplo.com", 1)

    assert resultado["nome"] == "João"
    mock_get.assert_called_once_with("https://api.exemplo.com/users/1")
```

```python
# pytest monkeypatch
def test_sem_conexao_externa(monkeypatch):
    def mock_get(*args, **kwargs):
        raise requests.ConnectionError("sem rede")

    monkeypatch.setattr(requests, "get", mock_get)

    with pytest.raises(requests.ConnectionError):
        buscar_usuario("https://api.exemplo.com", 1)
```

```python
# Fake — banco em memória
class FakeRepositorioUsuario:
    def __init__(self):
        self._dados: dict[int, Usuario] = {}

    def salvar(self, usuario: Usuario) -> None:
        self._dados[usuario.id] = usuario

    def buscar_por_id(self, user_id: int) -> Usuario | None:
        return self._dados.get(user_id)

    def listar_ativos(self) -> list[Usuario]:
        return [u for u in self._dados.values() if u.ativo]
```

## Property-Based Testing

Em vez de exemplos específicos, testa propriedades que devem ser verdadeiras para qualquer entrada. A biblioteca gera casos aleatórios e busca contra-exemplos.

```python
from hypothesis import given, strategies as st, assume

# Estratégias
inteiros = st.integers(min_value=1, max_value=1000)
textos = st.text(alphabet="abcdef ", min_size=1, max_size=50)
listas = st.lists(inteiros, min_size=1, max_size=100)
datas = st.dates()

@given(inteiros, inteiros)
def test_soma_comutativa(a, b):
    assert a + b == b + a

@given(listas)
def test_reverse_twice(lista):
    assume(len(lista) > 0)  # pré-condição
    assert list(reversed(list(reversed(lista)))) == lista

@given(st.text())
def test_strip_property(texto):
    result = texto.strip()
    # Propriedade: strip não deixa espaços nas bordas
    assert len(result) == 0 or (result[0] != ' ' and result[-1] != ' ')
```

```typescript
// fast-check — property-based em TypeScript
import fc from 'fast-check';

describe('Arrays', () => {
    it('reverse deve ser involução', () => {
        fc.assert(
            fc.property(fc.array(fc.anything()), (arr) => {
                expect(arr.reverse().reverse()).toEqual(arr);
            })
        );
    });

    it('filter deve preservar o predicado', () => {
        fc.assert(
            fc.property(fc.array(fc.integer()), (arr) => {
                const pares = arr.filter(n => n % 2 === 0);
                expect(pares.every(n => n % 2 === 0)).toBe(true);
            })
        );
    });
});
```

## Test Coverage

O que medir e como interpretar:

```bash
# pytest-cov
pytest --cov=src --cov-report=term-missing --cov-report=html
```

```ini
# .coveragerc — o que ignorar
[run]
omit =
    */migrations/*
    */tests/*
    */management/commands/*
    */settings/*
    conftest.py

[report]
exclude_lines =
    pragma: no cover
    def __str__
    def __repr__
    def __len__
    if __name__ == "__main__":
    raise NotImplementedError
    raise AssertionError
```

### Métricas relevantes vs irrelevantes

- **Line coverage** — útil mas enganoso. 100% de cobertura ≠ código livre de bugs.
- **Branch coverage** — mais importante. Testa cada caminho condicional.
- **Path coverage** — combinações de branches. Caro, mas robusto.

```python
# Exemplo: 100% line coverage, 50% branch coverage
def validar_idade(idade: int) -> bool:
    if idade < 0:     # nunca testado (branch)
        return False
    return idade >= 18  # sempre testado
```

## Testes em APIs

```python
# FastAPI + pytest + httpx
from fastapi import FastAPI
from httpx import AsyncClient, ASGITransport
import pytest

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@pytest.mark.anyio
async def test_read_item():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/items/42?q=teste")

    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "teste"}

# Fixture para banco de teste
@pytest.fixture
async def client():
    app.dependency_overrides[get_db] = lambda: test_db
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
    app.dependency_overrides.clear()
```

```typescript
// Supertest — testes de API Express
import request from 'supertest';
import app from '../app';

describe('GET /api/usuarios/:id', () => {
    it('retorna 200 com usuário válido', async () => {
        const res = await request(app)
            .get('/api/usuarios/1')
            .set('Authorization', `Bearer ${token}`)
            .expect(200);

        expect(res.body).toHaveProperty('id', 1);
        expect(res.body).toHaveProperty('nome');
    });

    it('retorna 404 para ID inexistente', async () => {
        await request(app)
            .get('/api/usuarios/99999')
            .expect(404);
    });

    it('retorna 401 sem token', async () => {
        await request(app)
            .get('/api/usuarios/1')
            .expect(401);
    });
});
```

### Testes de Contrato

```python
# Pact — testes de contrato entre serviços
from pact import Consumer, Provider

pact = Consumer("ServicoA").has_pact_with(Provider("ServicoB"))
pact.start_service()

pact.given("usuário existe").upon_receiving(
    "requisição de dados"
).with_request("GET", "/users/1").will_respond_with(200, body={
    "id": 1,
    "nome": "João",
    "email": "joao@email.com"
})

with pact:
    resultado = servico_a.buscar_usuario(1)
    assert resultado["nome"] == "João"
```

## Testes em Frontend

### React Testing Library

Foco em testar comportamento (não implementação). Princípio: quanto mais seus testes se parecem com como o software é usado, mais confiança eles dão.

```typescript
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { LoginForm } from './LoginForm';

describe('LoginForm', () => {
    it('renderiza campos de email e senha', () => {
        render(<LoginForm />);

        expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/senha/i)).toBeInTheDocument();
        expect(screen.getByRole('button', { name: /entrar/i })).toBeInTheDocument();
    });

    it('mostra erro para email inválido', async () => {
        render(<LoginForm />);

        const user = userEvent.setup();
        await user.type(screen.getByLabelText(/email/i), 'invalido');
        await user.click(screen.getByRole('button', { name: /entrar/i }));

        await waitFor(() => {
            expect(screen.getByText(/email inválido/i)).toBeInTheDocument();
        });
    });

    it('chama onSubmit com dados válidos', async () => {
        const onSubmit = vi.fn();
        render(<LoginForm onSubmit={onSubmit} />);

        const user = userEvent.setup();
        await user.type(screen.getByLabelText(/email/i), 'joao@email.com');
        await user.type(screen.getByLabelText(/senha/i), '123456');
        await user.click(screen.getByRole('button', { name: /entrar/i }));

        await waitFor(() => {
            expect(onSubmit).toHaveBeenCalledWith({
                email: 'joao@email.com',
                password: '123456',
            });
        });
    });
});
```

### Playwright

Testes E2E com múltiplos navegadores. Suporta mobile, interceptação de rede e snapshot visual.

```typescript
import { test, expect } from '@playwright/test';

test('usuário completa fluxo de compra', async ({ page }) => {
    await page.goto('/');

    // Login
    await page.fill('[data-testid="email"]', 'joao@email.com');
    await page.fill('[data-testid="senha"]', '123456');
    await page.click('[data-testid="entrar"]');
    await expect(page.locator('[data-testid="saudacao"]')).toContainText('João');

    // Buscar produto
    await page.fill('[data-testid="busca"]', 'teclado mecânico');
    await page.press('[data-testid="busca"]', 'Enter');
    await page.click('.produto:first-child a');

    // Adicionar ao carrinho
    await page.click('[data-testid="adicionar-carrinho"]');
    await expect(page.locator('[data-testid="carrinho-count"]')).toContainText('1');

    // Checkout
    await page.click('[data-testid="checkout"]');
    await page.fill('[name="endereco"]', 'Rua A, 123');
    await page.click('[data-testid="confirmar-pagamento"]');

    await expect(page.locator('[data-testid="confirmacao"]')).toBeVisible();
    await expect(page.locator('[data-testid="numero-pedido"]')).not.toBeEmpty();
});
```

### Cypress

```typescript
describe('Dashboard', () => {
    beforeEach(() => {
        cy.intercept('GET', '/api/dashboard', {
            fixture: 'dashboard.json'
        }).as('getDashboard');

        cy.visit('/dashboard');
    });

    it('exibe gráfico de vendas', () => {
        cy.wait('@getDashboard');
        cy.get('[data-testid="grafico-vendas"]').should('be.visible');
        cy.get('[data-testid="total-mes"]').should('contain', 'R$ 50.000');
    });

    it('filtra por período', () => {
        cy.get('[data-testid="filtro-data"]').click();
        cy.get('[data-testid="ultimos-7-dias"]').click();
        cy.wait('@getDashboard');
        cy.url().should('include', 'periodo=7d');
    });
});
```

## Testes de Mutação

Teste de mutação introduz pequenas alterações (mutações) no código e verifica se os testes existentes as detectam. Quanto mais mutações sobrevivem, mais frágil é a suíte de testes.

```python
# MutPy — mutation testing para Python
# pip install mutpy

# Código original
def soma(a, b):
    return a + b

# Mutações geradas automaticamente:
# 1. return a - b   (substitui + por -)
# 2. return a       (remove segundo operando)
# 3. return b       (remove primeiro operando)
# 4. return 0       (remove operação)

# Se os testes não detectarem a mutação → mutante sobreviveu → testes fracos

# Comando:
# mut.py --target src/soma.py --unit-test tests/test_soma.py
```

```bash
# Stryker — mutation testing para JS/TS
npx stryker run
```

```json
// stryker.conf.json
{
    "testRunner": "vitest",
    "mutate": ["src/**/*.ts", "!src/**/*.d.ts"],
    "thresholds": { "high": 80, "low": 60, "break": 50 },
    "reporters": ["html", "progress", "dashboard"]
}
```

```python
# Coverage vs Mutation: exemplo de teste que passa mas não pega mutação
# Mutação: trocar >= por >
def is_maior_de_idade(idade):
    return idade >= 18

# Esse teste passa, mas NÃO detectaria a mutação >= → >
def test_is_maior_de_idade():
    assert is_maior_de_idade(18) == True
    # Faltou testar: assert is_maior_de_idade(17) == False
```

## CI/CD Integration

```yaml
# .github/workflows/test.yml
name: Test Suite

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r requirements-dev.txt

      - name: Run linting
        run: ruff check src/

      - name: Run type checking
        run: mypy src/

      - name: Run tests
        run: pytest --cov=src --cov-fail-under=80 --timeout=30

      - name: Run mutation tests
        run: mut.py --target src/ --unit-test tests/ --timeout=5

      - name: Upload coverage
        uses: codecov/codecov-action@v4
```

```yaml
# Cache de dependências e resultados de teste
- name: Cache pytest
  uses: actions/cache@v4
  with:
    path: .pytest_cache
    key: pytest-${{ hashFiles('requirements-dev.txt') }}
```

## Boas Práticas

### Estrutura de Testes

```python
# Arrange-Act-Assert (AAA)

def test_criacao_pedido():
    # Arrange
    usuario = Usuario(nome="João", saldo=100)
    produto = Produto(nome="Livro", preco=30)

    # Act
    pedido = Pedido.criar(usuario, [produto])

    # Assert
    assert pedido.total == 30
    assert usuario.saldo == 70
    assert len(pedido.itens) == 1
```

### F.I.R.S.T. Principles

| Princípio | Significado |
|-----------|-------------|
| **F**ast | Testes devem rodar rápido (ms) |
| **I**solated | Um teste não depende de outro |
| **R**epeatable | Mesmo resultado em qualquer ambiente |
| **S**elf-validating | Passa ou falha, sem interpretação manual |
| **T**imely | Testes escritos na hora certa (antes do código) |

### Anti-patterns

```python
# ❌ Teste acoplado a implementação
def test_soma():
    calc = Calculadora()
    assert calc._resultado == 0  # acessa atributo privado

# ✅ Teste de comportamento
def test_soma():
    calc = Calculadora()
    assert calc.somar(2, 3) == 5

# ❌ Teste com múltiplos asserts desconexos
def test_usuario():
    user = Usuario("João", "joao@email.com")
    assert user.nome == "João"
    assert user.email == "joao@email.com"
    assert user.ativo == True
    assert user.pontos == 0

# ✅ Um conceito por teste
def test_cria_usuario_com_nome():
    user = Usuario("João", "joao@email.com")
    assert user.nome == "João"

def test_cria_usuario_ativo_por_default():
    user = Usuario("João", "joao@email.com")
    assert user.ativo == True

# ❌ Teste tocando rede/externa sem mock
def test_api_externa():
    data = requests.get("https://api.exemplo.com").json()
    assert data["status"] == "ok"
```

## Referências

- **Kent Beck — "Test-Driven Development: By Example"** (2002). O livro fundador do TDD.
- **Martin Fowler — "Refactoring: Improving the Design of Existing Code"** (2018). Testes são condição para refatoração segura.
- **Roy Osherove — "The Art of Unit Testing"** (2013). Guia prático de testes unitários.
- **Vladimir Khorikov — "Unit Testing Principles, Practices, and Patterns"** (2020). Abordagem moderna com foco em comportamento, não implementação.
- **Matt Wynne, Aslak Hellesøy — "The Cucumber Book"** (2017). BDD e testes de aceitação.
- **"Hypothesis: Property-Based Testing for Python"** — https://hypothesis.works/
- **"fast-check: Property Based Testing in TypeScript"** — https://fast-check.dev/
- **"Playwright: Fast and reliable end-to-end testing"** — https://playwright.dev/
- **"Testing Library"** — https://testing-library.com/
- **"Stryker Mutator: Mutation Testing for JavaScript and TypeScript"** — https://stryker-mutator.io/
- **"MutPy: Mutation Testing for Python"** — https://github.com/mutpy/mutpy
