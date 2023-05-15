'''
Crie um programa que tenha uma tupla totalmente preenchida com uma 
contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso'''

numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('número: '))
    print(numero[n])
    resposta = str(input('Continuar? S/N')).upper().strip()
    if resposta in 'N':
        break
    