'''Faça um programa que leia um número inteiro e mostre seu fatorial

Ex: 5*4*3*2*1 = 120'''


num = int(input('Digite um número: '))

while num >= 1:
    num = num * (num - 1) * (num - 2) * (num - 3)
print(num)
    


