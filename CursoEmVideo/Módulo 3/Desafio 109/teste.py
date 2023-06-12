'''109 - Modifique as funções que foram criadas no exercicios 107 para que elas aceitem um 
parÂmetro a mais, informando se o valor retornado por elas  vai ou não ser formatado pela 
função moeda(), desenvolvida no exercicio 108. '''
import moeda

v = float(input('Valor: '))
print(f'A metade de {moeda.moeda(v)} é {(moeda.metade(v, ))}')
print(f'O dobro de {moeda.moeda(v)} é {(moeda.dobro(v, ))}')
print(f'Aumentando 10% temos {(moeda.aumentar(v, 10))}')
print(f'Diminuindo 13% temos {(moeda.dimunuir(v, 13))}')