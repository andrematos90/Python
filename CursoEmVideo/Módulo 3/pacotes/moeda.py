def metade(numeroquequeroametade):
    return numeroquequeroametade / 2

def dobro(numeroquequeroodoro):
    return numeroquequeroodoro * 2

def aumentando(numeroquequeroaumentar):
    numeroquequeroaumentar = numeroquequeroaumentar + (numeroquequeroaumentar / 100) *10
    return numeroquequeroaumentar

def diminuindo(numeroquequerodiminmuir):
    numeroquequerodiminmuir = numeroquequerodiminmuir - ((numeroquequerodiminmuir / 100) *  13)
    return numeroquequerodiminmuir

def moeda(valor):
   return f'R${valor:.2f}'