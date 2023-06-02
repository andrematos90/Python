'''
99 - Faça um programa que tenha uma função chamada maior(), que receba
vários parâmetros com valores innteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior'''

def maior(*num):
    print(num)

numeros = ()
while True:
    numero = input("Digite um número (ou 's' para parar): ")
    if numero.lower() == 's':
        break
    numeros += (float(numero),)

print(numeros)
