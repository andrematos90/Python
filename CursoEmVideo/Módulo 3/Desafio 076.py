'''Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando os dados em 
forma tabular.'''


Produtos = ('ovo', 18.99, 'feijao', 5.88, 'carne', 10.99)

print('=' * 40)
print('{:^40}'.format('LISTA DE PRODUTOS'))
print('=' * 40)

for c in Produtos:
    print(f'{Produtos[0]+2}')