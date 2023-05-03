# Faça um programa que um nome e mostre o primeiro e o ultimo:

nome = str(input('Nome: ')).lower().strip()
nome_lista = nome.split()
print(f'Primeiro nome: {nome_lista[0]}')
print(f'Último nome: {nome_lista[-1]}')
