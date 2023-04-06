'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer.'''

'''escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
para o usuario descobrir qur número é esse. O Programa dira se acertou ou não.'''

import random
from time import sleep

cont = 0
computer = random.randint(0, 10)
user = int(input('Type the number: '))

while user != computer:
  print('O computador pensou no numero: {}'.format(computer))
  user = int(input('Type the number: '))
  cont = cont + 1

if user == computer:
    print('Acertou com depos de "{}" palpites'.format(cont +1))



