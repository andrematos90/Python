'''Crie um programa que leia duas notas, calcule a média e informe:

- média abaixo de 5: Reprovado
- média enrte 5 e 6.9: Recuperação
- média acima de 7: Aprovado'''

n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2) /2

if media < 4.9:
    print('Média: {} REPROVADO!'.format(media))

elif media >= 5 and media <= 6.9:
    print('Média: {} RECUPERAÇÃO!'.format(media))

else:
    print('Média: {} APROVAD0!'.format(media))


'''
outra forma 

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota :'))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'Média: {media} Reprovado!')
elif media > 5 and media < 6.9:
    print(f'Média: {media} Recuperação!')
else:
    print(f'Média: {media} Aprovado!')'''