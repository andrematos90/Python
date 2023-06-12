def aumentar(valor = 0, taxa = 0, formatada=False):
    res = valor + (valor * taxa /100)
    return res if formatada is False else moeda(res)

def dimunuir(valor = 0, taxa = 0, formatada=False):
    res = valor - (valor * taxa / 100)
    return res if formatada is False else moeda(res)

def dobro(valor = 0, formata=False):
    res = valor * 2
    return res if not formata else moeda(res)

def metade(valor = 0, formata = False):
    res = valor / 2
    return res if formata is False else moeda(res)
    
def moeda(valor= 0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

def resumo(v=0, taxa=10, taxar=5):
     print('-' * 30)
     print('RESUMO DO VALOR:'.center(30))
     print('-' * 30)
     print(f'Valor analisado: {moeda(v)}:')
     print(f'dobro: {dobro(v, True)}') 
     print(f'metade: {metade(v, True)}')
     print(f'Taxa de aumento \t{taxa}%: {aumentar(v, taxa, True)}')
     print(f'Taxa de diminuição \t{taxar}%: {dimunuir(v, taxar, True)}')
     print('-' * 30)