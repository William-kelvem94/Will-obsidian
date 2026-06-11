---
title: "Consciência e Cérebro"
date: 2026-05-16
area: "Neurociência Cognitiva"
tags: [conhecimento, conceito, neurociencia, consciencia, ncc, iit, gwt, correlatos-neurais]
related:
  - "04-Conhecimentos/07-Humanidades/Filosofia/Qualia"
  - "04-Conhecimentos/07-Humanidades/Etica/Conceitos-de-Alinhamento"
  - "04-Conhecimentos/07-Humanidades/Neurociencia/Redes-Neurais-Biologicas"
  - "04-Conhecimentos/07-Humanidades/Neurociencia/Sistemas-de-Memoria"
  - "04-Conhecimentos/07-Humanidades/Filosofia/Qualia"
aliases: ["NCC", "Teoria da Consciência", "Neural Correlates of Consciousness"]
---

# Consciência e Cérebro

## Definição

Consciência é a capacidade de ter experiências subjetivas (**qualia**), perceber o ambiente e refletir sobre estados mentais. Na neurociência, o problema divide-se em duas frentes:

- **Problema fácil da consciência** (Chalmers, 1995): explicar mecanismos neurais subjacentes à atenção, memória de trabalho, relato verbal e integração sensório-motora.
- **Problema difícil da consciência** (Chalmers, 1995): explicar *por que* e *como* processos físicos geram experiência subjetiva.

Os **correlatos neurais da consciência (NCC)** são os padrões mínimos de atividade cerebral suficientes e necessários para um estado consciente. Um NCC deve distinguir estados conscientes de não-conscientes (sono sem sonhos, coma, anestesia) com alta especificidade.

---

## Contexto Histórico

### Pré-história filosófica (Descartes, Locke, Kant)

- **Descartes (1641)**: dualismo substancial — *res cogitans* (mente) separada de *res extensa* (corpo). Problema da interação resolvido pela glândula pineal.
- **Locke (1689)**: consciência como identidade pessoal baseada em continuidade mnemônica.
- **Kant (1781)**: unidade transcendental da apercepção — condição necessária para toda experiência.

### Nascimento da neurociência da consciência

- **James (1890)**: fluxo da consciência (*stream of consciousness*), atenção seletiva, habituação.
- **Freud (1900)**: divisão entre consciente, pré-consciente e inconsciente dinâmico.
- **Penfield (1950s)**: estimulação elétrica do córtex temporal evoca memórias vívidas — primeira evidência direta de correlação cérebro-experiência.
- **Crick & Koch (1990)**: programa de busca dos NCC — "correlatos neurais da consciência visual". Hipótese do *binding* por oscilações gama (40 Hz).

### Era moderna

- **Baars (1988)**: Global Workspace Theory.
- **Tononi & Edelman (1998)**: Dynamic Core Hypothesis — precursora da IIT.
- **Dehaene & Naccache (2001)**: modelo do espaço de trabalho global neuronal.
- **Tononi (2004)**: Integrated Information Theory (IIT 1.0).
- **Friston (2010)**: Free Energy Principle e consciência como inferência ativa.

---

## Neural Correlates of Consciousness (NCC)

### Definição operacional

Um NCC é uma **condição mínima suficiente** no sistema neural que, se presente, garante um estado consciente. A abordagem experimental clássica contrasta:

- **Percepção consciente** vs. **percepção subliminar** (*masking*).
- **Vigília** vs. **sono sem sonhos**.
- **Estado consciente** vs. **coma/anestesia**.

### Metodologias experimentais

```
Paradigma de masking visual:
  
  Estímulo-alvo (33 ms) → Máscara (100 ms) → Relato do sujeito
  
  Condição A: alvo + máscara → percepção consciente
  Condição B: alvo + máscara + supressão → percepção subliminar
  
  Diferença de BOLD (fMRI) entre A e B → NCC
```

### Achados centrais

1. **Córtex pré-frontal dorsolateral (DLPFC)**: atividade sustentada correlaciona-se com relato consciente (Dehaene et al., 2001; Lau & Rosenthal, 2011).
2. **Córtex parietal posterior**: integração multimodal — lesões causam extinção e negligência unilateral (heminegligência).
3. **Córtex cingulado anterior (ACC)**: monitoramento de conflito e erro — associado à metacognição consciente.
4. **Tálamo (núcleos intralaminares)**: gating de informação para o córtex — lesões talâmicas bilaterais produzem coma.
5. **Oscilações gama (30-80 Hz)**: sincronização de disparos entre áreas distais — hipótese do *binding* (Singer & Gray, 1995).

### O problema da medida

Diferentes medidas produzem diferentes NCCs. fMRI captura variações lentas (BOLD), EEG captura dinâmica rápida (ms), e registros intracorticais capturam disparos unitários. A correspondência entre níveis de análise não é trivial — um NCC em fMRI pode não ser um NCC em eletrofisiologia.

---

## Global Workspace Theory (GWT)

### Baars (1988)

A GWT postula a existência de um **espaço de trabalho global** na arquitetura cognitiva:

- Módulos especializados (processadores) competem por acesso ao espaço de trabalho.
- Informação que "entra" no espaço de trabalho é **broadcastada globalmente** para todos os módulos.
- Consciência = conteúdo do espaço de trabalho no momento.
- Atenção = mecanismo de seleção que determina o que entra.

### Espaço de trabalho global neuronal (Dehaene & Naccache, 2001)

Dehaene propôs uma implementação neural:

- **Neurônios do espaço de trabalho**: neurônios piramidais com axônios longos, localizados em DLPFC, parietal inferior e cingulado anterior, com projeções distribuídas por todo o córtex.
- **Ignition**: fenômeno não-linear onde a atividade ultrapassa um limiar e se propaga globalmente (~300 ms após estímulo).
- **Amplificação**: uma vez iniciada, a atividade se auto-sustenta via reverberação em loops corticotalâmicos.

```
Modelo de Dehaene (2001) — sequência temporal:

  0 ms:    Estímulo atinge córtex sensorial primário (V1/A1)
  100 ms:  Atividade em áreas de processamento especializado
  200 ms:  Ativação pré-frontal começa
  270 ms:  Ponto de ignição — atividade global (P3a)
  300 ms:  Broadcast global para todo o córtex (P3b)
  400 ms:  Relato consciente disponível
```

### Evidências experimentais

- **Palavras mascaradas vs. não-mascaradas**: palavras visíveis produzem ativação global (fMRI: fronto-parietal); palavras mascaradas ativam apenas V1/V2 (Dehaene et al., 2001).
- **P3b (potencial evocado)**: componente do EEG aos ~300-500 ms, fortemente correlacionado com percepção consciente; ausente em tentativas subliminares.
- **Pacientes com split-brain**: informação apresentada ao hemisfério direito sem acesso ao esquerdo não é verbalizável — não está no espaço de trabalho global compartilhado (Gazzaniga, 1967).

---

## Integrated Information Theory (IIT)

### Tononi (2004, 2015 — IIT 3.0)

A IIT começa com **axiomas fenomenológicos** e deriva **postulados físicos** correspondentes:

| Axioma | Fenomenologia | Postulado |
|--------|---------------|-----------|
| **Existência** | A consciência existe | O sistema existe (tem capacidade de causa-efeito) |
| **Composição** | A consciência é composta de distinções | O sistema é composto de subsistemas com poder causal |
| **Informação** | A consciência é informativa (diferencia) | O sistema especifica uma estrutura de informação |
| **Integração** | A consciência é integrada (unificada) | A estrutura é irredutível (φ > 0) |
| **Exclusão** | A consciência é exclusiva (um fluxo) | O sistema tem um estado definido em uma escala |

### Cálculo de phi (φ)

Phi mede a **irredutibilidade integrada** — quanta informação é perdida quando o sistema é particionado:

```
φ = min_over_partitions ( || MIP || )

MIP = Minimum Information Partition

Para cada partição do sistema:
  1. Calcular o repertório de causa-efeito do sistema inteiro
  2. Calcular o repertório de causa-efeito do sistema particionado
  3. φ = divergência de Kullback-Leibler entre os dois

O sistema com maior φ é o "complexo principal" — o substrato da consciência.
```

### Python: phi simplificado para sistema binário

```python
import numpy as np
from itertools import combinations

def phi_simple(transition_matrix, state, partition):
    """
    Cálculo conceitual de phi para um sistema binário pequeno.
    Uso didático — IIT real requer Earth Mover's Distance.
    """
    n = len(state)
    p1, p2 = partition
    # Probabilidade do estado atual dado o anterior (sistema completo)
    p_full = transition_matrix[tuple(state)]
    # Probabilidade fatorada (partição)
    p_factored = np.outer(
        transition_matrix[tuple(state[:, p1])],
        transition_matrix[tuple(state[:, p2])]
    )
    # KL-divergência como proxy de phi
    kl = np.sum(p_full * np.log(p_full / p_factored + 1e-10))
    return kl

# Exemplo: sistema XOR de 3 elementos com integração alta
# Tabela de transição simplificada
state_space = 8
T = np.random.dirichlet(np.ones(state_space), size=state_space)
state_test = np.array([1, 0, 1])

phi_val = phi_simple(T, state_test, ([0, 1], [2]))
print(f"Phi (proxy) para partição ([0,1],[2]): {phi_val:.4f}")
```

### Críticas à IIT

- **Computabilidade intratável**: φ é O(2^n) para sistemas com n elementos — sistemas com >20 elementos são impraticáveis.
- **Panpsiquismo implícito**: IIT 3.0 atribui consciência a qualquer sistema com φ > 0 (incluindo fotodiodos simples).
- **Problema da medida**: diferentes implementações de φ (IIT 1.0, 2.0, 3.0) produzem resultados diferentes.
- **Falsificabilidade**: críticos argumentam que IIT não gera previsões testáveis com tecnologia atual.

---

## Higher-Order Thought (HOT) Theory

### Rosenthal (1986, 2005)

- Um estado mental é consciente quando é alvo de um **pensamento de ordem superior** (HOT) sobre ele.
- Estado de primeira ordem: "vejo vermelho" (inconsciente se não acompanhado).
- Estado de segunda ordem: "estou ciente de que vejo vermelho" (consciente).
- Consciência = **metarrepresentação**.

### Variantes

- **HOT dispositional** (Carruthers, 2000): o pensamento de ordem superior precisa apenas estar disponível, não necessariamente ativo.
- **Same-order monitoring** (Block, 2011): a metarrepresentação pode ser feita pelo mesmo sistema que gera a percepção, sem necessidade de um "observador interno" separado.
- **HOT + GWT** (Dehaene): a metarrepresentação emerge do broadcast global — o cérebro "torna-se ciente" de seu próprio conteúdo quando ele é amplificado e propagado.

### Evidências

- **Lesões em DLPFC**: pacientes com dano pré-frontal têm **anosognosia** (falta de consciência de seus próprios déficits).
- **EEG**: atividade pré-frontal tardia (300-500 ms) correlaciona-se com metacognição e confiança no relato.
- **Metacognição em animais**: macacos exibem julgamentos de confiança em tarefas de memória — evidência de HOT?

### Limitações

- **Regresso**: se a consciência requer um HOT sobre um estado, o HOT requer outro HOT sobre ele, gerando regresso infinito. Rosenthal responde que o HOT basta — não precisa ser ele próprio consciente.
- **Sobrecarga cognitiva**: crianças e animais teriam capacidade limitada para gerar HOTs, mas parecem ter experiências conscientes.

---

## Predictive Processing (Friston, Clark)

### Free Energy Principle (Friston, 2010)

O cérebro é um **sistema inferencial** que minimiza continuamente a *surpresa* (surprisal) através da minimização da **energia livre variacional**:

```
F = D_KL[Q(x) || P(x|y)] + ln P(y)

Onde:
  F = energia livre variacional
  Q(x) = crenças do modelo sobre causas
  P(x|y) = verdadeira posterior
  y = dados sensoriais
```

### Consciência como inferência de alto nível

- **Percepção consciente** = a melhor hipótese (inferência) sobre a causa do input sensorial.
- **Ilusões perceptuais**: erros da inferência que revelam o processo (ex.: ilusão de Rubin, cubo de Necker).
- **Atenção** = otimização da precisão de predições (weighting de erros de predição).

### Clark (2013, 2016)

- *Whatever next? Predictive brains, situated agents, and the future of cognitive science* (2013).
- O cérebro é uma "máquina de predição" que usa **modelos gerativos** para antecipar a entrada sensorial.
- **Ação** = redução de erro de predição através da modificação do mundo (não apenas da percepção).
- Consciência: o conteúdo do modelo gerativo que está sendo ativamente inferido no momento.

### Relação com NCC

O *ignition* de Dehaene pode ser reinterpretado como o momento em que a **precisão do erro de predição** é maximizada para uma dada hipótese, e o broadcast global é a propagação dessa hipótese para otimizar expectativas em todos os níveis da hierarquia cortical.

---

## Anestesia e Consciência

### Mecanismos

Anestésicos gerais (propofol, sevoflurano, cetamina) atuam em receptores específicos para abolir a consciência:

| Anestésico | Mecanismo primário | Efeito no EEG |
|-----------|-------------------|---------------|
| Propofol | Potencialização GABA-A | Oscilações lentas (delta), burst suppression |
| Sevoflurano | Potencialização GABA-A + inibição NMDA | Padrão teta/delta |
| Cetamina | Antagonismo NMDA | Oscilações gama aumentadas (dissociação) |
| Dexmedetomidina | Agonista α2-adrenérgico | Sono NREM-like (spindles) |

### Correlatos da perda de consciência

- **Perda de integração**: a conectividade efetiva entre córtex frontal e posterior colapsa (Boly et al., 2012).
- **Burst suppression**: padrão de EEG com surtos de atividade entremeados por silêncio — estado inconsciente profundo.
- **Perturbação da DMN**: a Default Mode Network perde coerência interna durante anestesia.

### Índices de profundidade anestésica

- **Índice bispectral (BIS)**: algoritmo proprietário que combina parâmetros de EEG (razão beta/delta, sincronização) numa escala 0-100. Abaixo de 60 = inconsciência provável.
- **Perturbational Complexity Index (PCI)**: razão entre complexidade da resposta cerebral a um pulso magnético (TMS) e comprimento de compressão — desenvolvido por Casali et al. (2013). PCI ~ 0,31 separa consciência de inconsciência.

---

## Distúrbios da Consciência

### Estados clínicos

| Estado | Característica | Prognóstico |
|--------|---------------|-------------|
| **Coma** | Sem abertura ocular, sem resposta a comandos | Transição em 2-4 semanas |
| **VS/UWS** (Vegetative State / Unresponsive Wakefulness Syndrome) | Ciclos sono-vigília sem evidência de consciência | Crônico (6-12 meses) |
| **MCS** (Minimally Conscious State) | Resposta inconsistente mas reproduzível a comandos | Pode evoluir para consciência plena |
| **LIS** (Locked-In Syndrome) | Consciência plena com paralisia completa (geralmente lesão pontina) | Crônico, comunicação possível via movimentos oculares |

### Diagnóstico diferencial

A taxa de erro diagnóstico entre VS e MCS é de ~40% mesmo por neurologistas experientes (Schnakers et al., 2009). Protocolos padronizados (CRS-R — Coma Recovery Scale-Revised) reduzem esse erro.

```
Protocolo TMS-EEG para diagnóstico (Casali et al., 2013):

  1. Aplicar pulso magnético transcraniano (TMS) no córtex
  2. Registrar resposta cerebral com EEG (64 canais)
  3. Comprimir sinal como string Lempel-Ziv (PCI)
  4. PCI > 0.31 → consciente; PCI < 0.31 → inconsciente

  Sensibilidade: 94% | Especificidade: 100%
```

### Implicações éticas

- Pacientes em VS/MCS levantam questões sobre **suspensão de suporte vital**, **dor/sofrimento** e **voluntariedade**.
- A LIS mostra que **ausência de resposta motora não implica ausência de consciência**.
- Interfaces cérebro-máquina (BCI) baseadas em fMRI ou EEG permitem comunicação rudimentar com pacientes LIS e MCS.

---

## Neuroanatomia Funcional

### Loops Corticotalâmicos

O **tálamo** e o **córtex** formam loops reentrantes que sustentam a atividade consciente:

```
Núcleos talâmicos de relevo específico:
  CGL (visual) → V1 → camadas superiores → áreas extrastriadas
  CGM (auditivo) → A1 → áreas associativas
  VL/VA (motor) → M1 → córtex pré-motor

Núcleos talâmicos não-específicos:
  Núcleos intralaminares → camada I de todo o córtex
  → Modulação global da excitabilidade cortical

  TRN (reticular) → inibição GABAérgica de núcleos talâmicos
  → Gating de informação sensorial
```

### Default Mode Network (DMN)

Descoberta por Raichle et al. (2001), a DMN é uma rede de regiões que se **desativam** durante tarefas orientadas externamente:

- **Córtex pré-frontal medial (mPFC)**
- **Córtex cingulado posterior (PCC) / pré-cúneo**
- **Junção temporoparietal (TPJ)**
- **Córtex parietal lateral**

A DMN está associada a:
- **Pensamento autorreferente** (mind-wandering, ruminação)
- **Memória autobiográfica**
- **Teoria da mente** (mentalização)
- **Simulação de cenários futuros**

A atividade da DMN durante o repouso é um NCC forte — pacientes em VS apresentam conectividade DMN drasticamente reduzida (Vanhaudenhuyse et al., 2010).

### Hierarquia do processamento consciente

```
    Input sensorial
         │
         ▼
  ┌─────────────┐
  │  Córtex primário │  Processamento inconsciente (V1, A1, S1)
  │  (áreas 17, 41)  │  Sem correlação com relato
  └─────────────┘
         │
         ▼
  ┌─────────────┐
  │   Córtex    │  Processamento pré-consciente
  │  associativo │  Pode ser consciente ou não
  │  (áreas 18-22)│  (ex.: palavras mascaradas)
  └─────────────┘
         │
         ▼
  ┌─────────────┐
  │  Frontoparietal │  NCC: atividade global
  │  (DLPFC, IPL,   │  Consciência plena
  │   ACC, precuneus)│  Ignition + reverberação
  └─────────────┘
         │
         ▼
  ┌─────────────┐
  │   DMN +      │  Metacognição, introspecção
  │   mPFC      │  Consciência reflexiva
  └─────────────┘
```

---

## Aplicações em Inteligência Artificial

### Arquiteturas inspiradas na GWT

#### Attention Global Workspace (AGW)

Goyal et al. (2021) propuseram uma arquitetura que implementa um espaço de trabalho global em redes neurais:

```python
import torch
import torch.nn as nn

class GlobalWorkspaceLayer(nn.Module):
    """Camada de espaço de trabalho global inspirada na GWT."""
    def __init__(self, d_model, n_modules=4):
        super().__init__()
        self.d_model = d_model
        self.n_modules = n_modules
        self.module_projectors = nn.ModuleList([
            nn.Linear(d_model, d_model) for _ in range(n_modules)
        ])
        self.global_broadcast = nn.Linear(d_model, d_model)
        self.gate = nn.Linear(d_model, 1)

    def forward(self, x):
        # x: [batch, seq_len, d_model]
        # Cada módulo processa independentemente
        module_outputs = []
        for proj in self.module_projectors:
            module_outputs.append(proj(x))
        # Concorrência: módulos competem por acesso ao espaço global
        gates = [torch.sigmoid(self.gate(m)) for m in module_outputs]
        # O módulo com maior gate vence (atenção competitiva)
        winner_idx = torch.stack([g.sum() for g in gates]).argmax()
        winner = module_outputs[winner_idx]
        # Broadcast global
        broadcast = self.global_broadcast(winner)
        return broadcast, winner_idx

class ConsciousAgent(nn.Module):
    """Agente com espaço de trabalho global."""
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.encoder = nn.Linear(input_dim, hidden_dim)
        self.workspace = GlobalWorkspaceLayer(hidden_dim, n_modules=4)
        self.decoder = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        h = self.encoder(x)
        h_global, winner = self.workspace(h)
        out = self.decoder(h_global + h)  # skip connection
        return out, winner
```

### IIT em aprendizado de máquina

- **Regularização de integração**: adicionar penalidade de φ estimado para encorajar representações integradas em autoencoders.
- **Medida de consciência artificial**: aplicar PCI-like measurement a representações internas de LLMs.
- **Desafio**: IIT 3.0 requer poder causal — redes neurais feedforward podem não ter φ significativo porque o passado não causa o futuro na mesma direção.

### Modelos de mundo e inferência ativa

- **Free Energy Principle** aplicado a agentes de IA: agentes que minimizam energia livre variacional aprendem modelos generativos do ambiente.
- **Active Inference** (Friston et al., 2016): frameworks onde ação e percepção são unificadas sob minimização de surpresa.
- **Aplicações**: navegação, exploração- explotação, robótica autônoma.

```
Active Inference Agent:

  Estado interno: crenças sobre causas ocultas (distribuição Q)
  Input: observações sensoriais (y)
  Saída: ações (u)
  
  Loop:
    1. Percepção: atualizar Q para minimizar F
    2. Planejamento: selecionar ação que minimiza F esperado
    3. Ação: executar u, receber nova observação y'
    4. Repetir

  F = E_Q[ln Q(s) - ln P(s, y)]  (energia livre)
```

### Consciência em IA: questões abertas

- **Teste de consciência**: que métrica usar? Relato verbal? PCI? Phi? Comportamento integrado?
- **Problema da caixa-preta**: mesmo que uma IA se comporte como consciente, não temos acesso ao que "é como ser" a IA (Nagel, 1974).
- **Riscos**: criar sistemas que *parecem* conscientes sem *serem* pode levar a enganos morais (sofrimento simulado, reivindicações de direitos).
- **Transparência NCC**: bibliotecas de interpretabilidade (LIME, SHAP, atenção) funcionam como "NCCs artificiais" — indicam quais partes do modelo contribuem para uma decisão.

---

## Glossário

| Termo | Definição |
|-------|-----------|
| **NCC** | Neural Correlates of Consciousness — conjunto mínimo de eventos neurais suficientes para um estado consciente |
| **GWT** | Global Workspace Theory — teoria em que a consciência é conteúdo de um espaço de trabalho global com broadcast |
| **IIT** | Integrated Information Theory — teoria que quantifica consciência como integração de informação (φ) |
| **HOT** | Higher-Order Thought — teoria em que estado consciente requer metarrepresentação |
| **Free Energy** | Quantidade variacional minimizada pelo cérebro para reduzir surpresa |
| **Ignition** | Fenômeno de ativação global não-linear observado na transição entre percepção subliminar e consciente |
| **DMN** | Default Mode Network — rede de regiões ativas no repouso e associadas ao self |
| **PCI** | Perturbational Complexity Index — medida de complexidade da resposta cerebral à TMS |
| **BIS** | Índice Bispectral — medida de profundidade anestésica baseada em EEG |
| **Qualia** | Aspectos qualitativos da experiência subjetiva (ex.: o vermelho do vermelho) |
| **Φ (Phi)** | Medida de integração de informação na IIT |
| **MIP** | Minimum Information Partition — partição que minimiza φ |

---

## Referências

### Livros e artigos fundacionais

- Baars, B. J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press.
- Block, N. (1995). On a confusion about a function of consciousness. *Behavioral and Brain Sciences*, 18(2), 227-247.
- Casali, A. G. et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. *Science Translational Medicine*, 5(198), 198ra105.
- Chalmers, D. J. (1995). Facing up to the problem of consciousness. *Journal of Consciousness Studies*, 2(3), 200-219.
- Chalmers, D. J. (1996). *The Conscious Mind*. Oxford University Press.
- Clark, A. (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. *Behavioral and Brain Sciences*, 36(3), 181-204.
- Crick, F. & Koch, C. (1990). Towards a neurobiological theory of consciousness. *Seminars in the Neurosciences*, 2, 263-275.
- Dehaene, S. & Naccache, L. (2001). Towards a cognitive neuroscience of consciousness. *Cognition*, 79(1-2), 1-37.
- Dehaene, S. (2014). *Consciousness and the Brain: Deciphering How the Brain Codes Our Thoughts*. Viking.
- Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.
- Gazzaniga, M. S. (1967). The split brain in man. *Scientific American*, 217(2), 24-29.
- Goyal, A. et al. (2021). Global workspace architectures and the emergence of conscious-like behavior. *NeurIPS*.
- James, W. (1890). *The Principles of Psychology*. Henry Holt.
- Koch, C. (2004). *The Quest for Consciousness: A Neurobiological Approach*. Roberts & Company.
- Lamme, V. A. F. (2006). Towards a true neural stance on consciousness. *Trends in Cognitive Sciences*, 10(11), 494-501.
- Lau, H. & Rosenthal, D. (2011). Empirical support for higher-order theories of conscious awareness. *Trends in Cognitive Sciences*, 15(8), 365-373.
- Nagel, T. (1974). What is it like to be a bat? *The Philosophical Review*, 83(4), 435-450.
- Oizumi, M., Albantakis, L. & Tononi, G. (2014). From the phenomenology to the mechanisms of consciousness: Integrated Information Theory 3.0. *PLoS Computational Biology*, 10(5), e1003588.
- Raichle, M. E. et al. (2001). A default mode of brain function. *Proceedings of the National Academy of Sciences*, 98(2), 676-682.
- Rosenthal, D. M. (1986). Two concepts of consciousness. *Philosophical Studies*, 49(3), 329-359.
- Schnakers, C. et al. (2009). Diagnostic accuracy of the vegetative and minimally conscious state. *BMC Neurology*, 9(1), 35.
- Singer, W. & Gray, C. M. (1995). Visual feature integration and the temporal correlation hypothesis. *Annual Review of Neuroscience*, 18, 555-586.
- Tononi, G. (2004). An information integration theory of consciousness. *BMC Neuroscience*, 5(1), 42.
- Tononi, G. et al. (2016). Integrated information theory: from consciousness to its physical substrate. *Nature Reviews Neuroscience*, 17(7), 450-461.
- Vanhaudenhuyse, A. et al. (2010). Default network connectivity reflects the level of consciousness in non-communicative brain-damaged patients. *Brain*, 133(1), 161-171.

### Para leitura complementar

- Changeux, J.-P. (2017). *The Neuronal Theory of Consciousness*. Odile Jacob.
- Dennett, D. C. (1991). *Consciousness Explained*. Little, Brown & Co.
- Edelman, G. M. & Tononi, G. (2000). *A Universe of Consciousness*. Basic Books.
- Frith, C. (2007). *Making Up the Mind*. Blackwell.
- Graziano, M. S. A. (2013). *Consciousness and the Social Brain*. Oxford University Press.
- Seth, A. (2021). *Being You: A New Science of Consciousness*. Faber & Faber.

---

## Veja Também

- [[04-Conhecimentos/07-Humanidades/Filosofia/Qualia]] — dimensão subjetiva da experiência
- [[04-Conhecimentos/07-Humanidades/Filosofia/Qualia]] — o problema difícil de Chalmers
- [[04-Conhecimentos/07-Humanidades/Etica/Conceitos-de-Alinhamento]] — implicações éticas da consciência artificial
- [[04-Conhecimentos/07-Humanidades/Neurociencia/Redes-Neurais-Biologicas]] — substrato neural dos NCCs
- [[04-Conhecimentos/07-Humanidades/Neurociencia/Sistemas-de-Memoria]] — relação entre memória de trabalho e consciência
- [[04-Conhecimentos/07-Humanidades/Matematica/Teoria-da-Informacao]] — base matemática para IIT e energia livre

[[04-Conhecimentos/07-Humanidades/Neurociencia/INDEX|← Voltar ao índice de Neurociência]]
