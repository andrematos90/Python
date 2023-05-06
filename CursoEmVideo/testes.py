'''Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas.
No final do programa mostre:
* A média de idade do grupo.
*Qual o nome do homem mais velho.
*Quantas mulheres tem menos de 21 anos '''

soma = 0
media = 0
velho = 0
mulheres_acima_de_21 = 0


for c in range(1, 5):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).upper().strip()
    soma = soma + idade
    media = soma / c

print(f'Media de idade do grupo: {media} anos')
