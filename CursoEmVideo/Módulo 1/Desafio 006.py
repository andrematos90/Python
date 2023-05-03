#crie um algoritimo que leia um numero e mostre seu dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))

d = n*2
t = n*3
r = n** (1/2)

print(' dobro:{}\n triplo:{}\n raiz:{}\n'.format(d,t,r))


'''
outra forma 

from math import sqrt

numero = int(input('Digite um número: '))

print(f'Dobro: {numero * 2}')
print(f'Triplo: {numero * 3}')
print(f'Raiz: { sqrt(numero)}')'''