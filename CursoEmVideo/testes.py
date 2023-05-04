'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um nadador
e indique sua categoria de acorda com a sua idade:

- Até 9 anos: MIRIN
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER '''


from datetime import datetime

ano_atual = datetime.now().year
ano_de_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_de_nascimento
if idade <= 9:
    print(f'Idade {idade} Categoria: Mirin')
elif idade > 9 and idade <= 14:
    print(f'Idade {idade} Categoria: Infantil')
elif idade > 14 and idade <= 19:
    print(f'Idade {idade} Categoria: Junior')
elif idade > 19 and idade <= 20:
    print(f'Idade {idade} Categoria: Senior')
else:
    print(f'idade {idade} Categoria: Master')