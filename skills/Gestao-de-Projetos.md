---
title: "Gestão de Projetos — Metodologias Ágeis, Scrum, Kanban e Estratégia"
description: "Fundamentos de gestão de projetos: metodologias waterfall, ágil, Scrum, Kanban, OKRs, roadmaps e gestão de riscos."
tags: [gestao, gerenciamento, metodologias-ageis, scrum, kanban, skills]
nivel: intermediário
updated: 2026-06-01
backlinks: []
assets: []
referencias: []
sensivel: false
date: 2026-06-01
---

# Gestão de Projetos — Metodologias Ágeis, Scrum, Kanban e Estratégia

## Fundamentos de Gestão de Projetos

Gestão de projetos é a aplicação de conhecimentos, habilidades, ferramentas e técnicas para atingir os objetivos de um projeto dentro das restrições de **escopo, tempo, custo e qualidade** — o chamado **Triângulo de Restrições**.

```
            Qualidade
               /\
              /  \
             /    \
            /      \
      Escopo ------ Tempo
           \        /
            \      /
             \    /
              \  /
              Custo
```

Alterar uma variável impacta as demais. Gestão de projetos é navegar esse trade-off.

### Conceitos Fundamentais

| Conceito | Definição |
|----------|-----------|
| **Projeto** | Esforço temporário com início, meio e fim, para criar um produto/serviço único |
| **Operação** | Trabalho contínuo e repetitivo (ex: suporte, manutenção) |
| **Stakeholder** | Qualquer pessoa impactada pelo projeto |
| **Entregável** | Produto ou resultado tangível gerado pelo projeto |
| **Marco** | Ponto de verificação no cronograma |
| **Linha de Base** | Versão aprovada do escopo, cronograma ou custo |

---

## Metodologias

### Waterfall (Cascata)

Abordagem tradicional, sequencial e linear. Cada fase depende da conclusão da anterior.

```
Requisitos → Design → Implementação → Testes → Implantação → Manutenção
```

**Quando usar:**
- Requisitos estáveis e bem definidos
- Projetos regulatórios (saúde, aeroespacial, construção civil)
- Equipes grandes e distribuídas

**Quando NÃO usar:**
- Requisitos incertos ou mutáveis
- Produtos digitais com ciclos rápidos
- Startups em fase de descoberta

### Agile (Metodologias Ágeis)

Conjunto de princípios definidos no **Manifesto Ágil** (2001):

1. **Indivíduos e interações** mais que processos e ferramentas
2. **Software funcionando** mais que documentação abrangente
3. **Colaboração com o cliente** mais que negociação de contratos
4. **Responder a mudanças** mais que seguir um plano

Agile não é uma metodologia, mas um conjunto de valores. Scrum e Kanban são implementações concretas.

### Scrum

Framework ágil para gestão de projetos complexos. Baseado em **sprints** (iterações de 1 a 4 semanas).

**Papéis:**

| Papel | Responsabilidade |
|-------|-----------------|
| **Product Owner** | Define o que fazer, prioriza backlog, maximiza valor do produto |
| **Scrum Master** | Facilita o processo, remove impedimentos, garante que o Scrum seja seguido |
| **Time de Desenvolvimento** | Auto-organizado, multidisciplinar, entrega as funcionalidades |

**Eventos:**

| Evento | Duração | Propósito |
|--------|---------|-----------|
| Sprint Planning | 2-4h/sprint | Planejar o que será feito |
| Daily Scrum | 15 min/dia | Sincronizar e ajustar plano |
| Sprint Review | 1-2h/sprint | Mostrar o que foi feito, receber feedback |
| Sprint Retrospective | 1-1.5h/sprint | Melhorar o processo |

**Artefatos:**

- **Product Backlog:** Lista priorizada de tudo que pode ser feito
- **Sprint Backlog:** Itens selecionados para o sprint atual
- **Incremento:** Soma de todos os itens concluídos (potencialmente entregável)

```python
# Exemplo: ferramenta simples de planejamento de sprint
class Sprint:
    def __init__(self, numero, dias_uteis, capacidade_horas):
        self.numero = numero
        self.dias_uteis = dias_uteis
        self.capacidade_total = capacidade_horas
        self.backlog = []
    
    def add_item(self, descricao, estimativa, prioridade):
        self.backlog.append({
            "descricao": descricao,
            "estimativa": estimativa,
            "prioridade": prioridade,
            "status": "pendente"
        })
    
    def capacidade_restante(self):
        soma = sum(item["estimativa"] for item in self.backlog 
                   if item["status"] in ("pendente", "em_andamento"))
        return self.capacidade_total - soma
    
    def velocity_historico(self, sprints_anteriores):
        """Calcula velocity média dos sprints anteriores"""
        if not sprints_anteriores:
            return self.capacidade_total * 0.7  # 70% inicial
        return sum(s.pontos_concluidos() for s in sprints_anteriores) / len(sprints_anteriores)
```

### Kanban

Sistema visual de gestão de fluxo de trabalho. Originado no Toyota Production System.

**Princípios:**
1. **Visualize o trabalho:** quadro com colunas (To Do → In Progress → Done)
2. **Limite o WIP (Work in Progress):** evita sobrecarga da equipe
3. **Gerencie o fluxo:** meça lead time e ciclo
4. **Políticas explícitas:** regras claras de quando algo avança
5. **Melhoria contínua:** Kaizen

**Kanban vs Scrum:**

| Aspecto | Scrum | Kanban |
|---------|-------|--------|
| Ciclo | Sprints fixos | Fluxo contínuo |
| Papéis | Definidos (PO, SM, Time) | Não define papéis |
| Priorização | Por sprint | Contínua |
| Métrica principal | Velocity | Lead Time / Cycle Time |
| Mudanças | Só entre sprints | A qualquer momento |
| Ideal para | Produtos complexos | Suporte, operações, manutenção |

---

## Ferramentas de Gestão

### OKRs (Objectives and Key Results)

Metodologia de definição de metas criada na Intel e popularizada pelo Google.

**Estrutura:**
- **Objective:** meta qualitativa, inspiradora, com prazo
- **Key Results:** 3-5 métricas quantitativas que medem progresso

```
Objective: Tornar o JARVIS o assistente de IA mais confiável do mercado

KR1: Atingir 99.9% de uptime nos microserviços
KR2: Reduzir falsos positivos em respostas para < 1%
KR3: Aumentar NPS de usuários de 65 para 85
```

**Boas práticas OKR:**
- OKRs são ambiciosos (70% de conclusão é sucesso)
- Cada pessoa/equipe deve ter 3-5 OKRs por trimestre
- OKRs são públicos e transparentes

### Roadmaps

Visão estratégica de alto nível que mostra a direção do produto ao longo do tempo.

```
Q2 2026        Q3 2026        Q4 2026        Q1 2027
│ MVP Core  │  Analytics  │  Mobile App  │  API Pública
│ Chat IA    │  │          │  │           │
│ RAG básico │  Dashboard  │  Push       │  Marketplace
```

**Tipos de roadmap:**
- **Tático:** próximas 4-8 semanas, granular
- **Estratégico:** 6-12 meses, temas, não funcionalidades
- **Visionário:** 12-24 meses, direção geral

### Gestão de Riscos

Identificar, analisar e responder a incertezas que podem afetar o projeto.

**Matriz de Riscos (Probabilidade x Impacto):**

```python
class Risco:
    def __init__(self, descricao, probabilidade, impacto, categoria):
        self.descricao = descricao
        self.probabilidade = probabilidade  # 1-5
        self.impacto = impacto  # 1-5
        self.categoria = categoria
        self.score = probabilidade * impacto
        self.plano_resposta = ""
        self.responsavel = ""

    def classificacao(self):
        if self.score >= 20: return "Crítico"
        elif self.score >= 12: return "Alto"
        elif self.score >= 6: return "Médio"
        else: return "Baixo"

riscos = [
    Risco("Churn de engenheiro-chave", 3, 5, "Pessoas"),
    Risco("Atraso em dependência externa", 4, 4, "Terceiros"),
    Risco("Mudança de escopo sem aviso", 5, 3, "Escopo"),
    Risco("Falha de infraestrutura cloud", 2, 5, "Infra"),
]

for r in riscos:
    respostas = {
        "Evitar": "Mudar abordagem para eliminar o risco",
        "Mitigar": "Reduzir probabilidade ou impacto",
        "Transferir": "Seguro, terceirização",
        "Aceitar": "Conviver com o risco, plano de contingência"
    }
```

---

## Conectando com Produtividade e Organização

### Gestão de Projetos no Desenvolvimento de Software

- **Fase de descoberta:** Roadmap + OKRs para alinhar visão
- **Fase de execução:** Scrum para entregas iterativas
- **Fase de operação:** Kanban para suporte e manutenção
- **Fase de aprendizado:** Retrospectivas para melhoria contínua

Veja [[Projetos]] para uma visão dos projetos ativos no vault.

### Para o Profissional Individual

Gestão de projetos não se aplica apenas a times. Para uso pessoal:

- **Kanban pessoal:** organize tarefas do dia/semana no [[Cerebro-Will]]
- **OKRs trimestrais:** defina metas de aprendizado e carreira
- **Roadmap de habilidades:** consulte o [[skills/SFIA-Mapping]] para planejar desenvolvimento técnico
- **Retrospectiva pessoal:** revise o que funcionou e o que melhorar

### Gestão de Projetos Técnicos

Para projetos de engenharia de dados, ML e infraestrutura, consulte:

- [[data-engineering/etl-pipelines]] — planejamento de pipelines
- [[devops/Kubernetes]] — gestão de clusters (infra como projeto)
- [[devops/FinOps]] — gestão de custos de cloud
- [[skills/Skill-Project-Matrix]] — mapeamento de skills para projetos

---

## Métricas-Chave de Projeto

| Métrica | O que mede | Metodologia |
|---------|-----------|-------------|
| **Velocity** | Pontos por sprint | Scrum |
| **Lead Time** | Tempo da demanda até entrega | Kanban |
| **Cycle Time** | Tempo do início ao fim do trabalho | Kanban |
| **CFR (Cumulative Flow)** | Distribuição do trabalho ao longo do tempo | Kanban |
| **Sprint Burndown** | Progresso vs planejado | Scrum |
| **Net Promoter Score** | Satisfação do stakeholder | Todas |
| **Índice de Entregas no Prazo** | Confiabilidade | Todas |

---

## Boas Práticas

1. **Não existe metodologia perfeita.** Adapte Scrum, Kanban e Waterfall ao contexto.
2. **Documente decisões, não burocracia.** O registro deve habilitar, não travar.
3. **Cerimônias com propósito.** Daily não é status report — é sincronização.
4. **Estimativas são aproximações.** Use ranges (3-5 dias), não pontos fixos.
5. **Risco não é negativo.** Risco bem gerenciado é vantagem competitiva.
6. **Celebre entregas, não ocupação.** Produtividade não é horas trabalhadas, é valor entregue.
7. **Melhoria contínua > perfeição.** Uma retrospectiva boa é melhor que um processo perfeito no papel.

---

*Consulte também: [[Projetos]], [[Cerebro-Will]], [[skills/SFIA-Mapping]], [[skills/Skill-Project-Matrix]], [[data-engineering/etl-pipelines]], [[devops/FinOps]].*

[[skills/README|← Voltar à Taxonomia de Skills]]
