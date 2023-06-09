'''108 - Adapte o código do exercicio 107, criando uma função adicional chamada moeda() que consiga mostrar
os valores como um valor monetário formatado.'''
from pacotes import moeda

v = float(input('Valor R$: '))

print(f'A metade de R${v:.2f} é {moeda.moeda(moeda.metade(v))}')
print(f'O dobro de R${v:.2f} é, {moeda.moeda(moeda.dobro(v))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentando(v))}')
print(f'Diminuido 13%, temos {moeda.moeda(moeda.diminuindo(v))}')