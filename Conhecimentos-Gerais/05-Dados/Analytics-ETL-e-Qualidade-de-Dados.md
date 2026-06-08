---
title: "Analytics, ETL e Qualidade de Dados"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, analytics, etl, dados, qualidade-de-dados]
related: [[SQL-Avancado-e-Consultas]], [[Banco-de-Dados-Avancado]], [[Taxonomia-Metadados-e-Ontologia]]
summary: "Guia sobre analytics, pipelines ETL/ELT, qualidade de dados, métricas, rastreabilidade e governança prática."
---

# Analytics, ETL e Qualidade de Dados

Analytics transforma dados em entendimento. ETL e ELT são processos para mover, limpar e preparar dados para análise ou uso operacional.

## ETL vs ELT

| Processo | Ordem | Uso comum |
|---|---|---|
| ETL | extrair, transformar, carregar | pipelines controlados antes do destino |
| ELT | extrair, carregar, transformar | data warehouses modernos |

## Pipeline de dados

1. Coleta.
2. Validação.
3. Limpeza.
4. Transformação.
5. Armazenamento.
6. Consulta.
7. Visualização.
8. Monitoramento.

## Qualidade de dados

| Dimensão | Pergunta |
|---|---|
| completude | faltam valores? |
| consistência | dados concordam entre fontes? |
| validade | formato está correto? |
| unicidade | existem duplicados? |
| atualidade | dado está recente? |
| precisão | dado representa a realidade? |
| rastreabilidade | sabemos a origem? |

## Métricas

Métrica boa tem definição clara.

Exemplo:

- nome;
- fórmula;
- fonte;
- período;
- responsável;
- limitações;
- frequência de atualização.

## Problemas comuns

- campo com significado ambíguo;
- métrica calculada de formas diferentes;
- origem desconhecida;
- atualização manual sem registro;
- duplicação de registros;
- ausência de dicionário de dados;
- dashboard bonito com dado fraco.

## Dicionário de dados

Um dicionário de dados deve conter:

- nome do campo;
- tipo;
- descrição;
- origem;
- regra de preenchimento;
- exemplo;
- observações.

## Checklist

- [ ] A métrica tem fórmula definida?
- [ ] A origem do dado é conhecida?
- [ ] Existem duplicados?
- [ ] Dados ausentes foram tratados?
- [ ] A atualização é automática ou manual?
- [ ] Há responsável pela métrica?
- [ ] O dashboard mostra limitações?

## Resumo para IA

Analytics confiável depende de definição, origem, qualidade e rastreabilidade. Antes de interpretar métrica, verificar fórmula, fonte, atualização e limitações.

## Links internos

- [[SQL-Avancado-e-Consultas]]
- [[Banco-de-Dados-Avancado]]
- [[Taxonomia-Metadados-e-Ontologia]]
