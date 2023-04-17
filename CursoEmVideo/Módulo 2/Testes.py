palavras = ('simba', 'bin', 'ovo', 'carro', 'aviao', 'telescopio','uva', 'paralelepipido')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')


'''
Esse é um programa Python que utiliza uma lista de palavras chamada "palavras" 
e faz um loop em cada uma delas para imprimir as vogais presentes em cada palavra.
Aqui está uma explicação passo a passo do código:

A lista de palavras "palavras" é definida com 8 elementos.

O loop "for p in palavras" é iniciado, percorrendo cada elemento da lista.

Dentro do loop "for p", o comando "print" é utilizado para exibir o valor da
variável "p", que é a palavra atual da lista. A função "upper()" é utilizada para 
transformar a palavra em letras maiúsculas.

Em seguida, um loop "for letra in p" é iniciado para percorrer cada letra da 
palavra "p".

Dentro do loop "for letra", a condição "if letra.lower() in 'aeiou'" é utilizada para 
verificar se a letra atual é uma vogal (minúscula).

Se a letra for uma vogal, ela é impressa na tela, utilizando o comando "print(letra, 
end='')". O parâmetro "end=''" é utilizado para que a próxima letra da palavra seja 
impressa ao lado da letra atual, em vez de uma nova linha ser criada.

O loop "for letra" continua a percorrer cada letra da palavra "p" até o final.

O loop "for p" continua a percorrer cada palavra da lista "palavras" até o final.

Ao final, o programa imprime as vogais de cada palavra da lista na tela.'''