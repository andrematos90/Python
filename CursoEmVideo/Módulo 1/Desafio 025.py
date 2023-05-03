'''
crie um programa que leia o nome de uma pessoa e diga se tem silva
'''

nome = input('Digite seu nome: ')

print('Possui o nome Silva? {}' .format('SILVA' in nome.upper()))

#resolvido com o operador "in"

'''
outra forma 

nome = str(input('Nome: ')).lower().strip()

if 'silva' in nome:
    print('Tem "Silva" no nome!')
else:
    print('Não tem silva no nome!')
    
    
outra forma 

nome = str(input('Nome: ')).lower().strip()

print(f'Possui Silva no nome? {"silva" in nome}')'''