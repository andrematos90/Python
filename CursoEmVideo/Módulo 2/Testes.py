Produtos = ('ovo', 18.99, 'feijao', 5.88, 'carne', 10.99)

'''
o loop for é iniciado, utilizando a função range() 
para iterar sobre cada elemento da lista "Produtos"
ou seja vai do "0" até o tamanho da lista "5".

A condição "if" verifica se o valor da variável
"pos" (que é o índice atual do elemento da lista)
é divisível por 2. Se for, significa que a posição 
é par e o código dentro do bloco if é executado.'''

for pos in range(0, len(Produtos)):
    if pos % 2 == 0:
       print(f'{Produtos[pos]:.<30}', end='')  #formata com 30 caracteres
                                               #alinha o texto a esquerda e enche de pontos
    else:
        print(f'R${Produtos[pos]:>7.2f}')
'''
O bloco if simplesmente imprime o elemento da
 lista que está na posição "pos". Como a condição
   if garante que só serão impressos os elementos 
   de posição par, o código imprimirá somente os 
   nomes dos produtos (e não os preços).
'''