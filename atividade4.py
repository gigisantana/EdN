# 1 - Calculadora Simples
num1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador (+ | - | * | /): ")
num2 = float(input("Digite o segundo número: "))

resultado = 0

if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: não é possível dividir nenhum número por 0!")
        resultado = "Indefinido"
else:
    print("Operador inválido.")
    resultado = "Erro"

if resultado != "Erro" and resultado != "Indefinido":
    print(f"O resultado é: {resultado}")

# 2 - Registro de notas e médias de uma turma
notas = []
while True:
    entrada = input("Digite a nota do aluno (ou 'fim' para terminar): ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Por favor, digite uma nota entre 0 e 10!!")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")

if notas:
    soma_notas = sum(notas)
    media_turma = soma_notas / len(notas)
    print("\n--- Notas Registradas ---")
    for i, nota in enumerate(notas):
        print(f"Aluno {i+1}: {nota:.2f}")
    print(f"\nMédia da turma: {media_turma:.2f}")
else:
    print("Nenhuma nota foi registrada.")

# 3 - Verificador de Senha Segura
senha = input("Crie sua senha: ")

tem_8_caracteres = len(senha) >= 8
contem_numero = False

for caractere in senha:
    if caractere.isdigit():
        contem_numero = True
        break

if tem_8_caracteres and contem_numero:
    print("Senha forte! Sua senha atende aos critérios de segurança.")
else:
    print("Senha fraca! Sua senha NÃO atende aos critérios de segurança porque:")
    if not tem_8_caracteres:
        print("- Deve ter pelo menos 8 caracteres.")
    if not contem_numero:
        print("- Deve conter pelo menos um número.")

# 4 - Contador de Números Ímpares e Pares
numeros_pares = 0
numeros_impares = 0

print("Digite vários números inteiros, e quando terminar, digite 'fim'")

while True:
    entrada = input("Digite um número: ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é um número PAR.")
            numeros_pares += 1
        else:
            print(f"{numero} é um número ÍMPAR.")
            numeros_impares += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'!")

print("\n--- Resumo ---")
print(f"Total de números pares inseridos: {numeros_pares}")
print(f"Total de números ímpares inseridos: {numeros_impares}")