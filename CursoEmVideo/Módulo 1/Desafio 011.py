# faça um programa que leia a altura e a lagura de uma parede em metros
# calcule sua area e a quantidade de tinta necesaria para pintala,
#sabendo que cada litro de tinta pinta uma area de 2m²


altura = float(input('Altura: '))
largura = float(input('Largura: '))

area = altura*largura

t = area/2

print(' Área parede: {} \n Tinta necessária: {:.2f} litros'.format(area,t))