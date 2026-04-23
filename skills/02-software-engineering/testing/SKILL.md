---
title: "Testing Architecture"
description: "Comprehensive testing strategies for full-stack applications"
tags: [testing, tdd, quality-assurance, automation, best-practices]
updated: 2026-04-23
---

# Testing Architecture Skill

Complete guide to building robust testing systems.

---

## 🎯 Testing Philosophy

### The Testing Pyramid

```
        /\
       /  \      E2E Tests (5-10%)
      /    \     - Slow, expensive
     /------\    - Test critical user flows
    /        \
   /  Integ.  \  Integration Tests (20-30%)
  /   Tests    \ - Test component interactions
 /--------------\
/                \
/  Unit Tests     \ Unit Tests (60-70%)
/   (Foundation)   \ - Fast, isolated
---------------------- - Test individual functions
```

**Key principles:**
1. **Most tests should be fast** (unit tests)
2. **Test user behavior**, not implementation
3. **Test what can break**, not everything
4. **Maintainable tests** are as important as maintainable code

---

## 🧪 Testing Levels

### 1. Unit Tests

**What:** Test individual functions/methods in isolation

**When:** Always. Should be majority of tests.

**Tools:**
- Python: `pytest`, `unittest`
- JavaScript: `Jest`, `Vitest`
- TypeScript: `Jest` with `ts-jest`

**Example (Python):**
```python
# calculator.py
def add(a: int, b: int) -> int:
    return a + b

# test_calculator.py
import pytest
from calculator import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_mixed_numbers():
    assert add(-2, 5) == 3
```

**Example (TypeScript/Jest):**
```typescript
// calculator.ts
export function add(a: number, b: number): number {
  return a + b
}

// calculator.test.ts
import { add } from './calculator'

describe('add', () => {
  it('adds positive numbers', () => {
    expect(add(2, 3)).toBe(5)
  })
  
  it('adds negative numbers', () => {
    expect(add(-2, -3)).toBe(-5)
  })
})
```

---

### 2. Integration Tests

**What:** Test interactions between components (DB, API, services)

**When:** For critical paths and data flows

**Tools:**
- Python: `pytest` with fixtures, `httpx` for API testing
- JavaScript: `Jest`, `Supertest`
- Database: Test containers (Docker), in-memory DBs

**Example (FastAPI + Database):**
```python
# test_api_integration.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db

# Test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Setup
@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine)
    
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as c:
        yield c
    
    Base.metadata.drop_all(bind=engine)

# Tests
def test_create_user(client):
    response = client.post(
        "/users",
        json={"email": "test@example.com", "name": "Test User"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_get_user(client):
    # Create user
    create_response = client.post(
        "/users",
        json={"email": "test@example.com", "name": "Test"}
    )
    user_id = create_response.json()["id"]
    
    # Get user
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
```

**Example (Next.js API Routes):**
```typescript
// __tests__/api/users.test.ts
import { createMocks } from 'node-mocks-http'
import handler from '@/app/api/users/route'

describe('/api/users', () => {
  it('returns users list', async () => {
    const { req, res } = createMocks({
      method: 'GET',
    })
    
    await handler(req, res)
    
    expect(res._getStatusCode()).toBe(200)
    expect(JSON.parse(res._getData())).toEqual(
      expect.arrayContaining([
        expect.objectContaining({ email: expect.any(String) })
      ])
    )
  })
})
```

---

### 3. E2E (End-to-End) Tests

**What:** Test full user flows in browser

**When:** Critical user paths (signup, checkout, login)

**Tools:**
- **Playwright** (recommended) - Fast, reliable, multi-browser
- **Cypress** - Developer-friendly, great DX
- **Selenium** - Legacy, still widely used

**Example (Playwright):**
```typescript
// tests/e2e/login.spec.ts
import { test, expect } from '@playwright/test'

test.describe('Login flow', () => {
  test('user can login successfully', async ({ page }) => {
    // Navigate
    await page.goto('http://localhost:3000/login')
    
    // Fill form
    await page.fill('input[name="email"]', 'test@example.com')
    await page.fill('input[name="password"]', 'password123')
    
    // Submit
    await page.click('button[type="submit"]')
    
    // Assert redirect
    await expect(page).toHaveURL('http://localhost:3000/dashboard')
    
    // Assert UI update
    await expect(page.locator('text=Welcome back')).toBeVisible()
  })
  
  test('shows error for invalid credentials', async ({ page }) => {
    await page.goto('http://localhost:3000/login')
    
    await page.fill('input[name="email"]', 'test@example.com')
    await page.fill('input[name="password"]', 'wrongpassword')
    await page.click('button[type="submit"]')
    
    // Assert error message
    await expect(page.locator('text=Invalid credentials')).toBeVisible()
  })
})
```

---

## 🏗️ Test Organization

### Directory Structure

```
project/
├── src/
│   ├── components/
│   ├── utils/
│   └── api/
├── tests/
│   ├── unit/
│   │   ├── components/
│   │   └── utils/
│   ├── integration/
│   │   ├── api/
│   │   └── database/
│   ├── e2e/
│   │   ├── auth.spec.ts
│   │   ├── checkout.spec.ts
│   │   └── dashboard.spec.ts
│   ├── fixtures/
│   │   ├── users.json
│   │   └── posts.json
│   └── helpers/
│       ├── setup.ts
│       └── factories.ts
└── pytest.ini / jest.config.js
```

---

## 🎭 Test Patterns

### Pattern 1: Arrange-Act-Assert (AAA)

```python
def test_user_creation():
    # Arrange - Setup
    email = "test@example.com"
    name = "Test User"
    
    # Act - Execute
    user = create_user(email=email, name=name)
    
    # Assert - Verify
    assert user.email == email
    assert user.name == name
    assert user.id is not None
```

### Pattern 2: Given-When-Then (BDD)

```python
def test_shopping_cart():
    # Given - Initial state
    cart = ShoppingCart()
    product = Product(name="Book", price=10)
    
    # When - Action
    cart.add(product)
    
    # Then - Expected outcome
    assert len(cart.items) == 1
    assert cart.total == 10
```

### Pattern 3: Test Fixtures

```python
# conftest.py (pytest)
@pytest.fixture
def db_session():
    """Create test database session"""
    session = create_test_session()
    yield session
    session.close()

@pytest.fixture
def sample_user(db_session):
    """Create sample user for testing"""
    user = User(email="test@example.com")
    db_session.add(user)
    db_session.commit()
    return user

# Usage in test
def test_update_user(db_session, sample_user):
    sample_user.name = "Updated"
    db_session.commit()
    
    assert sample_user.name == "Updated"
```

### Pattern 4: Factories

```typescript
// factories/userFactory.ts
export function createUser(overrides = {}) {
  return {
    id: 1,
    email: 'test@example.com',
    name: 'Test User',
    createdAt: new Date(),
    ...overrides
  }
}

// test
it('formats user name', () => {
  const user = createUser({ name: 'Alice' })
  expect(formatUserName(user)).toBe('Alice')
})
```

---

## 🔧 Testing Tools by Stack

### Python (FastAPI)

```bash
# Install
pip install pytest pytest-asyncio httpx

# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*

# Run tests
pytest
pytest -v  # Verbose
pytest tests/unit/  # Specific directory
pytest -k "test_user"  # Match pattern
pytest --cov=app --cov-report=html  # Coverage
```

### TypeScript (Next.js)

```bash
# Install
npm install -D jest @testing-library/react @testing-library/jest-dom

# jest.config.js
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1',
  },
}

# Run tests
npm test
npm test -- --watch  # Watch mode
npm test -- --coverage  # Coverage
```

### E2E (Playwright)

```bash
# Install
npm install -D @playwright/test

# playwright.config.ts
export default {
  testDir: './tests/e2e',
  use: {
    baseURL: 'http://localhost:3000',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
}

# Run tests
npx playwright test
npx playwright test --ui  # UI mode
npx playwright test --debug  # Debug mode
npx playwright codegen  # Generate tests
```

---

## 🎯 What to Test

### ✅ DO Test

- **Business logic** - Core functionality
- **Edge cases** - Null, empty, large inputs
- **Error handling** - What happens when things fail
- **User interactions** - Click, type, navigate
- **API contracts** - Request/response shapes
- **State management** - Redux, Context, Zustand
- **Authentication** - Login, logout, permissions

### ❌ DON'T Test

- **Third-party libraries** - They have their own tests
- **Implementation details** - How it's done
- **Framework behavior** - React, FastAPI internals
- **Trivial code** - Getters/setters
- **Constants** - Hard-coded values

---

## 🚀 Test Automation (CI/CD)

### GitHub Actions

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      
      - name: Run tests
        run: pytest --cov=app --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage.xml
```

---

## 🔗 Related Resources

- [[JARVIS/04-Engineering/Wiki/CheatSheets/FastAPI|FastAPI Cheat Sheet]]
- [[JARVIS/04-Engineering/Wiki/CheatSheets/Next.js|Next.js Cheat Sheet]]
- [[skills/02-software-engineering|Software Engineering Skills]]
- [[JARVIS/01-Identity/Will/Engineering-Principles|Engineering Principles]]

---

*Good tests are your safety net for refactoring and scaling.*
