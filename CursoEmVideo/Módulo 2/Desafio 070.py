'''
 crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário quer continuar.
 No final mostre:
 A - Quanto é o total gasto na compra.
 B - Quantos produtos custam mais de R$1000.
 C - Qual é o nome do produto mais barato.
'''

Total = MaisdeMil = menorpreço= 0
MaisBarato = ''

while True:
    produto = str(input('Qual o produto: '))
    preço = float(input('Preço R$: '))
    resposta = str(input('Quer continuar S/N? ')).upper().strip()[0]
    Total = preço + Total
    menorpreço +=1

    if preço > 1000:
        MaisdeMil = MaisdeMil + 1

    if menorpreço == 1:
        menorpreço = preço
        MaisBarato = produto
       
    if resposta == 'N':
        break
print(f'Total da compra: R${Total:.2f}')
print(f'Produtos acima de R$1000: {MaisdeMil}')
print(f'Produto mais barato: {MaisBarato}')


'''
Ele inicia definindo três variáveis: Total, MaisdeMil e menorpreço, 
todas com valor zero. Além disso, a variável MaisBarato é definida como 
uma string vazia.

O programa entra em um loop infinito usando o comando while True. Dentro do loop, 
ele solicita ao usuário o nome do produto e seu preço, e depois pergunta se o 
usuário quer continuar adicionando produtos.

O preço do produto é adicionado à variável Total.

Se o preço do produto for superior a R$1000, a variável MaisdeMil é incrementada 
em 1.

Se o preço do produto for menor do que o valor atual de menorpreço, então a variável
 MaisBarato recebe o nome do produto e menorpreço recebe o novo preço.

Se o usuário responder "N" à pergunta se deseja continuar adicionando produtos, o programa sai do loop.

Por fim, o programa exibe o valor total da compra, a quantidade de produtos com preço superior a R$1000 e o nome do produto mais barato.



                                CÓDIGO GUANABARA 

total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Produto: '))
    preco = int(input('Preço: R$'))
    total = total + preco
    cont += 1
    resposta = ' '
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    if preco > 1000:
        totmil += 1
    #enquanto a resposta nao for sim ou nao fica pedindo pra ler
    while resposta not in 'NS': 
        resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resposta == 'N':
        break
    #escreve -- e "fim do programa" centralizado
print('{:-^40}'.format('Fim do programa! '))
print(f'Total da Compra: R${total}')
print(f'Produtos acima de R$1000: {totmil}')
print(f'Produto mais barato: {barato}')

O programa começa inicializando quatro variáveis, todas com o valor 0: total, totmil,
 menor e cont.

Em seguida, uma variável barato é criada e inicializada com uma string vazia.

O programa entra em um loop infinito, que só será interrompido se o usuário escolher
 sair do programa. Dentro do loop, o programa pede ao usuário que insira o nome e o
   preço de um produto. O preço é adicionado ao total, e a variável cont é incrementada
     em 1. A variável resposta é inicializada com uma string vazia.

O programa verifica se este é o primeiro produto adicionado ou se o preço deste 
produto é menor do que o menor preço já registrado. Se sim, o preço do produto é
 armazenado na variável menor e o nome do produto é armazenado na variável barato.

O programa verifica se o preço do produto é maior do que 1000. Se sim, a variável
 totmil é incrementada em 1.

O programa pede ao usuário que insira 'S' ou 'N' para indicar se deseja continuar 
adicionando produtos ou não. O programa continuará pedindo até que uma resposta válida
 seja inserida.

Se a resposta do usuário for 'N', o loop é interrompido e o programa continua 
executando.

Finalmente, o programa imprime uma mensagem de finalização e, em seguida, imprime o 
total da compra, o número de produtos com preço acima de R$1000 e o nome do produto
 mais barato encontrado durante a execução do programa.

'''
