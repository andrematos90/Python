# converter graus Celcius para Fahrenheith

c = float(input('Digite em graus Celcius: '))

f =  c *1.8 + 32
k = c + 273

print('{}° Celcius equivalem a {}° Fahreinheit'.format(c,f))
print('e {}° Celcius correspondem a {}° Kelvin'.format(c,k))

'''
outra forma 

celcius = float(input('Digite em graus Celcius: '))

print(f'{celcius}°C em Farenheit é {celcius * 1.8 + 32}°F')'''