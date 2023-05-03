#programa para ler quantos reais uma pessoa tem e converter para dolares

R = float(input('Quantos Reais você tem? R$'))

D = 5.24

C = R/D

print('Pela cotação atual voce tem U${:.2f} (Dolares)'.format(C))

'''
outra forma 

reais = int(input('Digite quantos reais você tem: '))

dolar = (reais / 5.06)

print(f'{reais} equivalem a {dolar:.2f} dólares na cotação de hoje!')'''