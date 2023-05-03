'''Faça um programa que leia três numeros  e mostre qual é o maior e qual é o menor'''
maior = menor = 0
numero = []

for n in range(0,3):
    numero.append(int(input(f'Digite o {n +1}º número: ')))
numero.sort()
print(f'Menor número: {numero[0]}')
print(f'Maior número: {numero[-1]}')