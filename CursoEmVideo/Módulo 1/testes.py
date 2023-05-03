'''Faça um programa que leia uma frase e mostre:

* quantas vezes aparece a letra "A".
* em que posição ela aparece a primeira vez.
* em que posição ela aparece a ultima '''

frase = str(input('Frase: ')).lower()
quantidad_deA = frase.count('a')
print(f'A letra "A" aparece {quantidad_deA} na frase "{frase}"')
posicao_deA = frase.find('a')
print(f'Primeira ocorrência na posição {posicao_deA}')
ultima = frase.rfind('a')
print(f'A ultima ocorrênca acontece na posição: {ultima}')
