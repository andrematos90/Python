num = list()

for c in range(0, 5):
   num.append(int(input(f'Digite um valor para a posição {c}: ')))

print(f'Maior valor: {max(num)} na posição {num.index(max(num))}')
print(f'Menor valor: {min(num)} na posição {num.index(min(num))}')
