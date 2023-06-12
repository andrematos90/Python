def aumentar(valor = 0, taxa = 0, formatada=False):
    res = valor + (valor * taxa /100)
    return res if formatada is False else moeda(res)

def dimunuir(valor = 0, taxa = 0, formatada=False):
    res = valor - (valor * taxa / 100)
    return res if formatada is False else moeda(res)

def dobro(valor = 0, formata=False):
    res = valor * 2
    return res if formata is False else moeda(res)

def metade(valor = 0, formata = False):
    res = valor / 2
    return res if formata is False else moeda(res)
    
def moeda(valor= 0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')