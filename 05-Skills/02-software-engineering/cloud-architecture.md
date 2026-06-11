---
tags: [cloud, aws, gcp, azure, serverless, terraform, iac, cost-optimization, multi-cloud, skills-eng]
updated: 2026-06-10
title: "Cloud Architecture"
date: 2026-06-01
---

# Arquitetura de Cloud

Padroes de arquitetura cloud multi-provedor para agentes de codificacao.

---

## Principios de Design Cloud

### Well-Architected Framework - 6 Pilares

```
    +--------------------------------------------------+
    |              Well-Architected Framework            |
    +--------------------------------------------------+
    |                                                  |
    |  +----------------+    +----------------------+   |
    |  | Excelencia     |    | Seguranca            |   |
    |  | Operacional    |    | Security             |   |
    |  +----------------+    +----------------------+   |
    |                                                  |
    |  +----------------+    +----------------------+   |
    |  | Confiabilidade  |    | Eficiencia de        |   |
    |  | Reliability    |    | Performance          |   |
    |  +----------------+    +----------------------+   |
    |                                                  |
    |  +----------------+    +----------------------+   |
    |  | Otimizacao de  |    | Sustentabilidade     |   |
    |  | Custos         |    | Sustainability       |   |
    |  +----------------+    +----------------------+   |
    |                                                  |
    +--------------------------------------------------+
```

| Pilar | Foco | Boas Praticas |
|-------|------|---------------|
| Excelencia Operacional | Runbooks, automacao | IaC, CI/CD, observabilidade |
| Seguranca | IAM, encriptacao | Least privilege, defense in depth |
| Confiabilidade | Recovery, resiliencia | Multi-AZ, backups, health checks |
| Performance | Latencia, throughput | Caching, CDN, auto-scaling |
| Otimizacao de Custos | ROI, right-sizing | Spot instances, lifecycle policies |
| Sustentabilidade | Impacto ambiental | Regioes verdes, eficiencia |

---

## Padroes de Computacao

### VMs vs Containers vs Serverless

| Aspecto | VMs | Containers | Serverless |
|---------|-----|------------|------------|
| Isolamento | OS completo | Namespace/cgroups | Provider gerencia |
| Startup | Minutos | Segundos | Milissegundos |
| Scaling | Lento | Medio | Instantaneo |
| Custo | Alto (OS overhead) | Medio | Pay-per-use |
| Exemplos | EC2, GCE, VMs | EKS, GKE, AKS | Lambda, Cloud Functions |
| Ideal para | Legacy, compliance | Microservicos | Event-driven, APIs |

### Auto-scaling Strategies

```
TARGET TRACKING:
  Metrica alvo: CPU = 70%

  CPU%
  100 |     /\
   80 |    /  \    /\
   70 |---/----\--/--\---- Target
   60 |  /      \/    \
   40 | /              \
      +------------------- Time
         ^ Scale up    ^ Scale down

STEP SCALING:
  CPU > 80%  -> +2 instancias
  CPU > 60%  -> +1 instancia
  CPU < 40%  -> -1 instancia
  CPU < 20%  -> -2 instancias

SCHEDULED:
  09:00 -> Scale up (5 instancias)
  18:00 -> Scale down (2 instancias)
```

### Auto Scaling Group (AWS)

```python
# Terraform - AWS Auto Scaling Group
resource "aws_launch_template" "web" {
  name_prefix   = "web-"
  image_id      = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"

  user_data = base64encode(<<-EOF
    #!/bin/bash
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    echo "Hello from $(hostname)" > /var/www/html/index.html
  EOF
  )

  tag_specifications {
    resource_type = "instance"
    tags = {
      Name = "web-server"
    }
  }
}

resource "aws_autoscaling_group" "web" {
  name                = "web-asg"
  desired_capacity    = 2
  max_size            = 10
  min_size            = 1
  vpc_zone_identifier = aws_subnet.public[*].id

  launch_template {
    id      = aws_launch_template.web.id
    version = "$Latest"
  }

  target_group_arns = [aws_lb_target_group.web.arn]

  tag {
    key                 = "Name"
    value               = "web-server"
    propagate_at_launch = true
  }
}

resource "aws_autoscaling_policy" "web_cpu" {
  name                   = "web-cpu-policy"
  autoscaling_group_name = aws_autoscaling_group.web.name
  policy_type            = "TargetTrackingScaling"

  target_tracking_configuration {
    predefined_metric_specification {
      predefined_metric_type = "ASGAverageCPUUtilization"
    }
    target_value = 70.0
  }
}
```

### Managed Instance Group (GCP)

```hcl
# Terraform - GCP Managed Instance Group
resource "google_compute_instance_template" "web" {
  name_prefix = "web-"

  machine_type = "e2-micro"

  disk {
    source_image = "debian-cloud/debian-12"
    auto_delete  = true
    boot         = true
  }

  network_interface {
    network = google_compute_network.main.name
  }

  metadata_startup_script = <<-EOF
    #!/bin/bash
    apt-get update
    apt-get install -y nginx
    systemctl start nginx
  EOF
}

resource "google_compute_instance_group_manager" "web" {
  name               = "web-mig"
  base_instance_name = "web"
  zone               = "us-central1-a"
  target_size        = 3

  version {
    instance_template = google_compute_instance_template.web.id
  }

  auto_healing_policies {
    health_check      = google_compute_health_check.web.id
    initial_delay_sec = 300
  }
}

resource "google_compute_autoscaler" "web" {
  name   = "web-autoscaler"
  zone   = "us-central1-a"
  target = google_compute_instance_group_manager.web.id

  autoscaling_policy {
    max_replicas    = 10
    min_replicas    = 2
    cooldown_period = 60

    cpu_utilization {
      target = 0.7
    }
  }
}
```

### Spot/Preemptible Instances

```python
# Python - Fallback para on-demand se spot indisponivel
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

def launch_with_spot_fallback(instance_config):
    # Tenta spot primeiro
    try:
        response = ec2.request_spot_instances(
            SpotPrice=instance_config['spot_price'],
            InstanceCount=1,
            Type='one-time',
            LaunchSpecification={
                'ImageId': instance_config['ami'],
                'InstanceType': instance_config['type'],
            }
        )
        return response
    except ClientError:
        # Fallback para on-demand
        return ec2.run_instances(
            ImageId=instance_config['ami'],
            InstanceType=instance_config['type'],
            MinCount=1,
            MaxCount=1,
        )
```

```typescript
// TypeScript - GCP Preemptible com retry
import { InstancesClient } from '@google-cloud/compute'

async function launchPreemptibleWithFallback(config: any) {
  const client = new InstancesClient()

  try {
    // Tenta preemptible (70% mais barato)
    const [operation] = await client.insert({
      project: config.project,
      zone: config.zone,
      instanceResource: {
        name: `web-${Date.now()}`,
        machineType: `zones/${config.zone}/machineTypes/e2-micro`,
        scheduling: { preemptible: true },
        disks: [{ /* ... */ }],
        networkInterfaces: [{ /* ... */ }],
      },
    })
    return operation
  } catch (error) {
    // Fallback para standard
    console.log('Preemptible indisponivel, usando standard')
    // ... lancamento standard
  }
}
```

---

## Padroes de Storage

### Quando Usar Cada Tipo

| Tipo | Exemplos | Caso de Uso | Custo | Performance |
|------|----------|-------------|-------|-------------|
| Object | S3, GCS | Assets, backups, logs | Baixo | Medio |
| Block | EBS, PD | DBs, boot volumes | Medio | Alto |
| File | EFS, Filestore | Shared filesystem | Alto | Medio |

### S3 Lifecycle Policies

```hcl
# Terraform - S3 com lifecycle
resource "aws_s3_bucket" "data" {
  bucket = "my-app-data"
}

resource "aws_s3_bucket_lifecycle_configuration" "data" {
  bucket = aws_s3_bucket.data.id

  rule {
    id     = "transition-to-ia"
    status = "Enabled"

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }

    transition {
      days          = 90
      storage_class = "GLACIER"
    }

    expiration {
      days = 365
    }

    filter {
      prefix = "logs/"
    }
  }

  rule {
    id     = "abort-incomplete-uploads"
    status = "Enabled"

    abort_incomplete_multipart_upload {
      days_after_initiation = 7
    }
  }
}
```

---

## Padroes de Banco de Dados

### Managed Databases Comparison

| Feature | RDS (AWS) | Cloud SQL (GCP) | Azure SQL |
|---------|-----------|-----------------|-----------|
| Engines | MySQL, PG, Oracle, SQL Server | MySQL, PG, SQL Server | SQL Server, MySQL, PG |
| Multi-AZ | Sim | Sim (regional) | Sim |
| Read Replicas | Sim (5 max) | Sim (10 max) | Sim |
| Auto-scaling storage | Sim | Sim | Sim |
| Backup automatico | Sim | Sim | Sim |
| Point-in-time recovery | Sim | Sim | Sim |

### DynamoDB/NoSQL Patterns

```python
# Python - DynamoDB com boto3
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

# Put item
table.put_item(Item={
    'user_id': 'user-123',
    'email': 'joao@test.com',
    'name': 'Joao Silva',
    'created_at': '2026-05-16',
})

# Query por partition key
response = table.query(
    KeyConditionExpression=Key('user_id').eq('user-123')
)

# GSI Query
response = table.query(
    IndexName='email-index',
    KeyConditionExpression=Key('email').eq('joao@test.com')
)

# Update com conditional
table.update_item(
    Key={'user_id': 'user-123'},
    UpdateExpression='SET #n = :name, version = :version',
    ExpressionAttributeNames={'#n': 'name'},
    ExpressionAttributeValues={
        ':name': 'Joao Pereira',
        ':version': 2,
    },
    ConditionExpression='version = :current_version',
    ExpressionAttributeValues={
        ':current_version': 1,
    },
)
```

```typescript
// TypeScript - Firestore
import { Firestore } from '@google-cloud/firestore'

const db = new Firestore()

async function createUser(userId: string, data: any) {
  const userRef = db.collection('users').doc(userId)

  await userRef.set({
    ...data,
    createdAt: Firestore.timestamp(),
    updatedAt: Firestore.timestamp(),
  })

  return userRef
}

async function getUserByEmail(email: string) {
  const snapshot = await db.collection('users')
    .where('email', '==', email)
    .limit(1)
    .get()

  if (snapshot.empty) return null
  return snapshot.docs[0].data()
}

// Transaction
async function transferFunds(fromId: string, toId: string, amount: number) {
  return db.runTransaction(async (transaction) => {
    const fromRef = db.collection('accounts').doc(fromId)
    const toRef = db.collection('accounts').doc(toId)

    const fromDoc = await transaction.get(fromRef)
    const toDoc = await transaction.get(toRef)

    const fromBalance = fromDoc.data().balance
    if (fromBalance < amount) throw new Error('Saldo insuficiente')

    transaction.update(fromRef, { balance: fromBalance - amount })
    transaction.update(toRef, { balance: toDoc.data().balance + amount })
  })
}
```

---

## Networking

### VPC Design

```
    VPC: 10.0.0.0/16
    +--------------------------------------------------+
    |                                                  |
    |  Public Subnet        Private Subnet             |
    |  10.0.0.0/24          10.0.1.0/24                |
    |  +-----------+        +-----------+              |
    |  | ALB/NLB   |        | App Server|              |
    |  | (IGW)     |        | (NAT GW)  |              |
    |  +-----------+        +-----------+              |
    |                                                  |
    |  Private Subnet       Data Subnet                |
    |  10.0.2.0/24          10.0.3.0/24                |
    |  +-----------+        +-----------+              |
    |  | Worker    |        | Database  |              |
    |  | (NAT GW)  |        | (No IGW)  |              |
    |  +-----------+        +-----------+              |
    |                                                  |
    +--------------------------------------------------+
              |                    |
         Internet Gateway     NAT Gateway
```

### VPC Peering

```
    VPC A (10.0.0.0/16)          VPC B (10.1.0.0/16)
    +---------------+            +---------------+
    | Subnet A1     |            | Subnet B1     |
    | 10.0.1.0/24   |<---------->| 10.1.1.0/24   |
    |               |  Peering   |               |
    | Subnet A2     | Connection | Subnet B2     |
    | 10.0.2.0/24   |            | 10.1.2.0/24   |
    +---------------+            +---------------+

    # Regras de roteamento:
    # VPC A: 10.1.0.0/16 -> pcx-xxxxx
    # VPC B: 10.0.0.0/16 -> pcx-xxxxx
```

---

## Serverless Architecture

### Event-Driven Patterns

```
    +--------+     +-------------+     +--------+
    | API GW | --> |   Lambda    | --> | DynamoDB|
    +--------+     +-------------+     +--------+
                        |
                        v
                   +---------+
                   |   SNS   |
                   +----+----+
                        |
              +---------+---------+
              |                   |
              v                   v
         +--------+          +--------+
         | Lambda |          | Lambda |
         | Email  |          | Analytics|
         +--------+          +--------+
```

### Cold Start Mitigation

```python
# Python - Lambda com cold start optimization
import json

# Import pesado fora do handler (executado durante init)
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

# Connection pooling
db_pool = None

def get_db():
    global db_pool
    if db_pool is None:
        db_pool = create_connection_pool()
    return db_pool

def handler(event, context):
    # Logico leve dentro do handler
    user_id = event['pathParameters']['id']
    response = table.get_item(Key={'user_id': user_id})
    return {
        'statusCode': 200,
        'body': json.dumps(response.get('Item', {})),
    }

# Provisioned Concurrency (config via Terraform)
# resource "aws_lambda_provisioned_concurrency_config" "api" {
#   function_name                     = aws_lambda_function.api.function_name
#   provisioned_concurrent_executions = 10
#   qualifier                         = aws_lambda_alias.api.name
# }
```

```typescript
// TypeScript - Cloud Functions com warm start
import { onRequest } from 'firebase-functions/v2/https'

// Inicializacao fora do handler (reutilizada entre invocations)
const db = initializeDatabase()
const cache = new Map<string, any>()

export const apiHandler = onRequest(async (req, res) => {
  const userId = req.query.id as string

  // Check cache primeiro
  if (cache.has(userId)) {
    return res.json(cache.get(userId))
  }

  const user = await db.collection('users').doc(userId).get()
  const data = user.data()

  // Cache por 5 minutos
  cache.set(userId, data)
  setTimeout(() => cache.delete(userId), 5 * 60 * 1000)

  res.json(data)
})
```

### Serverless CRUD API Completo

```hcl
# Terraform - Serverless API com API Gateway + Lambda + DynamoDB
resource "aws_dynamodb_table" "users" {
  name         = "users"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "user_id"

  attribute {
    name = "user_id"
    type = "S"
  }
}

resource "aws_iam_role" "lambda" {
  name = "lambda-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy" "lambda_dynamo" {
  name = "lambda-dynamo-policy"
  role = aws_iam_role.lambda.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "dynamodb:GetItem",
        "dynamodb:PutItem",
        "dynamodb:UpdateItem",
        "dynamodb:DeleteItem",
        "dynamodb:Query",
      ]
      Resource = aws_dynamodb_table.users.arn
    }]
  })
}

resource "aws_lambda_function" "api" {
  filename         = "lambda.zip"
  function_name    = "users-api"
  role             = aws_iam_role.lambda.arn
  handler          = "handler.main"
  runtime          = "python3.11"
  timeout          = 30
  memory_size      = 256

  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.users.name
    }
  }
}

resource "aws_apigatewayv2_api" "api" {
  name          = "users-api"
  protocol_type = "HTTP"
}

resource "aws_apigatewayv2_route" "routes" {
  for_each = {
    "GET /users/{id}"    = "GET"
    "POST /users"        = "POST"
    "PUT /users/{id}"    = "PUT"
    "DELETE /users/{id}" = "DELETE"
  }

  api_id      = aws_apigatewayv2_api.api.id
  route_key   = "${each.value} ${each.key}"
  target      = "integrations/${aws_apigatewayv2_integration.lambda.id}"
}

resource "aws_apigatewayv2_integration" "lambda" {
  api_id                 = aws_apigatewayv2_api.api.id
  integration_type       = "AWS_PROXY"
  integration_uri        = aws_lambda_function.api.invoke_arn
  integration_method     = "POST"
  payload_format_version = "2.0"
}

resource "aws_lambda_permission" "api" {
  statement_id  = "AllowAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.api.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.api.execution_arn}/*/*"
}
```

---

## Container Orchestration

### EKS vs GKE vs AKS

| Feature | EKS (AWS) | GKE (GCP) | AKS (Azure) |
|---------|-----------|-----------|-------------|
| Control plane | Gerenciado ($0.10/h) | Gerenciado (gratis) | Gerenciado (gratis) |
| Auto-scaling | Karpenter/CA | Cluster Autoscaler | Cluster Autoscaler |
| Service mesh | App Mesh | Anthos Service Mesh | Service Mesh |
| Serverless | Fargate | Autopilot | ACI |
| Multi-cluster | EKS Anywhere | Fleet Manager | Arc |

### Helm Chart Multi-ambiente

```yaml
# values.yaml (default)
replicaCount: 2
image:
  repository: myapp/api
  tag: latest
resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 256Mi

---
# values-dev.yaml
replicaCount: 1
resources:
  requests:
    cpu: 50m
    memory: 64Mi

---
# values-prod.yaml
replicaCount: 3
image:
  tag: 1.0.0
resources:
  requests:
    cpu: 200m
    memory: 256Mi
  limits:
    cpu: 1000m
    memory: 512Mi
autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 10
```

```hcl
# Deploy com Helm
resource "helm_release" "api" {
  name       = "api"
  repository = "https://charts.myorg.com"
  chart      = "api"
  version    = "1.0.0"
  namespace  = "production"

  values = [
    file("${path.module}/values-prod.yaml")
  ]

  set {
    name  = "image.tag"
    value = var.api_version
  }
}
```

### Multi-service Deployment

```yaml
# docker-compose para desenvolvimento
version: '3.8'
services:
  api:
    build: ./api
    ports:
      - "8080:8080"
    environment:
      - DATABASE_URL=postgresql://postgres:pass@db:5432/app
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis

  worker:
    build: ./worker
    environment:
      - DATABASE_URL=postgresql://postgres:pass@db:5432/app
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis

  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: pass
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - api

volumes:
  pgdata:
```

---

## Infrastructure as Code

### Terraform Best Practices

```
projeto/
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── terraform.tfvars
│   ├── staging/
│   └── production/
├── modules/
│   ├── vpc/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── ecs/
│   └── rds/
└── backend.tf (state configuration)
```

### Modulo Terraform Completo

```hcl
# modules/webapp/main.tf
variable "environment" {
  type = string
}

variable "vpc_id" {
  type = string
}

variable "subnet_ids" {
  type = list(string)
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}

variable "min_size" {
  type    = number
  default = 1
}

variable "max_size" {
  type    = number
  default = 5
}

locals {
  name_prefix = "${var.environment}-webapp"
}

# Security Group
resource "aws_security_group" "web" {
  name_prefix = "${local.name_prefix}-sg"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

# Launch Template
resource "aws_launch_template" "web" {
  name_prefix   = "${local.name_prefix}-lt"
  image_id      = data.aws_ami.amazon_linux.id
  instance_type = var.instance_type

  vpc_security_group_ids = [aws_security_group.web.id]

  user_data = base64encode(<<-EOF
    #!/bin/bash
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    echo "Hello from ${var.environment}" > /var/www/html/index.html
  EOF
  )

  tag_specifications {
    resource_type = "instance"
    tags = {
      Name        = "${local.name_prefix}-instance"
      Environment = var.environment
    }
  }
}

# Auto Scaling Group
resource "aws_autoscaling_group" "web" {
  name                = "${local.name_prefix}-asg"
  desired_capacity    = var.min_size
  max_size            = var.max_size
  min_size            = var.min_size
  vpc_zone_identifier = var.subnet_ids

  launch_template {
    id      = aws_launch_template.web.id
    version = "$Latest"
  }

  tag {
    key                 = "Name"
    value               = "${local.name_prefix}-instance"
    propagate_at_launch = true
  }

  tag {
    key                 = "Environment"
    value               = var.environment
    propagate_at_launch = true
  }
}

# Outputs
output "asg_name" {
  value = aws_autoscaling_group.web.name
}

output "security_group_id" {
  value = aws_security_group.web.id
}
```

### Pulumi (TypeScript)

```typescript
// index.ts - Pulumi com TypeScript
import * as pulumi from '@pulumi/pulumi'
import * as aws from '@pulumi/aws'

const config = new pulumi.Config()
const environment = config.get('environment') || 'dev'

// VPC
const vpc = new aws.ec2.Vpc(`${environment}-vpc`, {
  cidrBlock: '10.0.0.0/16',
  enableDnsHostnames: true,
  enableDnsSupport: true,
  tags: { Environment: environment },
})

// Subnet
const subnet = new aws.ec2.Subnet(`${environment}-subnet`, {
  vpcId: vpc.id,
  cidrBlock: '10.0.1.0/24',
  availabilityZone: 'us-east-1a',
  mapPublicIpOnLaunch: true,
})

// Security Group
const sg = new aws.ec2.SecurityGroup(`${environment}-sg`, {
  vpcId: vpc.id,
  ingress: [{ protocol: 'tcp', fromPort: 80, toPort: 80, cidrBlocks: ['0.0.0.0/0'] }],
  egress: [{ protocol: '-1', fromPort: 0, toPort: 0, cidrBlocks: ['0.0.0.0/0'] }],
})

// EC2 Instance
const instance = new aws.ec2.Instance(`${environment}-web`, {
  instanceType: 't3.micro',
  ami: 'ami-0c55b159cbfafe1f0',
  subnetId: subnet.id,
  vpcSecurityGroupIds: [sg.id],
  tags: { Name: `${environment}-web`, Environment: environment },
})

export const publicIp = instance.publicIp
```

### Pulumi (Python)

```python
# __main__.py - Pulumi com Python
import pulumi
import pulumi_aws as aws

config = pulumi.Config()
environment = config.get('environment') or 'dev'

# S3 Bucket
bucket = aws.s3.Bucket(
    f"{environment}-data",
    tags={"Environment": environment},
)

# Lambda Function
role = aws.iam.Role(
    f"{environment}-lambda-role",
    assume_role_policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{"Action": "sts:AssumeRole", "Effect": "Allow",
                       "Principal": {"Service": "lambda.amazonaws.com"}}],
    }),
)

function = aws.lambda_.Function(
    f"{environment}-api",
    runtime=aws.lambda_.Runtime.PYTHON3_11,
    handler="handler.main",
    role=role.arn,
    code=pulumi.FileArchive("./lambda.zip"),
    environment={
        "variables": {"BUCKET_NAME": bucket.bucket},
    },
)

pulumi.export('bucket_name', bucket.bucket)
pulumi.export('function_arn', function.arn)
```

### AWS CDK (TypeScript)

```typescript
// lib/api-stack.ts
import * as cdk from 'aws-cdk-lib'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as apigateway from 'aws-cdk-lib/aws-apigateway'
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb'
import { Construct } from 'constructs'

export class ApiStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    // DynamoDB Table
    const table = new dynamodb.Table(this, 'UsersTable', {
      partitionKey: { name: 'user_id', type: dynamodb.AttributeType.STRING },
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    })

    // Lambda Function
    const handler = new lambda.Function(this, 'ApiHandler', {
      runtime: lambda.Runtime.PYTHON_3_11,
      handler: 'handler.main',
      code: lambda.Code.fromAsset('lambda'),
      environment: { TABLE_NAME: table.tableName },
      timeout: cdk.Duration.seconds(30),
    })

    table.grantReadWriteData(handler)

    // API Gateway
    new apigateway.LambdaRestApi(this, 'Api', {
      handler,
      defaultCorsPreflightOptions: {
        allowOrigins: apigateway.Cors.ALL_ORIGINS,
        allowMethods: apigateway.Cors.ALL_METHODS,
      },
    })
  }
}
```

---

## Otimizacao de Custos

### Comparacao de Pricing

| Tipo | Desconto | Compromisso | Ideal para |
|------|----------|-------------|------------|
| On-Demand | 0% | Nenhum | Carga imprevisivel |
| Reserved (1 ano) | ~40% | 1 ano | Carga estavel |
| Reserved (3 anos) | ~60% | 3 anos | Carga muito estavel |
| Spot/Preemptible | ~70-90% | Nenhum | Workloads tolerantes a falha |
| Savings Plans | ~30-50% | 1-3 anos | Compromisso de $/hora |

### Cost Allocation Tags

```hcl
# Terraform - Tags de custo
locals {
  common_tags = {
    Project     = "myapp"
    Environment = var.environment
    Team        = "backend"
    CostCenter  = "engineering"
    ManagedBy   = "terraform"
  }
}

resource "aws_instance" "web" {
  # ...
  tags = merge(local.common_tags, {
    Name = "web-server"
    Role = "frontend"
  })
}
```

### Budget Alerts

```hcl
resource "aws_budgets_budget" "monthly" {
  name              = "monthly-budget"
  budget_type       = "COST"
  limit_amount      = "1000"
  limit_unit        = "USD"
  time_unit         = "MONTHLY"

  notification {
    comparison_operator        = "GREATER_THAN"
    threshold                  = 80
    threshold_type             = "PERCENTAGE"
    notification_type          = "FORECASTED"
    subscriber_email_addresses = ["team@company.com"]
  }

  notification {
    comparison_operator        = "GREATER_THAN"
    threshold                  = 100
    threshold_type             = "PERCENTAGE"
    notification_type          = "ACTUAL"
    subscriber_email_addresses = ["team@company.com", "finops@company.com"]
  }
}
```

---

## Multi-Cloud e Hybrid

### Quando Usar Multi-Cloud

| Cenario | Recomendacao |
|---------|-------------|
| Evitar vendor lock-in | Multi-cloud estrategico |
| Compliance/regulacao | Multi-cloud por regiao |
| Alta disponibilidade | Active-active multi-cloud |
| Custo | Multi-cloud para spot pricing |
| Simplicidade | Single cloud recomendado |

### Data Sync Across Clouds

```python
# Python - S3 para GCS sync
import boto3
from google.cloud import storage

def sync_s3_to_gcs(source_bucket: str, dest_bucket: str, prefix: str = ''):
    s3 = boto3.client('s3')
    gcs = storage.Client()
    dest = gcs.bucket(dest_bucket)

    # Lista objetos S3
    paginator = s3.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=source_bucket, Prefix=prefix):
        for obj in page.get('Contents', []):
            key = obj['Key']

            # Download do S3
            s3_obj = s3.get_object(Bucket=source_bucket, Key=key)
            data = s3_obj['Body'].read()

            # Upload para GCS
            blob = dest.blob(key)
            blob.upload_from_string(data)
            print(f"Synced: {key}")
```

### Plataformas Multi-Cloud

| Plataforma | Provedor | Descricao |
|-----------|----------|-----------|
| Anthos | Google | Kubernetes multi-cloud/on-prem |
| Arc | Azure | Gestao de recursos multi-cloud |
| EKS Anywhere | AWS | Kubernetes on-prem com tooling AWS |
| Crossplane | Open Source | Control plane multi-cloud |

---

## Referencias Cruzadas

- [[devops/Kubernetes]] - Orquestracao de containers
- [[devops/FinOps]] - Gestao de custos cloud
- [[devops/ci-cd/INDEX]] - Automatizacao CI/CD
- [[03-infrastructure-mcp/local-llm-ops]] - Operacoes de LLM local
