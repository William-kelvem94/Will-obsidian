---
title: "Prisma Cheat Sheet"
description: "Quick reference for Prisma ORM"
tags: [cheatsheet, prisma, orm, database, typescript, jarvis-engenharia]
updated: 2026-06-10
date: 2026-04-27
---

# Prisma Cheat Sheet

Quick reference for Prisma ORM (PostgreSQL, MySQL, SQLite).

---

## 🚀 Setup

```bash
# Install
npm install prisma @prisma/client

# Initialize
npx prisma init

# Creates:
# - prisma/schema.prisma
# - .env
```

---

## 📄 Schema Definition

```prisma
// prisma/schema.prisma

generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql" // or "mysql", "sqlite"
  url      = env("DATABASE_URL")
}

model User {
  id        Int      @id @default(autoincrement())
  email     String   @unique
  name      String?
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  posts     Post[]
  profile   Profile?
}

model Profile {
  id     Int     @id @default(autoincrement())
  bio    String?
  userId Int     @unique
  user   User    @relation(fields: [userId], references: [id])
}

model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String?
  published Boolean  @default(false)
  authorId  Int
  author    User     @relation(fields: [authorId], references: [id])
  tags      Tag[]
  
  @@index([authorId])
}

model Tag {
  id    Int    @id @default(autoincrement())
  name  String @unique
  posts Post[]
}
```

---

## 🔗 Relationships

### One-to-One

```prisma
model User {
  id      Int      @id @default(autoincrement())
  profile Profile?
}

model Profile {
  id     Int  @id @default(autoincrement())
  userId Int  @unique
  user   User @relation(fields: [userId], references: [id])
}
```

### One-to-Many

```prisma
model User {
  id    Int    @id @default(autoincrement())
  posts Post[]
}

model Post {
  id       Int  @id @default(autoincrement())
  authorId Int
  author   User @relation(fields: [authorId], references: [id])
}
```

### Many-to-Many

```prisma
model Post {
  id   Int   @id @default(autoincrement())
  tags Tag[]
}

model Tag {
  id    Int    @id @default(autoincrement())
  posts Post[]
}

// Prisma auto-creates join table
```

### Explicit Many-to-Many

```prisma
model Post {
  id             Int              @id @default(autoincrement())
  categoriesOnPosts CategoriesOnPosts[]
}

model Category {
  id             Int              @id @default(autoincrement())
  categoriesOnPosts CategoriesOnPosts[]
}

model CategoriesOnPosts {
  postId     Int
  categoryId Int
  assignedAt DateTime @default(now())
  
  post     Post     @relation(fields: [postId], references: [id])
  category Category @relation(fields: [categoryId], references: [id])
  
  @@id([postId, categoryId])
}
```

---

## 🛠️ CLI Commands

```bash
# Generate Prisma Client
npx prisma generate

# Create migration
npx prisma migrate dev --name init

# Apply migrations (production)
npx prisma migrate deploy

# Reset database (dev only!)
npx prisma migrate reset

# Open Prisma Studio (GUI)
npx prisma studio

# Format schema
npx prisma format

# Validate schema
npx prisma validate

# Pull schema from existing DB
npx prisma db pull

# Push schema to DB (prototype, no migrations)
npx prisma db push
```

---

## 📦 Client Usage

### Initialize Client

```typescript
// lib/prisma.ts
import { PrismaClient } from '@prisma/client'

const globalForPrisma = global as unknown as { prisma: PrismaClient }

export const prisma =
  globalForPrisma.prisma ||
  new PrismaClient({
    log: ['query', 'error', 'warn'],
  })

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma
```

### Create

```typescript
import { prisma } from './lib/prisma'

// Create one
const user = await prisma.user.create({
  data: {
    email: 'alice@example.com',
    name: 'Alice',
  },
})

// Create with relation
const user = await prisma.user.create({
  data: {
    email: 'bob@example.com',
    name: 'Bob',
    posts: {
      create: {
        title: 'My first post',
        content: 'Content here',
      },
    },
  },
})

// Create many
const users = await prisma.user.createMany({
  data: [
    { email: 'user1@example.com' },
    { email: 'user2@example.com' },
  ],
})
```

### Read

```typescript
// Find all
const users = await prisma.user.findMany()

// Find with filter
const users = await prisma.user.findMany({
  where: {
    email: {
      contains: '@example.com',
    },
  },
})

// Find one
const user = await prisma.user.findUnique({
  where: { id: 1 },
})

// Find or throw
const user = await prisma.user.findUniqueOrThrow({
  where: { id: 1 },
})

// Find first
const user = await prisma.user.findFirst({
  where: {
    email: {
      contains: '@example.com',
    },
  },
})
```

### Update

```typescript
// Update one
const user = await prisma.user.update({
  where: { id: 1 },
  data: { name: 'Alice Updated' },
})

// Update many
const updateCount = await prisma.user.updateMany({
  where: {
    email: {
      contains: '@example.com',
    },
  },
  data: {
    name: 'Updated Name',
  },
})

// Upsert (update or create)
const user = await prisma.user.upsert({
  where: { email: 'alice@example.com' },
  update: { name: 'Alice Updated' },
  create: {
    email: 'alice@example.com',
    name: 'Alice',
  },
})
```

### Delete

```typescript
// Delete one
const user = await prisma.user.delete({
  where: { id: 1 },
})

// Delete many
const deleteCount = await prisma.user.deleteMany({
  where: {
    email: {
      contains: '@example.com',
    },
  },
})

// Delete all
const deleteCount = await prisma.user.deleteMany()
```

---

## 🔍 Querying

### Select Fields

```typescript
const users = await prisma.user.findMany({
  select: {
    id: true,
    email: true,
    posts: {
      select: {
        title: true,
      },
    },
  },
})
```

### Include Relations

```typescript
const users = await prisma.user.findMany({
  include: {
    posts: true,
    profile: true,
  },
})

// Nested include
const users = await prisma.user.findMany({
  include: {
    posts: {
      include: {
        tags: true,
      },
    },
  },
})
```

### Filtering

```typescript
// Basic
const users = await prisma.user.findMany({
  where: {
    email: 'alice@example.com',
  },
})

// Operators
const users = await prisma.user.findMany({
  where: {
    age: { gte: 18 }, // >=
    email: { contains: '@example.com' },
    name: { startsWith: 'A' },
  },
})

// AND, OR, NOT
const users = await prisma.user.findMany({
  where: {
    AND: [
      { age: { gte: 18 } },
      { email: { contains: '@example.com' } },
    ],
  },
})

const users = await prisma.user.findMany({
  where: {
    OR: [
      { email: { contains: '@example.com' } },
      { email: { contains: '@test.com' } },
    ],
  },
})

// Relation filter
const users = await prisma.user.findMany({
  where: {
    posts: {
      some: {
        published: true,
      },
    },
  },
})
```

### Sorting

```typescript
const users = await prisma.user.findMany({
  orderBy: {
    createdAt: 'desc',
  },
})

// Multiple fields
const users = await prisma.user.findMany({
  orderBy: [
    { name: 'asc' },
    { email: 'asc' },
  ],
})

// Relation count
const users = await prisma.user.findMany({
  orderBy: {
    posts: {
      _count: 'desc',
    },
  },
})
```

### Pagination

```typescript
// Skip & Take
const users = await prisma.user.findMany({
  skip: 10,
  take: 20,
})

// Cursor-based
const users = await prisma.user.findMany({
  take: 10,
  cursor: {
    id: lastSeenId,
  },
})
```

### Aggregation

```typescript
// Count
const count = await prisma.user.count()

const count = await prisma.user.count({
  where: { email: { contains: '@example.com' } },
})

// Aggregate
const result = await prisma.post.aggregate({
  _avg: { views: true },
  _max: { views: true },
  _min: { views: true },
  _sum: { views: true },
  _count: true,
})

// Group by
const result = await prisma.post.groupBy({
  by: ['authorId'],
  _count: {
    id: true,
  },
})
```

---

## 🔄 Transactions

```typescript
// Sequential
const result = await prisma.$transaction([
  prisma.user.create({ data: { email: 'user1@example.com' } }),
  prisma.user.create({ data: { email: 'user2@example.com' } }),
])

// Interactive
const result = await prisma.$transaction(async (tx) => {
  const user = await tx.user.create({
    data: { email: 'alice@example.com' },
  })
  
  const post = await tx.post.create({
    data: {
      title: 'My post',
      authorId: user.id,
    },
  })
  
  return { user, post }
})
```

---

## 🔐 Middleware

```typescript
prisma.$use(async (params, next) => {
  // Before query
  console.log('Query:', params.model, params.action)
  
  const result = await next(params)
  
  // After query
  console.log('Result:', result)
  
  return result
})

// Soft delete middleware
prisma.$use(async (params, next) => {
  if (params.action === 'delete') {
    params.action = 'update'
    params.args.data = { deletedAt: new Date() }
  }
  
  if (params.action === 'findMany' || params.action === 'findUnique') {
    params.args.where = { ...params.args.where, deletedAt: null }
  }
  
  return next(params)
})
```

---

## 🧪 Testing

```typescript
import { PrismaClient } from '@prisma/client'
import { mockDeep, mockReset, DeepMockProxy } from 'jest-mock-extended'

export const prisma = mockDeep<PrismaClient>()

beforeEach(() => {
  mockReset(prisma)
})

// Test
test('create user', async () => {
  prisma.user.create.mockResolvedValue({
    id: 1,
    email: 'test@example.com',
    name: 'Test',
  })
  
  const user = await prisma.user.create({
    data: { email: 'test@example.com' },
  })
  
  expect(user.email).toBe('test@example.com')
})
```

---

## 🐳 Docker Setup

```yaml
# docker-compose.yml
version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

```bash
# .env
DATABASE_URL="postgresql://user:password@localhost:5432/mydb"
```

---

## 📊 Prisma Studio

```bash
# Open GUI
npx prisma studio

# Access at http://localhost:5555
```

---

## 🚀 Production Best Practices

```typescript
// 1. Connection pooling
const prisma = new PrismaClient({
  datasources: {
    db: {
      url: process.env.DATABASE_URL + '?connection_limit=10',
    },
  },
})

// 2. Logging in production
const prisma = new PrismaClient({
  log: process.env.NODE_ENV === 'production'
    ? ['error']
    : ['query', 'error', 'warn'],
})

// 3. Graceful shutdown
process.on('beforeExit', async () => {
  await prisma.$disconnect()
})
```

---

## 🔗 Related

- [Prisma Docs](https://www.prisma.io/docs)
- [[02-JARVIS/04-Engineering/Playbooks/Docker-Not-Starting|Docker Troubleshooting]]
- [[05-Skills/02-software-engineering|Software Engineering Skills]]

[[02-JARVIS/README|← Voltar ao Command Center]]
