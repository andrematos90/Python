'''113 - Reescreva a função leiaInt do Desafio 104, incluindo agora a possibilidadeda digitação de um número de tipo inválido. Aproveite e crie tambem uma função leiaFloat() com a mesma fucionalidade.'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!\033[0m Digite um número inteiro válido.')
            continue
        else:
           return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            ('\033[031mERRO!\033[0m Digite um numero real válido.]')
            continue
        else:
            return n
numero = leiaInt('Digite um valor inteiro: ')
numero2 = leiaFloat('Digite um número real: ')
print(f'valor inteiro digitado: \033[031m{numero}\033[0m')
print(f'valor real digitado: \033[031m{numero2}\033[0m')


'''
A função leiaInt é definida com um parâmetro chamado msg, que é a mensagem exibida para o usuário solicitar a entrada do número inteiro.
Dentro da função leiaInt, há um loop while True que continuará até que um valor inteiro válido seja fornecido pelo usuário.
Dentro do loop, o código tenta executar a seguinte linha: n = int(input(msg)). Aqui, o usuário é solicitado a fornecer a entrada usando a mensagem msg, e a função input é usada para obter o valor digitado pelo usuário.
Se o valor fornecido puder ser convertido em um número inteiro, ele é atribuído à variável n. Caso contrário, uma exceção ValueError ou TypeError será lançada.
Se ocorrer uma exceção, o código exibirá a mensagem de erro "ERRO! Digite um número inteiro válido." em vermelho ('\033[0;31mERRO!\033[0m'), e o loop continuará para solicitar uma nova entrada do usuário.
Se nenhum erro ocorrer e um valor inteiro válido for digitado, o loop será interrompido e o valor inteiro será retornado pela linha return n.
O funcionamento da função leiaFloat é semelhante ao da função leiaInt, exceto que ela lida com números reais (ponto flutuante) em vez de inteiros. Os passos são essencialmente os mesmos, mas a conversão para float é usada e a mensagem de erro é diferente.

Depois de definir as funções, o código solicita ao usuário que digite um valor inteiro usando a função leiaInt e armazena-o na variável numero. Em seguida, solicita ao usuário que digite um número real usando a função leiaFloat e armazena-o na variável `numero'''