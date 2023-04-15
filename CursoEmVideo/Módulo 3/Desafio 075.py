'''
Desenvolva um programa que leia quatro valores inseridos  pelo usuário
e guarde-os em uma tupla. No final, mostre:

A - Quantas vezes apareceu o valor 9
B - Em que posição foi digitado o primeiro valor 3.
C - Quais foram os números pares.'''

numeros = ()

num9 = 0
primeiro_3 = 0
numerospares = ()

for c in range(4):
    num_digitado = int(input('Digite um número: '))
    numeros += (num_digitado,)

    if num_digitado == 9:
         num9 = num9 + 1
    if num_digitado == 3 and primeiro_3 == 0:
         primeiro_3 = numeros.index(3)
    if num_digitado % 2 == 0:
          numerospares += (num_digitado,)
         

print(f'O numero 9 apareceu: {num9} vezes')
print(f'Três digitado na posição: {primeiro_3 + 1}')
print(f'Numeros pares: {numerospares}')
