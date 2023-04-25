'''
82 - Crie um programa que leia varios números e coloque-os em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores
pares e os valores impares digitados, respectivamente. Ao final, mostre o 
conteúdo das três listas geradas.'''



numeros = pares = impares = []

while True:
    numeros.append(int(input('Número: ')))
    for c in numeros:
        if c % 2 == 0:
            pares.append(c)
        else:
            impares.append(c)

    res = str(input(input('Continuar: [S/N]')))
    if res in 'Nn':
        break
print(f'Lista: {numeros}')
print(f'Impares: {impares}')
print(f'Pares: {pares}')
