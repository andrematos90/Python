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

 '''
 outra pergunta 
 
 from time import sleep
import os
while True:
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    print()
    print('Qual operaçãp deseja realizar: ')
    operacao = int(input('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa 
    ''' ))
    if operacao == 1:
        print(f'Soma de {n1} + {n2} = {n1 + n2}')
    elif operacao == 2:
        print(f'Multiplicação de {n1} x {n2} = {n1 * n2}')
    elif operacao == 3:
        maior = 0
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior valor entre {n1} e {n2} é {maior}')
    elif operacao == 4:
        continue
    elif operacao == 5:
        print('Saindo do programa...')
        print('Encerrando .')
        sleep(1)
        os.system('cls')
        print('Encerrando ..')
        sleep(1)
        os.system('cls')
        print('Encerrando ...')
        sleep(1)
        os.system('cls')
        print('Encerrando ..')
        sleep(1)
        os.system('cls')
        print('Encerrando .')
        sleep
        os.system('cls')
        print('Encerrando ..')
        sleep(1)
        os.system('cls')
        print('Encerrando ...')
        sleep(1)
        os.system('cls')
        print('Encerrando ..')
        sleep(1)
        os.system('cls')
        print('Encerrando .')
        sleep(1)
        os.system('cls')
        print('FIM')
        sleep(1)
        break
     '''




