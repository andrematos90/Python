'''
Crieu uma tupla preenchida com os 20 primeiros colocados da tabela do brasileirão,
na ordem de colocação. Depois mostre:

A - Apenas os 5 primeiros
B - Os últimos 4 colocados
C - Crie uma lista com os times em ordem alfabética
D - Em que posição na tabela está o time do Joinville'''

Times = ('Joinville', 'Athletico-PR', 'Fluminense', 'Santos', 'Palmeiras', 'América-MG',
'Corinthians', 'Coritiba', 'Cruzeiro', 'Flamengo', 'Atlético-MG', 'Parana', 'Bahia',
'Botafogo', 'Internacional', 'Grêmio', 'Ponte Preta', 'Juventude', 'Criciuma', 'Sport')

print(f'Os cinco primeiros são: {Times[:5]}')
print(f'OS rebaixados são: {Times[-4:]}')
Ordem = sorted(Times)
print(f'Oderm alfabética: {Ordem}')
posicao = Times.index('Joinville')
print(f'Jec está na {posicao + 1}° posição')