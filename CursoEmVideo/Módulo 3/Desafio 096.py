'''
96 - Faça um programa que tenha uma função chamada area(), que receba as dimensões 
de um terreno retangular (largura x comprimento) e mostre a área do terreno'''

def area(largura, coprimento):
    a = largura * coprimento
    print(f'Área: {a:.2f} m²')

#prorgama principal
l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l, c)

'''
A função area é definida com dois parâmetros: largura e comprimento.
Dentro da função, uma variável a é criada e recebe o valor da multiplicação de largura por comprimento, o que calcula a área do retângulo.
O resultado é então impresso usando a função print e formatado como uma string com duas casas decimais usando formatação de string f: f'Área: {a:.2f}m²'.
O código solicita ao usuário que insira a largura do retângulo usando a função input, e o valor é armazenado na variável l após ser convertido para um número de ponto flutuante usando float(input('Largura: ')).
Da mesma forma, o código solicita ao usuário que insira o comprimento do retângulo, armazena o valor na variável c após convertê-lo para um número de ponto flutuante usando float(input('Comprimento: ')).
Por fim, a função area é chamada com os argumentos l e c, e a área do retângulo é calculada e impressa.

'''

