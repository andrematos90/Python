'''Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se ja passou do tempo de alistamento

O programa tambem deve mostrar o tempo que falta ou que passou do prazo'''


from datetime import datetime

ano = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year

if ano_atual - ano > 18:
    print('Fora do prazo de alistamento!')
elif ano_atual - ano < 18:
    print('Idade insuficiente para alistamento!')
else:
    print('Hora de se alistar')