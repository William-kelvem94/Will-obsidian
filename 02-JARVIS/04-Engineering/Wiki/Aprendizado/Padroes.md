---
title: "Padrões Recorrentes"
date: 2026-05-16
tags: [jarvis, aprendizado, padroes, arquitetura, jarvis-engenharia]
updated: 2026-06-13
---

# Padrões Recorrentes

> Catálogo de padrões que se repetem nos projetos de Will. Reconhecer o padrão é o primeiro passo para resolver o problema de forma consistente.

## 🏷️ Categorias

- **Arquitetura** — Padrões estruturais e de design de sistemas
- **Código** — Padrões de implementação, refatoração, boas práticas
- **UI/UX** — Padrões de interface e experiência do usuário
- **Processo** — Padrões de fluxo de trabalho e metodologia

---

## 📐 Arquitetura

### Padrão: Separação por Contexto

- **Contexto:** Projetos que começam pequenos e crescem organicamente
- **Problema:** Misturar arquivos de diferentes domínios em um único diretório dificulta navegação e manutenção
- **Solução:** Organizar diretórios por domínio de negócio, não por tipo de arquivo
- **Exemplo:** No vault Obsidian, separar Aprendizado/ de Memorias/ de System/ em vez de ter pastas /Notas, /Docs

### Padrão: Configuração Externalizada

- **Contexto:** Aplicações que precisam rodar em múltiplos ambientes
- **Problema:** Paths e segredos hard-coded quebram ao mudar de ambiente
- **Solução:** Usar arquivos .env e variáveis de ambiente para tudo que é específico do ambiente
- **Exemplo:** JARVIS usa JARVIS_KB_PATH e JARVIS_VAULT_ROOT no .env

---

## 💻 Código

### Padrão: API Primeiro

- **Contexto:** Projetos full-stack com backend e frontend separados
- **Problema:** Interface acoplada a implementação, mudanças no backend quebram o frontend
- **Solução:** Definir contratos de API antes de implementar, usar schemas (Pydantic/Zod)
- **Exemplo:** FastAPI + Pydantic models compartilhados com frontend via OpenAPI spec

### Padrão: Testes como Documentação

- **Contexto:** Projetos com múltiplos desenvolvedores ou que precisam ser mantidos por muito tempo
- **Problema:** Documentação desatualizada, comportamento não especificado
- **Solução:** Escrever testes que descrevem o comportamento esperado — testes passam ou quebram, docs mentem
- **Exemplo:** Testes de unidade com pytest descrevendo cenários de borda

---

## 🎨 UI/UX

### Padrão: Feedback Imediato

- **Contexto:** Ações do usuário que exigem confirmação visual
- **Problema:** Usuário não sabe se a ação foi registrada, causando cliques duplicados
- **Solução:** Sempre mostrar feedback visual imediato (loading, toast, animação)
- **Exemplo:** Botão de salvar desabilitado com spinner enquanto requisição está em andamento

---

## 🔄 Processo

### Padrão: Documentação Assíncrona

- **Contexto:** Sessões de trabalho com ferramentas de IA
- **Problema:** Perder contexto entre sessões ou ao trocar de agente/tool
- **Solução:** Documentar decisões, aprendizados e contexto imediatamente durante a sessão
- **Exemplo:** Jarvis registra memórias episódicas e fatos no vault em tempo real

---

## 📎 Referências

- [[INDEX|Índice de Aprendizado]]
- [[Erros-e-Licoes|Erros e Lições Aprendidas]]

---
*Última atualização: 2026-05-16*

[[02-JARVIS/Aprendizado/INDEX|← Voltar ao índice de Aprendizado]]
