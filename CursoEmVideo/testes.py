'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode excerder 30% do salário ou então o empréstimo será negado.'''

valor_casa = float(input('Valor da casa R$: '))
salario = float(input('Sálario R$: '))
margem = (salario * 30) / 100
ano = int(input('Anos de pagamneto: '))
parcela = valor_casa / (ano * 12)
if parcela <= margem:
    print(f'Valor da parcela: {parcela:.3f}, empréstimo concedido!')
else:
    print(f'O valor da parcela excede 30% de seu salário, empréstimo negado!')


