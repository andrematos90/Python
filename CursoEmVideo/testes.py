'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros
elementos de uma sequência de fibonacci'''


numero = int(input('quantidade de termos: '))
t1 = 0
t2 = 1

print(f'{t1} ➝  {t2} ➝  ', end='')
cont = 3
while cont <= numero:
   t3 = t1 + t2
   print(f'{t3} ➝  ', end='')
   t1 = t2
   t2 = t3
   cont += 1

