'''Faça um programa que leia um número inteiro e diga se ele é primo ou não'''

numero = int(input('Número: '))
divisores = 0

for c in range(1, numero + 1):
    if numero % c == 0: # Verifica se c é um divisor de número
        divisores += 1
        if divisores > 2: # Se já encontrou mais de 2 divisores, o número não é primo
            print('Não é primo')
            break

if divisores == 2: # Se encontrou exatamente 2 divisores, o número é primo
    print(f'O número {numero} é primo')
