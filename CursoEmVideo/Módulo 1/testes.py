'''Desenvolva um programa que leia o comprimento de três
retas e diga ao usuário se elas podem ou não formar um triângulo'''

lado_1 = int(input('Digite o tamanho do primeiro lado: '))
lado_2 = int(input('Digite o tamanho do segundo lado: '))
lado_3 = int(input('Digite o  tamanho do terceiro lado: '))

if lado_1 + lado_2 > lado_3:
    print('é possivel formar um triangulo')
elif lado_1 + lado_3 > lado_2:
    print('é possivel formar um triangulo')
elif lado_2 + lado_3 > lado_1:
    print('é possivel formar um triangulo')
else:
    print('Não é possivel formar um triangulo')
