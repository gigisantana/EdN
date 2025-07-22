# 1 - Classificador de Idade
idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    classificacao = "Criança"
elif 13 <= idade <= 17:
    classificacao = "Adolescente"
elif 18 <= idade <= 59:
    classificacao = "Adulto"
elif idade >= 60:
    classificacao = "Idoso"
else:
    classificacao = "Idade inválida!! Por favor, digite um número positivo."

print(f"Você se encaixa na categoria: {classificacao}")

# 2 - Calculadora de IMC
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

if altura <= 0 or peso <= 0:
    print("Os valores de peso e altura devem ser positivos!")
else:
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    elif imc < 35:
        classificacao = "Obesidade Grau I"
    elif imc < 40:
        classificacao = "Obesidade Grau II (Severa)"
    else:
        classificacao = "Obesidade Grau III (Mórbida)"

    print(f"\nSeu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")

# 3 - Conversor de Temperatura
temperatura = float(input("Digite o valor da temperatura: "))
unidade_origem = input("Qual a unidade de origem? (C = Celsius | F = Fahrenheit | K = Kelvin): ").upper()
unidade_final = input("Para qual unidade deseja converter? (C = Celsius | F = Fahrenheit | K = Kelvin): ").upper()

resultado = 0

if unidade_origem == 'C':
    if unidade_final == 'F':
        resultado = (temperatura * 9/5) + 32
        print(f"{temperatura:.2f}°C é equivalente a {resultado:.2f}°F")
    elif unidade_final == 'K':
        resultado = temperatura + 273.15
        print(f"{temperatura:.2f}°C é equivalente a {resultado:.2f}K")
    elif unidade_final == 'C':
        print(f"A temperatura já está em Celsius: {temperatura:.2f}°C")
    else:
        print("Unidade final inválida.")
elif unidade_origem == 'F':
    if unidade_final == 'C':
        resultado = (temperatura - 32) * 5/9
        print(f"{temperatura:.2f}°F é equivalente a {resultado:.2f}°C")
    elif unidade_final == 'K':
        resultado = (temperatura - 32) * 5/9 + 273.15
        print(f"{temperatura:.2f}°F é equivalente a {resultado:.2f}K")
    elif unidade_final == 'F':
        print(f"A temperatura já está em Fahrenheit: {temperatura:.2f}°F")
    else:
        print("Unidade final inválida.")
elif unidade_origem == 'K':
    if unidade_final == 'C':
        resultado = temperatura - 273.15
        print(f"{temperatura:.2f}K é equivalente a {resultado:.2f}°C")
    elif unidade_final == 'F':
        resultado = (temperatura - 273.15) * 9/5 + 32
        print(f"{temperatura:.2f}K é equivalente a {resultado:.2f}°F")
    elif unidade_final == 'K':
        print(f"A temperatura já está em Kelvin: {temperatura:.2f}K")
    else:
        print("Unidade final inválida.")
else:
    print("Unidade de origem inválida.")

# 4 - Verificador de Ano Bissexto
ano = int(input("Digite um ano: "))


if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} É um ano bissexto!!")
else:
    print(f"{ano} NÃO é um ano bissexto.")