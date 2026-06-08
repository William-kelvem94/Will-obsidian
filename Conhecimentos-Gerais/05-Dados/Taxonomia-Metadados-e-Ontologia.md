---
title: "Taxonomia, Metadados e Ontologia"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, dados, taxonomia, metadados, ontologia, obsidian]
related: [[../01-IA/RAG-e-Memoria-para-Agentes]], [[../01-IA/Token-Economy]], [[../99-Templates/Template-Nota-Atomica]]
summary: "Guia para organizar dados no Obsidian de forma consistente, pesquisável e útil para humanos e IA."
---

# Taxonomia, Metadados e Ontologia

Esta nota define como organizar conhecimento para que o vault seja navegável, pesquisável e útil para IA.

## Conceitos

| Termo | Definição |
|---|---|
| taxonomia | classificação por categorias |
| metadados | dados sobre a nota |
| ontologia | relação entre conceitos |
| tag | marcador flexível |
| MOC | mapa de conteúdo |
| entidade | objeto importante do domínio |
| relação | conexão entre entidades |

## Taxonomia recomendada

### Por área

- `ia`
- `engenharia-software`
- `dados`
- `estudos`
- `produtividade`
- `saude`
- `financas`
- `trabalho`
- `relacionamentos`
- `projetos`

### Por tipo

- `guide`
- `concept`
- `moc`
- `template`
- `playbook`
- `checklist`
- `decision`
- `log`

### Por estado

- `draft`
- `active`
- `review`
- `archived`

## YAML padrão

```yaml
title: "Nome da nota"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral]
related: [[Outra nota]]
summary: "Resumo curto."
```

## Regras de nomes

Bons nomes:

- `Prompt-Engineering.md`
- `RAG-e-Memoria-para-Agentes.md`
- `Docker-e-DevOps.md`
- `Decisao-e-Priorizacao.md`

Nomes ruins:

- `coisas.md`
- `teste.md`
- `novo.md`
- `anotacoes.md`

## Relações úteis

| Relação | Uso |
|---|---|
| `related` | notas próximas |
| `depends_on` | pré-requisitos |
| `used_by` | onde o conceito é aplicado |
| `source` | origem da informação |
| `project` | projeto relacionado |

## Tags boas

Tags devem ser poucas, consistentes e úteis para busca.

Exemplo:

```yaml
tags: [conhecimento-geral, ia, rag, memoria]
```

## Tags ruins

Evitar tags emocionais, muito específicas ou únicas demais, como:

- `coisa-legal`
- `importante-demais`
- `ver-depois-talvez`

## Como criar uma ontologia simples

1. Listar entidades principais.
2. Definir relações.
3. Criar notas canônicas.
4. Criar links entre notas.
5. Criar MOC por área.
6. Revisar duplicações.

## Exemplo de entidade

Entidade: Projeto

Campos:

- nome;
- objetivo;
- status;
- stack;
- decisões;
- riscos;
- próximos passos;
- links.

## Benefícios para IA

Boa taxonomia melhora:

- recuperação por busca;
- resumo automático;
- agrupamento de notas;
- análise de lacunas;
- redução de tokens;
- consistência das respostas.

## Checklist de nota bem estruturada

- [ ] Tem YAML?
- [ ] Tem título claro?
- [ ] Tem resumo?
- [ ] Tem links internos?
- [ ] Tem tags úteis?
- [ ] Tem data de atualização?
- [ ] Tem tipo definido?
- [ ] Não duplica uma nota existente?

## Links internos

- [[../01-IA/RAG-e-Memoria-para-Agentes]]
- [[../01-IA/Token-Economy]]
- [[../99-Templates/Template-Nota-Atomica]]
- [[../README]]
