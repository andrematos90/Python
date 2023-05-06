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
print('\n\033[m O número {} foi divísivel  {} vezes'.format(n, tot))
if tot == 2:
    print('primo')
else:
    print('não é primo')


'''
outra forma 
numero = int(input('Número: '))
divisores = 0

for c in range(1, numero + 1):
    if numero % c == 0: # Verifica se c é um divisor de número
        divisores += 1
        if divisores > 2: # Se já encontrou mais de 2 divisores, o número não é primo
            print('Não é primo')
            break

if divisores == 2: # Se encontrou exatamente 2 divisores, o número é primo
    print(f'O número {numero} é primo')
'''