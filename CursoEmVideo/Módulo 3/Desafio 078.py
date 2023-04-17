'''
Crie um program aque leia 5 valores numéricos e guarde em uma lista
No final, mostre qual foi o maior e o menor valor digitado e as respectivas
posições na lista'''

num = list()

for c in range(0,5):
   num.append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Maior valor: {max(num)} na posição {num.index(max(num))}')
print(f'Menor valor: {min(num)} na posição {num.index(min(num))}')

'''
num = list(): cria uma lista vazia chamada "num".

for c in range(0,5):: inicia um loop "for" que se repete 5 vezes, 
variando o valor da variável "c" de 0 a 4.

num.append(int(input(f'Digite um valor para a posição {c}: '))): dentro do loop, 
solicita ao usuário que digite um valor, converte o valor para um número inteiro 
com "int" e adiciona o valor à lista "num".

print(f'Maior valor: {max(num)} na posição {num.index(max(num))}'): após o loop, 
exibe o maior valor da lista usando a função "max" e a posição do maior valor na
lista usando o método "index".

print(f'Menor valor: {min(num)} na posição {num.index(min(num))}'): em seguida, 
exibe o menor valor da lista usando a função "min" e a posição do menor valor na 
lista usando o método "index".

Resumindo, este código cria uma lista "num" de comprimento 5, pede ao usuário que 
digite um valor para cada posição da lista e, em seguida, encontra e exibe o maior
e o menor valor da lista e suas posições correspondentes.'''

   

