

'''
99 - Faça um programa que tenha uma função chamada maior(), que receba
vários parâmetros com valores innteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior'''

from time import sleep

def maior(*num):
    pos = 0
    for i, v in enumerate(num):
        print(f'{num[pos]}', end=' ', flush=True)
        pos += 1
        sleep(0.5)
    print()
    print('-' * 30)
    print(f'foram informados {len(num)} valores')
    print(f'maior número: {max(num)}')
    print('-' * 30)

#programa principal
maior(10, 2, 1, 15)
maior(4, 7, 0)
maior(6)
maior(2,1)

'''
from time import sleep: Importa a função sleep do módulo time.

def maior(*num): Define a função maior com um parâmetro *num, que permite receber um número variável de argumentos.

pos = 0: Inicializa a variável pos com valor zero. Essa variável será usada para acompanhar a posição atual durante o loop.

for i, v in enumerate(num): Inicia um loop for utilizando a função enumerate para percorrer os valores e seus índices dentro do argumento num.

print(f'{num[pos]}', end=' ', flush=True): Imprime o valor atual, usando a variável pos como índice para acessar o valor em num.

pos += 1: Incrementa a variável pos para apontar para a próxima posição no próximo loop.

sleep(0.5): Pausa a execução por 0.5 segundos após imprimir cada valor.

print(): Imprime uma nova linha vazia para separar as informações.

print('-' * 30): Imprime uma linha horizontal de 30 caracteres "-" para fins de formatação.

print(f'foram informados {len(num)} valores'): Imprime a quantidade de valores informados.

print(f'maior número: {max(num)}'): Imprime o maior valor encontrado usando a função max() aplicada ao argumento num.

print('-' * 30): Imprime outra linha horizontal de 30 caracteres "-" para fins de formatação.

maior(10, 2, 1, 15): Chama a função maior com os valores 10, 2, 1 e 15 como argumentos.

maior(4, 7, 0): Chama a função maior com os valores 4, 7 e 0 como argumentos.

maior(6): Chama a função maior com o valor 6 como argumento.

maior(2, 1): Chama a função maior com os valores 2 e 1 como argumentos.'''


'''
                             CÓDIGO GUANABARA
                    
from time import sleep

def maior(*num):
    cont = maior = 0
    print('\n Analisando os valores....')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
             maior = valor
        cont += 1
    print(f'Foram passados {cont} valores')
    print(f'O maior valor valor foi {maior}')

#programa principal

maior(2, 9, 4, 5, 7, 1)

from time import sleep: Importa a função sleep do módulo time.

def maior(*num): Define a função maior com um parâmetro *num, que permite receber um número variável de argumentos.

cont = maior = 0: Inicializa as variáveis cont e maior com valor zero. cont será utilizada para contar a quantidade de valores passados, e maior irá armazenar o maior valor encontrado.

print('\n Analisando os valores....'): Imprime uma mensagem informando que os valores estão sendo analisados.

for valor in num:: Inicia um loop for para percorrer os valores passados como argumentos na função.

print(f'{valor}', end=' ', flush=True): Imprime cada valor passado no loop, separados por espaço, com um pequeno atraso de 0.3 segundos entre eles.

if cont == 0: maior = valor: Verifica se é o primeiro valor analisado. Se for, atribui esse valor à variável maior.

else: if valor > maior: maior = valor: Caso não seja o primeiro valor, compara o valor atual com o valor armazenado em maior. Se o valor atual for maior, atualiza maior com esse novo valor.

cont += 1: Incrementa o contador de valores cont.

print(f'Foram passados {cont} valores'): Imprime a quantidade de valores passados.

print(f'O maior valor valor foi {maior}'): Imprime o maior valor encontrado.

maior(2, 9, 4, 5, 7, 1): Chama a função maior passando os valores 2, 9, 4, 5, 7 e 1 como argumentos.

'''

