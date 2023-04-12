'''Faça um programa que jogue para ou impar com o computador. O jogo
só sera interrompido quando o jogador perder. Mostrando o total de vitórias 
consecutivas do jogador.'''

from random import randint
from time import sleep

computador = randint(1,10)
jogador = str(input('Par ou Impar: ' )).upper().strip()

if jogador == 'PAR':
    jogada_computadoR = 'IMPAR'
else:
    jogada_computadoR ='PAR'

num = int(input('Digite um número: '))
total = computador + num

print(f'Computador jogou {computador} e você {num} total {total}')
sleep(2)

if total %2 == 0 and jogador == 'PAR':
    print('Você venceu!')
else:
    print('Computador venceu!')










