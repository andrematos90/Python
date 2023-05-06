'''Faça um programa que leia o peso de cinco pessoas 
e mostre qual é o maior e menor peso.'''

cont = 0


maior = 0
menor = 0



for pessoa in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('o maior peso é {}kg da pessoa {}'.format(maior, pessoa))
print('o menor peso é {}kg'.format(menor))


'''
outra forma 

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
'''