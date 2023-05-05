'''Desenvola um programa que leia 6 números inteiros 
e mostre a soma apenas daqueles que forem par'''

soma = 0

for c in range(0, 6):
    numero = int(input('Numero: '))
    if numero % 2 == 0:
        soma = numero + soma
print(soma)
    