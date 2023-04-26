'''Faça um programa que leia o nome e peso de várias pessoas,
guardando tudo em uma lista, No final, mostre:

A - Quantas pessoas foram cadastradas.
B - Uma listagem das pessoas mais pesadas.
C - Uma listagem com as pessoas mais leves.'''

pesadas = []
leves = []

while True:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    if peso >= 70:
      pesadas.append(nome)
      pesadas.append(peso)
    elif peso <= 70:
       leves.append(nome)
       leves.append(peso)
    resposta = str(input('Continuar? [S/N]'))
    if resposta in 'Nn':
        break
print(f'Total de pessoas cadastradas: {len(pesadas) + len(leves) / 2}')
print(f'Pessoas mais pesadas: {pesadas}')
print(f'Pessoas mais leves: {leves}')
'''
pesadas = []: cria uma lista vazia para armazenar os nomes e pesos das pessoas pesadas.
leves = []: cria uma lista vazia para armazenar os nomes e pesos das pessoas leves.
while True:: inicia um loop infinito, que só será interrompido pelo comando break.
nome = str(input('Nome: ')): solicita o nome da pessoa ao usuário e armazena na variável nome.
peso = int(input('Peso: ')): solicita o peso da pessoa ao usuário e armazena na variável peso.
if peso >= 70:: verifica se o peso é maior ou igual a 70.
pesadas.append(nome): se o peso for maior ou igual a 70, adiciona o nome da pessoa à lista de pesadas.
pesadas.append(peso): se o peso for maior ou igual a 70, adiciona o peso da pessoa à lista de pesadas.
elif peso <= 70:: verifica se o peso é menor ou igual a 70.
leves.append(nome): se o peso for menor ou igual a 70, adiciona o nome da pessoa à lista de leves.
leves.append(peso): se o peso for menor ou igual a 70, adiciona o peso da pessoa à lista de leves.
resposta = str(input('Continuar? [S/N]')): pergunta ao usuário se deseja continuar adicionando pessoas à lista.
if resposta in 'Nn':: se a resposta for 'n' ou 'N', o loop será interrompido.
break: comando que interrompe o loop.
print(f'Total de pessoas cadastradas: {len(pesadas) + len(leves) / 2}'): exibe o total de pessoas cadastradas, que é a soma das pessoas pesadas e leves, dividido por 2.
print(f'Pessoas mais pesadas: {pesadas}'): exibe a lista de pessoas pesadas.
print(f'Pessoas mais leves: {leves}'): exibe a lista de pessoas leves.'''

'''
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
pesada com duas casas decimais.



                                 CÓDIGO GUANABARA


princ = []
temp = []
pesada = leve = 0

while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso: ')))
    if len(princ) == 0:
        pesada = leve = temp[1]
    else:
        if temp[1] > pesada:
            pesada = temp[1]
        if temp[1] < leve:
            leve = temp[1]

    princ.append(temp[:])
    temp.clear()


    resposta = str(input('Continuar? [S/N]'))
    if resposta in 'nN':
        break
for p in princ:
    if p[1] == pesada:
        print(f'{p[0]} é o(a) mais pesado(a) com {pesada}Kg')

for p in princ:
    if p[1] == leve:
        print(f'{p[0]} é o(a) mais leve com {leve};kg')

print(f'Total de pessoas cadastradas: {len(princ)}')


princ = []

Cria uma lista vazia chamada "princ", que será usada para armazenar todas as pessoas cadastradas.

temp = []

Cria outra lista vazia chamada "temp", que será usada temporariamente para armazenar o nome e o peso de cada pessoa.

pesada = leve = 0

Inicializa as variáveis "pesada" e "leve" com o valor 0. Essas variáveis serão usadas para determinar a pessoa mais pesada e a pessoa mais leve, respectivamente.

while True:

Inicia um loop infinito usando a palavra-chave "while" seguida da constante "True". Isso significa que o loop será executado repetidamente até que seja interrompido por alguma condição.

temp.append(str(input('Digite o nome: ')))

Solicita o nome de uma pessoa usando a função "input" do Python e armazena o valor digitado na lista "temp", convertendo-o em uma string usando a função "str" do Python. O método "append" adiciona o valor digitado ao final da lista "temp".

temp.append(float(input('Digite o peso: ')))

Solicita o peso da mesma pessoa usando a função "input" do Python e armazena o valor digitado na lista "temp", convertendo-o em um número decimal (float) usando a função "float" do Python.

if len(princ) == 0:

Verifica se a lista "princ" está vazia. Se estiver vazia, significa que esta é a primeira pessoa sendo cadastrada, e portanto seu peso deve ser definido como o valor inicial de "pesada" e "leve".

pesada = leve = temp[1]

Define o valor de "pesada" e "leve" como o peso da primeira pessoa cadastrada (o segundo elemento da lista "temp", que contém o peso).

else:

Se a lista "princ" não estiver vazia, significa que já há pelo menos uma pessoa cadastrada, e portanto é necessário comparar o peso da pessoa atual com os valores de "pesada" e "leve".

if temp[1] > pesada:

Verifica se o peso da pessoa atual (o segundo elemento da lista "temp") é maior que o valor de "pesada". Se for, atualiza o valor de "pesada" com o peso da pessoa atual.

if temp[1] < leve:
Verifica se o peso da pessoa atual é menor que o valor de "leve". Se for, atualiza o valor de "leve" com o peso da pessoa atual.

princ.append(temp[:])
Adiciona a lista "temp" à lista "princ" usando o método "append". É importante usar a sintaxe "temp[:]" em vez de simplesmente "temp", para que seja criada uma cópia da lista "temp" e adicionada à lista "princ", em vez de adicionar uma referência para a mesma lista.

temp.clear()
Limpa a lista "temp" usando o método "clear", para que possa ser reutil'''



