
'''22 - Crie um programa que leia o nome completo e mostre

*o nome com todas as letras maiusculas
*todas minusculas
*quantas letras sem considerar espaços
*quantas letras tem o primeiro nome
'''

# Solicita ao usuário o nome completo e remove quaisquer espaços extras no início e no final da string
nome = input('Nome Completo: ').strip()

# Remove quaisquer espaços extras entre as palavras do nome e conta o número de letras sem espaços em branco
quantidade_letras = len(nome.replace(' ', ''))
primeiro_nome = nome.split()[0]

# Imprime o nome em maiúsculas e minúsculas, juntamente com o número de letras sem espaços em branco
print(f'Nome em maiúsculas: {nome.upper()}')
print(f'Nome em minúsculas: {nome.lower()}')
print(f'Total de letras sem espaços: {quantidade_letras}')
print(f'Quantidade de letras do primeiro nome: {len(primeiro_nome)}')

