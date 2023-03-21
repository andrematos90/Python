#programa que le um numero inteiro e mostra sua tabuada

n = int(input('Digite um número: '))

nx1 = n*1
nx2 = n*2
nx3 = n*3
nx4 = n*4
nx5 = n*5
nx6 = n*6
nx7 = n*7
nx8 = n*8
nx9 = n*9
nx10 = n*10

print('{} x 1 = {}'.format(n,nx1))
print('{} x 2 = {}'.format(n,nx2))
print('{} x 3 = {}'.format(n,nx3))
print('{} x 4 = {}'.format(n,nx4))
print('{} x 5 = {}'.format(n,nx5))
print('{} x 6 = {}'.format(n,nx6))
print('{} x 7 = {}'.format(n,nx7))
print('{} x 8 = {}'.format(n,nx8))
print('{} x 9 = {}'.format(n,nx9))
print('{} x 10 = {}'.format(n,nx10))


#outra maneira de fazer:

n = int(input('Digite um número: '))

print('{} x {:2} = {}'.format(n,1,n*1))
print('{} x {:2} = {}'.format(n,2,n*2))
print('{} x {:2} = {}'.format(n,3,n*3))
print('{} x {:2} = {}'.format(n,4,n*4))
print('{} x {:2} = {}'.format(n,5,n*5))
print ('{} x {:2} = {}'.format(n,6,n*6))
print('{} x {:2} = {}'.format(n,7,n*7))
print('{} x {:2} = {}'.format(n,8,n*8))
print('{} x {:2} = {}'.format(n,9,n*9))
print('{} x {:2} = {}'.format(n,10,n*10))