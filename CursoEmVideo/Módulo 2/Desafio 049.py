'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando laço for.'''

n = int(input('Número: '))

for c in range (1, 11): 

 print('{} x {} = {}'.format(n, c, n * c))

 '''
 outra forma 
 
 numero = int(input('Numero: '))
print('-=' * 10)
print(f'Tabuda de {numero}')
print('-=' * 10)
for n in range(0, 11):
    print(f'{numero} x {n} = {numero * n}')'''
