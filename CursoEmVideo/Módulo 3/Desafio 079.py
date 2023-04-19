'''Crie um programa que leia vários números e os cadastre-os em 
uma lista. Caso o número ja exista ele não sera adicionado.
No final, serão exibidos todos os valores únicos digitados,
em ordem de crescente'''

numeros = []

while True:  # Entra em um loop infinito
    num = int(input('Digite um número: '))  # Pede para o usuário digitar um número e armazena na variável num
    if num not in numeros:  # Verifica se o número digitado já está na lista numeros
        numeros.append(num)  # Se o número não estiver na lista, adiciona-o à lista numeros
        print('Valor adicionado!')  # Imprime a mensagem "Valor adicionado!"
    else:
        print('Número repetido! Não adicionado a lista')  # Se o número já estiver na lista, imprime a mensagem "Número repetido! Não adicionado a lista"
    resposta = str(input('Quer continuar: [S/N] ?'))  # Pede para o usuário digitar se quer continuar ou não e armazena na variável resposta
    if resposta in 'Nn':  # Verifica se a resposta é "n" ou "N"
        break  # Se a resposta for "n" ou "N", sai do loop while True
numeros.sort()  # Ordena a lista numeros em ordem crescente
print(f'Números digitados: {numeros}')  # Imprime a lista numeros ordenada em ordem crescente

'''
A linha while True: cria um loop infinito, ou seja, um loop que se repete 
indefinidamente até que uma condição de parada seja alcançada.
A linha num = int(input('Digite um número: ')) pede para o usuário digitar um 
número e armazena o número digitado na variável num como um valor inteiro
(usando a função int()).
A linha if num not in numeros: verifica se o número digitado não está na lista numeros. Se o número não estiver na lista, o código dentro do bloco if é executado.
A linha numeros.append(num) adiciona o número digitado à lista numeros usando o
método append().
A linha print('Valor adicionado!') imprime a mensagem "Valor adicionado!" na tela.
Se o número já estiver na lista numeros, o código dentro do bloco else é executado.
A linha print('Número repetido! Não adicionado a lista') imprime a mensagem "Número 
repetido! Não adicionado a lista" na tela.
A linha resposta = str(input('Quer continuar: [S/N] ?')) pede para o usuário digitar
se deseja continuar ou não e armazena a resposta na variável resposta como uma string 
(usando a função str()).
A linha if resposta in 'Nn': verifica se a resposta do usuário é "n" ou "N" (usando a 
sintaxe de in para verificar se um caractere está contido em uma string).
Se a resposta do usuário for "n" ou "N", a linha break é executada, o que faz o código
sair do loop while.
A linha numeros.sort() ordena a lista numeros em ordem crescente usando o método sort().
A linha print(f'Números digitados: {numeros}') imprime a lista numeros'''
