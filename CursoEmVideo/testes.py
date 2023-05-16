'''Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando os dados em 
forma tabular.'''

produtos = ('ovo', 3.99, 'pao', 4.99, 'leite', 8.99)
for c in range(0, len(produtos), 2):
    print(produtos[c])

