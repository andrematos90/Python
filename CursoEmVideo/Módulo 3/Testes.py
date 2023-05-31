'''93 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de golds feitos em cada partida. No final, tudo será guardado em um dicionário, incluindo o total de gols feitos durante o campeona
95 - Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

from time import sleep
jogadores = []
jogador = {}
gols = []
tot = 0
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = input('Nome: ')
    jogador['partidas'] = int(input('Partidas: '))
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {c + 1}: ')))
    jogador['gol'] = gols.copy()
    jogadores.append(jogador.copy())
    tot = sum(jogador['gol'])
    while True:
        continuar = input('Continuar [S/N]: ' ).upper()[0]
        if continuar in  'SN':
            break
        print('ERRO! O campo aceita apenas S ou N!')
    if continuar == 'N':
        break
print(jogadores)
print()
print('-=' * 30)
print(f'{"cod":<5}{"NOME":>5}{"PARTIDAS":>15}{"GOLS" :>15}')
print()
for i, v in enumerate(jogadores):
    print(f'{i}')

    


