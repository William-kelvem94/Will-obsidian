---
title: "Banco de Dados"
date: 2026-05-16
area: "Programação e Engenharia de Software"
tags: [conhecimento, banco-de-dados, sql, nosql, postgresql, mongodb, redis]
related: ["Conhecimento-Geral/Programacao/Performance-e-Otimizacao"]
aliases: ["Database", "SQL", "NoSQL", "PostgreSQL"]
---

## Visão Geral

Banco de dados é o componente responsável por persistir, recuperar e gerenciar dados de forma estruturada. A escolha do banco impacta diretamente a arquitetura, desempenho e escalabilidade do sistema.

## Modelo Relacional

O modelo relacional organiza dados em tabelas com linhas e colunas, usando **SQL** como linguagem de consulta.

### Normalização

Processo de organizar dados para reduzir redundância e dependência:

| Forma | Regra |
|-------|-------|
| 1FN | Atributos atômicos, sem grupos repetitivos |
| 2FN | 1FN + toda coluna não-chave depende da chave completa |
| 3FN | 2FN + nenhuma dependência transitiva |
| BC | 3FN + toda dependência é de uma superchave |

```sql
-- Tabela não normalizada (viola 1FN)
CREATE TABLE pedidos (
    id INT PRIMARY KEY,
    cliente VARCHAR(100),
    itens VARCHAR(500) -- "produto1:2,produto3:5"
);

-- Forma normalizada
CREATE TABLE clientes (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE pedidos (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    cliente_id INT NOT NULL REFERENCES clientes(id),
    criado_em TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE itens_pedido (
    pedido_id INT NOT NULL REFERENCES pedidos(id),
    produto_id INT NOT NULL REFERENCES produtos(id),
    quantidade INT NOT NULL CHECK (quantidade > 0),
    PRIMARY KEY (pedido_id, produto_id)
);
```

### ACID

Propriedades que garantem transações confiáveis:

| Propriedade | Significado |
|-------------|-------------|
| **A**tomicity | Tudo ou nada — a transação completa ou não acontece |
| **C**onsistency | Dados permanecem em estado válido |
| **I**solation | Transações concorrentes não interferem entre si |
| **D**urability | Dados persistem mesmo após falha |

```python
# Exemplo de transação com SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("postgresql://user:pass@localhost/db")

with Session(engine) as session:
    try:
        session.add(Conta(id=1, saldo=100))
        session.add(Conta(id=2, saldo=0))
        session.flush()

        conta1 = session.get(Conta, 1)
        conta2 = session.get(Conta, 2)
        conta1.saldo -= 50
        conta2.saldo += 50

        session.commit()  -- tudo ou nada
    except Exception:
        session.rollback()
```

### Isolation Levels

O padrão SQL define quatro níveis que equilibram consistência e desempenho:

```sql
-- Níveis de isolamento no PostgreSQL
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;  -- = READ COMMITTED no PG
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;    -- default no PG
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

| Nível | Dirty Read | Non-repeatable Read | Phantom Read |
|-------|-----------|-------------------|-------------|
| READ UNCOMMITTED | Possível | Possível | Possível |
| READ COMMITTED | Evitado | Possível | Possível |
| REPEATABLE READ | Evitado | Evitado | Possível |
| SERIALIZABLE | Evitado | Evitado | Evitado |

### Índices

Estruturas que aceleram a busca de dados. PostgreSQL é referência pela variedade:

```sql
-- B-tree (default) — ideal para comparações: =, <, >, BETWEEN, LIKE (prefixo)
CREATE INDEX idx_usuarios_email ON usuarios (email);

-- Hash — apenas igualdade (=)
CREATE INDEX idx_hash_email ON usuarios USING hash (email);

-- GiST — dados geoespaciais, full-text search
CREATE INDEX idx_localizacao ON locais USING gist (coordenadas);

-- GIN — arrays, JSONB, full-text
CREATE INDEX idx_tags ON posts USING gin (tags);

-- Índice composto — ordem das colunas importa
CREATE INDEX idx_uf_cidade ON enderecos (uf, cidade);

-- Índice parcial — apenas registros que satisfazem condição
CREATE INDEX idx_pedidos_ativos ON pedidos (status)
    WHERE status = 'ativo';

-- Index-only scan — quando índice cobre toda a consulta
CREATE INDEX idx_cobrindo ON pedidos (cliente_id, status, total);
```

```python
# Análise de índice com EXPLAIN
import psycopg2

conn = psycopg2.connect("dbname=teste")
cur = conn.cursor()

cur.execute("EXPLAIN ANALYZE SELECT * FROM usuarios WHERE email = 'joao@email.com'")
for row in cur.fetchall():
    print(row)
```

### Joins

Combinam registros de múltiplas tabelas:

```sql
-- INNER JOIN — apenas correspondências
SELECT u.nome, p.titulo
FROM usuarios u
INNER JOIN posts p ON p.autor_id = u.id;

-- LEFT JOIN — todos da esquerda + correspondências da direita
SELECT u.nome, COALESCE(p.titulo, 'sem post') AS post
FROM usuarios u
LEFT JOIN posts p ON p.autor_id = u.id;

-- CROSS JOIN — produto cartesiano
SELECT a.nome, b.nome
FROM cores a CROSS JOIN tamanhos b;

-- LATERAL JOIN — subquery que referencia colunas anteriores
SELECT u.nome, ultimos.titulo
FROM usuarios u
LEFT JOIN LATERAL (
    SELECT titulo FROM posts
    WHERE autor_id = u.id
    ORDER BY criado_em DESC
    LIMIT 1
) ultimos ON TRUE;
```

### Transações

```sql
BEGIN;

UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100 WHERE id = 2;

SAVEPOINT antes_do_log;
INSERT INTO log_transacoes VALUES (...);
ROLLBACK TO SAVEPOINT antes_do_log;  -- desfaz só o log

COMMIT;  -- ou ROLLBACK
```

## NoSQL

Bancos não-relacionais surgem para cenários onde SQL não é ideal: alta escalabilidade horizontal, esquemas flexíveis, dados não estruturados.

### Document (MongoDB)

Armazena documentos JSON/BSON. Ideal para dados semi-estruturados.

```javascript
// MongoDB — agregação
db.pedidos.aggregate([
    { $match: { status: "entregue" } },
    { $group: { _id: "$cliente_id", total: { $sum: "$valor" } } },
    { $sort: { total: -1 } },
    { $limit: 10 },
    { $lookup: {
        from: "clientes",
        localField: "_id",
        foreignField: "_id",
        as: "cliente"
    }}
]);

// Índices no MongoDB
db.usuarios.createIndex({ email: 1 }, { unique: true });
db.pedidos.createIndex({ cliente_id: 1, criado_em: -1 });
db.colecao.createIndex({ geometria: "2dsphere" });  // geoespacial
```

### Key-Value (Redis)

Estrutura simples de chave-valor em memória. Latência de microssegundos.

```python
import redis.asyncio as redis

async def exemplo_redis():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    # String
    await r.set("user:1:nome", "João")
    nome = await r.get("user:1:nome")

    # List (fila)
    await r.lpush("fila:email", "email1", "email2")
    await r.brpop("fila:email", timeout=5)

    # Hash
    await r.hset("user:1", mapping={"nome": "João", "email": "joao@email.com"})

    # Set
    await r.sadd("tags:python", "async", "redis", "tutorial")

    # Sorted Set (leaderboard)
    await r.zadd("leaderboard", {"joao": 100, "maria": 200})
    ranking = await r.zrevrange("leaderboard", 0, 2, withscores=True)

    # Expiração
    await r.expire("cache:consulta", 300)

    # Pub/Sub
    pub = r.pubsub()
    await pub.subscribe("canal:notificacoes")
```

### Column (Cassandra)

Modelo baseado em famílias de colunas. Ideal para escrita intensa e séries temporais.

```sql
-- Cassandra Query Language (CQL)
CREATE KEYSPACE analytics
    WITH replication = {
        'class': 'NetworkTopologyStrategy',
        'datacenter1': 3
    };

CREATE TABLE eventos (
    usuario_id UUID,
    timestamp TIMESTAMP,
    tipo TEXT,
    payload TEXT,
    PRIMARY KEY ((usuario_id), timestamp, tipo)
) WITH CLUSTERING ORDER BY (timestamp DESC)
   AND default_time_to_live = 86400;
```

### Graph (Neo4j)

Modelo baseado em nós e arestas. Ideal para relações complexas.

```cypher
// Neo4j — Cypher
// Criar nós e relações
CREATE (joao:Usuario {nome: "João", idade: 30})
CREATE (maria:Usuario {nome: "Maria", idade: 28})
CREATE (joao)-[:AMIGO_DE {desde: 2020}]->(maria)
CREATE (joao)-[:SEGUE]->(post:Post {titulo: "Graph Databases"});

// Consultar recomendações
MATCH (u:Usuario {nome: "João"})-[:AMIGO_DE]->(amigo)-[:SEGUE]->(post)
WHERE NOT (u)-[:SEGUE]->(post)
RETURN post.titulo, collect(amigo.nome) AS recomendado_por;

// Path finding
MATCH path = shortestPath(
    (joao:Usuario {nome: "João"})-[:AMIGO_DE*]-(alvo:Usuario {nome: "Pedro"})
)
RETURN length(path) AS grau_separacao;
```

## Vector Databases

Bancos otimizados para armazenar e buscar embeddings — vetores numéricos que representam significado semântico. Essenciais para RAG (Retrieval-Augmented Generation).

```python
import numpy as np
from sentence_transformers import SentenceTransformer

modelo = SentenceTransformer("all-MiniLM-L6-v2")

# Gerar embedding
texto = "Banco de dados vetoriais são usados em IA"
embedding = modelo.encode(texto)  # vetor 384-d
```

### FAISS (Meta)

Biblioteca para busca de similaridade em larga escala.

```python
import faiss
import numpy as np

# Criar índice
dimensao = 384
index = faiss.IndexFlatL2(dimensao)  # L2 = distância euclidiana
index = faiss.IndexIDMap(index)

# Adicionar vetores
embeddings = np.random.rand(10000, dimensao).astype('float32')
ids = np.arange(10000)
index.add_with_ids(embeddings, ids)

# Busca
consulta = np.random.rand(1, dimensao).astype('float32')
distancias, indices = index.search(consulta, k=5)

# Índice otimizado para memória (IVF)
nlist = 100
quantizer = faiss.IndexFlatL2(dimensao)
index_ivf = faiss.IndexIVFFlat(quantizer, dimensao, nlist, faiss.METRIC_L2)
index_ivf.train(embeddings)
index_ivf.add_with_ids(embeddings, ids)
index_ivf.nprobe = 10  -- número de clusters a explorar na busca
```

### Pinecone

Serviço gerenciado de vector database com busca híbrida (vetorial + metadados).

```python
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key="sk-...")

# Criar índice
index = pc.create_index(
    name="documentos",
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-east-1")
)

# Upsert
index.upsert([
    ("id1", [0.1, 0.2, ...], {"texto": "Documento 1", "fonte": "wiki"}),
    ("id2", [0.3, 0.4, ...], {"texto": "Documento 2", "fonte": "blog"}),
])

# Query
resultados = index.query(
    vector=[0.15, 0.25, ...],
    top_k=3,
    filter={"fonte": {"$eq": "wiki"}},
    include_metadata=True
)
```

### Chroma

Banco vetorial open-source e leve, muito usado em projetos RAG com LangChain.

```python
import chromadb
from chromadb.config import Settings

cliente = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_data"
))

colecao = cliente.create_collection(
    name="artigos",
    metadata={"hnsw:space": "cosine"}
)

# Adicionar documentos com embeddings
colecao.add(
    documents=["O que são bancos vetoriais", "Embeddings em NLP"],
    metadatas=[{"fonte": "wiki"}, {"fonte": "blog"}],
    ids=["doc1", "doc2"]
)

# Busca semântica
resultados = colecao.query(
    query_texts=["bancos para IA"],
    n_results=3,
    where={"fonte": {"$eq": "wiki"}}
)
```

## ORMs vs Raw SQL

### Prisma (TypeScript)

```typescript
// Prisma Schema
// datasource db {
//   provider = "postgresql"
//   url      = env("DATABASE_URL")
// }

// model Usuario {
//   id        Int      @id @default(autoincrement())
//   email     String   @unique
//   nome      String?
//   posts     Post[]
//   criadoEm  DateTime @default(now())
// }

// model Post {
//   id        Int      @id @default(autoincrement())
//   titulo    String
//   conteudo  String?
//   publicado Boolean  @default(false)
//   autor     Usuario  @relation(fields: [autorId], references: [id])
//   autorId   Int
// }

import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

// Query com relações
const usuarios = await prisma.usuario.findMany({
    where: { posts: { some: { publicado: true } } },
    include: {
        posts: {
            where: { publicado: true },
            orderBy: { criadoEm: 'desc' },
            take: 5
        }
    },
    orderBy: { nome: 'asc' }
});

// Transação
await prisma.$transaction([
    prisma.conta.update({ where: { id: 1 }, data: { saldo: { decrement: 100 } } }),
    prisma.conta.update({ where: { id: 2 }, data: { saldo: { increment: 100 } } }),
]);

// Raw query (quando necessário)
const resultado = await prisma.$queryRaw`
    SELECT * FROM usuarios
    WHERE email ILIKE ${'%@gmail.com'}
`;
```

### SQLAlchemy (Python)

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Session, selectinload
from sqlalchemy import select

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    nome = Column(String)

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    autor_id = Column(Integer, ForeignKey("usuarios.id"))

engine = create_engine("postgresql://user:pass@localhost/db", echo=True)

# Eager loading com selectinload
stmt = (
    select(Usuario)
    .options(selectinload(Usuario.posts))
    .where(Usuario.email.ilike("%@gmail.com"))
    .order_by(Usuario.nome)
)
with Session(engine) as session:
    usuarios = session.scalars(stmt).all()

# Bulk insert
session.bulk_insert_mappings(Post, [
    {"titulo": "Post 1", "autor_id": 1},
    {"titulo": "Post 2", "autor_id": 1},
])
session.commit()
```

### Quando usar Raw SQL

```python
# Relatórios complexos — ORM gera SQL ineficiente
WITH RECURSIVE hierarquia AS (
    SELECT id, nome, parent_id, 1 AS nivel
    FROM categorias WHERE parent_id IS NULL
    UNION ALL
    SELECT c.id, c.nome, c.parent_id, h.nivel + 1
    FROM categorias c
    JOIN hierarquia h ON h.id = c.parent_id
)
SELECT * FROM hierarquia ORDER BY nivel, nome;
```

## Migrations

Gerenciamento de mudanças no esquema do banco ao longo do tempo.

### Prisma Migrate

```bash
npx prisma migrate dev --name add-campo-telefone
npx prisma migrate deploy  # produção
npx prisma migrate reset   # dev apenas
```

### Alembic (SQLAlchemy)

```python
# alembic/versions/0001_cria_tabelas.py
"""cria tabelas iniciais

Revision ID: 0001
Revises:
Create Date: 2026-05-16
"""

from alembic import op
import sqlalchemy as sa

revision = '0001'
down_revision = None

def upgrade():
    op.create_table(
        'usuarios',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('nome', sa.String()),
        sa.Column('criado_em', sa.DateTime(), server_default=sa.func.now()),
    )
    op.create_index('idx_email', 'usuarios', ['email'], unique=True)

def downgrade():
    op.drop_index('idx_email')
    op.drop_table('usuarios')
```

```python
# Comandos Alembic
# alembic revision --autogenerate -m "descricao"
# alembic upgrade head
# alembic downgrade -1
```

### Drizzle (TypeScript)

```typescript
import { pgTable, serial, text, timestamp } from 'drizzle-orm/pg-core';
import { migrate } from 'drizzle-orm/node-postgres/migrator';

export const usuarios = pgTable('usuarios', {
    id: serial('id').primaryKey(),
    email: text('email').notNull().unique(),
    nome: text('nome'),
    criadoEm: timestamp('criado_em').defaultNow(),
});

// migrations/0001_create_users.ts
import { sql } from 'drizzle-orm';

export async function up(db: any) {
    await db.execute(sql`
        ALTER TABLE usuarios ADD COLUMN telefone TEXT;
    `);
}

export async function down(db: any) {
    await db.execute(sql`
        ALTER TABLE usuarios DROP COLUMN telefone;
    });
}
```

## Query Optimization

### EXPLAIN ANALYZE

```sql
-- Analisar plano de execução
EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)
SELECT u.nome, COUNT(p.id) as total_posts
FROM usuarios u
LEFT JOIN posts p ON p.autor_id = u.id
WHERE u.criado_em > '2025-01-01'
GROUP BY u.id
ORDER BY total_posts DESC
LIMIT 10;

-- Indicadores importantes:
-- - Seq Scan vs Index Scan
-- - estimated rows vs actual rows (discrepância grande = estatísticas desatualizadas)
-- - Shared Hit Blocks (buffers lidos do cache)
-- - Actual Time (primeira linha vs última linha em loops)
```

### Indexing Strategies

```sql
-- 1. Composite index: colunas mais seletivas primeiro
CREATE INDEX idx_composite ON pedidos (status, criado_em DESC);

-- 2. Covering index: inclui colunas para index-only scan
CREATE INDEX idx_covering ON pedidos (cliente_id) INCLUDE (total, status);

-- 3. Partial index: apenas subset relevante
CREATE INDEX idx_recentes ON pedidos (criado_em)
    WHERE status != 'cancelado';

-- 4. Expressão: índice funcional
CREATE INDEX idx_lower_email ON usuarios (LOWER(email));

-- 5. Bloom filter: múltiplas colunas, qualquer combinação
CREATE INDEX idx_bloom ON produtos USING bloom (nome, descricao, sku);
```

```python
# Detectando N+1 com Django
from django.db import connection, reset_queries

# Antes (N+1) — 1 query para autores + N queries para livros
autores = Autor.objects.all()
for autor in autores:
    print(autor.livros.count())

# Depois — 2 queries totais
autores = Autor.objects.prefetch_related('livros').all()
for autor in autores:
    print(len(autor.livros.all()))

# Django Debug Toolbar mostra queries por request
```

### Sharding, Replication, Partitioning

```sql
-- Particionamento (PostgreSQL 10+)
CREATE TABLE vendas (
    id BIGINT,
    data DATE NOT NULL,
    valor DECIMAL(10,2)
) PARTITION BY RANGE (data);

CREATE TABLE vendas_2025 PARTITION OF vendas
    FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');

CREATE TABLE vendas_2026 PARTITION OF vendas
    FOR VALUES FROM ('2026-01-01') TO ('2027-01-01');

-- Partition pruning: PG só varre partições relevantes
EXPLAIN SELECT * FROM vendas WHERE data = '2026-05-16';
```

```yaml
# Replicação no PostgreSQL (pg_hba.conf + postgresql.conf)
# Primário
wal_level = replica
max_wal_senders = 3

# Réplica (standby)
primary_conninfo = 'host=192.168.1.10 port=5432 user=replicador'
hot_standby = on
```

## CAP Theorem

Um sistema distribuído pode garantir no máximo 2 de 3 propriedades:

| Propriedade | Significado |
|-------------|-------------|
| **C**onsistency | Todo nó vê os mesmos dados ao mesmo tempo |
| **A**vailability | Cada requisição recebe resposta (não necessariamente correta) |
| **P**artition Tolerance | Sistema continua operando mesmo com falha de comunicação |

### PACELC

Extensão do CAP: em caso de **P**artição (P), trade-off entre **A** e **C**; em estado normal (**E**lse), trade-off entre **L**atência e **C**onsistência.

| Sistema | CAP | PACELC |
|---------|-----|--------|
| PostgreSQL | CA (desliga partição) | CA/EL |
| MongoDB | CP (default) | CP/EL |
| Cassandra | AP | AP/EC |
| Redis Cluster | AP | AP/EL |
| CockroachDB | CP | CP/EC |

```python
# Modelagem de consistência no Cassandra
from cassandra.cluster import Cluster
from cassandra.query import ConsistencyLevel

cluster = Cluster(['192.168.1.10', '192.168.1.11'])
session = cluster.connect()

# QUORUM = maioria dos nós replica deve responder
# ONE = apenas um nó replica
# ALL = todos os nós replica

session.default_consistency_level = ConsistencyLevel.QUORUM

session.execute(
    "INSERT INTO usuarios (id, nome) VALUES (%s, %s)",
    (uuid.uuid4(), "João")
)

session.default_consistency_level = ConsistencyLevel.ONE
rows = session.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
```

## Referências

- **"Designing Data-Intensive Applications"** — Martin Kleppmann (2017). O livro definitivo sobre sistemas de dados distribuídos, cobrindo bancos relacionais, NoSQL, replicação, particionamento e transações.
- **"Database Internals"** — Alex Petrov (2019). Aprofunda em estruturas de armazenamento (B-tree, LSM-tree), algoritmos de indexação e sistemas distribuídos.
- **"Seven Databases in Seven Weeks"** — Eric Redmond, Jim R. Wilson (2018). Visão prática de 7 bancos diferentes.
- **"Readings in Database Systems"** (Red Book) — Peter Bailis, Joseph M. Hellerstein, Michael Stonebraker. Coleção de artigos seminais.
- **PostgreSQL Documentation** — https://www.postgresql.org/docs/current/
- **MongoDB University** — Cursos gratuitos oficiais da MongoDB.
- **FAISS GitHub** — https://github.com/facebookresearch/faiss
- **"Building Vector Search Systems"** — O'Reilly (2024) sobre sistemas de busca vetorial e RAG.
- **Aurélien Géron — "Mãos à Obra: Aprendizado de Máquina com Scikit-Learn & TensorFlow"** (capítulo sobre embeddings).
