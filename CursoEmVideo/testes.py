'''Faça um prorama que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F' .
Caso contrário, peça a digitação novamente até ter um valor correto.'''
sexo = ' '
while True:
    if sexo not in 'MF':
     sexo = str(input('Sexo: ')).upper().strip()
    else:
       break
print(f'Sexo definido como: {sexo}')

