'''Crie um programa que vai ler vários números  e colocar em uma lista.
Depois disso, mostre: 
A - Quantos números foram digitados.
B - A Lista de valores. ordenada de forma decrescente.
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
Imprime quantas vezes o número 5 aparece na lista "num", usando a variável "numero5".'''
