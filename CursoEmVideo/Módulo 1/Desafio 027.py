'''
Faça um programa que um nome e mostre o primeiro e o ultimo:
'''

nome = input('Digite seu nome:').split()

print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[len(nome)-1]))