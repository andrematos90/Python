'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer.'''
import random
from time import sleep

palpites = 0
computer = random.randint(0, 10)
user = int(input('Type the number: '))

while user != computer:
  user = int(input('Type the number: '))
  palpites =  palpites + 1
 
if user == computer:
    print('Acertou depois de "{}" palpites'.format(palpites + 1))
    print('O computador pensou no numero: {} tambem!'.format(computer))



