'''
crie um programa que leia a idade e sexo de várias pessoas. 
a cada pessoa cadastrada, o programa deverá perguntar se o usuário quer 
continuar. No final mostre: 
A - Quantas pessoas tem mais de 18 anos.
B - Quantos homens foram cadastrados.
C - Quantas mulheres tem menos de 20 anos.
'''
pessoas = 0
homens = 0
mulheres = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('M ou F? ')).upper().strip()[0]
    resposta = str(input('Quer continuar S/N? ')).upper().strip()[0]

    if idade > 18:
           pessoas = pessoas + 1
    if sexo == 'M':
            homens = homens +1
    if sexo == 'F' and idade < 20:
            mulheres = mulheres +1
    if resposta == 'N':
          break
print(f'Foram cadastradas {pessoas} pessoas com mais de 18 anos!')
print(f'{homens} homem(s)')
print(f'{mulheres} mulheres com menos de 20 anos')
