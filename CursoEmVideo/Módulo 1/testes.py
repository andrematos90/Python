# um professor quer sortear um dos seus quatro alunos para apagar o quadro
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido
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

