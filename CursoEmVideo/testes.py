'''Elabore um programa que calcule o valor a ser pago por um prouto, 
considerando o seu preço normal  e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

preco = float(input('Valor do produto: '))
desconto = 0
forma = int(input('''Digite o numero da opção de pagamento: 

1 - A vista 
2 - A vista no Cartão 
3-  2X no cartao 
4 - 3x ou mais no cartão \n'''))


if forma == 1:
    print(f'Valor do produto: R${ preco - (preco / 100 * 10):.2f}')
elif forma == 2:
    print(f'Valor do produto: R${preco - (preco /100 * 5):.2f}')
elif forma == 3:
    print(f'Valor do produto: R${preco}')
elif forma == 4:
    (print(f'valor do produto: R${preco + (preco / 100 * 20):.2f}'))
else:
    (print('Opção inválida!'))





