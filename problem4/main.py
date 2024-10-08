faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53,
}

def calcular_percentual_faturamento(faturamento_estados):
    faturamento_total = sum(faturamento_estados.values())
    percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estados.items()}
    return percentuais

percentuais = calcular_percentual_faturamento(faturamento_estados)
print("Percentual de faturamento por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")