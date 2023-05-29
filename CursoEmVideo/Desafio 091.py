'''91 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep

jogadores = {'':'', '':'', '':'', '':''}
jogador = 0
jogada = 0

for c in range(0, 4):
    jogador = c
    palpite = randint(0, 6)
    jogadores['jogador']  = jogador
    jogadores['jogada'] = palpite

for c in range (0, 4):
    print(f'O jogador {jogadores["jogador"]} jogador {jogadores["jogada"]}')
    sleep(1)
