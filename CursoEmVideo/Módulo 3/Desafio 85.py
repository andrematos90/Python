'''
85 - Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares e impares.
No final, mostre os valores pares e impares em ordem crescente.'''
lista = []

for c in range (0, 7):
    numero = int(input('Número: '))
    if c == 0:
        lista.append(numero)
    elif c > 0 and c % 2 == 0:
            lista.insert(0, numero)
    else:
            lista.append(numero)


print(lista)