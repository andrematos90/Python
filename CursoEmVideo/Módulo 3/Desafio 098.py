'''
98- Faça um programa que tenha uma função chamada contador(),
que receba três parametros: inicio, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada.

A - De 1 até 10, de um em um
B - De 10 até 0, de 2 em 2
C - Uma contagem personalizada.
'''
from time import sleep

def contador(*num):
     print('A - De 1 até 10, de um em um:')
     for c in range(1, 10 + 1, 1):
        print(f'{c}', end=' ' )
     sleep(1)
     print('FIM!')
     print('-' * 30 )
     print('B - De 10 até 0, de 2 em 2:')
     for c in range(10, 0, -2):
        print(f'{c}', end=' ' )
     sleep(1)
     print('FIM!')
     print('-' * 30 )
     print('C - Uma contagem personalizada:')
     inicio = int(input('Inicia em: '))
     fim = int(input('Termina em: '))
     passo = int(input('pula de: '))
     if passo == 0:
        passo = 1
     if inicio > fim:
        for c in range(inicio, fim - 1 , passo * (-1)):
           print(f'{c}', end=' ' )
     elif inicio < fim:
         for c in range(inicio, fim + 1, passo):
           print(f'{c}', end=' ' )
           sleep(1)
     elif passo < 0:
         for c in range(inicio, fim - 1, passo):
            print(f'{c}', end=' ' )
     sleep(1)
     print('FIM!')
     print('-' * 30 )
contador()