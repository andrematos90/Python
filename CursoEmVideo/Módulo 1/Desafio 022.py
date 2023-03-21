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



                                        #OUTRA FORMA DE FAZER



nome =  str(input('Nome: ')).strip()    #strip()   retira os espaços do inicio e do fim

print('nome em máiusculo: {}'.format(nome.upper()))
print('nome em minúsculo: {}'.format(nome.lower()))
print('quantidade de letras: {}'.format(len(nome) - nome.count(' ')))   #len conta os caracteres de nome e count conta a quantidade de letras
print('letras no primeiro nome: {}'.format(nome.find(' ')))             #find encontra o primeiro espaço                                 