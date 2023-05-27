'''
86 - Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores
lidos pelo teclado.
No final, motre a matriz na tela com a formatação correta.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'numero para a posição: {linha}:{coluna}: '))
print('=-' * 30)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()


