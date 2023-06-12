'''110 - Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre
na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui'''

import moeda

v = float(input('Valor: '))
print(f'A metade de {moeda.moeda(v)} é {(moeda.metade(v, ))}')
print(f'O dobro de {moeda.moeda(v)} é {(moeda.dobro(v, True))}')
print(f'Aumentando 10% temos {(moeda.aumentar(v, 10))}')
print(f'Diminuindo 13% temos {(moeda.dimunuir(v, 13))}')