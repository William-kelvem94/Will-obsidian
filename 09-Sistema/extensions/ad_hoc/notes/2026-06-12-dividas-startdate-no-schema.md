# Contrato de dívidas

A validação de `startDate` das dívidas foi movida para o schema. Agora uma data inválida falha como erro de validação, não como erro interno, e a service só grava datas já confiáveis.