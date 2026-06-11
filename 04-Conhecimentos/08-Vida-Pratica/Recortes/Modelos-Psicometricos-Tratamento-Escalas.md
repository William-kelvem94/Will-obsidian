Profissionais de desenvolvimento humano, cientistas de dados e operadores organizacionais frequentemente se deparam com o desafio de monitorar variáveis psicológicas de estresse e engajamento sem introduzir ruídos ou metodologias pseudocientíficas superficiais. Para estruturar diagnósticos de alta relevância clínica e pragmática, esta nota compila os principais modelos e questionários psicométricos validados internacionalmente, acompanhados de suas equações de calibração e diretrizes de escaneamento.

---

## 🎯 1. Inventário de Burnout de Maslach (MBI-GS)

O *Maslach Burnout Inventory — General Survey* (MBI-GS) é a métrica padrão-ouro reconhecida pela Organização Mundial da Saúde (OMS) na CID-11 para avaliação da Síndrome de Esgotamento Profissional. O modelo é subdividido em três eixos independentes avaliados por escala Likert de 7 pontos (frequência de $0$ a $6$):

```
                   ESTRUTURA TRIDIMENSIONAL DO MBI:
                        ┌──────────────────┐
                        │ Exaustão (EX)    │
                        └────────┬─────────┘
                                 │
                  ┌──────────────┴──────────────┐
                  ▼                             ▼
       ┌────────────────────┐        ┌────────────────────┐
       │ Despersonalização  │        │ Ineficácia (Efic.) │
       │ (CY - Cinismo)     │        │ (PE - Profissional)│
       └────────────────────┘        └────────────────────┘
```

### 1.1 Exaustão Emocional (EE / EX)
Mede a exaustão física e mental induzida por cargas extremas de trabalho contínuo. Avaliado por 5 itens estruturais.
$$EX\_Score = \frac{\sum_{i=1}^{5} Item\_EX_i}{5}$$

### 1.2 Cinismo / Despersonalização (CY)
Mede o distanciamento afetivo, frieza, cinismo e indiferença desenvolvidos como mecanismo de defesa e isolamento das pressões do labor. Avaliado por 5 itens estruturais.
$$CY\_Score = \frac{\sum_{i=1}^{5} Item\_CY_i}{5}$$

### 1.3 Eficácia Profissional (PE)
Mede o sentimento de competência pessoal, produtividade e realização no trabalho. Diferentemente das duas dimensões anteriores, **escores baixos** nesta dimensão de realização sinalizam Burnout. Avaliado por 6 itens estruturais.
$$PE\_Score = \frac{\sum_{i=1}^{6} Item\_PE_i}{6}$$

---

## ⚡ 2. Escala de Engajamento de Utrecht (UWES-9)

A escala *Utrecht Work Engagement Scale* (UWES-9) atua no polo positivo da psicologia organizacional, medindo o estado de realização profissional sustentável pelas vias de engajamento do colaborador. Diferencia-se de uma satisfação passiva por investigar proativamente o foco produtivo e dinâmicas cognitivas:

| Dimensão UWES | Descrição | Modelo Likert (0-6) |
|---|---|---|
| **Vigor (VI)** | Altos níveis de energia e resiliência mental enquanto trabalha. | *"No meu trabalho, sinto-me cheio de energia."* |
| **Dedicação (DE)** | Forte sentimento de significado, entusiasmo, inspiração e orgulho. | *"Estou entusiasmado com o meu trabalho."* |
| **Absorção (AB)** | Estado de imersão total e concentração profunda (*flow*). | *"O tempo 'voa' quando estou trabalhando."* |

### Equação de Calibração de Engajamento Geral
$$\text{UWES\_9\_Score} = \frac{\sum Item\_VI + \sum Item\_DE + \sum Item\_AB}{9}$$

*Status de Diagnóstico*: Escores de média superiores a $4.6$ classificam-se como de **Muito Alto Engajamento**, enquanto médias de escores abaixo de $1.9$ sinalizam apatia ou risco severo de absenteísmo.

---

## 📋 3. Escala de Estresse Percebido (PSS-10)

Desenvolvida por Sheldon Cohen, a *Perceived Stress Scale* (PSS-10) quantifica o grau em que as situações da vida e do trabalho de um indivíduo são avaliadas como imprevisíveis, incontroláveis e sobrecarregadas.

*   **Frequência de Escala**: De $0$ (Nunca) a $4$ (Sempre).
*   **Ajuste de Itens Inversos**: Os itens 4, 5, 7 e 8 medem sentimentos de controle e capacidade de lidar com estressores e, portanto, exigem inversão matemática de pontuação antes do cálculo final:
    $$\text{Item\_Inverso\_Score} = 4 - \text{Item\_Bruto\_Score}$$

### Cálculo do Escoramento Consolidado
$$\text{PSS\_10\_Score} = \sum (\text{Itens\_Normais}) + \sum (4 - \text{Itens\_Inversos})$$

```
Interpretação dos Scores Totais do PSS-10:
  • 0 a 13   ──► Estresse Baixo / Saudável
  • 14 a 26  ──► Estresse Moderado / Sinais de Alerta
  • 27 a 40  ──► Estresse Severo / Necessidade de Intervenção Clínica Imediata
```

---

## 🛡️ 4. Protocolo Organizacional de Escaneamento e Governança de Dados

Para garantir a confiabilidade dos relatórios e precaver distorções nas métricas causadas por vieses de desejabilidade social (colaboradores mascarando sintomas por receio de punições ou demissões), o pipeline de escaneamento deve contemplar as seguintes restrições:

1.  **Anonimização com Chaves Criptográficas Irreversíveis**: Os dados brutos das pesquisas Likert devem ser transmitidos por conexões seguras sem salvar o nome, e-mail ou IP do colaborador. Utilize hashes criptográficos irreversíveis contendo salt temporal caso precise rastrear respostas longitudinais no mesmo indivíduo de forma anônima.
2.  **Amostragem Mínima Viável por Squad**: Nunca exiba resultados de estatísticas analíticas de Burnout ou Engajamento para recortes populacionais (squads ou times) com menos de **5 respondentes**. Isso previne a re-identificação indireta das respostas individuais por cruzamento simples de dados de perfil pelo gestor.
3.  **Garantia de feedback reverso**: A squad deve re-acessar o painel consolidado de sua respectiva divisão, garantindo que o escaneamento não atue como um canal de controle unidirecional, mas como um termômetro transparente de cooperação técnica.

---

## 📑 5. Links no Cofre
- Acompanhamento prático e dashboard de bem-estar: [Painel-Health-Mental-Humor.md](00-Inbox/Ideias/Painel-Health-Mental-Humor.md)
- Estudo de fadiga em squads de DevOps: [[04-Conhecimentos/08-Vida-Pratica/Projetos/Rastreamento-Clinico-Fadiga-Cognitiva]]
- Protocolo ativo de cooldown nas sprints: [[04-Conhecimentos/08-Vida-Pratica/Checklists/Checklist-Mitigacao-Burnout-Squads]]
