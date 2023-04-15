palavra = ('abacaxi', 'banana', 'laranja', 'limao', 'morango')

vogais = []
# Iteração sobre cada letra da palavra
for letra in palavra:
    # Verifica se a letra é uma vogal
    if letra.lower() in 'aeiou':
        # Adiciona a vogal à lista de vogais da palavra
        vogais.append(letra)

# Imprime a palavra e suas vogais correspondentes
print(f'A palavra "{palavra}" tem as seguintes vogais: {vogais}')
