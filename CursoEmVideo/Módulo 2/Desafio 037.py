'''Escreva um programa que leia um numero inteiro e peça para qual base sera convertido
*1 -binário
*2 -octal
*3 -hexadecimal
'''

numero = int(input('Digite um número inteiro: '))
print('Qual será a base de conversão? \n Digite:\n 1 - Binario\n 2 - Octal\n 3 - Hexadecimal')
conversao = int(input('Base de conversão: '))

binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

if conversao == 1:
    print('O número {} convertido nada base binária é: {}'.format(numero, binario))
elif  conversao == 2:
     print('O número {} convertido em Octal é: {}'.format(numero, octal))

elif conversao == 3:
     print('O número {} convertido em Hexadecimal é: {}'.format(numero,hexadecimal))
    

