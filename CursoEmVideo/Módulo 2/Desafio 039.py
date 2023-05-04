'''Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se ja passou do tempo de alistamento

O programa tambem deve mostrar o tempo que falta ou que passou do prazo'''

import datetime


nascimento = int(input('Digite o seu ano de nascimento: '))
data_atual = datetime.datetime.now()
ano_atual = int ( data_atual. strftime ( "%Y" ))


if nascimento + 18 > ano_atual:
    print('Não se alista! ainda faltam {} ano(s) para se alistar.'.format((nascimento + 18) - ano_atual))
    
elif nascimento + 18 == ano_atual:
    print('É hora de se alistar!')

elif nascimento + 18 < ano_atual:
    print('já passou {} ano(s) da hora de se alistar'.format(abs((nascimento + 18) - ano_atual)))

'''
outra forma 

from datetime import datetime

ano = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year

if ano_atual - ano > 18:
    print('Fora do prazo de alistamento!')
elif ano_atual - ano < 18:
    print('Idade insuficiente para alistamento!')
else:
    print('Hora de se alistar')'''




