'''
79 - Crie um programa que leia vários números e os cadastre-os em 
uma lista. Caso o número ja exista ele não sera adicionado.
No final, serão exibidos todos os valores únicos digitados,
em ordem de crescente'''


lista = []
copia = lista[:]

while True:
    lista.append(int(input('Número: ')))
    resposta = str(input('Quer continuar? [S/N]'))
    if resposta in 'nN':
        break

   
print(copia)