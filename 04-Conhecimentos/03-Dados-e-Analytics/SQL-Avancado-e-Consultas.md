---
title: "SQL Avancado e Consultas"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, sql, dados, banco-de-dados, consultas]
related: [[Banco-de-Dados-Avancado]], [[Analytics-ETL-e-Qualidade-de-Dados]], [[../02-Engenharia-de-Software/APIs-Backend-Banco]]
summary: "Guia de SQL avançado: joins, agregações, CTEs, janelas, performance, índices e leitura crítica de consultas."
---

# SQL Avançado e Consultas

SQL é a linguagem mais comum para consultar bancos relacionais. Saber SQL bem permite diagnosticar dados, criar relatórios e entender sistemas com mais profundidade.

## Conceitos fundamentais

| Conceito | Uso |
|---|---|
| SELECT | escolher colunas |
| WHERE | filtrar linhas |
| JOIN | combinar tabelas |
| GROUP BY | agrupar dados |
| HAVING | filtrar grupos |
| ORDER BY | ordenar resultado |
| LIMIT | limitar quantidade |
| CTE | criar consulta intermediária |
| window function | cálculo sobre janela de linhas |

## Joins

| Tipo | Resultado |
|---|---|
| INNER JOIN | apenas correspondências |
| LEFT JOIN | tudo da esquerda e correspondências da direita |
| RIGHT JOIN | tudo da direita e correspondências da esquerda |
| FULL JOIN | todos os registros dos dois lados |
| CROSS JOIN | combinação cartesiana |

## CTE

CTE melhora legibilidade de consultas complexas.

```sql
WITH vendas_mes AS (
  SELECT cliente_id, SUM(valor) AS total
  FROM vendas
  GROUP BY cliente_id
)
SELECT *
FROM vendas_mes
WHERE total > 1000;
```

## Window functions

Permitem calcular sem colapsar linhas.

Exemplos de uso:

- ranking;
- soma acumulada;
- média móvel;
- comparação com linha anterior;
- particionamento por grupo.

## Performance

Antes de culpar o banco:

- verificar volume;
- analisar filtros;
- revisar joins;
- olhar índices;
- evitar selecionar colunas desnecessárias;
- paginar resultados;
- usar explain plan.

## Erros comuns

- esquecer condição de join;
- usar `SELECT *` sempre;
- filtrar depois de agrupar sem necessidade;
- não entender duplicação causada por join;
- usar índice errado;
- misturar regra de negócio demais na consulta;
- não validar números finais.

## Checklist de consulta

- [ ] As tabelas certas foram usadas?
- [ ] O join pode duplicar linhas?
- [ ] O filtro está no lugar certo?
- [ ] A agregação faz sentido?
- [ ] O resultado foi conferido com amostra?
- [ ] Há índice para filtros importantes?
- [ ] A consulta é legível para manutenção?

## Resumo para IA

SQL avançado exige pensar em relações, duplicação, filtros, agregação e performance. Ao revisar consultas, verificar joins, cardinalidade, índices e validação do resultado.

## Links internos

- [[Banco-de-Dados-Avancado]]
- [[Analytics-ETL-e-Qualidade-de-Dados]]
- [[../02-Engenharia-de-Software/APIs-Backend-Banco]]
