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