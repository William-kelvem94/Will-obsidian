---
title: "Física Fundamental — Mecânica, Termodinâmica, Ondas, Eletromagnetismo e Óptica"
date: 2026-05-18
area: "Física"
tags: [fisica, mecanica, termodinamica, ondas, eletromagnetismo, optica, gravitacao, conservacao, maxwell]
related:
  - "Conhecimento-Geral/Fisica/Fisica-Quantica"
  - "Conhecimento-Geral/Matematica/Calculo-e-Otimizacao"
  - "Conhecimento-Geral/Matematica/Algebra-Linear-Essencial"
  - "Conhecimento-Geral/Matematica/Teoria-da-Informacao"
  - "Conhecimento-Geral/Neurociencia/Redes-Neurais-Biologicas"
aliases: ["Física Clássica", "Mecânica Newtoniana", "Eletromagnetismo Clássico", "Termodinâmica"]
---

# Física Fundamental — Mecânica, Termodinâmica, Ondas, Eletromagnetismo e Óptica

> *"The most incomprehensible thing about the world is that it is comprehensible."* — Albert Einstein

---

## 1. O que é Física?

A física é a ciência natural que estuda os constituintes fundamentais do universo, as forças que eles exercem entre si e os resultados dessas interações. Em termos mais amplos, a física busca compreender as leis que governam o comportamento da matéria e da energia no espaço e no tempo.

### 1.1 Ramos da Física

A física divide-se tradicionalmente em:

| Ramo | Objeto de Estudo | Escala |
|------|------------------|--------|
| **Mecânica Clássica** | Movimento de corpos sob ação de forças | Macroscópica (v << c) |
| **Termodinâmica** | Calor, temperatura, entropia e processos energéticos | Macroscópica (muitas partículas) |
| **Ondas e Acústica** | Propagação de perturbações em meios | Macroscópica |
| **Eletromagnetismo** | Campos elétricos e magnéticos, luz | Todas as escalas |
| **Óptica** | Luz, visão, instrumentos ópticos | Macroscópica |
| **Mecânica Quântica** | Partículas subatômicas, quantização | Atômica e subatômica |
| **Relatividade** | Altas velocidades e grandes massas | Relativística e cosmológica |

### 1.2 O Método Científico na Física

A física utiliza o método científico de forma rigorosa:

1. **Observação**: coleta de dados experimentais sobre fenômenos naturais
2. **Hipótese**: formulação de uma explicação provisória
3. **Predição**: dedução de consequências testáveis da hipótese
4. **Experimentação**: teste controlado das predições
5. **Análise**: comparação entre predições e resultados experimentais
6. **Teoria**: se a hipótese sobrevive a testes repetidos, pode tornar-se uma teoria consolidada
7. **Revisão**: teorias são constantemente desafiadas e refinadas

> A física difere da matemática por ser uma ciência empírica: suas verdades dependem de verificação experimental. Como disse Richard Feynman: "O princípio da ciência, quase que a definição, é: o teste final de qualquer teoria é a experimentação."

### 1.3 Grandezas Físicas e Unidades

O **Sistema Internacional de Unidades (SI)** define sete grandezas fundamentais:

| Grandeza | Unidade | Símbolo |
|----------|---------|---------|
| Comprimento | metro | m |
| Massa | quilograma | kg |
| Tempo | segundo | s |
| Corrente elétrica | ampère | A |
| Temperatura | kelvin | K |
| Quantidade de substância | mol | mol |
| Intensidade luminosa | candela | cd |

Todas as demais grandezas físicas derivam destas sete. Por exemplo, força (newton, N = kg·m/s²), energia (joule, J = N·m = kg·m²/s²), potência (watt, W = J/s).

### 1.4 Análise Dimensional

A análise dimensional é uma ferramenta poderosa para verificar a consistência de equações físicas e derivar relações entre grandezas. Cada grandeza física possui uma dimensão que pode ser expressa em termos das dimensões fundamentais M (massa), L (comprimento), T (tempo), I (corrente), Θ (temperatura), N (quantidade), J (intensidade luminosa).

Por exemplo, a energia cinética $E_c = \frac{1}{2}mv^2$ tem dimensões:
- $[E_c] = [m][v]^2 = M \cdot (L/T)^2 = ML^2T^{-2}$

---

## 2. Mecânica Clássica

A mecânica clássica, formulada principalmente por Isaac Newton no *Philosophiæ Naturalis Principia Mathematica* (1687), descreve o movimento de corpos macroscópicos a velocidades muito menores que a da luz.

### 2.1 Leis de Newton

#### Primeira Lei — Lei da Inércia

> Um corpo permanece em repouso ou em movimento retilíneo uniforme a menos que uma força resultante externa atue sobre ele.

Matematicamente: se $\vec{F}_{\text{res}} = 0$, então $\vec{v} = \text{constante}$.

Esta lei define o conceito de **referencial inercial**: um referencial onde a primeira lei é válida. A Terra é aproximadamente um referencial inercial para muitos propósitos práticos.

#### Segunda Lei — Princípio Fundamental da Dinâmica

> A taxa de variação do momento linear de um corpo é proporcional à força resultante que atua sobre ele e ocorre na direção desta força.

Para massa constante:
$$\vec{F} = m\vec{a} = m\frac{d\vec{v}}{dt} = m\frac{d^2\vec{r}}{dt^2}$$

Para massa variável (caso geral):
$$\vec{F} = \frac{d\vec{p}}{dt} \quad \text{onde} \quad \vec{p} = m\vec{v}$$

#### Terceira Lei — Ação e Reação

> Para toda ação há uma reação de igual magnitude e direção oposta.

$$\vec{F}_{12} = -\vec{F}_{21}$$

Se o corpo 1 exerce uma força sobre o corpo 2, o corpo 2 exerce uma força de mesma intensidade e direção, mas sentido oposto, sobre o corpo 1.

### 2.2 Forças Fundamentais

Na física clássica, reconhecemos várias forças que, em última análise, derivam de quatro interações fundamentais:

1. **Força Gravitacional**: atração entre massas ($F = G\frac{m_1 m_2}{r^2}$)
2. **Força Eletromagnética**: interação entre cargas elétricas (lei de Coulomb, magnetismo)
3. **Força Nuclear Forte**: mantém prótons e nêutrons no núcleo
4. **Força Nuclear Fraca**: responsável por certos tipos de decaimento radioativo

Na mecânica clássica, trabalhamos principalmente com forças derivadas destas:

| Força | Equação | Descrição |
|-------|---------|-----------|
| Peso | $\vec{P} = m\vec{g}$ | Atração gravitacional da Terra |
| Normal | $\vec{N}$ | Reação perpendicular de superfícies |
| Atrito | $f_a = \mu N$ | Resistência ao movimento entre superfícies |
| Tração | $\vec{T}$ | Força transmitida por fios/cabos |
| Elástica | $\vec{F}_e = -k\vec{x}$ | Lei de Hooke (molas) |
| Centrípeta | $F_c = \frac{mv^2}{r}$ | Força que mantém movimento circular |

### 2.3 Leis de Conservação

As leis de conservação estão no coração da física. Elas refletem simetrias fundamentais da natureza (Teorema de Noether, 1918).

#### Conservação do Momento Linear

Em um sistema isolado (sem forças externas), o momento linear total permanece constante:
$$\vec{p}_{\text{total}} = \sum_i \vec{p}_i = \text{constante}$$

Esta lei está relacionada à simetria de translação espacial.

#### Conservação do Momento Angular

Em um sistema isolado, o momento angular total permanece constante:
$$\vec{L}_{\text{total}} = \sum_i \vec{r}_i \times \vec{p}_i = \text{constante}$$

Relacionada à simetria de rotação espacial.

#### Conservação da Energia Mecânica

Na ausência de forças dissipativas (atrito, resistência do ar), a energia mecânica total se conserva:
$$E_{\text{mec}} = E_c + E_p = \text{constante}$$

Onde:
- $E_c = \frac{1}{2}mv^2$ (energia cinética)
- $E_p = mgh$ (energia potencial gravitacional, perto da superfície)
- $E_p = \frac{1}{2}kx^2$ (energia potencial elástica)

Em sistemas com dissipação, a energia total (incluindo calor) ainda se conserva — é a primeira lei da termodinâmica.

### 2.4 Gravitação Universal

A lei da gravitação universal de Newton estabelece que duas massas quaisquer se atraem com uma força proporcional ao produto de suas massas e inversamente proporcional ao quadrado da distância entre seus centros:
$$F = G\frac{m_1 m_2}{r^2}$$

Onde $G = 6,674 \times 10^{-11} \, \text{N·m}^2/\text{kg}^2$ é a constante gravitacional.

#### Consequências da Gravitação

- **Órbitas planetárias**: as leis de Kepler derivam da gravitação newtoniana
  1. Órbitas são elípticas com o Sol em um dos focos
  2. O raio vetor varre áreas iguais em tempos iguais
  3. $T^2 \propto a^3$ (período ao quadrado proporcional ao semi-eixo maior ao cubo)
- **Velocidade de escape**: $v_e = \sqrt{2GM/R}$
- **Campo gravitacional**: $\vec{g}(\vec{r}) = -G\frac{M}{r^2}\hat{r}$

### 2.5 Trabalho e Energia

O conceito de **trabalho** em física difere do uso cotidiano:
$$W = \int \vec{F} \cdot d\vec{r}$$

Para uma força constante: $W = F \cdot d \cdot \cos\theta$.

O **teorema do trabalho-energia cinética** estabelece:
$$W_{\text{total}} = \Delta E_c = \frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2$$

A **potência** é a taxa de realização de trabalho:
$$P = \frac{dW}{dt} = \vec{F} \cdot \vec{v}$$

### 2.6 Mecânica dos Fluidos

A mecânica dos fluidos estuda o comportamento de líquidos e gases.

#### Hidrostática

- **Pressão**: $P = F/A$ (unidade: pascal, Pa = N/m²)
- **Princípio de Pascal**: a pressão aplicada a um fluido confinado transmite-se igualmente a todos os pontos
- **Princípio de Arquimedes**: todo corpo imerso em um fluido sofre uma força de empuxo igual ao peso do fluido deslocado
  $$E = \rho_{\text{fluido}} \cdot V_{\text{deslocado}} \cdot g$$
- **Pressão hidrostática**: $P = P_0 + \rho gh$

#### Hidrodinâmica

- **Equação da continuidade**: $A_1 v_1 = A_2 v_2$ (conservação da vazão)
- **Equação de Bernoulli**: $P + \frac{1}{2}\rho v^2 + \rho gh = \text{constante}$
  Esta equação explica desde a sustentação de aviões até o funcionamento de carburadores e atomizadores.

### 2.7 Oscilações e Movimento Harmônico

O **movimento harmônico simples (MHS)** é um dos movimentos mais importantes da física, descrevendo desde molas até circuitos elétricos oscilantes.

A equação diferencial do MHS:
$$\frac{d^2x}{dt^2} + \omega^2 x = 0$$

Solução: $x(t) = A\cos(\omega t + \phi)$, onde:
- $A$ = amplitude máxima
- $\omega$ = frequência angular ($\omega = \sqrt{k/m}$ para um sistema massa-mola)
- $\phi$ = fase inicial
- Período $T = 2\pi/\omega$
- Frequência $f = 1/T = \omega/2\pi$

#### Energia no MHS

$$E_{\text{total}} = \frac{1}{2}kA^2 = \frac{1}{2}mv_{\text{máx}}^2$$

A energia oscila entre cinética e potencial, mas a soma permanece constante.

#### Oscilações Amortecidas e Forçadas

- **Amortecimento**: a amplitude decai exponencialmente devido à dissipação: $x(t) = Ae^{-bt/2m}\cos(\omega't + \phi)$
- **Ressonância**: quando a frequência de uma força externa coincide com a frequência natural do sistema, a amplitude aumenta drasticamente — fenômeno crucial em engenharia (pontes, edifícios, instrumentos musicais)

---

## 3. Termodinâmica

A termodinâmica estuda as relações entre calor, trabalho, temperatura e energia. Diferentemente da mecânica, que descreve sistemas de poucas partículas, a termodinâmica trata de sistemas com um número enorme de partículas ($\sim 10^{23}$), usando conceitos estatísticos.

### 3.1 Conceitos Fundamentais

| Conceito | Definição | Unidade |
|----------|-----------|---------|
| **Sistema** | Porção do universo sendo estudada | — |
| **Vizinhança** | Resto do universo | — |
| **Fronteira** | Separa sistema de vizinhança | — |
| **Estado** | Condição do sistema definida por variáveis termodinâmicas | — |
| **Variável de estado** | Grandeza que define o estado ($P, V, T, U, S$) | — |
| **Processo** | Mudança de estado do sistema | — |
| **Temperatura** | Medida da energia cinética média das partículas | K |
| **Calor** | Energia transferida devido à diferença de temperatura | J |
| **Trabalho** | Energia transferida por meios mecânicos | J |
| **Energia interna** | Soma das energias cinética e potencial das partículas | J |

### 3.2 Lei Zero da Termodinâmica

> Se dois sistemas estão em equilíbrio térmico com um terceiro, então eles estão em equilíbrio térmico entre si.

Esta lei estabelece o conceito de **temperatura** como uma propriedade física mensurável e justifica o uso de termômetros.

### 3.3 Primeira Lei da Termodinâmica

> A energia não pode ser criada nem destruída, apenas transformada ou transferida.

$$\Delta U = Q - W$$

Onde:
- $\Delta U$ = variação da energia interna do sistema
- $Q$ = calor adicionado ao sistema
- $W$ = trabalho realizado pelo sistema

Para processos infinitesimais:
$$dU = \delta Q - \delta W$$

Note que $U$ é uma função de estado (diferencial exata), enquanto $Q$ e $W$ dependem do caminho (diferenciais inexatas).

#### Aplicações da Primeira Lei

| Processo | Condição | Consequência |
|----------|----------|--------------|
| Adiabático | $Q = 0$ | $\Delta U = -W$ |
| Isocórico (volume constante) | $W = 0$ | $\Delta U = Q$ |
| Isotérmico (temperatura constante) | $\Delta U = 0$ | $Q = W$ |
| Cíclico | $\Delta U = 0$ | $Q = W$ |

### 3.4 Segunda Lei da Termodinâmica

A segunda lei impõe uma direção para os processos naturais.

#### Formulações Históricas

- **Kelvin-Planck**: é impossível construir uma máquina térmica que converta integralmente calor em trabalho
- **Clausius**: é impossível transferir calor espontaneamente de um corpo frio para um corpo quente

#### Entropia

A entropia ($S$) é o conceito central da segunda lei. Em termos macroscópicos:
$$dS \geq \frac{\delta Q}{T}$$

Para processos reversíveis: $dS = \delta Q/T$. Para processos irreversíveis: $dS > \delta Q/T$.

A segunda lei afirma que a entropia total do universo sempre aumenta em processos reais:
$$\Delta S_{\text{universo}} \geq 0$$

#### Interpretação Estatística da Entropia (Boltzmann)

Ludwig Boltzmann forneceu uma interpretação microscópica revolucionária:
$$S = k_B \ln \Omega$$

Onde $\Omega$ é o número de microestados correspondentes a um dado macroestado, e $k_B = 1,381 \times 10^{-23} \, \text{J/K}$ é a constante de Boltzmann.

Esta equação está gravada no túmulo de Boltzmann em Viena e conecta diretamente a termodinâmica com a [[Conhecimento-Geral/Matematica/Teoria-da-Informacao]].

> **Conexão com Teoria da Informação**: Claude Shannon, ao desenvolver a teoria da informação em 1948, definiu a entropia da informação como $H = -\sum p_i \log_2 p_i$, uma forma matemática idêntica à entropia de Boltzmann-Gibbs. A entropia termodinâmica mede a desordem de um sistema físico; a entropia da informação mede a incerteza de uma variável aleatória. Ambas expressam o mesmo princípio subjacente: o número de estados possíveis de um sistema. Esta conexão é explorada em [[Conhecimento-Geral/Matematica/Teoria-da-Informacao]].

### 3.5 Terceira Lei da Termodinâmica

> A entropia de um cristal perfeito se aproxima de zero quando a temperatura se aproxima do zero absoluto.

$$\lim_{T \to 0} S = 0$$

Consequências:
- É impossível atingir o zero absoluto em um número finito de etapas
- Próximo ao zero absoluto, os calores específicos tendem a zero
- A terceira lei permite definir escalas de entropia absoluta

### 3.6 Máquinas Térmicas e Ciclos

Uma máquina térmica opera em ciclos, extraindo calor de uma fonte quente, convertendo parte em trabalho e rejeitando o restante para uma fonte fria.

#### Ciclo de Carnot

O ciclo de Carnot é o ciclo termodinâmico mais eficiente possível entre duas temperaturas. Consiste em quatro etapas reversíveis:
1. Expansão isotérmica (contato com fonte quente $T_H$)
2. Expansão adiabática
3. Compressão isotérmica (contato com fonte fria $T_C$)
4. Compressão adiabática

**Eficiência de Carnot** (máxima teórica):
$$\eta_{\text{Carnot}} = 1 - \frac{T_C}{T_H}$$

Nenhuma máquina real pode exceder esta eficiência.

#### Outros Ciclos

| Ciclo | Aplicação | Característica |
|-------|-----------|----------------|
| **Otto** | Motores a gasolina | Ignição por centelha |
| **Diesel** | Motores a diesel | Ignição por compressão |
| **Rankine** | Usinas termelétricas | Mudança de fase (água-vapor) |
| **Brayton** | Turbinas a gás | Combustão contínua |
| **Refrigeração** | Geladeiras, ar condicionado | Ciclo reverso |

### 3.7 Gases Ideais vs. Gases Reais

#### Gás Ideal

Equação de estado:
$$PV = nRT$$

Onde $R = 8,314 \, \text{J/(mol·K)}$ é a constante universal dos gases.

#### Gás Real (van der Waals)
$$\left(P + a\frac{n^2}{V^2}\right)(V - nb) = nRT$$

Onde $a$ corrige as forças de atração intermoleculares e $b$ corrige o volume finito das moléculas.

### 3.8 Transições de Fase

Transições de fase ocorrem quando a matéria muda de um estado para outro:

| Transição | De → Para | Condição |
|-----------|-----------|----------|
| Fusão | Sólido → Líquido | Aumento de T |
| Vaporização | Líquido → Gás | Aumento de T |
| Condensação | Gás → Líquido | Diminuição de T |
| Solidificação | Líquido → Sólido | Diminuição de T |
| Sublimação | Sólido → Gás | Baixa P, aumento T |
| Deposição | Gás → Sólido | Baixa P, diminuição T |

O **diagrama de fases** mostra as condições de pressão e temperatura para cada fase, incluindo o **ponto triplo** (onde as três fases coexistem) e o **ponto crítico** (acima do qual líquido e gás são indistinguíveis).

---

## 4. Ondas e Acústica

Ondas são perturbações que se propagam através de um meio (ou do vácuo, no caso de ondas eletromagnéticas) transportando energia sem transportar matéria.

### 4.1 Classificação das Ondas

| Critério | Tipo | Exemplo |
|----------|------|---------|
| **Natureza** | Mecânica | Som, ondas em cordas |
| | Eletromagnética | Luz, rádio, raios X |
| | Matéria | Ondas de matéria (mecânica quântica) |
| **Direção de vibração** | Transversal | Vibração perpendicular à propagação (luz, ondas em cordas) |
| | Longitudinal | Vibração paralela à propagação (som) |
| | Mista | Ondas na superfície da água |
| **Dimensão** | Unidimensional | Ondas em cordas |
| | Bidimensional | Ondas na superfície da água |
| | Tridimensional | Som no ar, luz |

### 4.2 Propriedades das Ondas

#### Parâmetros Fundamentais

| Parâmetro | Símbolo | Definição | Unidade |
|-----------|---------|-----------|---------|
| Amplitude | $A$ | Deslocamento máximo da posição de equilíbrio | m |
| Comprimento de onda | $\lambda$ | Distância entre dois pontos equivalentes consecutivos | m |
| Período | $T$ | Tempo para uma oscilação completa | s |
| Frequência | $f$ | Número de oscilações por segundo ($f = 1/T$) | Hz |
| Velocidade | $v$ | $v = \lambda f = \lambda/T$ | m/s |

#### Função de Onda

Para uma onda progressiva unidimensional:
$$y(x,t) = A\cos(kx - \omega t + \phi)$$

Onde:
- $k = 2\pi/\lambda$ = número de onda
- $\omega = 2\pi f$ = frequência angular
- $\phi$ = fase inicial

A equação de onda geral (unidimensional):
$$\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2 y}{\partial t^2}$$

### 4.3 Fenômenos Ondulatórios

#### Interferência

Quando duas ou mais ondas se encontram no mesmo ponto, o deslocamento resultante é a soma algébrica dos deslocamentos individuais (**princípio da superposição**).

- **Interferência construtiva**: cristas coincidem com cristas (aumento de amplitude)
  - Condição: diferença de caminho $\Delta r = n\lambda$ ($n$ inteiro)
- **Interferência destrutiva**: cristas coincidem com vales (cancelamento)
  - Condição: diferença de caminho $\Delta r = (n+1/2)\lambda$

#### Difração

A difração é o desvio de uma onda ao encontrar um obstáculo ou fenda. A quantidade de difração depende da relação entre o comprimento de onda e o tamanho do obstáculo:
- Se $\lambda \gg$ obstáculo: difração pronunciada
- Se $\lambda \ll$ obstáculo: propagação aproximadamente retilínea

#### Reflexão

Uma onda reflete-se ao encontrar uma interface entre dois meios:
- **Reflexão em extremidade fixa**: inversão de fase
- **Reflexão em extremidade livre**: sem inversão de fase
- **Lei da reflexão**: ângulo de incidência = ângulo de reflexão

#### Refração

Quando uma onda passa de um meio para outro, sua velocidade e comprimento de onda mudam, mas a frequência permanece constante. Isso causa a mudança de direção:
$$\frac{\sin\theta_1}{\sin\theta_2} = \frac{v_1}{v_2} = \text{constante}$$

#### Ressonância

A ressonância ocorre quando a frequência de uma força externa coincide com a frequência natural do sistema, causando um aumento máximo de amplitude. Exemplos:
- Instrumentos musicais (cordas, tubos)
- Pontes e edifícios (engenharia sísmica)
- Circuitos RLC elétricos

#### Ondas Estacionárias

Ondas estacionárias são formadas pela superposição de duas ondas de mesma frequência e amplitude propagando-se em direções opostas. Pontos de amplitude zero são **nós**; pontos de amplitude máxima são **ventres** ou **antinós**.

Para uma corda de comprimento $L$ com extremidades fixas:
$$f_n = n\frac{v}{2L} = n\frac{1}{2L}\sqrt{\frac{T}{\mu}} \quad (n = 1, 2, 3, ...)$$

Onde $n=1$ é o **modo fundamental** (primeiro harmônico), $n=2$ é o segundo harmônico, etc.

### 4.4 Acústica

O som é uma onda mecânica longitudinal que se propaga em meios materiais (sólidos, líquidos, gases).

#### Velocidade do Som

- No ar (20°C): ~343 m/s
- Na água: ~1482 m/s
- No aço: ~5960 m/s

A velocidade do som em um gás ideal: $v = \sqrt{\gamma RT/M}$, onde $\gamma = C_P/C_V$.

#### Intensidade Sonora

A intensidade de uma onda sonora é a potência por unidade de área:
$$I = \frac{P}{A} = \frac{1}{2}\rho v \omega^2 A^2$$

O **nível de intensidade sonora** usa a escala logarítmica de decibéis (dB):
$$\beta = 10\log_{10}\left(\frac{I}{I_0}\right)$$

Onde $I_0 = 10^{-12} \,\text{W/m}^2$ é o limiar da audição humana.

#### Efeito Doppler

O aparente aumento ou diminuição da frequência de uma onda devido ao movimento relativo entre fonte e observador:
$$f' = f\frac{v \pm v_o}{v \mp v_f}$$

- Fonte e observador se aproximando: $f' > f$ (tom mais agudo)
- Fonte e observador se afastando: $f' < f$ (tom mais grave)

O efeito Doppler tem aplicações em radar, sonar, astronomia (desvio para o vermelho) e diagnósticos médicos (ultrassom Doppler).

#### Batimento

O batimento ocorre quando duas ondas de frequências ligeiramente diferentes se superpõem:
$$f_{\text{batimento}} = |f_1 - f_2|$$

### 4.5 Ondas na Física Moderna

O conceito de ondas transcendeu a física clássica com:
- **Dualidade onda-partícula** (mecânica quântica): partículas como elétrons exibem comportamento ondulatório (ver [[Conhecimento-Geral/Fisica/Fisica-Quantica]])
- **Ondas gravitacionais**: ondulações no espaço-tempo previstas por Einstein (1916) e detectadas pelo LIGO em 2015

---

## 5. Eletromagnetismo

O eletromagnetismo unifica os fenômenos elétricos e magnéticos em uma única teoria. James Clerk Maxwell consumou esta unificação em 1864 com suas famosas equações.

### 5.1 Eletrostática

#### Carga Elétrica

A carga elétrica é uma propriedade fundamental da matéria, quantizada em múltiplos da carga elementar $e = 1,602 \times 10^{-19} \, \text{C}$.

| Partícula | Carga | Massa |
|-----------|-------|-------|
| Próton | $+e$ | $1,673 \times 10^{-27}$ kg |
| Elétron | $-e$ | $9,109 \times 10^{-31}$ kg |
| Nêutron | 0 | $1,675 \times 10^{-27}$ kg |

Princípios da eletrostática:
1. Cargas de mesmo sinal se repelem, cargas de sinais opostos se atraem
2. A carga total de um sistema isolado se conserva

#### Lei de Coulomb

A força entre duas cargas puntiformes é proporcional ao produto das cargas e inversamente proporcional ao quadrado da distância:
$$\vec{F} = k_e \frac{q_1 q_2}{r^2}\hat{r} = \frac{1}{4\pi\varepsilon_0}\frac{q_1 q_2}{r^2}\hat{r}$$

Onde $k_e = 8,988 \times 10^9 \, \text{N·m}^2/\text{C}^2$ e $\varepsilon_0 = 8,854 \times 10^{-12} \, \text{C}^2/(\text{N·m}^2)$ é a permissividade do vácuo.

#### Campo Elétrico

O campo elétrico $\vec{E}$ é definido como a força por unidade de carga:
$$\vec{E} = \frac{\vec{F}}{q}$$

Para uma carga pontual: $\vec{E} = \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\hat{r}$

#### Lei de Gauss

O fluxo elétrico total através de uma superfície fechada é proporcional à carga total no interior:
$$\oint \vec{E} \cdot d\vec{A} = \frac{Q_{\text{int}}}{\varepsilon_0}$$

A lei de Gauss é uma das quatro equações de Maxwell e é particularmente útil para calcular campos elétricos em situações de alta simetria.

#### Potencial Elétrico

O potencial elétrico $V$ é a energia potencial por unidade de carga:
$$V(\vec{r}) = -\int_{\infty}^{\vec{r}} \vec{E} \cdot d\vec{l}$$

Para uma carga pontual: $V(r) = \frac{1}{4\pi\varepsilon_0}\frac{q}{r}$

A diferença de potencial (tensão) entre dois pontos é:
$$\Delta V = V_b - V_a = -\int_a^b \vec{E} \cdot d\vec{l}$$

#### Capacitância

Um capacitor armazena energia no campo elétrico:
$$C = \frac{Q}{V}$$

Energia armazenada: $U = \frac{1}{2}CV^2 = \frac{Q^2}{2C}$

| Tipo de Capacitor | Capacitância |
|-------------------|--------------|
| Placas paralelas | $C = \varepsilon_0 \frac{A}{d}$ |
| Cilíndrico | $C = \frac{2\pi\varepsilon_0 L}{\ln(b/a)}$ |
| Esférico | $C = 4\pi\varepsilon_0 \frac{ab}{b-a}$ |

### 5.2 Corrente Elétrica

A corrente elétrica é o fluxo de cargas através de um condutor:
$$I = \frac{dQ}{dt} = nqv_dA$$

Onde $n$ é a densidade de portadores, $q$ a carga de cada portador, $v_d$ a velocidade de deriva e $A$ a área da seção transversal.

#### Lei de Ohm

Para muitos materiais (ôhmicos), a corrente é proporcional à tensão:
$$V = RI \quad \text{ou} \quad \vec{J} = \sigma\vec{E}$$

Onde $R$ é a resistência e $\sigma$ é a condutividade.

A resistência de um fio: $R = \rho\frac{L}{A}$, onde $\rho = 1/\sigma$ é a resistividade.

#### Potência Elétrica

$$P = VI = I^2R = \frac{V^2}{R}$$

#### Circuitos Elétricos

**Associação de Resistores**:
- Série: $R_{eq} = R_1 + R_2 + ... + R_n$
- Paralelo: $\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + ... + \frac{1}{R_n}$

**Leis de Kirchhoff**:
1. **Lei dos Nós**: a soma das correntes que entram em um nó é zero (conservação da carga)
2. **Lei das Malhas**: a soma das diferenças de potencial em torno de qualquer malha fechada é zero (conservação da energia)

#### Circuitos RC

- Carga do capacitor: $q(t) = Q_{\text{máx}}(1 - e^{-t/RC})$
- Descarga: $q(t) = Q_0 e^{-t/RC}$
- Constante de tempo: $\tau = RC$

### 5.3 Magnetismo

#### Campo Magnético

O campo magnético $\vec{B}$ é produzido por cargas em movimento. A força sobre uma carga em movimento é a **força de Lorentz**:
$$\vec{F} = q(\vec{v} \times \vec{B})$$

Força sobre um fio condutor: $\vec{F} = I(\vec{L} \times \vec{B})$

#### Lei de Biot-Savart

O campo magnético produzido por um elemento de corrente:
$$d\vec{B} = \frac{\mu_0}{4\pi}\frac{I\,d\vec{l} \times \hat{r}}{r^2}$$

Onde $\mu_0 = 4\pi \times 10^{-7} \, \text{T·m/A}$ é a permeabilidade do vácuo.

#### Lei de Ampère (antes de Maxwell)

A integral de linha de $\vec{B}$ em torno de uma curva fechada é proporcional à corrente que atravessa a superfície delimitada:
$$\oint \vec{B} \cdot d\vec{l} = \mu_0 I_{\text{int}}$$

#### Indução Eletromagnética

**Lei de Faraday-Lenz**: a força eletromotriz induzida em um circuito é igual à taxa de variação do fluxo magnético através do circuito:
$$\mathcal{E} = -\frac{d\Phi_B}{dt}$$

Onde $\Phi_B = \int \vec{B} \cdot d\vec{A}$.

O sinal negativo representa a **lei de Lenz**: a corrente induzida cria um campo magnético que se opõe à variação do fluxo.

#### Indutância

$$L = \frac{N\Phi_B}{I}$$

Energia armazenada em um indutor: $U = \frac{1}{2}LI^2$

Circuitos RL:
$$I(t) = I_{\text{máx}}(1 - e^{-t/\tau}), \quad \tau = L/R$$

### 5.4 Equações de Maxwell

As equações de Maxwell são a formulação completa do eletromagnetismo clássico:

| Nome | Forma Integral | Forma Diferencial |
|------|---------------|-------------------|
| Lei de Gauss (elétrica) | $\oint \vec{E} \cdot d\vec{A} = \frac{Q_{\text{int}}}{\varepsilon_0}$ | $\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}$ |
| Lei de Gauss (magnética) | $\oint \vec{B} \cdot d\vec{A} = 0$ | $\nabla \cdot \vec{B} = 0$ |
| Lei de Faraday | $\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi_B}{dt}$ | $\nabla \times \vec{E} = -\frac{\partial\vec{B}}{\partial t}$ |
| Lei de Ampère-Maxwell | $\oint \vec{B} \cdot d\vec{l} = \mu_0 I + \mu_0\varepsilon_0\frac{d\Phi_E}{dt}$ | $\nabla \times \vec{B} = \mu_0\vec{J} + \mu_0\varepsilon_0\frac{\partial\vec{E}}{\partial t}$ |

As equações de Maxwell preveem:
1. A existência de ondas eletromagnéticas
2. A velocidade da luz como $c = 1/\sqrt{\mu_0\varepsilon_0} \approx 3,00 \times 10^8 \, \text{m/s}$
3. Que a luz é uma onda eletromagnética
4. A conservação da carga elétrica

### 5.5 Ondas Eletromagnéticas

Uma onda eletromagnética consiste em campos elétrico e magnético oscilantes e perpendiculares entre si e à direção de propagação.

#### Propriedades

- Velocidade no vácuo: $c = 3,00 \times 10^8 \, \text{m/s}$
- Relação entre campos: $E = cB$
- Transportam energia e momento
- Não necessitam de meio material para propagação

#### Espectro Eletromagnético

| Faixa | Comprimento de Onda | Frequência | Aplicações |
|-------|-------------------|------------|------------|
| Ondas de rádio | $> 1$ m | $< 300$ MHz | Rádio, TV, comunicações |
| Micro-ondas | $1$ m — $1$ mm | $300$ MHz — $300$ GHz | Radar, fornos, WiFi |
| Infravermelho | $1$ mm — $700$ nm | $300$ GHz — $430$ THz | Aquecimento, sensores |
| Luz visível | $700$ — $400$ nm | $430$ — $750$ THz | Visão humana |
| Ultravioleta | $400$ — $10$ nm | $750$ THz — $30$ PHz | Esterilização, bronzeamento |
| Raios X | $10$ nm — $0,01$ nm | $30$ PHz — $30$ EHz | Radiografia, cristalografia |
| Raios Gama | $< 0,01$ nm | $> 30$ EHz | Radioatividade, astronomia |

### 5.6 Aplicações Tecnológicas do Eletromagnetismo

| Tecnologia | Princípio Físico |
|------------|------------------|
| Geradores elétricos | Indução eletromagnética (Faraday) |
| Motores elétricos | Força magnética sobre condutores |
| Transformadores | Indução mútua entre bobinas |
| Rádio e TV | Ondas eletromagnéticas, modulação |
| Ressonância Magnética (MRI) | Precessão nuclear em campo magnético |
| Microfones e alto-falantes | Conversão eletroacústica |
| Cabos coaxiais e guias de onda | Propagação confinada de ondas EM |

---

## 6. Óptica

A óptica estuda o comportamento da luz e sua interação com a matéria.

### 6.1 Natureza da Luz

Historicamente, duas teorias disputaram a natureza da luz:
- **Teoria corpuscular** (Newton): luz composta por partículas
- **Teoria ondulatória** (Huygens, Young, Fresnel): luz como onda

Hoje sabemos que a luz exibe **dualidade onda-partícula**: comporta-se como onda na propagação e como partícula (fóton) na interação com a matéria (ver [[Conhecimento-Geral/Fisica/Fisica-Quantica]]).

### 6.2 Reflexão da Luz

#### Leis da Reflexão

1. O raio incidente, o raio refletido e a normal estão no mesmo plano
2. O ângulo de incidência é igual ao ângulo de reflexão: $\theta_i = \theta_r$

#### Tipos de Reflexão

- **Reflexão especular**: superfície lisa → imagem nítida
- **Reflexão difusa**: superfície rugosa → luz espalhada em todas as direções

#### Espelhos

| Tipo | Imagem | Característica |
|------|--------|----------------|
| Plano | Virtual, direita, mesmo tamanho | $d_o = d_i$ |
| Côncavo | Real ou virtual | Depende da posição do objeto |
| Convexo | Virtual, direita, menor | $f < 0$, campo ampliado |

Equação dos espelhos esféricos:
$$\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}, \quad f = \frac{R}{2}$$

Aumento lateral: $m = -\frac{d_i}{d_o}$

### 6.3 Refração da Luz

#### Lei de Snell-Descartes

Quando a luz passa de um meio para outro:
$$n_1 \sin\theta_1 = n_2 \sin\theta_2$$

Onde $n = c/v$ é o índice de refração do meio.

#### Índices de Refração

| Meio | $n$ |
|------|-----|
| Vácuo | 1,0000 |
| Ar | 1,0003 |
| Água | 1,333 |
| Vidro (crown) | 1,52 |
| Vidro (flint) | 1,66 |
| Diamante | 2,42 |

#### Reflexão Interna Total

Quando a luz tenta passar de um meio mais refringente para outro menos refringente, ocorre reflexão total se $\theta_i > \theta_c$, onde:
$$\theta_c = \arcsin\left(\frac{n_2}{n_1}\right)$$

Aplicação: fibras ópticas, guias de luz, endoscópios.

#### Dispersão

O índice de refração depende do comprimento de onda. A luz branca, ao passar por um prisma, decompõe-se nas cores do arco-íris (dispersão cromática). Este fenômeno explica o arco-íris natural.

### 6.4 Lentes

#### Tipos de Lentes

| Tipo | Forma | Efeito em raios paralelos |
|------|-------|---------------------------|
| Convergente | Biconvexa | Focam em um ponto real |
| Divergente | Bicôncava | Divergem (ponto focal virtual) |

#### Equação das Lentes Delgadas

$$\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}$$

Equação do fabricante de lentes:
$$\frac{1}{f} = (n - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$$

#### Instrumentos Ópticos

| Instrumento | Componentes | Função |
|-------------|------------|--------|
| Lupa | Lente convergente | Ampliar objetos próximos |
| Microscópio | Duas lentes convergentes | Ampliar objetos muito pequenos |
| Telescópio refrator | Objetiva + ocular | Observar objetos distantes |
| Telescópio refletor | Espelho côncavo + ocular | Observar objetos distantes sem aberração cromática |
| Câmera fotográfica | Lente + diafragma + filme/sensor | Registrar imagens |
| Olho humano | Córnea + cristalino + retina | Visão natural |

### 6.5 Óptica Física

#### Interferência

O experimento da dupla fenda de Young demonstrou a natureza ondulatória da luz. Franjas de interferência ocorrem quando:
$$d\sin\theta = m\lambda \quad \text{(máximos, } m = 0, 1, 2, ...)$$
$$d\sin\theta = \left(m + \frac{1}{2}\right)\lambda \quad \text{(mínimos)}$$

#### Difração

A difração por uma fenda única produz um padrão com máximo central e máximos secundários decrescentes:
$$\sin\theta = m\frac{\lambda}{a} \quad \text{(mínimos, } m = 1, 2, 3, ...)$$

#### Redes de Difração

Uma rede de difração é um conjunto de muitas fendas paralelas que produz espectros de alta resolução:
$$d\sin\theta = m\lambda$$

Aplicações: espectroscopia, multiplexação por divisão de comprimento de onda (WDM) em fibras ópticas.

#### Polarização

A luz natural é não-polarizada (vibra em todas as direções perpendiculares à propagação). A polarização seleciona uma direção de vibração preferencial:
- **Polarização por absorção** (filtros Polaroid)
- **Polarização por reflexão** (ângulo de Brewster)
- **Polarização por espalhamento** (céu azul)
- **Polarização por birrefringência** (cristais como calcita)

### 6.6 Óptica Quântica

No limite quântico, a luz é composta por fótons. A óptica quântica estuda:
- **Efeito fotoelétrico**: emissão de elétrons por luz incidente ($E = hf$)
- **Efeito Compton**: espalhamento de fótons por elétrons
- **Laser**: emissão estimulada de radiação (Einstein, 1917)
- **Óptica não-linear**: interações luz-matéria que dependem não-linearmente da intensidade

---

## 7. Conexões com Computação, Engenharia e IA

### 7.1 Física na Computação

| Conceito Físico | Aplicação Computacional |
|----------------|------------------------|
| Transistor (física do estado sólido) | Base de todos os processadores modernos |
| Semicondutores e dopagem | Fabricação de chips |
| Eletromagnetismo | Transmissão de dados (cabos, WiFi, fibra óptica) |
| Termodinâmica | Dissipação térmica em processadores |
| Mecânica quântica | Chips de computadores (tunelamento em transistores nanométricos) |
| Eletrônica digital (portas lógicas) | Computação binária |
| Memorias (RAM, ROM, flash) | Armazenamento de dados |
| Discos rígidos (magnetismo) | Armazenamento magnético |
| Fibras ópticas | Comunicações de alta velocidade |

### 7.2 Física na Engenharia

- **Mecânica dos sólidos**: cálculo estrutural de pontes, edifícios, veículos
- **Termodinâmica**: motores, usinas, refrigeração, sistemas HVAC
- **Eletromagnetismo**: geração e distribuição de energia elétrica, telecomunicações
- **Mecânica dos fluidos**: aerodinâmica, hidráulica, tubulações
- **Óptica**: instrumentação, sensores, lasers industriais

### 7.3 Física na IA e Machine Learning

A física inspira e se conecta com a inteligência artificial de diversas maneiras:

#### Física-Inspired AI

| Método IA | Inspiração Física |
|-----------|------------------|
| **Simulated Annealing** | Processo de recozimento em metalurgia (termodinâmica) |
| **Algoritmos genéticos** | Evolução natural (seleção, mutação) |
| **Boltzmann Machines** | Mecânica estatística (distribuição de Boltzmann) |
| **Hopfield Networks** | Sistemas físicos com mínimos de energia |
| **Hamiltonian Neural Networks** | Mecânica hamiltoniana (conservação de energia) |
| **Physics-Informed Neural Networks (PINNs)** | Equações diferenciais da física como regularizadores |
| **Neural ODEs** | Equações diferenciais ordinárias como blocos de rede |
| **Tensor Networks** | Emaranhamento quântico para aprendizado eficiente |

#### IAs para a Física

- **Simulação de sistemas físicos**: previsão de clima, dinâmica de fluidos, astrofísica
- **Descoberta de leis físicas**: AI Feynman, symbolic regression
- **Aceleração de simulações**: surrogate models baseados em redes neurais
- **Processamento de dados experimentais**: LHC (CERN), LIGO, telescópios
- **Otimização de experimentos**: design de materiais, descoberta de drogas

#### Conexão com [[Conhecimento-Geral/Matematica/Calculo-e-Otimizacao]]

A física clássica depende fortemente do cálculo diferencial e integral. Leis de Newton são equações diferenciais de segunda ordem. O princípio da mínima ação (Lagrangiana) é um problema de otimização — mesma base matemática de algoritmos de otimização em machine learning, como gradient descent.

#### Conexão com [[Conhecimento-Geral/Matematica/Algebra-Linear-Essencial]]

O eletromagnetismo utiliza vetores e campos vetoriais. As equações de Maxwell são escritas de forma elegante usando operadores vetoriais (gradiente, divergente, rotacional). Autovalores aparecem em problemas de oscilações acopladas e modos normais.

#### Conexão com [[Conhecimento-Geral/Matematica/Teoria-da-Informacao]]

A conexão entre entropia termodinâmica e entropia da informação (Shannon) é profunda. O "demônio de Maxwell" foi resolvido mostrando que a obtenção de informação tem um custo termodinâmico mínimo — o limite de Landauer: apagar um bit de informação dissipa pelo menos $k_BT\ln 2$ de energia.

#### Conexão com [[Conhecimento-Geral/Neurociencia/Redes-Neurais-Biologicas]]

O neurônio biológico utiliza princípios eletroquímicos (eletromagnetismo, potenciais de membrana) para processar informação. O modelo de Hodgkin-Huxley (1963, Prêmio Nobel) descreve o potencial de ação usando equações diferenciais baseadas em condutâncias iônicas — uma aplicação direta do eletromagnetismo e da física dos meios contínuos à neurociência.

---

## 8. Glossário de Física Clássica

| Termo | Definição | Fórmula |
|-------|-----------|---------|
| Aceleração | Taxa de variação da velocidade | $\vec{a} = d\vec{v}/dt$ |
| Trabalho | Energia transferida por força | $W = \int \vec{F} \cdot d\vec{r}$ |
| Potência | Taxa de realização de trabalho | $P = dW/dt$ |
| Impulso | Variação do momento linear | $\vec{I} = \int \vec{F}\,dt = \Delta\vec{p}$ |
| Campo | Região onde uma força atua à distância | $\vec{E}, \vec{B}, \vec{g}$ |
| Fluxo | Medida de campo através de uma superfície | $\Phi = \int \vec{F} \cdot d\vec{A}$ |
| Gradiente | Taxa de variação espacial de um campo | $\nabla f$ |
| Divergente | Medida de fontes de um campo | $\nabla \cdot \vec{F}$ |
| Rotacional | Medida de circulação de um campo | $\nabla \times \vec{F}$ |
| Laplaciano | Divergente do gradiente | $\nabla^2 f = \nabla \cdot \nabla f$ |

---

## 9. Referências e Leitura Adicional

### Livros-texto clássicos

1. Halliday, Resnick, Walker — *Fundamentos de Física* (vol. 1, 2, 3, 4)
2. Nussenzveig, H. M. — *Curso de Física Básica* (vol. 1, 2, 3, 4)
3. Feynman, R. P. — *Lições de Física de Feynman* (vol. 1, 2, 3)
4. Sears & Zemansky — *Física Universitária*
5. Tipler & Mosca — *Física para Cientistas e Engenheiros*

### Leitura complementar

- *The Feynman Lectures on Physics* — leitura indispensável para intuição física
- *QED: The Strange Theory of Light and Matter* (Feynman) — óptica quântica
- *The Character of Physical Law* (Feynman) — natureza das leis físicas
- Maxwell, J. C. — *A Treatise on Electricity and Magnetism* (1873) — obra original
- Carnot, S. — *Reflections on the Motive Power of Fire* (1824) — origem da termodinâmica

### Conexões com outras notas

- [[Conhecimento-Geral/Fisica/Fisica-Quantica]] — a revolução quântica
- [[Conhecimento-Geral/Matematica/Calculo-e-Otimizacao]] — base matemática da física
- [[Conhecimento-Geral/Matematica/Algebra-Linear-Essencial]] — vetores, campos, autovalores
- [[Conhecimento-Geral/Matematica/Probabilidade-e-Estatistica]] — mecânica estatística
- [[Conhecimento-Geral/Matematica/Teoria-da-Informacao]] — entropia e informação
- [[Conhecimento-Geral/Neurociencia/Redes-Neurais-Biologicas]] — biofísica do neurônio
