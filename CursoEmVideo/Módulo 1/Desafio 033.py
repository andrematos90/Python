'''Faça um programa que leia três numeros  e mostre qual é o maior e qual é o menor'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

maior = n1

if n2 > n1:
    maior = n2

if n3 > maior:
    maior = n3

menor = n1

if n2 < n1:
    menor = 2

if n3 < menor:
    menor = n3

print('maior: {} \nmenor: {}'.format(maior,menor))


'''
outra forma 

maior = menor = 0
numero = []

for n in range(0,3):
    numero.append(int(input(f'Digite o {n +1}º número: ')))
numero.sort()
print(f'Menor número: {numero[0]}')
print(f'Maior número: {numero[-1]}')'''
