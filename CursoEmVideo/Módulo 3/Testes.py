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

