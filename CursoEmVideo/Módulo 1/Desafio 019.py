# um professor quer sortear um dos seus quatro alunos para apagar o quadro
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido
import random

aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')

print('Aluno Escolhido: {}'.format(random.choice([aluno1,aluno2,aluno3,aluno4])))

'''
outra maneira de fazer 

import random

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')

lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)

print('Escolhido: {}' .format(escolhido))

outra forma 

from random import randint
from time import sleep
aluno1 = str(input('Nome do aluno: '))
aluno2 = str(input('Nome do aluno: '))
aluno3 = str(input('Nome do aluno: '))
aluno4 = str(input('Nome do aluno: '))
sorteado = randint(1, 4)
print('sorteando...')
sleep(2)
if sorteado == 1:
    print(f'O aluno sorteado foi {aluno1}')
elif sorteado == 2:
    print(f'O aluno sorteado foi {aluno2 }')
elif sorteado == 3:
    print(f'O sorteado foi {aluno3}')
elif sorteado == 4:
    print(f'O sorteado foi {aluno4}')

'''