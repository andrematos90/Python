'''Crie um programa que eleia varios números inteiros. O Programa só vai parar qunado o usúario digitar 
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag "999")'''

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

