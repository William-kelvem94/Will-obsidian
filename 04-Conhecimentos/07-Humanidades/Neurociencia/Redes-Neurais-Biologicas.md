---
title: "Redes Neurais Biológicas"
date: 2026-05-16
area: "Neurociência Cognitiva"
tags: [conhecimento, conceito, neurociencia, neuronio, sinapse, plasticidade, hodgkin-huxley, hebb, oscilacoes, colsuna-cortical, neuromorfico]
related:
  - "04-Conhecimentos/07-Humanidades/Neurociencia/Sistemas-de-Memoria"
  - "04-Conhecimentos/07-Humanidades/Neurociencia/Consciencia-e-Cerebro"
  - "04-Conhecimentos/07-Humanidades/Matematica/Algebra-Linear-Essencial"
  - "04-Conhecimentos/07-Humanidades/Matematica/Calculo-e-Otimizacao"
  - "04-Conhecimentos/07-Humanidades/Fisica/Eletromagnetismo"
aliases: ["Neurônio Biológico", "Plasticidade Sináptica", "Rede Neural Biológica"]
---

# Redes Neurais Biológicas

## Definição

Redes neurais biológicas são sistemas de processamento de informação compostos por **neurônios** — células especializadas que se comunicam através de **sinapses**. Um neurônio típico recebe sinais por **dendritos**, integra-os no **soma** (corpo celular) e transmite pulsos elétricos (**potenciais de ação**) pelo **axônio** até terminais sinápticos. A força de cada sinapse se modifica dinamicamente com base na história de disparos, implementando **plasticidade** — o substrato físico do aprendizado e da memória.

O cérebro humano contém aproximadamente 86 bilhões de neurônios (~86 × 10⁹) e cerca de 10¹⁴ a 10¹⁵ sinapses. Cada neurônio recebe inputs de 1.000 a 10.000 outros neurônios, formando um grafo direcionado de complexidade incomparável a qualquer sistema artificial atual.

---

## Estrutura do Neurônio

### Componentes morfológicos

```
                    Dendritos (árvore dendrítica)
                    │    │    │    │
                    │    │    │    │
                    └────┴────┴────┘
                         │
                    ┌────┴────┐
                    │  SOMA   │  Núcleo + organelas
                    │ (corpo  │
                    │ celular)│
                    └────┬────┘
                         │
                    ┌────┴────┐
                    │  Axônio │  Segmento inicial (Zona de gatilho)
                    │         │
                    └────┬────┘
                         │
                    ─────┴───────  Bainha de mielina (nódulos de Ranvier)
                         │
                    ─────┴───────
                         │
                    ┌────┴────┐
                    │Terminais│  Botões sinápticos
                    │Sinápticos│  → vesículas com neurotransmissores
                    └─────────┘
```

### Classificação de neurônios

| Tipo | Estrutura | Localização | Função |
|------|-----------|-------------|--------|
| **Piramidal** | Corpo triangular, dendrito apical longo | Córtex, hipocampo | Projeção excitatória (glutamato) |
| **Estrelado** | Dendritos radiados | Córtex (camada IV) | Interneurônio excitatório |
| **Célula de Purkinje** | Árvore dendrítica planar elaborada | Cerebelo | Único output inibitório (GABA) |
| **Célula granular** | Corpo pequeno, dendrito curto | Giro denteado, cerebelo | Neurônio mais numeroso do cérebro |
| **Interneurônio** | Axônio local | Em todo o SNC | Inibição local (GABA) |

### Membrana neuronal

A membrana plasmática do neurônio mantém uma **diferença de potencial elétrico** (potencial de membrana) através de bombas iônicas e canais:

- **Potencial de repouso**: ~ -70 mV (interior negativo relativo ao exterior).
- **Bomba Na⁺/K⁺-ATPase**: 3 Na⁺ para fora, 2 K⁺ para dentro, consumindo ATP.
- **Distribuição iônica**:

| Íon | [Intracelular] (mM) | [Extracelular] (mM) | Potencial de Nernst (mV) |
|-----|---------------------|---------------------|--------------------------|
| Na⁺ | 15 | 150 | +67 |
| K⁺ | 150 | 5 | -89 |
| Ca²⁺ | 0,0001 | 2 | +123 |
| Cl⁻ | 10 | 110 | -62 |

---

## Potencial de Ação e Modelo de Hodgkin-Huxley

### Gênese do potencial de ação

1. **Estímulo despolarizante**: entrada de corrente positiva eleva o potencial de membrana.
2. **Limiar de disparo**: em cerca de -55 mV, canais de Na⁺ dependentes de voltagem abrem rapidamente.
3. **Despolarização**: influxo massivo de Na⁺ eleva o potencial para ~+40 mV.
4. **Repolarização**: canais de Na⁺ fecham (inativação), canais de K⁺ abrem, efluxo de K⁺.
5. **Hiperpolarização pós-potencial**: canais de K⁺ demoram a fechar → potencial cai abaixo de -70 mV.
6. **Recuperação**: bomba Na⁺/K⁺ e difusão restauram gradientes.

```
Potencial de membrana (mV) durante potencial de ação:

  +40 ─────────────────────────────────────────────────────────────────────────────────
       │                                                                              
       │              ┌─────────────────────┐                                        
  +20  │             ╱                       ╲                                       
       │            ╱                         ╲                                      
   0   │           ╱                           ╲                                     
       │          ╱                             ╲                                    
  -20  │         ╱                               ╲                                   
       │        ╱                                 ╲                                  
  -40  │       ╱                                   ╲                                 
       │      ╱                                     ╲                                
  -55  │ ────╱                                       ╲                              
       │   ╱                                          ╲                             
  -70  │──╱─────────────────────────────────────────────\─────────────→ Tempo (ms)   
       │ ╱                                               \                          
       0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20
```

### Modelo de Hodgkin-Huxley (1952)

Hodgkin e Huxley modelaram o potencial de ação no axônio gigante de lula (*Loligo pealei*) com um circuito elétrico equivalente:

```
Circuito de membrana:

  ┌───Cₘ───┬───R_Na───┬───R_K───┬───R_leak───┬────┐
  │       │          │         │            │    │
  │       │    E_Na  │   E_K   │  E_leak    │    │
  │       │    (+67) │   (-89) │   (-54)    │    │
  │       │          │         │            │    │
  └───────┴──────────┴─────────┴────────────┴────┘
                             I_inj
```

Equações diferenciais (Hodgkin-Huxley, 1952):

```
Cₘ * dV/dt = I_inj - (g_Na * m³ * h * (V - E_Na) + g_K * n⁴ * (V - E_K) + g_leak * (V - E_leak))

Onde:
  V = potencial de membrana (mV)
  Cₘ = capacitância da membrana (1 μF/cm²)
  g_Na, g_K = condutâncias máximas (120, 36 mS/cm²)
  m, h = variáveis de ativação/inativação do Na⁺
  n = variável de ativação do K⁺
  E_Na, E_K, E_leak = potenciais de reversão

dx/dt = αₓ(V) * (1 - x) - βₓ(V) * x   para x ∈ {m, h, n}
```

### Python: Simulação Hodgkin-Huxley

```python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parâmetros
C_m = 1.0       # μF/cm²
g_Na = 120.0    # mS/cm²
g_K = 36.0      # mS/cm²
g_L = 0.3       # mS/cm²
E_Na = 50.0     # mV
E_K = -77.0     # mV
E_L = -54.387   # mV

# Funções alfa e beta (Hodgkin-Huxley, 1952)
def alpha_m(V):
    return 0.1 * (V + 40.0) / (1.0 - np.exp(-(V + 40.0) / 10.0))

def beta_m(V):
    return 4.0 * np.exp(-(V + 65.0) / 18.0)

def alpha_h(V):
    return 0.07 * np.exp(-(V + 65.0) / 20.0)

def beta_h(V):
    return 1.0 / (1.0 + np.exp(-(V + 35.0) / 10.0))

def alpha_n(V):
    return 0.01 * (V + 55.0) / (1.0 - np.exp(-(V + 55.0) / 10.0))

def beta_n(V):
    return 0.125 * np.exp(-(V + 65.0) / 80.0)

# Sistema de EDOs
def hodgkin_huxley(t, y, I_inj_func):
    V, m, h, n = y
    I_inj = I_inj_func(t)

    # Correntes iônicas
    I_Na = g_Na * m**3 * h * (V - E_Na)
    I_K = g_K * n**4 * (V - E_K)
    I_L = g_L * (V - E_L)

    dVdt = (I_inj - I_Na - I_K - I_L) / C_m
    dmdt = alpha_m(V) * (1 - m) - beta_m(V) * m
    dhdt = alpha_h(V) * (1 - h) - beta_h(V) * h
    dndt = alpha_n(V) * (1 - n) - beta_n(V) * n

    return [dVdt, dmdt, dhdt, dndt]

# Condições iniciais
V0 = -65.0
m0 = alpha_m(V0) / (alpha_m(V0) + beta_m(V0))
h0 = alpha_h(V0) / (alpha_h(V0) + beta_h(V0))
n0 = alpha_n(V0) / (alpha_n(V0) + beta_n(V0))

# Pulso de corrente
def inj_current(t):
    return 10.0 if 10.0 <= t <= 40.0 else 0.0

# Integração numérica
sol = solve_ivp(
    hodgkin_huxley, [0, 60],
    [V0, m0, h0, n0],
    args=(inj_current,),
    method='RK45',
    max_step=0.01,
    rtol=1e-6
)

t, V = sol.t, sol.y[0]
print(f"Potencial máximo atingido: {V.max():.1f} mV")
print(f"Disparos detectados: {(np.diff(np.signbit(V)) & (V[:-1] > -20)).sum()}")

# Visualização conceitual (em notebook, usar plt.plot)
# plt.plot(t, V); plt.xlabel("Tempo (ms)"); plt.ylabel("V (mV)")
```

### Propagação do potencial de ação

- **Condução saltatória**: em axônios mielinizados, o potencial de ação "salta" entre nódulos de Ranvier, onde há alta densidade de canais de Na⁺. Velocidade: até 120 m/s (axônios mielinizados) vs. 0,5-2 m/s (não-mielinizados).
- **Lei do tudo-ou-nada**: ou o potencial atinge o limiar e dispara (amplitude fixa), ou não dispara.
- **Período refratário absoluto**: ~1-2 ms — canais de Na⁺ inativados; nenhum estímulo dispara outro potencial.
- **Período refratário relativo**: ~3-5 ms — pós-hiperpolarização; apenas estímulos mais fortes disparam.

---

## Sinapses e Neurotransmissão

### Sinapse química (predominante no SNC)

```
Terminal pré-sináptico:
  ┌────────────────────┐
  │  Vesículas         │
  │  sinápticas (NT)   │
  │  ┌──┐ ┌──┐ ┌──┐   │
  │  │  │ │  │ │  │   │
  │  └──┘ └──┘ └──┘   │
  │         │          │
  │  ┌──────┴──────┐   │
  │  │ Ca²⁺ entra  │   │
  │  │ (VDCC)      │   │
  │  └──────┬──────┘   │
  │         │          │
  └─────────┼──────────┘
            │ Fenda sináptica (~20 nm)
  ┌─────────┼──────────┐
  │  ┌──────┴──────┐   │
  │  │ Receptores  │   │
  │  │ pós-sinápt.│   │
  │  └──────┬──────┘   │
  │         │          │
  │  ┌──────┴──────┐   │
  │  │ Potencial   │   │
  │  │ pós-sinápt.│   │
  │  │ (EPSP/IPSP)│   │
  │  └─────────────┘   │
  └────────────────────┘
Terminal pós-sináptico
```

### Principais neurotransmissores

| NT | Efeito | Receptores | Sistema |
|----|--------|------------|---------|
| **Glutamato** | Excitatório | AMPA, NMDA, Kaínico | Principal excitatório do SNC |
| **GABA** | Inibitório | GABA-A (ionotrópico), GABA-B (metabotrópico) | Principal inibitório do SNC |
| **Acetilcolina (ACh)** | Excitatório (muscarínico/nicotínico) | mAChR, nAChR | Junção neuromuscular, atenção |
| **Dopamina** | Modulatório | D1-D5 | Recompensa, motivação, movimento |
| **Serotonina** | Modulatório | 5-HT1-7 | Humor, sono, apetite |
| **Noradrenalina** | Modulatório | α1-2, β1-3 | Vigília, estresse, atenção |
| **Endocanabinoides** | Inibitório retrógrado | CB1, CB2 | Plasticidade, apetite |

### Sinapse elétrica (gap junction)

- Canais diretos (conexinas) entre citoplasmas.
- Transmissão bidirecional e quase instantânea (< 0,1 ms).
- Comum em desenvolvimento, retina e algumas regiões do SNC adulto.

---

## Plasticidade Sináptica

### Long-Term Potentiation (LTP)

Descoberta por Bliss & Lømo (1973) no hipocampo:

- **Protocolo**: estimulação de alta frequência (100 Hz, 1 s) → aumento duradouro da força sináptica (horas a dias).
- **Mecanismo**: ativação de NMDA → entrada de Ca²⁺ → ativação de CaMKII → inserção de receptores AMPA na membrana pós-sináptica.
- **Propriedades**:
  - **Especificidade input**: apenas a sinapse estimulada é fortalecida.
  - **Associatividade**: sinapse fraca pode ser fortalecida se co-ocorrer com forte despolarização pós-sináptica.
  - **Cooperatividade**: múltiplas sinapses fracas podem cooperar para atingir o limiar de LTP.

### Long-Term Depression (LTD)

- **Protocolo**: estimulação de baixa frequência (1 Hz, 15 min) → redução prolongada da força sináptica.
- **Mecanismo**: entrada moderada de Ca²⁺ → ativação de fosfatases (calcineurina, PP1) → endocitose de receptores AMPA.
- **Importância**: LTD previne saturação sináptica e permite *homeostase* da excitabilidade.

### Spike-Timing-Dependent Plasticity (STDP)

Descoberta por Bi & Poo (1998) em culturas de hipocampo:

A plasticidade depende da ordem temporal precisa entre disparo pré e pós-sináptico:

```
Δw = A₊ * exp(-Δt / τ₊)    se Δt > 0 (pré → pós, LTP)
Δw = -A₋ * exp(Δt / τ₋)    se Δt < 0 (pós → pré, LTD)

Onde:
  Δt = t_pós - t_pré
  τ₊ ~ 10-20 ms (janela de LTP)
  τ₋ ~ 10-20 ms (janela de LTD)
  A₊, A₋ = amplitudes de plasticidade
```

```
                    Δw
                     │
         LTD         │         LTP
   (pós antes de pré)│   (pré antes de pós)
                     │
  ───────────────────┼──────────────────→ Δt (ms)
                     │
    -40   -20    0    20    40
                     │
                     │
```

#### Python: Curva STDP

```python
import numpy as np

def stdp_curve(dt, A_plus=0.01, A_minus=0.012, tau_plus=20.0, tau_minus=20.0):
    """
    Calcula mudança de peso sináptico pela regra STDP.
    
    Args:
        dt: diferença temporal t_post - t_pre (ms)
        A_plus: amplitude LTP
        A_minus: amplitude LTD
        tau_plus, tau_minus: constantes de tempo (ms)
    
    Returns:
        delta_w: mudança fracionária no peso
    """
    if dt > 0:
        return A_plus * np.exp(-dt / tau_plus)
    elif dt < 0:
        return -A_minus * np.exp(dt / tau_minus)
    return 0.0

# Exemplo: simular 100 pares pré-pós com jitter temporal
np.random.seed(42)
n_pairs = 100
# Média: pré 5 ms antes do pós (LTP)
dts = np.random.normal(5, 10, n_pairs)

delta_ws = [stdp_curve(dt) for dt in dts]
print(f"Média STDP: {np.mean(delta_ws):.5f}")
print(f"LTP: {sum(d > 0 for d in delta_ws)} | LTD: {sum(d < 0 for d in delta_ws)}")

# Aprendizado temporal: simular STDP em um neurônio pós-sináptico
class SynapticPlasticity:
    """Modelo simples de STDP para um par pré-pós."""
    def __init__(self, w_init=0.5, A_plus=0.01, tau=20.0):
        self.w = w_init
        self.A_plus = A_plus
        self.tau = tau
        self.last_pre_time = None

    def pre_spike(self, t):
        self.last_pre_time = t

    def post_spike(self, t):
        if self.last_pre_time is not None:
            dt = t - self.last_pre_time
            dw = stdp_curve(dt, A_plus=self.A_plus, A_minus=self.A_plus * 1.2)
            self.w += dw
            self.w = np.clip(self.w, 0.0, 1.0)
        self.last_pre_time = None

    def __repr__(self):
        return f"SynapticPlasticity(w={self.w:.3f})"
```

### Homeostase sináptica (metaplasticidade)

- **Escalonamento sináptico** (Turrigiano, 1998): neurônios monitoram sua taxa de disparo média e escalam todas as sinapses para manter a excitabilidade dentro de uma faixa homeostática.
- **Modelo BCM** (Bienenstock-Cooper-Munro, 1982): o limiar para LTP/LTD se desloca com base na atividade pós-sináptica média, implementando um ponto de equilíbrio natural.

---

## Aprendizado Hebbiano

### Hebb (1949): The Organization of Behavior

> *"When an axon of cell A is near enough to excite cell B and repeatedly or persistently takes part in firing it, some growth process or metabolic change takes place in one or both cells such that A's efficiency, as one of the cells firing B, is increased."*

— D.O. Hebb, *The Organization of Behavior* (1949)

### Regra de Hebb

Formalização matemática:

```
Δw_ij = η * x_i * y_j

Onde:
  Δw_ij = mudança no peso sináptico do neurônio i para o j
  η = taxa de aprendizado
  x_i = atividade do neurônio pré-sináptico
  y_j = atividade do neurônio pós-sináptico
```

### Variações

- **Oja's rule** (Oja, 1982): normalização que implementa Análise de Componentes Principais.
  Δw_ij = η * y_j * (x_i - y_j * w_ij)

- **Covariance rule**: o aprendizado depende da correlação entre atividade e média.
  Δw_ij = η * (x_i - ⟨x_i⟩) * (y_j - ⟨y_j⟩)

- **Hebbiano pós-sináptico**: inclui efeito da ordem temporal (STDP como caso especial).

### Python: Rede Hebbiana simples

```python
import numpy as np

class HebbianNetwork:
    """Rede neural Hebbiana simples com normalização de Oja."""
    def __init__(self, n_input, n_output, lr=0.01):
        self.W = np.random.randn(n_input, n_output) * 0.1
        self.lr = lr

    def forward(self, x):
        return x @ self.W

    def hebb_update(self, x, y):
        # Regra de Oja: estabiliza pesos
        self.W += self.lr * (x[:, None] * y[None, :] - y[None, :]**2 * self.W)
        return self.W

    def train(self, X, epochs=100):
        for _ in range(epochs):
            for x in X:
                y = self.forward(x)
                self.hebb_update(x, y)
        return self.W

# Exemplo: detectar padrão repetido
np.random.seed(0)
X = np.random.randn(200, 10)
pattern = np.array([1, -1, 1, -1, 1, -1, 1, -1, 1, -1])
X[50:100] = pattern + np.random.randn(50, 10) * 0.1  # padrão com ruído

net = HebbianNetwork(10, 5, lr=0.001)
W = net.train(X, epochs=50)
print("Pesos treinados (shape):", W.shape)
print("Norma dos pesos:", np.linalg.norm(W, axis=0))
```

---

## Oscilações Neurais

### Mecanismos

Oscilações emergem da interação entre populações de neurônios excitatórios e inibitórios, com atrasos de propagação e propriedades de membrana ressonantes.

```
Modelo E-I (Wilson-Cowan, 1972):

  τ_E * dE/dt = -E + S(w_EE * E - w_EI * I + I_ext_E)
  τ_I * dI/dt = -I + S(w_IE * E - w_II * I + I_ext_I)

  Onde S(x) = 1 / (1 + exp(-x))  (função sigmoide)
```

### Bandas de frequência

| Banda | Frequência (Hz) | Geração | Função | Oscilação dominante |
|-------|----------------|---------|--------|-------------------|
| **Delta** | 0,5-4 | Tálamo + córtex | Sono profundo, anestesia | Alto sincronismo |
| **Teta** | 4-8 | Hipocampo (pacemaker septal) | Navegação, memória episódica, REM | Theta-gamma coupling |
| **Alfa** | 8-13 | Córtex (occipital, somatossensorial) | Repouso com olhos fechados, supressão ativa | Idling rhythm |
| **Beta** | 13-30 | Córtex motor e sensorial | Movimento voluntário, atenção ativa | Ready state |
| **Gama** | 30-80+ | Interneurônios fast-spiking (PV+) | Binding perceptual, atenção, consciência | Sincronia de alta frequência |

### Acoplamento Theta-Gama

```
Potencial de campo local (LFP) — Hipocampo de rato:

  Theta (8 Hz): ────\────/────\────/────\────/────
                     │         │ 
  Gamma (40 Hz):    ─┴─┐  ┌─┐ └  ┐┌  └─┐  ┌─┐ ┌
                    │  └──┘ └──┘  └┘  └──┘ └──┘ │

  Cada ciclo teta contém 4-8 ciclos gama.
  Gama em fase ascendente do teta: codificação (encoding)
  Gama em fase descendente do teta: recuperação (retrieval)
```

### Oscilações e cognição

- **Memória de trabalho**: a manutenção de informação na WM correlaciona-se com aumento de potência beta e gama em DLPFC.
- **Navegação espacial**: células de lugar no hipocampo disparam em fases específicas do ciclo teta (*phase precession*).
- **Atenção**: oscilações alfa no córtex occipital suprimem processamento de locais não-atendidos.
- **Consciência**: a sincronia gama entre áreas distais é candidata a mecanismo de *binding* (Singer & Gray, 1995).

---

## Colunas Corticais e Hierarquias

### Coluna cortical (Mountcastle, 1957)

O neocórtex é organizado em **colunas** de ~300-500 μm de diâmetro, contendo ~10⁴-10⁵ neurônios, que processam uma função especializada:

```
Camadas do neocórtex (coluna somatossensorial):

  I  (molecular)    ───────  Sinapses apicais, feedback difuso
  II/III (piramidal) ───────  Projeções cortico-corticais (associação)
  IV  (granular)    ───────  Input talâmico (recepção sensorial)
  V   (piramidal)   ───────  Projeções subcorticais (output motor)
  VI  (polimorfa)   ───────  Feedback ao tálamo
```

### Macrocolunas e hipercolunas

- **Macrocoluna**: ~500-1000 μm, contém múltiplas minicolunas com propriedades funcionais relacionadas.
- **Hipercoluna** (Hubel & Wiesel, 1962, 1977): no V1, cada hipercoluna (~1 mm²) contém neurônios sensíveis a todas as orientações de uma região do campo visual.

### Hierarquia cortical

```
Níveis de processamento no córtex visual:

  V1 (córtex estriado) ──→ orientação, bordas, contrastes
        │
  V2 ───────────────────→ forma básica, textura
        │
  V3 ───────────────────→ movimento (global)
        │
  V4 ───────────────────→ cor, forma complexa (faces?)
        │
  V5/MT ────────────────→ movimento (direção, velocidade)
        │
  IT (temporal inferior) ──→ objetos, faces, cenas
        │
  PFC ──────────────────→ categorização, decisão, consciência

  Via ventral (what):   V1 → V2 → V4 → IT → PFC
  Via dorsal (where/how): V1 → V2 → V3 → MT → parietal
```

### Princípios da hierarquia

- **Feedforward** (ascendente): detalhe → abstração (convoluções).
- **Feedback** (descendente): predições → resíduos (expectativas).
- **Lateral**: competição e cooperação entre colunas vizinhas.
- **Especialização**: cada área processa aspectos específicos do estímulo.

---

## Comparação: Redes Biológicas vs. Artificiais

| Característica | Rede Biológica | Rede Artificial (DNN) |
|---------------|---------------|----------------------|
| **Unidade** | Neurônio com dinâmica complexa (HH) | Perceptron: soma ponderada + ativação |
| **Comunicação** | Pulsos discretos (spikes) | Valores contínuos (floats) |
| **Sincronização** | Assíncrona, dependente de spike | Síncrona (batches) |
| **Sinapse** | Química, com dinâmica complexa (STDP, LTP) | Peso escalar, atualizado por gradiente |
| **Plasticidade** | Local (STDP, Hebbiano) + homeostase | Global (backpropagation) |
| **Topologia** | 3D, esparsa (10⁻⁴ conectividade) | 2D camadas, fully-connected ou convolução |
| **Feedback** | Abundante (feedback em todos os níveis) | Limitado (skip connections, resnets) |
| **Energia** | ~20 W (cérebro humano) | ~300-1000 W (GPU moderna) |
| **Paradigma** | Aprendizado local, não-supervisionado | Aprendizado global, supervisionado |

### Limitações das metáforas

1. **Backpropagation não é biológico**: não há evidência de que o cérebro propague gradientes por toda a hierarquia sináptica.
2. **Spikes importam**: a codificação temporal (precise spike timing) carrega informação que DNNs ignoram.
3. **Homeostase e neuromodulação**: o cérebro não apenas aprende pesos, mas regula constantemente excitabilidade, limiares e taxas de disparo.
4. **Custo sináptico**: o cérebro minimiza o comprimento de axônios e o número de sinapses — DNNs maximizam parâmetros.

---

## Computação Neuromórfica

### Definição

Sistemas de hardware e software que imitam a arquitetura e o funcionamento de sistemas nervosos biológicos, usando **spikes** (pulsos discretos) em vez de valores contínuos.

### Plataformas

| Plataforma | Desenvolvedor | Neurônios | Sinapses | Consumo |
|-----------|--------------|-----------|----------|---------|
| **Loihi 2** | Intel | 1M | 120M | < 1 W |
| **TrueNorth** | IBM | 1M | 256M | 70 mW |
| **SpiNNaker** | Manchester | 1M (em 48 chips) | 1B | ~1 kW |
| **BrainScaleS** | Heidelberg | 4M (acelerado 10⁴x real) | 40M | ~400 W |
| **Neurogrid** | Stanford | 1M | 6B | ~5 W |

### Modelo LIF (Leaky Integrate-and-Fire)

Modelo simplificado para hardware neuromórfico:

```python
class LIFNeuron:
    """Neurônio Leaky Integrate-and-Fire."""
    def __init__(self, tau=10.0, v_thresh=-55.0, v_reset=-70.0, v_rest=-65.0):
        self.tau = tau          # constante de tempo (ms)
        self.v_thresh = v_thresh
        self.v_reset = v_reset
        self.v_rest = v_rest
        self.v = v_rest
        self.spiked = False

    def step(self, I_inj, dt=1.0):
        """
        Atualiza potencial de membrana (Euler).
        
        Args:
            I_inj: corrente de entrada (nA)
            dt: passo de tempo (ms)
        
        Returns:
            spike: True se disparou
        """
        dv = (-(self.v - self.v_rest) + I_inj) / self.tau
        self.v += dv * dt
        if self.v >= self.v_thresh:
            self.v = self.v_reset
            self.spiked = True
            return True
        self.spiked = False
        return False

    def reset(self):
        self.v = self.v_rest
        self.spiked = False

# Simular 100 ms de atividade em um neurônio LIF
neuron = LIFNeuron(tau=10.0)
spike_train = []
current = 2.0  # nA constante

for t in range(100):
    spike = neuron.step(current)
    spike_train.append(1 if spike else 0)

firing_rate = sum(spike_train) / 0.1  # spikes/segundo
print(f"Taxa de disparo: {firing_rate:.1f} Hz")
print(f"Trem de spikes (primeiros 50 ms): {''.join(str(s) for s in spike_train[:50])}")
```

### Codificação neural em hardware

- **Rate coding**: informação codificada na taxa de disparo (Hz).
- **Temporal coding**: informação codificada no *timing* preciso dos spikes.
- **Population coding**: informação codificada no padrão de atividade de uma população.
- **Delta modulation**: spikes representam mudanças no sinal, não o valor absoluto.

### Aplicações

- **Processamento sensorial de baixo consumo**: detectores de borda, reconhecimento de áudio.
- **Robótica autônoma**: controle motor com latência ultrabaixa (< 1 ms).
- **Brain-computer interfaces**: processamento de sinais neurais em tempo real.
- **Edge AI**: inferência em dispositivos com bateria limitada (wearables, IoT).

---

## Glossário

| Termo | Definição |
|-------|-----------|
| **Axônio** | Prolongamento do neurônio que conduz potenciais de ação do soma para terminais sinápticos |
| **Dendrito** | Prolongamento ramificado que recebe inputs sinápticos de outros neurônios |
| **Sinapse** | Junção especializada onde um neurônio transmite sinal a outro |
| **Potencial de ação** | Pulsos elétricos de amplitude fixa (~100 mV, ~1-2 ms) que propagam informação |
| **LTP** | Long-Term Potentiation — fortalecimento duradouro de sinapses |
| **LTD** | Long-Term Depression — enfraquecimento duradouro de sinapses |
| **STDP** | Spike-Timing-Dependent Plasticity — plasticidade dependente da ordem temporal de disparos |
| **EPSP** | Excitatory Postsynaptic Potential — potencial pós-sináptico excitatório (despolarizante) |
| **IPSP** | Inhibitory Postsynaptic Potential — potencial pós-sináptico inibitório (hiperpolarizante) |
| **GABA** | Ácido gama-aminobutírico — principal neurotransmissor inibitório do SNC |
| **Glutamato** | Principal neurotransmissor excitatório do SNC |
| **LIF** | Leaky Integrate-and-Fire — modelo simplificado de neurônio para simulação neuromórfica |
| **Mielina** | Bainha isolante produzida por oligodendrócitos (SNC) e células de Schwann (SNP) |
| **Coluna cortical** | Unidade funcional vertical do neocórtex, processando um tipo específico de informação |
| **NMDA** | N-metil-D-aspartato — receptor de glutamato crítico para LTP e plasticidade |
| **Oscilação** | Atividade rítmica sincronizada em uma população neural (delta a gama) |
| **Homeostase sináptica** | Mecanismo que mantém a excitabilidade neural dentro de uma faixa estável |
| **Neuromórfico** | Hardware/software que imita arquiteturas neurais biológicas usando spikes |

---

## Referências

### Artigos fundacionais

- Bi, G. Q. & Poo, M. M. (1998). Synaptic modifications in cultured hippocampal neurons: dependence on spike timing, synaptic strength, and postsynaptic cell type. *Journal of Neuroscience*, 18(24), 10464-10472.
- Bienenstock, E. L., Cooper, L. N. & Munro, P. W. (1982). Theory for the development of neuron selectivity: orientation specificity and binocular interaction in visual cortex. *Journal of Neuroscience*, 2(1), 32-48.
- Bliss, T. V. P. & Lømo, T. (1973). Long-lasting potentiation of synaptic transmission in the dentate area of the anaesthetized rabbit following stimulation of the perforant path. *Journal of Physiology*, 232(2), 331-356.
- Hebb, D. O. (1949). *The Organization of Behavior: A Neuropsychological Theory*. Wiley.
- Hodgkin, A. L. & Huxley, A. F. (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. *Journal of Physiology*, 117(4), 500-544.
- Hubel, D. H. & Wiesel, T. N. (1962). Receptive fields, binocular interaction and functional architecture in the cat's visual cortex. *Journal of Physiology*, 160(1), 106-154.
- McCulloch, W. S. & Pitts, W. (1943). A logical calculus of the ideas immanent in nervous activity. *Bulletin of Mathematical Biophysics*, 5(4), 115-133.
- Mountcastle, V. B. (1957). Modality and topographic properties of single neurons of cat's somatic sensory cortex. *Journal of Neurophysiology*, 20(4), 408-434.
- Oja, E. (1982). Simplified neuron model as a principal component analyzer. *Journal of Mathematical Biology*, 15(3), 267-273.
- Singer, W. & Gray, C. M. (1995). Visual feature integration and the temporal correlation hypothesis. *Annual Review of Neuroscience*, 18, 555-586.
- Turrigiano, G. G. et al. (1998). Activity-dependent scaling of quantal amplitude in neocortical neurons. *Nature*, 391(6670), 892-896.
- Wilson, H. R. & Cowan, J. D. (1972). Excitatory and inhibitory interactions in localized populations of model neurons. *Biophysical Journal*, 12(1), 1-24.

### Livros-texto

- Bear, M. F., Connors, B. W. & Paradiso, M. A. (2020). *Neuroscience: Exploring the Brain* (4th ed.). Wolters Kluwer.
- Dayan, P. & Abbott, L. F. (2001). *Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems*. MIT Press.
- Gerstner, W. & Kistler, W. M. (2002). *Spiking Neuron Models: Single Neurons, Populations, Plasticity*. Cambridge University Press.
- Kandel, E. R. et al. (2021). *Principles of Neural Science* (6th ed.). McGraw-Hill.
- Purves, D. et al. (2018). *Neuroscience* (6th ed.). Sinauer.
- Squire, L. R. et al. (2012). *Fundamental Neuroscience* (4th ed.). Academic Press.

### Computação neuromórfica

- Furber, S. B. (2016). Large-scale neuromorphic computing systems. *Journal of Neural Engineering*, 13(5), 051001.
- Indiveri, G. & Liu, S. C. (2015). Memory and information processing in neuromorphic systems. *Proceedings of the IEEE*, 103(8), 1379-1397.
- Mead, C. (1990). Neuromorphic electronic systems. *Proceedings of the IEEE*, 78(10), 1629-1636.
- Merolla, P. A. et al. (2014). A million spiking-neuron integrated circuit with a scalable communication network and interface. *Science*, 345(6197), 668-673.
- Pfeiffer, M. & Pfeil, T. (2018). Deep learning with spiking neurons: opportunities and challenges. *Frontiers in Neuroscience*, 12, 774.

---

## Veja Também

- [[04-Conhecimentos/07-Humanidades/Neurociencia/Sistemas-de-Memoria]] — plasticidade hipocampal, consolidação e replay
- [[04-Conhecimentos/07-Humanidades/Neurociencia/Consciencia-e-Cerebro]] — atividade neural global e emergência da consciência
- [[04-Conhecimentos/07-Humanidades/Matematica/Algebra-Linear-Essencial]] — base matemática para operações em redes neurais
- [[04-Conhecimentos/07-Humanidades/Matematica/Calculo-e-Otimizacao]] — modelagem de dinâmica de membrana e populações
- [[04-Conhecimentos/07-Humanidades/Matematica/Teoria-da-Informacao]] — codificação de informação em spikes
- [[05-Skills/01-agentic-intelligence/reinforcement-learning]] — paralelos com plasticidade por recompensa (dopamina)

[[04-Conhecimentos/07-Humanidades/Neurociencia/INDEX|← Voltar ao índice de Neurociência]]
