# digite um angulo e calcule o seno,cosseno e tangente desse angulo

import math
from math import sin,cos,tan

A = int(input('Angulo: '))

seno = math.sin(A)
cosseno = math.cos(A)
tangente = math.tan(A)

print('Seno: {:.2f}' .format(seno))
print('Cosseno: {:.2f}'.format(cosseno))
print('Tangente: {:.2f}'.format(tangente))

'''
outra forma 

import math

angulo = int(input('Digite o angulo: '))
print(f'Seno: {math.sin(angulo):.2f}')
print(f'Cosseno: {math.cos(angulo):.2f}')
print(f'Tangente: {math.tan(angulo):.2f}')'''