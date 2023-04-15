'''Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para cada palavra,
quais são as vogais'''

palavras = ('simba', 'aviao', 'mulher', 'agua', 'carro', 'cachorro')
vogais = []

# Iteração sobre cada letra da palavra
for letra in palavras:
    # Verifica se a letra é uma vogal
    if letra.lower() in 'aeiou':
        # Adiciona a vogal à lista de vogais da palavra
        vogais.append(letra)

# Imprime a palavra e suas vogais correspondentes
print(f'A palavra "{palavras}" tem as seguintes vogais: {vogais}')