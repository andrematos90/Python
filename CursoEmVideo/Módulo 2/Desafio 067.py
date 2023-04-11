'''
Faça umn programa que mostre a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usúario.O programa será interrompido quando o número solicitado for negativo.
'''

num = 0

while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num <= 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-' *30)
print('Fim')
  