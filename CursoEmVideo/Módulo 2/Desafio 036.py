'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não pode excerder 30% do salário ou então o empréstimo será negado.
'''

casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anos = int(input('Anos de Financiamento: '))

prestacao = casa / (anos*12)
psalario = salario * 30 /100

if prestacao >= psalario:
     print(prestacao)
     print('Negado')
   
else:
    print('Empréstmo concedido!, Valor das Prestações: R$\033[32;40m{:.2f}'.format(prestacao))