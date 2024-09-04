import json
import xml.etree.ElementTree as ET


with open('dados.json', 'r') as json_file:
    dados_json = json.load(json_file)


tree = ET.parse('dados2.xml')
root = tree.getroot()
dados_xml = []
for row in root.findall('row'):
    dia = int(row.find('dia').text)
    valor = float(row.find('valor').text)
    dados_xml.append({"dia": dia, "valor": valor})
    
def analisar_faturamento(dados):
    dias_validos = [dado["valor"] for dado in dados if dado["valor"] > 0]
    menor_faturamento = min(dias_validos)
    maior_faturamento = max(dias_validos)
    media_mensal = sum(dias_validos) / len(dias_validos)
    dias_acima_media = sum(1 for valor in dias_validos if valor > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_media

menor_json, maior_json, dias_acima_media_json = analisar_faturamento(dados_json)

menor_xml, maior_xml, dias_acima_media_xml = analisar_faturamento(dados_xml)


# Exibindo os resultados
print("Análise dos dados JSON:")
print(f"Menor Faturamento: {menor_json:.2f}")
print(f"Maior Faturamento: {maior_json:.2f}")
print(f"Dias com faturamento acima de média: {dias_acima_media_json}\n")

print("Análise dos dados XML:")
print(f"Menor Faturamento: {menor_xml:.2f}")
print(f"Maior Faturamento: {maior_xml:.2f}")
print(f"Dias com faturamento acima de média: {dias_acima_media_xml}\n")