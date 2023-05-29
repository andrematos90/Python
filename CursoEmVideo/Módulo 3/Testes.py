aluno = dict()

aluno['nome'] = str(input('Aluno: '))
aluno['media'] = float(input(f'média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
    
for k, v in aluno.items():
    print(f'{k} é igual {v}')