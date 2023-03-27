from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)
print('''Escolha:
[ 0] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input('Digite sua Opção: '))
print('-='*10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*10)

if computador == 0:   #computador jogou pedra
    if jogador == 0:
       print('empatou')
    elif jogador == 1:
       print('jogador vence')
    elif jogador == 2:
       print('Computador vence')
    else:
      print('Jogada inválida!')
elif computador == 1:  # computador jogou papl
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
         print('empatou')
    elif jogador == 2:
        print('jogador vence')
    else:
      print('Jogada inválida!')


elif computador == 2: # computador jogou tesoura
    if jogador == 0:
     print('jogador vence')
    elif jogador == 1:
      print('Computador vence')
    elif jogador == 2:
      print('empatou')
    else:
      print('Jogada inválida!')
