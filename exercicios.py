# Exercícios

# Inteiros (int)
# 01 - Escreva um programa que soma dois números inteiros inseridos pelo usuário.

ex1_num1 = int(input("Digite o primeiro número inteiro: "))
ex1_num2 = int(input("Digite o segundo número inteiro: "))
resultado_soma = ex1_num1 + ex1_num2

print("A soma é:", resultado_soma)

## 02 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

ex2_div_1 = int(input("Digite um número: "))
ex2_dividendo = 5

resultado_da_divisao = ex2_div_1 // ex2_dividendo

print(resultado_da_divisao)

## 03 - Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

ex3_num1 = int(input("Digite o primeiro número inteiro: "))
ex3_num2 = int(input("Digite o segundo número inteiro: "))
resultado_multiplicacao = ex3_num1 * ex3_num2

print("O resultado é:", resultado_multiplicacao)

## 04 - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

ex4_num1 = int(input("Digite o primeiro número: "))
ex4_num2 = int(input("Digite o segundo número: "))

divisao = ex4_num1 // ex4_num2

print(divisao)

## 05 -Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

ex5_base = int(input("digite um número: "))
ex5_expoente = 2

potenciacao = ex5_base ** ex5_expoente

print(potenciacao)

##Números de Ponto Flutuante (float)
## 06 - Escreva um programa que receba dois números flutuantes e realize sua adição.

flo_1 = float(input("Digite o primeiro numero: "))
flo_2 = float(input("Digite o primeiro numero: "))

soma = flo_1 + flo_2

print(soma)

## 07 - Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

med_1 = float(input("Digite o primeiro número: "))
med_2 = float(input("Digite o segundo número: "))

calculo_media = (med_1 + med_2)/2

print(calculo_media)

## 08 - Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

pot_1 = float(input("Digite o número da base: "))
exp_2 = float(input("Digite o número do expoente: "))

calculo_potencia = (pot_1**exp_2)

print(calculo_potencia)

## 09 - Faça um programa que converta a temperatura de Celsius para Fahrenheit.

celsus = float(input("Digite o valor do Celsus: "))
calculo_far = (celsus * 9/5) + 32

print(f"{celsus}Cº é igual a {calculo_far}Fº")

## 10 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio = float(input("digite o valor do raio: "))
area = 3.14159 * raio ** 2

print (f"o valor da area do circulo é {round(area)}")

# #Strings (str)
# 11 - Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

str_1 = str(input("Digite uma frase aqui: "))
print_str_1 = str_1.upper()

print(print_str_1)

# 12 - Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

str_2 = str(input("Digite o texto aqui: "))
print_str_2 = str_2.lower()

print(print_str_2)

# 13 - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

str_3 = str(input("Digite o texto aqui: "))
print_str_3 = str_3.strip()

print(print_str_3)

# 14 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

str_4 = str(input("Digite uma data: "))

dia, mes, ano = str_4.split("/")
print(dia)
print(mes)
print(ano)

# 15 - Escreva um programa que concatene duas strings fornecidas pelo usuário.

parte1 = input("Digite a primeira parte do texto: ")
parte2 = input("Digite a segunda parte do texto: ")

texto_concatenado = parte1 + parte2
print("Texto concatenado:", texto_concatenado)

# #Booleanos (bool)
# 16 - Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

# 17 - Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

valor1 = True
valor2 = False

resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

# 18 - Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

valor1 = True
valor2 = False

resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

# 19 - Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

num1 = 5
num2 = 5

resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)

# 20 -Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

num1 = 4
num2 = 5

resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)