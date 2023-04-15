'''Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando os dados em 
forma tabular.'''


Produtos = ('ovo', 18.99, 'feijao', 5.88, 'carne', 10.99)

print('=' * 40)
print('{:^40}'.format('LISTA DE PRODUTOS'))
print('=' * 40)

for i in range(0, len(Produtos), 2):
             print(f'{Produtos[i]:.<30} R${Produtos[i+1]:>7.2f}')

print('=' * 40)


'''
Produtos = ('ovo', 18.99, 'feijao', 5.88, 'carne', 10.99) - cria uma tupla de produtos,
onde cada elemento é um nome de produto seguido pelo seu preço.
print('=' * 40) - imprime uma linha horizontal de 40 caracteres de comprimento, 
composta pelo caractere "=" repetido 40 vezes.
print('{:^40}'.format('LISTA DE PRODUTOS')) - imprime o título "LISTA DE PRODUTOS" 
centralizado em uma linha de 40 caracteres.
print('=' * 40) - imprime outra linha horizontal de 40 caracteres de comprimento.
for i in range(0, len(Produtos), 2): - itera sobre os índices da tupla de produtos, 
começando em 0, até o comprimento da tupla, avançando de 2 em 2 (ou seja, a cada dois
elementos). Isso permite que o código processe os nomes e preços de cada produto.
print(f'{Produtos[i]:.<30} R${Produtos[i+1]:>7.2f}') - para cada elemento ímpar na
tupla (ou seja, o nome do produto), formata a string de saída para que o nome seja 
alinhado à esquerda com pontos para preencher o espaço restante até 30 caracteres, 
seguido pela string "R$" e o preço do produto alinhado à direita com zeros para 
preencher o espaço restante até 7 caracteres e duas casas decimais.
print('=' * 40) - imprime uma linha horizontal de 40 caracteres de comprimento.'''

