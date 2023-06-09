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
Essas funções podem ser usadas para realizar cálculos matemáticos simples, como obter a metade, o dobro, aumentar ou diminuir um número em uma determinada porcentagem e formatar valores monetários.




FUNÇÃO RESUMO 

Impressão de linhas de separação:

A função imprime uma linha de caracteres '-' repetidos 30 vezes usando o operador de multiplicação (print('-' * 30)). Isso cria uma linha visualmente separada para o resumo.
Impressão do título "RESUMO DO VALOR":

A função imprime a string "RESUMO DO VALOR" usando a função print().
Impressão de linhas de separação:

A função imprime novamente uma linha de caracteres '-' repetidos 30 vezes para separar o título do restante do resumo.
Impressão do valor analisado:

A função imprime a string formatada f'Valor analisado: R${valor:.2f}'. Essa string inclui o valor fornecido como argumento com o símbolo de real (R$) e duas casas decimais.
Impressão do dobro do valor:

A função chama a função dobro() passando o valor fornecido como argumento e True como segundo argumento para obter o dobro do valor formatado. O resultado é impresso utilizando a função print().
Impressão da metade do valor:

A função chama a função metade() passando o valor fornecido como argumento e True como segundo argumento para obter a metade do valor formatada. O resultado é impresso utilizando a função print().
Impressão do aumento de 10%:

A função chama a função aumentando() passando o valor fornecido como argumento e True como segundo argumento para obter o valor aumentado em 10% formatado. O resultado é impresso utilizando a função print().
Impressão da redução de 13%:

A função chama a função diminuindo() passando o valor fornecido como argumento e True como segundo argumento para obter o valor reduzido em 13% formatado. O resultado é impresso utilizando a função print().
Impressão de linhas de separação:

A função imprime novamente uma linha de caracteres '-' repetidos 30 vezes para '''

