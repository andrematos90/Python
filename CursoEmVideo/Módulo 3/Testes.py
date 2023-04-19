numeros_digitados = []
impares = []
pares = []

while True:
    numeros_digitados.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N] ?'))
    if resposta in 'nN':
     break

for indice, valor in enumerate(numeros_digitados):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f'Números digitados! {numeros_digitados}')
print(f'pares: {pares}')
print(f'impares: {impares}')

