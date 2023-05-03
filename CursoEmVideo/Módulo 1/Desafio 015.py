#escreva um programa que pergunte a quantidade de km percorrido por um carro alugado
#e a quantidade de dias pelos quais foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

d = int(input('Dias: '))
km = float(input('Quilômetros: '))

print('Total a pagar: R${:.2f}'.format(d*60 + km *0.15))

'''
outra forma 

km = float(input('quilómetros: '))
dias = int(input('Quantidade de dias: '))
preco = (dias * 60) + (km * 0.15)
print(f'Total a pagar R$ {preco:.2f}')'''