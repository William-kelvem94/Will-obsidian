---
tags: [skills, skills-eng, database, sql, nosql]
updated: 2026-06-07
title: "Database Skills - SQL, NoSQL, Otimizacao"
date: 2026-04-27
---

# Database Skills — SQL, NoSQL e Otimizacao

Referencia pratica para modelagem de dados, migracoes, otimizacao de consultas e estrategias de indexacao em bancos relacionais e NoSQL.

## Padroes de Migracao

### Alembic (FastAPI + SQLAlchemy)

```python
"""migration: adiciona tabela de memorias"""
from alembic import op
import sqlalchemy as sa

revision = "20260516_add_memories"
down_revision = "20260501_init"

def upgrade():
    op.create_table(
        "memories",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id")),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("embedding", sa.ARRAY(sa.Float()), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now()),
        sa.Column("importance", sa.Float(), default=0.5),
    )
    op.create_index("idx_memories_user", "memories", ["user_id"])
    op.create_index("idx_memories_embedding", "memories", ["embedding"], postgresql_using="hnsw")

def downgrade():
    op.drop_table("memories")
```

### Prisma (Node.js)

```prisma
model Memory {
  id        Int      @id @default(autoincrement())
  userId    Int
  content   String   @db.Text
  embedding Unsupported("vector(1536)")?
  createdAt DateTime @default(now())
  importance Float   @default(0.5)
  user      User     @relation(fields: [userId], references: [id])

  @@index([userId])
  @@index([embedding], type: BTree)
}
```

## Otimizacao de Consultas

### Usando EXPLAIN ANALYZE

```sql
EXPLAIN ANALYZE
SELECT m.content, m.importance
FROM memories m
WHERE m.user_id = 42
  AND m.importance > 0.7
ORDER BY m.created_at DESC
LIMIT 10;
```

### Padroes de Query Otimizada

```python
# Ruim: N+1 queries
users = session.query(User).all()
for user in users:
    print(user.memories)  # query por usuario

# Bom: eager loading
users = session.query(User).options(
    joinedload(User.memories)
).all()

# Otimo: join explcito com filtro
results = session.query(User, Memory).join(
    Memory, User.id == Memory.user_id
).filter(
    Memory.importance > 0.7,
    User.id == 42
).limit(10).all()
```

## Estrategias de Indexacao

| Tipo de Indice | Uso Ideal | Exemplo |
|----------------|-----------|---------|
| B-tree | Colunas ordenaveis, buscas por intervalo | `created_at`, `id` |
| Hash | Buscas por igualdade exata | `user_id = 42` |
| GIN | Arrays, JSONB, full-text search | `tags @> ['urgente']` |
| HNSW (pgvector) | Similaridade vetorial | `embedding <=> query_vec` |
| GiST | Busca geometrica ou de intervalo | `daterange`, `tsvector` |

### Criando Indices Eficientes

```sql
-- Indice composto para query frequente
CREATE INDEX idx_user_importance
ON memories (user_id, importance DESC);

-- Indice parcial para dados filtrados
CREATE INDEX idx_active_users
ON users (email)
WHERE active = true;

-- Indice para busca full-text
CREATE INDEX idx_content_search
ON memories USING GIN (to_tsvector('portuguese', content));
```

## Pool de Conexoes

### SQLAlchemy Async

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://user:pass@localhost:5432/jarvis"

engine = create_async_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    pool_recycle=3600,
)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_session():
    async with async_session() as session:
        yield session
```

### Psycopg2 Pool

```python
from psycopg2.pool import ThreadedConnectionPool

pool = ThreadedConnectionPool(
    minconn=2,
    maxconn=10,
    dsn="dbname=jarvis user=postgres password=secret"
)

def query(sql: str, params: tuple = ()):
    conn = pool.getconn()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()
    finally:
        pool.putconn(conn)
```

## MongoDB — Padroes de Agregacao

```javascript
db.memories.aggregate([
  { $match: { user_id: ObjectId("...") } },
  { $sort: { importance: -1, created_at: -1 } },
  { $limit: 20 },
  { $group: {
      _id: "$category",
      total: { $sum: 1 },
      avg_importance: { $avg: "$importance" }
  }},
  { $out: "memory_summary" }
]);
```

## Referencias

- [[backend|Backend]] — Integracao com APIs e servicos
- [[05-Skills/skills/04-knowledge-systems/advanced-rag-strategies|RAG Avancado]] — Busca hibrida e indexacao vetorial
- [[05-Skills/skills/04-knowledge-systems/memory-management|Gestao de Memoria]] — Estrategias de banco vetorial
- [[04-Conhecimentos/07-Humanidades/Matematica/Algebra-Linear-Essencial|Algebra Linear]] — Fundamentos de similaridade vetorial
