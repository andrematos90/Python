'''
85 - Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares e impares.
No final, mostre os valores pares e impares em ordem crescente.'''
lista = []
par = []
impar = []

for c in range (0, 7):
    numero = int(input('Número: '))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
par.sort()
lista.append(par)
impar.sort()
lista.append(impar)
print(f'pares: {lista[0]}')
print(f'impares: {lista[1]}')

'''
Cria três listas vazias: lista, par e impar.
Inicia um loop for que executa 7 vezes.
Pede ao usuário para inserir um número.
Verifica se o número é par ou ímpar usando o operador %.
Se o número for par, adiciona-o à lista par, caso contrário, adiciona-o à lista impar.
Ordena as listas par e impar usando o método sort().
Adiciona a lista par à lista lista.
Adiciona a lista impar à lista lista.
Imprime a lista par na tela usando a f-string formatada com lista[0].
Imprime a lista impar na tela usando a f-string formatada com lista[1].


                                 CÓDIGO GUANABARA


num = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()
print(f'Pares: {num[0]}')
print(f'impares: {num[1]}')


Cria uma lista num com duas listas vazias dentro: num[0] e num[1].
Inicia um loop for que executa 7 vezes.
Pede ao usuário para inserir um número.
Verifica se o número é par ou ímpar usando o operador %.
Se o número for par, adiciona-o à lista num[0], caso contrário, adiciona-o à lista num[1].
Ordena as listas num[0] e num[1] usando o método sort().
Imprime a lista num[0] na tela usando a f-string formatada com num[0] mostra  os valores do indice "0" que são os pares.
Imprime a lista num[1] na tela usando a f-string formatada com num[1] mostra os valores do indice "1" que são os impares.
'''



