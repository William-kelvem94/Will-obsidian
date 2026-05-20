---
title: "Sistemas de Memória"
date: 2026-05-16
area: "Neurociência Cognitiva"
tags: [conhecimento, conceito, neurociencia, memoria, working-memory, ltp, hipocampo, ebbinghaus, amnesia, experiencia-replay, consolidacao]
related:
  - "Conhecimento-Geral/Neurociencia/Redes-Neurais-Biologicas"
  - "Conhecimento-Geral/Neurociencia/Consciencia-e-Cerebro"
  - "Conhecimento-Geral/Matematica/Teoria-da-Informacao"
  - "Conhecimento-Geral/Matematica/Probabilidade-e-Estatistica"
  - "skills/01-agentic-intelligence/reinforcement-learning"
aliases: ["Memória Cognitiva", "Sistemas de Memória Humana", "Taxonomia da Memória"]
---

# Sistemas de Memória

## Definição

Sistemas de memória são os processos e substratos neurais pelos quais informação é **codificada**, **armazenada** e **recuperada** no cérebro. A memória não é um sistema único e monolítico — é uma coleção de sistemas interconectados com diferentes:

- **Duração**: icônica (ms), curto prazo (s/min), longo prazo (horas-anos).
- **Capacidade**: limitada (WM: 7±2 itens) a virtualmente ilimitada (LTM).
- **Conteúdo**: fatos (semântica), eventos (episódica), habilidades (procedural).
- **Substrato neural**: hipocampo, amígdala, corpo estriado, cerebelo, córtex.

O estudo moderno da memória começa com **Hermann Ebbinghaus** (1885), que usou sílabas sem sentido para quantificar o esquecimento, e com o paciente **HM** (1957), cuja lesão bilateral do lobo temporal medial revelou a dissociação entre memória declarativa e procedural.

---

## Contexto Histórico

### Ebbinghaus (1885)

- Método: listas de sílabas consoante-vogal-consoante (e.g., "ZOK", "TAF", "GIR").
- Autoexperimentação com 2.300 listas, medindo economia de reaprendizagem.
- Curva do esquecimento: declínio exponencial, estabilização após ~1 semana.

### William James (1890)

- Distinguiu **memória primária** (presente imediato) de **memória secundária** (passado recuperado).
- Diferenciou **hábito** (memória procedural) de **lembrança** (memória declarativa).

### Patient HM (Scoville & Milner, 1957)

- Remoção bilateral do lobo temporal medial (incluindo hipocampo) para tratar epilepsia.
- Resultado: **amnésia anterógrada grave** (incapacidade de formar novas memórias declarativas).
- Memória procedural preservada: HM aprendeu *mirror drawing* sem lembrar de ter praticado.
- Conclusão: o hipocampo é crítico para consolidação, mas não para armazenamento de longo prazo.

### Tulving (1972, 1985)

- Distinguiu memória **episódica** (eventos pessoais, *autonoetic consciousness*) de **semântica** (fatos gerais, *noetic consciousness*).
- Memória episódica é única aos humanos? Evidências controversas em aves (scrub jays) e primatas.

---

## Taxonomia dos Sistemas de Memória

```
                            MEMÓRIA
                               │
              ┌────────────────┴────────────────┐
              │                                 │
        DECLARATIVA                      NÃO-DECLARATIVA
        (EXPLÍCITA)                        (IMPLÍCITA)
              │                                 │
    ┌─────────┴─────────┐            ┌──────────┴──────────┐
    │                   │            │                     │
  EPISÓDICA         SEMÂNTICA    PROCEDURAL         CONDICIONAMENTO
  (eventos,         (fatos,      (habilidades,       (respostas
   tempo/lugar)      conceitos)   hábitos)            aprendidas)
    │                   │            │                     │
    │                   │            │                     │
  "O que comi        "Paris é      Andar de         Medo (amígdala)
   no café da         capital       bicicleta        Reflexo (cerebelo)
   manhã"            da França"
    │                   │            │                     │
    └───────────────────┴────────────┴─────────────────────┘
                              │
                    PRIMING & PERCEPTUAL
                    (reconhecimento implícito
                     de estímulos)
```

---

## Modelo Multiestágios (Atkinson-Shiffrin, 1968)

### Arquitetura

```
  Input sensorial
       │
       ▼
  ┌────────────┐
  │ REGISTRO   │  Duração: 200-500 ms
  │ SENSORIAL  │  Capacidade: alta (toda a cena visual)
  │ (icônico/  │  Perda: decaimento
  │  ecoico)   │
  └──────┬─────┘
         │ (atenção)
         │
         ▼
  ┌────────────┐
  │ MEMÓRIA DE │  Duração: 15-30 s (sem repetição)
  │ CURTO PRAZO │  Capacidade: 7 ± 2 chunks (Miller, 1956)
  │  (STM)     │  Perda: deslocamento / decaimento
  └──────┬─────┘
         │ (repetição / codificação)
         │
         ▼
  ┌────────────┐
  │ MEMÓRIA DE │  Duração: dias a anos
  │ LONGO PRAZO│  Capacidade: virtualmente ilimitada
  │  (LTM)    │  Perda: interferência / falha de recuperação
  └────────────┘
```

### Críticas e reformulações

- O modelo original subestimou o papel do **processamento ativo** (não apenas repetição) na transferência para LTM.
- Níveis de processamento (Craik & Lockhart, 1972): a profundidade da codificação (estrutural → fonêmico → semântico) determina a retenção, não o tempo na STM.
- A STM não é um armazenamento unitário — Baddeley a substituiu pela memória de trabalho multicomponente.

---

## Memória de Trabalho (Baddeley & Hitch, 1974)

### Modelo original (1974)

```
                     ┌──────────────┐
                     │ EXECUTIVO    │
                     │ CENTRAL      │
                     │ (atenção +   │
                     │  controle)   │
                     └──────┬───────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
      ┌───────┴───────┐           ┌───────┴───────┐
      │ LOOP          │           │ ESBOÇO        │
      │ FONOLÓGICO    │           │ VISUOESPACIAL │
      │ (fala, som)   │           │ (imagem,      │
      │              │           │  espaço)      │
      │ Armazena:    │           │               │
      │  ~2 s de fala│           │ Armazena:     │
      │ Buffer:      │           │  ~3-4 objetos │
      │  repetição   │           │  visuais      │
      │  subvocal    │           │               │
      └──────────────┘           └───────────────┘
```

### Atualização: Buffer Episódico (Baddeley, 2000)

- **Buffer episódico**: sistema de armazenamento temporário que integra informação de múltiplas modalidades (fonológica, visuoespacial) com a LTM em representações episódicas únicas.
- Capacidade: ~4 chunks.
- Conecta o executivo central à LTM episódica.

### Executivo Central

Componente atencional que:
1. **Foca a atenção**: seleciona inputs relevantes.
2. **Divide a atenção**: coordena tarefas duais.
3. **Muda de estratégia**: alterna entre tarefas.
4. **Inibe**: suprime respostas prepotentes.
5. **Atualiza**: monitora e revisa conteúdo da WM.

### Capacidade da WM

- **Span de dígitos**: 7 ± 2 (Miller, 1956) → revisado para ~4 chunks (Cowan, 2001).
- **Chunking**: agrupar itens individuais em unidades significativas ("1-9-4-5" → "1945").
- **Diferenças individuais**: correlatedas com QI fluido, raciocínio e controle atencional.
- **Desenvolvimento**: capacity aumenta da infância (~2 chunks) à idade adulta (~4-5).

### Neuroanatomia da WM

| Componente | Região | Função |
|-----------|--------|--------|
| Executivo central | DLPFC, ACC | Controle atencional, manipulação |
| Loop fonológico | IPL (esquerdo), área de Broca | Armazenamento fonológico, repetição |
| Esboço visuoespacial | Córtex parietal, occipital | Manutenção visual/espacial |
| Buffer episódico | Hipocampo, PFC | Integração multimodal |

---

## Memória de Longo Prazo

### Memória Episódica

- **Definição**: memória para eventos específicos localizados no tempo e espaço.
- **Consciência autonoética**: capacidade de "viajar mentalmente no tempo" (Tulving, 1985).
- **Substrato**: hipocampo (especialmente CA1, CA3), córtex entorrinal.
- **Células de lugar** (place cells, O'Keefe, 1971): neurônios hipocampais que disparam em locais específicos.
- **Células de grade** (grid cells, Moser & Moser, 2005): no córtex entorrinal — representam espaço de forma hexagonally periódica.

### Memória Semântica

- **Definição**: conhecimento geral sobre o mundo, independente de contexto temporal.
- **Exemplos**: "A Terra orbita o Sol", "um triângulo tem três lados", "cachorros latem".
- **Substrato**: neocórtex temporal (lobo temporal anterior), córtex parietal.
- **Organização**: hierarquias conceituais (animais → mamíferos → cães → labradores), categorias naturais (Warrington & Shallice, 1984).

### Dissociação episódica/semântica

| Critério | Episódica | Semântica |
|----------|-----------|-----------|
| **Experiência** | Re-experimentação ("lembrar") | Conhecimento ("saber") |
| **Contexto** | Tempo/lugar específico | Atemporal |
| **Consciência** | Autonoética | Noética |
| **Lesão hipocampal** | Gravemente afetada | Preservada em graus variados |
| **Desenvolvimento** | Surge mais tarde (~3-4 anos) | Surge mais cedo (~1-2 anos) |
| **Esquecimento** | Mais rápido | Mais lento |

### Memória Procedural

- **Definição**: memória para habilidades e hábitos motores e cognitivos.
- **Exemplos**: andar, tocar piano, digitar, andar de bicicleta.
- **Substrato**: corpo estriado (putamen, caudado), cerebelo, córtex motor.
- **Características**: adquirida lentamente (por repetição), resistente ao esquecimento, implícita.
- **Modelo**: Fitts & Posner (1967) — estágios cognitivo → associativo → autônomo.

### Memória de Reconhecimento

- **Familiaridade** vs. **Relembrança** (Yonelinas, 2002):
  - **Familiaridade**: sensação de já ter visto, sem contexto ("sei que vi essa face").
  - **Relembrança**: recuperação detalhada do contexto ("vi essa face na festa ontem").
  - **Substrato**: familiaridade → córtex perirrinal; relembrança → hipocampo.

---

## Consolidação da Memória

### Consolidação Sináptica (minutos a horas)

- **Mecanismo**: cascata de sinalização intracelular → síntese de proteínas → alteração estrutural das sinapses.
- **Via principal**: NMDA → Ca²⁺ → CaMKII → PKA → CREB → transcrição gênica de proteínas sinápticas (BDNF, Arc, c-Fos).
- **Depende de**: RNAm local (tradução nos dendritos), fatores tróficos (BDNF).

```
Cascata de consolidação sináptica:

  NMDA ativado
       │
  Influxo de Ca²⁺
       │
  CaMKII / PKA ativadas
       │
  CREB fosforilado (transcrição)
       │
  Síntese de: Arc, BDNF, c-Fos, proteínas sinápticas
       │
  Inserção de canais AMPA, crescimento de espinhas dendríticas
       │
  FORTALECIMENTO SINÁPTICO (LTP mantido)
```

### Consolidação Sistêmica (dias a anos)

- **Teoria do traço duplo**: a memória é armazenada simultaneamente no hipocampo e no córtex. Com o tempo, o córtex se torna independente do hipocampo.
- **Reativação hipocampal**: durante o sono, o hipocampo "reproduz" sequências de disparo que foram codificadas durante o dia (replay hipocampal).
- **Padrão pontual** (*sharp-wave ripples*, SWR): eventos de 150-250 Hz no hipocampo (CA1) durante NREM, associados a replay de trajetórias.

```
  Dia 1:            Hipocampo <───── neocórtex
                       │                   │
                  Evento vivenciado    Armazenamento
                   codificado           parcial
                       │                   │
  Noite 1:         Replay (SWR) ────→ Fortalecimento
                                        neocortical
                       │
  Semana 1:        Replays múltiplos
                       │
  Mês 1+:          Hipocampo ────→   Córtex autossuficiente
                    perde papel        (memória remota)
```

### Reconsolidação

- Quando uma memória é recuperada, ela retorna a um estado **lábil** e precisa ser **reconsolidada** para persistir (Nader et al., 2000).
- Janela de reconsolidação: ~6 horas.
- Potencial terapêutico: interromper reconsolidação de memórias traumáticas (TEPT) com propranolol.

---

## Sono e Memória

### Estágios do sono

```
Ciclo noturno (~90 min por ciclo, 4-5 ciclos por noite):

  ACORDADO: beta (13-30 Hz), gamma (30+ Hz)
       │
  NREM-1: teta (4-8 Hz) — transição, ~5% do sono
       │
  NREM-2: teta + spindles (12-15 Hz) + complexos K
       │    ~50% do sono — consolidação declarativa
       │
  NREM-3 (slow-wave sleep): delta (0.5-4 Hz)
       │    ~20% do sono — consolidação máxima
       │
  REM: teta + gamma, movimento ocular rápido
       ~25% do sono — consolidação procedural
       │
  Repete ciclo (NREM-1 → NREM-2 → NREM-3 → REM)
```

### Mecanismos da consolidação durante o sono

- **Slow-wave sleep (SWS)**:
  - Oscilações lentas (0,5-1 Hz) do córtico-talâmico organizam o *timing* de eventos hipocampais.
  - **Spindles** do tálamo (12-15 Hz) sincronizam a transferência hipocampo → neocórtex.
  - **Sharp-wave ripples** (150-250 Hz) no hipocampo ocorrem durante a fase *up* das oscilações lentas.
  - Acoplamento SWS-spindle-ripple: a coordenação tripla é preditiva de retenção no dia seguinte.

```
  Oscilação lenta (córtex):  ~~~~\____/~~~~\____/~~~~\____/
                                   │         │
  Spindle (tálamo):             ───┴─┐┌─┐───┴─┐┌─┐───┴─┐┌─┐
                                       │         │
  Ripple (hipocampo):               ───┐┌───────┐┌───────┐┌─
```

- **REM (Rapid Eye Movement)**:
  - Reativação de padrões neurais no hipocampo e amígdala.
  - Importante para memória emocional e procedural.
  - Reorganização de representações neocorticais (integração com conhecimento existente).

### Evidências experimentais

- **Efeito do sono na memória**: pessoas que dormem após aprender retêm significativamente mais do que quem fica acordado (Plihal & Born, 1997).
- **Privação de REM**: prejudica aprendizado procedural (e.g., mirror tracing).
- **Privação de SWS**: prejudica consolidação declarativa (e.g., pares de palavras).

---

## Esquecimento

### Curva do Esquecimento (Ebbinghaus, 1885)

```
Retenção (%)
  100 │
      │    
   80 │       ┌──────────┐
      │      ╱            ╲
   60 │     ╱              ╲
      │    ╱                ╲
   40 │   ╱                  ╲
      │  ╱                    ╲
   20 │ ╱                      ╲
      │╱                        ╲
    0 └────────────────────────────→ Tempo
       1h   1d   1sem   1mês
```

### Python: Curva de Ebbinghaus

```python
import numpy as np
import matplotlib.pyplot as plt

def ebbinghaus_curve(t, S=1.0, R0=100.0, k=0.1):
    """
    Curva do esquecimento de Ebbinghaus.
    
    Args:
        t: tempo (horas)
        S: força inicial da memória
        R0: retenção inicial (%)
        k: taxa de esquecimento (decay)
    
    Returns:
        R: retenção em %
    """
    return R0 * np.exp(-k * t / S)

# Força de memória com repetição (efeito de espaçamento)
def memory_with_repetition(repetition_times, base_k=0.1, boost=0.5):
    """
    Simula retenção com repetições espaçadas.
    
    Args:
        repetition_times: lista de tempos (horas) das repetições
        base_k: taxa de esquecimento base
        boost: aumento de força por repetição
    """
    t_continuous = np.linspace(0, 168, 1680)  # 1 semana
    S = 1.0  # força inicial
    R = []
    
    for t in t_continuous:
        # Aplicar boosts nos tempos de repetição
        for rt in repetition_times:
            if abs(t - rt) < 0.5:  # Janela de repetição
                S += boost
                break
        # Calcular retenção com força atualizada
        ret = ebbinghaus_curve(t, S=S, k=base_k)
        R.append(ret)
    
    return t_continuous, np.array(R)

# Simular: sem repetição vs. com repetições espaçadas
t, R_no_repeat = memory_with_repetition([], base_k=0.1)
t, R_spaced = memory_with_repetition([24, 72, 144], base_k=0.1)  # 1h, 3dias, 6dias

print(f"Retenção após 1 semana (sem repetição): {R_no_repeat[-1]:.1f}%")
print(f"Retenção após 1 semana (com repetições): {R_spaced[-1]:.1f}%")

# Aplicação: scheduling de revisão estilo Anki/SRS
def spaced_repetition_schedule(n_reviews, initial_interval_hours=4, multiplier=2.0):
    """
    Gera cronograma de repetição espaçada (SRS).
    
    Args:
        n_reviews: número de revisões
        initial_interval_hours: intervalo inicial
        multiplier: fator de multiplicação do intervalo
    
    Returns:
        intervals: lista de intervalos entre revisões (horas)
    """
    intervals = []
    current = initial_interval_hours
    for _ in range(n_reviews):
        intervals.append(current)
        current *= multiplier
    return intervals

sched = spaced_repetition_schedule(6)
print(f"Cronograma SRS (horas): {[f'{h:.1f}' for h in sched]}")
# Cronograma típico: 4h, 8h, 16h, 32h, 64h, 128h (~5 dias)
```

### Teorias do Esquecimento

| Teoria | Proponente | Ideia central | Evidência |
|--------|-----------|---------------|-----------|
| **Decaimento** | Ebbinghaus, Thorndike | Traços de memória enfraquecem com o tempo | Curva de Ebbinghaus |
| **Interferência** | McGeoch, Postman | Esquecimento por competição entre traços | List-learning paradigms |
| **Falha de recuperação** | Tulving | Informação existe mas é inacessível | Efeito do contexto, dicas |
| **Mudança de contexto** | Estes, Bower | O contexto de codificação difere do de recuperação | Efeito da congruência ambiental |

### Interferência

- **Interferência proativa**: informação antiga interfere com nova ("decorei o novo número do telefone mas ainda falo o antigo").
- **Interferência retroativa**: informação nova interfere com antiga ("depois de aprender francês, espanhol sai pior").

### Experimento clássico (Underwood, 1957)

Participantes aprendem listas de sílabas sem sentido:

```
Grupo A: aprende 1 lista → retém 70%
Grupo B: aprende 20 listas → retém 25%

Conclusão: interferência proativa é maior quanto mais material similar foi aprendido.
```

---

## Amnésia

### Paciente HM (Henry Molaison, 1926-2008)

- **Procedimento**: remoção bilateral do lobo temporal medial (hipocampo, córtex entorrinal, amígdala) em 1953 para epilepsia refratária.
- **Consequências**:
  - **Amnésia anterógrada**: incapacidade de formar novas memórias declarativas.
  - **Amnésia retrógrada**: perda parcial de memórias dos 2-3 anos antes da cirurgia; memórias remotas (infância) preservadas.
  - **WM preservada**: podia manter uma conversa, mas esquecia o que foi dito minutos depois.
  - **Memória procedural preservada**: aprendeu *mirror drawing* — curva de aprendizado normal, mas sem lembrança consciente de ter praticado.
- **Legado**: estabeleceu a dissociação entre:
  - Memória declarativa (explícita) vs. procedural (implícita).
  - Consolidação (hipocampo) vs. armazenamento permanente (córtex).
  - WM vs. LTM.

### Paciente Clive Wearing (n. 1938)

- **Diagnóstico**: encefalite por herpes simples → destruição bilateral do hipocampo e partes do lobo temporal.
- **Apresentação clínica**: amnésia anterógrada total + amnésia retrógrada grave.
- **Sintoma marcante**: "consciência de momento a momento" — relata que "acordou" pela primeira vez a cada 10-30 segundos.
- **Memórias preservadas**: música (piano, regência) — memória procedural musical intacta.
- **Consciência**: mantém senso de self, emoções e memória de trabalho — mas sem capacidade de formar novas memórias episódicas.

### Outros tipos de amnésia

| Tipo | Causa | Efeito | Sistema afetado |
|------|-------|--------|-----------------|
| **Amnésia global transitória** | Isquemia temporária (TGA) | Perda súbita de novas memórias por 4-6h | Hipocampo temporário |
| **Síndrome de Korsakoff** | Deficiência de tiamina (alcoolismo) | Amnésia anterógrada + confabulação | Corpos mamilares, tálamo |
| **Doença de Alzheimer** | Amiloide β + tau | Perda progressiva de memória (episódica primeiro) | Hipocampo → neocórtex difuso |
| **Amnésia psicogênica** | Trauma psicológico | Perda de memória autobiográfica seletiva | Mecanismo não claro |
| **Amnésia infantil** | Desenvolvimento | Incapacidade de lembrar eventos < 3-4 anos | Hipocampo imaturo, linguagem |

---

## Memória em Inteligência Artificial

### Memória episódica em aprendizado por reforço

#### Experience Replay (Mnih et al., 2015 — DQN)

```python
import numpy as np
import random
from collections import deque

class ExperienceReplayBuffer:
    """
    Buffer de replay para aprendizado por reforço.
    Inspirado no replay hipocampal durante o sono.
    """
    def __init__(self, capacity=10000):
        self.buffer = deque(maxlen=capacity)

    def push(self, state, action, reward, next_state, done):
        """Armazena experiência (como evento episódico)."""
        self.buffer.append((state, action, reward, next_state, done))

    def sample(self, batch_size):
        """Amostra experiências aleatórias para replay."""
        batch = random.sample(self.buffer, min(batch_size, len(self.buffer)))
        states, actions, rewards, next_states, dones = zip(*batch)
        return (np.array(states), np.array(actions),
                np.array(rewards), np.array(next_states),
                np.array(dones))

    def prioritized_sample(self, batch_size, td_errors, alpha=0.6):
        """
        Amostragem priorizada (Schaul et al., 2016).
        Experiências com maior erro TD são amostradas com mais frequência
        — análogo à "salience-based consolidation".
        """
        priorities = np.abs(td_errors) ** alpha
        probs = priorities / priorities.sum()
        indices = np.random.choice(len(self.buffer), batch_size, p=probs)
        return indices  # + dados correspondentes

class ReplayAgent:
    """Agente RL com experiência replay e consolidação."""
    def __init__(self, state_dim, action_dim):
        self.memory = ExperienceReplayBuffer(50000)
        self.state_dim = state_dim
        self.action_dim = action_dim

    def learn_from_replay(self, batch_size=64):
        """Corresponde à consolidação durante "sono"."""
        if len(self.memory.buffer) < batch_size:
            return None
        batch = self.memory.sample(batch_size)
        # Atualizar Q-network com batch
        # (simplificado — usaríamos uma rede neural real)
        loss = np.random.random()  # placeholder
        return loss

    def sleep_consolidate(self, n_iterations=100):
        """Replay maciço de experiências, como consolidação sistêmica."""
        losses = []
        for _ in range(n_iterations):
            loss = self.learn_from_replay()
            if loss is not None:
                losses.append(loss)
        return np.mean(losses)

# Simular agente
agent = ReplayAgent(state_dim=10, action_dim=4)
# Agente coleta experiências
for _ in range(1000):
    s = np.random.randn(10)
    a = random.randint(0, 3)
    r = random.random()
    ns = np.random.randn(10)
    d = random.random() < 0.1
    agent.memory.push(s, a, r, ns, d)

# "Sono" — consolidação via replay
consolidation_loss = agent.sleep_consolidate(200)
print(f"Loss de consolidação: {consolidation_loss:.4f}")
```

#### Memory-Augmented Neural Networks

- **Neural Turing Machines** (Graves et al., 2014): rede neural com memória externa endereçável por conteúdo e localização.
- **Differentiable Neural Computer** (Graves et al., 2016): NTM expandida com alocação temporal, liberação de memória e links temporais.
- **Transformer** (Vaswani et al., 2017): mecanismo de **atenção** funciona como uma memática endereçável por *queries* — cada token pode "recordar" tokens anteriores no contexto.

### Mecanismo de Atenção como Memória de Trabalho

```
Transformer Decoder:

  Contexto (KV cache): tokens anteriores
       ↓
  Query (token atual) → Atenção → Weighted sum sobre contexto
       ↓
  Cada cabeça de atenção recupera informação específica
  (posicional, semântica, sintática)
       ↓
  O contexto funciona como memória de trabalho virtual
  (análoga ao buffer episódico de Baddeley)
```

### Episodic Memory em RL Profundo

- **Episodic Control** (Lengyel & Dayan, 2007): agente armazena trajetórias completas e recupera recompensas de situações similares.
- **Neural Episodic Control** (Pritzel et al., 2017): memória episódica diferencial para aprendizado rápido (one-shot) em RL.
- **Memory-based Meta-Learning** (Santoro et al., 2016): redes neurais recorrentes com memória externa aprendem a "lembrar" episódios recentes.

### RAG (Retrieval-Augmented Generation)

RAG é análogo à memória semântica humana:

```python
class RetrievalAugmentedMemory:
    """
    Sistema de busca e recuperação, análogo à memória semântica.
    """
    def __init__(self, documents, embedder):
        self.documents = documents
        self.embedder = embedder
        # Pré-computar embeddings
        self.doc_embeddings = [embedder(doc) for doc in documents]

    def retrieve(self, query, k=3):
        """Recupera documentos relevantes (análogo a priming semântico)."""
        query_emb = self.embedder(query)
        similarities = [
            np.dot(query_emb, doc_emb)
            for doc_emb in self.doc_embeddings
        ]
        top_k = np.argsort(similarities)[-k:][::-1]
        return [self.documents[i] for i in top_k]

    def consolidate(self, new_doc):
        """
        Consolida novo conhecimento na memória de longo prazo
        (análogo à consolidação sistêmica).
        """
        self.documents.append(new_doc)
        self.doc_embeddings.append(self.embedder(new_doc))
```

### Modelos de Linguagem como Memória

- **LLMs** armazenam conhecimento semântico extenso nos pesos pós-treinamento.
- **Janela de contexto** (~4K-1M tokens) funciona como memória de trabalho de longo prazo.
- **Fine-tuning** é análogo à consolidação de novos conhecimentos em LTM.
- **In-context learning**: o modelo usa exemplos fornecidos no contexto para inferir novas tarefas — análogo a recuperar memórias episódicas e generalizar.

---

## Glossário

| Termo | Definição |
|-------|-----------|
| **WM** | Working Memory — sistema de capacidade limitada para manutenção e manipulação temporária de informação |
| **LTM** | Long-Term Memory — armazenamento de informação de longa duração, capacidade virtualmente ilimitada |
| **STM** | Short-Term Memory — conceito precursor da WM; armazenamento de curta duração sem manipulação |
| **Episódica** | Memória para eventos pessoais localizados no tempo e espaço |
| **Semântica** | Memória para fatos e conhecimento geral do mundo |
| **Procedural** | Memória para habilidades e hábitos motores |
| **Consolidação** | Processo de estabilização de uma memória após codificação inicial |
| **Reconsolidação** | Reestabilização de memória recuperada (lábil → estável) |
| **LTP** | Long-Term Potentiation — fortalecimento sináptico duradouro, base celular da memória |
| **Spindle** | Oscilação de 12-15 Hz no tálamo durante NREM-2, associada à consolidação |
| **SWR** | Sharp-Wave Ripple — evento de alta frequência (150-250 Hz) no hipocampo durante replay |
| **Replay** | Reativação de sequências de disparo hipocampal durante o sono |
| **SRS** | Spaced Repetition System — cronograma de revisão que otimiza retenção |
| **Interferência** | Competição entre memórias que reduz a capacidade de recuperação |
| **Amnésia** | Perda patológica de memória, anterógrada (novas) ou retrógrada (antigas) |
| **Priming** | Facilitação implícita de recuperação por exposição prévia |
| **DRM** | Deese-Roediger-McDermott — paradigma de falsas memórias por associação semântica |
| **Chunking** | Agrupamento de itens individuais em unidades significativas |
| **Autoenoese** | Consciência do self como contínuo no tempo (Tulving) |

---

## Referências

### Livros e artigos fundacionais

- Atkinson, R. C. & Shiffrin, R. M. (1968). Human memory: A proposed system and its control processes. *The Psychology of Learning and Motivation*, 2, 89-195.
- Baddeley, A. D. & Hitch, G. (1974). Working memory. *The Psychology of Learning and Motivation*, 8, 47-89.
- Baddeley, A. D. (2000). The episodic buffer: a new component of working memory? *Trends in Cognitive Sciences*, 4(11), 417-423.
- Bliss, T. V. P. & Lømo, T. (1973). Long-lasting potentiation of synaptic transmission in the dentate area of the anaesthetized rabbit following stimulation of the perforant path. *Journal of Physiology*, 232(2), 331-356.
- Cowan, N. (2001). The magical number 4 in short-term memory: a reconsideration of mental storage capacity. *Behavioral and Brain Sciences*, 24(1), 87-114.
- Craik, F. I. M. & Lockhart, R. S. (1972). Levels of processing: A framework for memory research. *Journal of Verbal Learning and Verbal Behavior*, 11(6), 671-684.
- Ebbinghaus, H. (1885/1913). *Über das Gedächtnis* (Memory: A Contribution to Experimental Psychology). Teachers College, Columbia University.
- James, W. (1890). *The Principles of Psychology*. Henry Holt.
- Kandel, E. R. (2001). The molecular biology of memory storage: a dialogue between genes and synapses. *Science*, 294(5544), 1030-1038.
- McGaugh, J. L. (2000). Memory — a century of consolidation. *Science*, 287(5451), 248-251.
- Miller, G. A. (1956). The magical number seven, plus or minus two: some limits on our capacity for processing information. *Psychological Review*, 63(2), 81-97.
- Nader, K., Schafe, G. E. & LeDoux, J. E. (2000). Fear memories require protein synthesis in the amygdala for reconsolidation after retrieval. *Nature*, 406(6797), 722-726.
- O'Keefe, J. & Nadel, L. (1978). *The Hippocampus as a Cognitive Map*. Oxford University Press.
- Pavlov, I. P. (1927). *Conditioned Reflexes*. Oxford University Press.
- Plihal, W. & Born, J. (1997). Effects of early and late nocturnal sleep on declarative and procedural memory. *Journal of Cognitive Neuroscience*, 9(4), 534-547.
- Schacter, D. L. (1987). Implicit memory: History and current status. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 13(3), 501-518.
- Scoville, W. B. & Milner, B. (1957). Loss of recent memory after bilateral hippocampal lesions. *Journal of Neurology, Neurosurgery & Psychiatry*, 20(1), 11-21.
- Squire, L. R. (1992). Memory and the hippocampus: a synthesis from findings with rats, monkeys, and humans. *Psychological Review*, 99(2), 195-231.
- Squire, L. R. (2009). Memory and brain systems: 1969-2009. *Journal of Neuroscience*, 29(41), 12711-12716.
- Tulving, E. (1972). Episodic and semantic memory. In E. Tulving & W. Donaldson (Eds.), *Organization of Memory* (pp. 381-403). Academic Press.
- Tulving, E. (1985). Memory and consciousness. *Canadian Psychology*, 26(1), 1-12.
- Tulving, E. (2002). Episodic memory: from mind to brain. *Annual Review of Psychology*, 53, 1-25.
- Underwood, B. J. (1957). Interference and forgetting. *Psychological Review*, 64(1), 49-60.
- Warrington, E. K. & Shallice, T. (1984). Category specific semantic impairments. *Brain*, 107(3), 829-853.
- Yonelinas, A. P. (2002). The nature of recollection and familiarity: A review of 30 years of research. *Journal of Memory and Language*, 46(3), 441-517.

### Sono e consolidação

- Buzsáki, G. (2015). Hippocampal sharp wave-ripple: A cognitive biomarker for episodic memory and planning. *Hippocampus*, 25(10), 1073-1188.
- Diekelmann, S. & Born, J. (2010). The memory function of sleep. *Nature Reviews Neuroscience*, 11(2), 114-126.
- Rasch, B. & Born, J. (2013). About sleep's role in memory. *Physiological Reviews*, 93(2), 681-766.
- Stickgold, R. & Walker, M. P. (2007). Sleep-dependent memory consolidation and reconsolidation. *Sleep Medicine*, 8(4), 331-343.

### Memória em IA

- Graves, A., Wayne, G. & Danihelka, I. (2014). Neural Turing Machines. *arXiv:1410.5401*.
- Graves, A. et al. (2016). Hybrid computing using a neural network with dynamic external memory. *Nature*, 538(7626), 471-476.
- Mnih, V. et al. (2015). Human-level control through deep reinforcement learning. *Nature*, 518(7540), 529-533.
- Pritzel, A. et al. (2017). Neural Episodic Control. *ICML 2017*.
- Santoro, A. et al. (2016). Meta-learning with memory-augmented neural networks. *ICML 2016*.
- Schaul, T. et al. (2016). Prioritized experience replay. *ICLR 2016*.
- Vaswani, A. et al. (2017). Attention is all you need. *NeurIPS 2017*.

### Sobreviventes históricos

- Hilts, P. J. (1995). *Memory's Ghost: The Strange Tale of Mr. M. and the Nature of Memory*. Simon & Schuster. [Biografia do paciente HM]
- Sacks, O. (1985). *The Man Who Mistook His Wife for a Hat*. Duckworth. [Capítulo sobre Clive Wearing]
- Wilson, B. A. & Wearing, D. (1995). Prisoner of consciousness: A state of just awakening following herpes simplex encephalitis. In R. Campbell & M. A. Conway (Eds.), *Broken Memories*.

---

## Veja Também

- [[Conhecimento-Geral/Neurociencia/Redes-Neurais-Biologicas]] — LTP, LTD, STDP e plasticidade como base molecular da memória
- [[Conhecimento-Geral/Neurociencia/Consciencia-e-Cerebro]] — consciência e memória de trabalho
- [[Conhecimento-Geral/Matematica/Teoria-da-Informacao]] — capacidade de memória e compressão
- [[Conhecimento-Geral/Matematica/Probabilidade-e-Estatistica]] — modelagem de recall, reconhecimento e ruído
- [[skills/01-agentic-intelligence/reinforcement-learning]] — experience replay, episodic control, TD-learning
- [[Conhecimento-Geral/Filosofia/Qualia]] — relação entre memória episódica e self
- [[Conhecimento-Geral/Filosofia/Conceitos-Fundamentais]] — memória como constitutiva do self (Locke)

[[Conhecimento-Geral/Neurociencia/INDEX|← Voltar ao índice de Neurociência]]
