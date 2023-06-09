from pacotes import moeda

def resumo(valor):
    print('-' * 30)
    print('RESUMO DO VALOR')
    print('-' * 30)
    print(f'Valor analisado: R${valor:.2f}')
    print(f'Dobro do Valor: {moeda.dobro(valor, True)}')
    print(f'Metade do Valor: {moeda.metade(valor, True)}')
    print(f'10% de aumento: {moeda.aumentando(valor, True)}')
    print(f'13% de redução: {moeda.diminuindo(valor, True)}')
    print('-' * 30)

'''
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
