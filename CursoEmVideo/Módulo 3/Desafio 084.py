'''Faça um programa que leia o nome e peso de várias pessoas,
guardando tudo em uma lista, No final, mostre:

A - Quantas pessoas foram cadastradas.
B - Uma listagem das pessoas mais pesadas.
C - Uma listagem com as pessoas mais leves.'''

pessoas = []
while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    pessoas.append((nome, peso))
    resp = input('Deseja continuar? [S/N]: ')
    if resp in 'nN':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')

# Ordenando as pessoas por peso
pessoas.sort(key=lambda pessoa: pessoa[1])

# Imprimindo as pessoas mais leves
print('Pessoas mais leves:')
for pessoa in pessoas:
    if pessoa[1] == pessoas[0][1]:
        print(f'{pessoa[0]} ({pessoa[1]:.2f} kg)')

# Imprimindo as pessoas mais pesadas
print('Pessoas mais pesadas:')
for pessoa in reversed(pessoas):
    if pessoa[1] == pessoas[-1][1]:
        print(f'{pessoa[0]} ({pessoa[1]:.2f} kg)')

'''
pessoas = []: Cria uma lista vazia chamada "pessoas" que irá armazenar tuplas com o nome e o peso de cada pessoa.
while True:: Inicia um loop infinito.
nome = input('Nome: '): Solicita ao usuário que digite o nome da pessoa e
armazena na variável "nome".
peso = float(input('Peso: ')): Solicita ao usuário que digite o peso da pessoa
e armazena na variável "peso" como um número de ponto flutuante.
pessoas.append((nome, peso)): Adiciona uma tupla contendo o nome e o peso da pessoa à 
lista "pessoas".
resp = input('Deseja continuar? [S/N]: '): Pergunta ao usuário se deseja continuar
adicionando pessoas à lista.
if resp in 'nN':: Verifica se a resposta é "n" ou "N" (para sair do loop).
break: Sai do loop caso a resposta seja "n" ou "N".
print(f'Foram cadastradas {len(pessoas)} pessoas.'): Imprime a quantidade de pessoas 
cadastradas na lista "pessoas".
pessoas.sort(key=lambda pessoa: pessoa[1]): Ordena a lista "pessoas" com base no 
segundo elemento de cada tupla, que é o peso.
print('Pessoas mais leves:'): Imprime uma mensagem indicando que a lista de pessoas
mais leves será exibida.
for pessoa in pessoas:: Inicia um loop que percorre cada tupla na lista "pessoas".
if pessoa[1] == pessoas[0][1]:: Verifica se o peso da pessoa atual é igual ao peso 
da primeira pessoa na lista (ou seja, é a pessoa mais leve).
print(f'{pessoa[0]} ({pessoa[1]:.2f} kg)'): Imprime o nome e o peso da pessoa mais
leve com duas casas decimais.
print('Pessoas mais pesadas:'): Imprime uma mensagem indicando que a lista de pessoas
mais pesadas será exibida.
for pessoa in reversed(pessoas):: Inicia um loop que percorre cada tupla na lista 
"pessoas" de trás para frente.
if pessoa[1] == pessoas[-1][1]:: Verifica se o peso da pessoa atual é igual ao peso 
da última pessoa na lista (ou seja, é a pessoa mais pesada).
print(f'{pessoa[0]} ({pessoa[1]:.2f} kg)'): Imprime o nome e o peso da pessoa mais 
pesada com duas casas decimais.'''

