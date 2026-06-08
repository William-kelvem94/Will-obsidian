---
tags: [etl, elt, data-pipelines, airflow, dagster, data-validation, cdc, data-engineering, skills]
updated: 2026-06-07
title: "ETL/ELT Pipelines - Data Pipeline Engineering"
date: 2026-06-01
---

# ETL/ELT Pipelines

Engenharia de pipelines de dados. Este guia cobre desde fundamentos de ETL vs ELT ate orquestracao avancada com Airflow e Dagster, validacao com Great Expectations, e padroes de producao como CDC e dead letter queues.

## Taxonomia de Topicos

- ETL vs ELT
- Batch vs Streaming
- Pipeline design patterns
- Orquestracao com Airflow
- Orquestracao com Dagster
- Data validation
- Schema evolution
- Data lake vs warehouse vs lakehouse
- Processamento incremental e CDC
- Error handling e dead letter queues
- Cost optimization

## ETL vs ELT

### ETL (Extract, Transform, Load)

```
Fonte -> [Extract] -> [Transform] -> [Load] -> Data Warehouse
              |            |            |
           Raw data    CPU-intensive   Dados
           extracao    transformacao   prontos
```

**Quando usar**:
- Dados sensiveis que precisam de transformacao antes do armazenamento
- Warehouses com capacidade de processamento limitada
- Compliance requer transformacao antes do storage
- Dados de fontes nao confiaveis

### ELT (Extract, Load, Transform)

```
Fonte -> [Extract] -> [Load] -> Data Lake/Warehouse -> [Transform]
              |            |                              |
           Raw data    Dados brutos                   Transformacao
           extracao    armazenados                    no destino
```

**Quando usar**:
- Cloud data warehouses (BigQuery, Snowflake, Redshift) com poder computacional
- Preservacao de dados brutos para reprocessamento
- Flexibilidade para transformacoes futuras
- Dados de fontes confiaveis

### Comparacao

| Aspecto | ETL | ELT |
|---|---|---|
| Ordem | Transform antes de load | Load antes de transform |
| Infraestrutura | Servidor de transformacao dedicado | Usa poder do warehouse |
| Dados brutos | Nao preservados | Preservados |
| Flexibilidade | Menor (schema fixo) | Maior (schema-on-read) |
| Custo | Infra extra | Usa warehouse existente |
| Compliance | Melhor (dados sensiveis transformados) | Requer cuidado extra |
| Velocidade | Mais lento | Mais rapido |
| Ferramentas | Airflow, Talend, Informatica | dbt, Spark, BigQuery |

## Batch vs Streaming

| Aspecto | Batch | Streaming |
|---|---|---|
| Latencia | Horas/dias | Segundos/milissegundos |
| Volume | Grandes volumes | Eventos individuais |
| Complexidade | Baixa | Alta |
| Custo | Menor por volume | Maior por evento |
| Tolerancia a falhas | Re-execucao simples | checkpointing complexo |
| Use Case | Relatorios diarios, ML training | Alertas, dashboards realtime |

## Pipeline Design Patterns

### Fan-Out Pattern

```
                    +--------+
                    | Fonte  |
                    +---+----+
                        |
              +---------+---------+
              |         |         |
              v         v         v
        +----------+ +------+ +-------+
        | Pipeline | |Pipe- | |Pipe-  |
        |   A      | |line B| |line C |
        +----------+ +------+ +-------+
              |         |         |
              v         v         v
        [Destino A] [Destino B] [Destino C]
```

```python
# Airflow - Fan-out com branching
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime

def escolher_caminho(**kwargs):
    """Decide qual caminho seguir baseado nos dados."""
    volume = kwargs["ti"].xcom_pull(task_ids="extrair", key="volume")
    if volume > 1000000:
        return "processar_grande"
    return "processar_normal"

with DAG("fanout_pipeline", start_date=datetime(2026, 1, 1), schedule="@daily") as dag:
    extrair = PythonOperator(task_id="extrair", python_callable=extrair_dados)

    branch = BranchPythonOperator(task_id="branch", python_callable=escolher_caminho)

    processar_grande = PythonOperator(task_id="processar_grande", python_callable=processar_grande_volume)
    processar_normal = PythonOperator(task_id="processar_normal", python_callable=processar_normal_volume)

    carregar = PythonOperator(task_id="carregar", python_callable=carregar_dados)

    extrair >> branch >> [processar_grande, processar_normal] >> carregar
```

### Fan-In Pattern

```
        +----------+ +------+ +-------+
        | Fonte A  | |Fonte | |Fonte  |
        |          | |  B   | |  C    |
        +----+-----+ +--+---+ +--+----+
             |          |        |
             +----------+--------+
                        |
                        v
                  +-----+------+
                  |  Unificar  |
                  +-----+------+
                        |
                        v
                  [ Destino ]
```

### DAG Orchestration

```
    extrair_usuarios    extrair_pedidos    extrair_produtos
          |                    |                  |
          v                    v                  v
    validar_usuarios    validar_pedidos    validar_produtos
          |                    |                  |
          +----------+---------+--------+---------+
                     |                  |
                     v                  v
              transformar_dados   carregar_dwh
                     |                  |
                     +--------+---------+
                              |
                              v
                        gerar_relatorio
```

## Orquestracao com Apache Airflow

### DAG Completa de Producao

```python
# dags/jarvis_etl_pipeline.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.utils.task_group import TaskGroup
from datetime import datetime, timedelta
import pandas as pd
import sqlalchemy as sa
from typing import List

# Default args
default_args = {
    "owner": "data-engineering",
    "depends_on_past": False,
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "retry_exponential_backoff": True,
    "max_retry_delay": timedelta(hours=1),
}

def extrair_usuarios(**kwargs):
    """Extrai dados de usuarios do banco transacional."""
    engine = sa.create_engine("postgresql://user:pass@source-db:5432/app")
    query = """
        SELECT id, email, nome, status, criado_em, atualizado_em
        FROM usuarios
        WHERE atualizado_em >= '{{ ds }}'
    """
    df = pd.read_sql(query, engine)
    df.to_csv("/tmp/usuarios.csv", index=False)
    kwargs["ti"].xcom_push(key="row_count", value=len(df))

def extrair_pedidos(**kwargs):
    """Extrai dados de pedidos."""
    engine = sa.create_engine("postgresql://user:pass@source-db:5432/app")
    query = """
        SELECT p.id, p.usuario_id, p.total, p.status, p.criado_em,
               i.produto_id, i.quantidade, i.preco
        FROM pedidos p
        JOIN itens_pedido i ON i.pedido_id = p.id
        WHERE p.criado_em >= '{{ ds }}'
    """
    df = pd.read_sql(query, engine)
    df.to_csv("/tmp/pedidos.csv", index=False)
    kwargs["ti"].xcom_push(key="row_count", value=len(df))

def validar_dados(**kwargs):
    """Valida qualidade dos dados extraidos."""
    usuarios = pd.read_csv("/tmp/usuarios.csv")
    pedidos = pd.read_csv("/tmp/pedidos.csv")

    # Validacoes
    assert len(usuarios) > 0, "Nenhum usuario extraido"
    assert len(pedidos) > 0, "Nenhum pedido extraido"
    assert usuarios["email"].isnull().sum() == 0, "Emails nulos encontrados"
    assert (pedidos["total"] >= 0).all(), "Totais negativos encontrados"

    # Report
    print(f"Usuarios: {len(usuarios)}, Pedidos: {len(pedidos)}")

def transformar_dados(**kwargs):
    """Transforma dados para modelo analitico."""
    usuarios = pd.read_csv("/tmp/usuarios.csv")
    pedidos = pd.read_csv("/tmp/pedidos.csv")

    # Agregacoes
    pedidos_agg = pedidos.groupby("usuario_id").agg(
        total_pedidos=("id", "count"),
        total_gasto=("total", "sum"),
        ticket_medio=("total", "mean"),
        ultimo_pedido=("criado_em", "max"),
    ).reset_index()

    # Merge
    resultado = usuarios.merge(pedidos_agg, on="usuario_id", how="left")
    resultado.fillna({"total_pedidos": 0, "total_gasto": 0, "ticket_medio": 0}, inplace=True)

    resultado.to_csv("/tmp/usuarios_analitico.csv", index=False)

def carregar_dwh(**kwargs):
    """Carrega dados transformados no data warehouse."""
    engine = sa.create_engine("postgresql://user:pass@dwh-db:5432/analytics")
    df = pd.read_csv("/tmp/usuarios_analitico.csv")

    with engine.begin() as conn:
        df.to_sql("usuarios_analitico", conn, if_exists="append", index=False, method="multi")

def gerar_alertas(**kwargs):
    """Gera alertas baseado nos dados."""
    usuarios = pd.read_csv("/tmp/usuarios_analitico.csv")

    # Alerta: usuarios sem pedidos
    sem_pedidos = usuarios[usuarios["total_pedidos"] == 0]
    if len(sem_pedidos) > 100:
        print(f"ALERTA: {len(sem_pedidos)} usuarios sem pedidos")

# DAG definition
with DAG(
    "jarvis_etl_diario",
    default_args=default_args,
    description="Pipeline ETL diario do JARVIS",
    schedule_interval="0 2 * * *",  # 2am todos os dias
    start_date=datetime(2026, 1, 1),
    catchup=False,
    max_active_runs=1,
    tags=["jarvis", "etl", "diario"],
) as dag:

    # Task groups para organizacao
    with TaskGroup("extracao", tooltip="Extracao de dados") as extracao:
        ext_usuarios = PythonOperator(task_id="usuarios", python_callable=extrair_usuarios)
        ext_pedidos = PythonOperator(task_id="pedidos", python_callable=extrair_pedidos)

        ext_usuarios >> ext_pedidos

    with TaskGroup("validacao", tooltip="Validacao de dados") as validacao:
        val_dados = PythonOperator(task_id="qualidade", python_callable=validar_dados)

    with TaskGroup("transformacao", tooltip="Transformacao de dados") as transformacao:
        trans_dados = PythonOperator(task_id="agregar", python_callable=transformar_dados)

    with TaskGroup("carga", tooltip="Carga no warehouse") as carga:
        load_dwh = PythonOperator(task_id="dwh", python_callable=carregar_dwh)
        alertas = PythonOperator(task_id="alertas", python_callable=gerar_alertas)

        load_dwh >> alertas

    # Dependencies
    extracao >> validacao >> transformacao >> carga
```

### Airflow Operators Essenciais

```python
# Bash Operator
run_dbt = BashOperator(
    task_id="run_dbt",
    bash_command="cd /opt/dbt && dbt run --models staging.*",
)

# Python Operator com parametros
process_data = PythonOperator(
    task_id="process_data",
    python_callable=processar,
    op_kwargs={"fonte": "api", "formato": "parquet"},
)

# Sensor - espera condicao
wait_for_upstream = ExternalTaskSensor(
    task_id="wait_for_source",
    external_dag_id="source_pipeline",
    external_task_id="final_task",
    timeout=3600,
    poke_interval=60,
)

# Branch Python Operator
def choose_env(**kwargs):
    return "task_prod" if kwargs["ds"] >= "2026-01-01" else "task_legacy"

branch = BranchPythonOperator(task_id="branch", python_callable=choose_env)
```

## Orquestracao com Dagster

### Asset-Based Pipeline

```python
# jarvis_pipeline/assets.py
from dagster import asset, op, job, Definitions, AssetExecutionContext
import pandas as pd
import sqlalchemy as sa

@asset
def usuarios_raw(context: AssetExecutionContext) -> pd.DataFrame:
    """Extrai usuarios do banco transacional."""
    engine = sa.create_engine("postgresql://user:pass@source-db:5432/app")
    query = "SELECT * FROM usuarios WHERE atualizado_em >= CURRENT_DATE - INTERVAL '1 day'"
    df = pd.read_sql(query, engine)
    context.log.info(f"Extraidos {len(df)} usuarios")
    return df

@asset
def pedidos_raw(context: AssetExecutionContext) -> pd.DataFrame:
    """Extrai pedidos do banco transacional."""
    engine = sa.create_engine("postgresql://user:pass@source-db:5432/app")
    query = "SELECT * FROM pedidos WHERE criado_em >= CURRENT_DATE - INTERVAL '1 day'"
    df = pd.read_sql(query, engine)
    context.log.info(f"Extraidos {len(df)} pedidos")
    return df

@asset
def usuarios_validados(usuarios_raw: pd.DataFrame) -> pd.DataFrame:
    """Valida dados de usuarios."""
    assert len(usuarios_raw) > 0, "Nenhum usuario extraido"
    assert usuarios_raw["email"].notna().all(), "Emails nulos"
    return usuarios_raw

@asset
def pedidos_validados(pedidos_raw: pd.DataFrame) -> pd.DataFrame:
    """Valida dados de pedidos."""
    assert len(pedidos_raw) > 0, "Nenhum pedido extraido"
    assert (pedidos_raw["total"] >= 0).all(), "Totais negativos"
    return pedidos_raw

@asset
def usuarios_analitico(
    context: AssetExecutionContext,
    usuarios_validados: pd.DataFrame,
    pedidos_validados: pd.DataFrame,
) -> pd.DataFrame:
    """Cria tabela analitica de usuarios."""
    pedidos_agg = pedidos_validados.groupby("usuario_id").agg(
        total_pedidos=("id", "count"),
        total_gasto=("total", "sum"),
        ticket_medio=("total", "mean"),
    ).reset_index()

    resultado = usuarios_validados.merge(pedidos_agg, on="id", how="left")
    resultado.fillna({"total_pedidos": 0, "total_gasto": 0}, inplace=True)

    context.log.info(f"Tabela analitica: {len(resultado)} linhas")
    return resultado

@asset
def usuarios_no_dwh(usuarios_analitico: pd.DataFrame) -> None:
    """Carrega no data warehouse."""
    engine = sa.create_engine("postgresql://user:pass@dwh-db:5432/analytics")
    with engine.begin() as conn:
        usuarios_analitico.to_sql("usuarios_analitico", conn, if_exists="append", index=False)

# Definitions
defs = Definitions(
    assets=[
        usuarios_raw,
        pedidos_raw,
        usuarios_validados,
        pedidos_validados,
        usuarios_analitico,
        usuarios_no_dwh,
    ],
)
```

```bash
# Dagster CLI
dagster dev  # Inicia UI local

# Materializa assets
dagster asset materialize --select usuarios_analitico

# Testa pipeline
dagster job execute -j usuarios_analitico
```

### Airflow vs Dagster

| Aspecto | Airflow | Dagster |
|---|---|---|
| Paradigma | Task-oriented (DAGs) | Data asset-oriented |
| Foco | Orquestracao de workflows | Data pipeline development |
| Data awareness | Nao (so tasks) | Sim (data flow entre assets) |
| Testing | Complexo | Nativo (unit tests em assets) |
| UI | Task execution view | Data lineage view |
| Learning curve | Media | Media-Alta |
| Ideal para | Workflows genericos | Data pipelines complexos |

## Data Validation com Great Expectations

```python
# expectations/usuarios.json
import great_expectations as gx
from great_expectations.core import ExpectationSuite

# Cria suite
suite = gx.ExpectationSuite(name="usuarios.validacao")

# Expectations
suite.add_expectation(
    gx.expectations.ExpectColumnToExist(column="id")
)
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToNotBeNull(column="email")
)
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToMatchRegex(
        column="email",
        regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    )
)
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeBetween(
        column="total_gasto",
        min_value=0,
        max_value=1000000
    )
)
suite.add_expectation(
    gx.expectations.ExpectTableRowCountToBeBetween(
        min_value=1,
        max_value=None
    )
)

# Executa validacao
validator = gx.get_validator(
    batch=usuarios_df,
    expectation_suite=suite,
)

result = validator.validate()

if not result["success"]:
    print("Validacao falhou:")
    for r in result["results"]:
        if not r["success"]:
            print(f"  - {r['expectation_config']['type']}: {r['exception_info']}")
    raise ValueError("Dados nao passaram na validacao")
```

### Great Expectations no Airflow

```python
from airflow.providers.great_expectations.operators.great_expectations import GreatExpectationsOperator

validate_usuarios = GreatExpectationsOperator(
    task_id="validate_usuarios",
    data_context_root_dir="great_expectations",
    dataframe_to_validate=usuarios_df,
    expectation_suite_name="usuarios.validacao",
    execution_engine="PandasExecutionEngine",
    return_json_dict=True,
)
```

## Schema Evolution

### Avro Schema Evolution

```json
// schema_v1.avsc
{
  "type": "record",
  "name": "Usuario",
  "namespace": "com.jarvis",
  "fields": [
    {"name": "id", "type": "string"},
    {"name": "email", "type": "string"},
    {"name": "nome", "type": "string"}
  ]
}

// schema_v2.avsc - Adiciona campo (backward compatible)
{
  "type": "record",
  "name": "Usuario",
  "namespace": "com.jarvis",
  "fields": [
    {"name": "id", "type": "string"},
    {"name": "email", "type": "string"},
    {"name": "nome", "type": "string"},
    {"name": "status", "type": "string", "default": "ativo"}
  ]
}

// schema_v3.avsc - Remove campo (forward compatible)
{
  "type": "record",
  "name": "Usuario",
  "namespace": "com.jarvis",
  "fields": [
    {"name": "id", "type": "string"},
    {"name": "email", "type": "string"},
    {"name": "nome", "type": ["null", "string"], "default": null},
    {"name": "status", "type": "string", "default": "ativo"}
  ]
}
```

### Protobuf Schema Evolution

```protobuf
// usuario.proto
syntax = "proto3";

message Usuario {
  string id = 1;
  string email = 2;
  string nome = 3;
  // Campo removido: string telefone = 4;  // NUNCA reutilizar numero
  string status = 5;
  repeated string tags = 6;  // Campo novo
}
```

### Regras de Evolucao

| Mudanca | Compatibilidade | Impacto |
|---|---|---|
| Adicionar campo com default | Backward + Forward | Seguro |
| Remover campo com default | Backward + Forward | Seguro |
| Renomear campo | Breaking | Nao fazer |
| Mudar tipo de campo | Breaking | Nao fazer |
| Adicionar campo obrigatorio | Breaking | Evitar |

## Data Lake vs Data Warehouse vs Data Lakehouse

| Aspecto | Data Lake | Data Warehouse | Data Lakehouse |
|---|---|---|---|
| Dados | Brutos, qualquer formato | Estruturados, schema-on-write | Brutos + estruturados |
| Schema | Schema-on-read | Schema-on-write | Schema-on-read + write |
| Custo | Baixo (object storage) | Alto (storage proprietario) | Medio |
| Performance | Variavel | Alta (otimizado) | Alta (com indexing) |
| Use Case | ML, exploracao | BI, relatorios | BI + ML unificado |
| Formatos | Parquet, JSON, CSV | Proprietario | Parquet + Delta/Iceberg |
| Transacoes | Nao | ACID | ACID (Delta, Iceberg) |
| Ferramentas | Spark, Presto | BigQuery, Snowflake, Redshift | Databricks, Trino |

## Processamento Incremental e CDC

### CDC com Debezium

```json
// Debezium connector config
{
  "name": "usuarios-connector",
  "config": {
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    "database.hostname": "source-db",
    "database.port": "5432",
    "database.user": "debezium",
    "database.password": "password",
    "database.dbname": "app",
    "topic.prefix": "jarvis",
    "table.include.list": "public.usuarios,public.pedidos",
    "plugin.name": "pgoutput"
  }
}
```

```python
# Consumindo CDC events
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "jarvis.public.usuarios",
    bootstrap_servers=["kafka:9092"],
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset="earliest",
)

for message in consumer:
    event = message.value
    if event["op"] == "c":
        print(f"CREATE: {event['after']}")
    elif event["op"] == "u":
        print(f"UPDATE: {event['before']} -> {event['after']}")
    elif event["op"] == "d":
        print(f"DELETE: {event['before']}")
```

### Incremental Processing no Airflow

```python
def processar_incremental(**kwargs):
    """Processa apenas dados novos desde ultima execucao."""
    execution_date = kwargs["ds"]  # Data de execucao (YYYY-MM-DD)

    engine = sa.create_engine("postgresql://user:pass@source-db:5432/app")

    # Busca apenas dados novos
    query = f"""
        SELECT * FROM pedidos
        WHERE criado_em >= '{execution_date}'
          AND criado_em < '{execution_date}'::date + INTERVAL '1 day'
    """

    df = pd.read_sql(query, engine)
    processar(df)
```

## Error Handling e Dead Letter Queues

### Dead Letter Queue Pattern

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import json

def processar_registro(registro: dict) -> dict:
    """Processa um registro. Pode falhar."""
    try:
        # Logica de processamento
        resultado = transformar(registro)
        return {"status": "success", "data": resultado}
    except Exception as e:
        return {"status": "error", "error": str(e), "record": registro}

def salvar_dlq(registros_erro: list):
    """Salva registros com erro na dead letter queue."""
    if not registros_erro:
        return

    with open("/tmp/dlq/erros.jsonl", "a") as f:
        for registro in registros_erro:
            f.write(json.dumps({
                "timestamp": datetime.now().isoformat(),
                "error": registro["error"],
                "record": registro["record"],
            }) + "\n")

    print(f"Salvos {len(registros_erro)} registros na DLQ")

def processar_com_dlq(**kwargs):
    """Processa registros com DLQ para erros."""
    registros = carregar_registros()
    erros = []
    sucessos = []

    for registro in registros:
        resultado = processar_registro(registro)
        if resultado["status"] == "error":
            erros.append(resultado)
        else:
            sucessos.append(resultado["data"])

    # Salva DLQ
    salvar_dlq(erros)

    # Processa sucessos
    if sucessos:
        salvar_dwh(sucessos)

    kwargs["ti"].xcom_push(key="erros", value=len(erros))
    kwargs["ti"].xcom_push(key("sucessos"), value=len(sucessos))
```

## Cost Optimization

### Estrategias de Otimizacao

| Estrategia | Impacto | Implementacao |
|---|---|---|
| Particionamento | Reduz scan de dados | Particionar por data |
| Compressao | Reduz storage 60-80% | Usar Parquet com Snappy |
| Clustered indexes | Melhora query performance | Ordenar por coluna de filtro |
| Materialized views | Evita recomputacao | Cache de queries frequentes |
| Spot instances | Reduz custo 60-70% | Usar para workloads tolerantes |
| Data lifecycle | Remove dados antigos | Archive para cold storage |
| Query optimization | Reduz computacao | EXPLAIN ANALYZE, indices |

### Parquet Optimization

```python
import pyarrow.parquet as pq
import pyarrow as pa

# Escreve Parquet otimizado
table = pa.Table.from_pandas(df)

pq.write_table(
    table,
    "dados.parquet",
    compression="snappy",        # Compressao
    row_group_size=100000,       # Tamanho do row group
    use_dictionary=True,         # Dictionary encoding
    write_statistics=True,       # Statistics para predicate pushdown
)

# Le com predicate pushdown (so le dados relevantes)
table = pq.read_table(
    "dados.parquet",
    filters=[("data", ">=", "2026-01-01")],
    columns=["id", "nome", "total"],  # Project columns
)
```

## Referencias Cruzadas

- [[../02-software-engineering/database|Database]] - Fundamentos de banco de dados
- [[../02-software-engineering/performance|Performance]] - Otimizacao de queries
- [[streaming|Stream Processing]] - Processamento em tempo real
- [[../03-infrastructure-mcp/INDEX|Infrastructure]] - Infraestrutura para pipelines
- [[../devops/Observabilidade|Observabilidade]] - Monitoring de pipelines
