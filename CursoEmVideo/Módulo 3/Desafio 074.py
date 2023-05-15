'''
Crie um programa que gere 5 números aleatórios e colocque-os em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor
que está na tupla.
'''

from random import randint

Numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print(Numeros)
print(f'Maior número {max(Numeros)} e o menor é o {min(Numeros)}')

'''
from random import randint: essa linha importa a função randint do módulo random. 
A função randint é usada para gerar números inteiros aleatórios entre dois valores.

Numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), 
randint(0,10)): essa linha cria uma tupla chamada Numeros que contém 5 
números inteiros aleatórios gerados pela função randint com valores entre 0 e 10.

print(Numeros): essa linha exibe na tela a tupla Numeros.

print(f'Maior número {max(Numeros)} e o menor é o {min(Numeros)}'): 
essa linha usa as funções max e min para determinar o maior e o menor 
número na tupla Numeros e exibe esses valores na tela em uma string formatada.

Em resumo, esse código Python gera uma tupla com 5 números inteiros
 aleatórios entre 0 e 10 e exibe na tela essa tupla e o maior e o menor número nela.
 
 outra forma 
 
 from random import  randint
numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10),)
print(numeros)
print(f'maior: {max(numeros)}')
print(f'menor: {min(numeros)}')'''