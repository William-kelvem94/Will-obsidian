# Segurança, Privacidade & RAG Compliance

## Diretrizes Gerais
- Todo arquivo sensível deve conter `sensivel: true` no frontmatter.
- Arquivos sensíveis NUNCA devem ser enviados para indexação RAG público!
- Use scripts `audit_sensitives.py` (pré-push/CI) para bloquear, mover, ou alertar.

## Checklist LGPD/GDPR para Vaults
- [ ] Consentimento: arquivos de uso pessoal devem estar identificados (tag, path, frontmatter)
- [ ] Minimização: apenas metadados estritamente necessários
- [ ] Indexação restrita para sensíveis
- [ ] Log de acesso: registrar acessos em queries a dados sensíveis
- [ ] Relatar/excluir conteúdo sob demanda

## Estratégias de segurança
- Uso de GITLEAKS, pre-commit hooks e CI
- Auditoria periódica (report automático)
- Documentação transparente via meta-notas
