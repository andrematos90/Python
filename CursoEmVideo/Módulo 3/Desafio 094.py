'''
94 - Crie um programa que leia o nome, sexo  e idade de várias pessoas, guardando os dados de cada uma delas em um dicionário e todos os dicionários em uma lista. No final mostre:
A - Quantas pessoas foram cadastradas.
B - A Média de idade do grupo.
C - Uma lista com todas as mulheres.
D - Uma lista com todas as pessoas com idade acima da média.'''

pessoa = {}
galera = []
acima_da_media = []
total_pessoas = 0
soma_idades = 0
media = 0


while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! O Campo aceita apenas M/F')       
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    total_pessoas += 1
    
    while True:    
        continuar = input('Continuar[S/N]: ').upper().strip()
        if continuar in 'SN':
            break
        print('ERRO! O campo aceita apenas S/N')
    if continuar == 'N':
        break
print('-=' * 30)
print()
print(galera)
print()
print('-=' * 30)
print()
#analisando os dados
print('A - Quantas pessoas foram cadastradas:')
print(f'{total_pessoas} pessoas.')
print()
print('B - A Média de idade do grupo.')
idades = [pessoa['idade'] for pessoa in galera]
soma_idades = sum(idades)
media = soma_idades / total_pessoas
print(f'{media} anos.')
print()
print('C - Uma lista com todas as mulheres.')
for p in galera:
    if p['sexo'] == "F":
        print(p['nome'])
print()
print('D - Uma lista com todas as pessoas com idade acima da média.')
print()
for p in galera:
    if media < p['idade']:
        print(p['nome'])

'''
Inicialização das variáveis: As variáveis "pessoa", "galera", "acima_da_media", "total_pessoas", "soma_idades" e "media" são inicializadas.

Loop principal (while True): Esse loop permite adicionar informações de várias pessoas à lista "galera". Ele continua executando até que a condição de parada (continuar == 'N') seja satisfeita.

Solicitação de informações da pessoa: Dentro do loop principal, as informações da pessoa (nome, sexo e idade) são solicitadas ao usuário utilizando a função input() e armazenadas no dicionário "pessoa".

Validação do sexo: Existe um loop while True que verifica se o sexo fornecido é válido ('M' ou 'F'). O loop continua até que um valor válido seja inserido. Se o valor for inválido, uma mensagem de erro é exibida.

Adição da pessoa à lista "galera": O dicionário "pessoa" é copiado e adicionado à lista "galera" usando o método append(). A variável "total_pessoas" é incrementada em 1.

Validação para continuar: Outro loop while True é usado para verificar se o usuário deseja continuar adicionando mais pessoas. O loop continua até que um valor válido ('S' ou 'N') seja inserido. Uma mensagem de erro é exibida se um valor inválido for inserido.

Impressão dos resultados:

Impressão da lista "galera": É exibida a lista completa "galera" com todas as informações das pessoas cadastradas.

Impressão da quantidade de pessoas cadastradas: A variável "total_pessoas" é impressa para indicar o número total de pessoas cadastradas.

Cálculo e impressão da média de idade do grupo: Uma lista chamada "idades" é criada com as idades das pessoas usando uma compreensão de lista. A função sum() é usada para calcular a soma das idades, que é armazenada na variável "soma_idades". A média de idade é calculada dividindo a soma das idades pelo número total de pessoas ("total_pessoas"). O valor da média é impresso.

Impressão da lista com todas as mulheres: Um loop for percorre cada pessoa na lista "galera". Se o valor da chave "sexo" for igual a "F", o nome da pessoa é impresso.

Impressão da lista de pessoas com idade acima da média: Outro loop for percorre cada pessoa na lista "galera". Se a idade da pessoa for maior que a média de idade, o nome da pessoa é impresso.'''




