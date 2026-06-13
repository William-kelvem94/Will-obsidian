# Contrato de investimentos

A API de listagem de investimentos passou a sanitizar `minAmount` e `maxAmount` antes de montar o filtro. Isso evita `NaN` em queries com valores inválidos vindos da URL.