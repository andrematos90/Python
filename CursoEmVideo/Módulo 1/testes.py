#algoritmo que le o nome de quatro alunos e sorteie uma ordem de apresentação

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



