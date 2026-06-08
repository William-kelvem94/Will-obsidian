---
title: "Consequencialismo"
area: "Ética"
related: ["Utilitarismo", "Responsabilidade", "Deontologia", "Etica-das-Virtudes"]
embeddings_model: "all-MiniLM-L6-v2"
tags: [conhecimento, conceito, etica, consequencialismo, utilitarismo, filosofia-moral]
updated: 2026-05-16
---

# Consequencialismo

## Visão Geral

O consequencialismo é uma família de teorias éticas normativas que afirmam que o valor moral de uma ação é determinado exclusivamente por suas consequências. Em sua formulação mais geral:

$$
\text{Valor Moral}(A) = f(\text{Consequências}(A))
$$

Onde $f$ é uma função de avaliação que mapeia estados de coisas resultantes para valores morais. A ação moralmente correta é aquela que produz o melhor estado de coisas global, de acordo com algum critério de "melhor".

Diferentemente da [[04-Conhecimentos/07-Humanidades/Etica/Deontologia|Deontologia]], que julga ações por sua conformidade a regras ou deveres, e da [[04-Conhecimentos/07-Humanidades/Etica/Etica-das-Virtudes|Ética das Virtudes]], que foca no caráter do agente, o consequencialismo olha exclusivamente para os resultados produzidos.

## Fundamentação Histórica

### Antecedentes Clássicos

Embora o consequencialismo moderno seja associado ao utilitarismo, elementos de pensamento consequencialista aparecem em diversas tradições:

- **Epicuro (341–270 a.C.)**: O hedonismo epicurista afirmava que o prazer é o único bem intrínseco e a dor o único mal.
- **Mozi (470–391 a.C.)**: Filósofo chinês que propunha avaliar ações por seu benefício ao povo.
- **Thomas Hobbes (1588–1679)**: O contrato social é justificado por suas consequências benéficas (paz e segurança).

### Utilitarismo Clássico

#### Jeremy Bentham (1748–1832)

Bentham é geralmente creditado como o fundador do utilitarismo moderno. Em *An Introduction to the Principles of Morals and Legislation* (1789), ele estabeleceu o princípio da **maior felicidade**:

> "A natureza colocou a humanidade sob o governo de dois senhores soberanos: a dor e o prazer. Cabe a eles indicar o que devemos fazer."

Bentham propôs o **cálculo hedônico** (felicific calculus) para medir o valor moral de uma ação com base em sete dimensões:

1. **Intensidade**: Quão forte é o prazer ou dor?
2. **Duração**: Por quanto tempo?
3. **Certeza**: Qual a probabilidade de ocorrer?
4. **Proximidade**: Quão imediato?
5. **Fecundidade**: Quantos prazeres adicionais gerará?
6. **Pureza**: Qual a probabilidade de produzir dor?
7. **Extensão**: Quantas pessoas serão afetadas?

```python
import numpy as np

class HedonicCalculus:
    """
    Implementação conceitual do cálculo hedônico de Bentham.
    """
    def __init__(self):
        self.dimensions = [
            'intensity', 'duration', 'certainty', 
            'proximity', 'fecundity', 'purity', 'extent'
        ]
    
    def evaluate_action(self, action, stakeholders):
        """
        Avalia uma ação calculando utilidade total.
        Formulação moderna: U = Σ w_i * u_i
        """
        total_utility = 0
        evaluations = []
        
        for stakeholder in stakeholders:
            pleasure = self._calculate_pleasure(action, stakeholder)
            pain = self._calculate_pain(action, stakeholder)
            net_utility = pleasure - pain
            total_utility += net_utility
            
            evaluations.append({
                'stakeholder': stakeholder.name,
                'pleasure': pleasure,
                'pain': pain,
                'net': net_utility
            })
        
        return {
            'total_utility': total_utility,
            'per_stakeholder': evaluations,
            'is_moral': total_utility > 0
        }
    
    def _calculate_pleasure(self, action, stakeholder):
        """Calcula prazer total da ação para o stakeholder"""
        scores = {}
        for dim in self.dimensions[:6]:  # exclude 'extent'
            score = getattr(stakeholder, f'{dim}_pleasure')(action)
            scores[dim] = score
        
        # Fórmula hedônica
        pleasure = (
            scores['intensity'] * scores['duration'] *
            scores['certainty'] * scores['proximity'] *
            (1 + scores['fecundity']) * (1 - scores['purity'])
        )
        return pleasure * stakeholder.count
    
    def _calculate_pain(self, action, stakeholder):
        """Calcula dor total da ação para o stakeholder"""
        scores = {}
        for dim in self.dimensions[:6]:
            score = getattr(stakeholder, f'{dim}_pain')(action)
            scores[dim] = score
        
        pain = (
            scores['intensity'] * scores['duration'] *
            scores['certainty'] * scores['proximity']
        )
        return pain * stakeholder.count
```

#### John Stuart Mill (1806–1873)

Mill refinou o utilitarismo benthamita em *Utilitarianism* (1863). Suas contribuições principais:

1. **Distinção qualitativa entre prazeres**: "É melhor ser um ser humano insatisfeito do que um porco satisfeito; é melhor ser Sócrates insatisfeito do que um tolo satisfeito." Mill argumentou que prazeres intelectuais e morais são qualitativamente superiores a prazeres meramente físicos.

2. **Prova do utilitarismo**: Mill tentou provar que a utilidade é o fundamento da moralidade:
   - Cada pessoa deseja sua própria felicidade (desejabilidade individual)
   - A felicidade geral é desejável para a soma de todas as pessoas (princípio de universalização)
   - Logo, a felicidade geral é o padrão da moralidade

3. **Proteção de direitos**: Mill argumentou que direitos individuais são protegidos pelo utilitarismo porque violá-los reduz a confiança social e o bem-estar geral.

### Utilitarismo Contemporâneo

#### Peter Singer (1946–)

Singer, em *Practical Ethics* (1979) e *The Expanding Circle* (1981), defende um utilitarismo de preferências que:

1. **Expande o círculo moral**: Inclui animais sencientes na consideração moral.
2. **Princípio de igual consideração de interesses**: Interesses similares merecem consideração similar, independentemente de espécie, raça ou gênero.
3. **Obrigação de doação efetiva**: Se podemos evitar que algo ruim aconteça sem sacrificar algo de importância moral comparável, devemos fazê-lo.

```python
class PreferenceUtilitarianism:
    """
    Modelo de utilitarismo de preferências (Singer, Hare).
    """
    def __init__(self, sentient_beings):
        self.beings = sentient_beings  # Todos os seres sencientes
    
    def evaluate_action(self, action):
        """
        Avalia ação por sua capacidade de satisfazer preferências.
        """
        utility = 0
        for being in self.beings:
            # Preferências do ser são ponderadas igualmente
            preference_satisfaction = being.evaluate_preference(action)
            utility += preference_satisfaction * being.moral_weight()
        
        # Princípio de igual consideração
        # Todos os seres com capacidade de sofrer têm o mesmo peso moral
        return utility
    
    def calculate_effective_donation(self, income, donation_pct=0.1):
        """
        Aplicação do princípio de doação efetiva de Singer.
        Calcula o impacto moral de doar vs consumir.
        """
        donation = income * donation_pct
        
        # Custo de oportunidade moral
        charity_impact_per_dollar = 0.95  # GiveWell estimativas
        consumption_impact_per_dollar = 0.1  # Utilidade marginal decrescente
        
        charity_utility = donation * charity_impact_per_dollar
        consumption_loss = donation * consumption_impact_per_dollar
        
        net_moral_gain = charity_utility - consumption_loss
        
        return {
            'donation': donation,
            'charity_utility': charity_utility,
            'consumption_loss': consumption_loss,
            'net_gain': net_moral_gain,
            'should_donate': net_moral_gain > 0
        }
```

## Variedades de Consequencialismo

### Utilitarismo de Ato (Act Utilitarianism)

**Definição**: Cada ação individual é julgada diretamente pelo princípio da utilidade.

$$
\text{Correto}(A) \iff U(A) \geq U(B) \ \forall B \in \mathcal{A}
$$

Onde $U(A)$ é a utilidade total resultante da ação $A$ e $\mathcal{A}$ é o conjunto de ações alternativas.

**Críticas**:
- **Carga computacional**: Calcular consequências de cada ação em tempo real.
- **Violação de direitos**: Pode justificar violações de direitos se o cálculo utilitário favorecer.
- **Inconsistência prática**: Ações aparentemente imorais podem ser justificadas.

### Utilitarismo de Regra (Rule Utilitarianism)

**Definição**: Ações são julgadas por sua conformidade a regras que, se universalmente seguidas, maximizariam a utilidade.

$$
\text{Correto}(A) \iff A \text{ está em conformidade com } R
$$

Onde $R$ é uma regra tal que $\forall x, \text{seguir}(R, x)$ maximiza utilidade agregada.

**Vantagens sobre utilitarismo de ato**:
- Evita violações de direitos individuais.
- Fornece guias práticos para ação.
- Mais consistente com intuições morais comuns.

```python
class RuleUtilitarianism:
    """
    Utilitarismo de regra: avalia regras pela utilidade de sua adoção universal.
    """
    def __init__(self):
        self.rules = {}
        self.rule_utilities = {}
    
    def evaluate_rule(self, rule, world_simulator, num_simulations=1000):
        """
        Avalia uma regra simulando sua adoção universal.
        """
        total_utility = 0
        
        for _ in range(num_simulations):
            sim = world_simulator.run_with_rule(rule)
            total_utility += sim.total_welfare()
        
        avg_utility = total_utility / num_simulations
        self.rule_utilities[rule.name] = avg_utility
        return avg_utility
    
    def action_is_correct(self, action, rule_set):
        """
        Ação correta se conforme à regra com maior utilidade esperada.
        """
        best_rule = max(rule_set, key=lambda r: self.rule_utilities.get(r.name, 0))
        return best_rule.applies_to(action) and best_rule.is_satisfied(action)
    
    def candidate_rules(self):
        """
        Exemplos de regras candidatas para avaliação utilitária de regra.
        """
        return [
            Rule("Não matar", "Não tirar a vida humana intencionalmente"),
            Rule("Não mentir", "Não enganar intencionalmente"),
            Rule("Ajudar em emergências", 
                 "Prestar assistência quando o custo é baixo e o benefício alto"),
            Rule("Cumprir promessas", "Honrar compromissos assumidos"),
            Rule("Respeitar propriedade", "Não tomar o que pertence a outros"),
        ]

class Rule:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def applies_to(self, action):
        return True
    
    def is_satisfied(self, action):
        return action.adheres_to(self.name)
```

### Utilitarismo de Preferência

O utilitarismo de preferência (Hare, 1981; Singer, 1979) substitui o prazer/pela satisfação de preferências como a utilidade basal:

$$
U(A) = \sum_{i} w_i \cdot S_i(A)
$$

Onde $S_i(A)$ é a satisfação das preferências do indivíduo $i$ causada por $A$, e $w_i$ é o peso moral.

**Vantagem teórica**: Evita a acusação de que o hedonismo reduz toda experiência humana a sensações brutas. Permite que preferências sobre estados complexos (liberdade, conhecimento, arte) sejam contadas.

### Consequencialismo Negativo

Defende que o objetivo moral primário é **minimizar sofrimento** em vez de maximizar felicidade. Karl Popper sugeriu:

> "Do ponto de vista moral, não podemos colocar a maximização da felicidade em pé de igualdade com a minimização do sofrimento."

Formalmente:

$$
\text{Melhor Estado} = \arg\min_{S} \sum_{i} \text{Sofrimento}_i(S)
$$

## Críticas e Problemas

### 1. O Monstro da Utilidade (Utility Monster)

Originalmente proposto por Nozick (1974) como crítica ao utilitarismo: se existe um ser que obtém utilidade imensamente maior de recursos do que outros, o cálculo utilitário exigiria alocar **todos** os recursos a esse monstro.

```
Recursos: 100 unidades
Pessoa A: utilidade marginal por unidade = 1
Monstro:  utilidade marginal por unidade = 1000

Cálculo utilitário:
- Dar 100 para A: U = 100 * 1 = 100
- Dar 100 para Monstro: U = 100 * 1000 = 100,000
- Distribuir igualmente: U = 50*1 + 50*1000 = 50,050

=> Utilitarismo prefere Monstro receber tudo
```

### 2. Exigência Excessiva (Demandingness Objection)

O consequencialismo parece exigir que **toda** ação seja otimizada para o bem máximo, não deixando espaço para projetos pessoais, relacionamentos ou lazer que não maximizem utilidade.

**Resposta de Singer**: Devemos doar tudo acima do necessário para sobrevivência. **Crítica**: Isso é excessivamente exigente e alienante.

### 3. Problema dos Direitos

O consequencialismo parece não levar direitos individuais a sério. Se violar o direito de uma pessoa salva muitas, o cálculo pode justificar a violação.

**Exemplo clássico**: O xerife que enquadra um inocente para evitar um linchamento:
- Utilitarismo de ato: justifica (mais vidas salvas)
- Intuição comum: injusto

### 4. Problema da Medição

Como medir e comparar utilidade interpessoalmente? Não há escala cardinal compartilhada para experiências subjetivas.

```python
class UtilityMeasurementProblem:
    """
    Demonstração dos problemas de mensuração de utilidade.
    """
    def __init__(self):
        # Sem acesso direto aos estados mentais de outros
        pass
    
    def ordinal_ranking(self, alternatives, persons):
        """
        Agregação de preferências ordinais: impossibilidade de Arrow.
        Arrow (1951): não existe função de bem-estar social que satisfaça
        todas as condições razoáveis simultaneamente.
        """
        # Preferências individuais (ordinais)
        preferences = {
            p: p.rank(alternatives) 
            for p in persons
        }
        
        # Tentativa de agregação
        # Problema: ciclo de Condorcet possível
        return self._condorcet_check(preferences, alternatives)
    
    def _condorcet_check(self, preferences, alternatives):
        """Verifica ciclo de votação (Condorcet)"""
        victories = {a: 0 for a in alternatives}
        for a in alternatives:
            for b in alternatives:
                if a != b:
                    # Conta votos: quantos preferem a sobre b
                    a_over_b = sum(
                        1 for p in preferences.values()
                        if p[a] > p[b]
                    )
                    if a_over_b > len(preferences) / 2:
                        victories[a] += 1
        
        winner = max(victories, key=victories.get)
        has_cycle = max(victories.values()) < len(alternatives) - 1
        
        return {
            'winner': winner,
            'victory_counts': victories,
            'has_condorcet_cycle': has_cycle
        }
```

### 5. Problema da Separação

Rawls (1971) argumentou que o utilitarismo não leva a sério a **separabilidade das pessoas**. Ao agregar utilidade, trata a sociedade como um único indivíduo, desrespeitando a distinção entre pessoas.

### 6. Consequências Imprevisíveis

O problema epistêmico: nunca conhecemos todas as consequências de uma ação, especialmente a longo prazo. Isso torna o cálculo utilitário inviável na prática.

## Aplicações em Ética de IA

### Problema da Função de Utilidade

Em aprendizado por reforço, especificamos uma função de recompensa $R(s, a)$ que é essencialmente uma função de utilidade. Todos os problemas do consequencialismo filosófico se manifestam aqui:

```python
import numpy as np

class AIUtilityFunction:
    """
    Função de utilidade para agente de IA com problemas consequencialistas.
    """
    def __init__(self, weights):
        self.weights = weights  # Pesos para diferentes objetivos
    
    def __call__(self, state):
        # Problema 1: Medição
        welfare = self._measure_welfare(state)
        
        # Problema 2: Agregação
        if self.aggregation == 'sum':  # Utilitarismo total
            return np.sum(welfare)
        elif self.aggregation == 'average':  # Utilitarismo médio
            return np.mean(welfare)
        elif self.aggregation == 'minimax':  # Rawlsiano
            return np.min(welfare)
        
        # Problema 3: Direitos vs Utilidade
        if self._violates_rights(state):
            # Como modelar direitos na função?
            return -np.inf  # Opção 1: proibição absoluta
            # ou penalty ajustável
        
        return np.dot(self.weights, welfare)
    
    def _measure_welfare(self, state):
        """
        Medição de bem-estar: proxy imperfeito.
        """
        # Podemos medir renda, saúde, educação...
        # Mas felicidade subjetiva é inacessível
        return np.array([
            state.income,
            state.health_score,
            state.education_level
        ])
```

### Dilemas Éticos em Sistemas Autônomos

O consequencialismo em IA apresenta dilemas específicos:

1. **Veículos autônomos e o problema do bonde**: A programação utilitária pode sacrificar um pedestre para salvar mais ocupantes.
2. **Sistemas de recomendação**: Maximizar engajamento (consequência) pode radicalizar usuários.
3. **Alocação de recursos médicos**: Priorizar pacientes com maior expectativa de sobrevivência.
4. **Justiça algorítmica**: Viés sistêmico como consequência de otimização de métricas.

```python
class AutonomousVehicleEthics:
    """
    Dilemas éticos de veículos autônomos sob diferentes frameworks.
    """
    def __init__(self):
        self.consequentialist = True
    
    def utilitarian_decision(self, scenario):
        """
        Decisão utilitária: minimizar dano total.
        """
        outcomes = {
            'brake': self._simulate_brake(scenario),
            'swerve_left': self._simulate_swerve(scenario, 'left'),
            'swerve_right': self._simulate_swerve(scenario, 'right')
        }
        
        best_outcome = min(outcomes, key=lambda o: self._total_harm(outcomes[o]))
        
        return {
            'decision': best_outcome,
            'expected_harm': self._total_harm(outcomes[best_outcome]),
            'victims': outcomes[best_outcome]['victims']
        }
    
    def _total_harm(self, outcome):
        """
        Cálculo de dano total.
        Utiliza anos de vida perdidos (YLL) como métrica.
        """
        total_yll = 0
        for victim in outcome['victims']:
            # Anos de vida perdidos por vítima
            yll = victim.life_expectancy - victim.age
            total_yll += yll * victim.number
        
        # Dano moral (sofrimento, trauma)
        moral_damage = outcome['survivor_trauma'] * 0.1 * total_yll
        
        return total_yll + moral_damage
    
    def deontological_decision(self, scenario):
        """
        Contraste: decisão deontológica proíbe matar intencionalmente.
        """
        # Princípio de não causar dano direto
        # O veículo não pode escolher ATIVAMENTE matar alguém
        # Portanto: frear (ação passiva) é preferível a desviar (ação ativa)
        
        outcomes = {
            'brake': self._simulate_brake(scenario),
            'swerve_left': self._simulate_swerve(scenario, 'left'),
            'swerve_right': self._simulate_swerve(scenario, 'right')
        }
        
        # Só frear é permitido (sem ação de desviar que cause morte)
        return {
            'decision': 'brake',
            'reason': 'Desviar ativamente viola o dever de não matar',
            'consequences': outcomes['brake']
        }
```

## Glossário

| Termo | Definição |
|-------|-----------|
| **Consequencialismo** | Teoria ética que avalia ações por suas consequências |
| **Utilitarismo** | Variante que maximiza utilidade (prazer, preferência, bem-estar) |
| **Utilitarismo de Ato** | Cada ação é avaliada individualmente por sua utilidade |
| **Utilitarismo de Regra** | Ações avaliadas por conformidade a regras úteis |
| **Utilitarismo de Preferência** | Utilidade = satisfação de preferências |
| **Monstro da Utilidade** | Ser hipotético com capacidade desproporcional de utilidade |
| **Cálculo Hedônico** | Método benthamita de medir prazer e dor |
| **Exigência Excessiva** | Crítica: utilitarismo exige demais dos agentes morais |
| **Princípio de Utilidade** | Ação correta maximiza felicidade geral |
| **Utilidade Marginal** | Mudança na utilidade por unidade adicional de recurso |

## Exercícios

1. **Comparação**: Compare utilitarismo de ato e de regra aplicados à decisão de um carro autônomo em um dilema de bonde. Sob qual framework a decisão difere?

2. **Implementação**: Implemente uma simulação de Monte Carlo para comparar diferentes funções de utilidade (total, média, Rawlsiana) em uma sociedade simulada com 100 agentes.

3. **Crítica**: Responda à objeção do "Monstro da Utilidade" de Nozick. O utilitarismo pode acomodar direitos individuais?

4. **Aplicação em IA**: Projete uma função de recompensa para um sistema de triagem médica que (a) maximize vidas salvas e (b) evite violar direitos de pacientes. Onde o consequencialismo e a deontologia entram em conflito?

5. **Análise de Singer**: O argumento de Singer sobre doação efetiva implica que profissionais de alta renda (ex: médicos, engenheiros) devem doar a maior parte de sua renda para caridade. Você concorda? Use ferramentas formais para defender sua posição.

6. **Simulação**: Crie um ambiente de gridworld onde um agente RL com função de recompensa utilitária (maximizar soma de recompensas para todos os agentes) pode levar a resultados injustos. Que modificações na função de recompensa corrigiriam isso?

## Referências

- Arrow, K. (1951). *Social Choice and Individual Values*. Yale University Press.
- Bentham, J. (1789). *An Introduction to the Principles of Morals and Legislation*.
- Hare, R. M. (1981). *Moral Thinking: Its Levels, Method, and Point*. Oxford University Press.
- Mill, J. S. (1863). *Utilitarianism*.
- Nozick, R. (1974). *Anarchy, State, and Utopia*. Basic Books.
- Parfit, D. (1984). *Reasons and Persons*. Oxford University Press.
- Popper, K. (1945). *The Open Society and Its Enemies*. Routledge.
- Rawls, J. (1971). *A Theory of Justice*. Harvard University Press.
- Scheffler, S. (1982). *The Rejection of Consequentialism*. Oxford University Press.
- Sidgwick, H. (1874). *The Methods of Ethics*.
- Singer, P. (1979). *Practical Ethics*. Cambridge University Press.
- Singer, P. (1981). *The Expanding Circle*. Princeton University Press.
- Smart, J. J. C. & Williams, B. (1973). *Utilitarianism: For and Against*. Cambridge University Press.
- Williams, B. (1985). *Ethics and the Limits of Philosophy*. Harvard University Press.

[[04-Conhecimentos/07-Humanidades/Etica/INDEX|← Voltar ao índice de Ética]]
