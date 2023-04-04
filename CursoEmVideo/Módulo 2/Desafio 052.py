'''Faça um programa que leia um número inteiro e diga se ele é primo ou não'''

n = int(input('Digite um número: '))
tot = 0

for c in range (1, n+1):
    if n % c == 0:
       print('\033[33m', end=' ')
       tot += 1 # é o mesmo que tot = tot + 1
    else:
        print('\033[34m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m O número {} foi divísivel por {} vezes'.format(n, tot))
if tot == 2:
    print('primo')
else:
    print('não é primo')