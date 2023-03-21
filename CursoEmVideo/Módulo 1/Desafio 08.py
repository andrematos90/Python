# Programa que le valor em metro e converte para centimetros e milimetros

metros = float(input('Digite um número em metros: '))

cm = metros*100

mm = metros*1000

print('"{}" metros em centimetros é {:.0f}cm e em milimetros {:.0f}mm'.format(metros,cm,mm))