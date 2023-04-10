'''Faça um programa que leia um número inteiro e mostre seu fatorial

Ex: 5*4*3*2*1 = 120'''

from math import factorial

n = int(input('Digite um número: '))

f = factorial(n)

print('O Fatorial de {} é {}'.format(n, f))





