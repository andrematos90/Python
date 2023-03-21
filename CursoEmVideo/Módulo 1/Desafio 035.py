'''Desenvolva um programa que leia o comprimento de três
retas e diga ao usuário se elas podem ou não formar um triângulo'''

n1 = float(input('Digite um número: '))

n2 = float(input('Digite um número: '))

n3 =float(input('Digite um número: '))

if n1 + n2 > n3:
    print('Pode formar um triÂngulo')
else:
    print('Não forma')