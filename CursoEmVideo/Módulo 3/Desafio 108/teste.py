'''108 - Adapte o código do exercicio 107, criando uma função adicional chamada moeda() que consiga mostrar
os valores como um valor monetário formatado.'''
import moeda

v = float(input('Valor: '))
print(f'A metade de {moeda.moeda(v)} é {moeda.moeda(moeda.metade(v))}')
print(f'O dobro de {moeda.moeda(v)} é {moeda.moeda(moeda.dobro(v))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(v, 10))}')
print(f'Diminuindo 13% temos {moeda.moeda(moeda.dimunuir(v, 13))}')