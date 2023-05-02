#crie um algoritimo que leia um numero e mostre seu dobro, triplo e raiz quadrada

from math import sqrt

numero = int(input('Digite um número: '))

print(f'Dobro: {numero * 2}')
print(f'Triplo: {numero * 3}')
print(f'Raiz: { sqrt(numero)}')