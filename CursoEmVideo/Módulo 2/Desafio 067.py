'''
Faça umn programa que mostre a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usúario.O programa será interrompido quando o número solicitado for negativo.
'''



while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    print('-' *30)
    if num <= 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-' *30)
print('Fim')


'''
Neste código, usamos um loop while True para ler o número digitado pelo 
usuário e exibir a sua tabuada. Se o usuário digitar um valor negativo,
 saímos do loop usando a instrução break.

Dentro do loop, usamos um loop for para exibir a tabuada do número digitado
 pelo usuário. O loop for percorre os números de 1 a 10 (inclusive) e exibe o 
 resultado da multiplicação do número digitado pelo usuário pelo número do loop.'''
  
'''
outra forma 

while True:
    cont =  0
    numero = int(input('Numero: '))
    if numero < 0:
        break
    for c in range(1, 11):
        cont += 1
        resultado = numero * cont
        print(f'{numero} x {cont} = {resultado}')'''