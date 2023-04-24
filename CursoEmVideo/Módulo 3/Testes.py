'''
78 - Crie um programa que leia 5 valores numéricos e guarde em uma lista
No final, mostre qual foi o maior e o menor valor digitado e as respectivas
posições na lista'''

numeros  = []
maior = menor = 0

for c in range(0, 5):
    numeros.append(int(input(f'Digite o numero para a posição {c}: ')))
    if c == 0: 
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]

print(f'Lista: {numeros}')

for i, v in enumerate(numeros):
    if v == maior:
        print()
     
print(f'na posição {i} temos {maior} como maior')

for i, v in enumerate(numeros):
    if v == menor:
        print()

print(f'na posição {i} temos { menor} como menor')

