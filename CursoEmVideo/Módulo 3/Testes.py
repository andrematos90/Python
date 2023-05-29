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