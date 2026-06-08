---
title: "RAG e Memória para Agentes"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, ia, rag, agentes, memoria, embeddings]
related: [[Prompt-Engineering]], [[Token-Economy]], [[../05-Dados/Taxonomia-Metadados-e-Ontologia]]
summary: "Guia prático sobre RAG, memória de agentes, embeddings, chunking e uso do Obsidian como base de conhecimento consultável por IA."
---

# RAG e Memória para Agentes

RAG significa **Retrieval-Augmented Generation**. A ideia é simples: antes de responder, a IA busca informações relevantes em uma base externa e usa esses trechos como contexto.

## Por que usar RAG

Modelos de linguagem têm limites:

- não conhecem todos os dados privados;
- esquecem contexto entre sessões;
- podem inventar detalhes;
- custam mais quando recebem contexto demais;
- perdem precisão quando a conversa fica grande.

RAG resolve parte disso usando uma base organizada, como este vault.

## Pipeline básico

1. Coletar documentos.
2. Limpar e normalizar texto.
3. Dividir em chunks.
4. Gerar embeddings.
5. Salvar em banco vetorial.
6. Receber pergunta.
7. Buscar chunks relevantes.
8. Montar contexto curto.
9. Gerar resposta.
10. Registrar aprendizado novo.

## Tipos de memória

| Tipo | O que guarda | Exemplo |
|---|---|---|
| memória semântica | fatos e conceitos | "Docker isola ambientes" |
| memória episódica | eventos e histórico | "em 2026-06-07 foi criada a pasta Conhecimentos-Gerais" |
| memória procedural | como fazer algo | checklist de deploy |
| memória de preferência | estilo e escolhas | preferência por Docker no Windows |
| memória operacional | estado atual | projeto ativo, pendências, foco |

## Obsidian como memória

O Obsidian é bom para RAG porque usa Markdown local, links internos e pastas legíveis. Cada nota pode virar documento, e cada seção pode virar chunk.

## Chunking

### Estratégia por cabeçalho

- `#` define o documento.
- `##` define blocos principais.
- `###` define sub-blocos.

### Estratégia por tamanho

- conceitos: 300 a 900 palavras;
- comandos: blocos pequenos;
- listas e checklists: preservar unidade;
- tabelas: não dividir.

### Estratégia por significado

Nunca separar definição de exemplo. Nunca separar problema de solução. Nunca separar decisão de justificativa.

## Metadados importantes

```yaml
title: "Nome"
type: guide
status: active
tags: [ia, rag]
summary: "Resumo curto"
related: [[Outra nota]]
```

Metadados ajudam filtros, busca, dashboards e agentes.

## Riscos

| Risco | Descrição | Mitigação |
|---|---|---|
| contexto errado | busca retorna nota irrelevante | melhorar tags e títulos |
| duplicação | vários arquivos dizem a mesma coisa | usar MOCs e links |
| nota muito grande | chunk confuso | dividir por conceito |
| nota sem resumo | IA precisa ler demais | preencher `summary` |
| dados sensíveis | vazamento em IA externa | separar privado e público |

## Padrão de resposta RAG

Uma IA usando RAG deve responder com:

1. resposta direta;
2. evidências usadas;
3. nível de confiança;
4. lacunas;
5. próximos passos.

## Memória boa para agente

Uma memória boa é:

- curta o suficiente para ser recuperada;
- específica o suficiente para ser útil;
- datada quando envolve evento;
- linkada quando envolve conceito;
- separada por tipo.

## Memória ruim para agente

- frases soltas sem contexto;
- logs automáticos sem limpeza;
- pensamentos duplicados;
- arquivos enormes sem cabeçalhos;
- notas sem tags;
- registros emocionais misturados com decisões técnicas.

## Relação com o vault

- `JARVIS/` guarda identidade, estado, decisões e memórias do agente.
- `Conhecimentos-Gerais/` guarda conhecimento estável e reutilizável.
- `Projetos/` guarda execução e entregas.
- `skills/` guarda habilidades técnicas estruturadas.

## Links internos

- [[Prompt-Engineering]]
- [[Token-Economy]]
- [[../05-Dados/Taxonomia-Metadados-e-Ontologia]]
- [[../../skills/04-knowledge-systems/obsidian-neural-vault]]
