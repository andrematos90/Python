#Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

m = (n1+n2)/2

print('Média: {:.1f}'.format(m))