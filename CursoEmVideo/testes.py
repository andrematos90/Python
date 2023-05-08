'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer.'''


from random import randint
from time import sleep

palpites = 0
numero = randint(0, 10)



while True:
        chute = int(input('Digite um número entre 0 e 10: '))
        print('Processando.')
        sleep(1)
        print('Processando..')
        sleep(1)

        if numero == chute:
            print(f'Boa! Acertou! com {palpites +1} palpites!')

            break

        else:
            print('Tente na próxima!')
            palpites += 1


        