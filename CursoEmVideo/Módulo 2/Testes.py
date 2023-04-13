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


