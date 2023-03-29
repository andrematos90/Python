'''Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três
e que se encontram no intervalo de 1 até 500'''

for n in range (0, 501, 3):
    for n in range (0, 501, n+n):
        if n % 2 == 0:
            print(n)
