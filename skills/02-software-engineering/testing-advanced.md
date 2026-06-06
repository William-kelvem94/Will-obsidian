---
tags: [testing, tdd, bdd, property-based-testing, mutation-testing, integration-testing, e2e, mocking, performance-testing, ci-cd, skills-eng]
updated: 2026-06-05
title: "Testing Advanced"
date: 2026-06-01
---

# Testes Avancados para Engenharia de Software

Guia completo de praticas avancadas de testes para agentes de codificacao.

---

## TDD (Test-Driven Development)

### Ciclo Red-Green-Refactor

```
    +-------+     +-------+     +-----------+
    |  RED  | --> | GREEN | --> | REFACTOR  |
    |       |     |       |     |           |
    | Escreve |     | Faz     |     | Melhora     |
    | teste   |     | passar  |     | o codigo    |
    | falhando|     | o teste |     |             |
    +-------+     +-------+     +-----------+
         ^                              |
         |         +-------+            |
         +-------- | Repete | <---------+
                   +-------+
```

1. **RED**: Escreva um teste que falha (o comportamento ainda nao existe)
2. **GREEN**: Escreva o codigo minimo para fazer o teste passar
3. **REFACTOR**: Melhore o codigo sem alterar o comportamento

### Outside-in vs Inside-out TDD

| Aspecto | Outside-in | Inside-out |
|---------|-----------|------------|
| Inicio | Interface/camada externa | Componentes internos |
| Foco | Comportamento do usuario | Implementacao interna |
| Mocks | Muitos mocks iniciais | Menos mocks |
| Ideal para | Sistemas orientados a UX | Bibliotecas/algoritmos |
| Risco | Testes acoplados a interface | Perder visao do todo |

### Exemplo Completo TDD: Validador de Senha

**Passo 1 - RED (Teste inicial):**

```python
# test_password_validator.py
import pytest
from password_validator import validate_password

def test_password_min_length():
    with pytest.raises(ValueError, match="minimo de 8 caracteres"):
        validate_password("short")
```

```typescript
// password-validator.test.ts
import { validatePassword } from './password-validator'

describe('validatePassword', () => {
  it('deve rejeitar senhas com menos de 8 caracteres', () => {
    expect(() => validatePassword('short')).toThrow(
      'minimo de 8 caracteres'
    )
  })
})
```

**Passo 2 - GREEN (Implementacao minima):**

```python
# password_validator.py
def validate_password(password: str) -> bool:
    if len(password) < 8:
        raise ValueError("minimo de 8 caracteres")
    return True
```

```typescript
// password-validator.ts
export function validatePassword(password: string): boolean {
  if (password.length < 8) {
    throw new Error('minimo de 8 caracteres')
  }
  return true
}
```

**Passo 3 - Adicionar mais testes (RED novamente):**

```python
def test_password_requires_uppercase():
    with pytest.raises(ValueError, match="deve conter letra maiuscula"):
        validate_password("alllowercase1!")

def test_password_requires_digit():
    with pytest.raises(ValueError, match="deve conter um digito"):
        validate_password("NoDigitsHere!")

def test_password_valid():
    assert validate_password("ValidPass1!") is True
```

```typescript
it('deve rejeitar senhas sem letra maiuscula', () => {
  expect(() => validatePassword('alllowercase1!')).toThrow(
    'deve conter letra maiuscula'
  )
})

it('deve rejeitar senhas sem digito', () => {
  expect(() => validatePassword('NoDigitsHere!')).toThrow(
    'deve conter um digito'
  )
})

it('deve aceitar senha valida', () => {
  expect(validatePassword('ValidPass1!')).toBe(true)
})
```

**Passo 4 - GREEN (Implementacao completa):**

```python
import re

def validate_password(password: str) -> bool:
    if len(password) < 8:
        raise ValueError("minimo de 8 caracteres")
    if not re.search(r'[A-Z]', password):
        raise ValueError("deve conter letra maiuscula")
    if not re.search(r'\d', password):
        raise ValueError("deve conter um digito")
    return True
```

```typescript
export function validatePassword(password: string): boolean {
  if (password.length < 8) {
    throw new Error('minimo de 8 caracteres')
  }
  if (!/[A-Z]/.test(password)) {
    throw new Error('deve conter letra maiuscula')
  }
  if (!/\d/.test(password)) {
    throw new Error('deve conter um digito')
  }
  return true
}
```

**Passo 5 - REFACTOR:**

```python
import re
from dataclasses import dataclass

@dataclass
class PasswordRule:
    pattern: re.Pattern
    message: str

RULES = [
    PasswordRule(re.compile(r'.{8,}'), "minimo de 8 caracteres"),
    PasswordRule(re.compile(r'[A-Z]'), "deve conter letra maiuscula"),
    PasswordRule(re.compile(r'\d'), "deve conter um digito"),
    PasswordRule(re.compile(r'[!@#$%^&*]'), "deve conter caractere especial"),
]

def validate_password(password: str) -> bool:
    for rule in RULES:
        if not rule.pattern.search(password):
            raise ValueError(rule.message)
    return True
```

```typescript
interface PasswordRule {
  pattern: RegExp
  message: string
}

const RULES: PasswordRule[] = [
  { pattern: /.{8,}/, message: 'minimo de 8 caracteres' },
  { pattern: /[A-Z]/, message: 'deve conter letra maiuscula' },
  { pattern: /\d/, message: 'deve conter um digito' },
  { pattern: /[!@#$%^&*]/, message: 'deve conter caractere especial' },
]

export function validatePassword(password: string): boolean {
  for (const rule of RULES) {
    if (!rule.pattern.test(password)) {
      throw new Error(rule.message)
    }
  }
  return true
}
```

---

## BDD (Behavior-Driven Development)

### Sintaxe Gherkin (Given/When/Then)

```gherkin
# features/autenticacao.feature
Funcionalidade: Autenticacao de usuario

  Cenario: Login bem-sucedido
    Dado que o usuario "joao" existe no sistema
    E a senha do usuario e "Senha123!"
    Quando eu faco login com "joao" e "Senha123!"
    Entao devo ver a pagina do dashboard
    E o token de sessao deve ser valido

  Cenario: Login com credenciais invalidas
    Dado que o usuario "joao" existe no sistema
    Quando eu faco login com "joao" e "senha_errada"
    Entao devo ver a mensagem "Credenciais invalidas"
    E nao devo ser redirecionado

  Cenario Outline: Bloqueio apos tentativas falhas
    Dado que o usuario "maria" existe no sistema
    Quando eu faco login com "maria" e "errada" <tentativas> vezes
    Entao a conta deve estar <estado>

    Exemplos:
      | tentativas | estado           |
      | 3          | ativa            |
      | 5          | temporariamente_bloqueada |
```

### Step Definitions em Python (Behave)

```python
# steps/autenticacao_steps.py
from behave import given, when, then
from app.auth import AuthService

@given('que o usuario "{username}" existe no sistema')
def step_usuario_existe(context, username):
    context.auth = AuthService()
    context.auth.create_user(username, "Senha123!")

@when('eu faco login com "{username}" e "{password}"')
def step_faco_login(context, username, password):
    context.result = context.auth.login(username, password)

@when('eu faco login com "{username}" e "{password}" {n:d} vezes')
def step_faco_login_repetido(context, username, password, n):
    for _ in range(n):
        try:
            context.auth.login(username, password)
        except Exception:
            pass

@then('devo ver a pagina do dashboard')
def step_vejo_dashboard(context):
    assert context.result['success'] is True
    assert 'token' in context.result

@then('o token de sessao deve ser valido')
def step_token_valido(context):
    token = context.result['token']
    assert context.auth.verify_token(token) is True
```

### Step Definitions em TypeScript (Cucumber.js)

```typescript
// steps/autenticacao.steps.ts
import { Given, When, Then } from '@cucumber/cucumber'
import { expect } from 'chai'
import { AuthService } from '../src/auth'

let context: { auth: AuthService; result: any }

Given('que o usuario {string} existe no sistema', function (username: string) {
  this.auth = new AuthService()
  this.auth.createUser(username, 'Senha123!')
})

When('eu faco login com {string} e {string}', async function (
  username: string,
  password: string
) {
  this.result = await this.auth.login(username, password)
})

Then('devo ver a pagina do dashboard', function () {
  expect(this.result.success).to.be.true
  expect(this.result).to.have.property('token')
})

Then('o token de sessao deve ser valido', function () {
  const token = this.result.token
  expect(this.auth.verifyToken(token)).to.be.true
})
```

### Documentacao Viva

BDD gera documentacao executavel. Os arquivos `.feature` servem como:
- Especificacao do comportamento
- Testes automatizados
- Documentacao para nao-desenvolvedores

Execute com `behave --format=html` ou `cucumber --format=html` para gerar relatorios.

---

## Property-Based Testing

### Conceito

Em vez de exemplos especificos, defina **propriedades** que devem ser verdadeiras para qualquer entrada.

| Tipo | Exemplo | Cobertura |
|------|---------|-----------|
| Baseado em exemplos | `assert add(2, 3) == 5` | Casos especificos |
| Baseado em propriedades | `add(a, b) == add(b, a)` | Infinitos casos |

### Hypothesis (Python)

```python
# test_sorting.py
from hypothesis import given, settings, strategies as st

@given(st.lists(st.integers()))
def test_sort_is_idempotent(numbers):
    """Ordenar duas vezes produz o mesmo resultado"""
    sorted_once = sorted(numbers)
    sorted_twice = sorted(sorted_once)
    assert sorted_once == sorted_twice

@given(st.lists(st.integers(), min_size=1))
def test_sort_preserves_length(numbers):
    """Ordenar nao altera o tamanho da lista"""
    assert len(sorted(numbers)) == len(numbers)

@given(st.lists(st.integers()))
def test_sort_produces_ordered_list(numbers):
    """Resultado esta ordenado"""
    result = sorted(numbers)
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1]

@given(st.lists(st.integers()))
def test_sort_is_permutation(numbers):
    """Resultado e permutacao da entrada"""
    assert sorted(numbers) == sorted(sorted(numbers))
    # Verifica elementos
    from collections import Counter
    assert Counter(numbers) == Counter(sorted(numbers))
```

```python
# test_string_utils.py
from hypothesis import given, strategies as st

@given(st.text(min_size=1))
def test_reverse_twice_is_identity(text):
    """Reverter duas vezes retorna ao original"""
    assert text[::-1][::-1] == text

@given(st.text())
def test_reverse_preserves_length(text):
    assert len(text[::-1]) == len(text)

@given(st.text(alphabet=st.characters(blacklist_categories=('Cs',))))
def test_encode_decode_roundtrip(text):
    import base64
    encoded = base64.b64encode(text.encode()).decode()
    decoded = base64.b64decode(encoded).decode()
    assert decoded == text
```

### fast-check (TypeScript)

```typescript
// test-sorting.test.ts
import fc from 'fast-check'

describe('sorting properties', () => {
  it('e idempotente', () => {
    fc.assert(
      fc.property(fc.array(fc.integer()), (numbers) => {
        const sortedOnce = [...numbers].sort((a, b) => a - b)
        const sortedTwice = [...sortedOnce].sort((a, b) => a - b)
        expect(sortedOnce).toEqual(sortedTwice)
      })
    )
  })

  it('preserva o comprimento', () => {
    fc.assert(
      fc.property(fc.array(fc.integer()), (numbers) => {
        const sorted = [...numbers].sort((a, b) => a - b)
        expect(sorted.length).toBe(numbers.length)
      })
    )
  })

  it('produz lista ordenada', () => {
    fc.assert(
      fc.property(fc.array(fc.integer()), (numbers) => {
        const sorted = [...numbers].sort((a, b) => a - b)
        for (let i = 0; i < sorted.length - 1; i++) {
          expect(sorted[i]).toBeLessThanOrEqual(sorted[i + 1])
        }
      })
    )
  })
})
```

### Geradores Customizados

```python
from hypothesis import strategies as st

# Email valido
email_strategy = st.emails()

# CPF brasileiro
@st.composite
def cpf_strategy(draw):
    digits = [draw(st.integers(min_value=0, max_value=9)) for _ in range(9)]
    # Calcular digitos verificadores (simplificado)
    return ''.join(map(str, digits))

# JSON arbitrario
arbitrary_json = st.recursive(
    st.none() | st.booleans() | st.floats() | st.text(),
    lambda children: st.lists(children) | st.dictionaries(st.text(), children),
    max_leaves=10
)
```

```typescript
import fc from 'fast-check'

// Gerador de email
const emailArb = fc
  .string({ minLength: 1, maxLength: 10 })
  .map((s) => `${s}@example.com`)

// Gerador de usuario
const userArb = fc.record({
  id: fc.nat(),
  email: emailArb,
  age: fc.integer({ min: 0, max: 150 }),
  tags: fc.array(fc.string({ minLength: 1 })),
})

// Uso
fc.assert(
  fc.property(userArb, (user) => {
    expect(user.email).toMatch(/@example\.com$/)
    expect(user.age).toBeGreaterThanOrEqual(0)
  })
)
```

### Quando Usar Property-Based Testing

| Use Property-Based | Use Exemplo-Based |
|-------------------|-------------------|
| Funcoes matematicas | Casos de borda conhecidos |
| Algoritmos de ordenacao | Testes de regressao de bugs |
| Serializacao/deserializacao | Documentacao de API |
| Propriedades de invariantes | Cenarios de negocio especificos |
| Fuzzing de parsers | Testes de integracao |

---

## Mutation Testing

### Conceito

Mutation testing modifica seu codigo fonte ("mutantes") e verifica se os testes detectam as mudancas.

```
    Codigo Original
         |
    +----+----+
    |         |
  Mutante 1  Mutante 2  ...  Mutante N
  (if > v)   (if < v)         (+ v -)
    |         |                 |
  Testes    Testes            Testes
    |         |                 |
  FALHOU?   PASSOU?           FALHOU?
    |         |                 |
  Morto    Vivo (problema!)   Morto
```

### Mutmut (Python)

```bash
# Instalacao
pip install mutmut

# Execucao
mutmut run

# Ver mutantes sobreviventes
mutmut results

# Aplicar mutante para investigar
mutmut apply 1
```

```python
# codigo original
def discount(price: float, is_member: bool) -> float:
    if is_member:
        return price * 0.9
    return price

# mutante 1: if is_member -> if True (deve ser pego)
# mutante 2: 0.9 -> 1.0 (deve ser pego)
# mutante 3: 0.9 -> 0.0 (deve ser pego)

# teste que mata todos os mutantes
def test_discount_member():
    assert discount(100, True) == 90.0

def test_discount_non_member():
    assert discount(100, False) == 100.0
```

### Stryker (JavaScript/TypeScript)

```bash
npm install --save-dev @stryker-mutator/core @stryker-mutator/jest-runner
```

```javascript
// stryker.conf.js
module.exports = {
  mutator: 'javascript',
  testRunner: 'jest',
  reporters: ['html', 'clear-text', 'progress'],
  mutate: [
    'src/**/*.ts',
    '!src/**/*.test.ts',
    '!src/**/*.spec.ts',
  ],
  thresholds: {
    high: 80,
    low: 60,
    break: 50,
  },
}
```

```typescript
// src/utils.ts - codigo original
export function clamp(value: number, min: number, max: number): number {
  if (value < min) return min
  if (value > max) return max
  return value
}

// Mutantes gerados pelo Stryker:
// 1. if (value < min) -> if (value <= min)
// 2. if (value > max) -> if (value >= max)
// 3. return min -> return max
// 4. return max -> return min
// 5. return value -> return 0

// Testes que matam todos os mutantes
describe('clamp', () => {
  it('retorna min quando value < min', () => {
    expect(clamp(5, 10, 20)).toBe(10)
  })
  it('retorna max quando value > max', () => {
    expect(clamp(25, 10, 20)).toBe(20)
  })
  it('retorna value quando dentro do intervalo', () => {
    expect(clamp(15, 10, 20)).toBe(15)
  })
})
```

### Interpretando Scores de Mutacao

| Score | Significado | Acao |
|-------|------------|------|
| 90-100% | Excelente | Manter qualidade |
| 70-89% | Bom | Investigar mutantes vivos |
| 50-69% | Regular | Adicionar testes criticos |
| <50% | Ruim | Revisar estrategia de testes |

---

## Testes de Integracao

### Testcontainers

```python
# test_db_integration.py
import pytest
from testcontainers.postgres import PostgresContainer
from sqlalchemy import create_engine, text

@pytest.fixture
def postgres():
    with PostgresContainer("postgres:16") as pg:
        engine = create_engine(pg.get_connection_url())
        with engine.connect() as conn:
            conn.execute(text("CREATE TABLE users (id SERIAL PRIMARY KEY, name TEXT, email TEXT)"))
            conn.commit()
        yield engine

def test_insert_and_query(postgres):
    with postgres.connect() as conn:
        conn.execute(text("INSERT INTO users (name, email) VALUES (:name, :email)"),
                     {"name": "Joao", "email": "joao@test.com"})
        conn.commit()
        result = conn.execute(text("SELECT * FROM users WHERE name = :name"), {"name": "Joao"})
        row = result.fetchone()
        assert row[1] == "Joao"
        assert row[2] == "joao@test.com"
```

```typescript
// test-db-integration.test.ts
import { GenericContainer, StartedTestContainer, Wait } from 'testcontainers'
import { Client } from 'pg'

describe('PostgreSQL Integration', () => {
  let container: StartedTestContainer
  let client: Client

  beforeAll(async () => {
    container = await new GenericContainer('postgres:16')
      .withEnvironment({ POSTGRES_PASSWORD: 'test', POSTGRES_DB: 'testdb' })
      .withExposedPorts(5432)
      .withWaitStrategy(Wait.forLogMessage('database system is ready'))
      .start()

    client = new Client({
      host: container.getHost(),
      port: container.getMappedPort(5432),
      user: 'postgres',
      password: 'test',
      database: 'testdb',
    })
    await client.connect()
    await client.query(`
      CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
      )
    `)
  }, 60000)

  afterAll(async () => {
    await client.end()
    await container.stop()
  })

  it('insere e consulta usuario', async () => {
    await client.query(
      'INSERT INTO users (name, email) VALUES ($1, $2)',
      ['Joao', 'joao@test.com']
    )
    const result = await client.query(
      'SELECT * FROM users WHERE name = $1',
      ['Joao']
    )
    expect(result.rows).toHaveLength(1)
    expect(result.rows[0].email).toBe('joao@test.com')
  })
})
```

### Estrategias de Teste de Banco de Dados

| Estrategia | Velocidade | Isolamento | Uso |
|-----------|-----------|------------|-----|
| Transacao com rollback | Rapida | Alto | Testes unitarios |
| Truncar tabelas | Media | Alto | Testes de integracao |
| Container efemero | Lenta | Maximo | CI/CD |
| Banco em memoria | Rapida | Medio | Desenvolvimento |

### Teste de API com Mocking

```python
# test_api_integration.py
import pytest
from unittest.mock import patch
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_create_order_with_external_payment():
    with patch('app.services.payment.process_payment') as mock_payment:
        mock_payment.return_value = {"status": "approved", "transaction_id": "tx123"}

        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            response = await client.post("/orders", json={
                "user_id": 1,
                "items": [{"product_id": 5, "quantity": 2}],
                "payment_method": "credit_card"
            })

        assert response.status_code == 201
        data = response.json()
        assert data["status"] == "confirmed"
        mock_payment.assert_called_once()
```

```typescript
// test-api-integration.test.ts
import request from 'supertest'
import { app } from '../src/app'
import { paymentService } from '../src/services/payment'

jest.mock('../src/services/payment')

describe('POST /orders', () => {
  it('cria pedido com pagamento externo', async () => {
    ;(paymentService.processPayment as jest.Mock).mockResolvedValue({
      status: 'approved',
      transactionId: 'tx123',
    })

    const response = await request(app)
      .post('/orders')
      .send({
        userId: 1,
        items: [{ productId: 5, quantity: 2 }],
        paymentMethod: 'credit_card',
      })

    expect(response.status).toBe(201)
    expect(response.body.status).toBe('confirmed')
    expect(paymentService.processPayment).toHaveBeenCalledTimes(1)
  })
})
```

---

## Testes E2E Avancados

### Playwright: Fixtures e Page Objects

```typescript
// fixtures/test-fixtures.ts
import { test as base } from '@playwright/test'
import { LoginPage } from '../pages/login-page'
import { DashboardPage } from '../pages/dashboard-page'

export type AppFixtures = {
  loginPage: LoginPage
  dashboardPage: DashboardPage
}

export const test = base.extend<AppFixtures>({
  loginPage: async ({ page }, use) => {
    await use(new LoginPage(page))
  },
  dashboardPage: async ({ page }, use) => {
    await use(new DashboardPage(page))
  },
})

export { expect } from '@playwright/test'
```

```typescript
// pages/login-page.ts
import { Page, Locator } from '@playwright/test'

export class LoginPage {
  readonly page: Page
  readonly emailInput: Locator
  readonly passwordInput: Locator
  readonly submitButton: Locator
  readonly errorMessage: Locator

  constructor(page: Page) {
    this.page = page
    this.emailInput = page.locator('input[name="email"]')
    this.passwordInput = page.locator('input[name="password"]')
    this.submitButton = page.locator('button[type="submit"]')
    this.errorMessage = page.locator('[data-testid="error-message"]')
  }

  async goto() {
    await this.page.goto('/login')
  }

  async login(email: string, password: string) {
    await this.emailInput.fill(email)
    await this.passwordInput.fill(password)
    await this.submitButton.click()
  }
}
```

```typescript
// tests/e2e/auth-flow.spec.ts
import { test, expect } from '../fixtures/test-fixtures'

test.describe('Fluxo de Autenticacao', () => {
  test('login bem-sucedido redireciona para dashboard', async ({
    loginPage,
    dashboardPage,
  }) => {
    await loginPage.goto()
    await loginPage.login('user@test.com', 'Senha123!')

    await expect(dashboardPage.welcomeMessage).toBeVisible()
    await expect(test).toHaveURL(/.*dashboard/)
  })

  test('credenciais invalidas mostram erro', async ({ loginPage }) => {
    await loginPage.goto()
    await loginPage.login('user@test.com', 'senha-errada')

    await expect(loginPage.errorMessage).toBeVisible()
    await expect(loginPage.errorMessage).toContainText('Credenciais invalidas')
  })
})
```

### Teste Visual com Playwright

```typescript
// tests/e2e/visual.spec.ts
import { test, expect } from '@playwright/test'

test('pagina inicial deve corresponder ao snapshot', async ({ page }) => {
  await page.goto('/')
  await expect(page).toHaveScreenshot('homepage.png', {
    fullPage: true,
    maxDiffPixelRatio: 0.02,
  })
})

test('componente de card deve corresponder ao snapshot', async ({ page }) => {
  await page.goto('/components')
  const card = page.locator('[data-testid="product-card"]')
  await expect(card).toHaveScreenshot('product-card.png')
})
```

### Execucao Paralela

```typescript
// playwright.config.ts
import { defineConfig } from '@playwright/test'

export default defineConfig({
  testDir: './tests/e2e',
  fullyParallel: true,
  workers: process.env.CI ? 4 : undefined,
  retries: process.env.CI ? 2 : 0,
  reporter: [['html'], ['junit', { outputFile: 'results.xml' }]],
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    { name: 'chromium', use: { browserName: 'chromium' } },
    { name: 'firefox', use: { browserName: 'firefox' } },
    { name: 'webkit', use: { browserName: 'webkit' } },
  ],
})
```

---

## Mocking e Stubbing

### Diferencas

| Tipo | Comportamento | Uso |
|------|--------------|-----|
| **Stub** | Retorna dados pre-definidos | Simular dependencias |
| **Mock** | Verifica interacoes | Validar chamadas |
| **Spy** | Envolve funcao real | Monitorar chamadas |
| **Fake** | Implementacao simplificada | Substituir servico complexo |

### unittest.mock Avancado (Python)

```python
from unittest.mock import patch, MagicMock, call, AsyncMock
import pytest

# Mock de objeto complexo
def test_email_service():
    mock_smtp = MagicMock()
    mock_smtp.send_email.return_value = {"status": "sent", "id": "msg-123"}

    service = EmailService(smtp=mock_smtp)
    result = service.send_welcome_email("user@test.com")

    assert result["status"] == "sent"
    mock_smtp.send_email.assert_called_once_with(
        to="user@test.com",
        subject="Bem-vindo!",
        body=ANY
    )

# AsyncMock para funcoes assincronas
@pytest.mark.asyncio
async def test_async_api_call():
    mock_client = AsyncMock()
    mock_client.get.return_value.json.return_value = {"data": [1, 2, 3]}

    service = DataService(client=mock_client)
    result = await service.fetch_data()

    assert result == [1, 2, 3]
    mock_client.get.assert_called_once_with("/api/data")

# patch como decorator
@patch('app.services.external_api.get')
def test_with_patch(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"id": 1}

    result = fetch_user(1)
    assert result["id"] == 1

# patch como context manager
def test_with_context_manager():
    with patch('app.cache.redis_client') as mock_redis:
        mock_redis.get.return_value = None  # Cache miss
        result = get_user_with_cache(1)
        mock_redis.set.assert_called_once()

# side_effect para sequencia de retornos
def test_side_effect_sequence():
    mock_api = MagicMock()
    mock_api.call.side_effect = [
        {"status": "pending"},
        {"status": "processing"},
        {"status": "completed"},
    ]

    assert mock_api.call()["status"] == "pending"
    assert mock_api.call()["status"] == "processing"
    assert mock_api.call()["status"] == "completed"

# side_effect para excecoes
def test_side_effect_exception():
    mock_api = MagicMock()
    mock_api.call.side_effect = ConnectionError("timeout")

    with pytest.raises(ConnectionError):
        mock_api.call()
```

### Jest Mocking Patterns (TypeScript)

```typescript
// jest.mock de modulo inteiro
jest.mock('../src/services/payment', () => ({
  processPayment: jest.fn().mockResolvedValue({
    status: 'approved',
    transactionId: 'tx-123',
  }),
}))

// jest.spyOn
describe('UserService', () => {
  it('monitora chamadas do repositorio', () => {
    const repo = new UserRepository()
    const spy = jest.spyOn(repo, 'findById')

    const service = new UserService(repo)
    service.getUser(1)

    expect(spy).toHaveBeenCalledWith(1)
    expect(spy).toHaveBeenCalledTimes(1)

    spy.mockRestore()
  })
})

// mockImplementation
jest.mock('axios')
const mockedAxios = axios as jest.Mocked<typeof axios>

it('usa mockImplementation', async () => {
  mockedAxios.get.mockImplementation(async (url) => {
    if (url === '/users/1') {
      return { data: { id: 1, name: 'Joao' } }
    }
    throw new Error('Not found')
  })

  const user = await fetchUser(1)
  expect(user.name).toBe('Joao')
})

// mock de modulo com factory dinamica
jest.mock('../src/config', () => ({
  __esModule: true,
  default: jest.fn(() => ({
    apiUrl: 'http://test-api',
    timeout: 1000,
  })),
}))
```

### HTTP Mocking

```python
# responses (Python - requests)
import responses
import requests

@responses.activate
def test_api_call():
    responses.add(
        responses.GET,
        'https://api.example.com/users/1',
        json={'id': 1, 'name': 'Joao'},
        status=200
    )

    resp = requests.get('https://api.example.com/users/1')
    assert resp.json()['name'] == 'Joao'

# httpx mock (Python - httpx)
import httpx
from pytest_httpx import HTTPXMock

@pytest.mark.asyncio
async def test_async_httpx(HTTPXMock: HTTPXMock):
    HTTPXMock.add_response(
        url='https://api.example.com/data',
        json={'key': 'value'},
        status_code=200,
    )

    async with httpx.AsyncClient() as client:
        resp = await client.get('https://api.example.com/data')
        assert resp.json()['key'] == 'value'
```

```typescript
// nock (Node.js)
import nock from 'nock'
import axios from 'axios'

describe('API call', () => {
  afterEach(() => nock.cleanAll())

  it('mocks GET request', async () => {
    nock('https://api.example.com')
      .get('/users/1')
      .reply(200, { id: 1, name: 'Joao' })

    const response = await axios.get('https://api.example.com/users/1')
    expect(response.data.name).toBe('Joao')
  })

  it('mocks com delay', async () => {
    nock('https://api.example.com')
      .get('/slow')
      .delay(1000)
      .reply(200, { data: 'ready' })

    const start = Date.now()
    const response = await axios.get('https://api.example.com/slow')
    expect(Date.now() - start).toBeGreaterThanOrEqual(900)
  })
})

// MSW (Mock Service Worker) - Browser e Node
import { http, HttpResponse } from 'msw'
import { setupServer } from 'msw/node'

const server = setupServer(
  http.get('https://api.example.com/users/:id', ({ params }) => {
    return HttpResponse.json({ id: params.id, name: 'Joao' })
  }),
  http.post('https://api.example.com/users', async ({ request }) => {
    const body = await request.json()
    return HttpResponse.json({ id: 1, ...body }, { status: 201 })
  })
)

beforeAll(() => server.listen())
afterEach(() => server.resetHandlers())
afterAll(() => server.close())
```

---

## Testes de Performance

### Load Testing com k6

```javascript
// load-test.js
import http from 'k6/http'
import { check, sleep } from 'k6'
import { Rate } from 'k6/metrics'

// Metricas customizadas
const errorRate = new Rate('errors')

export const options = {
  stages: [
    { duration: '30s', target: 20 },    // Ramp-up para 20 usuarios
    { duration: '1m', target: 20 },     // Mantem 20 usuarios
    { duration: '30s', target: 50 },    // Pico para 50 usuarios
    { duration: '1m', target: 50 },     // Mantem pico
    { duration: '30s', target: 0 },     // Ramp-down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],   // 95% das reqs < 500ms
    http_req_failed: ['rate<0.05'],     // Menos de 5% de erros
    errors: ['rate<0.1'],               // Menos de 10% de erros customizados
  },
}

export default function () {
  // Teste de login
  const loginRes = http.post('http://localhost:3000/api/auth/login', JSON.stringify({
    email: 'user@test.com',
    password: 'Senha123!',
  }), {
    headers: { 'Content-Type': 'application/json' },
  })

  const loginOk = check(loginRes, {
    'login status is 200': (r) => r.status === 200,
    'has token': (r) => JSON.parse(r.body).token !== undefined,
  })

  errorRate.add(!loginOk)

  if (loginOk) {
    const token = JSON.parse(loginRes.body).token

    // Teste de API autenticada
    const dataRes = http.get('http://localhost:3000/api/users/profile', {
      headers: { Authorization: `Bearer ${token}` },
    })

    check(dataRes, {
      'profile status is 200': (r) => r.status === 200,
      'has user data': (r) => JSON.parse(r.body).email !== undefined,
    })
  }

  sleep(1)
}
```

```bash
# Execucao
k6 run load-test.js
k6 run --out json=results.json load-test.js
k6 run --out influxdb=http://localhost:8086/k6 load-test.js
```

### Benchmarking com pytest-benchmark

```python
# test_benchmarks.py
import pytest

def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def test_fibonacci_comparison(benchmark):
    # Benchmark recursivo
    result_recursive = benchmark(fibonacci_recursive, 20)

    # Benchmark iterativo
    result_iterative = benchmark(fibonacci_iterative, 20)

    assert result_recursive == result_iterative == 6765

def test_list_comprehension_vs_map(benchmark):
    data = list(range(10000))

    # List comprehension
    result_comp = benchmark(lambda: [x * 2 for x in data])

    # Map
    result_map = benchmark(lambda: list(map(lambda x: x * 2, data)))

    assert result_comp == result_map
```

```bash
pytest --benchmark-only --benchmark-compare --benchmark-histogram
```

---

## Automatizacao de Testes em CI/CD

### Execucao Paralela

```yaml
# .github/workflows/test-parallel.yml
name: Testes Paralelos

on: [push, pull_request]

jobs:
  test-unit:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.11', '3.12']
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: pip install -r requirements-dev.txt
      - run: pytest tests/unit/ -n auto --cov=app

  test-integration:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: test
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements-dev.txt
      - run: pytest tests/integration/ -v

  test-e2e:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npx playwright install --with-deps
      - run: npm run test:e2e
      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: playwright-report
          path: playwright-report/
```

### Deteccao de Testes Flaky

```python
# conftest.py - Plugin de deteccao de flaky tests
import pytest
from collections import defaultdict

test_results = defaultdict(list)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    test_results[item.nodeid].append(result.outcome)

def pytest_sessionfinish(session, exitstatus):
    flaky_tests = {
        test: results
        for test, results in test_results.items()
        if len(set(results)) > 1  # Mistura de pass/fail
    }
    if flaky_tests:
        print("\n=== TESTES FLAKY DETECTADOS ===")
        for test, results in flaky_tests.items():
            print(f"  {test}: {results}")
```

### Thresholds de Coverage

```toml
# pyproject.toml
[tool.pytest.ini_options]
addopts = """
  --cov=app
  --cov-report=html
  --cov-report=term-missing
  --cov-fail-under=80
"""

[tool.coverage.run]
source = ["app"]
omit = ["*/tests/*", "*/migrations/*"]

[tool.coverage.report]
fail_under = 80
show_missing = true
exclude_lines = [
    "pragma: no cover",
    "if TYPE_CHECKING:",
    "raise NotImplementedError",
]
```

```json
// package.json - Jest coverage
{
  "jest": {
    "coverageThreshold": {
      "global": {
        "branches": 80,
        "functions": 85,
        "lines": 85,
        "statements": 85
      }
    }
  }
}
```

---

## Referencias Cruzadas

- [[testing/SKILL]] - Fundamentos de testes
- [[devops/ci-cd/github-actions]] - Automatizacao CI/CD
- [[backend]] - Arquitetura backend
- [[performance]] - Otimizacao de performance
