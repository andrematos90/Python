def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [4, 5, 6 ]
dobra(valores)
print(valores)