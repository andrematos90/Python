'''Refaça o exercicio 051, lendo o primeiro de uma PA e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

'''Programa que leia o primeiro termo e a razão de uma Progressão aritimética.
No final mostre os 10 primeiros termos dessa progressão'''

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termo = primeiro_termo
cont = 1

while cont <= 10:
    termo = termo + razao
    cont = cont + 1
    print('{} '.format((termo)))
    


