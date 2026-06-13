---
title: "PromptLayer — Gerenciamento e Observabilidade de Prompts"
description: "Guia completo sobre PromptLayer: logging de prompts, versionamento, experimentação, análise de custo e debugging para pipelines LLM."
tags: [promptlayer, llm-ops, prompt-management, logging, skills]
nivel: intermediário
updated: 2026-06-13
backlinks: []
assets: []
referencias: []
sensivel: false
date: 2026-06-01
---

# PromptLayer — Gerenciamento e Observabilidade de Prompts

## O que é PromptLayer?

**PromptLayer** é uma plataforma de LLMOps focada em gerenciamento de prompts. Funciona como um middleware entre sua aplicação e as APIs de LLM (OpenAI, Anthropic, Google, etc.), capturando cada requisição e resposta para oferecer:

- **Logging centralizado** de todos os prompts e respostas
- **Versionamento** de templates de prompt
- **Experimentação e testes A/B** de variações
- **Análise de custo**, latência e tokens
- **Debugging e replay** de requisições
- **Regressão** — detectar quando uma mudança no prompt quebra respostas

É uma ferramenta essencial para times que levam LLMs para produção, similar ao que DataDog é para infraestrutura ou Weights & Biases para ML.

---

## Arquitetura

```
Aplicação → LangChain/OpenAI SDK → PromptLayer → API do LLM
                                       ↓
                              Dashboard Web
                           (logs, métricas, versões)
```

O PromptLayer intercepta chamadas via:
- SDK próprio (`promptlayer` Python/Node.js)
- Integração com LangChain (`PromptLayerCallbackHandler`)
- Proxy HTTP (configurável via variáveis de ambiente)

---

## Funcionalidades Principais

### 1. Logging de Prompts

Cada chamada de LLM é registrada automaticamente com:
- Prompt completo e resposta gerada
- Metadados: modelo, temperatura, max_tokens, top_p
- Timestamps e latência
- Tags customizáveis para organização
- Custo estimado por requisição

```python
import promptlayer

# Inicialização (requer API key do PromptLayer)
pl = promptlayer.PromptLayer(api_key="pl_xxxxx")

# Log manual
response = pl.track.openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Explique RAG em 1 parágrafo"}],
    pl_tags=["prod", "rag-explicacao"]
)
```

### 2. Versionamento de Prompts

Prompts mudam com frequência. O PromptLayer mantém histórico de todas as versões:

```python
# Registrar template no PromptLayer
pl.prompts.register(
    name="traducao-profissional",
    prompt="Traduza o seguinte texto para {idioma}, mantendo tom formal:\n\n{texto}",
    version_name="v1.0"
)

# Usar versão específica no código
template = pl.prompts.get("traducao-profissional", version="v1.0")
prompt = template.format(idioma="inglês", texto="Olá, tudo bem?")
```

**Vantagens:**
- Rollback instantâneo se uma versão quebrar
- Diff entre versões no dashboard
- Prompts versionados independentes do código

### 3. Experimentação (Prompt Registry)

Teste variações de prompt lado a lado:

```python
# Registrar múltiplas versões
pl.prompts.register("classificador-sentimento", prompt_A, version="v1-detalhado")
pl.prompts.register("classificador-sentimento", prompt_B, version="v2-conciso")

# No código, usar uma variável de ambiente para selecionar versão
import os
versao = os.getenv("PROMPT_VERSION", "v2-conciso")
template = pl.prompts.get("classificador-sentimento", version=versao)
```

No dashboard, compare: precisão, custo, latência e taxa de erros entre versões.

### 4. Análise de Custo

PromptLayer calcula custo automaticamente baseado no modelo usado:

- Tokens de entrada x saída
- Modelo específico (GPT-4o, Claude Sonnet, Gemini Pro)
- Agregação por tag, usuário, período

```python
# Tags para rastrear custo por funcionalidade
response = pl.track.openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[...],
    pl_tags=["funcionalidade:chat", "usuario:william", "ambiente:prod"]
)

# Consultar custo via API
custos = pl.requests.get(
    filter={"tags": {"funcionalidade": "chat"}},
    aggregate="cost",
    date_from="2026-05-01"
)
```

### 5. Debugging e Replay

Quando uma resposta parece errada, o PromptLayer permite:

- **Replay:** reenviar o mesmo prompt para o modelo e ver a nova resposta
- **Modify & Replay:** editar o prompt e reenviar para testar correções
- **Comparação lado a lado:** resposta original vs nova tentativa
- **Score manual:** marcar respostas como corretas/incorretas para criar datasets

### 6. Testes de Regressão

Defina assertions que rodam automaticamente:

```python
# PromptLayer pode verificar respostas contra regras
# Ex: resposta não deve mencionar "não sei"
# Ex: resposta deve ter entre 50 e 200 tokens
# Ex: resposta deve conter um CEP válido
```

Isso transforma o PromptLayer em um sistema de CI/CD para prompts.

---

## Integração com LangChain

```python
from langchain_openai import ChatOpenAI
from langchain.callbacks import PromptLayerCallbackHandler
from langchain.schema import HumanMessage

# Callback do PromptLayer
pl_callback = PromptLayerCallbackHandler(
    pl_tags=["langchain", "prod"],
    pl_id_callback=lambda x: print(f"Request ID: {x}")
)

llm = ChatOpenAI(model="gpt-4o", temperature=0)
result = llm.invoke(
    [HumanMessage(content="O que é LLMOps?")],
    config={"callbacks": [pl_callback]}
)
```

A integração captura automaticamente:
- Chains completas (prompts + respostas intermediárias)
- Metadados do LangChain
- Steps do chain (RetrievalQA, etc.)

Veja [[04-knowledge-systems/advanced-rag-strategies]] para como RAG pipelines se beneficiam desse logging.

---

## Conexão com LLMOps

PromptLayer se insere no ecossistema LLMOps como a **camada de observabilidade de prompts**. Enquanto ferramentas como [[05-Skills/Explainable-AI]] focam em explicar outputs, o PromptLayer foca em gerenciar o processo de criação e evolução de prompts.

**LLMOps Stack típica:**

| Camada | Ferramenta |
|--------|------------|
| Orquestração | LangChain, LlamaIndex |
| **Prompt Management** | **PromptLayer** |
| Avaliação | LangSmith, MLFlow |
| Monitoramento | Datadog, Grafana |
| Fine-tuning | Weights & Biases |

Ver [[devops/Observabilidade]] para como logs de LLM se integram com monitoramento tradicional.

---

## Boas Práticas

1. **Tagge tudo.** Sem tags, o dashboard vira um mar de requisições sem contexto.
2. **Versionamento desde o dia 1.** Todo prompt deve ter um nome e versão registrados.
3. **Nunca logue dados sensíveis.** Configure o PromptLayer para mascarar PII. Veja [[SEGURANCA_PRIVACIDADE]].
4. **Use replay para debugar.** Antes de editar código, edite o prompt no dashboard.
5. **Defina testes de regressão** para prompts críticos (classificação, extração).
6. **Monitore custo por funcionalidade.** PromptLayer ajuda a identificar quais features consomem mais tokens.

---

## Exemplo Completo: Pipeline de Classificação

```python
import promptlayer
from langchain_openai import ChatOpenAI
from langchain.callbacks import PromptLayerCallbackHandler
from langchain.prompts import ChatPromptTemplate

pl = promptlayer.PromptLayer(api_key="pl_xxxxx")

template = ChatPromptTemplate.from_messages([
    ("system", "Classifique o sentimento do texto como positivo, negativo ou neutro."),
    ("human", "{texto}")
])

prompt_info = pl.prompts.register(
    name="classificador-sentimento",
    prompt=template.format(),
    version_name="v1.0",
    metadata={"tipo": "classificacao", "equipe": "nlp"}
)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    callbacks=[PromptLayerCallbackHandler(
        pl_tags=["classificador", "prod"],
        prompt_id=prompt_info["id"]
    )]
)

textos = ["Produto excelente!", "Atrasou a entrega", "Ok, nada demais"]
for texto in textos:
    result = llm.invoke(template.format_messages(texto=texto))
    print(f"{texto} -> {result.content}")
```

---

*Consulte também: [[04-knowledge-systems/advanced-rag-strategies]], [[05-Skills/Explainable-AI]], [[devops/Observabilidade]], [[02-software-engineering/api-design]].*

[[05-Skills/README|← Voltar à Taxonomia de Skills]]
