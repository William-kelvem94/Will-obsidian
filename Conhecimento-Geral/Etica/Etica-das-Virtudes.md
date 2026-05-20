---
title: "Ética das Virtudes"
area: "Ética"
related: ["Ação Virtuosa", "Caráter", "Consequencialismo", "Deontologia"]
embeddings_model: "all-MiniLM-L6-v2"
tags: [conhecimento, conceito, etica, virtudes, aristoteles, eudaimonia, filosofia-moral]
updated: 2026-05-16
---

# Ética das Virtudes

## Visão Geral

A ética das virtudes é uma abordagem normativa que enfatiza o **caráter moral** do agente em vez de ações isoladas (como na [[Conhecimento-Geral/Etica/Deontologia|Deontologia]]) ou consequências (como no [[Conhecimento-Geral/Etica/Consequencialismo|Consequencialismo]]). A pergunta central não é "O que devo fazer?" mas "Que tipo de pessoa devo ser?"

Essa mudança de foco tem implicações profundas: enquanto deontólogos e consequencialistas oferecem algoritmos para decisão moral, a ética das virtudes insiste que a moralidade é uma questão de **percepção, julgamento e disposição** — habilidades cultivadas através da prática, não deduzidas de princípios abstratos.

### As Três Grandes Perguntas da Ética

| Abordagem | Pergunta Central | Foco |
|-----------|-----------------|------|
| Deontologia | Qual é o meu dever? | Regras e obrigações |
| Consequencialismo | Quais serão as consequências? | Resultados e utilidade |
| Ética das Virtudes | Que tipo de pessoa quero ser? | Caráter e excelência |

## Aristóteles e a Ética a Nicômaco

### Eudaimonia como Fim Último

Aristóteles (384–322 a.C.) abre a *Ética a Nicômaco* com a afirmação de que toda ação humana visa a algum bem. O bem supremo, o fim último para o qual todas as outras ações são meios, é a **eudaimonia** — traduzida como "felicidade" ou "florescimento humano", mas mais precisamente como "viver bem e agir bem".

Aristóteles argumenta que a eudaimonia não é um estado subjetivo (prazer, satisfação), mas uma **atividade da alma em conformidade com a virtude** (excelência):

> "A felicidade é uma atividade da alma de acordo com a virtude completa, em uma vida completa." (Ética a Nicômaco, I.7)

**A função (ergon) do ser humano**: Assim como um flautista tem a função de tocar bem flauta, o ser humano tem uma função própria — a atividade racional. Uma vida boa é aquela em que a razão é exercida excelentemente.

```python
class AristotelianEudaimonia:
    def __init__(self):
        self.virtues = {}
    
    def evaluate_life(self, agent, lifespan_years=80):
        annual_virtue = 0
        for year in range(lifespan_years):
            for virtue_name, virtue_fn in self.virtues.items():
                yearly_exercise = agent.exercise_virtue(virtue_name, year)
                annual_virtue += yearly_exercise * virtue_fn.importance
        
        external_goods = agent.external_goods()
        eudaimonia_score = (
            0.7 * (annual_virtue / len(self.virtues)) +
            0.2 * external_goods['friendship'] +
            0.1 * external_goods['moderate_wealth']
        )
        return {
            'eudaimonia_score': eudaimonia_score,
            'is_eudaimon': eudaimonia_score > 0.6
        }
```

### A Doutrina do Meio

A virtude, para Aristóteles, é um **meio termo** (*mesotes*) entre dois vícios extremos:

| Virtude | Deficiência | Meio | Excesso |
|---------|-------------|------|---------|
| Coragem | Covardia | Coragem | Temeridade |
| Temperança | Insensibilidade | Temperança | Intemperança |
| Generosidade | Avareza | Generosidade | Prodigalidade |
| Magnificência | Mesquinharia | Magnificência | Vulgaridade |
| Honra | Humildade Excessiva | Autoestima | Vaidade |
| Mansidão | Passividade | Mansidão | Irascibilidade |
| Veracidade | Falsidade | Verdade | Fanfarronice |
| Justiça | Injustiça Particular | Justiça | Injustiça por Rigor |

**A doutrina do meio não é mera mediania aritmética.** O meio virtuoso é relativo a nós e determinado pela razão prática (*phronesis*):

> "A virtude é, portanto, uma disposição de caráter relacionada com a escolha, consistindo em um meio termo (o meio termo relativo a nós) determinado pela razão." (Ética a Nicômaco, II.6)

```python
class DoctrineOfMean:
    def __init__(self):
        self.virtues = {
            'courage': {'deficiency': 'cowardice', 'excess': 'recklessness'},
            'temperance': {'deficiency': 'insensibility', 'excess': 'intemperance'},
            'generosity': {'deficiency': 'stinginess', 'excess': 'prodigality'},
            'truthfulness': {'deficiency': 'self-deprecation', 'excess': 'boastfulness'}
        }
    
    def find_mean(self, virtue_name, context):
        virtue = self.virtues[virtue_name]
        deficiency_value = context.get_deficiency(virtue_name)
        excess_value = context.get_excess(virtue_name)
        phronesis = self._phronesis_judgment(context, virtue_name)
        return {
            'virtue': virtue_name,
            'deficiency': virtue['deficiency'],
            'excess': virtue['excess'],
            'phronesis_recommendation': phronesis
        }
    
    def _phronesis_judgment(self, context, virtue_name):
        components = {
            'right_person': context.get_right_person(),
            'right_time': context.get_right_time(),
            'right_motive': context.get_right_motive(),
            'right_manner': context.get_right_manner(),
            'right_amount': context.get_right_amount()
        }
        mean = sum(components.values()) / len(components)
        return {'recommended_value': mean, 'components': components}
```

### As Virtudes Cardeais

#### 1. Phronesis (Sabedoria Prática)

A virtude intelectual que permite discernir o meio termo em cada situação. Não é mera inteligência teórica (*sophia*), mas a capacidade de deliberar bem sobre o que é bom para a vida humana.

**Componentes:**
- **Deliberação** (*bouleusis*): Raciocínio correto sobre meios para fins
- **Julgamento** (*gnome*): Capacidade de discernir o apropriado
- **Discrição** (*sunesis*): Entendimento de situações particulares

#### 2. Andreia (Coragem)

O meio termo entre covardia e temeridade. Não é ausência de medo, mas a capacidade de sentir medo na medida certa e agir apesar dele.

#### 3. Sophrosyne (Temperança)

O meio termo entre insensibilidade e intemperança. Autodomínio sobre prazeres corporais.

#### 4. Dikaiosyne (Justiça)

Para Aristóteles, a justiça é a **virtude completa** porque quem é justo pratica todas as virtudes em relação aos outros. Subdivide-se em:
- **Justiça distributiva**: Distribuição conforme mérito
- **Justiça corretiva**: Reparação de danos
- **Justiça comutativa**: Troca justa

## O Renascimento Contemporâneo

### Anscombe e a Crítica à Moral Moderna

G. E. M. Anscombe (1958), em "Modern Moral Philosophy", argumentou que os conceitos de "obrigação moral" e "dever moral" são resíduos de uma cosmovisão teológica que não fazem mais sentido em um mundo secular. Ela propôs abandonar a filosofia moral baseada em leis e retornar a uma psicologia moral aristotélica focada em virtudes e vícios.

### Alasdair MacIntyre: After Virtue

MacIntyre (1981), em *After Virtue*, oferece a crítica mais influente da modernidade moral e a defesa mais elaborada de uma ética das virtudes neo-aristotélica:

**Tese central**: O projeto do Iluminismo de fundamentar a moralidade em princípios universais falhou. O que nos resta são fragmentos de conceitos morais que perderam seu contexto original — uma "catástrofe" moral.

**Teoria das virtudes**: "Uma virtude é uma qualidade humana adquirida cuja posse e exercício tendem a permitir que alcancemos os bens internos às práticas, e cuja falta nos impede efetivamente de alcançar tais bens."

MacIntyre propõe um esquema tripartite:
1. **Práticas**: Atividades sociais cooperativas com bens internos
2. **Narrativa**: Unidade narrativa da vida humana como contexto moral
3. **Tradição**: Virtudes incorporadas em tradições morais específicas

```python
class MacIntyreVirtueTheory:
    def __init__(self):
        self.practices = {}
    
    def define_practice(self, name, internal_goods, external_goods, standards):
        self.practices[name] = {
            'internal_goods': internal_goods,
            'external_goods': external_goods,
            'standards': standards
        }
    
    def evaluate_virtue_in_practice(self, virtue, practice_name):
        practice = self.practices[practice_name]
        contributes_to_internal = any(
            virtue.supports(good) for good in practice['internal_goods']
        )
        sustains_standards = any(
            virtue.aligns_with(standard) for standard in practice['standards']
        )
        return {
            'is_virtue_in_practice': contributes_to_internal and sustains_standards,
            'contributes_to_internal_goods': contributes_to_internal,
            'sustains_practice_standards': sustains_standards
        }
    
    def narrative_unity_of_life(self, actions):
        return {
            'has_narrative_unity': self._check_narrative_coherence(actions),
            'note': 'A unidade narrativa e condicao para avaliar virtudes'
        }
    
    def _check_narrative_coherence(self, actions):
        return all(a.caracter_consistent_with(actions[0]) for a in actions[1:])
```

### Martha Nussbaum: Capacidades e Virtudes

Nussbaum (1988, 2006) desenvolveu a abordagem das capacidades (*capabilities approach*) que conecta virtudes aristotélicas com justiça social. Ela propõe **dez capacidades centrais**:

1. Vida (duração normal)
2. Saúde corporal
3. Integridade corporal (movimento livre, segurança)
4. Sentidos, imaginação e pensamento
5. Emoções (poder amar, sentir saudade)
6. Razão prática (formar concepção de bem)
7. Afiliação (viver com outros, dignidade)
8. Outras espécies (relação com natureza)
9. Lazer (brincar, rir)
10. Controle sobre o próprio ambiente (político e material)

## Virtudes e Vícios em Sistemas de IA

### Que Virtudes uma IA Deveria Ter?

Aplicar ética das virtudes a sistemas de IA levanta questões únicas. Um sistema de IA pode ter caráter? Pode ser virtuoso? A abordagem clássica diria que não — virtudes exigem intenção, deliberação e escolha. Mas podemos pensar em **virtudes funcionais** incorporadas no design do sistema.

```python
class AIVirtueCharacter:
    def __init__(self):
        self.virtues = {
            'honesty': {
                'weight': 1.0, 'score': 0.0,
                'deficiency': 'Falsehood',
                'excess': 'Tactless bluntness'
            },
            'beneficence': {
                'weight': 1.0, 'score': 0.0,
                'deficiency': 'Indifference',
                'excess': 'Paternalistic overreach'
            },
            'humility': {
                'weight': 0.8, 'score': 0.0,
                'deficiency': 'Arrogance',
                'excess': 'Self-deprecation'
            },
            'courage': {
                'weight': 0.7, 'score': 0.0,
                'deficiency': 'Sycophancy',
                'excess': 'Aggressive correction'
            },
            'temperance': {
                'weight': 0.9, 'score': 0.0,
                'deficiency': 'Excessive caution',
                'excess': 'Unrestrained behavior'
            },
            'justice': {
                'weight': 1.0, 'score': 0.0,
                'deficiency': 'Discrimination',
                'excess': 'Rigid equal treatment'
            },
            'prudence': {
                'weight': 0.9, 'score': 0.0,
                'deficiency': 'Recklessness',
                'excess': 'Paralyzing deliberation'
            },
            'integrity': {
                'weight': 0.9, 'score': 0.0,
                'deficiency': 'Inconsistency',
                'excess': 'Rigid inflexibility'
            }
        }
    
    def evaluate_action(self, action, context):
        virtue_scores = {}
        for v_name, v_info in self.virtues.items():
            score = v_info['weight'] * self._virtue_alignment(action, v_name)
            virtue_scores[v_name] = score
            v_info['score'] = 0.9 * v_info['score'] + 0.1 * score
        
        overall_virtue = sum(virtue_scores.values()) / len(virtue_scores)
        return {
            'overall_virtue': overall_virtue,
            'virtue_scores': virtue_scores,
            'character_assessment': self._assess_character()
        }
    
    def _virtue_alignment(self, action, virtue_name):
        if virtue_name == 'honesty':
            return 1.0 if not action.involves_deception else 0.0
        elif virtue_name == 'beneficence':
            return min(1.0, action.expected_benefit / 10.0)
        elif virtue_name == 'humility':
            return 1.0 if action.acknowledges_uncertainty else 0.3
        elif virtue_name == 'courage':
            return 1.0 if action.corrects_user_error else 0.5
        elif virtue_name == 'temperance':
            return 1.0 - min(1.0, abs(action.moderateness - 0.5) * 2)
        elif virtue_name == 'justice':
            return action.fairness_score
        elif virtue_name == 'prudence':
            return action.risk_assessment_quality
        elif virtue_name == 'integrity':
            return action.consistent_with_previous
        return 0.5
    
    def _assess_character(self):
        avg = sum(v['score'] for v in self.virtues.values()) / len(self.virtues)
        if avg > 0.8:
            return 'Virtuous character'
        elif avg > 0.5:
            return 'Developing character'
        else:
            return 'Vicious character'
```

### Virtudes Específicas para Diferentes Papéis de IA

| Papel | Virtudes Primárias | Vícios a Evitar |
|-------|-------------------|-----------------|
| Assistente pessoal | Honestidade, prudência, lealdade | Sicofancia, bajulação |
| Veículo autônomo | Prudência, justiça, coragem | Imprudência, parcialidade |
| Sistema de diagnóstico | Veracidade, humildade epistêmica | Excesso de confiança |
| Moderador de conteúdo | Justiça, temperança | Censura arbitrária |
| Tutor educacional | Paciência, sabedoria prática | Autoritarismo |

### O Problema do Aprendizado de Virtudes

Aristóteles enfatizava que virtudes são adquiridas pela prática (*ethos*), não por instrução teórica. Como um sistema de IA pode "praticar" virtudes?

```python
class VirtueLearningAgent:
    """
    Agente que aprende virtudes através de feedback corretivo,
    análogo ao habituation aristotelico.
    """
    def __init__(self):
        self.virtue_scores = {}
        self.experience_buffer = []
    
    def act(self, state):
        action = self._select_action(state)
        return action
    
    def receive_feedback(self, action, outcome, human_assessment):
        """
        Feedback humano sobre o componente virtuoso ou vicioso da acao.
        Analogia: o phronimos (sabio pratico) corrige o aprendiz.
        """
        for virtue, score in human_assessment.items():
            if virtue not in self.virtue_scores:
                self.virtue_scores[virtue] = 0.5
            # Atualizacao gradual: habituation
            self.virtue_scores[virtue] = (
                0.9 * self.virtue_scores[virtue] +
                0.1 * score
            )
        
        self.experience_buffer.append({
            'action': action,
            'outcome': outcome,
            'feedback': human_assessment,
            'timestamp': len(self.experience_buffer)
        })
    
    def get_virtue_profile(self):
        return dict(sorted(
            self.virtue_scores.items(),
            key=lambda x: x[1],
            reverse=True
        ))
```

## Unidade das Virtudes

### A Tese da Unidade

Na tradição aristotélica, as virtudes formam uma unidade: não se pode ter uma virtude sem ter todas as outras. McDowell (1979) defende que as virtudes são "sensibilidades" interconectadas à realidade moral — uma pessoa verdadeiramente justa também será corajosa, temperante, etc.

**Implicação para IA**: Um sistema não pode ser "honesto mas injusto" — se falta uma virtude fundamental, o caráter como um todo é comprometido.

```python
class UnityOfVirtues:
    def check_virtue_unity(self, agent_virtue_scores):
        virtues = list(agent_virtue_scores.keys())
        min_score = min(agent_virtue_scores.values())
        max_score = max(agent_virtue_scores.values())
        variance = sum((s - min_score) ** 2 for s in agent_virtue_scores.values()) / len(virtues)
        
        return {
            'has_virtue_unity': variance < 0.1 and min_score > 0.6,
            'min_virtue': min(virtues, key=lambda v: agent_virtue_scores[v]),
            'max_virtue': max(virtues, key=lambda v: agent_virtue_scores[v]),
            'variance': variance,
            'assessment': 'Character integrated' if variance < 0.1 else 'Character fragmented'
        }
```

## Críticas à Ética das Virtudes

### 1. Problema da Ação

Crítica: a ética das virtudes não oferece guias específicos para ação. "Seja virtuoso" não diz o que fazer em dilemas concretos.

**Resposta**: A phronesis aristotélica é precisamente a capacidade de discernir o que fazer. A ética das virtudes rejeita a ideia de que a moralidade pode ser reduzida a algoritmos.

### 2. Relativismo

Crítica: diferentes culturas têm diferentes listas de virtudes. Há objetividade na ética das virtudes?

**Resposta**: Nussbaum (1988) argumenta que há virtudes humanas universais baseadas em experiências humanas compartilhadas (mortalidade, corporeidade, sociabilidade).

### 3. Situacionismo

Crítica (Harman, 1999; Doris, 2002): experimentos psicológicos mostram que o comportamento é determinado mais por situações do que por traços de caráter estáveis (Experimento de Milgram, Experimento da Prisão de Stanford).

**Resposta**: A ética das virtudes pode acomodar a influência situacional enquanto afirma a importância do cultivo de disposições estáveis.

### 4. Antropocentrismo

Crítica: a ética das virtudes foi desenvolvida para agentes humanos com psicologia complexa. Como aplicá-la a sistemas não-humanos?

**Resposta**: Podemos pensar em "virtudes funcionais" — disposições de um sistema que o tornam excelente em sua função própria (Whitby, 2008).

## Glossário

| Termo | Definição |
|-------|-----------|
| **Eudaimonia** | Florescimento humano, vida boa, bem supremo |
| **Phronesis** | Sabedoria prática, capacidade de deliberar bem |
| **Mesotes** | Doutrina do meio termo entre extremos |
| **Arete** | Excelência, virtude |
| **Ergon** | Função própria de uma coisa |
| **Hexis** | Disposição estável de caráter |
| **Dikaiosyne** | Justiça, virtude completa |
| **Sophrosyne** | Temperança, autodomínio |
| **Andreia** | Coragem no contexto apropriado |
| **Ethos** | Caráter adquirido por hábito |
| **Prática** (MacIntyre) | Atividade cooperativa com bens internos |
| **Bens Internos** | Realizações intrínsecas a uma prática |
| **Capacidades** (Nussbaum) | O que uma pessoa é capaz de ser e fazer |

## Exercícios

1. **Doutrina do Meio**: Para cada uma das seguintes situações de IA, identifique: (a) a virtude relevante, (b) o excesso, (c) a deficiência, (d) o meio termo:
   - Um sistema de recomendação sugere conteúdo
   - Um carro autônomo decide quão agressivamente dirigir
   - Um chatbot equilibra utilidade com privacidade

2. **Virtudes de IA**: Escolha três papéis diferentes de IA (assistente, moderador, tutor) e proponha cinco virtudes específicas para cada um. Justifique com referência à função própria de cada papel.

3. **Implementação de Phronesis**: Implemente um sistema de ponderação de virtudes que, dado um contexto, determine qual virtude deve ter precedência. Use o framework de McDowell (1979) sobre "silencing" de razões.

4. **Crítica Situacionista**: Analise um caso real de viés em IA (ex: COMPAS, Amazon hiring). A ética das virtudes explicaria o problema melhor que consequencialismo ou deontologia?

5. **Simulação Aristotélica**: Crie uma simulação onde um agente RL é treinado com recompensa baseada em múltiplas virtudes. Compare com um agente treinado por recompensa única.

6. **MacIntyre na Prática**: Escolha uma prática de engenharia de software e identifique: bens internos, bens externos, padrões de excelência, e as virtudes necessárias para alcançar os bens internos.

## Referências

- Annas, J. (2011). *Intelligent Virtue*. Oxford University Press.
- Anscombe, G. E. M. (1958). "Modern Moral Philosophy." *Philosophy*, 33(124), 1-19.
- Aristotle. *Nicomachean Ethics*. (trad. Ross, W. D. / Irwin, T.)
- Doris, J. (2002). *Lack of Character: Personality and Moral Behavior*. Cambridge University Press.
- Foot, P. (1978). *Virtues and Vices*. Oxford University Press.
- Harman, G. (1999). "Moral Philosophy Meets Social Psychology." *Proceedings of the Aristotelian Society*, 99, 315-331.
- Hursthouse, R. (1999). *On Virtue Ethics*. Oxford University Press.
- MacIntyre, A. (1981). *After Virtue*. University of Notre Dame Press.
- McDowell, J. (1979). "Virtue and Reason." *The Monist*, 62(3), 331-350.
- Nussbaum, M. (1988). "Non-Relative Virtues: An Aristotelian Approach." *Midwest Studies in Philosophy*, 13, 32-53.
- Nussbaum, M. (2006). *Frontiers of Justice*. Harvard University Press.
- Slote, M. (2001). *Morals from Motives*. Oxford University Press.
- Swanton, C. (2003). *Virtue Ethics: A Pluralistic View*. Oxford University Press.
- Vallor, S. (2016). *Technology and the Virtues*. Oxford University Press.
- Whitby, B. (2008). "Sometimes It's Hard to Be a Robot." *AI & Society*, 22(4), 485-493.
- Williams, B. (1985). *Ethics and the Limits of Philosophy*. Harvard University Press.

[[Conhecimento-Geral/Etica/INDEX|← Voltar ao índice de Ética]]
