'''Crie um programa que leia uma frase e diga se ela ela é um palíndromo, desconsiderando os espaços'''



frase = str(input('Frase: ')).lower().strip()
inverso = frase[::-1]

if frase == inverso:
    print('Palíndromo')
else:
    print('Não é palindromo')



