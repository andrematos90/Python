'''93 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de golds feitos em cada partida. No final, tudo será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
from time import sleep
jogador = {}
gols = []
jogador['nome'] = input('Nome: ')
jogador['partidas'] = int(input('Partidas: '))
for c in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
jogador['gol'] = gols
print(jogador)
for i, v in enumerate(gols):
    print(f'na partida {i + 1} fez {v} gols')
    sleep(1)
    


