'''
Crie um programa que leia vários números inteiros. No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valor lido. O programa deve perguntar ao usúario se ele quer ou não continuar
a digitar valores
'''


r = 's'
c = 0
m = 0
s = 0
menor = 0
maior = 0

while r in 'Ss':
    n = int(input('Digite um número: '))
    c+=1
    s = s + n
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar digitando s/n? ')).upper().strip()[0]
m = s / c
print('Você digitou {} números'.format(c))
print('A Média entre os números somados é {:.2f}'.format(m))
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))



# strip()[0] remove os espaços e considera só a primeira letra


'''
outra forma 

cont = media = maior = menor = soma = 0
primeiro = True
while True:
    numero = int(input('Numero: '))
    resposta = str(input('Continuar? S/N ')).upper().strip()
    soma = soma + numero
    cont += 1

    if primeiro:
       maior = menor = numero
       primeiro = False
    else: 
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    if resposta in 'Nn':
        break

print(f'Média: {soma / cont}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')

Inicializamos as variáveis cont, media, maior, menor e soma com o valor 0. A variável primeiro é inicializada como True para controlar se o número atual é o primeiro número digitado.

Iniciamos um loop infinito usando while True.

O usuário é solicitado a digitar um número utilizando a função input, e o valor é convertido para um número inteiro e armazenado na variável numero.

O usuário é solicitado a responder se deseja continuar digitando números. A resposta é convertida para letras maiúsculas usando o método upper() e espaços em branco são removidos do início e do final usando o método strip(). O resultado é armazenado na variável resposta.

O número digitado é adicionado à variável soma para realizar a soma acumulada dos números.

O contador cont é incrementado em 1 para contar a quantidade de números digitados.

Verificamos se é o primeiro número digitado usando a variável primeiro. Se for, atribuímos o valor de numero tanto para as variáveis maior quanto para menor e atualizamos a variável primeiro para False.

Se não for o primeiro número digitado, verificamos se o número atual (numero) é maior que o valor armazenado na variável maior. Se sim, atualizamos maior com o novo valor.

Em seguida, verificamos se o número atual (numero) é menor que o valor armazenado na variável menor. Se sim, atualizamos menor com o novo valor.

Verificamos se a resposta do usuário é "N" ou "n". Se for, utilizamos o comando break para sair do loop e continuar a execução do programa.

Calculamos a média dos números digitados, dividindo a soma pela quantidade de números (soma / cont) e armazenamos o resultado na variável media.

Fora do loop, utilizamos f-strings para exibir a média, o maior e o menor número digitado.

'''



