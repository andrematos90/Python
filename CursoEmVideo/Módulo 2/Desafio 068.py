'''Faça um programa que jogue para ou impar com o computador. O jogo
só sera interrompido quando o jogador perder. Mostrando o total de vitórias 
consecutivas do jogador.'''

from random import randint
from time import sleep

while True:
    computador = randint(1,10)
    jogador = str(input('Par ou Impar: ' )).upper().strip()
    jogadas = 0

    if jogador == 'PAR':
        jogada_computadoR = 'IMPAR'
    else:
        jogada_computadoR ='PAR'

    num = int(input('Digite um número: '))
    total = computador + num
   
    print(f'Computador jogou {computador} e você {num} total {total}')
    sleep(2)

    if total %2 == 0 and jogador == 'PAR':
        vitoria =+1
        print('Deu Par, você venceu!')    
    elif total %2 == 0 and jogada_computadoR == 'PAR':
        print('Deu Par, computador venceu!')
        print(f'Você teve {vitoria} vitórias!')
        break
    elif total %2 != 0 and jogador == 'IMPAR':
        print('Deu Impar, você venceu!')
        vitoria =+1
    elif total %2 != 0 and jogada_computadoR == 'IMPAR':
        print('Deu Impar, o computador venceu!')
        print(f'Você teve {vitoria} vitórias!')
        break










