'''Faça um programa que mostre na tela um contagem regressiva  de 10 até 0
com intervalo de 1 segundo'''
from time import sleep

for c in range(10, 0, -1):
    sleep(1)
    print(c)
    
   
    