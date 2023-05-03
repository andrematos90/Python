'''escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
para o usuario descobrir que número é esse. O Programa dira se acertou ou não.'''

from random import randint
from time import sleep

numero = randint(0,5)

chute = int(input('Digite um número entre 0 e 5: '))
print('Processando.')
sleep(1)
print('Processando..')
sleep(1)
print('Processando...')
sleep(1)
print('Processando.')
sleep(1)
print('Processando..')
sleep(1)
print('Processando...')
sleep(1)

if numero == chute:
    print('Boa! Acertou!')

else:
    print('Tente na próxima!')

print('Número da sorte {}'.format(numero))


'''
outra forma 

from random import randint
from time import sleep

computador = randint(0, 5)
usuario = int(input('Chute um número de 0 a 5:  '))

if computador == usuario:
    print('Pensando...')
    sleep(2)
    print('Você acertou!')
else:
    print('Pensando..')
    sleep(2)
    print(f'Você errou! O computador pensou no número {computador}!')
    '''