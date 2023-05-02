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

'''outra maneira de fazer:

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

outra forma
numero = int(input('Digite um número: '))


print('-=' * 7)
print(f'TABUADA DE {numero}')
print('-=' * 7)
print(f'1 x {numero} = {1 * numero}')
print(f'2 x {numero} = {2 * numero}')
print(f'3 x {numero} = {3 * numero}')
print(f'4 x {numero} = {4 * numero}')
print(f'5 x {numero} = {5 * numero}')
print(f'6 x {numero} = {6 * numero}')
print(f'7 x {numero} = {7 * numero}')
print(f'8 x {numero} = {8 * numero}')
print(f'9 x {numero} = {9 * numero}')
print(f'10 x {numero} = {10 * numero}')



'''