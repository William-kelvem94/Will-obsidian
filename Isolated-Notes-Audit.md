# Auditoria de Notas e Links do Vault

Esta nota resume o estado atual do vault e os ajustes feitos para reduzir a bagunça de arquivos soltos.

## O que foi verificado

- Identificação de arquivos Markdown isolados no gráfico do Obsidian.
- Atenção especial aos hubs principais: `Bem-vindo.md`, `Projetos/README.md`, `skills/README.md` e `JARVIS/README.md`.
- Busca por índices que referenciam arquivos apenas como texto, sem link ativo.

## Ajustes aplicados

- Atualizado `Bem-vindo.md` para incluir:
  - `[[skills/README|Skills Hub]]`
  - `[[JARVIS/README|JARVIS Hub]]`
- Atualizado `Projetos/README.md` para criar links ativos para:
  - `Projetos/Plano-de-Acao`
  - `Projetos/Organizacao-Completa`
  - `Projetos/GitHub-Completo`
  - `Projetos/Privados/README`
  - `Projetos/EstudosFocados/README`
  - `Projetos/EstudosPesquisas/README`
  - `Projetos/Objetivos/README`
  - `Projetos/Privados/PROJECT_JARVIS_5.0`
  - `Projetos/Privados/IA-LOCAL`
  - `Projetos/EstudosFocados/IA-LOCAL`
  - `Projetos/EstudosPesquisas/AI-Local-Gratuita`

## O que pode ser ajustado em seguida

- Converter listas de arquivos em `skills/vscode-ai/README.md` e `skills/fullstack/README.md` para links ativos se quiser que eles apareçam mais claramente no grafo.
- Criar um índice de `Will-Pessoal/Perfil` com links diretos para todas as notas do perfil. (Iniciado via `JARVIS/Sobre-Will/Perfil.md`)
- Adicionar um índice de `JARVIS/Memorias` se quiser que as memórias de diário e episódicas apareçam como parte da navegação.
- **[Concluído 2026-04-14]** Reorganização da KnowledgeBase e criação do módulo `Sobre-Will/` para personalização profunda.
- **[Concluído 2026-04-14]** Adição da nota técnica `Sistemas-Sensoriais.md` e limpeza de links legados no `Mapa.md`.

## Notas sobre arquivos que não precisam ser deletados

Alguns arquivos podem parecer "soltos" no grafo, mas são normais:

- `JARVIS/Memorias/Diario/*.md` e `JARVIS/Memorias/Episodicas/*.md` são entradas de memória temporal. (Garantida persistência no Git via `.gitignore`)
- `JARVIS/Sobre-Will/*.md` contém o contexto de personalização do usuário.
- `skills/vscode-ai/*.md` e `skills/fullstack/*.md` são conteúdos de skill que já têm um hub central (`skills/README.md`).
- Arquivos de perfil pessoal como `Will-Pessoal/Perfil/Bio.md` e `Will-Pessoal/Vida/Habitos.md` são notas de referência e não precisam de links internos em todos os lugares.

## Recomendações

1. Use `Bem-vindo.md` como ponto de entrada principal.
2. Mantenha `skills/README.md` e `JARVIS/README.md` atualizados como hubs.
3. Se quiser, converta referências textuais em wiki links nos índices principais.
4. Não delete notas de diário ou memórias episódicas apenas porque aparecem isoladas.

---

> Resultado: o foco de limpeza foi nos hubs e índices, não na remoção de conteúdo.
