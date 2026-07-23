# Contrato de dívidas

A service de dívidas passou a rejeitar `startDate` inválida antes de persistir. Isso impede datas quebradas no banco e mantém o contrato de criação/edição mais confiável.