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


'''
 iniciam três variáveis, pessoas, homens e mulheres, com o valor inicial zero. 
 Essas variáveis serão usadas posteriormente para contar quantas pessoas têm mais 
 de 18 anos, quantos homens e quantas mulheres com menos de 20 anos foram cadastrados.
  um loop while True, que significa que o loop continuará executando indefinidamente, 
  a menos que seja interrompido por um comando break.
  As varíaveis solicitam ao usuário que insira a idade, o sexo e se deseja continuar 
  cadastrando pessoas. O comando input() é usado para capturar a entrada do usuário 
  e as funções int(), str(), upper() e strip() são usadas para converter, formatar 
  e limpar a entrada.
  
      if idade > 18:
        pessoas = pessoas + 1

Essa linha de código verifica se a idade inserida pelo usuário é maior que 18.
 Se for, a variável pessoas é incrementada em 1.


     if sexo == 'M':
        homens = homens +1

Essa linha de código verifica se o sexo inserido pelo usuário é masculino. 
Se for, a variável homens é incrementada em 1.

    if sexo == 'F' and idade < 20:
        mulheres = mulheres +1

Essa linha de código verifica se o sexo inserido pelo usuário é feminino e
 se a idade é menor que 20. Se ambas as condições forem verdadeiras, a variável 
 mulheres é incrementada em 1.



     if resposta == 'N':
        break
        

Essa linha de código verifica se o usuário deseja continuar cadastrando pessoas. 
Se a resposta for "N", o comando break interrompe o loop while.

print(f'Foram cadastradas {pessoas} pessoas com mais de 18 anos!')
print(f'{homens} homem(s)')
print(f'{mulheres} mulheres com menos de 20 anos')

Essas três linhas de código imprimem o resultado final da contagem. 
As f-strings são usadas para inserir os valores das variáveis diretamente 
nas strings. O resultado exibido será o número total de pessoas com mais de 18
 anos, o número total de homens e o número total de mulheres com menos de 20 anos.


                                   CÓDIGO GUANABARA




tot18 = totm20 = toth = 0

while True:    
        idade = int(input('Digite a idade: '))
        sexo = ' '
        while sexo not in 'FM':
                sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]

        if idade >= 18:
               tot18 +=1

        if sexo =='M':
               toth +=1

        if sexo == 'F' and idade < 20:
               totm20 +=1

        resposta = ' '
        while resposta not in 'SN':
                resposta = str(input('Quer continuar?')).upper().strip()[0]
        if resposta == 'N':
          break

print(f'{tot18} Pessoas com mais de 18 anos!')
print(f'{toth} Homens foram cadastrados!')
print(f'{totm20} Mulheres tem menos de 20 anos!')


O programa começa com três variáveis sendo inicializadas como 0:
 "tot18", "totm20" e "toth".

Em seguida, é iniciado um loop "while True" que continuará executando até que o usuário
decida sair do programa. Dentro desse loop, o programa solicita que o usuário digite
a idade e o sexo da pessoa, verifica se a idade é maior ou igual a 18 anos e, se
for, incrementa a variável "tot18" em 1. O programa também verifica se o sexo é 
masculino (letra "M") e, se for, incrementa a variável "toth" em 1. Além disso,
o programa verifica se o sexo é feminino (letra "F") e a idade é menor do que
20 anos, e se for, incrementa a variável "totm20" em 1.

Depois disso, o programa pergunta se o usuário quer continuar a digitar mais pessoas 
ou sair do programa. Se o usuário digitar "N", o loop é interrompido e o programa 
exibe na tela as contagens de "tot18", "totm20" e "toth" que foram acumuladas durante 
a execução do loop.

Por fim, o programa exibe na tela a quantidade de pessoas com mais de 18 anos, a quantidade de homens cadastrados e a quantidade de mulheres com menos de 20 anos.

outra forma 

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



'''
