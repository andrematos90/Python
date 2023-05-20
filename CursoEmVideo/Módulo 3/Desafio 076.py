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
print('=' * 40) - imprime uma linha horizontal de 40 caracteres de comprimento.




                                COÓDIGO GUANABARA


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


Produtos = ('ovo', 18.99, 'feijao', 5.88, 'carne', 10.99)


o loop for é iniciado, utilizando a função range() 
para iterar sobre cada elemento da lista "Produtos"
ou seja vai do "0" até o tamanho da lista "5".

A condição "if" verifica se o valor da variável
"pos" (que é o índice atual do elemento da lista)
é divisível por 2. Se for, significa que a posição 
é par e o código dentro do bloco if é executado.

for pos in range(0, len(Produtos)):
    if pos % 2 == 0:
       print(f'{Produtos[pos]:.<30}', end='')  #formata com 30 caracteres
                                               #alinha o texto a esquerda e enche de pontos
    else:
        print(f'R${Produtos[pos]:>7.2f}')

O bloco if simplesmente imprime o elemento da
 lista que está na posição "pos". Como a condição
   if garante que só serão impressos os elementos 
   de posição par, o código imprimirá somente os 
   nomes dos produtos (e não os preços).
'''

 
