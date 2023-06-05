'''
98- Faça um programa que tenha uma função chamada contador(),
que receba três parametros: inicio, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada.

A - De 1 até 10, de um em um
B - De 10 até 0, de 2 em 2
C - Uma contagem personalizada.
'''
from time import sleep

def contador(*num):
     print('A - De 1 até 10, de um em um:')
     for c in range(1, 10 + 1, 1):
        print(f'{c}', end=' ' )
     sleep(1)
     print('FIM!')
     print('-' * 30 )
     print('B - De 10 até 0, de 2 em 2:')
     for c in range(10, 0, -2):
        print(f'{c}', end=' ' )
     sleep(1)
     print('FIM!')
     print('-' * 30 )
     print('C - Uma contagem personalizada:')
     inicio = int(input('Inicia em: '))
     fim = int(input('Termina em: '))
     passo = int(input('pula de: '))
     if passo == 0:
        passo = 1
     if passo < 0:
        passo = passo * (-1)
     if inicio > fim:
        for c in range(inicio, fim - 1 , passo * (-1)):
           print(f'{c}', end=' ' )
           sleep(0.5)
     elif inicio < fim:
         for c in range(inicio, fim + 1, passo):
           print(f'{c}', end=' ' )
           sleep(1)
     elif passo < 0:
         for c in range(inicio, fim - 1, passo):
            print(f'{c}', end=' ' )
     sleep(1)
     print('FIM!')
     print('-' * 30 )
contador()

'''   
                                    CÓDIGO GUANABARA
                                    
                                    
from time import sleep

def contador(i, f, p):
  if p < 0:
     p *= -1
  if p == 0:
     p = 1
  print(f'contagem de {i} até {f} de {p} em {p}')
  if i < f:
    cont = i
    while cont <= f:
        print(f'{cont}', end=' ', flush=True)
        sleep(0.5)
        cont += p
    print('FIM!')
  else:
     cont = i
     while cont >= f:
        print(f'{cont}', end=' ',flush=True)
        sleep(0.5)
        cont -= p
     print('FIM!')


#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('CONTAGEM PERSONALIZADA')
ini = int(input('Inicio:  '))
fim= int(input('Fim:      '))
pas = int(input('Passo:   '))
contador(ini, fim, pas)

from time import sleep: Importa a função sleep do módulo time.

def contador(i, f, p): Define a função contador com três parâmetros: i (início), f (fim) e p (passo).

if p < 0:: Verifica se o valor do passo é negativo.

p *= -1: Multiplica o valor do passo por -1 para torná-lo positivo.

if p == 0:: Verifica se o valor do passo é igual a zero.

p = 1: Define o valor do passo como 1.

print(f'contagem de {i} até {f} de {p} em {p}'): Imprime uma mensagem informando a contagem que será realizada.

if i < f:: Verifica se o valor de início é menor que o valor de fim.

cont = i: Inicializa a variável cont com o valor de início.

while cont <= f:: Inicia um loop enquanto o valor de cont for menor ou igual ao valor de fim.

print(f'{cont}', end=' ', flush=True): Imprime o valor atual de cont.

sleep(0.5): Pausa a execução por 0.5 segundos.

cont += p: Incrementa o valor de cont pelo valor do passo.

print('FIM!'): Imprime "FIM!" quando a contagem é concluída.

else:: Caso a condição do passo negativo ou zero não seja atendida.

cont = i: Inicializa a variável cont com o valor de início.

while cont >= f:: Inicia um loop enquanto o valor de cont for maior ou igual ao valor de fim.

print(f'{cont}', end=' ',flush=True): Imprime o valor atual de cont.

sleep(0.5): Pausa a execução por 0.5 segundos.

cont -= p: Decrementa o valor de cont pelo valor do passo.

print('FIM!'): Imprime "FIM!" quando a contagem é concluída.

contador(1, 10, 1): Chama a função contador com os argumentos 1, 10 e 1.

contador(10, 0, 2): Chama a função contador com os argumentos 10, 0 e 2.

print('CONTAGEM PERSONALIZADA'): Imprime uma mensagem informando sobre a contagem personalizada.

ini = int(input('Inicio: ')): Solicita ao usuário o valor de início e o converte para inteiro.

fim = int(input('Fim: ')): Solicita ao usuário o valor de fim e o converte para inteiro.

pas = int(input('Passo: ')): Solicita ao usuário o valor do passo e o converte para inteiro.

contador(ini, fim, pas): Chama a função contador com os parametros'''

