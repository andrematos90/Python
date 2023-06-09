'''109 - Modifique as funções que foram criadas no exercicios 107 para que elas aceitem um 
parÂmetro a mais, informando se o valor retornado por elas  vai ou não ser formatado pela 
função moeda(), desenvolvida no exercicio 108. '''

from pacotes import moeda

v = float(input('Valor: '))
print(f'A metade de R${v} é {moeda.metade(v, False)}')
print(f'O dobro de R${v} é {moeda.dobro(v, False)}')
print(f'Aumentando 10% de R${v}, fica: {moeda. aumentando(v, True)}')
print(f'Diminuindo 13% de {v}, fica: {moeda.diminuindo(v, False)}')


'''
Importação do módulo moeda:

O código começa importando o módulo moeda de um pacote externo. Isso permite o acesso às funções e recursos implementados nesse módulo.
Solicitação de um valor numérico ao usuário:

O código usa a função input() para solicitar ao usuário que insira um valor numérico. O valor inserido é lido como uma string.
Conversão do valor para tipo float:

O valor lido do usuário é convertido para o tipo float usando a função float(). Isso garante que o valor seja tratado como um número de ponto flutuante.
Utilização das funções do módulo moeda:

O código chama as funções do módulo moeda para realizar operações matemáticas e formatação de valores.
A função moeda.metade() é chamada passando o valor lido como argumento e o segundo argumento é definido como False. O resultado é exibido usando a função print().
A função moeda.dobro() é chamada da mesma maneira, passando o valor lido e False como argumentos.
A função moeda.aumentando() é chamada com o valor lido e True como argumentos. O resultado é exibido usando a função print().
A função moeda.diminuindo() é chamada com o valor lido e False como argumentos. O resultado é exibido usando a função print().
Exibição dos resultados formatados:

Os resultados das operações são exibidos usando a função print().
As strings formatadas usam f-strings para incluir os valores originais e os resultados das operações.'''