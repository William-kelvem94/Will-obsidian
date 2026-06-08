---
tags: [data-engineering, index, hub, etl, streaming, data-pipelines, skills]
updated: 2026-06-07
title: "Data Engineering - Index"
date: 2026-06-01
---

# Data Engineering

Hub central de engenharia de dados do JARVIS. Este dominio cobre desde fundamentos de ETL/ELT ate processamento de streaming em tempo real, com foco em pipelines escalaveis, confiaveis e custo-eficientes.

## Panorama da Engenharia de Dados

A engenharia de dados evoluiu de simples scripts ETL para ecossistemas complexos de processamento distribuido. O landscape atual inclui:

```
                    +------------------------+
                    |     Fontes de Dados    |
                    |  DBs, APIs, Streams,   |
                    |  Files, IoT, Logs      |
                    +-----------+------------+
                                |
                    +-----------v------------+
                    |     Ingestao           |
                    |  Batch | Streaming     |
                    +-----------+------------+
                                |
                    +-----------v------------+
                    |     Processamento      |
                    |  Transformacao,        |
                    |  Validacao, Enriquec.  |
                    +-----------+------------+
                                |
                    +-----------v------------+
                    |     Armazenamento      |
                    |  Data Lake | Warehouse |
                    |  Lakehouse             |
                    +-----------+------------+
                                |
                    +-----------v------------+
                    |     Consumo            |
                    |  BI, ML, APIs, Apps    |
                    +------------------------+
```

## Taxonomia Completa

```
data-engineering/
├── INDEX.md ....................... Hub central (voce esta aqui)
├── etl-pipelines.md ............... Pipelines ETL/ELT (Airflow, Dagster)
└── streaming.md ................... Processamento de streaming (Kafka, Flink)
```

## Notas Ativas

### [[etl-pipelines|ETL/ELT Pipelines]]
Guia completo de pipelines de dados batch e streaming. Cobre ETL vs ELT, orquestracao com Apache Airflow (DAGs em Python) e Dagster (asset-based), validacao com Great Expectations, evolucao de schema (Avro, Protobuf), processamento incremental, CDC (Change Data Capture), dead letter queues, e otimizacao de custos. Inclui exemplos completos de DAGs e pipelines de producao.

### [[streaming|Stream Processing]]
Processamento de dados em tempo real com Apache Kafka e Flink. Cobre arquitetura do Kafka (brokers, topics, partitions, consumer groups), padroes de event-driven architecture, semantica de processamento (exactly-once, at-least-once), Schema Registry, event sourcing, CQRS com streaming, pipelines de analytics em tempo real, e monitoring de sistemas de streaming.

## Arquiteturas de Pipeline

### Lambda Architecture

```
                    +-------------------+
                    |   Camada Batch    |
                    |  (Hadoop/Spark)   |
                    |  Dados completos  |
                    +--------+----------+
                             |
                    +--------v----------+
   Fonte --------->|  Camada Serving   |<--+
                    |  (View unificada) |
                    +--------^----------+
                             |
                    +--------+----------+
                    |  Camada Speed     |
                    |  (Storm/Flink)    |
                    |  Dados recentes   |
                    +-------------------+
```

**Quando usar**: Sistemas que precisam de visoes completas (batch) e em tempo real (speed) simultaneamente. Complexo de manter, sendo substituido por Kappa.

### Kappa Architecture

```
                    +-------------------+
                    |   Stream Layer    |
                    |  (Kafka + Flink)  |
                    |  Batch = Stream   |
                    |  com janela       |
                    +--------+----------+
                             |
                    +--------v----------+
                    |   Serving Layer   |
                    |  (DB / Data Lake) |
                    +-------------------+
```

**Quando usar**: Simplificacao da Lambda. Tudo e tratado como stream. Re-processamento via replay do Kafka.

### Data Mesh

```
                    +-------------------+
                    |   Domain Team A   |
                    |  Produto de Dados |
                    |  (Owner, SLA)     |
                    +--------+----------+
                             |
                    +--------v----------+
   Consumidor ---> |  Self-Service      |
                    |  Data Platform     |
                    +--------^----------+
                             |
                    +--------+----------+
                    |   Domain Team B   |
                    |  Produto de Dados |
                    |  (Owner, SLA)     |
                    +-------------------+
```

**Quando usar**: Organizacoes grandes com multiplas equipes. Cada dominio e dono dos seus dados como produto. Requer cultura de data governance.

## Comparacao de Ferramentas

| Ferramenta | Tipo | Linguagem | Use Case | Curva |
|---|---|---|---|---|
| Apache Airflow | Orquestracao | Python | DAGs batch, scheduling | Media |
| Dagster | Orquestracao | Python | Data assets, testing | Media-Alta |
| Apache Spark | Processamento | Scala/Python/SQL | Batch processing, ML | Media |
| Apache Kafka | Streaming | Java/Scala | Event streaming | Alta |
| Apache Flink | Stream Processing | Java/Scala/Python | Real-time processing | Alta |
| dbt | Transformacao | SQL | Transformations in warehouse | Baixa |
| Great Expectations | Validacao | Python | Data quality checks | Baixa-Media |
| Apache Beam | Processamento | Java/Python | Pipeline portavel (batch+stream) | Alta |

## Guia de Navegacao

### Por Nivel

```
Iniciante:
  etl-pipelines.md (ETL basics, Airflow DAGs)
     |
     v
Intermediario:
  etl-pipelines.md (Dagster, Great Expectations, CDC)
     |
     v
Avancado:
  streaming.md (Kafka, Flink, Event Sourcing)
```

### Por Caso de Uso

| Caso de Uso | Notas | Ferramentas |
|---|---|---|
| Pipeline batch diario | [[etl-pipelines]] | Airflow, dbt |
| Pipeline com validacao | [[etl-pipelines]] | Great Expectations |
| CDC de banco de dados | [[etl-pipelines]] | Debezium, Airflow |
| Analytics em tempo real | [[streaming]] | Kafka, Flink |
| Event-driven microservices | [[streaming]] | Kafka, Schema Registry |
| Reprocessamento historico | [[streaming]] | Kafka replay, Flink |

## Referencias Cruzadas

### Skills Internas

| Dominio | Notas | Conexao |
|---|---|---|
| [[../02-software-engineering/database|Database]] | Modelagem, SQL, indices | Pipelines consomem e produzem dados |
| [[../02-software-engineering/performance|Performance]] | Query optimization, caching | Pipelines precisam ser eficientes |
| [[../02-software-engineering/advanced-backend-architecture|Advanced Backend]] | Event-driven, CQRS | Compartilha padroes com streaming |
| [[../03-infrastructure-mcp/INDEX|Infrastructure]] | MCP servers, monitoring | Infraestrutura para pipelines |
| [[../devops/Observabilidade|Observabilidade]] | Logging, metrics | Monitoring de pipelines |
| [[../devops/ci-cd|CI/CD]] | Deploy pipelines | CI/CD para data pipelines |

### Conhecimento Geral

| Nota | Conexao |
|---|---|
| [[../../../04-Conhecimentos/07-Humanidades/Computacao/Algoritmos-e-Estruturas|Algoritmos e Estruturas]] | Base para processamento eficiente |
| [[../../../04-Conhecimentos/07-Humanidades/Computacao/Ciencia-da-Computacao|Ciencia da Computacao]] | Fundamentos de sistemas distribuidos |

### Skills Relacionadas

| Dominio | Notas |
|---|---|
| [[../01-agentic-intelligence/INDEX|Agentic Intelligence]] | Agentes consomem dados processados |
| [[../04-knowledge-systems/INDEX|Knowledge Systems]] | RAG pipelines usam dados estruturados |

## Principios de Data Engineering

- **Dados como produto** - Cada pipeline tem dono, SLA e documentacao
- **Idempotencia** - Pipelines devem ser re-executaveis sem duplicacao
- **Schema evolution** - Schemas evoluem sem quebrar consumidores
- **Data quality first** - Validacao antes de producao, nao depois
- **Cost awareness** - Otimizar custo de computacao e armazenamento
- **Observability** - Logs, metricas e alertas para cada pipeline
- **Reproducibility** - Todo dado pode ser reprocessado do zero

## Pre-requisitos Recomendados

- [[../02-software-engineering/database|Database Fundamentals]] - SQL e modelagem de dados
- [[../02-software-engineering/backend|Backend Fundamentals]] - Python para pipelines
- [[../../../04-Conhecimentos/07-Humanidades/Computacao/Ciencia-da-Computacao|Ciencia da Computacao]] - Sistemas distribuidos

## Status do Dominio

| Area | Cobertura | Ultima Atualizacao |
|---|---|---|
| ETL/ELT Pipelines | Completa | 2026-05-16 |
| Stream Processing | Completa | 2026-05-16 |
| Data Quality | Parcial (via Great Expectations) | 2026-05-16 |
| Data Governance | Parcial | 2026-05-16 |
| Machine Learning Ops | Nao coberto | - |
