---
title: "PROJECT_JARVIS_5.0 Second Brain"
description: "Definição e regras do segundo cérebro do Jarvis, incluindo ingestão de conhecimento e prioridades de uso." 
tags:
  - jarvis
  - jarvis-engenharia
  - second-brain
  - knowledge
  - ingestion
updated: 2026-06-13
date: 2026-04-27
---

# PROJECT_JARVIS_5.0 Second Brain

Esta nota define o segundo cérebro do Jarvis e como ele deve consumir todo o conteúdo da pasta `PROJECT_JARVIS_5.0-KnowledgeBase`.

## O que é o segundo cérebro
- É a fonte de verdade do Jarvis para conhecimento, persona, arquitetura, estratégia e casos de uso.
- Não é apenas uma coleção de notas; é o contexto usado em tempo real pelo assistente.
- O segundo cérebro está em:
  `D:\OBSIDIAN\Will\Projetos\Privados\PROJECT_JARVIS_5.0-KnowledgeBase`

## O que Jarvis deve consumir
- Todas as notas Markdown (`*.md`) dentro de `PROJECT_JARVIS_5.0-KnowledgeBase`.
- Prioridade:
  1. `PROJECT_JARVIS_5.0-Knowledge.md`
  2. `PROJECT_JARVIS_5.0-Personality.md`
  3. `PROJECT_JARVIS_5.0-Architecture.md`
  4. `PROJECT_JARVIS_5.0-Strategy.md`
  5. `PROJECT_JARVIS_5.0-UseCases.md`
  6. `PROJECT_JARVIS_5.0-Tools.md`
  7. `PROJECT_JARVIS_5.0-Integration.md`
  8. `PROJECT_JARVIS_5.0-SecondBrain.md`
  9. `PROJECT_JARVIS_5.0-Map.md`
  10. `PROJECT_JARVIS_5.0.md`
  11. `PROJECT_JARVIS_5.0-README/INDEX/CONFIG/RULES`

## Porque esta pasta importa
- Ela é o segundo cérebro do Jarvis e deve estar alinhada com o código em `C:\Users\willi\Documents\GitHub\PROJECT_JARVIS_5.0`.
- O código local deve usar `JARVIS_KB_PATH` para carregar o conhecimento.
- Qualquer duplicata fora desta pasta deve ser tratada como referência ou histórico, não como verdade principal.

## Como organizar a ingestão
- Leia e normalize todos os arquivos Markdown.
- Use embeddings e RAG para cada documento.
- Marque a prioridade de cada nota e use a ordem para montar o prompt base.
- Reindexar sempre que `RULES.md`, `INDEX.md`, `CONFIG.md` ou qualquer documento estratégico mudar.

## Pipeline de ingestão do segundo cérebro
1. **Leitura**
   - Carregue cada arquivo `.md` da pasta `PROJECT_JARVIS_5.0-KnowledgeBase`.
   - Extraia texto útil e preserve seções importantes.
2. **Normalização**
   - Remova frontmatter YAML quando necessário.
   - Padronize títulos, subtítulos e listas.
   - Divida o conteúdo em blocos de parágrafo ou seções lógicas.
3. **Embeddings**
   - Gere vetores para cada bloco de texto.
   - Use o mesmo modelo de embeddings que o Jarvis utiliza em produção.
4. **RAG**
   - Armazene vetores em um índice local (FAISS, Pinecone, etc.).
   - Use um retriever para buscar trechos relevantes com base na query.
   - Combine a recuperação com prompts de contexto que priorizam as notas mais importantes.

## Regras de atualização e reindexação
- Reindexe sempre que qualquer arquivo na KB mudar de forma significativa.
- Para mudanças pequenas de estilo ou ortografia, uma reindexação diária ou semanal é suficiente.
- Para mudanças em `RULES.md`, `INDEX.md`, `CONFIG.md` ou arquivos de arquitetura/estratégia, reindexe imediatamente.
- Mantenha logs de reindexação para rastrear quando a KB foi atualizada.

## Verdade canônica vs referência histórica
- **Verdade canônica**:
  - `PROJECT_JARVIS_5.0-KnowledgeBase` é a fonte principal.
  - Notas dentro desta pasta são a base de decisão do Jarvis.
- **Referência histórica**:
  - Arquivos fora dessa pasta (por exemplo, versões antigas ou notas de pesquisa externas) devem ser usados apenas como contexto adicional.
  - Não substituem o que está em `PROJECT_JARVIS_5.0-KnowledgeBase`.
- Quando houver conflito:
  1. priorize a KB canônica.
  2. consulte `JARVIS/Decisoes/` para histórico de mudanças.
  3. registre a divergência e atualize a KB se necessário.

## Uso de variáveis de ambiente no código
- `JARVIS_KB_PATH` deve apontar para a base de conhecimento do Jarvis.
- `JARVIS_PROJECT_ROOT` deve apontar para o repositório de código real.
- O Jarvis deve carregar `JARVIS_KB_PATH` antes de executar ações de RAG ou planos.
- `JARVIS_PROJECT_ROOT` é usado para localizar código, scripts e recursos de execução.

## Formatos esperados para arquivos de KB
- `INDEX.md`:
  - lista de arquivos disponíveis e seus propósitos.
  - prioridade de leitura e links diretos.
- `RULES.md`:
  - normas de criação, edição, sincronização e uso da KB.
  - critérios de validação e estilo.
- `CONFIG.md`
  - variáveis de ambiente, caminhos, parâmetros de indexação e modelos de embeddings.
  - instruções de setup e runtime.

## Regras do segundo cérebro
- Mantenha apenas um caminho canônico para o conhecimento: esta pasta.
- Crie novas notas com prefixo `PROJECT_JARVIS_5.0-`.
- Atualize `INDEX.md` sempre que adicionar ou remover páginas.
- Use `RULES.md` para manter consistência.
- Trate `PROJECT_JARVIS_5.0-KnowledgeBase` como o local que Jarvis deve consultar primeiro.

## Nota para o código
- `JARVIS_KB_PATH` deve apontar para `D:\OBSIDIAN\Will\Projetos\Privados\PROJECT_JARVIS_5.0-KnowledgeBase`
- `JARVIS_PROJECT_ROOT` deve apontar para `C:\Users\willi\Documents\GitHub\PROJECT_JARVIS_5.0`
- O Jarvis deve carregar a pasta inteira como `secondBrain` antes de executar ações.

[[02-JARVIS/README|← Voltar ao Command Center]]
