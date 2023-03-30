'''Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três
e que se encontram no intervalo de 1 até 500'''

soma = 0
cont =  0

for n in range (1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
        cont = cont + 1
print('A soma entre todos os {} valores encontrados é: {}'.format(cont, soma))

