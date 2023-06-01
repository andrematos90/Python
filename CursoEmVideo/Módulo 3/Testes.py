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
    tot = sum(jogador['gol'])
    jogador['total'] = tot
    jogadores.append(jogador.copy()) 
    while True:
        continuar = input('Continuar [S/N]: ' ).upper()[0]
        if continuar in  'SN':
            break
        print('ERRO! O campo aceita apenas S ou N!')
    if continuar == 'N':
        break
print()
print(jogadores)
print()
print('-=' * 30)
print(f'{"cod":<5}{"NOME":<10}{"PARTIDAS":<10}{"GOLS":<20}{"TOTAL":<10}')
print('-' * 60)
for i, jogador in enumerate(jogadores):
    print(f'{i+1:<5}{jogador["nome"]:<10}{jogador["partidas"]:<10}{str(jogador["gol"]):<20}{jogador["total"]:<10}')
print('-' * 60)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999] para parar: '))
    if busca == 999:
        break
    else:
        print(f'Estatísticas de {jogadores[busca]["nome"]}')


    
    


