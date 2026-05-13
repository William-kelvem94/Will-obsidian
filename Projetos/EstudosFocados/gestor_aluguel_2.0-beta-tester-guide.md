# Guia de Beta Tester - Gestor de Aluguel 2.0

Versao espelhada para a area de estudos, com foco em execucao manual e validacao do usuario final.

## Arquivos de apoio
- [[../Privados/gestor_aluguel_2.0-beta-tester-guide|Guia completo]]
- [[../Privados/gestor_aluguel_2.0-beta-tester-manual.txt|Versao texto]]

## Ordem de execucao
1. Login do painel principal
2. Cadastro de propriedade
3. Cadastro de inquilino
4. Criacao de contrato
5. Visualizacao de pagamento
6. Portal do inquilino
7. Convite e aceite
8. Webhook e logout

## Casos mais importantes
- contrato em rascunho versus contrato ativo
- pagamento manual versus retorno por webhook
- portal autenticado versus portal sem sessao
- refresh no meio do formulario
- erro de rede durante salvamento

## O que a beta precisa provar
- que o fluxo principal fecha ponta a ponta
- que o portal nao vaza dados entre tenants
- que o financeiro nao quebra com dado legado
- que o erro externo nao derruba a experiencia toda

