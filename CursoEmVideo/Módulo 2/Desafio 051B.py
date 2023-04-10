'''Programa que leia o primeiro termo e a razão de uma Progressão aritimética.
No final mostre os 10 primeiros termos dessa progressão'''

N = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
decimo = N + (10 - 1) * razao

for c in range(N, decimo + razao, razao):
    print('{}'.format(c), end=' > ')
print('Fim')