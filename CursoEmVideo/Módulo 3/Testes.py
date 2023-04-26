'''
84 - Faça um programa que leia o nome e peso de várias pessoas,
guardando tudo em uma lista, No final, mostre:

A - Quantas pessoas foram cadastradas.
B - Uma listagem das pessoas mais pesadas.
C - Uma listagem com as pessoas mais leves.'''


pesadas = []
leves = []

while True:
    nome = str(input('Nome: '))
    peso = str(input('Peso: '))
    if peso >= 70:
      pesadas.append(nome)
      pesadas.append(peso)
    elif peso >= 70:
       leves.append(nome)
       leves.append
    resposta = str(input('Continuar? [S/N]'))
    if resposta in 'Nn':
        break

print(f'Pessoas mais pesados: {pesadas}')
print(f'Pessoas mais leves: {leves}')






