#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#calcule e mostre o tamanho da hipotenusa.
from math import sqrt
oposto = float(input('Cateto oposto: '))
adjacente  = float(input('Cateto adjacente: '))
hipotenusa = sqrt(oposto **2 + adjacente **2) 
print(f'A hipotenusa é {(hipotenusa)}')