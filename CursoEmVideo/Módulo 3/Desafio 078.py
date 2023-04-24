'''
Crie um programa que leia 5 valores numéricos e guarde em uma lista
No final, mostre qual foi o maior e o menor valor digitado e as respectivas
posições na lista'''

num = list()

for c in range(0,5):
   num.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Maior valor: {max(num)} na posição {num.index(max(num))}')
print(f'Menor valor: {min(num)} na posição {num.index(min(num))}')

'''
num = list(): cria uma lista vazia chamada "num".

for c in range(0,5):: inicia um loop "for" que se repete 5 vezes, 
variando o valor da variável "c" de 0 a 4.

num.append(int(input(f'Digite um valor para a posição {c}: '))): dentro do loop, 
solicita ao usuário que digite um valor, converte o valor para um número inteiro 
com "int" e adiciona o valor à lista "num".

print(f'Maior valor: {max(num)} na posição {num.index(max(num))}'): após o loop, 
exibe o maior valor da lista usando a função "max" e a posição do maior valor na
lista usando o método "index".

print(f'Menor valor: {min(num)} na posição {num.index(min(num))}'): em seguida, 
exibe o menor valor da lista usando a função "min" e a posição do menor valor na 
lista usando o método "index".

Resumindo, este código cria uma lista "num" de comprimento 5, pede ao usuário que 
digite um valor para cada posição da lista e, em seguida, encontra e exibe o maior
e o menor valor da lista e suas posições correspondentes.




                                 CÓDIGO GUANABARA


listanum = []
maior = 0
menor = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
          if listanum[c] > maior:
              maior = listanum[c]
          if listanum[c] < menor:
                menor = listanum[c]

print('=- * 30')
print(f'Você digitou os valores{listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}... ', end='')
print()

listanum = []: Cria uma lista vazia chamada "listanum" para armazenar os valores informados pelo usuário.
maior = 0: Inicializa a variável "maior" com o valor 0.
menor = 0: Inicializa a variável "menor" com o valor 0.
for c in range(0,5):: Inicia um laço de repetição for que se repete 5 vezes (uma vez para cada posição na lista).
listanum.append(int(input(f'Digite um valor para a posição {c}: '))): Em cada repetição do laço, o código solicita ao usuário que digite um número para a posição atual na lista e adiciona o número na lista "listanum".
if c == 0:: Verifica se é a primeira vez que o laço está sendo executado.
maior = menor = listanum[c]: Se for a primeira vez, inicializa as variáveis "maior" e "menor" com o valor do primeiro elemento da lista.
else:: Se não for a primeira vez, executa o bloco de código seguinte.
if listanum[c] > maior:: Verifica se o número atual é maior que a variável "maior".
maior = listanum[c]: Se for maior, atualiza a variável "maior" com o número atual.
if listanum[c] < menor:: Verifica se o número atual é menor que a variável "menor".
menor = listanum[c]: Se for menor, atualiza a variável "menor" com o número atual.
print('=-' * 30): Imprime uma linha de caracteres "=" para separar os resultados.
print(f'Você digitou os valores {listanum}'): Imprime os valores digitados pelo usuário.
print(f'O maior valor digitado foi {maior} nas posições ', end=''): Imprime o maior
valor digitado e a(s) posição(ões) em que ele aparece.
for i, v in enumerate(listanum):: Inicia um novo laço for que percorre a 
lista "listanum" e atribui a cada elemento o índice "i" e o valor "v".
if v == maior:: Verifica se o valor atual é igual ao maior valor encontrado.
print(f'{i}...', end=''): Se for igual, imprime o índice do valor na lista.
print(): Imprime uma nova linha para separar a saída.
print(f'O menor valor digitado foi {menor} nas posições ', end=''): Imprime o 
menor valor digitado e a(s) posição(ões) em que ele aparece.
for i, v in enumerate(listanum):: Inicia um novo laço for que percorre a 
lista "listanum" e atribui a cada elemento o índice "i" e o valor "v".
if v == menor:: Verifica se o valor atual é igual ao menor valor encontrado.
print(f'{i}... ', end=''): Se for igual, imprime o índ
'''

   

