'''
88 - Crie um programa que ajude um jogador da mega sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e sortear 6 números
para cada um deles  entre 1, 60, cadastrando tudo em uma lista composta.'''
from random import randint

jogos = int(input('Quantos jogos? '))
palpites = []

for p in range (0, jogos):  
    for c in range(0, 6):
        palpites.append(randint(1, 60))
        print(palpites)
    palpites.clear()

    
