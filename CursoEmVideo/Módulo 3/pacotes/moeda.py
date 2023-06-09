def metade(numeroquequeroametade, formatado=False):
    if formatado == False:
        return numeroquequeroametade / 2
    else:
       return moeda(numeroquequeroametade)

def dobro(numeroquequeroodoro, formatado=False):
    if formatado == False:
        return numeroquequeroodoro * 2
    else:
        return moeda(numeroquequeroodoro * 2)

def aumentando(numeroquequeroaumentar, formatado=False):
    if formatado == False:
        numeroquequeroaumentar = numeroquequeroaumentar + (numeroquequeroaumentar / 100) *10
        return numeroquequeroaumentar
    else:
          numeroquequeroaumentar = numeroquequeroaumentar + (numeroquequeroaumentar / 100) *10
          return moeda(numeroquequeroaumentar)

def diminuindo(numeroquequerodiminmuir, formatado=False):
    if formatado == False:
        numeroquequerodiminmuir = numeroquequerodiminmuir - ((numeroquequerodiminmuir / 100) *  13)
        return numeroquequerodiminmuir
    else:
        numeroquequerodiminmuir = numeroquequerodiminmuir - ((numeroquequerodiminmuir / 100) *  13)
        return moeda(numeroquequerodiminmuir)

def moeda(valor):
   return f'R${valor:.2f}'

def resumo(valor):
    print('-' * 30)
    print('RESUMO DO VALOR')
    print('-' * 30)
    print(f'Valor analisado: R${valor:.2f}')
    print(f'Dobro do Valor: {dobro(valor, True)}')
    print(f'Metade do Valor: {metade(valor, True)}')
    print(f'10% de aumento: {aumentando(valor, True)}')
    print(f'13% de redução: {diminuindo(valor, True)}')
    print('-' * 30)

'''
Função metade(numeroquequeroametade, formatado=False):

Esta função recebe um número como argumento (numeroquequeroametade) e um argumento opcional chamado formatado.
Se formatado for False, a função retorna a metade do número fornecido (numeroquequeroametade / 2).
Caso contrário, a função chama a função moeda passando o número fornecido como argumento e retorna o valor formatado pela função moeda.
Função dobro(numeroquequeroodoro, formatado=False):

Esta função recebe um número como argumento (numeroquequeroodoro) e um argumento opcional chamado formatado.
Se formatado for False, a função retorna o dobro do número fornecido (numeroquequeroodoro * 2).
Caso contrário, a função chama a função moeda passando o dobro do número fornecido como argumento e retorna o valor formatado pela função moeda.
Função aumentando(numeroquequeroaumentar, formatado=False):

Esta função recebe um número como argumento (numeroquequeroaumentar) e um argumento opcional chamado formatado.
Se formatado for False, a função aumenta o número em 10% e retorna o valor resultante (numeroquequeroaumentar + (numeroquequeroaumentar / 100) * 10).
Caso contrário, a função chama a função moeda passando o número aumentado em 10% como argumento e retorna o valor formatado pela função moeda.
Função diminuindo(numeroquequerodiminmuir, formatado=False):

Esta função recebe um número como argumento (numeroquequerodiminmuir) e um argumento opcional chamado formatado.
Se formatado for False, a função diminui o número em 13% e retorna o valor resultante (numeroquequerodiminmuir - ((numeroquequerodiminmuir / 100) * 13)).
Caso contrário, a função chama a função moeda passando o número diminuído em 13% como argumento e retorna o valor formatado pela função moeda.
Função moeda(valor):

Esta função recebe um valor numérico como argumento.
A função formata o valor numérico fornecido como uma string formatada para representar um valor monetário com o símbolo de real (R$) e duas casas decimais (f'R${valor:.2f}').
Em seguida, retorna a string formatada representando o valor monetário.
Essas funções podem ser usadas para realizar cálculos matemáticos simples, como obter a metade, o dobro, aumentar ou diminuir um número em uma determinada porcentagem e formatar valores monetários.'''