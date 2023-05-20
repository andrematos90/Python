''' 076 - Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando os dados em 
forma tabular.'''


produtos = ('ovo', 2.99,
            'pao', 3.44,
            'açucar', 8.99,
            'arroz', 10.88)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'RS{produtos[pos]:>5}')