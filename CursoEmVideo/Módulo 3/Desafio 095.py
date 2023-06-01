'''95 - Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

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

'''
Inicialize as variáveis:

jogadores: uma lista vazia para armazenar os dados dos jogadores.
jogador: um dicionário vazio para armazenar os dados de cada jogador.
gols: uma lista vazia para armazenar a quantidade de gols em cada partida.
Inicie um loop infinito para adicionar os jogadores:

Limpe o dicionário jogador e a lista gols a cada iteração.
Solicite o nome do jogador e a quantidade de partidas jogadas.
Inicie outro loop para inserir a quantidade de gols em cada partida, armazenando-os na lista gols.
Copie a lista gols para a chave 'gol' do dicionário jogador.
Calcule a soma dos gols e armazene o total na chave 'total' do dicionário jogador.
Adicione uma cópia do dicionário jogador à lista jogadores.
Após a coleta dos dados dos jogadores, utilize um loop para exibir as estatísticas de cada jogador:

Imprima o cabeçalho da tabela.
Utilize um loop enumerate para percorrer a lista jogadores e obter o índice e o dicionário de cada jogador.
Imprima os dados de cada jogador na tabela formatada.
Em seguida, inicie um novo loop para mostrar os detalhes do aproveitamento de um jogador específico:

Solicite ao usuário o código do jogador que deseja visualizar ou digite "999" para encerrar o programa.
Se o código for igual a 999, saia do loop.
Caso contrário, exiba os detalhes do jogador com base no código fornecido pelo usuário.'''