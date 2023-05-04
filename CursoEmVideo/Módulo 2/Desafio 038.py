'''Escreva um programa que leia dois numneros inteiros e compare-os,
mostrando uma mensagem na tela:

- o primeiro é o maior
- o segundo é o maior
- não existe valor maior os dois são iguais'''

n1 = int(input('digite um número: '))
n2 = int(input('digite o segundo número: '))

if n1 > n2:
    print('O primeiro numero {} é maior que segundo {}'.format(n1,n2))
elif n2 > n1:
    print('O Segundo número {} é maior que o primeiro {}'.format(n2,n1))
elif n1 == n2:
    print('Os números digitados {} e {} são iguais!'.format(n1,n2))

'''
outra forma


n1 = int(input('primeiro número: '))
n2 = int(input('segundo número: '))

if n1 > n2:
    print('O primeiro valor é o maior!')
elif n2 > n1:
    print('O segundo número é o maior!')
else:
    print('Os numeros são  iguais!')'''