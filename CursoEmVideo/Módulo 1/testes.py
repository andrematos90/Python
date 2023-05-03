# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "santo"


cidade = str(input('Digite a cidade: ')).lower().split()

if 'santo' in cidade[0]:
    print('O nome da cidade começa com "Santo"!')
else:
    print('Não começa com "Santo!')


print(cidade[0:2])

