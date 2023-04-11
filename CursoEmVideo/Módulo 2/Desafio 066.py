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


