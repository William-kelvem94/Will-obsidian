# Contrato de dashboard

O endpoint `GET /api/dashboard/expenses-by-category` passou a usar limite superior exclusivo no mês. Isso evita perder despesas registradas no último instante do período.