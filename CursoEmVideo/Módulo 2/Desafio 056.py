'''Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas.
No final do programa mostre:
* A média de idade do grupo.
*Qual o nome do homem mais velho.
*Quantas mulheres tem menos de 21 anos '''

soma = 0
total = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0


for pessoa in range(1,5):
   
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Masculo ou Femino? '))
  
    soma = soma + idade
    total = total + 1
    media = soma / total 

    if pessoa == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    
    if sexo in'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1

print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('O total de mulheres com menos de 20 anos é de {} Mulheres'.format(totmulher20))




