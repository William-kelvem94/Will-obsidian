---
title: "Política de Privacidade e Indexação"
date: 2026-07-07
updated: 2026-07-07
type: policy
status: active
tags: [sistema, privacidade, rag, indexacao, governanca]
summary: "Regras para decidir o que pode ser indexado, resumido ou mantido fora de fluxos de IA/RAG no WILL-OBSIDIAN."
---

# Política de Privacidade e Indexação

Esta política define como tratar conteúdo do WILL-OBSIDIAN antes de expandir JARVIS, RAG, agentes ou automações.

## Princípios

1. **Minimização:** indexar somente o necessário.
2. **Separação:** distinguir fonte bruta, síntese, regra e memória operacional.
3. **Reversibilidade:** preferir resumo e referência em vez de duplicação integral.
4. **Rastreabilidade:** registrar de onde veio uma informação usada por agentes.
5. **Segurança por padrão:** em dúvida, não indexar diretamente.

## Classificação de conteúdo

| Classe | Exemplos | Pode indexar? | Regra |
|---|---|---:|---|
| Público técnico | README, skills, arquitetura, runbooks | Sim | Indexação liberada |
| Projeto privado | roadmap, status, stack, decisões | Sim, com cuidado | Usar sínteses operacionais |
| Operação do vault | auditorias, migração, dashboards | Sim | Pode alimentar agentes |
| Dados brutos | clippings, fontes, bases importadas | Parcial | Preferir síntese curada |
| Pessoal sensível | saúde, finanças, relacionamento, identidade | Não por padrão | Usar resumo mínimo quando necessário |
| Material restrito | credenciais, dados íntimos, identificadores privados | Nunca | Manter fora de índices e automações |
| Logs locais | erros, traces, dumps | Parcial | Sanitizar antes de uso |

## Regras para 02-JARVIS/RAG

- `02-JARVIS/` pode armazenar memória operacional.
- `04-Conhecimentos/` deve conter síntese estável.
- `05-Skills/` pode ser indexado como capacidade técnica.
- `06-Will-Pessoal/` deve ser tratado como área restrita.
- `11-Dados-Brutos/` deve servir como fonte, não como destino final.
- `.logs/` deve ser revisado antes de entrar em qualquer índice.

## Política para área pessoal

Conteúdos de `06-Will-Pessoal/` só devem ser usados por IA quando forem:

- necessários para personalização real;
- resumidos de forma mínima;
- livres de detalhes íntimos desnecessários;
- marcados como contexto pessoal;
- revisáveis pelo usuário.

Frontmatter recomendado:

```yaml
classe_privacidade: pessoal-resumido
indexavel: false
uso_ia: restrito
```

## Política para projetos

Notas em `03-Projetos/` podem ser indexadas quando contiverem:

- objetivo;
- status;
- stack;
- decisões;
- riscos;
- próximos passos;
- comandos de execução sem material restrito.

## Frontmatter recomendado

```yaml
---
title: "Nome da Nota"
status: active
classe_privacidade: publico-tecnico | projeto-privado | pessoal-sensivel | restrito | bruto
indexavel: true | false
uso_ia: livre | resumido | restrito | proibido
fonte_canonica: true | false
updated: 2026-07-07
---
```

## Checklist antes de indexar

- [ ] A nota tem classe de privacidade?
- [ ] Existe dado pessoal desnecessário?
- [ ] Existe material restrito?
- [ ] A nota é fonte bruta ou síntese curada?
- [ ] O conteúdo pode ser resumido em vez de copiado?
- [ ] O caminho é canônico?
- [ ] O uso por IA está explícito?

## Decisão padrão

Quando houver dúvida:

> **Não indexar diretamente. Criar síntese curta e revisar depois.**
