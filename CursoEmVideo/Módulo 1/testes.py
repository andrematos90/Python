'''
crie um programa que leia o nome de uma pessoa e diga se tem silva
'''

nome = str(input('Nome: ')).lower().strip()

print(f'Possui Silva no nome? {"silva" in nome}')