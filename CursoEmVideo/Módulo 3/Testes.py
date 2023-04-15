num = (int(input('Digite um numero: ')),
      int(input('Digite um numero: ')),
      int(input('Digite um numero: ')),
      int(input('Digite um numero: ')))
      
print(f' O número "9" aparece {num.count(9)} vezes.')

if 3 in num:
    print(f'A primeira vez que o numero "3" aparece é na posição {num.index(3) + 1}')
else:
    print('O número "3" não aparece')

print('Números pares: ')
for n in num:   # para cada numero em n 
    if n % 2 == 0: # verifico se o resto é 0, se for 
        print(n, end=' ')# dou print em n