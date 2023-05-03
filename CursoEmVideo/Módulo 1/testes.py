
'''22 - Crie um programa que leia o nome completo e mostre

*o nome com todas as letras maiusculas
*todas minusculas
*quantas letras sem considerar espaços
*quantas letras tem o primeiro nome
'''

nome = str(input('Nome Completo: '))

print(f'{nome.upper()}')
print(f'{nome.lower()}')
print(f'{len(nome.split())} letras')
