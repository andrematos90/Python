'''Faça um prorama que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F' .
Caso contrário, peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Digite o sexo M/F: ').strip().upper()[0])  #strip tira os espaços, upper deixa maicuscolo, [0] pega só a primeira letra 
while sexo not in 'MF':
    sexo = input('O sexo deve ser M ou F: ')
print('Registrado com sucesso')



'''outra forma 

sexo = ' '
while True:
    if sexo not in 'MF':
     sexo = str(input('Sexo: ')).upper().strip()
    else:
       break
print(f'Sexo definido como: {sexo}')

'''