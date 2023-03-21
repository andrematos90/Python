#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#calcule e mostre o tamanho da hipotenusa.

catop = float(input('Cateto oposto:'))
catadj = float(input('Cateto adjacente:'))

hip = (catop ** 2 + catadj ** 2) **(1/2)

print('Hipotenusa: {:.2f}'.format(hip))
