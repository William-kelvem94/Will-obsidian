---
title: "Manual de Qualidade de Dados, DataOps e Barreiras de Erro em Business Intelligence"
tags: [checklist, qualidade, bi, incident, dataops, great-expectations, schemas, python]
updated: 2026-06-07
status: active
date: 2026-06-01
---

# 📊 Manual de Qualidade de Dados, DataOps e Barreiras de Erro em Business Intelligence

Em sistemas analíticos de alta performance, a confiabilidade decisória depende exclusivamente da integridade das bases ingressantes. Decisões gerenciais baseadas em dashboards comprometidos por anomalias silenciosas de schema, mutações intempestivas de tipagem, ou desvios de distribuição de valores (*data drift*) resultam em graves impactos financeiros e operacionais.

Este manual estabelece as práticas recomendadas de engenharia de dados de acordo com premissas de **DataOps**, integrando barreiras de erro ativas (Quality Gates) e automação de tratamento de incidentes.

---

## 🛡️ 1. Princípios de Barreiras de Qualidade (Quality Gates)

Uma governança resiliente de pipelines de dados deve at atuar de forma proativa utilizando barreiras de contenção sequenciais antes que os dados alcancem as tabelas de consumo do Data Warehouse:

```
                            PIPELINE DATAOPS QUALITY GATES:
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│  Raw Ingestion  │ ──px─►│   Schema Gate   │ ──px─►│ Statistical Gate│ ──px─►│ Curated Table   │
│  (Data Lake)    │       │ (Types & Nulls) │       │   (Outliers)    │       │ (Trusted Area)  │
└─────────────────┘       └─────────────────┘       └─────────────────┘       └─────────────────┘
```

1.  **Validação de Schema Síncrona**: Bloqueio de ingestão automatizada se houver alterações estruturais não documentadas nas colunas (ex: nova coluna injetada sem mapeamento ou exclusão de campos indispensáveis de auditoria).
2.  **Validação Estatística de Integridade**: Triagem de desvios padrão para vetores de volume físico de ingestão diária ($N$ desvios da média histórica) para bloquear alertas de anomalias (ex: base de dados com 90% a menos de faturamento do que os dias anteriores).
3.  **Higienização Lógica de Negócio**: Cruzamento referencial obrigatório (ex: todas as transações importadas devem obrigatoriamente possuir um identificador de cliente válido existente na tabela cadastral principal).

---

## 🐍 2. Código de Engenharia: Validador de Qualidade Great Expectations (Python)

Abaixo está detalhado o script de validação de qualidade desenvolvido em Python, simulando o comportamento do framework industrial **Great Expectations**. Ele intercepta um DataFrame síncrono da pipeline, valida estruturas e distribuições, e emite disparos de notificação preventiva em caso de inconformidades estruturais críticas.

```python
import pandas as pd
import numpy as np
import logging
import json
from datetime import datetime

# Setup de Log estruturado
logger = logging.getLogger("DataOps_Validation")
logging.basicConfig(level=logging.INFO)

class DataOpsQualityGate:
    """Implementa um portão de qualidade analítico robusto inspirado no Great Expectations."""
    
    def __init__(self, dataset_name: str):
        self.dataset_name = dataset_name
        self.validation_results = {
            "dataset": dataset_name,
            "timestamp": datetime.utcnow().isoformat(),
            "summary": {"total_tests": 0, "passed": 0, "failed": 0},
            "details": []
        }
        
    def _add_result(self, assertion_name: str, status: bool, meta: dict):
        self.validation_results["summary"]["total_tests"] += 1
        if status:
            self.validation_results["summary"]["passed"] += 1
        else:
            self.validation_results["summary"]["failed"] += 1
            
        self.validation_results["details"].append({
            "assertion": assertion_name,
            "success": status,
            "metadata": meta
        })

    def validate_schema(self, df: pd.DataFrame, expected_schema: dict):
        """Valida que todos os campos obrigatórios e tipos de dados coincidem com o schema de referência."""
        meta = {"expected_columns": list(expected_schema.keys())}
        failed_cols = []
        
        # 1. Checagem de Colunas Faltantes
        missing_cols = [col for col in expected_schema if col not in df.columns]
        if missing_cols:
            meta["missing_columns"] = missing_cols
            self._add_result("expect_table_columns_to_match_schema", False, meta)
            logger.error(f"❌ Falha de Schema: Colunas ausentes no dataset: {missing_cols}")
            return False
            
        # 2. Checagem de Tipificação Físico-Lógica
        for col, col_type in expected_schema.items():
            actual_type = str(df[col].dtype)
            if not np.issubdtype(df[col].dtype, col_type):
                failed_cols.append((col, f"Esperado: {col_type}, Obtido: {actual_type}"))
                
        if failed_cols:
            meta["type_failures"] = failed_cols
            self._add_result("expect_column_types_to_match", False, meta)
            logger.error(f"❌ Falha de Tipagem: Divergências de domínios em {failed_cols}")
            return False
            
        self._add_result("expect_table_columns_to_match_schema", True, meta)
        return True

    def validate_nullability(self, df: pd.DataFrame, non_nullable_columns: list):
        """Valida que campos obrigatórios de integridade referencial não contêm valores vazios/nulos."""
        meta = {"checked_columns": non_nullable_columns}
        failures = {}
        
        for col in non_nullable_columns:
            null_count = int(df[col].isnull().sum())
            if null_count > 0:
                failures[col] = f"{null_count} nulos identificados."
                
        if failures:
            meta["null_failures"] = failures
            self._add_result("expect_column_values_to_not_be_null", False, meta)
            logger.warning(f"⚠️ Alerta de Qualidade: Nulos detectados em colunas mandatórias: {failures}")
            return False
            
        self._add_result("expect_column_values_to_not_be_null", True, meta)
        return True

    def validate_numerical_bounds(self, df: pd.DataFrame, col: str, min_val: float, max_val: float):
        """Força que os limiares de valores numéricos habitem intervalos reais de distribuição lógica."""
        meta = {"column": col, "min_allowed": min_val, "max_allowed": max_val}
        
        if col not in df.columns:
            self._add_result(f"expect_column_values_to_be_between_{col}", False, {"error": "Coluna ausente"})
            return False
            
        outliers_df = df[(df[col] < min_val) | (df[col] > max_val)]
        outlier_count = len(outliers_df)
        
        if outlier_count > 0:
            meta["outlier_count"] = outlier_count
            meta["outliers_sample"] = outliers_df[col].head(3).tolist()
            self._add_result(f"expect_column_values_to_be_between_{col}", False, meta)
            logger.warning(f"⚠️ Alerta de Outliers: {outlier_count} registros fora dos limiares para a coluna `{col}`!")
            return False
            
        self._add_result(f"expect_column_values_to_be_between_{col}", True, meta)
        return True

    def get_report(self) -> dict:
        """Gera o sumário compilado do portão para ingestão final nos dashboards de telemetria."""
        return self.validation_results

# ============================================================================
# Sandbox - Execução Real da Validação Síncrona
# ============================================================================

if __name__ == "__main__":
    # 1. Simulação do DataFrame de Entrada de Transações Financeiras
    raw_data = {
        "invoice_id": [101, 102, 103, 104],
        "customer_id": ["CUST90", "CUST91", None, "CUST93"],  # Contém um nulo irregular!
        "amount": [150.50, 4200.00, -10.00, 240.00],        # Negativo irregular detected!
        "date_str": ["2026-06-01", "2026-06-01", "2026-06-02", "2026-06-02"]
    }
    df_sandbox = pd.DataFrame(raw_data)
    
    # 2. Schema de Validação Técnico-Lógico Esperado
    # Mapeando tipos estritos usando numpy dtypes
    target_schema = {
        "invoice_id": np.integer,
        "amount": np.floating,
        "date_str": np.object_
    }
    
    # Execução das validações passo a passo
    gate = DataOpsQualityGate(dataset_name="faturamento_diario_rj")
    
    gate.validate_schema(df_sandbox, target_schema)
    gate.validate_nullability(df_sandbox, ["invoice_id", "customer_id"])
    gate.validate_numerical_bounds(df_sandbox, col="amount", min_val=0.0, max_val=10000.0)
    
    # Relatório compilado gerado como asset de metadados
    final_report = gate.get_report()
    print("\n--- RELATÓRIO DO PORTÃO DE QUALIDADE DATAOPS ---")
    print(json.dumps(final_report, indent=2))
```

---

## 📋 3. Checklist Técnico de Governança de Dados

### 3.1 Definição do Pipeline (Fase de Ingestão)
- [ ] **Barreira Schema Lock**: Implementado barreira automática de validação que interrompe a execução caso colunas estruturais sejam alteradas.
- [ ] **Métricas Estatísticas Históricas**: Pipelines calculam diariamente desvio-padrão e limites de amplitude para volumes, bloqueando lotes anômalos.
- [ ] **Segurança de Truncamento**: Em faturamento/valores monetários, os tipos numéricos são restritos a formato decimal exato (*Fixed-point Decimal*), vedando perdas estocásticas de redondeza decorrentes de ponto flutuante binário (`float`).

### 3.2 Contingência e SLAs de Dados
- [ ] **Isolamento de Quarentena**: Arquivos corrompidos ou com schema violado são movidos automaticamente para uma pasta isolada (*Dead Letter Queue* - OLQ) e não contaminam a base operacional.
- [ ] **Livro de Auditoria de Incidentes**: Cada falha sistêmica de dados autogerada é registrada no ledger principal da plataforma para auditoria semanal do time de BI.

---

## 📑 4. Referências e Conexões Cruzadas
- Mapeamento e mitigação analítica de inconsistências: [dashboards/INDEX.md](01-Hubs/dashboards/INDEX.md)
- Organização e topologia de bancos relacionais robustos: [[05-Skills/alloydb-basics/SKILL]]
- Detecção e escalonamento de alarmes: [Checklist-Workflow.md](Checklist-Workflow.md)
- Governança de arquivos sensíveis e privacidade: [[04-Conhecimentos/04-Seguranca-e-Redes/Projetos/Script-audit_sensitives.py]]
