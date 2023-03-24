'''Elabore um programa que calcule o valor a ser pago por um prouto, 
considerando o seu preço normal  e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

preco = float(input('Valor do produto:'))
forma = int(input('Digite a forma de pagamento: \n 1 - A vista Dinheiro/Cheque\n 2 - A vista no Cartão\n 3 - 2X no Cartão\n 4 - 3x No cartão:\n'))



if forma == 1:
    print('Total a pagar: R${:.2f}'.format(abs((preco / 100 * 10) - preco)))

elif forma == 2:
    print('Total a pagar: R${:.2f}'.format(abs((preco / 100 *5) - preco)))

elif forma == 3:
    print('Total a pagar: R${:.2f}'.format(preco))

else:
    print('Total a pagar: R${:.2f}'.format(abs((preco / 100 + 20)  + preco)))


