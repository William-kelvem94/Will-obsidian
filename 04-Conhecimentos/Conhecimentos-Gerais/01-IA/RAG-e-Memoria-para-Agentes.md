---
title: "RAG e Memória para Agentes"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, ia, rag, agentes, memoria, embeddings]
related: [[Modelos-de-Linguagem-LLMs]], [[Embeddings-e-Busca-Semantica]], [[Context-Engineering]], [[Avaliacao-de-RAG-e-Qualidade-de-Contexto]], [[Token-Economy]], [[../00-Ontologia-de-Conhecimento-para-IA]]
summary: "Guia aprofundado sobre RAG, memória de agentes, embeddings, chunking, recuperação, contexto e uso do Obsidian como base consultável por IA."
---

# RAG e Memória para Agentes

RAG significa **Retrieval-Augmented Generation**. A ideia é complementar um modelo de linguagem com busca em fontes externas antes da resposta.

## Ideia central

Um LLM sozinho responde com base no treinamento e no contexto da conversa. Um sistema RAG busca documentos relevantes, monta um contexto menor e orienta o modelo a responder com base neles.

## Por que usar RAG

Modelos de linguagem têm limites:

- não conhecem todos os dados privados;
- esquecem contexto entre sessões;
- podem inventar detalhes quando falta fonte;
- custam mais quando recebem contexto demais;
- perdem precisão quando a conversa fica grande;
- não sabem automaticamente o que mudou no vault.

RAG resolve parte disso usando uma base organizada, como este vault.

## Pipeline básico

1. Coletar documentos.
2. Limpar e normalizar texto.
3. Dividir em chunks.
4. Gerar embeddings.
5. Salvar em banco vetorial.
6. Receber pergunta.
7. Gerar embedding da pergunta.
8. Buscar chunks relevantes.
9. Reordenar resultados quando necessário.
10. Montar contexto curto.
11. Gerar resposta.
12. Validar resposta.
13. Registrar aprendizado novo.

## Componentes de um sistema RAG

| Componente | Função |
|---|---|
| loader | lê arquivos e fontes |
| parser | extrai texto e metadados |
| chunker | divide documentos |
| embedder | transforma texto em vetor |
| vector store | guarda vetores |
| retriever | busca candidatos |
| reranker | melhora ordem dos resultados |
| context builder | monta contexto final |
| generator | gera resposta |
| evaluator | avalia qualidade |

## Tipos de memória

| Tipo | O que guarda | Exemplo |
|---|---|---|
| memória semântica | fatos e conceitos | "Docker isola ambientes" |
| memória episódica | eventos e histórico | "em 2026-06-07 foi criada a pasta Conhecimentos-Gerais" |
| memória procedural | como fazer algo | checklist de deploy |
| memória de preferência | estilo e escolhas | preferência por Docker no Windows |
| memória operacional | estado atual | projeto ativo, pendências, foco |
| memória normativa | regras e limites | não versionar secrets |
| memória avaliativa | critérios de qualidade | resposta precisa citar lacunas |

## Obsidian como memória

O Obsidian é bom para RAG porque usa Markdown local, links internos e pastas legíveis. Cada nota pode virar documento, e cada seção pode virar chunk.

## Separação importante

| Pasta | Papel |
|---|---|
| `JARVIS/` | identidade, estado, decisões e memória do agente |
| `Conhecimentos-Gerais/` | conhecimento estável e reutilizável |
| `Projetos/` | execução, entregas e estado de projetos |
| `skills/` | habilidades técnicas estruturadas |
| `Will-Pessoal/` | contexto pessoal profundo |

## Chunking

### Estratégia por cabeçalho

- `#` define o documento.
- `##` define blocos principais.
- `###` define sub-blocos.

### Estratégia por tamanho

- conceitos: 300 a 900 palavras;
- comandos: blocos pequenos;
- listas e checklists: preservar unidade;
- tabelas: não dividir;
- templates: preservar bloco inteiro.

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
updated: 2026-06-07
```

Metadados ajudam filtros, busca, dashboards, agentes e auditoria.

## Recuperação boa

Uma boa recuperação deve:

- trazer nota específica antes da genérica;
- preservar caminho do arquivo;
- incluir título e resumo;
- evitar duplicações;
- separar contexto privado de público;
- preferir notas atualizadas;
- informar quando não há resposta suficiente.

## Riscos

| Risco | Descrição | Mitigação |
|---|---|---|
| contexto errado | busca retorna nota irrelevante | melhorar tags e títulos |
| duplicação | vários arquivos dizem a mesma coisa | usar MOCs e links |
| nota muito grande | chunk confuso | dividir por conceito |
| nota sem resumo | IA precisa ler demais | preencher `summary` |
| dados sensíveis | vazamento em IA externa | separar privado e público |
| fonte antiga | resposta usa dado obsoleto | considerar `updated` |
| mistura de domínio | pessoal e técnico confundidos | separar pastas e tags |

## Padrão de resposta RAG

Uma IA usando RAG deve responder com:

1. resposta direta;
2. notas ou evidências usadas;
3. nível de confiança;
4. lacunas;
5. próximos passos.

## Memória boa para agente

Uma memória boa é:

- curta o suficiente para ser recuperada;
- específica o suficiente para ser útil;
- datada quando envolve evento;
- linkada quando envolve conceito;
- separada por tipo;
- atualizada quando muda;
- conectada a uma decisão ou ação.

## Memória ruim para agente

- frases soltas sem contexto;
- logs automáticos sem limpeza;
- pensamentos duplicados;
- arquivos enormes sem cabeçalhos;
- notas sem tags;
- registros emocionais misturados com decisões técnicas;
- dados sensíveis sem controle;
- conceitos repetidos sem nota canônica.

## Checklist de implementação

- [ ] Markdown preservado?
- [ ] YAML indexado?
- [ ] Links internos preservados?
- [ ] Chunks respeitam cabeçalhos?
- [ ] Tabelas não foram quebradas?
- [ ] Dados sensíveis foram separados?
- [ ] Há avaliação de qualidade?
- [ ] Perguntas sem resposta retornam lacuna?

## Resumo para IA

RAG melhora respostas quando o vault está limpo, bem linkado e com notas canônicas. O sistema deve recuperar pouco contexto, mas contexto certo. Priorize especificidade, metadados, data de atualização e separação entre memória, conhecimento e projeto.

## Links internos

- [[Modelos-de-Linguagem-LLMs]]
- [[Embeddings-e-Busca-Semantica]]
- [[Context-Engineering]]
- [[Avaliacao-de-RAG-e-Qualidade-de-Contexto]]
- [[Token-Economy]]
- [[../00-Ontologia-de-Conhecimento-para-IA]]
- [[../../../05-Skills/skills/04-knowledge-systems/obsidian-neural-vault]]
