matriz = [[0, 0 ,0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3): 
      for coluna in range(0, 3):
          matriz[linha][coluna] = int(input(f'Digite um valor para a posição {linha},{coluna}: '))

for linha in range(0, 3):
     for coluna in range(0, 3):
          print(f'[{matriz[linha][coluna]:^5}]', end=' ')
     print()


'''
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
