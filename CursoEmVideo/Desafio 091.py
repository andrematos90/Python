'''91 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = list()
print('Valores Sorteados')
sleep(3)
for k, v in jogo.items():
    print(f'{k} tirou: {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}')
    sleep(1)

'''
from random import randint: Importa a função randint do módulo random. Essa função será usada para gerar números aleatórios.

from time import sleep: Importa a função sleep do módulo time. Essa função será usada para adicionar pausas entre as ações do jogo.

from operator import itemgetter: Importa a função itemgetter do módulo operator. Essa função será usada para ordenar o dicionário pelo valor de um determinado item.

jogo = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6), 'jogador 3': randint(1, 6), 'jogador 4': randint(1, 6)}: Cria um dicionário chamado "jogo" com quatro jogadores. Cada jogador recebe um número aleatório entre 1 e 6 (simulando um lançamento de um dado).

ranking = list(): Cria uma lista vazia chamada "ranking" que será usada para armazenar o ranking dos jogadores.

for k, v in jogo.items():: Percorre o dicionário "jogo" usando o loop for. A cada iteração, a chave (nome do jogador) é armazenada em k e o valor (número tirado) é armazenado em v.

6.1. print(f'{k} tirou: {v}'): Imprime na tela o nome do jogador e o número tirado.

6.2. sleep(1): Aguarda 1 segundo antes de prosseguir para a próxima iteração.

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True): Ordena os itens do dicionário "jogo" com base nos valores (números tirados) em ordem decrescente. O resultado é atribuído à lista "ranking".

print('-=' * 30): Imprime na tela uma linha separadora para destacar o ranking.

for i, v in enumerate(ranking):: Percorre a lista "ranking" usando o loop for. A cada iteração, o índice é armazenado em i e o valor (tupla contendo o nome do jogador e o número tirado) é armazenado em v.

9.1. print(f'{i + 1}° lugar: {v[0]} com {v[1]}'): Imprime na tela a posição do jogador no ranking, seu nome e o número tirado.

9.2. sleep(1): Aguarda 1 segundo antes de prosseguir para a próxima iteração.


OUTRA FORMA

from random import randint
from time import sleep

players = dict()
print('Drawn values: ')
for play in range(1, 5):
    players[f'player{play}'] = randint(1, 6)
    print(f'    Player {play} rolled {players[f"player{play}"]}')
    sleep(0.5)
print('Player ranking')
for key, value in enumerate(sorted(players, key=players.get, reverse=True)):
    print(f'    {key + 1}° place: {value} with {players[value]}')
    sleep(0.5)
    
from random import randint: Importa a função randint do módulo random. Essa função será usada para gerar números aleatórios.

from time import sleep: Importa a função sleep do módulo time. Essa função será usada para adicionar pausas entre as ações do jogo.

players = dict(): Cria um dicionário vazio chamado "players" que será usado para armazenar os jogadores e os números tirados por eles.

print('Drawn values: '): Imprime na tela a mensagem "Drawn values: " para indicar que os números estão sendo sorteados.

for play in range(1, 5):: Percorre um loop for com o valor de play variando de 1 a 4, representando os jogadores.

5.1. players[f'player{play}'] = randint(1, 6): Atribui a cada jogador (chave do dicionário) um número aleatório entre 1 e 6 (simulando o lançamento de um dado) e armazena-o no dicionário "players".

5.2. print(f' Player {play} rolled {players[f"player{play}"]}'): Imprime na tela o número tirado por cada jogador.

5.3. sleep(0.5): Aguarda 0,5 segundos antes de prosseguir para o próximo jogador.

print('Player ranking'): Imprime na tela a mensagem "Player ranking" para indicar que o ranking dos jogadores será exibido.

for key, value in enumerate(sorted(players, key=players.get, reverse=True)):: Percorre um loop for utilizando a função enumerate para obter o índice (chave) e o valor do dicionário "players" em ordem decrescente com base nos números tirados pelos jogadores.

7.1. print(f' {key + 1}° place: {value} with {players[value]}'): Imprime na tela a posição do jogador no ranking, seu nome (chave) e o número tirado (valor).

7.2. sleep(0.5): Aguarda 0,5 segundos antes de prosseguir para o próximo jogador
    
    '''