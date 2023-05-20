'''Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para cada palavra,
quais são as vogais'''

tupla = ('andre', 'camila', 'davi', 'isabella')

for palavra in tupla:
    print(f'\nNa palavra {palavra} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
         print(letra, end=' ')

'''
Primeiro, definimos a tupla de palavras: tupla = ('andre', 'camila', 'davi', 'isabella').

Em seguida, iniciamos um loop for para percorrer cada palavra na tupla: for palavra in tupla:.

Para cada palavra na tupla, imprimimos a mensagem inicial com a palavra atual: print(f'\nNa palavra {palavra} temos as vogais: ', end=''). O uso de \n antes da mensagem imprime uma nova linha para cada palavra.

Agora, iniciamos um segundo loop for para percorrer cada letra na palavra atual: for letra in palavra:.

Para cada letra na palavra, verificamos se ela é uma vogal. Usamos letra.lower() para converter a letra para minúscula e garantir uma comparação case-insensitive. A condição if letra.lower() in 'aeiou': verifica se a letra está presente na string de vogais.

Se a letra for uma vogal, a imprimimos seguida de um espaço em branco: print(letra, end=' '). O uso de end=' ' substitui a quebra de linha padrão por um espaço em branco, permitindo que as vogais sejam impressas lado a lado.

Após o término do segundo loop for, o fluxo do programa volta para o primeiro loop for, avançando para a próxima palavra na tupla.

Esse processo se repete para cada palavra na tupla até que todas as palavras tenham sido percorridas.'''