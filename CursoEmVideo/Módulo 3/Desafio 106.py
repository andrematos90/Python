'''Faça um mini-sistema que utilize o interactive help do python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra "Fim", o programa encerrará. '''
c = ('\033[m',                # 0 - sem cor
     '\033[0;30;41m',        # 1 - vermelho
     '\033[0;30;42m',        # 2 - verde
     '\033[0;30;43m',        # 3 - amarelo
     '\033[0;30;44m',        # 4 - azul
     '\033[0;30;45m',        # 5 - roxo
     '\033[7;30m'            # 6 - branco
    )

def ajuda(com):
    help(com)
    return com

def titulo(msg, cor=1):
    tam = len(msg)
    print('~' * tam)
    print(c[cor], end='')
    print(msg)
    print(c[0], end='')
    print('~' * len(msg))

# programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP')
    comando = input('Função ou Biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)


'''
A primeira parte do código define uma tupla chamada c, que contém códigos de escape ANSI para formatar a saída no terminal com cores. Cada elemento da tupla representa uma cor específica.

A função ajuda(com) é definida. Ela recebe um argumento com (que geralmente seria um comando ou nome de biblioteca) e chama a função help(com) para exibir a documentação do comando ou biblioteca fornecida como entrada. Em seguida, retorna o próprio argumento com.

A função titulo(msg, cor=1) é definida. Ela recebe uma mensagem msg e um argumento opcional cor (com valor padrão igual a 1). Essa função imprime uma linha de caracteres '' com o mesmo comprimento da mensagem, em seguida imprime a mensagem formatada com a cor especificada pelo argumento cor. A cor é aplicada usando os códigos de escape ANSI presentes na tupla c. Finalmente, outra linha de caracteres '' é impressa para completar o título.

No programa principal, uma variável chamada comando é inicializada como uma string vazia.

Em seguida, há um loop while True que continuará até que o usuário insira 'FIM' como entrada para o comando.

Dentro do loop, o título 'SISTEMA DE AJUDA PYHELP' é impresso usando a função titulo(). O usuário é então solicitado a fornecer uma função ou biblioteca para a qual precisa de ajuda.

Se o usuário inserir 'FIM', o loop é interrompido e o programa termina.

Caso contrário, a função ajuda() é chamada com o comando fornecido como entrada. A função ajuda() exibe a documentação para o comando usando a função help(). O comando também é retornado, mas não é usado neste código.'''

    