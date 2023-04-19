'''
Crie um programa que leia varios números e coloque-os em uma lista.
Depois disso, crie duas listas extras qie vão conter apennas os valores
pares e os valores impares digitados, respectivamente. Ao final, mostre o 
conteúdo das três listas geradas.'''

numero = []
pares = []
impares = []

while True:
    numero.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar: [S/N] ?')).upper().strip()
    if resposta == 'N':
        break

for numerodalista in numero:
    if numerodalista % 2 == 0:
        pares.append(numerodalista)
    else:
        impares.append(numerodalista)

print(f'Números digitados: {numero}')
print(f'Números pares: {pares}')
print(f'Números impares: {impares}')


'''
Cria-se uma lista vazia chamada numero.
Cria-se outras duas listas vazias chamadas pares e impares.
Inicia-se um loop infinito usando a estrutura while True.
Pede-se para o usuário digitar um número e converte-se a entrada para um inteiro 
usando a função int().
Adiciona-se o número digitado à lista numero usando o método append().
Pergunta-se ao usuário se ele deseja continuar digitando números, e armazena-se a
resposta em uma variável chamada resposta. A entrada do usuário é convertida para
maiúsculas usando o método upper() e removem-se os espaços em branco usando o 
método strip().
Se a resposta do usuário for igual a 'N', o loop é interrompido usando a instrução 
break.
Inicia-se outro loop usando a estrutura for para percorrer cada número na lista numero.
Verifica-se se o número é par usando a operação de módulo % para verificar 
se o resto da divisão do número por 2 é igual a zero.
Se o número for par, ele é adicionado à lista pares usando o método append().
Se o número for ímpar, ele é adicionado à lista impares usando o método append().
Quando todos os números da lista numero foram verificados, imprime-se a lista numero,
a lista pares e a lista impares usando a função print(), com f-strings para formatar 
as strings a serem impressas.'''
