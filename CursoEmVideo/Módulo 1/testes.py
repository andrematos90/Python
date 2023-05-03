'''Escreva um programa que leia  a velocidade de um carro
se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
a multa vai custar R$7,00 por quilólemtro'''


velocidade = int(input('Velocidade do veiculo km/h: '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f'Excesso de velocidade! Multado em R${multa:.2f}')
else:
    print('Abaixo do limite! Boa viagem!')