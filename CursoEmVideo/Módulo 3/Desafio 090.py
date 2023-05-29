''' 90 - Faça um programa que leia o nome de média de um aluno, guardando tambem a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

Aluno = {}

Aluno['nome'] = str(input('Nome do aluno: '))
Aluno['media'] = int(input(f'Média de {Aluno["nome"]}: '))

if Aluno['media'] >= 7:
    print(f'{Aluno["nome"]} está aprovado!')
else:
    print(f'{Aluno["nome"]} está reprovado!')