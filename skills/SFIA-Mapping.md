---
title: "Mapeamento SFIA"
tags: [skills, sfia, career, framework]
date: 2026-04-27
updated: 2026-05-16
---

# Mapeamento SFIA (Skills Framework for the Information Age)

O SFIA é um framework global para mapear habilidades de tecnologia da informação. Este documento mapeia as skills do vault JARVIS para o SFIA 8, permitindo identificar lacunas, planejar desenvolvimento de carreira e alinhar skills técnicas com níveis de proficiência reconhecidos internacionalmente.

## Sobre o SFIA

Criado em 2000 pela SFIA Foundation, o framework define **102 skills** agrupadas em **6 categorias** e **7 níveis de responsabilidade**.

### Os 7 Níveis SFIA

| Nível | Título | Característica Principal |
|-------|--------|------------------------|
| 1 | Follow | Executa tarefas sob supervisão direta |
| 2 | Assist | Auxilia, executa tarefas rotineiras |
| 3 | Apply | Executa de forma independente tarefas definidas |
| 4 | Enable | Habilita outros, define padrões, revisa trabalho |
| 5 | Ensure/Advise | Garante, aconselha, tem responsabilidade estratégica |
| 6 | Initiate/Influence | Inicia, influencia, lidera mudanças significativas |
| 7 | Set strategy | Define estratégia, inspira, tem visão de mercado |

### Categorias SFIA

1. **Strategy & Architecture** (Estratégia e Arquitetura)
2. **Change & Transformation** (Mudança e Transformação)
3. **Development & Implementation** (Desenvolvimento e Implementação)
4. **Delivery & Operation** (Entrega e Operação)
5. **People & Skills** (Pessoas e Habilidades)
6. **Relationships & Engagement** (Relacionamentos e Engajamento)

## Mapeamento Skills do Vault → SFIA

| Categoria SFIA | Subcategoria | Nível Típico | Skill Pessoal | Skill no Vault |
|---------------|--------------|-------------|---------------|----------------|
| Strategy & architecture | Enterprise architecture | 5 | Arquitetura de Sistemas | [[02-software-engineering/advanced-backend-architecture]] |
| Strategy & architecture | Innovation | 5 | Inovação tecnológica | [[01-agentic-intelligence/advanced-workflows]] |
| Strategy & architecture | AI strategy | 5 | Estratégia de IA | [[01-agentic-intelligence/INDEX]] |
| Strategy & architecture | Emerging technology monitoring | 4 | Pesquisa de tendências | [[04-knowledge-systems/obsidian-neural-vault]] |
| Development & implementation | Systems design | 4 | Design de sistemas | [[02-software-engineering/advanced-backend-architecture]] |
| Development & implementation | Programming/software development | 4 | Desenvolvimento full-stack | [[02-software-engineering/backend]], [[02-software-engineering/frontend]] |
| Development & implementation | Database design | 4 | Modelagem de dados | [[02-software-engineering/Bancos-de-Dados/PostgreSQL-Advanced]] |
| Development & implementation | Testing | 3 | Testes automatizados | [[02-software-engineering/testing/SKILL.md\|Testing SKILL]] |
| Development & implementation | User experience design | 3 | UX/UI | [[02-software-engineering/frontend]] |
| Delivery & operation | Service operation | 3 | Operação de serviços | [[03-infrastructure-mcp/local-llm-ops]] |
| Delivery & operation | Cloud operations | 4 | Cloud e infra | [[03-infrastructure-mcp/mcp-servers]] |
| Delivery & operation | Security | 3 | Segurança da informação | *A definir* |
| Delivery & operation | Service desk | 2 | Suporte técnico | *A definir* |
| People & skills | Learning & development | 3 | Desenvolvimento pessoal | [[softskills/Comunicacao-Tecnica]] |
| People & skills | Performance management | 2 | Gestão de performance | *A definir* |
| People & skills | Teaching and mentoring | 4 | Mentoria técnica | [[01-agentic-intelligence/prompts]] |
| Relationships & engagement | Stakeholder management | 4 | Gestão de stakeholders | *A definir* |
| Relationships & engagement | Consulting | 5 | Consultoria técnica | [[01-agentic-intelligence/use-cases]] |

## Mapeamento de Skills AI/ML Específicas

### Prompt Engineering (Nível SFIA 4)
- **Habilidade:** Criação sistemática de prompts, chain-of-thought, few-shot.
- **Skills relacionadas:** [[01-agentic-intelligence/prompt-engineering/SKILL.md|Prompt Engineering]], [[01-agentic-intelligence/prompts]].
- **Indicadores de nível 4:** Cria templates reutilizáveis, avalia resultados, debuga falhas.

### RAG Systems (Nível SFIA 5)
- **Habilidade:** Design e implementação de sistemas Retrieval-Augmented Generation.
- **Skills relacionadas:** [[04-knowledge-systems/advanced-rag-strategies]], [[04-knowledge-systems/memory-management]].
- **Indicadores de nível 5:** Define arquitetura, escolhe estratégias de chunking/reranking, otimiza latência.

### Local LLM Operations (Nível SFIA 4)
- **Habilidade:** Deploy, configuração e otimização de LLMs locais.
- **Skills relacionadas:** [[03-infrastructure-mcp/local-llm-ops]].
- **Indicadores de nível 4:** Configura Ollama/vLLM, gerencia quantização, monitora performance.

### Multi-Agent Orchestration (Nível SFIA 5)
- **Habilidade:** Orquestração de múltiplos agentes autônomos.
- **Skills relacionadas:** [[01-agentic-intelligence/multi-agent-orchestration]], [[01-agentic-intelligence/autonomous-workflow]].
- **Indicadores de nível 5:** Desenha arquitetura multi-agente, implementa consenso e fallback.

### MCP Protocol (Nível SFIA 4)
- **Habilidade:** Implementação de servidores e clientes MCP.
- **Skills relacionadas:** [[01-agentic-intelligence/mcp]], [[03-infrastructure-mcp/mcp-servers]].
- **Indicadores de nível 4:** Cria MCP servers, gerencia autenticação, versiona APIs.

## Plano de Desenvolvimento por Nível

### Do Nível 3 para o Nível 4
```markdown
## Ações Concretas
1. **Revisão:** Comece a revisar código de outros membros do time
2. **Padrões:** Proponha e documente padrões de design
3. **Autonomia:** Pegue tarefas complexas sem supervisão direta
4. **Mentoria:** Ajude desenvolvedores nível 2-3 com dúvidas técnicas

## Skills Relevantes no Vault
- [[02-software-engineering/advanced-backend-architecture]] (padrões)
- [[02-software-engineering/testing/SKILL.md]] (revisão)
- [[softskills/Comunicacao-Tecnica]] (documentação)
```

### Do Nível 4 para o Nível 5
```markdown
## Ações Concretas
1. **Visão sistêmica:** Desenhe arquiteturas completas, não apenas componentes
2. **Tomada de decisão:** Participe de decisões de tecnologia do time
3. **Cross-team:** Colabore com outros times em iniciativas técnicas
4. **Inovação:** Proponha melhorias que impactem múltiplos projetos

## Skills Relevantes no Vault
- [[01-agentic-intelligence/advanced-workflows]] (workflows complexos)
- [[04-knowledge-systems/advanced-rag-strategies]] (design de sistemas de IA)
- [[03-infrastructure-mcp/local-llm-ops]] (infraestrutura)
```

### Do Nível 5 para o Nível 6
```markdown
## Ações Concretas
1. **Estratégia:** Participe na definição de roadmap técnico
2. **Liderança:** Lidere guildas técnicas, comunidades de prática
3. **Mentoria em escala:** Crie programas de desenvolvimento
4. **Impacto organizacional:** Suas decisões afetam a direção técnica da empresa

## Skills Relevantes no Vault
- [[SFIA-Mapping]] (visão de framework)
- [[01-agentic-intelligence/multi-agent-orchestration]] (orquestração complexa)
- [[01-agentic-intelligence/use-cases]] (visão de negócio)
```

## Gap Analysis (Lacunas Identificadas)

| Área | Nível Atual | Nível Desejado | Gap | Ações |
|------|-------------|----------------|-----|-------|
| Observabilidade | 3 | 5 | Grande | Estudar [[devops/Monitoramento]], implementar tracing |
| Segurança | 2 | 4 | Grande | Criar skill de segurança, estudar OWASP |
| Gestão de stakeholders | 3 | 5 | Médio | Praticar em projetos reais, documentar cases |
| Cloud native | 3 | 5 | Médio | Certificação AWS/Azure, hands-on com Kubernetes |
| Liderança técnica | 3 | 5 | Médio | Mentoria, tech talks, RFCs |

## Como Usar Este Mapeamento

### Para Planejamento de Carreira
1. Identifique seu nível atual em cada skill
2. Defina o nível desejado para seu próximo cargo
3. Use o gap analysis para priorizar estudos
4. Atualize este documento trimestralmente

### Para Oportunidades de Mercado
```markdown
## Cargos e Níveis SFIA Típicos

- Desenvolvedor Júnior: Nível 1-2
- Desenvolvedor Pleno: Nível 3
- Desenvolvedor Sênior: Nível 4
- Tech Lead / Staff: Nível 5
- Principal / Architect: Nível 6
- CTO / VP Engineering: Nível 7
```

### Para Avaliação de Skills
Use as skills do vault como evidência concreta para cada nível:
- **Nível 3:** "Implementei um pipeline RAG básico seguindo o guia em [[04-knowledge-systems/advanced-rag-strategies]]"
- **Nível 4:** "Desenhei e implementei a arquitetura de memória do JARVIS usando [[04-knowledge-systems/memory-management]]"
- **Nível 5:** "Defini a estratégia de RAG para o time, escolhendo entre GraphRAG e Self-RAG com base nos requisitos de negócio"

## Notas

- Níveis: 1 (Iniciante) a 7 (Estratégico).
- Adaptado do SFIA 8 (lançado em 2024).
- Skills marcadas como "*A definir*" são lacunas a serem preenchidas.

## Ferramentas de Autoavaliação

### Planilha de Progresso Trimestral

Crie uma nota no Obsidian para acompanhar seu progresso:

```markdown
---
title: "Progresso SFIA Q2 2026"
tags: [sfia, progresso, career]
date: 2026-05-16
---

# Progresso SFIA - Q2 2026

| Skill | Nível Anterior | Nível Atual | Nível Alvo | Evidência |
|-------|---------------|-------------|------------|-----------|
| RAG Systems | 3 | 4 | 5 | Implementei pipeline GraphRAG |
| LLM Ops | 3 | 4 | 4 | Configurei Ollama + vLLM em produção |
| Comunicação Técnica | 3 | 4 | 4 | Apresentei 2 tech talks |

## Próximos Passos
1. [ ] Obter certificação AWS Solutions Architect (Q3)
2. [ ] Mentorear 2 devs juniors (Q3-Q4)
3. [ ] Liderar RFC de arquitetura multi-agente (Q3)
```

### Checklist de Promoção por Nível

```markdown
## Nível 4 → 5 (Tech Lead)

### Checklist
- [ ] Desenhei e liderei a implementação de um sistema complexo
- [ ] Documentei decisões arquiteturais em ADRs
- [ ] Mentorei ao menos 2 desenvolvedores nível 3
- [ ] Contribuí com RFCs que foram aprovadas e implementadas
- [ ] Apresentei em ao menos 1 evento interno (tech talk, guild)
- [ ] Tenho visibilidade cross-team do meu trabalho

### Evidências no Vault
- ADRs em [[Projetos/Decisoes/]]
- Skills documentadas em [[skills/README]]
- Tech talks documentadas em [[softskills/Comunicacao-Tecnica]]
```

## Referências

- [SFIA 8 Official Site](https://sfia-online.org/en)
- [SFIA 8 Framework Reference](https://sfia-online.org/en/sfia-8)
- [Skills Taxonomy Browser](https://sfia-online.org/en/sfia-8/skills-taxonomy)

---

*Consulte também: [[softskills/Comunicacao-Tecnica]], [[01-agentic-intelligence/skills-categories|Skills Categories]], [[README]].*
