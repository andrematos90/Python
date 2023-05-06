'''Crie um programa que leia o ano de nascimento de 7 pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade (21 anos) e quantos ja são maiores '''

import datetime
ano_nascimento = 0
maiores = 0
menores = 0

for c in range(0, 7):
    ano_nascimento = int(input('Ano de Nascimento: '))
    idade = datetime.datetime.now().year - ano_nascimento
    if idade > 21:
        maiores += 1
    else:
        menores += 1
print(f'{maiores} Pessoas maiores de idade')
print(f'{menores} Pessoas menores de idade')
