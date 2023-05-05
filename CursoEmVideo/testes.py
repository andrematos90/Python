'''Programa que leia o primeiro termo e a razão de uma Progressão aritimética.
No final mostre os 10 primeiros termos dessa progressão'''

primeiro_termo = int(input('Primeiro termo da progressão: '))
razao = int(input('Razão da progressão: '))

for c in range(primeiro_termo, primeiro_termo + 10, razao):
    print(c)