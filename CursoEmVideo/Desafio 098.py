'''
98- Faça um programa que tenha uma função chamada contador(),
que receba três parametros: inicio, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada.

A - De 1 até 10, de um em um
B - De 10 até 0, de 2 em 2
C - Uma contagem personalizada.
'''

def contador(inicio, fim, passo):
    #A - De 1 até 10, de um em um
    for c in range(inicio, fim + 1, passo):
        print(c )

inicio = int(input('Inicia em: '))
fim = int(input('Termina em: '))
passo = int(input('pula de: '))

contador(inicio, fim, passo)