---
title: "Blueprints — Templates do Jarvis"
description: "Templates estruturados para o Jarvis capturar, organizar e consultar informações sobre Will e seu universo."
tags: [jarvis, templates, blueprints, jarvis-sistema]
updated: 2026-06-13
date: 2026-04-27
---

# Blueprints — Templates do Jarvis

Esta pasta contém os _blueprints_ (modelos estruturados) que o agente JARVIS utiliza para capturar e organizar informações de forma consistente. Cada template define um formato padronizado de _frontmatter_ e seções, permitindo que o sistema de memória e RAG processe os dados de maneira previsível e eficiente.

## Templates disponíveis

### [[02-JARVIS/05-System/Blueprints/Template-Memoria-Episodica|Template-Memoria-Episodica]]
Captura uma memória de interação entre Will e o JARVIS — uma conversa, um evento, um momento significativo. O template inclui campos para: título, data, hora, categoria da interação (trabalho, pessoal, aprendizado, projeto), importância (baixa/média/alta), projeto associado, keywords para indexação semântica, e uma seção de notas livres. As memórias episódicas alimentam o sistema de memória de curto prazo do JARVIS e são periodicamente consolidadas em memórias semânticas mais abstratas. Sem este template, o JARVIS não teria como registrar "o que aconteceu hoje" de forma estruturada.

### [[02-JARVIS/05-System/Blueprints/Template-Diario|Template-Diario]]
O registro diário de atividades, reflexões e descobertas. Diferente da memória episódica (que captura eventos específicos), o diário é um sumário do dia: quantas sessões de trabalho ocorreram, quais projetos foram tocados, descobertas importantes, links para notas criadas ou modificadas, e reflexões pessoais. O template define uma estrutura de seções que o JARVIS pode preencher automaticamente ou com assistência do usuário. O diário serve como _index_ temporal para navegação retrospectiva — "o que aconteceu na terça-feira passada?".

### [[02-JARVIS/05-System/Blueprints/Template-Perfil-Will|Template-Perfil-Will]]
O questionário fundamental que define quem é Will — a identidade, valores, preferências, e biografia que o JARVIS precisa conhecer para agir de forma alinhada. Este template não é preenchido uma única vez, mas evolui continuamente: novas perguntas são adicionadas conforme o JARVIS descobre mais sobre Will. O perfil cobre: dados pessoais, valores fundamentais, objetivos de curto e longo prazo, estilo de trabalho, preferências de comunicação, áreas de expertise, projetos ativos e arquivados, rede de contatos, e configurações de privacidade. Este template é a ancora identitária de todo o sistema JARVIS.

## Como os blueprints se conectam

Os três templates formam um sistema complementar:

1. **Memória Episódica** captura eventos atômicos ("Will disse X sobre o projeto Y").
2. **Diário** agrega as memórias episódicas em um sumário diário coerente.
3. **Perfil-Will** fornece o contexto permanente sobre quem é Will, permitindo que o JARVIS interprete e priorize as memórias episódicas e os diários.

Juntos, eles permitem que o sistema RAG do JARVIS (em [[05-Skills/04-knowledge-systems/INDEX|Knowledge Systems]]) recupere não apenas _o que_ aconteceu, mas _quem_ é a pessoa envolvida e _qual o significado_ daquela memória no contexto maior.

## Notas sobre templates ausentes

Os seguintes templates estão planejados mas ainda não foram criados:

- **Template-Decisão** — Para registrar decisões importantes com fundamentação, alternativas consideradas e resultado esperado.
- **Template-Aprendizado** — Para capturar novos aprendizados de forma estruturada (conceito, fonte, nível de compreensão, conexões com conhecimento existente).
- **Template-Projeto** — Para documentar projetos com escopo, milestones, recursos e lições aprendidas.

## Conexões

- [[02-JARVIS/Templates/INDEX|Templates (pasta raiz)]] — Versão simplificada dos templates na raiz do JARVIS.
- [[05-Skills/04-knowledge-systems/memory-management|Gestão de Memória]] — Como as memórias capturadas por estes templates são processadas e armazenadas.
- [[05-Skills/04-knowledge-systems/advanced-rag-strategies|Estratégias RAG]] — Como os templates estruturados melhoram a qualidade da recuperação.
