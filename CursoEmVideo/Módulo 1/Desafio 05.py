#Faça um programa que leia um numero inteiro e mostre na tela se sucessor e seu antecessor


n = int(input('Digite um número:'))

print('Antecessor: {}'.format(n-1,n))
print('Sucessor: {}'.format(n+1,n))

'''
outra forma

numero = int(input('Digite um número: '))

print(f'Você digitou o número {numero} o antecessor dele é {numero - 1} e o sucessor é {numero + 1}')

'''
