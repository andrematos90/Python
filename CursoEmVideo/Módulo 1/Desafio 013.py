#faça um algoritimo que leia um sálario e calcule e exiba esse sálario com 15% de aumento


s = float(input('Digite o salário:  '))

porcentagem = s/100

novosalario = s + (porcentagem*15)

print('O novo salário é: R${:.2f}'.format(novosalario))

'''
outra forma

salario = float(input('Digite o salario: R$ '))

aumento = (salario / 100 ) * 15

print(f'O novo salário é de R${salario + aumento:.2f}')'''