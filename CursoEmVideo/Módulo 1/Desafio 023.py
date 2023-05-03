#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

'''ex: numero :1834

unidade: 4
dezena: 3
centena: 8
milhar: 1
'''

numero = (input('Digite um numero: '))


print('Unidade: {}'.format(numero[3]))
print('dezena: {}'.format(numero[2]))
print('centena: {}'.format(numero[1]))
print('milhar: {}'.format(numero[0]))


'''
                                    #OUTRA FORMA DE FAZER


numero = int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 100
m = numero // 1000 % 1000

print('Analisando o numero: {}'.format(numero))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar {}'.format(m))


outra forma de fazer 

numero = int(input('Digite o número: '))
numuero_str = str(numero)
print(f'Milhar: {numuero_str[0]}')
print(f'Centena: {numuero_str[1]}')
print(f'Dezena: {numuero_str[2]}')
print(f'Unidade: {numuero_str[-1]}')
'''