'''Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo será formado?

- equilárero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes'''

lado1 = float(input('Digite o tamanho da mediado do primeiro lado do triângulo: '))
lado2 = float(input('Digite a medida do segundo lado: '))
lado3 = float(input('Digite a terceira medida: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:

     if lado1 == lado2 == lado3:
      print('é possivel formar um triangulo equilatero')
     elif lado1 != lado2 != lado3 != lado1:
      print('é possivel formar um triangulo escaleno')
     else:
      print('é possível formar um triangulo isósceles')

else:
  print('Não forma um triangulo')


