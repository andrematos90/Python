'''
 crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário quer continuar.
 No final mostre:
 A - Quanto é o total gasto na compra.
 B - Quantos produtos custam mais de R$1000.
 C - Qual é o nome do produto mais barato.
'''

Total = MaisdeMil = menorpreço= 0
MaisBarato = ''

while True:
    produto = str(input('Qual o produto: '))
    preço = float(input('Preço R$: '))
    resposta = str(input('Quer continuar S/N? ')).upper().strip()[0]
    Total = preço + Total
    menorpreço = preço

    if preço > 1000:
        MaisdeMil = MaisdeMil + 1

    if preço < menorpreço:
        MaisBarato = produto
        menorpreço = preço

    if resposta == 'N':
        break
print(f'Total da compra: R${Total:.2f}')
print(f'Produtos acima de R$1000: {MaisdeMil}')
print(f'Produto mais barato: {MaisBarato}')
