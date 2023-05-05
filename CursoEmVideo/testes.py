'''Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três
e que se encontram no intervalo de 1 até 500'''
soma = 0
tot = 0

for c in range(0, 501):
    if c % 2 != 0 and  c % 3 == 0:
        soma = soma + c
        tot += 1
print(f'A soma entre os {tot} valores é : {soma}')

