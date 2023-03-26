from datetime import date

ano_atual = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - nascimento



if idade == 18:
    print('Se alistar')
elif idade < 18:
    saldo = 18 - idade
    print('ainda faltam {} anos(s) para se alistar'.format(saldo))
    ano = ano_atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Já devia ter se alistado a {} ano'.format(saldo))
    ano = ano_atual - saldo
    print('Seu alistamento deveria ter sido em {}'.format(ano))