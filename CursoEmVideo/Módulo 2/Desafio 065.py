'''
Crie um programa que leia vários números inteiros. No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valor lido. O programa deve perguntar ao usúario se ele quer ou não continuar
a digitar valores
'''

num = int(input("Digite o primeiro termo da PA: "))
cont = 1
mais = 10
total = 1
resposta = 'S'

while resposta != 'N':  
    total = total + mais
    while cont <= total:
        print('{} '.format((termo)))
        termo += razao
        cont += 1
    print('Pausa')
    resposta = int(input('Quer continuar? '))
print('fim')

