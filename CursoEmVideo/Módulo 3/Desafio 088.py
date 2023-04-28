'''
88 - Crie um programa que ajude um jogador da mega sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e sortear 6 números
para cada um deles  entre 1, 60, cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
lista = []
jogos = []
print('=' *30)
print('                MEGA SENA            ')
print('=' * 30)
quantidade = int(input('Quantos jogos? '))
tot = 1
while tot <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'=' * 3, f' SORTEANDO {quantidade} JOGOS', '=' * 3)
for i, l in enumerate(jogos):
    print(f'jogo {i +1}: {l}')
    sleep(2)


'''
O código importa as bibliotecas random e sleep usando o comando from random import randint e from time import sleep, respectivamente. Isso permite que o código gere números aleatórios e faça uma pausa entre cada jogo sorteado.
O código cria duas listas vazias: lista e jogos. A lista lista será usada para armazenar temporariamente os 6 números sorteados para cada jogo, enquanto a lista jogos armazenará todas as listas de números sorteados.
O código imprime na tela uma mensagem de boas-vindas com um título e um visual mais elaborado usando caracteres especiais.
O usuário é solicitado a inserir a quantidade de jogos que deseja gerar. Essa quantidade é armazenada na variável quantidade.
O código inicia um loop while que irá sortear os números para cada jogo. O loop executa quantidade vezes, ou seja, sorteia números para a quantidade de jogos que o usuário especificou.
Dentro do loop principal, o código inicializa uma variável cont para controlar quantos números já foram sorteados para o jogo atual. Em seguida, o código inicia outro loop while que irá sortear um número por vez até que sejam sorteados 6 números diferentes entre 1 e 60.
Dentro do loop interno, o código usa a função randint para sortear um número aleatório entre 1 e 60 e verifica se esse número já está na lista lista com o comando if num not in lista. Se o número ainda não estiver na lista, o código o adiciona à lista com o comando lista.append(num) e incrementa a variável cont em 1.
Quando a lista lista contém 6 números diferentes, o loop interno é encerrado com o comando break. A lista lista é então ordenada com o comando lista.sort() para colocar os números em ordem crescente.
A lista lista com os 6 números sorteados é adicionada à lista jogos com o comando jogos.append(lista[:]). O [:] garante que o código adicione uma cópia da lista lista à lista jogos, em vez de uma referência à lista lista original.
A lista lista é limpa com o comando lista.clear() para que possa ser usada para armazenar os números do próximo jogo.
A variável tot é incrementada em 1, para controlar quantos jogos já foram sorteados dentro do loop principal.
Depois que todos os jogos foram sorteados e armazenados na lista jogos, o código imprime uma mensagem na tela indicando que os jogos estão sendo sorteados.
O código inicia outro loop for que percorre todos os jogos na lista jogos. Para cada jogo, o código imprime na tela uma mensagem com o número do jogo e a lista de 6 números sorteados.
Entre cada jogo, o código faz uma pausa de 2 segundos usando a função sleep(2) da biblioteca time'''
    
