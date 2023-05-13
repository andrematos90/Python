'''Faça um programa que jogue para ou impar com o computador. O jogo
só sera interrompido quando o jogador perder. Mostrando o total de vitórias 
consecutivas do jogador.'''

from random import randint

vitorias_jogador = jogador = computador = resultado = 0
palpite = ''
while True:
    palpite = str(input('Par ou Impar: ')).upper().strip()
    computador = randint(0 ,5)
    jogador = int(input('Numero de 0 a 5: '))
    resultado = computador + jogador
    print(f'Computador jogou: {computador}')
    print(f'Resultado: {resultado}')
    if palpite == 'PAR' and resultado %2 == 0:
        vitorias_jogador += 1
        print('Você venceu!')
    else:
        print('Computador venceu!')
        print(f'Quantidade de vitórias suas: {vitorias_jogador}')
        break


