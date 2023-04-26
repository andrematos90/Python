princ = []
temp = []
pesada = leve = 0

while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso: ')))
    if len(princ) == 0:
        pesada = leve = temp[1]
    else:
        if temp[1] > pesada:
            pesada = temp[1]
        if temp[1] < leve:
            leve = temp[1]

    princ.append(temp[:])
    temp.clear()


    resposta = str(input('Continuar? [S/N]'))
    if resposta in 'nN':
        break
for p in princ:
    if p[1] == pesada:
        print(f'{p[0]} é o(a) mais pesado(a) com {pesada}Kg')

for p in princ:
    if p[1] == leve:
        print(f'{p[0]} é o(a) mais leve com {leve};kg')

print(f'Total de pessoas cadastradas: {len(princ)}')

'''
princ = []

Cria uma lista vazia chamada "princ", que será usada para armazenar todas as pessoas cadastradas.

temp = []

Cria outra lista vazia chamada "temp", que será usada temporariamente para armazenar o nome e o peso de cada pessoa.

pesada = leve = 0

Inicializa as variáveis "pesada" e "leve" com o valor 0. Essas variáveis serão usadas para determinar a pessoa mais pesada e a pessoa mais leve, respectivamente.

while True:

Inicia um loop infinito usando a palavra-chave "while" seguida da constante "True". Isso significa que o loop será executado repetidamente até que seja interrompido por alguma condição.

temp.append(str(input('Digite o nome: ')))

Solicita o nome de uma pessoa usando a função "input" do Python e armazena o valor digitado na lista "temp", convertendo-o em uma string usando a função "str" do Python. O método "append" adiciona o valor digitado ao final da lista "temp".

temp.append(float(input('Digite o peso: ')))

Solicita o peso da mesma pessoa usando a função "input" do Python e armazena o valor digitado na lista "temp", convertendo-o em um número decimal (float) usando a função "float" do Python.

if len(princ) == 0:

Verifica se a lista "princ" está vazia. Se estiver vazia, significa que esta é a primeira pessoa sendo cadastrada, e portanto seu peso deve ser definido como o valor inicial de "pesada" e "leve".

pesada = leve = temp[1]

Define o valor de "pesada" e "leve" como o peso da primeira pessoa cadastrada (o segundo elemento da lista "temp", que contém o peso).

else:

Se a lista "princ" não estiver vazia, significa que já há pelo menos uma pessoa cadastrada, e portanto é necessário comparar o peso da pessoa atual com os valores de "pesada" e "leve".

if temp[1] > pesada:

Verifica se o peso da pessoa atual (o segundo elemento da lista "temp") é maior que o valor de "pesada". Se for, atualiza o valor de "pesada" com o peso da pessoa atual.

if temp[1] < leve:
Verifica se o peso da pessoa atual é menor que o valor de "leve". Se for, atualiza o valor de "leve" com o peso da pessoa atual.

princ.append(temp[:])
Adiciona a lista "temp" à lista "princ" usando o método "append". É importante usar a sintaxe "temp[:]" em vez de simplesmente "temp", para que seja criada uma cópia da lista "temp" e adicionada à lista "princ", em vez de adicionar uma referência para a mesma lista.

temp.clear()
Limpa a lista "temp" usando o método "clear", para que possa ser reutil'''




