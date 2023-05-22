'''Crie um programa que vai ler vários números  e colocar em uma lista.
Depois disso, mostre: 
A - Quantos números foram digitados.
B - A Lista de valores ordenada de forma decrescente.
C - Se o valor 5 foi digitado e está ná lista ou não.
'''


lista = []
cont = 0

while True:
    numero = int(input('número: '))
    lista.append(numero)
    cont += 1
    continuar = str(input('Continuar? (S/N) ')).upper().strip()
    if continuar in 'N':
        break
print(f'{cont} numeros digitados!')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print(f'O numero 5 está na lista! Na posição: {lista.index(5)}')
else:
    print('Numero 5 não foi digitado!')


