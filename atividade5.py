# 1 - 
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return valor_gorjeta

try:
    valor_conta = float(input("Digite o valor total da conta: R$ "))
    porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta desejada (ex: 10 para 10%): "))

    if valor_conta < 0 or porcentagem_gorjeta < 0:
        print("Valores da conta e porcentagem de gorjeta devem ser positivos.")
    else:
        gorjeta_calculada = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
        total_conta = valor_conta + gorjeta_calculada

        print(f"\nValor da conta: R$ {valor_conta:.2f}")
        print(f"Porcentagem da gorjeta: {porcentagem_gorjeta:.2f}%")
        print(f"Valor da gorjeta: R$ {gorjeta_calculada:.2f}")
        print(f"Total a pagar (conta + gorjeta): R$ {total_conta:.2f}")
except ValueError:
    print("Entrada inválida. Por favor, digite números válidos para o valor da conta e a porcentagem.")

# 2 - Verificador de Palíndromo
import re

def verificar_palindromo(texto):
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto).lower() # remove alguns caracteres
    return texto_limpo == texto_limpo[::-1]

texto = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

if verificar_palindromo(texto):
    print(f"'{texto}' é um palíndromo? Sim")
else:
    print(f"'{texto}' é um palíndromo? Não")

# 3 - Calculadora de Descontos

def calcular_desconto(preco_inicial, porcentagem_desconto):
    valor_desconto = preco_inicial * (porcentagem_desconto / 100)
    preco_final = preco_inicial - valor_desconto
    return preco_final

try:
    preco_inicial = float(input("Digite o preço original do produto: R$ "))
    desconto_perc = float(input("Digite a porcentagem de desconto (ex: 15 para 15%): "))

    if preco_inicial < 0 or desconto_perc < 0:
        print("Preço e porcentagem de desconto devem ser valores positivos.")
    else:
        preco_desconto = calcular_desconto(preco_inicial, desconto_perc)
        print(f"\nPreço original: R$ {preco_inicial:.2f}")
        print(f"Desconto aplicado: {desconto_perc:.2f}%")
        print(f"Preço final com desconto: R$ {preco_desconto:.2f}")
except ValueError:
    print("Entrada inválida. Por favor, digite números para preço e porcentagem.")

# 4 - Calculadora de quantidade de dias vividos 
from datetime import date

def calcular_dias_vividos(data_nascimento_str):
    try:
        dia, mes, ano = map(int, data_nascimento_str.split('-')) # converte a string da data de nascimento para um objeto date
        data_nascimento = date(ano, mes, dia)

        data_atual = date.today()

        if data_nascimento > data_atual:
            print("A data de nascimento não pode ser no futuro.")
            return None

        diferenca = data_atual - data_nascimento
        return diferenca.days
    except ValueError:
        print("Formato de data inválido. Use DD-MM-AAAA.")
        return None

data_nascimento = input("Digite sua data de nascimento (DD-MM-AAAA): ")
dias_vivos = calcular_dias_vividos(data_nascimento)

if dias_vivos is not None:
    print(f"Você está vivo há aproximadamente {dias_vivos} dias.")