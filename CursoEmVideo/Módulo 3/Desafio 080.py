'''Crie um programa onde o usuário possa digitar cinco valores
e cadastre-os em uma lista, ja na posição correta de inserção
(sem usar o sort(). No final, mostre a lista ordenada na tela.)'''

lista = []
for i in range(5):
    valor = int(input('Digite um valor: '))
    if i == 0:
        lista.append(valor)
    else:
        posicao = 0
        while posicao < len(lista) and valor > lista[posicao]:
            posicao += 1
        lista.insert(posicao, valor)
print('A lista ordenada é:', lista)

'''
Cria uma lista vazia chamada "lista".
Inicia um loop "for" que executa 5 vezes.
Dentro do loop, solicita que o usuário insira um valor inteiro.
Verifica se a variável "i" é igual a 0. Se sim, adiciona o valor à lista vazia.
 Se não, segue para o próximo passo.
Inicia um loop "while" para inserir o valor em ordem crescente na lista. 
O loop continua enquanto a variável "posicao" é menor que o comprimento da lista
 e o valor a ser inserido é maior do que o valor na posição atual.
Quando a posição correta é encontrada, insere o valor na lista.
Retorna ao loop "for" e repete os passos 3 a 6 para os próximos valores inseridos pelo usuário.
Quando o loop "for" termina, imprime a lista ordenada.'''