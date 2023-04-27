'''
Aprimore o desafio anterior, mostrando no final:
A - A soma de todos os valores pares digitados.
B - A soma dos valores da terceira coluna .
C - O maior valor da segunda linha.'''


matriz = [[0, 0 ,0], [0, 0, 0], [0, 0, 0]]
pares = []
segunda_linha = []

for linha in range(0, 3): 
      for coluna in range(0, 3):
          matriz[linha][coluna] = int(input(f'Digite um valor para a posição {linha},{coluna}: '))
          if matriz[linha][coluna] % 2 == 0:
               pares.append(matriz[linha][coluna])
for linha in range(0, 3):
     for coluna in range(0, 3):
          print(f'[{matriz[linha][coluna]:^5}]', end=' ')
     print()
print(f'soma dos valores pares é: {sum(pares)}')
soma = 0
for linha in matriz:
               soma+= linha[2]
print(f'soma da terceira coluna: {soma}')

segunda_linha = matriz[1]
segunda_linha.sort()
print(f'O maior valor da segunda linha é: {segunda_linha[-1]}')

'''
Criação da matriz vazia com valores iniciais zerados.
Criação de duas listas vazias, "pares" e "segunda_linha", que serão utilizadas para armazenar os valores pares digitados e a segunda linha da matriz, respectivamente.
Utilização de dois loops "for" encadeados para percorrer cada posição da matriz, solicitando ao usuário que digite um valor para cada posição. Além disso, o código verifica se o valor digitado é par, e caso seja, adiciona esse valor na lista "pares".
Utilização de outros dois loops "for" para exibir a matriz preenchida com os valores digitados pelo usuário. Para cada posição da matriz, o valor é exibido entre colchetes "[ ]" e centralizado em uma área de 5 caracteres, utilizando a função "print".
Cálculo da soma de todos os valores pares digitados, utilizando a função "sum" da linguagem Python para somar os valores presentes na lista "pares". O resultado é exibido na tela.
Cálculo da soma dos valores presentes na terceira coluna da matriz, utilizando mais um loop "for" para percorrer todas as linhas e somar os valores da terceira coluna. O resultado é exibido na tela.
Atribuição da segunda linha da matriz para a lista "segunda_linha". Em seguida, a lista é ordenada em ordem crescente utilizando o método "sort". Por fim, é exibido na tela o maior valor presente na segunda linha da matriz.'''


              
       