# 1 - Conversor de Moeda
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print(f"Valor em Reais: R$ {valor_reais:.2f}")
print(f"Taxa do Dólar: R$ {taxa_dolar:.2f}")
print(f"Taxa do Euro: R$ {taxa_euro:.2f}")
print(f"Valor em Dólares: US$ {valor_dolar:.2f}")
print(f"Valor em Euros: € {valor_euro:.2f}")

# 2 - Calculadora de Desconto
nome_produto = "Camiseta"
preco_inicial = 50.00
porcentagem_desconto = 20

valor_desconto = preco_inicial * (porcentagem_desconto / 100)
preco_final = preco_inicial - valor_desconto

print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_inicial:.2f}")
print(f"Porcentagem de desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")

# 3 - Calculadora de Média Escolar
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")
print(f"Média: {media:.2f}")

# 4 - Calculadora de Consumo de Combustível
distancia_percorrida = 300  # km
combustivel_gasto = 25      # litros

consumo_medio = distancia_percorrida / combustivel_gasto

print(f"Distância percorrida: {distancia_percorrida} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")