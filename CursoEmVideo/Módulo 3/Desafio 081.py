'''Crie um programa que vai ler vários números  e colocar em uma lista.
Depois disso, mostre: 
A - Quantos números foram digitados.
B - A Lista de valores ordenada de forma decrescente.
C - Se o valor 5 foi digitado e está ná lista ou não.
'''

num = list()
numero5 = ''


while True:
        num.append(int(input('Digite um número: ')))
        res = str(input('Quero continuar? [S/N]')).upper().strip()
        numero5 = num.count(5)
        if res == 'N':
            break
     


print(f'foram digitados {len(num)} números')
print(f'Números em ordem decrescente: {sorted(num, reverse=True)}')
print(f'O número "5" foi encontrado {numero5} vezes')

'''
Cria uma lista vazia chamada "num".
Cria uma variável vazia chamada "numero5".
Entra em um loop "while" que é executado continuamente até que o usuário decida parar de adicionar números à lista.
Dentro do loop "while", solicita ao usuário que digite um número e adiciona esse número à lista "num".
Pergunta ao usuário se ele deseja continuar adicionando números à lista. Se o usuário responder "N", o loop é interrompido e o programa passa para a próxima seção.
Verifica se o número 5 foi digitado em algum momento da lista "num". Se sim, define a variável "numero5" como o número de vezes que o número 5 aparece na lista. Se não, define a variável "numero5" como zero.
Imprime o número de itens na lista "num" usando a função "len()".
Imprime os números na lista "num" em ordem decrescente usando a função "sorted()" com o argumento "reverse=True".
Imprime quantas vezes o número 5 aparece na lista "num", usando a variável "numero5".


                             CÓDIGO GUANABARA
        
        
lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N] ? '))
    if resposta in 'nN':
        break

lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números.')
print(f'Lista Descrescente: {lista}')
if 5 in lista:
    print('Número "5" existe na lista!')
else:
    print('Número "5" não encontrado na lista!')




    
lista = [] - Cria uma lista vazia chamada lista.

while True: - Cria um loop infinito.

lista.append(int(input('Digite um número: '))) - Solicita que o usuário digite
um número inteiro e adiciona esse número à lista.

resposta = str(input('Quer continuar? [S/N] ? ')) - Pergunta ao usuário se ele
 eseja continuar digitando números.

if resposta in 'nN': - Verifica se a resposta do usuário é "n" ou "N" (ou seja,
se ele não quer continuar digitando números). Se for, o loop é interrompido com 
a palavra-chave break.

lista.sort(reverse=True) - Ordena a lista em ordem decrescente.

print(f'Foram digitados {len(lista)} números.') - Exibe o número de elementos 
presentes na lista.

print(f'Lista Descrescente: {lista}') - Exibe a lista em ordem decrescente.

if 5 in lista: - Verifica se o número 5 está presente na lista.

print('Número "5" existe na lista!') - Se o número 5 estiver presente na lista, 
exibe uma mensagem indicando que ele foi encontrado.

else: - Se o número 5 não estiver presente na lista, executa o bloco de código
seguinte.

print('Número "5" não encontrado na lista!') - Exibe uma mensagem indicando que o 
número 5 não foi encontrado na lista.






outra forma 

lista = []
cont = 0

while True:
    numero = int(input('número: '))
    lista.append(numero)
    cont += 1
    continuar = str(input('Continuar? (S/N) ')).upper().strip()
    if continuar in 'N':
        break
print(f'{cont} numeros digitados!')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print(f'O numero 5 está na lista! Na posição: {lista.index(5)}')
else:
    print('Numero 5 não foi digitado!')'''
