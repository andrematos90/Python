'''
Crie um programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
opcao = 0

while opcao >= 0 and opcao < 4:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o primeiro número: '))
    opcao = int(input('''
     Digite o número da opcão desejada
     [1] Somar
     [2] Multiplicar
     [3] Maior
     [4] Novos números
     [5] Sair do programa
     
     Qual a opção Escolhida: 
     '''))
    
    if opcao == 1:
        print('A soma é {}'.format(num1 + num2))
    elif opcao == 2:
        print('A multiplicação é {}'.format(num1 * num1))
    elif opcao == 3:
        if num1 > num2:
            print('O maior número é {}'.format(num1))
        else:
            print('O maior número é o {}'.format(num2))
    elif opcao == 4:
        del num1, num2
        opcao == 0




