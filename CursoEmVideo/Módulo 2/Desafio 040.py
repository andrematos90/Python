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