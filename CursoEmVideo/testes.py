'''
 crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário quer continuar.
 No final mostre:
 A - Quanto é o total gasto na compra.
 B - Quantos produtos custam mais de R$1000.
 C - Qual é o nome do produto mais barato.
'''
total_gasto = mais_de_mil = 0
mais_barato = 0
produto_mais_barato = ''
mais_barato = float('inf')
while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço: '))
    continuar = str(input('Continuar S/N: ')).upper().strip()
    total_gasto += preco
    if preco >= 1000:
        mais_de_mil += 1
    if preco < mais_barato:
        mais_barato = preco
        produto_mais_barato = produto
    if continuar in 'N':
        break
print(f'Total: R${total_gasto:.2f}')
print(f'Quantidade de produtos com valor maior que R$1000: {mais_de_mil}')
print(f'Produto mais barato: {produto_mais_barato}')