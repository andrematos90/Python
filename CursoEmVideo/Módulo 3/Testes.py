'''80 - Crie um programa onde o usuário possa digitar cinco valores
e cadastre-os em uma lista, ja na posição correta de inserção
(sem usar o sort(). No final, mostre a lista ordenada na tela.)
'''

lista = []
posicao = 0

for c in range(0, 5):
    numero = int(input('Número: '))
    if c == 0:
        lista.append(numero)
    else:
        if numero > c:
            lista.append(numero)
        else:
              posicao = 0  # Define a variável 'posicao' como zero (posição inicial para a inserção do valor)
        while posicao < len(lista) and numero > lista[posicao]:  # Loop que roda enquanto a posição atual for menor que o tamanho da lista e o valor for maior do que o valor na posição atual da lista
            posicao += 1  # Incrementa a variável 'posicao' em uma unidade
        lista.insert(posicao, numero)  # Insere o valor na posição correta da lista
print('A lista ordenada é:', lista)  #















'''for c in range(0, 5):
    numero.append(int(input('Número: ')))
    if c == 0:
        lista.append(numero[c])
    else:
        if c > 0 and numero[c]:'''
            