---
title: "Glossário Estruturado - Métricas e Modelos de Experimentação"
tags: [experimentacao, testes, glossario, abtest, dicionario]
updated: 2026-06-05
status: concluded
---
# GLOSSÁRIO ACADÊMICO E ESTRUTURADO - EXPERIMENTAÇÃO E TESTES

## 🔬 Conceitos Estatísticos e Fundamentais

### 1. Teste A/B (A/B Testing)
Método de design experimental em que duas versões de um elemento (Versão A, o controle, e Versão B, o tratamento) são comparadas entre grupos homogêneos de usuários. O objetivo é isolar uma única variável e determinar se alterações produzem diferenças estatisticamente significativas em uma métrica alvo especificada.

### 2. Significância Estatística (Statistical Significance - p-valor)
A probabilidade (expressa como $p$) de obter um resultado igual ou mais extremo que o observado, assumindo que a hipótese nula ($H_0$) seja verdadeira. Tradicionalmente na ciência e indústria, usa-se o limiar de $\alpha = 0.05$ (5%), o que significa que há apenas 5% de chance de o efeito observado ser fruto de ruído aleatório.

### 3. Erro Tipo I e Erro Tipo II
* **Erro Tipo I ($\alpha$ - Falso Positivo)**: Rejeitar a hipótese nula quando ela é verdadeira. Na prática, declarar que há uma diferença estatisticamente vencedora no tratamento quando, na verdade, não há nenhum efeito real.
* **Erro Tipo II ($\beta$ - Falso Negativo)**: Falhar em rejeitar a hipótese nula quando ela é falsa. Declarar que não há vantagem estatística quando, na verdade, uma variação significativa de comportamento ocorreu.

### 4. Poder Estatístico (Statistical Power - $1 - \beta$)
A sensibilidade do experimento para detectar um efeito real caso ele exista de fato. Um poder estatístico alvo comum na indústria é $80\%$, significando que se o tratamento de fato alterar o comportamento dos usuários, o teste detectará essa mudança em 8 de cada 10 vezes.

---

## 🧪 Práticas Avançadas de Testes de Software e DataOps

### 1. Teste Multivariavel (MVT)
Diferente dos testes A/B/C convencionais, os testes multivariados testam combinações simultâneas de múltiplas variáveis independentes de forma matricial para compreender o efeito cruzado e as interações entre os componentes.

### 2. Canary Deployment (Implantação Canário)
Prática de implantação de software de infraestrutura onde a nova versão é distribuída de forma segmentada para um percentual ínfimo de tráfego inicial (ex: 1% a 5%). Isso permite colher telemetria de falhas em produção de forma controlada antes do deploy total.

### 3. Feature Flags / Feature Toggles
Mecanismos de desenvolvimento de software que permitem ligar e desligar rotas de código, integrações e layouts em tempo real para grupos segmentados direto no servidor de produção, sem a necessidade estrita de realizar deploys ou rollbacks de pipelines CI/CD.
