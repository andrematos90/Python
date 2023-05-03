# faça um programa que leia a altura e a lagura de uma parede em metros
# calcule sua area e a quantidade de tinta necesaria para pintala,
#sabendo que cada litro de tinta pinta uma area de 2m²


altura = float(input('Altura: '))
largura = float(input('Largura: '))
area = altura * largura
litros = area / 2

print(f'Para uma parede de {area}m² de área, serão utilizados {litros:.2f} litros.')