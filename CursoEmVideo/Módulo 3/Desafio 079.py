'''Crie um program que leia vários números e os cadastre-os em 
uma lista. Caso o número ja exista ele não sera adicionado.
No final, serão exibidos todos os valores únicos digitados,
em ordem de crescente'''

num = list()


while True:
    num.append(int(input('Digite um número:')))
    copiadenum = num[:]
    resposta = str(input('Quer continuar[S/N]? ')).lower().strip()
    if 'n' in resposta:
        break
print(num)
set_num = set(num)
set_num.sort()
print(set_num)
