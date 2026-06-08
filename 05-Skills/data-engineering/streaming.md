---
tags: [streaming, kafka, flink, event-driven, event-sourcing, cqrs, real-time, data-engineering, skills]
updated: 2026-06-08
title: "Stream Processing - Real-Time Data Engineering"
date: 2026-06-01
---

# Stream Processing

Processamento de dados em tempo real. Este guia cobre arquitetura do Kafka, processamento com Flink, padroes de event-driven architecture, event sourcing, CQRS, e monitoring de sistemas de streaming em producao.

## Taxonomia de Topicos

- Arquitetura do Kafka
- Event-driven architecture
- Stream processing com Flink
- Spark Streaming vs Flink vs Kafka Streams
- Semantica de processamento
- Schema Registry
- Event sourcing
- CQRS com streaming
- Real-time analytics
- Monitoring e alerting

## Arquitetura do Kafka

### Componentes Principais

```
                    +------------------------------------------+
                    |              Kafka Cluster               |
                    |                                          |
                    |  +--------+  +--------+  +--------+      |
                    |  |Broker 1|  |Broker 2|  |Broker 3|      |
                    |  +---+----+  +---+----+  +---+----+      |
                    |      |          |          |              |
                    |  +---v----+  +--v-----+  +-v------+      |
                    |  |Topic A |  |Topic A |  |Topic A |      |
                    |  |P0, P1  |  |P2, P3  |  |P4, P5  |      |
                    |  +--------+  +--------+  +--------+      |
                    |                                          |
                    +------------------------------------------+
                               |              |
                    +----------v----+   +-----v---------+
                    | Consumer Grp 1|   | Consumer Grp 2|
                    | (C1, C2, C3)  |   | (C4, C5)      |
                    +---------------+   +---------------+
```

### Conceitos Fundamentais

| Conceito | Definicao | Analogia |
|---|---|---|
| Broker | Servidor Kafka | Caixa de correio |
| Topic | Categoria de mensagens | Pasta de emails |
| Partition | Subdivisao ordenada do topic | Fila numerada |
| Offset | Posicao na partition | Numero da carta |
| Producer | Publica mensagens | Remetente |
| Consumer | Consome mensagens | Destinatario |
| Consumer Group | Grupo de consumidores | Equipe de leitura |
| Replica | Copia da partition | Backup |
| ISR | In-Sync Replicas | Replicas atualizadas |

### Producer em Python

```python
from confluent_kafka import Producer
import json

conf = {
    "bootstrap.servers": "kafka1:9092,kafka2:9092,kafka3:9092",
    "acks": "all",                    # Espera todas as replicas
    "retries": 3,                     # Retenta em falha
    "batch.size": 16384,              # Batch de 16KB
    "linger.ms": 5,                   # Espera 5ms para batch
    "compression.type": "lz4",        # Compressao
    "enable.idempotence": True,       # Exactly-once
}

producer = Producer(conf)

def delivery_report(err, msg):
    if err:
        print(f"Erro: {err}")
    else:
        print(f"Enviado para {msg.topic()} [{msg.partition()}] offset {msg.offset()}")

# Produz mensagem
def publicar_evento(topic: str, key: str, value: dict):
    producer.produce(
        topic=topic,
        key=key.encode("utf-8"),
        value=json.dumps(value).encode("utf-8"),
        callback=delivery_report,
    )
    producer.poll(0)  # Processa callbacks

# Flush antes de sair
producer.flush()
```

### Consumer em Python

```python
from confluent_kafka import Consumer, KafkaError
import json

conf = {
    "bootstrap.servers": "kafka1:9092,kafka2:9092,kafka3:9092",
    "group.id": "jarvis-processamento",
    "auto.offset.reset": "earliest",
    "enable.auto.commit": False,      # Commit manual
    "max.poll.interval.ms": 300000,
    "session.timeout.ms": 10000,
}

consumer = Consumer(conf)
consumer.subscribe(["jarvis.public.usuarios", "jarvis.public.pedidos"])

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            print(f"Erro: {msg.error()}")
            continue

        # Processa mensagem
        evento = json.loads(msg.value().decode("utf-8"))
        processar_evento(evento)

        # Commit apos processamento
        consumer.commit(msg)

except KeyboardInterrupt:
    pass
finally:
    consumer.close()
```

## Event-Driven Architecture Patterns

### Event Notification

```
Servico A --[Evento: "PedidoCriado"]--> Kafka --> Servico B (reage)
                                                Servico C (reage)
                                                Servico D (reage)
```

```python
# Publica evento
def criar_pedido(pedido: dict):
    # Salva no DB
    db.add(pedido)
    db.commit()

    # Publica evento
    publicar_evento("pedidos", pedido["id"], {
        "type": "PedidoCriado",
        "data": pedido,
        "timestamp": datetime.now().isoformat(),
    })
```

### Event-Carried State Transfer

```
Servico A --[Evento com dados completos]--> Kafka
                                            |
Servico B <---[Atualiza cache local]--------+
```

```python
# Consumer que mantem estado local
class UsuarioCache:
    def __init__(self):
        self.cache = {}
        self.consumer = criar_consumer("jarvis.public.usuarios")

    def consumir(self):
        for msg in self.consumer:
            evento = json.loads(msg.value())
            if evento["type"] == "UsuarioAtualizado":
                self.cache[evento["data"]["id"]] = evento["data"]
            elif evento["type"] == "UsuarioRemovido":
                self.cache.pop(evento["data"]["id"], None)

    def get_usuario(self, user_id: str) -> dict:
        return self.cache.get(user_id)
```

### Event Sourcing

```
State = Apply(Event1, Event2, Event3, ...)

+----------------+     +----------------+     +----------------+
| UsuarioCriado  | --> | EmailAlterado  | --> | StatusMudado   |
| {id, email}    |     | {id, novo}     |     | {id, status}   |
+----------------+     +----------------+     +----------------+
```

```python
from dataclasses import dataclass
from typing import List, Union
from datetime import datetime

@dataclass
class UsuarioCriado:
    user_id: str
    email: str
    nome: str
    timestamp: datetime

@dataclass
class EmailAlterado:
    user_id: str
    antigo_email: str
    novo_email: str
    timestamp: datetime

@dataclass
class StatusMudado:
    user_id: str
    antigo_status: str
    novo_status: str
    timestamp: datetime

Event = Union[UsuarioCriado, EmailAlterado, StatusMudado]

class Usuario:
    def __init__(self, user_id: str):
        self.id = user_id
        self.email = None
        self.nome = None
        self.status = "pendente"
        self.events: List[Event] = []

    def apply(self, event: Event):
        if isinstance(event, UsuarioCriado):
            self.email = event.email
            self.nome = event.nome
        elif isinstance(event, EmailAlterado):
            self.email = event.novo_email
        elif isinstance(event, StatusMudado):
            self.status = event.novo_status
        self.events.append(event)

    @classmethod
    def from_events(cls, user_id: str, events: List[Event]) -> "Usuario":
        usuario = cls(user_id)
        for event in events:
            usuario.apply(event)
        return usuario

# Uso
eventos = carregar_eventos_do_kafka("usuario-123")
usuario = Usuario.from_events("usuario-123", eventos)
print(usuario.email, usuario.status)
```

## Stream Processing com Apache Flink

### Flink com Python (PyFlink)

```python
# flink_job.py
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, EnvironmentSettings
from pyflink.common.typeinfo import Types

# Setup
env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(4)

# Le do Kafka
env.add_jars("file:///opt/flink/lib/flink-sql-connector-kafka-1.17.0.jar")

t_env = StreamTableEnvironment.create(env)

# Cria tabela source (Kafka)
t_env.execute_sql("""
    CREATE TABLE pedidos_source (
        id STRING,
        usuario_id STRING,
        total DOUBLE,
        status STRING,
        criado_em TIMESTAMP(3),
        WATERMARK FOR criado_em AS criado_em - INTERVAL '5' SECOND
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'jarvis.public.pedidos',
        'properties.bootstrap.servers' = 'kafka:9092',
        'properties.group.id' = 'flink-analytics',
        'format' = 'json',
        'scan.startup.mode' = 'latest-offset'
    )
""")

# Cria tabela sink (PostgreSQL)
t_env.execute_sql("""
    CREATE TABLE metrics_sink (
        usuario_id STRING,
        total_pedidos BIGINT,
        total_gasto DOUBLE,
        ticket_medio DOUBLE,
        window_start TIMESTAMP(3),
        window_end TIMESTAMP(3)
    ) WITH (
        'connector' = 'jdbc',
        'url' = 'jdbc:postgresql://dwh:5432/analytics',
        'table-name' = 'usuario_metrics',
        'username' = 'flink',
        'password' = 'flinkpass'
    )
""")

# Query com tumbling window
t_env.execute_sql("""
    INSERT INTO metrics_sink
    SELECT
        usuario_id,
        COUNT(*) as total_pedidos,
        SUM(total) as total_gasto,
        AVG(total) as ticket_medio,
        TUMBLE_START(criado_em, INTERVAL '1' HOUR) as window_start,
        TUMBLE_END(criado_em, INTERVAL '1' HOUR) as window_end
    FROM pedidos_source
    GROUP BY
        usuario_id,
        TUMBLE(criado_em, INTERVAL '1' HOUR)
""").wait()
```

### Flink DataStream API (Java)

```java
// FlinkJob.java
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.windowing.time.Time;
import org.apache.flink.api.common.functions.MapFunction;
import org.apache.flink.api.java.tuple.Tuple2;

public class FlinkJob {
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        // Le do Kafka
        DataStream<String> stream = env
            .addSource(new FlinkKafkaConsumer<>("jarvis.public.pedidos", new SimpleStringSchema(), props));

        // Processa
        DataStream<Tuple2<String, Double>> metrics = stream
            .map((MapFunction<String, Tuple2<String, Double>>) value -> {
                JsonObject json = JsonParser.parseString(value).getAsJsonObject();
                return new Tuple2<>(json.get("usuario_id").getAsString(), json.get("total").getAsDouble());
            })
            .keyBy(value -> value.f0)
            .timeWindow(Time.minutes(5))
            .reduce((a, b) -> new Tuple2<>(a.f0, a.f1 + b.f1));

        // Escreve no sink
        metrics.addSink(new JdbcSink<>());

        env.execute("JARVIS Stream Processing");
    }
}
```

## Spark Streaming vs Flink vs Kafka Streams

| Aspecto | Spark Streaming | Apache Flink | Kafka Streams |
|---|---|---|---|
| Modelo | Micro-batch | True streaming | True streaming |
| Latencia | 100ms-1s | 1-10ms | 1-10ms |
| Throughput | Muito alto | Alto | Medio-Alto |
| State management | Checkpointing | RocksDB state backend | Kafka changelog topics |
| Windowing | Sim | Sim (avançado) | Sim |
| Exactly-once | Sim | Sim | Sim |
| Deploy | Spark cluster | Flink cluster | Embedded (app Java) |
| Linguagem | Scala/Python/Java | Java/Scala/Python | Java/Scala |
| Ideal para | Batch + streaming unificado | Streaming complexo | Apps Kafka-native |
| Curva de aprendizado | Media | Alta | Media |

### Quando Escolher

```
Spark Streaming:
  - Ja usa Spark para batch
  - Precisa de batch + streaming unificado
  - Latencia de segundos e aceitavel

Flink:
  - Latencia de milissegundos necessaria
  - Processamento de estado complexo
  - CEP (Complex Event Processing)
  - Watermarks e event time avancado

Kafka Streams:
  - Ja usa Kafka extensivamente
  - Quer deploy simples (library, nao cluster)
  - Microservicos que consomem Kafka
```

## Semantica de Processamento

### At-Most-Once

```
Producer --> Kafka --> Consumer
  |                      |
  v                      v
Envia             Processa e commit
                  ANTES de processar
```

**Resultado**: Pode perder mensagens, nunca duplica.

```python
# At-most-once: commit antes de processar
consumer = Consumer({
    "enable.auto.commit": True,
    "auto.commit.interval.ms": 1000,
})

for msg in consumer:
    processar(msg)  # Se falhar aqui, mensagem ja foi commitada
```

### At-Least-Once

```
Producer --> Kafka --> Consumer
  |                      |
  v                      v
Confirma            Processa e commit
reenvio             DEPOIS de processar
```

**Resultado**: Nunca perde mensagens, pode duplicar.

```python
# At-least-once: commit depois de processar
consumer = Consumer({
    "enable.auto.commit": False,
})

for msg in consumer:
    processar(msg)
    consumer.commit(msg)  # Commit so apos sucesso
```

### Exactly-Once

```
Producer --> Kafka --> Consumer
  |                      |
  v                      v
Idempotent          Transactional
producer            commit
```

**Resultado**: Nunca perde, nunca duplica.

```python
# Exactly-once: producer idempotente + consumer transactions
producer = Producer({
    "enable.idempotence": True,
    "acks": "all",
    "max.in.flight.requests.per.connection": 5,
})

# Flink com exactly-once
env.enable_checkpointing(5000)
env.get_checkpoint_config().set_checkpointing_mode(CheckpointingMode.EXACTLY_ONCE)
```

### Comparacao

| Semantica | Perda | Duplicacao | Performance | Use Case |
|---|---|---|---|---|
| At-most-once | Sim | Nao | Mais rapida | Logs, metricas |
| At-least-once | Nao | Sim | Media | Maioria dos casos |
| Exactly-once | Nao | Nao | Mais lenta | Financeiro, contagem |

## Schema Registry

### Confluent Schema Registry

```bash
# Registra schema
curl -X POST http://schema-registry:8081/subjects/jarvis.usuarios-value/versions \
  -H "Content-Type: application/vnd.schemaregistry.v1+json" \
  -d '{
    "schema": "{\"type\":\"record\",\"name\":\"Usuario\",\"fields\":[{\"name\":\"id\",\"type\":\"string\"},{\"name\":\"email\",\"type\":\"string\"}]}"
  }'

# Busca schema
curl http://schema-registry:8081/subjects/jarvis.usuarios-value/versions/latest

# Valida compatibilidade
curl http://schema-registry:8081/config/jarvis.usuarios-value
# Retorna: {"compatibilityLevel":"BACKWARD"}
```

### Producer com Schema Registry

```python
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka import Producer

schema_registry_client = SchemaRegistryClient({"url": "http://schema-registry:8081"})

schema_str = """
{
  "type": "record",
  "name": "Usuario",
  "fields": [
    {"name": "id", "type": "string"},
    {"name": "email", "type": "string"},
    {"name": "nome", "type": "string"}
  ]
}
"""

avro_serializer = AvroSerializer(schema_registry_client, schema_str)

producer = Producer({
    "bootstrap.servers": "kafka:9092",
    "key.serializer": StringSerializer("utf_8"),
    "value.serializer": avro_serializer,
})

producer.produce(
    topic="jarvis.public.usuarios",
    key="user-123",
    value={"id": "user-123", "email": "joao@email.com", "nome": "Joao"},
)
producer.flush()
```

## CQRS com Event Streaming

```
                    +-------------------+
   Write ---------> |  Command Side     |
   Commands         |  (Valida, Aplica) |
                    +--------+----------+
                             |
                    +--------v----------+
                    |   Event Store     |
                    |   (Kafka)         |
                    +--------+----------+
                             |
              +--------------+--------------+
              |              |              |
              v              v              v
        +----------+  +----------+  +----------+
        |  View A  |  |  View B  |  |  View C  |
        | (Query)  |  | (Query)  |  | (Query)  |
        +----------+  +----------+  +----------+
              |              |              |
              v              v              v
         Read            Read           Read
```

```python
# Command Handler
def criar_usuario_command(command: dict):
    """Valida e cria evento."""
    # Valida
    if not is_valid_email(command["email"]):
        raise ValueError("Email invalido")

    # Cria evento
    evento = {
        "type": "UsuarioCriado",
        "aggregate_id": command["id"],
        "data": {
            "id": command["id"],
            "email": command["email"],
            "nome": command["nome"],
        },
        "timestamp": datetime.now().isoformat(),
    }

    # Publica no Kafka
    publicar_evento("usuarios-events", command["id"], evento)

# View Projections
def projetar_lista_usuarios():
    """Projeta eventos para view de lista."""
    consumer = criar_consumer("usuarios-events")

    for msg in consumer:
        evento = json.loads(msg.value())

        if evento["type"] == "UsuarioCriado":
            db.execute(
                "INSERT INTO usuarios_list (id, email, nome) VALUES (%s, %s, %s)",
                (evento["data"]["id"], evento["data"]["email"], evento["data"]["nome"]),
            )
        elif evento["type"] == "EmailAlterado":
            db.execute(
                "UPDATE usuarios_list SET email = %s WHERE id = %s",
                (evento["data"]["novo_email"], evento["aggregate_id"]),
            )
```

## Real-Time Analytics Pipelines

### Pipeline de Analytics

```
Kafka (eventos) --> Flink (agregacao) --> Redis (cache) --> Dashboard
```

```python
# Flink - Real-time dashboard aggregation
t_env.execute_sql("""
    CREATE TABLE dashboard_metrics (
        metric_name STRING,
        metric_value DOUBLE,
        updated_at TIMESTAMP(3)
    ) WITH (
        'connector' = 'redis',
        'mode' = 'single',
        'host' = 'redis',
        'port' = '6379',
        'format' = 'json'
    )
""")

t_env.execute_sql("""
    INSERT INTO dashboard_metrics
    SELECT
        'pedidos_por_minuto' as metric_name,
        COUNT(*) as metric_value,
        CURRENT_TIMESTAMP as updated_at
    FROM pedidos_source
    GROUP BY TUMBLE(criado_em, INTERVAL '1' MINUTE)
""")
```

### Clickstream Analytics

```python
# Processa clickstream em tempo real
t_env.execute_sql("""
    CREATE TABLE clickstream (
        user_id STRING,
        page STRING,
        action STRING,
        timestamp TIMESTAMP(3),
        session_id STRING,
        WATERMARK FOR timestamp AS timestamp - INTERVAL '10' SECOND
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'clickstream',
        'properties.bootstrap.servers' = 'kafka:9092',
        'format' = 'json'
    )
""")

# Detecta padroes de navegacao
t_env.execute_sql("""
    INSERT INTO user_behavior
    SELECT
        user_id,
        session_id,
        COUNT(*) as page_views,
        COUNT(DISTINCT page) as unique_pages,
        MAX(timestamp) - MIN(timestamp) as session_duration
    FROM clickstream
    GROUP BY
        user_id,
        session_id,
        SESSION(timestamp, INTERVAL '30' MINUTE)
""")
```

## Monitoring e Alerting para Streaming

### Kafka Monitoring

```bash
# Kafka JMX metrics
# Monitor consumer lag
kafka-consumer-groups.sh --bootstrap-server kafka:9092 \
  --describe --group jarvis-processamento

# Output:
# GROUP                  TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG
# jarvis-processamento   pedidos         0          150000          150500          500
# jarvis-processamento   pedidos         1          149800          150200          400
```

### Flink Monitoring

```python
# Flink Metrics custom
from pyflink.metrics import MetricGroup

class CustomMetrics:
    def __init__(self, context):
        self.metrics = context.get_metric_group()
        self.processed = self.metrics.counter("processed_events")
        self.errors = self.metrics.counter("processing_errors")
        self.latency = self.metrics.histogram("processing_latency_ms")

    def record_processed(self):
        self.processed.inc()

    def record_error(self):
        self.errors.inc()

    def record_latency(self, ms: float):
        self.latency.update(ms)
```

### Prometheus + Grafana

```yaml
# docker-compose.yml - Monitoring stack
services:
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    ports:
      - "3000:3000"
    depends_on:
      - prometheus

  kafka-exporter:
    image: danielqsj/kafka-exporter
    command:
      - --kafka.server=kafka:9092
    ports:
      - "9308:9308"
```

```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "kafka"
    static_configs:
      - targets: ["kafka-exporter:9308"]

  - job_name: "flink"
    static_configs:
      - targets: ["flink-jobmanager:9249"]
```

### Alertas Essenciais

| Alerta | Condicao | Severidade | Acao |
|---|---|---|---|
| Consumer Lag | Lag > 10.000 | Critical | Scale consumers |
| Broker Down | Broker nao responde | Critical | Failover automatico |
| Disk Usage | > 85% | Warning | Expandir storage |
| Error Rate | > 1% | Critical | Investigar erros |
| Processing Latency | p99 > 1s | Warning | Otimizar job |
| Throughput Drop | < 50% do normal | Warning | Verificar fontes |

## Referencias Cruzadas

- [[etl-pipelines|ETL/ELT Pipelines]] - Pipelines batch e CDC
- [[../02-software-engineering/advanced-backend-architecture|Advanced Backend Architecture]] - Event-driven, CQRS
- [[../03-infrastructure-mcp/INDEX|Infrastructure & MCP]] - Infraestrutura para streaming
- [[../devops/Observabilidade|Observabilidade]] - Monitoring e alerting
- [[../02-software-engineering/performance|Performance]] - Otimizacao de processamento
