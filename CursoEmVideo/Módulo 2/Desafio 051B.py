'''Programa que leia o primeiro termo e a razão de uma Progressão aritimética.
No final mostre os 10 primeiros termos dessa progressão'''

N = int(input('Digite o primeiro termo da P.A: '))
R = int(input('Digite a razão da P.A: '))
D = N + (10 - 1) * R

for c in range(N, D + R, R):
    print('{}'.format(c), end=' > ')
print('Fim')