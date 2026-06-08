---
title: "Banco de Dados Avancado"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, dados, banco-de-dados, sql, performance]
related: [[Taxonomia-Metadados-e-Ontologia]], [[../02-Engenharia-Software/APIs-Backend-Banco]], [[../02-Engenharia-Software/Sistemas-Distribuidos-e-Escalabilidade]]
summary: "Conceitos avançados de banco de dados: índices, transações, normalização, performance, locks e consistência."
---

# Banco de Dados Avançado

Banco de dados não é só armazenamento. Ele define consistência, velocidade, integridade e capacidade de evolução do sistema.

## Conceitos essenciais

| Conceito | Função |
|---|---|
| índice | acelerar busca |
| transação | agrupar operações com segurança |
| lock | controlar acesso concorrente |
| normalização | reduzir duplicação e inconsistência |
| desnormalização | melhorar leitura com duplicação controlada |
| constraint | regra de integridade |
| migration | evolução versionada do esquema |
| query plan | plano usado pelo banco para executar consulta |

## Índices

Índices aceleram leitura, mas podem deixar escrita mais lenta.

Usar índice quando:

- coluna é usada em filtros frequentes;
- coluna participa de ordenação;
- há busca por chave estrangeira;
- consulta é lenta e recorrente.

Evitar excesso quando:

- tabela recebe muita escrita;
- coluna muda constantemente;
- índice não é usado pelo plano de consulta.

## Transações

Transações protegem operações que precisam ocorrer juntas.

Exemplo: transferir dinheiro exige debitar uma conta e creditar outra. Se uma etapa falhar, tudo deve voltar.

## Normalização vs desnormalização

| Estratégia | Ganha | Perde |
|---|---|---|
| normalização | consistência | consultas podem ficar complexas |
| desnormalização | leitura rápida | risco de duplicação errada |

## Performance

Antes de otimizar:

- medir consulta lenta;
- verificar índices;
- analisar volume de dados;
- revisar joins;
- evitar buscar colunas desnecessárias;
- paginar listas grandes;
- usar cache quando fizer sentido.

## Erros comuns

- criar campo textual para tudo;
- não usar constraints;
- apagar dados sem histórico;
- não ter backup;
- criar índice sem medir;
- fazer consulta que retorna dados demais;
- misturar regra de negócio só no banco.

## Checklist

- [ ] Tabelas têm chave primária?
- [ ] Relações têm chave estrangeira quando necessário?
- [ ] Campos críticos têm constraints?
- [ ] Consultas lentas foram medidas?
- [ ] Dados importantes têm backup?
- [ ] Migrações estão versionadas?
- [ ] Existe estratégia de auditoria?

## Relações

- [[Taxonomia-Metadados-e-Ontologia]]
- [[../02-Engenharia-Software/APIs-Backend-Banco]]
- [[../02-Engenharia-Software/Sistemas-Distribuidos-e-Escalabilidade]]
