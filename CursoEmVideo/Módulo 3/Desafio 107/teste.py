import moeda

v = float(input('Valor: '))
print(f'A metade de R${v} é {moeda.metade(v)}')
print(f'O dobro de R${v} é {moeda.dobro(v)}')
print(f'Aumentando 10% temos {moeda.aumentar(v, 10)}')
print(f'Diminuindo 13% temos {moeda.dimunuir(v, 13)}')