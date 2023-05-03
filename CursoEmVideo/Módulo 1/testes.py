'''Escreva um program que pergunte o salário de um funcionário
e calcule o valor do seu aumento, para salários superiores a
R$ 1250.00 calcule um aumento de 10%, para os inferiores ou iguais
o aumento é de 15%'''

salario = float(input('Sálario R$: '))

if salario <= 1250:
    print(f'Novo salário: {salario + (salario / 100 * 15):.2f}')
elif salario > 1250:
    print(f'Novo salário: {salario + (salario / 100 * 10):.2f}')