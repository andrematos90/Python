#algoritmo que le o nome de quatro alunos e sorteie uma ordem de apresentação
import random

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')

lista = [a1,a2,a3,a4]

random.shuffle(lista)

print('Ordem: {}'.format(lista))


'''
outra forma

import random
aluno1 = str(input('Nome do aluno: '))
aluno2 = str(input('Nome do aluno: '))
aluno3 = str(input('Nome do aluno: '))
aluno4 = str(input('Nome do aluno: '))
alunos = []

alunos.append(aluno1)
alunos.append(aluno2)
alunos.append(aluno3)
alunos.append(aluno4)
random.shuffle(alunos)
print(f'Ordem de apresnetação: ')

for a in alunos:
    print(f'{a}')
    
    '''