''' 90 - Faça um programa que leia o nome de média de um aluno, guardando tambem a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

Aluno = {}

Aluno['nome'] = str(input('Nome do aluno: '))
Aluno['media'] = int(input(f'Média de {Aluno["nome"]}: '))

if Aluno['media'] >= 7:
    print(f'{Aluno["nome"]} está aprovado!')
else:
    print(f'{Aluno["nome"]} está reprovado!')

'''
                            CÓDIGO GUANABARA 
                            
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
    
    
aluno = dict(): Cria um dicionário vazio chamado "aluno".

aluno['nome'] = str(input('Aluno: ')): Solicita ao usuário o nome do aluno e armazena-o na chave 'nome' do dicionário "aluno".

aluno['media'] = float(input(f'média de {aluno["nome"]}: ')): Solicita ao usuário a média do aluno e armazena-a na chave 'media' do dicionário "aluno". O uso de float() garante que a média seja armazenada como um número decimal (float).

A estrutura condicional if-elif-else avalia a média do aluno e atribui a situação correspondente à chave 'situação' do dicionário "aluno":

Se a média for maior ou igual a 7, a situação é definida como 'Aprovado'.
Se a média for menor que 7, a situação é definida como 'Recuperação'.
Caso contrário, a situação é definida como 'Reprovado'.
O loop for percorre todas as chaves e valores do dicionário "aluno" usando o método items(). A cada iteração, a chave é armazenada em k e o valor correspondente é armazenado em v.

print(f'{k} é igual {v}'): Imprime na tela cada chave e seu valor correspondente no formato "chave é igual valor".
'''