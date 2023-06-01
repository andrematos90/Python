'''97 - Faça um programa que tenha uma função chamdada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex: escreva('Olá, mundo!')

       -----------
saida: olá, mundo!
       -----------
'''

def escreva(txt):
    print('-' * len(txt))
    print(txt)
    print('-' * len(txt))
#programa principal
texto = input('digite um texto: ')
escreva(texto)

'''
def escreva(txt):

Esta linha define a função escreva com um parâmetro txt, que representa o texto a ser exibido.
print('-' * len(txt))

Esta linha imprime uma linha de traços (-) multiplicados pelo comprimento do texto txt. Isso cria uma linha horizontal estilizada que tem o mesmo comprimento do texto.
print(txt)

Aqui, o código simplesmente imprime o texto fornecido como argumento para a função.
print('-' * len(txt))

Da mesma forma que na linha 2, esta linha imprime outra linha de traços (-) multiplicados pelo comprimento do texto. Isso cria uma linha horizontal estilizada após o texto.
texto = input('digite um texto: ')

Esta linha solicita ao usuário que digite um texto e o armazena na variável texto usando a função input().
escreva(texto)

Por fim, a função escreva é chamada, passando o texto fornecido pelo usuário como argumento. A função escreva será executada, exibindo o texto de forma estilizada.'''