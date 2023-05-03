'''
Faça um programa que um nome e mostre o primeiro e o ultimo:
'''

nome = input('Digite seu nome:').split()

print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[len(nome)-1]))

'''
outra forma 

nome = str(input('Nome: ')).lower().strip()
nome_lista = nome.split()
print(f'Primeiro nome: {nome_lista[0]}')
print(f'Último nome: {nome_lista[-1]}')
'''