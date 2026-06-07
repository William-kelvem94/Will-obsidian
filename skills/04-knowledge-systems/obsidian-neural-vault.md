---
tags: [knowledge, obsidian, rag, second-brain, dataview, templater, automation, skills-knowledge]
updated: 2026-06-07
title: "Obsidian Neural Vault"
date: 2026-04-27
---

# Obsidian Neural Vault

Transformando uma coleção estática de notas em um sistema de conhecimento dinâmico e alimentado por IA. Este guia cobre desde a organização do vault até automações avançadas com Dataview, Templater e integração com agentes como o [[JARVIS/Main|JARVIS]].

## 1. Vault Organization Strategies

### Estrutura de Diretórios Recomendada

```
vault/
├── 00-INDEX/              # Páginas de entrada e hubs
│   ├── Bem-vindo.md
│   ├── Dashboard.md
│   └── Projetos.md
├── 01-Agentic Intelligence/
│   ├── INDEX.md           # Map of Content (MOC)
│   ├── autonomous-workflow.md
│   └── mcp.md
├── 02-Software Engineering/
│   ├── INDEX.md
│   ├── backend.md
│   └── frontend.md
├── 03-Infrastructure-MCP/
│   ├── INDEX.md
│   ├── local-llm-ops.md
│   └── mcp-servers.md
├── 04-Knowledge Systems/
│   ├── INDEX.md
│   ├── memory-management.md
│   ├── advanced-rag-strategies.md
│   └── obsidian-neural-vault.md
├── Projetos/              # Projetos ativos
│   ├── 01-Ativos/
│   └── 02-Em-Andamento/
├── JARVIS/                # Memórias do agente
│   ├── Memorias/
│   └── Decisoes/
├── softskills/
│   └── Comunicacao-Tecnica.md
├── ai/
├── devops/
└── frontend/
```

### Princípios de Organização

1. **Atomicidade:** Uma nota = um conceito. Notas muito longas devem ser quebradas.
2. **Links abundantes:** Cada nota deve ter no mínimo 3 links para outras notas.
3. **MOCs (Maps of Content):** Cada diretório tem um `INDEX.md` que serve como hub.
4. **Consistência de frontmatter:** Toda nota tem YAML com `title`, `tags`, `date`, `updated`.

```yaml
---
title: "Obsidian Neural Vault"
tags: [knowledge, obsidian, automation]
date: 2026-04-27
updated: 2026-05-16
---

# Título
Conteúdo com [[links]] para [[conceitos]] relacionados.
```

## 2. Dataview Queries para Gestão do Conhecimento

### Consultas Básicas

````dataview
```dataview
TABLE 
  file.cday AS "Criado",
  file.mday AS "Atualizado",
  length(file.outlinks) AS "Links"
FROM "skills"
SORT file.mday DESC
LIMIT 10
```
````

### Dashboard de Projetos

````dataview
```dataview
TABLE
  choice(completed = "true", "✅", "🔄") AS Status,
  priority AS "Prioridade",
  deadline AS "Prazo"
FROM "Projetos"
WHERE type = "projeto"
SORT priority ASC
```
````

### Finding Orphan Notes (Notas sem Links)

````dataview
```dataview
LIST "⚠️ NOTA ÓRFÃ" 
FROM -"00-INDEX"
WHERE length(file.outlinks) = 0
  AND length(file.inlinks) = 0
  AND file.name != "README"
```
````

### Tags mais Usadas

````dataview
```dataview
TABLE rows.file.link AS "Notas"
FROM #skills-eng OR #skills-ai OR #skills-knowledge OR #skills-mcp
GROUP BY file.etags
SORT length(rows) DESC
```
````

### Skills Framework Viewer

````dataview
```dataview
TABLE
  category AS "Categoria",
  level AS "Nível",
  date AS "Início"
FROM "skills"
SORT category ASC, level ASC
```
````

### DataviewJS para Análise Avançada

```javascript
```dataviewjs
// Contagem de notas por categoria
const categories = dv.pages('"skills"')
  .groupBy(p => p.category || "Sem categoria")
  .map(g => [g.key, g.rows.length])
  .sort((a, b) => b[1] - a[1]);

dv.table(["Categoria", "Quantidade"], categories);

// Notas atualizadas na última semana
const recent = dv.pages('"skills"')
  .filter(p => p.file.mday.ts > Date.now() - 7 * 24 * 60 * 60 * 1000)
  .sort(p => p.file.mday, "desc");

dv.header(3, `📝 ${recent.length} notas atualizadas esta semana`);
dv.list(recent.file.link);
```
```

### Gráfico de Evolução do Conhecimento

```javascript
```dataviewjs
// Evolução mensal de criação de notas
const pages = dv.pages('"skills"');
const monthly = {};

for (const p of pages) {
  const month = p.file.cday.toFormat("yyyy-MM");
  monthly[month] = (monthly[month] || 0) + 1;
}

const data = Object.entries(monthly)
  .sort(([a], [b]) => a.localeCompare(b))
  .slice(-12);  // Últimos 12 meses

dv.paragraph(`📈 Evolução: ${data.map(([m, c]) => `${m}: ${c}`).join(" → ")}`);
```
```

## 3. Templater Automation

### Template Base para Skills

```markdown
---
title: "{{title}}"
tags: [skills, {{category}}]
date: {{date:YYYY-MM-DD}}
updated: {{date:YYYY-MM-DD}}
---

# {{title}}

## Visão Geral
Breve descrição do skill.

## Nível de Competência
- Atual: 
- Desejado: 

## Tópicos
1. 
2. 
3. 

## Projetos Relacionados
- 

## Referências
- 

---

*Tags: #{{category}}*
```

### Template para Decisões de Arquitetura (ADR)

```markdown
---
title: "ADR: {{title}}"
status: "proposed"  # proposed | accepted | deprecated
date: {{date:YYYY-MM-DD}}
tags: [adr, decision]
---

# ADR: {{title}}

## Contexto
[Descreva o problema e contexto]

## Decisão
[A decisão tomada]

## Consequências
[Impactos positivos e negativos]

## Alternativas Consideradas
1. 
2. 

## Links
- [[nota-relacionada]]
```

### Automação com Templater + Dataview

```markdown
<%*
// Cria automaticamente um MOC para todas as notas de uma tag
const tag = "rag";
const pages = dv.pages(`#${tag}`);
const list = pages.map(p => `- [[${p.file.path.replace(/\.md$/, "")}]]`).join("\n");

tR += `# MOC: ${tag}\n\n`;
tR += `Notas relacionadas (${pages.length}):\n\n`;
tR += list;
%>
```

## 4. Graph View Optimization

### Configuração de Grupos de Cores

Para manter o grafo visualmente informativo, configure grupos no plugin Graph View:

```json
{
  "groups": [
    { "query": "path:skills/01-agentic-intelligence", "color": {"a": 1, "rgb": [59, 130, 246]}},
    { "query": "path:skills/02-software-engineering", "color": {"a": 1, "rgb": [34, 197, 94]}},
    { "query": "path:skills/03-infrastructure-mcp", "color": {"a": 1, "rgb": [234, 179, 8]}},
    { "query": "path:skills/04-knowledge-systems", "color": {"a": 1, "rgb": [168, 85, 247]}},
    { "query": "path:skills/softskills", "color": {"a": 1, "rgb": [236, 72, 153]}},
    { "query": "path:Projetos", "color": {"a": 1, "rgb": [249, 115, 22]}},
    { "query": "path:JARVIS", "color": {"a": 1, "rgb": [6, 182, 212]}}
  ]
}
```

### Dicas para Grafo Saudável

- **Mantenha 3-10 links por nota:** Abaixo de 3 = ilha, acima de 10 = ruído.
- **Use links bidirecionais:** Sempre que criar um link `[[A]]` em B, considere se A também deveria linkar B.
- **Hubs naturais:** Notas INDEX e MOCs devem ser os hubs centrais com 20+ links.
- **Evite ciclos viciados:** Links A→B→C→A são ok, mas não se apoie apenas neles.

## 5. Tags vs Folders vs MOCs

| Aspecto | Tags | Folders | MOCs |
|---------|------|---------|------|
| Escopo | Atômico (1 conceito) | Hierárquico | Relacional |
| Flexibilidade | Muitas por nota | 1 por nota | Muitos por nota |
| Manutenção | Fácil de adicionar | Difícil de reorganizar | Moderada |
| Busca | Exata | Exata | Semântica |
| Graph view | Sim (agrupamento) | Sim | Sim (links) |

### Quando Usar Cada Um

```markdown
## Tags
- Para categorias transversais: #python, #rag, #docker
- Para estados: #wip, #review, #done
- Para níveis de skill: #beginner, #advanced

## Folders
- Para separação física de áreas: skills/ vs Projetos/ vs JARVIS/
- Para limites de privacidade: Projetos/01-Ativos/ vs Projetos/02-Em-Andamento/
- Para plugins que exigem path (ex: Dataview queries)

## MOCs (Maps of Content)
- Como hub de navegação: cada INDEX.md na raiz de diretórios
- Para curadoria de tópicos: "Principais recursos sobre RAG"
- Para sequências de aprendizado: "Roadmap de Agentes Autônomos"
```

### Estratégia Híbrida Recomendada

```yaml
# Use TUDO, mas com propósito:
# - Folder para namespace (skills/04-knowledge-systems/)
# - Tag para metadados transversais (#rag, #vector-db)
# - MOC para curadoria e navegação (INDEX.md)
# - Links [[wiki]] para conexões semânticas
```

## 6. Integração com IA e RAG

### Semantic Layer (Embeddings)
```python
# Gere embeddings de todas as notas para busca semântica
import frontmatter
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def index_vault(vault_path: str):
    for md_file in Path(vault_path).rglob("*.md"):
        with open(md_file) as f:
            post = frontmatter.load(f)
        
        # Gera embedding do conteúdo (excluindo frontmatter)
        content = post.content
        embedding = client.embeddings.create(
            model="nomic-embed-text", input=content[:8000]
        ).data[0].embedding
        
        # Salva no banco vetorial
        vector_db.upsert(
            id=str(md_file.relative_to(vault_path)),
            values=embedding,
            metadata={
                "title": post.get("title", md_file.stem),
                "tags": post.get("tags", []),
                "path": str(md_file),
            }
        )
```

### Context Loading Automático
```python
# Carrega automaticamente notas relevantes ao iniciar uma sessão
def load_context_for_session(topic: str) -> str:
    results = vector_db.query(
        query_embeddings=[embed(topic)],
        n_results=10,
    )
    
    context = []
    for i, metadata in enumerate(results["metadatas"][0]):
        with open(metadata["path"]) as f:
            context.append(f"--- Documento {i+1}: {metadata['title']} ---\n{f.read()[:2000]}")
    
    return "\n\n".join(context)

# Uso no prompt do agente
context = load_context_for_session("RAG strategies with memory management")
```

### Auto-Tagging com LLM
```python
def auto_tag(note_content: str, existing_tags: list[str] | None = None) -> list[str]:
    prompt = f"""Analise o conteúdo desta nota e sugira 3-5 tags.
    
    Tags existentes no vault: #agentic, #mcp, #rag, #embeddings, #vector-db,
    #python, #infrastructure, #docker, #llm, #prompt-engineering, #testing,
    #frontend, #backend, #devops, #monitoring, #security
    
    Conteúdo: {note_content[:2000]}
    
    Retorne apenas as tags separadas por vírgula."""
    
    response = llm_generate(prompt)
    return [t.strip().lower() for t in response.split(",")]
```

## 7. Publicação e Compartilhamento

### GitHub Sync Automático
```bash
# Script de sync (agendado via cron/task scheduler)
#!/bin/bash
cd /path/to/vault
DATE=$(date +%Y-%m-%d)
git add -A
git commit -m "sync: atualização automática $DATE" --allow-empty
git push origin main
```

### Publicação com Quartz ou Obsidian Publish
```yaml
# _quartz/config.toml
baseURL = "https://will-obsidian.vercel.app/"
enableRSS = true
enableSitemap = true

[plugins]
  [[plugins.transformers]]
    name = "ObsidianFlavoredMarkdown"
  [[plugins.transformers]]
    name = "Description"
    description = "Personal knowledge vault"
```

## 8. Plugins Essenciais

| Plugin | Função | Prioridade |
|--------|--------|------------|
| Dataview | Consultas SQL-like nas notas | Essencial |
| Templater | Templates avançados com JS | Essencial |
| Graph Analysis | Métricas do grafo | Alta |
| Obsidian Git | Sync automático | Alta |
| QuickAdd | Captura rápida de notas | Alta |
| Editor Syntax Highlight | Destaque de código | Média |
| Excalidraw | Diagramas técnicos | Média |
| Kanban | Gestão visual de tarefas | Média |
| Periodic Notes | Daily/Weekly notes | Opcional |

## 9. Workflows Avançados

### Research Loop
1. IA busca no vault por conceitos relacionados via busca semântica
2. IA pesquisa na web por informações atualizadas
3. IA sintetiza insights em uma nova nota
4. Nota é linkada ao MOC relevante
5. Gatilho: toda sexta-feira 17h

### Code Reference Loop
1. Ao abrir uma issue técnica, IA busca skills relevantes
2. Recupera exemplos de implementações passadas
3. Sugere padrões de código baseados no vault
4. Gatilho: comando `!search-code <problema>`

### Daily Context Loading
1. Ao iniciar sessão, IA verifica projetos ativos
2. Carrega notas relevantes no contexto do prompt
3. Apresenta resumo do último progresso
4. Gatilho: início de cada sessão JARVIS

---

*Consulte também: [[advanced-rag-strategics]], [[memory-management]], [[SFIA-Mapping]].*
