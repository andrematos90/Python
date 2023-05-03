'''Faça um programa que leia um ano qualquer e mostre se é bissexto'''

import datetime

ano_atual = datetime.datetime.now().year

ano = int(input('Digite o ano ou 0 para o ano atual: '))

if ano == 0:
    ano = datetime.datetime.now().year

if ano % 4 == 0 and ano % 100 != 0:
    print('Ano bissexto')
elif  ano %400 == 0:
    print('Ano bissexto')
else:
    print('Não é ano bissexto')