'''Crie um program que leia vários números inteiros. O programa só vai parar quando o usúario
digitar o valor "999", que é a condição de parada.No final, mostre quantos 
números foram digitados e qual foi a soma entre eles desconsiderando o "flag"'''

n = soma = contador = 0

while True:
    n = int(input('Digite um número[999] para parar: '))
    if n == 999:
        break
    contador +=1
    soma += n

print(f'Foram digitados {contador} números e a soma entre eles é {soma}')

'''
Neste código, criamos duas variáveis: soma e contador. A variável soma armazenará 
a soma dos números digitados pelo usuário, enquanto a variável contador contará 
quantos números foram digitados.

Dentro do while True, lemos um número inteiro digitado pelo usuário usando a função
 input() e o convertemos para um número inteiro usando a função int(). Se o número 
 digitado for igual a 999, usamos a instrução break para sair do loop. Caso contrário,
   adicionamos o número à variável soma e incrementamos a variável quantidade em 1.

Por fim, fora do loop, exibimos a mensagem com o número total de valores digitados
 e a soma desses valores.'''


 '''outra forma
 
 cont = 0
soma = 0
while True:
    n = int(input('Número [999 para parar]:  '))
    if n == 999:
        break
    else:
       soma = soma + n
       cont += 1
    
print(f'Foram digitados {cont} e a soma entre eles é: {soma}')
'''


