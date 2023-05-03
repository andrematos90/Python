'''Faça um programa que leia uma frase e mostre:

* quantas vezes aparece a letra "A".
* em que posição ela aparece a primeira vez.
* em que posição ela aparece a ultima vez.'''



frase = input('Digite uma frase: ').upper().strip()

print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A')+1))
print ('Aparece pela última vez na posição {}'.format(frase.rfind('A')+1))


'''
outra forma 

frase = str(input('Frase: ')).lower()
quantidad_deA = frase.count('a')
print(f'A letra "A" aparece {quantidad_deA} na frase "{frase}"')
posicao_deA = frase.find('a')
print(f'Primeira ocorrência na posição {posicao_deA}')
ultima = frase.rfind('a')
print(f'A ultima ocorrênca acontece na posição: {ultima}')'''