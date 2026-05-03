---
title: "Prompt Engineering"
description: "Techniques for crafting effective LLM prompts"
tags: [llm, prompt-engineering, ai, copilot, chatgpt, best-practices, skills-ai]
updated: 2026-05-03
date: 2026-04-27
---

# Prompt Engineering Skill

Master the art of communicating with AI models for optimal results.

---

## 🎯 Core Principles

### 1. Be Specific and Clear

**❌ Vague:**
```
Write code for a website
```

**✅ Specific:**
```
Create a React component for a responsive navigation bar with:
- Logo on the left
- Menu items in the center (Home, About, Contact)
- Dark mode toggle on the right
- Mobile hamburger menu for screens < 768px
- Use Tailwind CSS for styling
```

### 2. Provide Context

**❌ No context:**
```
Fix this bug
```

**✅ With context:**
```
I have a FastAPI endpoint that returns 500 when the database is empty.
Expected: Return empty array with 200 status
Current behavior: Throws DatabaseError

Code:
@app.get("/users")
def list_users():
    return db.query(User).all()

Error message: "NoneType object is not iterable"

How can I handle the case where no users exist?
```

### 3. Use Examples

**❌ Abstract:**
```
Format the data nicely
```

**✅ With examples:**
```
Transform this user data into a formatted string:

Input:
{
  "name": "Alice",
  "age": 30,
  "email": "alice@example.com"
}

Expected output:
"Alice (30) - alice@example.com"

Please apply the same format to a list of users.
```

---

## 📐 Prompt Templates

### Template 1: Code Generation

```
Task: [What you want to build]
Language/Framework: [Tech stack]
Requirements:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]
Constraints:
- [Any limitations]
Context:
- [Relevant background]

Example input/output: [If applicable]
```

**Example:**
```
Task: Create a function to validate email addresses
Language/Framework: Python
Requirements:
- Check if email format is valid
- Return boolean (True/False)
- Handle edge cases (empty string, no @, multiple @)
Constraints:
- No external libraries (use regex)
Context:
- Part of user registration system
- Will be used in FastAPI endpoint

Example:
validate_email("user@example.com") → True
validate_email("invalid.email") → False
```

### Template 2: Debugging

```
Problem: [Describe the issue]
Expected behavior: [What should happen]
Actual behavior: [What actually happens]
Error message: [Full error with stack trace]

Code:
[Paste relevant code]

What I've tried:
- [Attempt 1]
- [Attempt 2]

Environment:
- [Python 3.11, FastAPI 0.100, etc.]
```

### Template 3: Refactoring

```
I have this code:
[Paste code]

Current issues:
- [Issue 1: e.g., hard to test]
- [Issue 2: e.g., repetitive]

Please refactor to:
- [Goal 1: e.g., more modular]
- [Goal 2: e.g., follow SOLID principles]
- [Goal 3: e.g., add type hints]

Preserve:
- [What must stay the same, e.g., API interface]
```

### Template 4: Explanation

```
Explain [concept/code] as if I'm:
- [Your experience level: beginner/intermediate/expert]
- Coming from [background: e.g., frontend → backend]

Focus on:
- [What you want to understand]

Use:
- [Preferred format: analogies, diagrams, examples]
```

---

## 🧩 Advanced Techniques

### Chain of Thought

Break complex problems into steps:

```
Let's solve this step by step:

1. First, identify the inputs and outputs
2. Then, determine the data structure
3. Next, outline the algorithm
4. Finally, implement in [language]

Problem: Sort array of objects by nested property

Step 1 - Inputs/Outputs:
Input: [{ user: { age: 30 } }, { user: { age: 25 } }]
Output: Sorted by user.age ascending

Step 2 - Data structure:
...
```

### Role Playing

Assign the AI a specific role:

```
You are a senior DevOps engineer reviewing a Dockerfile.
Analyze this Dockerfile and suggest improvements for:
- Build time
- Image size
- Security
- Best practices

[Paste Dockerfile]

Provide:
1. Issues found (with severity: low/medium/high)
2. Specific fixes with code examples
3. Explanation of why each change matters
```

### Constraint-Based

Set explicit boundaries:

```
Create a function to paginate results.

Constraints:
- Must work with both lists and database queries
- Support both offset and cursor-based pagination
- Type-safe (use TypeScript)
- Maximum 3 function parameters
- Include comprehensive docstring
- No external dependencies
```

### Iterative Refinement

Build on previous responses:

```
[After getting initial code]

Good start! Now let's improve:
1. Add error handling for edge cases
2. Make it work with async/await
3. Add unit tests
4. Optimize for large datasets

Keep the same interface but enhance the implementation.
```

---

## 🎭 Prompt Patterns

### Pattern 1: Persona Pattern

```
Act as a [role] with [experience level].
You specialize in [domain].
Your communication style is [style].

Now, [task].
```

**Example:**
```
Act as a frontend architect with 10+ years of React experience.
You specialize in performance optimization and accessibility.
Your communication style is direct and example-driven.

Now, review this React component and suggest performance improvements.
```

### Pattern 2: Format Pattern

```
Respond in the following format:

# [Section 1 Title]
[Content]

# [Section 2 Title]
[Content]

Example:
# Problem
[Describe issue]

# Solution
[Provide fix]

# Why it works
[Explain reasoning]
```

### Pattern 3: Few-Shot Learning

Provide examples before the actual task:

```
Convert function names from camelCase to snake_case.

Examples:
getUserData → get_user_data
fetchAllPosts → fetch_all_posts
updateProfileImage → update_profile_image

Now convert:
calculateTotalPrice → ?
validateEmailAddress → ?
```

### Pattern 4: Constraint Addition

Add constraints progressively:

```
1. Create a function that adds two numbers
[Get response]

2. Now add type hints
[Get response]

3. Now add input validation
[Get response]

4. Now add comprehensive docstring and examples
```

---

## 🚫 Common Mistakes

### Mistake 1: Too Vague

**❌ Bad:**
```
Make it better
```

**✅ Good:**
```
Improve this function by:
1. Adding error handling
2. Making it async-compatible
3. Adding type hints
4. Optimizing the database query
```

### Mistake 2: No Context

**❌ Bad:**
```
Why doesn't this work?
[Code only]
```

**✅ Good:**
```
This pagination function should return 10 items per page,
but it's returning all items. The database has 100 records.

Expected: 10 items
Actual: 100 items

[Code]
```

### Mistake 3: Assuming Knowledge

**❌ Bad:**
```
Use the thing to fix the other thing
```

**✅ Good:**
```
Use Prisma's `findMany` with `skip` and `take` parameters
to implement pagination in this Next.js API route.
```

### Mistake 4: Single Massive Request

**❌ Bad:**
```
Build a complete e-commerce site with auth, payment, admin panel,
product catalog, reviews, cart, wishlist, and recommendations
```

**✅ Good:**
```
Let's build an e-commerce site step by step.

Step 1: Create the product model and basic CRUD endpoints
[Work on this first]

[Then iterate: Step 2 - Auth, Step 3 - Cart, etc.]
```

---

## 🎯 Use Case Examples

### Use Case 1: Code Review

```
Review this TypeScript function for:
1. Type safety issues
2. Potential runtime errors
3. Performance bottlenecks
4. Code style violations (ESLint, Prettier)
5. Missing error handling

[Code]

For each issue:
- Severity (high/medium/low)
- Line number
- Explanation
- Suggested fix with code example
```

### Use Case 2: Learning New Tech

```
I'm learning FastAPI and want to understand dependency injection.

My background: 5 years of Express.js experience

Explain:
1. What is dependency injection in FastAPI?
2. How is it different from Express middleware?
3. Common use cases (DB connections, auth, etc.)
4. Show a practical example: API endpoint that uses:
   - Database session dependency
   - Current user dependency
   - Pagination parameters dependency

Use code examples and compare to Express where helpful.
```

### Use Case 3: Architecture Decision

```
I need to choose between:
- Option A: Server-side rendering (SSR) with Next.js
- Option B: Static site generation (SSG) with Next.js
- Option C: Client-side rendering (CSR) with React

Project context:
- Blog with 100+ posts
- Posts updated weekly
- High SEO importance
- Low budget (serverless preferred)
- International audience

Analyze each option:
1. Pros/cons for this specific use case
2. Performance implications
3. Cost estimates
4. SEO impact
5. Development complexity

Recommend the best option with reasoning.
```

### Use Case 4: Test Generation

```
Generate pytest tests for this Python function:

[Code]

Requirements:
- Test happy path (valid inputs)
- Test edge cases (empty, null, max values)
- Test error cases (invalid types, out of range)
- Use pytest fixtures for setup
- Use parametrize for multiple test cases
- Each test should be independent
- Follow AAA pattern (Arrange-Act-Assert)
```

---

## 🔗 Related Resources

- [[skills/01-agentic-intelligence/|Agentic Intelligence Skills]]
- [[skills/04-knowledge-systems/rag-implementation/SKILL.md|RAG Implementation]]
- [[JARVIS/KnowledgeBase/Personalidade|JARVIS Personality]] - Prompt patterns

---

*Effective prompts are conversations, not commands. Iterate and refine.*
