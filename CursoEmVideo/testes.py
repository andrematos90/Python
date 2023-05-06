'''Faça um programa que leia o peso de cinco pessoas 
e mostre qual é o maior e menor peso.'''

maior = float('-inf')
menor = float('inf')

for c in range(0, 5):
    peso = float(input('Peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'Maior: {maior}')
print(f'Menor: {menor}')
