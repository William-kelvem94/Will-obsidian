---
category: Computational Neuroscience
tags: [Neural Coding, SNN, Hodgkin-Huxley]
links: [[05-Psicologia-e-Cognicao]]
---

# Neural Coding and Spiking Networks

## Modelagem Biofísica: O Modelo de Hodgkin-Huxley
O modelo de Hodgkin-Huxley (HH) descreve a iniciação e propagação de *action potentials* através de equações diferenciais que modelam a condutância da membrana para íons $\text{Na}^+$ e $\text{K}^+$. O HH define a dinâmica do *membrane potential* baseando-se em *voltage-gated ion channels*, onde a probabilidade de abertura dos canais depende do potencial elétrico.

$\text{C}_m \frac{dV}{dt} = I_{\text{ext}} - \bar{g}_{\text{Na}} m^3 h (V - E_{\text{Na}}) - \bar{g}_{\text{K}} n^4 (V - E_{\text{K}}) - \bar{g}_{\text{L}} (V - E_{\text{L}})$

Este modelo fornece a base para entender a *excitability* neuronal, mas sua complexidade computacional torna a simulação de redes em larga escala proibitiva.

## Leaky Integrate-and-Fire (LIF) e Simplificações Computacionais
Para viabilizar a simulação de *Spiking Neural Networks (SNNs)*, utiliza-se o modelo *Leaky Integrate-and-Fire*. O LIF simplifica a dinâmica do potencial de membrana como um capacitor com um resistor em paralelo (*leak*). Quando o potencial atinge um *threshold*, um *spike* é gerado e o potencial é resetado instantaneamente.

A principal vantagem do LIF é a redução da dinâmica neuronal a um evento binário (*spike*), permitindo a análise de *Temporal Coding* e *Rate Coding*. No *Rate Coding*, a informação é representada pela frequência de disparos, enquanto no *Temporal Coding*, a precisão do timing dos spikes é a portadora da informação.

## Bases Biológicas de Spiking Neural Networks (SNNs)
As SNNs buscam mimetizar a *sparsity* e a eficiência energética do cérebro. Ao contrário de redes neurais artificiais tradicionais, as SNNs processam informações via *asynchronous events*.

A plasticidade nas SNNs é frequentemente implementada via *Spike-Timing-Dependent Plasticity (STDP)*. A STDP dita que a força da *synaptic connection* aumenta se o neurônio pré-sináptico disparar logo antes do pós-sináptico (*Long-Term Potentiation* - LTP) e diminui se disparar depois (*Long-Term Depression* - LTD). Esse mecanismo é a base biológica para o aprendizado não supervisionado e a *self-organization* de mapas neurais.
