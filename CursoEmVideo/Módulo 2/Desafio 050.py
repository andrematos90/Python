'''Desenvola um programa que leia 6 números inteiros 
e mostre a soma apenas daqueles que forem par'''

soma = 0


for c in range (1, 7):
  n = int(input('Digite o numero {}°: '.format(c)))
  if n % 2 == 0:
   soma = soma + n


print('Soma dos numeros pares: {}'.format(soma))


'''
outra forma 

soma = 0

for c in range(0, 6):
    numero = int(input('Numero: '))
    if numero % 2 == 0:
        soma = numero + soma
print(soma)
    '''