#programa para ler quantos reais uma pessoa tem e converter para dolares

R = float(input('Quantos Reais você tem? R$'))

D = 5.24

C = R/D

print('Pela cotação atual voce tem U${:.2f} (Dolares)'.format(C))