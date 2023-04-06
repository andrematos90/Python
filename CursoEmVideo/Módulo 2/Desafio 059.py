'''
Crie um programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.

'''
from time import sleep

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite o segundo número: '))
opcao = 0

while opcao != 5 :
    print(''' Digite o número da opcão desejada
     [1] Somar
     [2] Multiplicar
     [3] Maior
     [4] Novos números
     [5] Sair do programa
     
     Qual a opção Escolhida: ''')


    opcao = int(input('Digite o número da opção: '))

    if opcao == 1:
        sleep(2)
        print('A soma é {}'.format(num1 + num2))
    elif opcao == 2:
        print('A multiplicação é {}'.format(num1 * num1))
    elif opcao == 3:
        if num1 > num2:
            print('O maior número é {}'.format(num1))
        elif num2 > num1:
            print('O maior número é o {}'.format(num2))
        else:
            print('Os numeros são iguais!')
    elif opcao == 4:
        num1 = int(input('Digite o primeiro numero novamente: '))
        num2 = int(input('Digite o segundo número novamente: '))
    elif opcao == 5:
        print('FIM')
        break
    else:
        print('Opção inexistente!')
        sleep(2)

 




