'''
96 - Faça um programa que tenha uma função chamada area(), que receba as dimensões 
de um terreno retangular (largura x comprimento) e mostre a área do terreno'''

def area(l, c):
    r = l * c
    print(f'Área: {r:.2f}m²')

l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l, c)

'''
def area(l, c):

Esta linha define uma função chamada area com dois parâmetros: l (largura) e c (comprimento).
r = l * c

Nesta linha, o código calcula a área multiplicando a largura (l) pelo comprimento (c) e armazena o resultado na variável r.
print(f'Área: {r:.2f}m²')

Aqui, a função exibe a área calculada usando a função print(). A sintaxe {r:.2f} formata o valor de r como um número de ponto flutuante com duas casas decimais.
l = float(input('Largura: '))

Esta linha solicita ao usuário que digite a largura e armazena o valor na variável l. A função input() é usada para obter a entrada do usuário como uma string, e a função float() é usada para converter a string em um número de ponto flutuante.
c = float(input('Comprimento: '))

Aqui, o código solicita ao usuário que digite o comprimento e armazena o valor na variável c. Assim como na linha anterior, a função float() é usada para converter a entrada do usuário em um número de ponto flutuante.
area(l, c)

Esta linha chama a função area, passando os valores de l e c como argumentos. A função será executada, calculando a área e exibindo o resultado.'''

