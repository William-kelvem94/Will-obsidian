---
title: "Índice de Templates — Jarvis (Raiz)"
description: "Templates para o Jarvis capturar informações estruturadas sobre Will — versão raiz do sistema de blueprints."
tags: [jarvis, templates]
date: 2026-04-27
updated: 2026-05-16
---

# Templates — Jarvis (Raiz)

Esta pasta contém os templates principais que o JARVIS utiliza para estruturar informações sobre Will. Cada template define um formato padronizado de _frontmatter_ e seções que alimentam o sistema de memória, RAG e processamento de conhecimento. Estes templates são a versão raiz, com links diretos para as notas no sistema de blueprints em `05-System/Blueprints/`.

## Templates disponíveis

### [[JARVIS/Templates/Template-Memoria-Episodica|Template-Memoria-Episodica]]
Registra uma memória de interação entre Will e o JARVIS — conversas, eventos, momentos significativos. O _frontmatter_ inclui título, data, hora, categoria (trabalho, pessoal, aprendizado, projeto), nível de importância (baixa/média/alta), projeto associado e keywords para indexação semântica. A nota resultante alimenta o sistema de memória de curto prazo e é periodicamente consolidada em memórias semânticas no pipeline RAG. Sem este template, o JARVIS não teria como registrar experiências de forma estruturada e recuperável.

**Uso típico:** Após uma conversa produtiva, o JARVIS pergunta se Will quer salvar como memória episódica, preenche o template automaticamente e armazena no banco vetorial.

### [[JARVIS/Templates/Template-Diario|Template-Diario]]
Registro diário de atividades, descobertas e reflexões. O template define campos para data, número de sessões de trabalho, links para notas criadas/modificadas no dia, uma seção de "descobertas" (aprendizados novos), "progresso" (o que avançou) e "reflexão" (insights pessoais). Funciona como um _log_ temporal navegável, respondendo "o que aconteceu no dia X". Diferente da memória episódica (que foca em um evento), o diário agrega múltiplos eventos em um panorama diário coerente.

**Uso típico:** No final do dia, o JARVIS ajuda Will a revisar o que foi feito, sugere conexões entre atividades e preenche o diário. Também pode ser usado como contexto matinal para "O que estamos fazendo hoje?".

### [[JARVIS/Templates/Template-Perfil-Will|Template-Perfil-Will]]
O questionário fundamental que define a identidade, valores e contexto de Will. Contém perguntas sobre: dados pessoais, valores fundamentais, objetivos (curto e longo prazo), estilo de trabalho, preferências de comunicação, áreas de expertise, projetos ativos, rede de contatos profissionais, histórico profissional e configurações de privacidade para o JARVIS. Este template evolui continuamente — novas perguntas são adicionadas conforme o relacionamento entre Will e JARVIS se aprofunda. É a âncora identitária de todo o sistema.

**Uso típico:** Preenchido durante a fase de _onboarding_ e revisitado periodicamente para atualizações. O JARVIS consulta este perfil para alinhar respostas, recomendações e decisões com os valores de Will.

## Hierarquia de templates

- **Perfil-Will** → Quem é Will (identidade permanente, evolui lentamente)
- **Memória Episódica** → O que aconteceu (eventos atômicos, alta frequência)
- **Diário** → Como foi o dia (agregação diária de memórias episódicas)

Esta hierarquia reflete o modelo de memória humana: identidade estável na base, eventos específicos no meio, e sumários diários no topo.

## Relação com os Blueprints

Esta pasta raiz contém os mesmos templates que [[JARVIS/05-System/Blueprints/INDEX|Blueprints (05-System)]], mas em localização mais acessível para criação rápida de notas. Os blueprints em `05-System/Blueprints/` são as versões canônicas com documentação mais detalhada; esta pasta serve como atalho para o uso diário.

## Conexões

- [[JARVIS/05-System/Blueprints/INDEX|Blueprints — Templates Detalhados]] — Versão canônica com documentação completa.
- [[skills/04-knowledge-systems/obsidian-neural-vault|Obsidian Neural Vault]] — Como o vault estrutura o conhecimento que alimenta o JARVIS.
- [[skills/04-knowledge-systems/memory-management|Gestão de Memória Long-Term]] — Pipeline de processamento das memórias capturadas.
