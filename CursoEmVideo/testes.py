'''Crie um program que leia vários números inteiros. O programa só vai parar quando o usúario
digitar o valor "999", que é a condição de parada.No final, mostre quantos 
números foram digitados e qual foi a soma entre eles desconsiderando o "flag"'''

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

