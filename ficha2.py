# -*- coding: utf-8 -*-
"""ficha2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1urCPPCdFFGTQ0SJI113MmRFG5hDHA59o

LISTA DE EXERCÍCIOS DE ALGORITMOS ESTRUTURAS DE REPETIÇÃO

1) Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de
três e que se encontram no conjunto dos números de 1 até 500.
"""

soma = 0

for num in range(1, 501):
    if num % 3 == 0:
        soma += num
        print(num)

"""2) Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e
mostrar :

a. A menor altura do grupo;

b. A maior altura do grupo;
"""

menor_altura = float('inf')
maior_altura = float('-inf')

for altura in range(15):
    altura = float(input("Digite a altura: "))
    if altura < menor_altura:
        menor_altura = altura
    if altura > maior_altura:
        maior_altura = altura

print("Menor altura:", menor_altura)
print("Maior altura:", maior_altura)

"""3) Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a
média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
negativos e o percentual de valores negativos e positivos.
"""

soma_positivos = 0
soma_negativos = 0
num_positivos = 0
num_negativos = 0
total_valores = 0

while True:
    num = float(input("Digite um número (ou 0 para parar): "))
    if num == 0:
        break
    if num > 0:
        soma_positivos += num
        num_positivos += 1
    elif num < 0:
        soma_negativos += num
        num_negativos += 1
    total_valores += 1

if total_valores > 0:
    media = (soma_positivos + soma_negativos) / total_valores

    percentual_positivos = (num_positivos / total_valores) * 100
    percentual_negativos = (num_negativos / total_valores) * 100

    print(f"Média: {media}")
    print(f"Quantidade de valores positivos: {num_positivos}")
    print(f"Quantidade de valores negativos: {num_negativos}")
    print(f"Percentual de valores positivos: {percentual_positivos:.2f}%")
    print(f"Percentual de valores negativos: {percentual_negativos:.2f}%")
else:
    print("Nenhum valor foi inserido.")

"""4) Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles
estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve
terminar quando for lido um número negativo.

"""

num_0_25 = 0
num_26_50 = 0
num_51_75 = 0
num_76_100 = 0

while True:
    num = float(input("Digite um número (ou um número negativo para parar): "))
    if num < 0:
        break
    if 0 <= num <= 25:
      num_0_25 += 1
    elif 26 <= num <= 50:
      num_26_50 += 1
    elif 51 <= num <= 75:
      num_51_75 += 1
    elif 76 <= num <= 100:
      num_76_100 += 1

    print(f"Números no intervalo [0-25]: {num_0_25}")
    print(f"Números no intervalo [26-50]: {num_26_50}")
    print(f"Números no intervalo [51-75]: {num_51_75}")
    print(f"Números no intervalo [76-100]: {num_76_100}")

"""5) Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos.
Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos
números lidos. O número que encerrará a leitura será zero.
"""

num_pares_pares = 0
num_pares_impares = 0
soma_pares = 0
soma_total = 0
total_numeros = 0

while True:
    num = float(input("Digite um número positivo (ou 0 para parar): "))
    if num == 0:
        break  # Sai do loop se o número for 0
    if num > 0:
        soma_total += num
        total_numeros += 1
        if num % 2 == 0:
            num_pares_pares += 1
            soma_pares += num
        else:
            num_pares_impares += 1

if total_numeros > 0:
    media_pares = soma_pares / num_pares_pares if num_pares_pares > 0 else 0
    media_geral = soma_total / total_numeros
else:
    media_pares = 0
    media_geral = 0

print(f"Quantidade de números pares: {num_pares_pares}")
print(f"Quantidade de números ímpares: {num_pares_impares}")
print(f"Média dos valores pares: {media_pares:.2f}")
print(f"Média geral dos números lidos: {media_geral:.2f}")

"""6) Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200."""

for num in range(100, 201):
        print(num)

"""7) Escrever um algoritmo que leia um valor para uma variável N de 1 a 10 e calcule a tabuada de  
N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N, 2 x N = 2N, ..., 10 x N = 10N.
"""

N = int(input("Digite um valor para N (de 1 a 10): "))

if 1 <= N <= 10:
    for i in range(11):
        resultado = i * N
        print(f"{i} x {N} = {resultado}")
else:
    print("Valor de N fora do intervalo permitido.")

"""8) Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em
P.A. contendo 10 valores.  
"""

a = float(input("Digite o valor inicial A: "))
r = float(input("Digite a razão R: "))

for n in range(10):
    termo = a + n * r
    print(f"Termo {n + 1}: {termo}")

"""9) Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em
P.G. contendo 10 valores.
"""

a = float(input("Digite o valor inicial A: "))
r = float(input("Digite a razão R: "))

for n in range(10):
    termo = a * (r ** n)
    print(f"Termo {n + 1}: {termo}")

"""10) Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de
A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
"""

a = int(input("Digite um valor para A: "))

resultado = 1
sequencia = ""

for i in range(a, 0, -1):
    resultado *= i
    if i == a:
        sequencia += f"{i}"
    else:
        sequencia += f" * {i}"

print(f"{a}! = {sequencia} = {resultado}")