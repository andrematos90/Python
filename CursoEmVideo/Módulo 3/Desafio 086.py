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




                                CÓDIGO GUANABARA


matriz = [[0, 0 ,0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3): 
      for coluna in range(0, 3):
          matriz[linha][coluna] = int(input(f'Digite um valor para a posição {linha},{coluna}: '))

for linha in range(0, 3):
     for coluna in range(0, 3):
          print(f'[{matriz[linha][coluna]:^5}]', end=' ')
     print()



A primeira linha do código cria uma matriz 3x3 e a inicializa com zeros. A matriz é armazenada na variável "matriz".

A segunda linha inicia um loop "for" que irá iterar pelas linhas da matriz. O loop percorre as linhas de 0 a 2 (pois a matriz tem 3 linhas).

Dentro do loop "for" das linhas, é iniciado outro loop "for" que irá iterar pelas colunas da matriz. O loop percorre as colunas de 0 a 2 (pois a matriz tem 3 colunas).

Dentro do loop "for" das colunas, a função "input" é utilizada para solicitar que o usuário digite um valor para a posição atual da matriz. A posição é indicada pelas variáveis "linha" e "coluna", que foram definidas pelos loops anteriores. O valor digitado pelo usuário é convertido para um número inteiro e armazenado na posição correspondente da matriz.

Quando o loop "for" das colunas é concluído, o controle é retornado ao loop "for" das linhas. O próximo conjunto de linhas é iterado e o processo se repete.

Após todos os valores da matriz serem preenchidos pelo usuário, o programa entra em outro loop "for" que também itera pelas linhas da matriz.

Dentro deste novo loop "for", um terceiro loop "for" é iniciado para iterar pelas colunas da matriz.

Dentro do loop "for" das colunas, a função "print" é utilizada para imprimir na tela o valor armazenado na posição correspondente da matriz. A letra "f" antes da string indica que a string é uma f-string, que permite que variáveis e expressões sejam incorporadas na string. O valor é impresso com 5 espaços de largura, alinhado no centro.

O argumento "end" é passado para a função "print" com o valor " " (um espaço em branco), o que significa que um espaço em branco será impresso após o valor da matriz em vez de um caractere de nova linha. Isso é feito para que todos os valores da mesma linha da matriz sejam impressos na mesma linha da tela.

Quando o loop "for" das colunas é concluído, a função "print" é chamada novamente sem argumentos, o que significa que um caractere de nova linha é impresso na tela. Isso é feito para que a próxima linha da matriz seja impressa abaixo da linha anterior.

Quando o loop "for" das linhas é concluído, o programa termina.'''