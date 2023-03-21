
'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "santo"
'''

cidade = input('Cidade: ').stript()

existe = 'Santo' in cidade[0:5]

print('Existe a palavra "Santo": {}'.format(existe))


                                     #OUTRA FORMA DE FAZER



cidade = str(input('Cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')

