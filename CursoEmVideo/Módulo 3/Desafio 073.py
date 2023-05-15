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

print('='* 50)
print(f'5 Primeiros: {Times[0:5]}\n')
print('='* 50)
print(f'OS 4 ultimos são: {Times[-4:]}')
print('='* 50)
print(f'Ordem alfabética: {sorted(Times)}')
print('='* 50)
print(f'JEC está na posição: {Times.index("Joinville") +1 }ª Posição')
print('='* 50)


'''
print('='* 50): essa linha exibe uma linha de 50 caracteres iguais de '=' na tela.

print(f'5 Primeiros: {Times[0:5]}\n'): essa linha exibe os primeiros 5 elementos da 
lista Times em uma string formatada e adiciona uma nova linha no final.

print('='* 50): essa linha exibe outra linha de 50 caracteres iguais de '=' na tela.

print(f'OS 4 ultimos são: {Times[-4:]}'): essa linha exibe os últimos 4 elementos da 
lista Times em uma string formatada.

print('='* 50): essa linha exibe outra linha de 50 caracteres iguais de '=' na tela.

print(f'Ordem alfabética: {sorted(Times)}'): essa linha exibe a lista Times 
ordenada em ordem alfabética em uma string formatada.

print('='* 50): essa linha exibe outra linha de 50 caracteres iguais de '=' na tela.

print(f'JEC está na posição: {Times.index("Joinville") +1 }ª Posição'): essa linha 
determina a posição da string "Joinville" na lista Times e exibe essa informação em
 uma string formatada.

print('='* 50): essa linha exibe outra linha de 50 caracteres iguais de '=' na tela.


outra forma 

Times = ('Joinville', 'Athletico-PR', 'Fluminense', 'Santos', 'Palmeiras', 'América-MG',
'Corinthians', 'Coritiba', 'Cruzeiro', 'Flamengo', 'Atlético-MG', 'Parana', 'Bahia',
'Botafogo', 'Internacional', 'Grêmio', 'Ponte Preta', 'Juventude', 'Criciuma', 'Sport')

print(f'Os cinco primeiros são: {Times[:5]}')
print(f'OS rebaixados são: {Times[-4:]}')
Ordem = sorted(Times)
print(f'Oderm alfabética: {Ordem}')
posicao = Times.index('Joinville')
print(f'Jec está na {posicao + 1}° posição')'''