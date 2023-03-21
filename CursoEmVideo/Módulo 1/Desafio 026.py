'''Faça um programa que leia uma frase e mostre:

* quantas vezes aparece a letra "A".
* em que posição ela aparece a primeira vez.
* em que posição ela aparece a ultima vez.'''



frase = input('Digite uma frase: ').upper().strip()

print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A')+1))
print ('Aparece pela última vez na posição {}'.format(frase.rfind('A')+1))