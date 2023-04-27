'''
86 - Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores
lidos pelo teclado.
No final, motre a matriz na tela com a formatação correta.
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        numero = int(input(f' Digite um número para a posição [{i}] [{j}]: '))
        matriz[i][j] = numero

for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()

'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]: Aqui, estamos criando uma matriz 3x3 inicialmente preenchida com zeros.

for i in range(3):: Esse laço for percorre cada linha da matriz, onde i é o índice da linha atual.

for j in range(3):: Esse laço for percorre cada coluna da matriz, onde j é o índice da coluna atual.

numero = int(input(f' Digite um número para a posição [{i}] [{j}]: ')): Aqui, estamos solicitando ao usuário que insira um número para a posição [i][j] da matriz. A função input() recebe o valor digitado pelo usuário e a função int() converte o valor para um número inteiro.

matriz[i][j] = numero: Aqui, estamos atribuindo o valor digitado pelo usuário na posição [i][j] da matriz.

for linha in matriz:: Esse laço for percorre cada linha da matriz.

for elemento in linha:: Esse laço for percorre cada elemento da linha atual.

print(elemento, end=' '): Aqui, estamos imprimindo cada elemento da matriz na mesma linha, separados por um espaço em branco. O parâmetro end especifica o caractere a ser adicionado ao final da linha, que por padrão é a quebra de linha \n.

print(): Aqui, estamos imprimindo uma quebra de linha para iniciar a impressão da próxima linha da matriz.

Em resumo, o código solicita ao usuário que insira um número para cada posição da matriz e, em seguida, imprime a matriz preenchida.
'''