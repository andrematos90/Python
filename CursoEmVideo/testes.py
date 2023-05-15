'''
Crie um programa que gere 5 números aleatórios e colocque-os em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor
que está na tupla.
'''

from random import  randint

numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10),)
print(numeros)
print(f'maior: {max(numeros)}')
print(f'menor: {min(numeros)}')