'''Crie um programa onde o usuário possa digitar cinco valores
e cadastre-os em uma lista, ja na posição correta de inserção
(sem usar o sort(). No final, mostre a lista ordenada na tela.)'''

lista = []  # Cria uma lista vazia
for i in range(5):  # Loop que roda 5 vezes
    valor = int(input('Digite um valor: '))  # Pede para o usuário digitar um valor e guarda na variável 'valor'
    if i == 0:  # Se o índice 'i' for igual a zero, significa que é o primeiro valor a ser adicionado à lista
        lista.append(valor)  # Adiciona o valor na primeira posição da lista
    else:  # Caso contrário (se o índice 'i' for diferente de zero), a lista já tem pelo menos um elemento
        posicao = 0  # Define a variável 'posicao' como zero (posição inicial para a inserção do valor)
        while posicao < len(lista) and valor > lista[posicao]:  # Loop que roda enquanto a posição atual for menor que o tamanho da lista e o valor for maior do que o valor na posição atual da lista
            posicao += 1  # Incrementa a variável 'posicao' em uma unidade
        lista.insert(posicao, valor)  # Insere o valor na posição correta da lista
print('A lista ordenada é:', lista)  # Imprime a lista ordenada


'''
Cria uma lista vazia chamada "lista".
Inicia um loop "for" que executa 5 vezes.
Dentro do loop, solicita que o usuário insira um valor inteiro.
Verifica se a variável "i" é igual a 0. Se sim, adiciona o valor à lista vazia.
Se não, segue para o próximo passo.
Inicia um loop "while" para inserir o valor em ordem crescente na lista. 
O loop continua enquanto a variável "posicao" é menor que o comprimento da lista
e o valor a ser inserido é maior do que o valor na posição atual.
Quando a posição correta é encontrada, insere o valor na lista.
Retorna ao loop "for" e repete os passos 3 a 6 para os próximos valores inseridos pelo usuário.
Quando o loop "for" termina, imprime a lista ordenada.



                            CÓDIGO GUANABARA
                            
lista = []
for c in range(0,5):
    n = int(input('Digite um número: '))
    if c == 0:
        lista.append(n)
        print('Adicionado ao final da lista!')
    else:
        pos = 0
        while pos <len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista!')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram: {lista}')



lista = [] - Cria uma lista vazia chamada lista.

for c in range(0, 5): - Cria um loop que irá se repetir 5 vezes.

n = int(input('Digite um número: ')) - Solicita que o usuário digite um número 
inteiro e armazena esse valor na variável n.

if c == 0: - Verifica se o valor da variável c é igual a 0. Se for,
 o número digitado será adicionado ao final da lista.

lista.append(n) - Adiciona o número digitado ao final da lista.

print('Adicionado ao final da lista!') - Exibe uma mensagem informando que o número
foi adicionado ao final da lista.

else: - Se o valor da variável c não for igual a 0, o código seguirá para essa linha.

pos = 0 - Define o valor da variável pos como 0.

while pos < len(lista): - Cria um loop que irá se repetir enquanto o valor da 
variável pos for menor que o tamanho da lista.

if n <= lista[pos]: - Verifica se o número digitado é menor ou igual ao valor 
presente na posição atual da lista.

lista.insert(pos, n) - Adiciona o número digitado na posição atual da lista, 
deslocando os valores posteriores para a direita.

print(f'Adicionado na posição {pos} da lista!') - Exibe uma mensagem informando 
em que posição o número foi adicionado.

break - Interrompe o loop while.

pos += 1 - Incrementa o valor da variável pos em 1.

print('-=' * 30) - Exibe uma linha de separação.

print(f'Os valores digitados em ordem foram: {lista}') - Exibe uma mensagem 
informando os valores digitados em ordem crescente na lista.'''


