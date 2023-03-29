'''Faça um programa que mostre na tela um contagem regressiva  de 10 até 0
com intervalo de 1 segundo'''

from time import sleep
import os 

for cont  in range (10, -1, -1):
    sleep(1)
    os.system('cls') or None
    print(cont)
print('=-' * 6, 'FOGOS', '=-' *6)
   
    