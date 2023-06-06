'''
102 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros. O primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.'''


n = int(input('número: '))

for c in range(0, n):
    fatorial = n * (n - 1)
    n = n - 1
print(fatorial)
