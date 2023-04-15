'''
Desenvolva um programa que leia quatro valores inseridos  pelo usuário
e guarde-os em uma tupla. No final, mostre:

A - Quantas vezes apareceu o valor 9
B - Em que posição foi digitado o primeiro valor 3.
C - Quais foram os números pares.'''

numeros = ()

num9 = 0
primeiro_3 = 0
numerospares = ()

for c in range(4):
    num_digitado = int(input('Digite um número: '))
    numeros += (num_digitado,)

    if num_digitado == 9:
         num9 = num9 + 1
    if num_digitado == 3 and primeiro_3 == 0:
         primeiro_3 = numeros.index(3)
  
    if num_digitado % 2 == 0:
          numerospares += (num_digitado,)
         

print(f'O numero 9 apareceu: {num9} vezes')
if primeiro_3 == 0:
     print('Três não foi digitado')
else:
     print(f'Três digitado na posição: {primeiro_3 + 1}')
print(f'Numeros pares: {numerospares}')

'''
O código cria uma tupla vazia chamada "numeros", que será preenchida posteriormente.
Em seguida, ele cria três variáveis vazias: "num9", que será usada para contar 
quantas vezes o número 9 foi digitado; "primeiro_3", que será usada para armazenar 
a posição do primeiro número 3 digitado; e "numerospares", que será usada para 
armazenar todos os números pares digitados.
O código entra em um loop "for" que executará quatro vezes. Em cada iteração do 
loop, o usuário é solicitado a digitar um número inteiro.
O número digitado é adicionado à tupla "numeros".
Se o número digitado for igual a 9, a variável "num9" é incrementada em 1.
Se o número digitado for igual a 3 e o valor de "primeiro_3" ainda for 0, a 
posição do primeiro número 3 digitado é armazenada na variável "primeiro_3".
 Caso contrário, o valor de "primeiro_3" permanecerá 0.
Se o número digitado for par (ou seja, o resto da divisão por 2 for igual a 0),
 ele é adicionado à tupla "numerospares".
Após o loop terminar, o código imprime o número de vezes que o número 9 foi digitado.
Em seguida, o código verifica se um número 3 foi digitado. Se nenhum número 
3 foi digitado, ele imprime "Três não foi digitado". Caso contrário, ele imprime
 a posição do primeiro número 3 digitado na tupla "numeros".
Finalmente, o código imprime todos os números pares digitados 
na tupla "numerospares".


                                 CÓDIGO GUANABARA


num = (int(input('Digite um numero: ')),
      int(input('Digite um numero: ')),
      int(input('Digite um numero: ')),
      int(input('Digite um numero: ')))
      
print(f' O número "9" aparece {num.count(9)} vezes.')

if 3 in num:
    print(f'A primeira vez que o numero "3" aparece é na posição {num.index(3) + 1}')
else:
    print('O número "3" não aparece')

print('Números pares: ')
for n in num:   # para cada numero em n 
    if n % 2 == 0: # verifico se o resto é 0, se for 
        print(n, end=' ')# dou print em n



int(input('Digite um numero: '))): Essa linha cria uma tupla chamada num com quatro
 elementos. Cada elemento é um número inteiro digitado pelo usuário usando a função
   input() e convertido para inteiro com a função int().

print(f' O número "9" aparece {num.count(9)} vezes.'): Essa linha usa a 
função count() para contar quantas vezes o número 9 aparece na tupla num. 
O resultado é impresso na tela usando a f-string.

if 3 in num:: Essa linha verifica se o número 3 está presente na tupla num.

print(f'A primeira vez que o numero "3" aparece é na posição {num.index(3) + 1}'): 
Se o número 3 estiver presente na tupla num, essa linha usa a função index()
 para encontrar a posição do primeiro número 3 e adiciona 1 ao resultado 
 (porque as posições na tupla começam em 0, mas queremos que a posição seja 
 exibida a partir de 1). O resultado é impresso na tela usando a f-string.

else:: Se o número 3 não estiver presente na tupla num, essa linha é executada.

print('Números pares: '): Essa linha imprime na tela a mensagem "Números pares: ".

for n in num:: Essa linha inicia um loop for que percorre todos os elementos da 
tupla num. A cada iteração, o valor do elemento atual é armazenado na variável n.

if n % 2 == 0:: Essa linha verifica se o valor atual da variável n é par, ou seja,
 se o resto da divisão por 2 é igual a 0.

print(n, end=' '): Se o valor atual da variável n for par, essa linha imprime 
o valor na tela, seguido de um espaço em branco. A instrução end=' ' 
faz com que a próxima impressão seja feita na mesma linha, separada por um espaço 
em branco.






















'''