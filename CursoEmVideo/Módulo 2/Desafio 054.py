'''Crie um programa que leia o ano de nascimento de 7 pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade (21 anos) e quantos ja são maiores '''

from datetime import date

ano_atual = date.today().year
maiores = 0
menores = 0

for pessoa in range(1, 8):
    ano_nascimento = int(input('Digite o ano de Nascimento da {}ª pessoa: '.format(pessoa)))
    idade = ano_atual - ano_nascimento
    if idade <= 21:
       menores = menores +1
    else: 
        maiores = maiores +1

print('A quantidade de maiores é de {} pessoas'.format(maiores))
print('A quantidade de menores é {} pessoas'.format(menores))
