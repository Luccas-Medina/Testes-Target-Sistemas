faturamento_diario = [
    1000, 1500, 0, 0, 2500, 3000, 4000, 0, 0, 500, 700,
    2000, 0, 0, 4500, 5500, 1000, 2000, 0, 0, 7000, 8000,
    1500, 0, 0, 9000, 11000, 6000, 0, 0
]

# Excluindo finais de semana
faturamento_real = [f for f in faturamento_diario if f > 0]

menor_faturamento = min(faturamento_real)
maior_faturamento = max(faturamento_real)

media_mensal = sum(faturamento_real) / len(faturamento_real)

dias_acima_da_media = sum(1 for f in faturamento_real if f > media_mensal)

print(f"Menor faturamento em um dia do mês: {menor_faturamento}")
print(f"Maior faturamento em um dia do mês: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
