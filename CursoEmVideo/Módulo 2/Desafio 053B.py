frase = str(input('Digite uma frase: ')).strip().upper  # strip() retira os espaços do inicio e do final
                                                        #upper retorna a string em maiúsculo

palavras = frase.split() # separa as  palavras em substrings
junto = ''.join(palavras) # junta todas as palavra
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('é um palindromo!')
else:
    print('não é um palindromo!')
