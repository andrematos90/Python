'''
Crie um programa que leia vários números inteiros. No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valor lido. O programa deve perguntar ao usúario se ele quer ou não continuar
a digitar valores
'''


r = 's'
c = 0
m = 0
s = 0
menor = 0
maior = 0

while r in 'Ss':
    n = int(input('Digite um número: '))
    c+=1
    s = s + n
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar digitando s/n? ')).upper().strip()[0]
m = s / c
print('Você digitou {} números'.format(c))
print('A Média entre os números somados é {:.2f}'.format(m))
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))



# strip()[0] remove os espaços e considera só a primeira letra



