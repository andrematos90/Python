'''Escreva um programa que leia um numero inteiro e peça para qual base sera convertido
*1 -binário
*2 -octal
*3 -hexadecimal
'''

numero = int(input('Numero: '))
base = str(input('Qual a base de conversão Binario/Octal ou Hexadecimal? ')).lower().strip()

if 'binario' in base:
    print(f'Binário: {bin(numero)}')
elif 'octal' in base:
    print(f'Octal: {oct(numero)}')
elif 'hexadecimal' in base:
    print(f'Hexadecimal: {hex(numero)}')