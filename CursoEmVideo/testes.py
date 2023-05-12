'''
Crie um programa que leia vários números inteiros. No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valor lido. O programa deve perguntar ao usúario se ele quer ou não continuar
a digitar valores
'''

cont = media = maior = menor = soma = 0
primeiro = True
while True:
    numero = int(input('Numero: '))
    resposta = str(input('Continuar? S/N ')).upper().strip()
    soma = soma + numero
    cont += 1

    if primeiro:
       maior = menor = numero
       primeiro = False
    else: 
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    if resposta in 'Nn':
        break

print(f'Média: {soma / cont}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')

