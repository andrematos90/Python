'''Crie um prorgama que jogue jokenpo com você'''

from random import randint
from time import sleep

numero = randint(0,2)

if numero == 0:
    computador = 'pedra'

elif numero == 1:
    computador = 'tesoura' 

else:
    computador = 'papel'



usuario = str(input('Digite "pedra, "tesoura" ou "papel": ')).lower()
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print(computador)
sleep(1)


if computador == usuario:
    print('Ninguem ganha!')
elif numero == 0 and usuario == 'tesoura':
    print('Eu venci você!')
elif numero == 0 and usuario =='papel':
    print('Você me venceu!')
elif numero == 1 and usuario == 'pedra':
     print('Você me venceu!')
elif numero == 1 and usuario =='papel':
       print('Eu venci você!')
elif numero == 2 and usuario == 'pedra':
       print('Eu venci você!')
elif numero == 2 and usuario == 'tesoura':
     print('Você me venceu!')



