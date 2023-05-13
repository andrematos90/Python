'''
crie um programa que leia a idade e sexo de várias pessoas. 
a cada pessoa cadastrada, o programa deverá perguntar se o usuário quer 
continuar. No final mostre: 
A - Quantas pessoas tem mais de 18 anos.
B - Quantos homens foram cadastrados.
C - Quantas mulheres tem menos de 20 anos.
'''
maior_18 = 0
homens_cadastrados = 0
mulheres_menor_de_20 = 0
while True:
    
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).upper().strip()
    resposta = str(input('Continuar S/N: ')).upper().strip()
    if idade >= 18:
        maior_18 += 1
    if sexo == 'M':
     homens_cadastrados += 1
    if sexo == 'F' and idade <= 20:
       mulheres_menor_de_20 +=1
    if resposta in 'nN':
        break
print(f'Pessoas maiores de 18: {maior_18}')
print(f'Homens cadastrados: {homens_cadastrados}')
print(f'Mulheres menores de 20 anos: {mulheres_menor_de_20}')