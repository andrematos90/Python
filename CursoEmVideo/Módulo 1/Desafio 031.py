

'''Desenvolva um programa que pergunte a distâñcia de uma viagem em km.
Calcule o preço da passagem cobrando R$0,50 por quilometro para viagens de até 200km
e R$ 0,45 para viagens mais longas'''

dist = float(input('Quantos km tera a viagem? '))

if dist <= 200:
    print('Valor á pagar: R${:.2f}'.format(0.50 * dist))

else:
    print('Valor á pagar: R${:.2f}'.format(0.45*dist))


'''
outra forma 

distancia = int(input('Quilometros: '))

if distancia <= 200:
    print(f'Valor da viagem: R${distancia * 0.50:.2f}')
else:
    print(f'Valor da viagem: R${distancia * 0.45:.2f}')'''