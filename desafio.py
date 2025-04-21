"""
Exercícios
Aqui estão cinco exercícios que envolvem TypeError, verificação de tipo (type check), o uso de try-except para tratamento de exceções e a utilização da estrutura condicional if. 
Esses exercícios aumentam progressivamente em dificuldade e abordam situações práticas onde você pode aplicar esses conceitos.
"""

# # Exercício 21: Conversor de Temperatura
# # Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# # O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
# # garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

# try:
#     celsius = float(input("Digite a temperatura em Celsius: "))
#     fahrenheit = (celsius * 1.8) + 32
#     print(f"{celsius}°C é igual a {fahrenheit}°F.")
# except ValueError:
#     print("Por favor, digite um número válido para a temperatura.")

# # Exercício 22: Verificador de Palíndromo
# # Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# # Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

# palavra = input("Digite uma palavra: ").lower()
# palavra = ''.join(filter(str.isalnum, palavra))

# if palavra == palavra[::-1]:
#     print(f'A palavra "{palavra}" é um palíndromo.')
# else:
#     print(f'A palavra "{palavra}" não é um palíndromo.')

# # Exercício 23: Calculadora Simples
# # Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# # Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar 
# # a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

# def soma(n1, n2):
#     return n1 + n2

# def subtracao(n1, n2):
#     return n1 - n2

# def multiplicacao(n1, n2):
#     return n1 * n2

# def divisao(n1, n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError:
#         return "Erro: Divisão por zero não é permitida."

# print("Opções de operações matemáticas:\n"
#       "+. Soma\n"
#       "-. Subtração\n"
#       "*. Multiplicação\n"
#       "/. Divisão\n")

# sel = input("Selecione a operação (+, -, *, /): ")
# print(f"Você escolheu a operação: {sel}")

# try:
#     n1 = int(input("Digite o primeiro número: "))
#     n2 = int(input("Digite o segundo número: "))

#     if sel == "+":
#         print(f"O resultado de {n1} + {n2} = {soma(n1, n2)}")
#     elif sel == "-":
#         print(f"O resultado de {n1} - {n2} = {subtracao(n1, n2)}")
#     elif sel == "*":
#         print(f"O resultado de {n1} * {n2} = {multiplicacao(n1, n2)}")
#     elif sel == "/":
#         print(f"O resultado de {n1} / {n2} = {divisao(n1, n2)}")
#     else:
#         print("Operação inválida. Tente novamente.")
# except ValueError:
#     print("Erro: Por favor, insira números válidos.")

# # Exercício 24: Classificador de Números
# # Escreva um programa que solicite ao usuário para digitar um número. 
# # Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número 
# # como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

# try:
#     numero = int(input("Digite um número: "))
#     if numero > 0:
#         tipo = "Positivo"
#     elif numero < 0:
#         tipo = "Negativo"
#     else:
#         tipo = "Zero"

#     paridade = "Par" if numero % 2 == 0 else "Ímpar"

#     print(f"O número {numero} é {tipo} e {paridade}.")
# except ValueError:
#     print("Por favor, digite um número inteiro válido.")

# # Exercício 25: Conversão de Tipo com Validação
# # Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# # O programa deve converter a string de entrada em uma lista de números inteiros. 
# # Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
# # Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

try:
    # Solicita a entrada do usuário e converte diretamente para uma lista de inteiros
    entrada_lista = input("Digite uma lista de números separados por vírgula: ")
    numeros_int = [int(num.strip()) for num in entrada_lista.split(",")]

    # Exibe a lista de inteiros
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")