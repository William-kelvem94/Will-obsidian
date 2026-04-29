---
title: "Code Snippets Library"
date: 2026-04-27
tags: [jarvis-engenharia]
updated: 2026-04-29
---

# Code Snippets Library

Reusable code snippets for common patterns and tasks.

---

## 📁 Structure

```
Snippets/
├── README.md (this file)
├── API/
│   ├── fastapi-crud.py
│   ├── express-auth.js
│   └── nextjs-api-handler.ts
├── Database/
│   ├── prisma-setup.ts
│   ├── sqlalchemy-models.py
│   └── mongo-connection.js
├── Frontend/
│   ├── react-custom-hooks.tsx
│   ├── nextjs-layouts.tsx
│   └── tailwind-components.tsx
├── Utilities/
│   ├── logger.py
│   ├── file-helpers.ts
│   └── date-formatters.js
└── DevOps/
    ├── dockerfile-templates/
    ├── github-actions/
    └── docker-compose-examples/
```

---

## 🚀 Quick Access

### API Patterns

- **[[Snippets/API/fastapi-crud.py|FastAPI CRUD]]** - Complete CRUD with Pydantic
- **[[Snippets/API/express-auth.js|Express Auth]]** - JWT authentication
- **[[Snippets/API/nextjs-api-handler.ts|Next.js API Handler]]** - Typed API routes

### Database

- **[[Snippets/Database/prisma-setup.ts|Prisma Setup]]** - Client initialization & connection
- **[[Snippets/Database/sqlalchemy-models.py|SQLAlchemy Models]]** - Base models with mixins
- **[[Snippets/Database/mongo-connection.js|MongoDB Connection]]** - Connection pooling

### Frontend

- **[[Snippets/Frontend/react-custom-hooks.tsx|React Hooks]]** - useFetch, useLocalStorage, useDebounce
- **[[Snippets/Frontend/nextjs-layouts.tsx|Next.js Layouts]]** - Nested layouts with TypeScript
- **[[Snippets/Frontend/tailwind-components.tsx|Tailwind Components]]** - Buttons, cards, forms

### Utilities

- **[[Snippets/Utilities/logger.py|Python Logger]]** - Structured logging
- **[[Snippets/Utilities/file-helpers.ts|File Helpers]]** - Read, write, path utilities
- **[[Snippets/Utilities/date-formatters.js|Date Formatters]]** - Timezone-aware formatting

### DevOps

- **[[Snippets/DevOps/dockerfile-templates/|Dockerfile Templates]]** - Node, Python, Go
- **[[Snippets/DevOps/github-actions/|GitHub Actions]]** - CI/CD workflows
- **[[Snippets/DevOps/docker-compose-examples/|Docker Compose]]** - Multi-service stacks

---

## 📋 Usage Patterns

### Pattern 1: Copy-Paste Snippets

For one-off usage:
1. Find snippet in category
2. Copy code
3. Adapt to your project

### Pattern 2: Template Generation

For project scaffolding:
```bash
# Example: Generate FastAPI CRUD from template
python .scripts/generate_from_snippet.py \
  --template Snippets/API/fastapi-crud.py \
  --model User \
  --output api/users.py
```

### Pattern 3: IDE Integration

VSCode snippets (`.vscode/snippets.code-snippets`):
```json
{
  "FastAPI CRUD": {
    "prefix": "fastapi-crud",
    "body": [
      "# ... snippet content ..."
    ]
  }
}
```

---

## 🎯 Snippet Guidelines

When adding new snippets:

### 1. File Naming
- Lowercase with hyphens: `file-name.ext`
- Extension matches language: `.py`, `.ts`, `.js`

### 2. Documentation
Each snippet should have:
```python
"""
Brief description of what this does

Usage:
    from snippets import function_name
    result = function_name(arg1, arg2)

Dependencies:
    - package1>=1.0.0
    - package2>=2.0.0

Example:
    >>> function_name("test")
    "expected result"
"""
```

### 3. Parameterization
Use placeholders for customization:
```python
# ❌ Bad (hardcoded)
DB_HOST = "localhost"

# ✅ Good (parameterized)
DB_HOST = os.getenv("DB_HOST", "localhost")
```

### 4. Error Handling
Include proper error handling:
```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    raise
```

### 5. Testing
Include basic test example:
```python
def test_function_name():
    result = function_name("input")
    assert result == "expected"
```

---

## 🔍 Finding Snippets

### By Category
Browse folders: `API/`, `Database/`, `Frontend/`, `Utilities/`, `DevOps/`

### By Technology
- **Python**: `.py` files
- **TypeScript**: `.ts`, `.tsx` files
- **JavaScript**: `.js`, `.jsx` files
- **YAML**: `.yml`, `.yaml` files
- **Dockerfile**: `.dockerfile`, `Dockerfile.*`

### By Use Case
- Authentication → `API/express-auth.js`, `API/fastapi-auth.py`
- CRUD operations → `API/fastapi-crud.py`, `API/express-crud.js`
- Database setup → `Database/prisma-setup.ts`, `Database/sqlalchemy-models.py`
- React hooks → `Frontend/react-custom-hooks.tsx`

---

## 📊 Most Used Snippets

Based on frequency of access:

1. **FastAPI CRUD** - Complete REST API pattern
2. **Prisma Setup** - Database connection singleton
3. **React Custom Hooks** - useFetch, useDebounce
4. **Docker Templates** - Multi-stage builds
5. **Next.js API Handler** - Type-safe API routes

---

## 🔗 Related Resources

- [[JARVIS/04-Engineering/Wiki/CheatSheets/|Cheat Sheets]] - Quick references
- [[skills/02-software-engineering/|Software Engineering Skills]]
- [[JARVIS/KnowledgeBase/Ferramentas|Ferramentas]] - Tool documentation

---

## 📝 Contributing

To add a snippet:

1. **Choose category** (or create new if needed)
2. **Follow naming convention** (`feature-name.ext`)
3. **Add documentation header**
4. **Include usage example**
5. **Test the code**
6. **Update this README** with link

Example structure:
```python
"""
Feature Name - Brief Description

Description:
    Longer explanation of what this does and when to use it.

Usage:
    # Basic usage
    result = my_function(param1)
    
    # Advanced usage
    result = my_function(param1, param2, option=True)

Dependencies:
    pip install package1 package2

Example:
    >>> my_function("test")
    "result"

See also:
    - [[Related snippet]]
    - [[Related documentation]]
"""

def my_function(param1: str, param2: Optional[str] = None) -> str:
    """
    Brief description.
    
    Args:
        param1: Description of param1
        param2: Description of param2 (optional)
    
    Returns:
        Description of return value
    """
    # Implementation
    pass


if __name__ == "__main__":
    # Test/demo
    print(my_function("test"))
```

---

*Keep snippets DRY (Don't Repeat Yourself) and well-documented for maximum reusability.*
