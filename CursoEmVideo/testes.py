'''61 - Refaça o exercicio 051, lendo o primeiro de uma PA e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.

a10 = a1 + (10 - 1)d

Onde:

a10 é o décimo termo da sequência;
a1 é o primeiro termo da sequência;
d é a diferença comum entre os termos da sequência.
Basicamente, essa fórmula utiliza a diferença comum d para calcular o valor do décimo termo, que é encontrado adicionando (10 - 1) d ao valor do primeiro termo a1.

'''

primeiro = int(input('primeiro termo: '))
razao = int(input('razão: '))
decimo = 0

for c in range(primeiro, primeiro + 10, razao):
    print(f'{decimo == primeiro + (10 - 1) *razao}')

