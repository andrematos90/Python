estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())  

print(brasil)

''' nao da para fazer fatiamento com dicionarios, para copiar usa-se o método copy()'''


