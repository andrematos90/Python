import aula22modulos as uteis

num = int(input('Digite um número: '))
fat = uteis.fatorial(num)
print(f'o Factorial de {num} é {fat}')
print(f'o dobro de {num} é {uteis.dobro(num)}')
print(f'o triplo de {num} é {uteis.triplo(num)}')