---
title: "PostgreSQL Prático para Projetos"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, postgresql, banco-de-dados, sql, projetos]
related: [[Banco-de-Dados-Avancado]], [[SQL-Avancado-e-Consultas]], [[Analytics-ETL-e-Qualidade-de-Dados]], [[../02-Engenharia-de-Software/APIs-Backend-Banco]]
summary: "Guia prático de PostgreSQL para projetos web, com modelagem, constraints, índices, transações, migrações, backups e erros comuns."
---

# PostgreSQL Prático para Projetos

PostgreSQL é um banco relacional forte para sistemas web, APIs, dashboards, ERPs pequenos, produtos SaaS e projetos pessoais com dados importantes.

## Quando escolher PostgreSQL

Escolher quando o projeto precisa de:

- dados relacionais;
- integridade forte;
- transações;
- consultas complexas;
- relatórios;
- suporte a JSON quando necessário;
- boa compatibilidade com ORMs;
- estabilidade para produção.

## Modelagem básica

Uma tabela boa deve ter:

- chave primária;
- tipos corretos;
- campos obrigatórios bem definidos;
- constraints;
- datas de criação e atualização quando útil;
- relações explícitas;
- nomes consistentes.

## Tipos úteis

| Tipo | Uso |
|---|---|
| `uuid` | identificadores públicos difíceis de prever |
| `text` | textos variáveis |
| `varchar` | texto com limite claro |
| `integer` | números inteiros |
| `numeric` | dinheiro e precisão decimal |
| `boolean` | verdadeiro/falso |
| `timestamp` | data e hora |
| `jsonb` | estrutura flexível com consulta |

## Constraints

Constraints protegem integridade.

| Constraint | Protege contra |
|---|---|
| `NOT NULL` | dado obrigatório ausente |
| `UNIQUE` | duplicidade indevida |
| `FOREIGN KEY` | relação inválida |
| `CHECK` | valor fora da regra |
| `DEFAULT` | ausência de valor padrão |

## Índices

Índice melhora leitura, mas custa escrita e armazenamento.

Criar índice para:

- campos usados em busca frequente;
- chaves estrangeiras;
- colunas usadas em ordenação;
- filtros de relatórios;
- campos de login, como e-mail.

Evitar índice para:

- campo pouco usado;
- coluna que muda demais;
- tabela pequena sem gargalo real;
- tentativa de otimização sem medição.

## Transações

Usar transação quando várias operações precisam dar certo juntas.

Exemplos:

- criar pedido e itens do pedido;
- mover saldo entre contas;
- registrar pagamento e atualizar status;
- criar usuário e perfil.

## Migrações

Migrações precisam ser versionadas. Evitar mexer diretamente no banco sem deixar rastro.

Boas práticas:

- revisar antes de aplicar;
- não apagar dados sem backup;
- separar alteração estrutural de carga de dados;
- testar em ambiente local;
- planejar rollback quando possível.

## Backup

Projeto com dado importante precisa de backup.

Perguntas:

- onde o backup fica?
- quem acessa?
- com que frequência roda?
- já foi testada a restauração?
- backup contém dado sensível?

## Erros comuns

- usar `float` para dinheiro;
- não criar foreign key;
- guardar tudo em JSON sem motivo;
- não ter índice em campo pesquisado;
- não versionar migração;
- não testar restauração de backup;
- retornar dados demais para frontend.

## Checklist de projeto PostgreSQL

- [ ] Entidades principais estão claras?
- [ ] Relações têm foreign key?
- [ ] Campos obrigatórios usam `NOT NULL`?
- [ ] Dados únicos usam `UNIQUE`?
- [ ] Dinheiro usa `numeric`?
- [ ] Migrações estão versionadas?
- [ ] Backups foram planejados?
- [ ] Consultas críticas foram medidas?

## Resumo para IA

Ao projetar banco PostgreSQL, priorizar integridade, modelagem clara, constraints, migrações e backups. Só otimizar com índice depois de entender consulta e uso real.

## Links internos

- [[Banco-de-Dados-Avancado]]
- [[SQL-Avancado-e-Consultas]]
- [[Analytics-ETL-e-Qualidade-de-Dados]]
- [[../02-Engenharia-de-Software/APIs-Backend-Banco]]
