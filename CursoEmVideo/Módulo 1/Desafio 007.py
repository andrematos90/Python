#Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

m = (n1+n2)/2

print('Média: {:.1f}'.format(m))


'''
outra forma

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

print(f'A média é {media}')
'''