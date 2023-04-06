'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer.'''

from random import randint

computador = randint(0, 10)
acertou = False
palpites = 0

while not acertou:
    usuario = int(input('Digite um numero de 0 a 10: '))
    palpites+=1
    if usuario == computador:
        acertou = True
    else:
        if usuario < computador:
            print('Mais')
        elif usuario > computador:
            print("Menos")
print('Acertou com {} tentativas'.format(palpites))


