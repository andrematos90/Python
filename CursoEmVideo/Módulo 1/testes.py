#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

'''ex: numero :1834

unidade: 4
dezena: 3
centena: 8
milhar: '''

numero = int(input('Digite o número: '))
numuero_str = str(numero)
print(f'Milhar: {numuero_str[0]}')
print(f'Centena: {numuero_str[1]}')
print(f'Dezena: {numuero_str[2]}')
print(f'Unidade: {numuero_str[-1]}')