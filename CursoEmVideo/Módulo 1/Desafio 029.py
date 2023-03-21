'''Escreva um programa que leia  a velocidade de um carro
se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
a multa vai custar R$7,00 por quilólemtro'''


v = float(input('Velocidade: '))

if v > 80:
    multa = (v-80)*7

    print('Multado! Valor a pagar R${:.2f}'.format(multa))
else:
    print('sem multas!')

