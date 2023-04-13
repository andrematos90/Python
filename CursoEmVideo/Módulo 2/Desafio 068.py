'''Faça um programa que jogue para ou impar com o computador. O jogo
só sera interrompido quando o jogador perder. Mostrando o total de vitórias 
consecutivas do jogador.'''

from random import randint
from time import sleep
vitoria = 0
while True:
    computador = randint(1,10)

    jogador = str(input('Par ou Impar: ' )).upper().strip()
    
    if jogador == 'PAR':
        jogada_computadoR = 'IMPAR'
    else:
        jogada_computadoR ='PAR'

    num = int(input('Digite um número: '))
    total = computador + num
   
    print(f'Computador jogou {computador} e você {num} total {total}')
    sleep(2)

    if total %2 == 0 and jogador == 'PAR':
        vitoria = vitoria + 1
        print('Deu Par, você venceu!')    
    elif total %2 == 0 and jogada_computadoR == 'PAR':
        print('Deu Par, computador venceu!')
        print(f'Você teve {vitoria} vitórias!')
        break
    elif total %2 != 0 and jogador == 'IMPAR':
        vitoria = vitoria + 1
        print('Deu Impar, você venceu!')
    elif total %2 != 0 and jogada_computadoR == 'IMPAR':
        print('Deu Impar, o computador venceu!')
        print(f'Você teve {vitoria} vitórias!')
        break


'''
O código começa com um loop while True, que executa o jogo repetidamente até que o
 usuário decida sair.

Dentro do loop, o computador escolhe um número aleatório entre 1 e 10, e o
 usuário escolhe se quer jogar Par ou Ímpar. O código verifica se o jogador
   escolheu Par ou Ímpar e escolhe automaticamente a jogada oposta para o computador.

O código então pede ao usuário para digitar um número, e calcula a soma do
 número escolhido pelo usuário e o número escolhido pelo computador. O código 
 então verifica se a soma é par ou ímpar e compara com a escolha do jogador para
   determinar se o jogador venceu ou perdeu a rodada.

Se o jogador venceu a rodada, o código adiciona 1 ao contador de vitórias (vitoria). 
Se o jogador perdeu a rodada, o código exibe o número total de vitórias do jogador 
e sai do loop while.


                              CODIGO GUANABARA
                              
                              
from random import randint

v = 0 
while True:
    jogador = int(input('Diga o valor: '))
    computador = randint(0,10)
    total = computador + jogador
    tipo = ' '

    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total {total}', end=' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu Impar!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!')
        else:
            print('Você Perdeu!')
            break
print(f'Você venceu {v} vezes')



O código começa importando a função randint do módulo random. 
Em seguida, ele inicializa uma variável chamada 'v' para acompanhar o 
número de vezes que o usuário venceu.

O loop while com a condição True continuará sendo executado até que o 
usuário perca o jogo. Dentro do loop, o usuário é solicitado a digitar 
um número, e o computador gera aleatoriamente outro número. Em seguida, 
o código verifica se o usuário escolheu par ou ímpar e exibe a soma dos 
números e se ela é par ou ímpar.

Se o usuário escolheu par e a soma dos números for par, o código exibe a 
mensagem "Você Venceu!" e adiciona 1 à variável 'v'. Caso contrário, o 
código exibe "Você Perdeu!" e interrompe o loop. O mesmo acontece se o 
usuário escolheu ímpar e a soma dos números for ímpar.

Fora do loop, o código exibe quantas vezes o usuário venceu o jogo
        
        
        '''










