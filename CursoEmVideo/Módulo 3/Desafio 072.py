'''
Crie um programa que tenha uma tupla totalmente preenchida com uma 
contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso'''


tupla = ('zero', 'um', 'dois', 'três', 'quatro', 
         'cinco', 'seis', 'sete', 'oiteo', 'nove', 
         'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze','dezesseis', 'dezessete', 'dezoito', 
         'dezenove', 'vinte' )

while True:

    n = int(input('Digite um número entre 0 e 20: '))

    if 0 <= n <= 20:
         break

print(f'Você digitou: {tupla[n]}')
   
'''
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
'seis', 'sete', 'oiteo', 'nove', 'dez', 'onze', 'doze', 'treze', 
'quatorze', 'quinze','dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )

Essa linha define uma tupla chamada "tupla" contendo as palavras que 
representam os números de 0 a 20.

while True:

Essa linha começa um loop "while True" que continuará executando enquanto
a condição for verdadeira.

n = int(input('Digite um número entre 0 e 20: '))

Essa linha solicita ao usuário que digite um número entre 0 e 20 
e armazena o valor digitado na variável "n". A função "input" é usada para
obter a entrada do usuário e a função "int" é usada para converter a entrada 
em um número inteiro.

if 0 <= n <= 20:

Essa linha verifica se o número digitado pelo usuário está 
dentro do intervalo de 0 a 20 usando uma estrutura de condição "if". 
Se o número estiver dentro do intervalo, o código dentro do bloco "if" será executado.

break

Essa linha é executada se a condição do "if" na linha anterior for verdadeira.
A instrução "break" interrompe o loop "while True".

print(f'Você digitou: {tupla[n]}')

Essa linha é executada após o loop ser interrompido. Ela usa a função "print"
para exibir uma mensagem informando o número digitado pelo usuário. O número é
acessado na tupla usando a variável "n" como índice, e a palavra correspondente
é exibida usando a formatação de string f-string.'''