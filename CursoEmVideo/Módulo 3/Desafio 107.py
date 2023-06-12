'''
107 - Crie um módulo chamado moeda.py que tenha funções incorporadas
aumentar(), diminuir(). dobro(), e metade().

Faça também um programa que importe esse módulo e use algumas dessas funções'''

from pacotes import moeda

#programa principal

p = float(input('Valor R$: '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentando(p)}')
print(f'Diminuido 13%, temos {moeda.diminuindo(p)}')