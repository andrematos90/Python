'''
Crie um programa que leia o nome completo e mostre

*o nome com todas as letras maiusculas
*todas minusculas
*quantas letras sem considerar espaços
*quantas letras tem o primeiro nome
'''

nome = input('Digite seu nome completo: ')
maiscula = nome.upper()
minusculo = nome.lower()
junto = nome.replace(' ','' )
firstname = nome[0:5]



print('Nome em maiúsculo: {}'.format(maiscula))
print('Nome em minúsculo: {}'.format(minusculo))
print('Quantidade de letras: {}'.format(len(junto)))
print('Quantidade de letras do primeiro nome: {}'.format(len(firstname)))


'''

                                        #OUTRA FORMA DE FAZER



nome =  str(input('Nome: ')).strip()    #strip()   retira os espaços do inicio e do fim

print('nome em máiusculo: {}'.format(nome.upper()))
print('nome em minúsculo: {}'.format(nome.lower()))
print('quantidade de letras: {}'.format(len(nome) - nome.count(' ')))   #len conta os caracteres de nome e count conta a quantidade de letras
print('letras no primeiro nome: {}'.format(nome.find(' ')))             #find encontra o primeiro espaço        





outra forma de fazer 

# Solicita ao usuário o nome completo e remove quaisquer espaços extras no início e no final da string
nome = input('Nome Completo: ').strip()

# Remove quaisquer espaços extras entre as palavras do nome e conta o número de letras sem espaços em branco
quantidade_letras = len(nome.replace(' ', ''))
primeiro_nome = nome.split()[0]

# Imprime o nome em maiúsculas e minúsculas, juntamente com o número de letras sem espaços em branco
print(f'Nome em maiúsculas: {nome.upper()}')
print(f'Nome em minúsculas: {nome.lower()}')
print(f'Total de letras sem espaços: {quantidade_letras}')
print(f'Quantidade de letras do primeiro nome: {len(primeiro_nome)}')'''