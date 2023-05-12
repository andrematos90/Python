'''Crie um programa que eleia varios números inteiros. O Programa só vai parar qunado o usúario digitar 
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag "999")'''

n = soma = cont = 0 # todas as variáveis recebem o valor "0"
n = int(input('Digite um número [999 para encerrar!]: '))

while n != 999:
    soma = soma + n
    cont = cont + 1 
    n = int(input('Digite um número [999 para encerrar!]: '))
print('Foram Digitiados {} números e a soma total é de {}'.format(cont, soma))


'''
outra forma 

soma = 0
cont = 0
numero = 0

while True:
    numero = int(input('Numero: [999] para parar: '))
    if numero == 999:
        break
    else:
     soma = soma + numero
     cont += 1
print(f'Soma dos números: {soma}')
print(f'Quantidade de números somados: {cont}')


Inicializamos três variáveis: soma, cont e numero. A soma será usada para armazenar a soma dos números digitados, cont será usado para contar a quantidade de números somados, e numero é inicializado com o valor 0.

Inicia-se um loop infinito utilizando while True. Isso significa que o loop continuará executando até que seja explicitamente interrompido por um break.

Dentro do loop, solicitamos ao usuário que digite um número utilizando a função input. O texto exibido ao usuário é "Numero: [999] para parar: ". A função int é utilizada para converter a entrada em um número inteiro, e o valor digitado é armazenado na variável numero.

Verificamos se o número digitado é igual a 999, que é o critério para sair do loop. Se for verdadeiro, usamos o comando break para sair do loop e continuar a execução do programa.

Caso contrário, somamos o número digitado à variável soma e incrementamos o contador cont em 1 para contar mais um número somado.

O programa retorna ao início do loop, repetindo os passos 3 a 5 até que o número 999 seja digitado.

Quando o loop é interrompido, o programa continua sua execução fora do loop.

Utilizando uma f-string, exibimos a soma dos números digitados pelo usuário, formatada na frase "Soma dos números: {soma}".

Utilizando outra f-string, exibimos a quantidade de números somados, formatada na frase "Quantidade de números somados: {cont}".

A execução do programa é concluída.

'''