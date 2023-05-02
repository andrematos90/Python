'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
possiveis sobre ele.'''

digitado = str(input('Digite algo: '))

print(f'O que foi digitado é do tipo de dado:  {type(digitado)}') # solicitada que o usuário digite algo
print(f'só tem espaços? {digitado.isspace()}') # informa se o que foi inserido são apenas espaços
print(f'É um número? {digitado.isnumeric()}') # informa se é um número
print(f'É alfabético? {digitado.isalpha()}') # informa se são letras
print(f'É alfanumérico? {digitado.isalnum()}') # informa se são números
print(f'Está em maisúculo? {digitado.isupper()}') # informa se só tem  letras maiúsculas
print(f'Está em minúsculo {digitado.islower()}') # inforam se só tem letras minúsculas
print(f'Está capitalzada? {digitado.istitle()}') # informa se tem letras maiúsculas e minúsculas