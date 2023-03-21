
'''Faça um programa que leia um ano qualquer e mostre se é bissexto'''

ano = int(input('Digite o Ano: '))

if ano % 4 ==0 and ano % 100 !=0 or ano % 400 == 0:
    print('ano bissexto')
else:
    print ('ano não bissexto')
