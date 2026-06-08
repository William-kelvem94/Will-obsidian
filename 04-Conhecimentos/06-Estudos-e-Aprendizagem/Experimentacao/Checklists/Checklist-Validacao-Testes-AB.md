---
title: "Checklist - Validação e Pipeline de Testes AB em Produção"
tags: [experimentacao, testes, checklist, abtest, producao]
updated: 2026-06-05
status: concluded
---
# CHECKLIST DE EXECUÇÃO E PIPELINE DE TESTES AB

## 📋 1. Fase de Planejamento e Desenho Estatístico
- [ ] **Definição da Métrica Estrita**: Métrica de Conversão Alvo (Sinal) definida com precisão e métrica de salvaguarda (Ex: tempo de resposta da página para segurança).
- [ ] **Definição das Hipóteses**:
  - Hipótese Nula ($H_0$): As duas variações se comportam de forma idêntica.
  - Hipótese Alternativa ($H_1$): O tratamento aumenta a conversão em pelo menos $X\%$.
- [ ] **Determinação do Tamanho Amostral (Sample Size)**: Calculado o tamanho mínimo da amostra para cada grupo usando o MDE (Minimum Detectable Effect) desejado e o poder estatístico ($\alpha=0.05, 1-\beta=0.80$).

## 🛠️ 2. Fase de Validação Técnica e Pré-Deploy
- [ ] **Homogeneidade dos Grupos (A/A Testing)**: Executados testes do tipo A/A para verificar a integridade do balanceamento probabilístico de usuários sem aplicação de tratamentos. No ruído puramente estatístico, o teste deve passar sem desvios sistemáticos.
- [ ] **Configuração das Feature Flags**: Verificadas as regras de direcionamento (hashes estáveis de usuário baseados em ID ou cookie) no painel de Feature Toggle.

## 🚀 3. Monitoramento em Produção e Saneamento
- [ ] **Prevenção de Amostragem Enviesada (Sample Ratio Mismatch - SRM)**: Realizada auditoria diária do número de usuários em ambos os grupos. Um desvio significativo de proporção (ex: $49.2\%$ vs $50.8\%$ esperado) indica que a infraestrutura está corrompendo a divisão de tráfego.
- [ ] **Não Peeking**: Garantir que as equipes técnicas e PMs não tomem decisões precipitadas de interrupção ou migração de tráfego antes de atingir o tamanho amostral de limite calculado.
