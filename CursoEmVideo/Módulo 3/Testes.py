#faça um algoritimo que leia um sálario e calcule e exiba esse sálario com 15% de aumento

salario = float(input('Digite o salario: R$ '))

aumento = (salario / 100 ) * 15

print(f'O novo salário é de R${salario + aumento:.2f}')

