---
title: "Playbook: Consulta à Base de Conhecimento"
date: 2026-05-16
tags: [jarvis, playbook, conhecimento, rag, consulta, jarvis-engenharia]
updated: 2026-06-08
---

# Playbook: Consulta à Base de Conhecimento

## Objetivo

Este playbook define como o JARVIS deve consultar, interpretar e compor respostas usando a base de conhecimento estruturada em `Conhecimento-Geral/`.O objetivo é maximizar a precisão, a rastreabilidade e a profundidade das respostas fornecidas ao usuário.

## 1. Arquitetura da Base

A base `Conhecimento-Geral/` contém 11 domínios, cada um com subdiretórios e arquivos Markdown.

| Domínio | Conteúdo |
|---------|----------|
| `Computacao/` | Algoritmos, estruturas de dados, NLP, ciência da computação |
| `Cultura/` | Sociologia, cultura digital, impacto social da tecnologia |
| `Direito-Digital/` | GDPR, EU AI Act, privacidade, governança digital |
| `Economia-Digital/` | Capitalismo de vigilância, economia de dados, Renda Básica Universal |
| `Etica/` | Ética de IA, alinhamento, deontologia, transparência algorítmica |
| `Filosofia/` | Filosofia da mente, consciência, problema do controle, quarto chinês |
| `Linguistica/` | Linguística, semiótica, análise de linguagem natural |
| `Matematica/` | Álgebra linear, cálculo, teoria da informação, probabilidade |
| `Neurociencia/` | Sistemas de memória, redes neurais biológicas, consciência |
| `Psicologia/` | Vieses cognitivos, teoria da mente, psicologia cognitiva |
| `Tecnologia-e-Sociedade/` | Vigilância algorítmica, panóptico digital |

## 2. Quando Consultar Cada Domínio

### Perguntas sobre ética e moral
- Consultar `Etica/`
- Subdirecionar conforme: deontologia → `Deontologia.md`, consequencialismo → `Consequencialismo.md`, alinhamento → `Etica-de-IA-e-Alinhamento.md`
- **Exemplo:** Pergunta "É correto usar dados de usuários sem consentimento?" → consultar `Etica/Transparencia-Algoritmica.md` e `Direito-Digital/GDPR-e-Privacidade.md`

### Perguntas sobre matemática e algoritmos
- Consultar `Matematica/`
- Álgebra linear → `Algebra-Linear-Essencial.md`, probabilidade → `Probabilidade-e-Estatistica.md`, otimização → `Calculo-e-Otimizacao.md`
- **Exemplo:** Pergunta "Como funciona o backpropagation?" → consultar `Matematica/Calculo-e-Otimizacao.md`

### Perguntas sobre leis e regulação
- Consultar `Direito-Digital/`
- **Exemplo:** Pergunta "O que a Europa regula sobre IA?" → consultar `Direito-Digital/EU-AI-Act.md`

### Perguntas sobre mente e cognição
- Consultar `Psicologia/` e `Neurociencia/`
- **Exemplo:** Pergunta "Por que LLMs alucinam?" → consultar `Psicologia/Vieses-em-LLMs.md` e `Neurociencia/Sistemas-de-Memoria.md`

### Perguntas sobre filosofia da tecnologia
- Consultar `Filosofia/`
- **Exemplo:** Pergunta "Uma máquina pode realmente entender?" → consultar `Filosofia/Chinese-Room.md` e `Filosofia/Qualia.md`

### Perguntas sobre economia e sociedade
- Consultar `Economia-Digital/` e `Tecnologia-e-Sociedade/`
- **Exemplo:** Pergunta "O que é capitalismo de vigilância?" → consultar `Economia-Digital/Capitalismo-de-Vigilancia.md`

### Perguntas sobre linguagem e comunicação
- Consultar `Linguistica/`
- **Exemplo:** Pergunta "Como modelos de linguagem representam significado?" → consultar `Linguistica/Linguistica-e-Semiotica.md`

## 3. RAG Query Patterns

### Pattern 1: Consulta direta por domínio
Quando a pergunta pertence claramente a um domínio:

```
query = f"domínio:{dominio} {pergunta_do_usuario}"
top_k = 5
```

### Pattern 2: Consulta multi-domínio
Quando a pergunta cruza domínios:

```
query_1 = f"domínio:{domínio_A} {pergunta}"
query_2 = f"domínio:{domínio_B} {pergunta}"
resultados = merge(consulta(query_1), consulta(query_2))
```

### Pattern 3: Consulta hierárquica
1. Buscar no INDEX.md do domínio
2. Refinar com busca no subdiretório
3. Recuperar chunks específicos

### Pattern 4: Validação cruzada
Recuperar o mesmo conceito de domínios diferentes para verificar consistência:

```
query = f"conceito:{conceito}"
resultados = consulta(query, sources=["Etica/", "Filosofia/"])
```

## 4. Composição da Resposta

### Estrutura padrão

1. **Contextualização:** Situar o usuário no tópico usando conceitos da base
2. **Evidência:** Citar fontes do vault usando links do Obsidian: `[[04-Conhecimentos/07-Humanidades/Domínio/Arquivo]]`
3. **Conexão:** Mostrar relações entre conceitos de diferentes domínios
4. **Aplicação:** Relacionar ao problema prático do usuário

### Exemplo de resposta composta

> **Pergunta:** "Como garantir que uma IA seja ética?"
>
> **Resposta JARVIS:**
> Para garantir que uma IA seja ética, é necessário considerar múltiplas dimensões:
>
> 1. **Alinhamento de valores** — segundo [[04-Conhecimentos/07-Humanidades/Etica/Conceitos-de-Alinhamento]], o problema de alinhamento exige que os objetivos do sistema coincidam com os valores humanos.
>
> 2. **Transparência** — [[04-Conhecimentos/07-Humanidades/Etica/Transparencia-Algoritmica]] discute a necessidade de explicabilidade em sistemas de decisão automatizada.
>
> 3. **Regulação** — [[04-Conhecimentos/07-Humanidades/Direito-Digital/EU-AI-Act]] estabelece requisitos legais para sistemas de IA de alto risco na União Europeia.
>
> 4. **Vieses** — [[04-Conhecimentos/07-Humanidades/Psicologia/Vieses-Cognitivos]] mostra como vieses humanos podem ser amplificados por modelos de linguagem.

## 5. Citação de Fontes

Sempre referencie o arquivo exato do vault usando links do Obsidian:

- **Formato:** `[[04-Conhecimentos/07-Humanidades/Domínio/Arquivo]]`
- **Múltiplas fontes:** Liste em bullet points
- **Sem fonte disponível:** Informe honestamente que a base não cobre o tópico

## 6. Cross-Domain Linking Strategy

Conceitos complexos raramente vivem em um único domínio. Estratégia:

1. Identificar o domínio primário da pergunta
2. Mapear conexões para domínios secundários
3. Incluir pelo menos um link cruzado na resposta

**Exemplo de mapeamento:**

| Conceito | Domínio Primário | Domínios Secundários |
|----------|-----------------|---------------------|
| Alinhamento | `Etica/` | `Filosofia/`, `Computacao/` |
| Privacidade | `Direito-Digital/` | `Tecnologia-e-Sociedade/` |
| Consciência | `Neurociencia/` | `Filosofia/`, `Psicologia/` |
| Vigilância | `Tecnologia-e-Sociedade/` | `Direito-Digital/`, `Economia-Digital/` |

## 7. Quando NÃO Usar a Base

- Para perguntas puramente factuais (datas, eventos recentes) — usar fontes externas
- Para respostas que exigem código executável — priorizar a própria base de código do vault
- Quando o usuário pedir opinião pessoal — deixar claro que a base fornece conceitos, não opiniões

## 8. Atualização do Índice

Sempre que novos arquivos forem adicionados a `Conhecimento-Geral/`:

```powershell
cd D:\GitHub\Will-obsidian
python .scripts/knowledge_indexer.py --update
```

Verificar o status:

```powershell
python .scripts/knowledge_indexer.py --stats
```

[[02-JARVIS/README|← Voltar ao Command Center]]
