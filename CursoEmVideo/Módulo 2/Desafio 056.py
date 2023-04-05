'''Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas.
No final do programa mostre:
* A média de idade do grupo.
*Qual o nome do homem mais velho.
*Quantas mulheres tem menos de 21 anos '''

soma = 0
total = 0


for pessoa in range(1,5):
   
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Masculo ou Femino? '))
  
    soma = soma + idade
    total = total + 1
    media = soma / total 
print('A média de idade do grupo é de {} anos'.format(media))


    


