'''crie um programa que leia um nunmero e diga se é impar ou par'''

numero = int(input('Digite um número: '))

if numero %2 == 0:
    print('par')
else:
    print('impar')

'''
outra forma 

numero = int(input('Digite o número: '))
if numero %2 == 0:
    print(f'Numero {numero} é par!')
else:
    print(f'Número {numero} é impar!')'''