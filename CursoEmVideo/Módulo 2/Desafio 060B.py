'''Faça um programa que leia um número inteiro e mostre seu fatorial

Ex: 5*4*3*2*1 = 120'''

from time import sleep

n = int(input('Digite um número para visualizar seu fatorial: '))
c = n
f = 1

print('Caluculando fatorial de {}!'.format(n))
sleep(2)

while c > 0:
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else '= ', end='')
    f = f * c
    c = c - 1
print(f)