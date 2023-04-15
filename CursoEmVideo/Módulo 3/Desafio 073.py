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


print(f'5 Primeiros: {Times[0:5]}\n')
print(f'Ordem alfabética: {sorted(Times)}')
Joinville = 'Joinville'
print(f'JEC está na posição: {Times.index(Joinville) +1 }ª Posição')