galera = []
dados = []
totmaio = 0
totmen = 0

for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)

#para mostrar somente os maiores de idade

for p in galera:
    if p[1] > 18:
        print(f' {p[0]} é maior de idade!')
        totmaio +=1
    else:
        print(f'{p[0]} é menor de idade')
        totmen +=1
print(f'total de maiores {totmaio}')
print(f'total de menores {totmen}')