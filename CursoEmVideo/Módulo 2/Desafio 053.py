'''Crie um programa que leia uma frase e diga se ela ela é um palíndromo, desconsiderando os espaços'''

frase = str(input('Digite uma frase: ')).replace(' ','')

fraseinvertida = frase[:: -1]

if fraseinvertida == frase:
    print('A frase "{}" é um palindromo'.format(fraseinvertida))
else:
    print('A frase "{}" não é um palindromo'.format(fraseinvertida))

'''
outra forma 

frase = str(input('Frase: ')).lower().strip()
inverso = frase[::-1]

if frase == inverso:
    print('Palíndromo')
else:
    print('Não é palindromo')


'''


