'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC E mostre
seu status, se acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal 
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('IMC: {:.2f}'.format(imc))
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('IMC: {:.2f}'.format(imc))
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('IMC: {:.2f}'.format(imc))
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('IMC: {:.2f}'.format(imc))
    print('Obeso')
elif imc > 40:
    print('IMC: {:.2f}'.format(imc))
    print('Obesidade morbida')


'''
outra forma 

peso = float(input('Peso: '))
altura = float(input('Digite a altura: '))
imc = peso /(altura ** 2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc > 18.5 and imc < 25:
    print('Peso ideal')
elif imc > 25 and imc < 30:
    print('Sobrepeso')
elif imc > 30 and imc < 40:
    print('Obeso')
else:
    print('Obesidade Morbida')

'''