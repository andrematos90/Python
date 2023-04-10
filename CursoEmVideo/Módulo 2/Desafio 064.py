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
