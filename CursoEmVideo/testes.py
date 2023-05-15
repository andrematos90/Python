'''
Desenvolva um programa que leia quatro valores inseridos  pelo usuário
e guarde-os em uma tupla. No final, mostre:

A - Quantas vezes apareceu o valor 9
B - Em que posição foi digitado o primeiro valor 3.
C - Quais foram os números pares.'''
n1 = int(input('Número: '))
n2 = int(input('Número: '))
n3 = int(input('Número: '))
n4 = int(input('Número: '))
numeros = (n1, n2, n3, n4)
print(f'quantidade de numero 9: {numeros.count(9)}')
primeiro_3 = 0
if n1 == 3 or n2 == 3 or n3 == 3 or n4 == 3 and primeiro_3 == 0:
    primeiro_3 = numeros.index(3)
    print(f'primeiro 3 : {primeiro_3 + 1}')
pares = ()
if n1 % 2 == 0:
    pares = (pares + (n1,) )
if n2 % 2 == 0:
    pares = (pares + (n2,) )
if n3 % 2 == 0:
    pares = (pares + (n3,) )
if n4 % 2 == 0:
    pares = (pares + (n4,) )
print(f'pares: {pares}')