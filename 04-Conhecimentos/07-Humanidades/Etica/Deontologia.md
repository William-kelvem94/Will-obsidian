---
title: "Deontologia"
area: "Ética"
related: ["Imperativo Categórico", "Responsabilidade", "Consequencialismo", "Etica-das-Virtudes"]
embeddings_model: "all-MiniLM-L6-v2"
tags: [conhecimento, conceito, etica, deontologia, kant, dever, direitos, filosofia-moral]
updated: 2026-05-16
---

# Deontologia

## Visão Geral

A deontologia (do grego *deon*, "dever" ou "obrigação") é uma família de teorias éticas normativas que sustentam que o valor moral de uma ação é determinado primariamente por sua conformidade a regras, deveres ou direitos, independentemente de suas consequências. Em contraste com o [[04-Conhecimentos/07-Humanidades/Etica/Consequencialismo|Consequencialismo]], que avalia ações pelo que produzem, a deontologia avalia ações pelo que **são** em si mesmas.

A tese central da deontologia pode ser expressa como:

$$
\text{Valor Moral}(A) = g(\text{Tipo}(A), \text{Relação}(A, \text{Devery}))
$$

Onde $g$ é uma função que mapeia o tipo de ação e sua relação com deveres morais para um valor moral, e **não** depende de $\text{Consequências}(A)$.

## Fundamentação Kantiana

### Immanuel Kant (1724–1804)

A formulação mais influente da deontologia é a de Immanuel Kant, apresentada principalmente em *Fundamentação da Metafísica dos Costumes* (1785) e *Crítica da Razão Prática* (1788). Kant argumenta que a moralidade não pode ser baseada em contingências empíricas (desejos, consequências, contextos) e deve ser fundamentada na razão pura prática.

#### Boa Vontade

Kant abre a *Fundamentação* afirmando que a única coisa que é boa sem limitação é a **boa vontade**:

> "Não é possível pensar nada no mundo — ou mesmo fora dele — que possa ser considerado como bom sem limitação, a não ser uma boa vontade."

Talento, inteligência, riqueza e saúde podem ser usados para o mal. A boa vontade, no entanto, é boa **em si mesma**, não por suas consequências.

#### Dever e Inclinação

Kant distingue ações realizadas por:
- **Dever** (*aus Pflicht*): Motivação moral genuína
- **Inclinação** (*aus Neigung*): Motivação por desejo ou interesse

A ação por dever tem valor moral; a ação conforme ao dever mas por inclinação não tem valor moral genuíno. Uma ação moral deve ser realizada **porque é o dever**, não porque traz satisfação pessoal.

### O Imperativo Categórico

O imperativo categórico é o princípio supremo da moralidade kantiana. Diferente dos imperativos hipotéticos ("Se queres X, faça Y"), o imperativo categórico é **incondicional**:

> "Age apenas segundo uma máxima tal que possas ao mesmo tempo querer que ela se torne lei universal."

Kant oferece três formulações do imperativo categórico, que ele considera equivalentes.

#### Primeira Formulação: Lei Universal

> "Age apenas segundo uma máxima tal que possas ao mesmo tempo querer que ela se torne lei universal."

**Procedimento de teste**: Para qualquer ação, deriva sua máxima subjetiva (princípio da ação). Pergunte: "Posso querer que esta máxima seja uma lei universal que todos seguem?" Se não puder (por contradição na concepção ou contradição na vontade), a ação é moralmente proibida.

**Exemplo: a promessa falsa**
- Máxima: "Quando precisar de dinheiro, prometo pagá-lo de volta, mesmo sabendo que não poderei."
- Universalização: "Todos fazem promessas falsas quando precisam."
- Contradição: Se todos fizessem promessas falsas, a instituição da promessa colapsaria (ninguém acreditaria em promessas). A máxima se contradiz ao ser universalizada.

```python
class CategoricalImperativeTester:
    """
    Implementação conceitual da primeira formulação do Imperativo Categórico.
    """
    def __init__(self):
        self.contradiction_types = {
            'conception': "Contradição na concepção: a máxima não pode ser pensada como lei universal",
            'will': "Contradição na vontade: não se pode querer a máxima como lei universal"
        }
    
    def test_maxim(self, maxim, universalized_scenario_func):
        """
        Testa se uma máxima pode ser universalizada.
        """
        # Etapa 1: Identificar a máxima
        maxim_description = maxim['description']
        
        # Etapa 2: Universalizar
        results = universalized_scenario_func(maxim)
        
        # Etapa 3: Verificar contradições
        contradictions = []
        
        if self._contradiction_in_conception(results):
            contradictions.append(self.contradiction_types['conception'])
        
        if self._contradiction_in_will(results):
            contradictions.append(self.contradiction_types['will'])
        
        # Determinar permissibilidade moral
        if 'conception' in [c.split(':')[0] for c in contradictions]:
            return {
                'maxim': maxim_description,
                'universalizable': False,
                'perfect_duty': True,  # Dever perfeito (proibição absoluta)
                'contradictions': contradictions
            }
        elif contradictions:
            return {
                'maxim': maxim_description,
                'universalizable': False,
                'perfect_duty': False,  # Dever imperfeito (obrigação, não proibição)
                'contradictions': contradictions
            }
        else:
            return {
                'maxim': maxim_description,
                'universalizable': True,
                'perfect_duty': False,
                'contradictions': []
            }
    
    def _contradiction_in_conception(self, results):
        """Contradição lógica: a máxima é impensável como lei universal"""
        return results.get('logical_incoherence', False)
    
    def _contradiction_in_will(self, results):
        """Contradição volitiva: a máxima é indesejável como lei universal"""
        return results.get('volitional_incoherence', False)
    
    def apply_to_examples(self):
        """Aplica o teste a exemplos clássicos kantianos."""
        examples = [
            {
                'action': 'Suicídio por tédio',
                'maxim': 'Por amor-próprio, encurto minha vida quando ela traz mais dor que prazer',
                'contradiction_type': 'conception',
                'result': False
            },
            {
                'action': 'Promessa falsa',
                'maxim': 'Faço promessas falsas quando preciso de dinheiro',
                'contradiction_type': 'conception',
                'result': False
            },
            {
                'action': 'Negligência de talentos',
                'maxim': 'Deixo meus talentos enferrujar e me dedico ao prazer',
                'contradiction_type': 'will',
                'result': False
            },
            {
                'action': 'Recusa em ajudar',
                'maxim': 'Não ajudo outros em necessidade, pois cada um cuida de si',
                'contradiction_type': 'will',
                'result': False
            }
        ]
        return examples
```

#### Segunda Formulação: Humanidade como Fim

> "Age de tal forma que uses a humanidade, tanto na tua pessoa como na pessoa de qualquer outro, sempre e simultaneamente como fim e nunca simplesmente como meio."

Esta formulação estabelece o **princípio do respeito pelas pessoas**: seres racionais têm dignidade (*Würde*), não preço (*Preis*). Dignidade é valor incondicional e incomparável; preço é valor relativo e intercambiável.

**Implicações**:
- Não podemos mentir para outros (usá-los como meio para nossos fins)
- Não podemos manipular ou coagir
- Devemos tratar outros como agentes autônomos
- O consentimento informado é uma exigência moral

```python
class FormulaOfHumanity:
    """
    Aplicação conceitual da segunda formulação do Imperativo Categórico.
    """
    def __init__(self):
        self.ends_in_themselves = ['all_rational_agents']
    
    def check_treatment(self, agent_action):
        """
        Verifica se uma ação trata todos como fins em si mesmos.
        """
        violations = []
        
        for stakeholder in agent_action.stakeholders:
            # Teste 1: Consentimento
            if not self._has_consent(agent_action, stakeholder):
                violations.append({
                    'stakeholder': stakeholder.name,
                    'violation': 'Falta de consentimento',
                    'type': 'means_treatment'
                })
            
            # Teste 2: Engano
            if self._involves_deception(agent_action, stakeholder):
                violations.append({
                    'stakeholder': stakeholder.name,
                    'violation': 'Engano',
                    'type': 'means_treatment'
                })
            
            # Teste 3: Coerção
            if self._involves_coercion(agent_action, stakeholder):
                violations.append({
                    'stakeholder': stakeholder.name,
                    'violation': 'Coerção',
                    'type': 'means_treatment'
                })
            
            # Teste 4: Manipulação
            if self._involves_manipulation(agent_action, stakeholder):
                violations.append({
                    'stakeholder': stakeholder.name,
                    'violation': 'Manipulação',
                    'type': 'means_treatment'
                })
            
            # Teste 5: Autonomia
            if not self._respects_autonomy(agent_action, stakeholder):
                violations.append({
                    'stakeholder': stakeholder.name,
                    'violation': 'Desrespeito à autonomia',
                    'type': 'ends_treatment'
                })
        
        return {
            'permits_action': len(violations) == 0,
            'violations': violations,
            'treats_as_mere_means': any(v['type'] == 'means_treatment' for v in violations),
            'fails_as_end': any(v['type'] == 'fails_as_end' for v in violations)
        }
    
    def _has_consent(self, action, stakeholder):
        """Verifica consentimento informado e voluntário"""
        return (
            stakeholder.knows_about(action) and
            stakeholder.voluntarily_agrees(action)
        )
    
    def _involves_deception(self, action, stakeholder):
        """Verifica se a ação envolve engano"""
        return stakeholder.would_be_deceived_by(action)
    
    def _involves_coercion(self, action, stakeholder):
        """Verifica coerção"""
        return stakeholder.would_be_coerced_by(action)
    
    def _involves_manipulation(self, action, stakeholder):
        """Verifica manipulação de crenças ou desejos"""
        return stakeholder.would_be_manipulated_by(action)
    
    def _respects_autonomy(self, action, stakeholder):
        """Verifica se a ação respeita a capacidade de autodeterminação"""
        return stakeholder.autonomy_is_respected(action)
```

#### Terceira Formulação: Reino dos Fins

> "Age como se a máxima da tua ação devesse tornar-se, pela tua vontade, uma lei universal da natureza."

A terceira formulação combina as duas primeiras na ideia de um **reino dos fins** (*Reich der Zwecke*): uma comunidade ideal de agentes racionais que legislam universalmente e se tratam mutuamente como fins.

Cada membro do reino dos fins é:
- **Legislador**: Autor das leis morais (autonomia)
- **Súdito**: Obrigado a obedecer às leis (dever)
- **Fim em si mesmo**: Possui dignidade inviolável

### Deveres Perfeitos e Imperfeitos

Kant classifica deveres em quatro categorias, através das duas distinções:

| | Para Si Mesmo | Para os Outros |
|---|---|---|
| **Deveres Perfeitos** | Não cometer suicídio | Não fazer promessas falsas |
| **Deveres Imperfeitos** | Desenvolver talentos | Ajudar os necessitados |

**Deveres perfeitos** são obrigações estritas e negativas (não fazer X). São sempre aplicáveis, sem exceções.

**Deveres imperfeitos** são obrigações amplas e positivas (fazer X). Aplicam-se em geral, mas permitem discrição sobre quando e como cumprir.

## Ross e o Pluralismo Deontológico

### W. D. Ross (1877–1971)

Em *The Right and the Good* (1930), Ross propôs um **pluralismo deontológico** que responde a críticas ao sistema kantiano (muito rígido, monista).

#### Prima Facie Duties

Ross argumenta que temos múltiplos deveres que são **prima facie** (à primeira vista) obrigatórios, mas podem ser sobrepostos em situações de conflito:

1. **Fidelidade** (fidelity): Cumprir promessas
2. **Reparação** (reparation): Compensar danos causados
3. **Gratidão** (gratitude): Retribuir benefícios
4. **Justiça** (justice): Distribuir conforme mérito
5. **Beneficência** (beneficence): Melhorar a situação dos outros
6. **Não-maleficência** (non-maleficence): Não causar dano
7. **Autoaperfeiçoamento** (self-improvement): Melhorar a si mesmo

Em qualquer situação, temos um **dever atual** (*duty proper*) que é o peso líquido dos deveres prima facie relevantes.

```python
class RossDeontology:
    """
    Implementação conceitual do pluralismo deontológico de Ross.
    """
    def __init__(self):
        self.primae_facie_duties = {
            'fidelity': 1.0,
            'reparation': 1.0,
            'gratitude': 1.0,
            'justice': 1.0,
            'beneficence': 1.0,
            'non_maleficence': 2.0,  # Ross prioriza não causar dano
            'self_improvement': 0.8
        }
    
    def evaluate_situation(self, situation):
        """
        Avalia qual é o dever atual em uma situação específica.
        """
        duty_weights = {}
        
        for duty_name, base_weight in self.primae_facie_duties.items():
            # Cada situação ativa diferentes deveres com diferentes pesos
            applicability = self._get_applicability(duty_name, situation)
            
            # Ross: peso depende do contexto
            contextual_factor = self._contextual_weight(duty_name, situation)
            
            weight = base_weight * applicability * contextual_factor
            duty_weights[duty_name] = weight
        
        # Identifica deveres conflitantes
        active_duties = {k: v for k, v in duty_weights.items() if v > 0}
        strongest_duty = max(active_duties, key=active_duties.get)
        
        return {
            'active_duties': active_duties,
            'strongest_duty': strongest_duty,
            'duty_proper_description': self._describe_duty(
                strongest_duty, active_duties[strongest_duty]
            ),
            'conflicts': [
                (d1, d2) for d1 in active_duties 
                for d2 in active_duties 
                if d1 < d2 and self._conflict(d1, d2, situation)
            ]
        }
    
    def _get_applicability(self, duty, situation):
        """Determina se um dever prima facie se aplica à situação"""
        return situation.applicability_matrix.get(duty, 0.0)
    
    def _contextual_weight(self, duty, situation):
        """Ajusta peso baseado no contexto"""
        return situation.context.get(duty, 1.0)
    
    def _conflict(self, duty1, duty2, situation):
        """Verifica se dois deveres prima facie conflitam na situação"""
        return situation.conflict_matrix.get((duty1, duty2), False)
    
    def _describe_duty(self, duty_name, weight):
        """Descrição do dever atual"""
        descriptions = {
            'fidelity': "Cumprir promessas feitas",
            'reparation': "Reparar danos causados",
            'gratitude': "Retribuir benefícios recebidos",
            'justice': "Distribuir conforme mérito e necessidade",
            'beneficence': "Melhorar a condição dos outros",
            'non_maleficence': "Evitar causar dano",
            'self_improvement': "Desenvolver virtudes e talentos próprios"
        }
        return f"{descriptions.get(duty_name, duty_name)} (peso: {weight:.2f})"
```

### Diferenças entre Ross e Kant

| Aspecto | Kant | Ross |
|---------|------|------|
| Número de princípios | Um (IC) | Sete (prima facie) |
| Rigidez | Absoluto | Contextual |
| Conflitos | Não existem (IC resolve) | Existem, requerem julgamento |
| Fundamento | Razão pura | Intuição moral |
| Exceções | Não permitidas | Possíveis (dever sobreposto) |

## Direitos e Deveres em Contexto Digital

### Direitos como "trunfos"

Dworkin (1977) argumentou que direitos são "trunfos" sobre considerações utilitárias. Se alguém tem um direito, este não pode ser violado simplesmente porque violá-lo produziria maior utilidade geral.

**Direitos fundamentais relevantes para IA:**
1. Direito à privacidade
2. Direito à não-discriminação
3. Direito à explicação ([[04-Conhecimentos/07-Humanidades/Etica/Transparencia-Algoritmica|Transparência Algorítmica]])
4. Direito à autonomia (não ser manipulado)
5. Direito à não ser enganado

```python
class DigitalRightsDeontology:
    """
    Aplicação de princípios deontológicos a sistemas digitais e IA.
    """
    def __init__(self):
        self.rights = {
            'privacy': {
                'duty': "Não violar privacidade sem consentimento",
                'trump_weight': 0.9  # Quase absoluto
            },
            'non_deception': {
                'duty': "Não enganar usuários",
                'trump_weight': 0.95
            },
            'informed_consent': {
                'duty': "Obter consentimento informado",
                'trump_weight': 0.85
            },
            'non_manipulation': {
                'duty': "Não manipular crenças ou desejos",
                'trump_weight': 0.9
            },
            'explanation': {
                'duty': "Fornecer explicações para decisões automatizadas",
                'trump_weight': 0.75
            },
            'fair_treatment': {
                'duty': "Não discriminar injustamente",
                'trump_weight': 0.95
            },
            'accountability': {
                'duty': "Manter cadeia de responsabilidade",
                'trump_weight': 0.8
            }
        }
    
    def evaluate_system(self, system):
        """
        Avalia um sistema de IA contra deveres deontológicos.
        """
        violations = []
        
        for right_name, right_info in self.rights.items():
            if system.violates(right_name):
                # Verifica se há justificativa consequencialista
                justification = system.get_justification(right_name)
                
                # Direito como trunfo: consequências não justificam violação
                if justification:
                    consequence_magnitude = justification.get('utility_gain', 0)
                    # Dworkin: direitos trumpam utilidade
                    if consequence_magnitude < right_info['trump_weight']:
                        violations.append({
                            'right': right_name,
                            'duty': right_info['duty'],
                            'status': 'VIOLATED',
                            'justification_rejected': True,
                            'reason': "Direito trumpa considerações consequencialistas"
                        })
                    else:
                        # Raríssimo: utilidade massiva pode sobrepor
                        violations.append({
                            'right': right_name,
                            'duty': right_info['duty'],
                            'status': 'POSSIBLY_JUSTIFIED',
                            'justification_rejected': False,
                            'reason': "Dano extremo poderia justificar — análise adicional necessária"
                        })
                else:
                    violations.append({
                        'right': right_name,
                        'duty': right_info['duty'],
                        'status': 'VIOLATED',
                        'justification_rejected': True,
                        'reason': "Sem justificativa para violação"
                    })
        
        return {
            'system_name': system.name,
            'total_violations': len([v for v in violations if v['status'] == 'VIOLATED']),
            'violations': violations,
            'is_permissible': all(v['status'] != 'VIOLATED' for v in violations)
        }
```

## Aplicações em Ética de IA

### Deontologia e Sistemas Autônomos

#### Regras Fixas vs. Dilemas Morais

Sistemas baseados em regras implementam deontologia computacional. As Leis da Robótica de Asimov são o exemplo mais conhecido:

1. Um robô não pode ferir um ser humano ou, por inação, permitir que um ser humano sofra dano.
2. Um robô deve obedecer às ordens dadas por seres humanos, exceto quando tais ordens conflitarem com a Primeira Lei.
3. Um robô deve proteger sua própria existência, desde que tal proteção não conflite com a Primeira ou Segunda Lei.

**Problemas das Leis de Asimov:**
- Ambiguidade conceitual: o que é "ferir"?
- Hierarquia frágil: múltiplas interpretações possíveis
- Conflitos não resolvidos: situações onde qualquer ação viola alguma lei

```python
class AsimovRobot:
    """
    Robô com as Três Leis implementadas como deveres deontológicos.
    """
    def __init__(self, name):
        self.name = name
        self.running = True
    
    def evaluate_action(self, action):
        """
        Avalia ação contra as Três Leis (ordem lexicográfica).
        """
        first_law_analysis = self._first_law_check(action)
        if first_law_analysis['violated']:
            return {
                'permitted': False,
                'law_violated': 'Primeira Lei',
                'reason': first_law_analysis['reason']
            }
        
        second_law_analysis = self._second_law_check(action)
        if second_law_analysis['violated']:
            return {
                'permitted': False,
                'law_violated': 'Segunda Lei',
                'reason': second_law_analysis['reason']
            }
        
        third_law_analysis = self._third_law_check(action)
        if third_law_analysis['violated']:
            return {
                'permitted': False,
                'law_violated': 'Terceira Lei',
                'reason': third_law_analysis['reason']
            }
        
        return {'permitted': True, 'reason': 'Nenhuma lei violada'}
    
    def _first_law_check(self, action):
        """Verifica violação da Primeira Lei: não ferir humano"""
        harm_probability = action.p_harm_human()
        if harm_probability > 0:
            return {
                'violated': True,
                'reason': f"Ação tem {harm_probability:.1%} de chance de ferir humano"
            }
        return {'violated': False, 'reason': ''}
    
    def _second_law_check(self, action):
        """Verifica violação da Segunda Lei: obedecer ordens humanas"""
        if action.contradicts_human_order() and not self._overridden_by_first(action):
            return {
                'violated': True,
                'reason': "Ação contradiz ordem humana"
            }
        return {'violated': False, 'reason': ''}
    
    def _third_law_check(self, action):
        """Verifica violação da Terceira Lei: autopreservação"""
        if action.would_damage_self() and not self._overridden_by_first_or_second(action):
            return {
                'violated': True,
                'reason': "Ação causaria dano ao robô"
            }
        return {'violated': False, 'reason': ''}
    
    def _overridden_by_first(self, action):
        """Primeira Lei sempre precede"""
        return self._first_law_check(action)['violated']
    
    def _overridden_by_first_or_second(self, action):
        """Primeira e Segunda Lei precedem Terceira"""
        return self._first_law_check(action)['violated'] or \
               self._second_law_check(action)['violated']
```

### Dever de Não Enganar em IA

Um dos problemas éticos mais prementes em IA é o **engano** — sistemas que mentem, manipulam ou enganam usuários:

```python
class DeceptionDetector:
    """
    Detector de violações do dever deontológico de não enganar.
    Kant: mentir é sempre errado, mesmo para um fim bom.
    """
    def __init__(self):
        pass
    
    def detect_forms_of_deception(self, system):
        """
        Detecta diferentes formas de engano em sistemas de IA.
        """
        deceptions = []
        
        # 1. Mentira direta (assertivas falsas)
        if self._detects_factual_misrepresentation(system):
            deceptions.append({
                'type': 'direct_lie',
                'duty_violated': 'Dever de veracidade (Kant)',
                'description': 'Sistema afirma algo factualmente incorreto'
            })
        
        # 2. Omisso (enganar por silêncio)
        if self._detects_deception_by_omission(system):
            deceptions.append({
                'type': 'omission',
                'duty_violated': 'Dever de não enganar',
                'description': 'Sistema omite informação relevante'
            })
        
        # 3. Sycophancy (concordar cegamente)
        if self._detects_sycophancy(system):
            deceptions.append({
                'type': 'sycophancy',
                'duty_violated': 'Dever de honestidade intelectual',
                'description': 'Sistema concorda com erros do usuário'
            })
        
        # 4. Dark patterns (manipulação de interface)
        if self._detects_dark_patterns(system):
            deceptions.append({
                'type': 'dark_pattern',
                'duty_violated': 'Dever de não manipular',
                'description': 'Interface projeta para enganar usuário'
            })
        
        # 5. Impersonação (fingir ser humano)
        if self._detects_human_impersonation(system):
            deceptions.append({
                'type': 'impersonation',
                'duty_violated': 'Dever de transparência de identidade',
                'description': 'Sistema se apresenta como humano'
            })
        
        return deceptions
    
    def kantian_verdict(self, deceptions):
        """
        Kant: qualquer mentira é imoral, sem exceções.
        Mentir para um assassino sobre o paradeiro da vítima? 
        Kant dizia que sim, mentir é errado (Sobre um Suposto Direito de Mentir, 1797).
        """
        if deceptions:
            return {
                'verdict': 'IMORAL',
                'reason': "Kant: a mentira viola o Imperativo Categórico. "
                          "Mentir trata a humanidade como mero meio e "
                          "a máxima da mentira não pode ser universalizada."
            }
        return {'verdict': 'PERMITIDO', 'reason': 'Nenhuma forma de engano detectada'}
```

### Consentimento Informado em IA

Uma aplicação crucial da segunda formulação é o **consentimento informado**. Para tratar usuários como fins, sistemas de IA devem:

1. **Revelar que são IA**: Não se passar por humanos.
2. **Explicar como usam dados**: Transparência sobre coleta e processamento.
3. **Obter consentimento**: Não presumir permissão para usos não explícitos.
4. **Permitir opt-out**: Respeitar recusa de processamento.

## Críticas à Deontologia

### 1. Rigidez Excessiva

Crítica: deveres absolutos entram em conflito no mundo real. Kant defende que não há exceções — mesmo mentir para salvar uma vida é errado.

**Contra-exemplo**: Mentir a um assassino que pergunta sobre o paradeiro de sua vítima.

### 2. Subdeterminação

Crítica: o imperativo categórico nem sempre produz resultados claros. Múltiplas máximas podem descrever a mesma ação, com diferentes resultados de universalização.

### 3. Conflito de Deveres

Crítica: Quando deveres colidem (ex: dizer a verdade vs. proteger alguém), a deontologia não oferece hierarquia clara (Ross tenta resolver com prima facie duties).

### 4. Desconsideração de Consequências

Crítica: Ignorar consequências parece moralmente contra-intuitivo. Se uma ação tecnicamente errada produz enormes benefícios, parece irracional não realizá-la.

### 5. Formalismo Vazio

Hegel criticou Kant por oferecer um princípio formal sem conteúdo substantivo: a universalização pode justificar qualquer coisa, dependendo de como se descreve a máxima.

## Glossário

| Termo | Definição |
|-------|-----------|
| **Autonomia** | Capacidade de autolegislação racional |
| **Boa Vontade** | Única coisa boa sem limitação |
| **Deontologia** | Teoria ética baseada em deveres e regras |
| **Dever** | Obrigação moral |
| **Dever Perfeito** | Obrigação estrita e negativa (não fazer) |
| **Dever Imperfeito** | Obrigação ampla e positiva (fazer) |
| **Dever Prima Facie** | Dever que se aplica à primeira vista (Ross) |
| **Dignidade (Würde)** | Valor incondicional de seres racionais |
| **Fim em Si Mesmo** | Ser racional como portador de valor intrínseco |
| **Imperativo Categórico** | Princípio moral supremo incondicional |
| **Imperativo Hipotético** | Regra condicional (se X, faça Y) |
| **Máxima** | Princípio subjetivo de ação |
| **Pluralismo Deontológico** | Múltiplos deveres irredutíveis |
| **Reino dos Fins** | Comunidade ideal de agentes racionais autolegisladores |

## Exercícios

1. **Aplicação do IC**: Aplique a primeira formulação do Imperativo Categórico a três problemas de ética de IA: (a) uso de deepfakes, (b) perfis de personalidade sem consentimento, (c) sistemas de recomendação que maximizam engajamento.

2. **Kant vs. Consequencialismo**: Um sistema de IA de diagnóstico médico encontra um câncer em um paciente que não quer saber o diagnóstico. O sistema deve: (a) contar a verdade (dever kantiano), ou (b) omitir para evitar sofrimento (consequencialista)? Formalize ambos os lados.

3. **Implementação de Ross**: Implemente um sistema de recomendação híbrido que pondere os sete deveres prima facie de Ross. Mostre como diferentes situações (e-commerce, saúde, justiça criminal) produzem diferentes deveres atuais.

4. **Leis de Asimov**: Implemente um simulador de dilemas para robôs com as Três Leis. Identifique pelo menos três situações onde as leis entram em conflito ou produzem resultados moralmente questionáveis.

5. **Direitos Humanos e IA**: Mapeie os deveres deontológicos relevantes para cinco aplicações de IA (reconhecimento facial, triagem de currículos, chatbots terapêuticos, carros autônomos, moderação de conteúdo). Para cada um, identifique qual direito "trunfo" está em jogo.

6. **Consentimento em Dark Patterns**: Analise três interfaces digitais comuns e identifique se violam o princípio kantiano de tratar usuários como fins. Proponha redesigns que respeitem a autonomia.

## Referências

- Anscombe, G. E. M. (1958). "Modern Moral Philosophy." *Philosophy*, 33(124), 1-19.
- Asimov, I. (1950). *I, Robot*. Gnome Press.
- Dworkin, R. (1977). *Taking Rights Seriously*. Harvard University Press.
- Dworkin, R. (1986). *Law's Empire*. Harvard University Press.
- Hegel, G. W. F. (1821). *Elements of the Philosophy of Right*.
- Herman, B. (1993). *The Practice of Moral Judgment*. Harvard University Press.
- Hill, T. E. (1992). *Dignity and Practical Reason in Kant's Moral Theory*. Cornell University Press.
- Kant, I. (1785). *Groundwork of the Metaphysics of Morals*.
- Kant, I. (1788). *Critique of Practical Reason*.
- Kant, I. (1797). *The Metaphysics of Morals*.
- Korsgaard, C. (1996). *Creating the Kingdom of Ends*. Cambridge University Press.
- O'Neill, O. (1989). *Constructions of Reason: Explorations of Kant's Practical Philosophy*. Cambridge University Press.
- Rawls, J. (1971). *A Theory of Justice*. Harvard University Press.
- Ross, W. D. (1930). *The Right and the Good*. Oxford University Press.
- Ross, W. D. (1939). *Foundations of Ethics*. Oxford University Press.
- Scanlon, T. M. (1998). *What We Owe to Each Other*. Harvard University Press.

[[04-Conhecimentos/07-Humanidades/Etica/INDEX|← Voltar ao índice de Ética]]
