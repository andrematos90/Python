# Programa que le valor em metro e converte para centimetros e milimetros


metro = float(input('Digite quantos metros: '))

cent = metro * 100
mili = metro * 1000

print(f'{metro} metros em centrimetros são: {cent} centímetro', end=' ')
print(f' em milímetro são {mili} milímetros.')
