'''
94 - Crie um programa que leia o nome, sexo  e idade de várias pessoas, guardando os dados de cada uma delas em um dicionário e todos os dicionários em uma lista. No final mostre:
A - Quantas pessoas foram cadastradas.
B - A Média de idade do grupo.
C - Uma lista com todas as mulheres.
D - Uma lista com todas as pessoas com idade acima da média.'''

pessoa = {}
galera = []
media = total = 0


while True:
        pessoa.clear()
        pessoa['nome'] = input('Nome: ')
        while True:
                pessoa['sexo'] = input('Sexo [M/F]: ').upper()[0]
                if pessoa['sexo'] in 'MF':
                        break
                print('ERRO! O campo aceita apenas M ou F!')
        pessoa['idade'] = int(input('Idade: '))
        galera.append(pessoa.copy())
        total += 1
        while True:
                continuar = input('Continuar? [S/N]: ').upper()[0]
                if continuar in 'SN':
                  break
                print('ERRO! O campo aceita apena S ou N!')
        if continuar in 'N':
               break
print('-=' * 50)
print()
print(galera)
print()
print('-=' * 50)
print()
print('A - Quantas pessoas foram cadastradas.')
print(f'{total} Pessoas.')
