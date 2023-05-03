#Crie um program que leia um número real e mostre na tela somente sua porção inteira
from math import trunc
num = float(input('Digite um número real: '))

inteiro = trunc(num)

print('parte inteira: {}'.format(inteiro))


'''


outra forma de fazer

import math

num = float(input('Digite um número real: '))

print('parte interia {}'.format(math.trunc(num)))




outra maneira sem importar modulos

num = float(input('Digite um numero real: '))

print('parte inteira: {}' .format(int(num)))

outra forma 

numero = float(input('Digite um número real: '))
print(f'{numero:.0f}')


'''