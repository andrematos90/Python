'''
100 - Faça um programa que tenha uma lista  chamada numeros e duas funções chamadas sorteio() e somarPar()A primeira função vai sortear 5 números e vai colocálos dentro de uma lista e a segunda função vai mostrar a soma entre todos valores pares sorteados pela função anterior'''


from random import randint

def sorteio(lista):
   for cont in range(0, 5):
        lista.append(randint(0,60))
   print(f'Números sorteados: {numeros}')

def somarPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f'soma dos numeros pares: {soma}')

#programa principal
numeros = list()
sorteio(numeros)
somarPar(numeros)



'''
from random import randint: Importa a função randint do módulo random, que será usada para gerar números aleatórios.

def sorteio(lista): Define a função sorteio com um parâmetro lista, que receberá os números sorteados.

for cont in range(0, 5):: Inicia um loop que será executado 5 vezes.

lista.append(randint(0, 60)): Gera um número aleatório entre 0 e 60 usando a função randint e adiciona esse número à lista.

print(f'Números sorteados: {numeros}'): Imprime a lista de números sorteados.

def somarPar(numeros): Define a função somarPar com um parâmetro numeros, que receberá a lista de números sorteados.

soma = 0: Inicializa a variável soma com valor zero. Essa variável será usada para armazenar a soma dos números pares.

for c in numeros:: Inicia um loop que percorre cada número na lista numeros.

if c % 2 == 0:: Verifica se o número é par, ou seja, se o resto da divisão por 2 é igual a zero.

soma = soma + c: Se o número for par, adiciona-o à variável soma.

print(f'soma dos numeros pares: {soma}'): Imprime a soma dos números pares.

numeros = list(): Cria uma lista vazia chamada numeros.

sorteio(numeros): Chama a função sorteio passando a lista numeros como argumento para preenchê-la com os números sorteados.

somarPar(numeros): Chama a função somarPar passando a lista numeros como argumento para somar os números pares.'''



