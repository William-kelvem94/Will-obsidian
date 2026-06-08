---
title: "Seguranca da Informacao"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, seguranca, privacidade, engenharia-software]
related: [[../02-Engenharia-Software/APIs-Backend-Banco]], [[../02-Engenharia-Software/Docker-e-DevOps]], [[../05-Dados/Taxonomia-Metadados-e-Ontologia]]
summary: "Fundamentos de segurança da informação para proteger dados, sistemas, contas e projetos."
---

# Segurança da Informação

Segurança da informação protege confidencialidade, integridade e disponibilidade dos dados e sistemas.

## Tríade CIA

| Pilar | Significado |
|---|---|
| confidencialidade | só pessoas autorizadas acessam |
| integridade | dados não são alterados indevidamente |
| disponibilidade | sistema funciona quando necessário |

## Princípios

- menor privilégio;
- defesa em profundidade;
- autenticação forte;
- validação de entrada;
- logs de eventos relevantes;
- backup e recuperação;
- atualização de dependências;
- separação de ambientes;
- cuidado com dados sensíveis.

## Dados sensíveis

Dados sensíveis incluem senhas, tokens, chaves, documentos, dados financeiros, dados de saúde, localização e informações pessoais.

## Boas práticas para projetos

- não versionar secrets;
- usar variáveis de ambiente;
- validar permissões no backend;
- aplicar HTTPS em produção;
- registrar auditoria de ações críticas;
- limitar exposição de APIs;
- revisar dependências;
- proteger backups;
- usar senhas fortes e 2FA.

## Riscos comuns

| Risco | Exemplo | Mitigação |
|---|---|---|
| vazamento de segredo | token no GitHub | usar `.env` e rotação |
| permissão fraca | usuário acessa dado alheio | checagem no backend |
| injeção | entrada vira comando | validação e parametrização |
| dependência vulnerável | pacote antigo | atualização e auditoria |
| backup exposto | banco público | criptografia e acesso restrito |

## Checklist

- [ ] Existe `.env.example` sem segredo real?
- [ ] Secrets reais estão fora do Git?
- [ ] Rotas críticas verificam permissão?
- [ ] Dados sensíveis são minimizados?
- [ ] Logs evitam expor senha ou token?
- [ ] Backups têm controle de acesso?
- [ ] Dependências são revisadas?

## Relações

- [[../02-Engenharia-Software/APIs-Backend-Banco]]
- [[../02-Engenharia-Software/Docker-e-DevOps]]
- [[../05-Dados/Taxonomia-Metadados-e-Ontologia]]
