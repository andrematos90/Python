'''
79 - Crie um programa que leia vários números e os cadastre-os em 
uma lista. Caso o número ja exista ele não sera adicionado.
No final, serão exibidos todos os valores únicos digitados,
em ordem de crescente'''


lista = []
unicos = []

while True:
    lista.append(int(input('Número: ')))
    resposta = str(input('Quer continuar? [S/N]'))
    if resposta in 'nN':
        break

   
for item in lista:
    if item not in unicos:
        unicos.append(item)
        

unicos.sort()
print(f'Valores únicos digitados em ordem: {unicos}')