'''93 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''


jogador = {}
gols = []
jogador['nome'] = input('Nome: ')
jogador['partidas'] = int(input('Partidas: '))

for c in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
    total = sum(gols)
jogador['gols'] = gols
jogador['total'] = total
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor: {v}')
    if k == jogador['partidas']:
        jogos = [k]
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou: {jogador["partidas"]} partidas.')
for i, v in enumerate (jogador['gols']):
    print(f' => na partida {i} fez {v} gols.')
print(f'Total de {total} gols')
print('=-' * 30)

'''
O código cria um dicionário vazio chamado jogador.
O programa solicita ao usuário que insira o nome do jogador usando a função input(). O valor digitado é armazenado no dicionário jogador com a chave 'nome'.
Em seguida, o programa solicita ao usuário que insira o número de partidas jogadas pelo jogador usando a função input(). O valor digitado é convertido para um inteiro usando int(), e é armazenado no dicionário jogador com a chave 'partidas'.
Em seguida, é iniciado um loop for que itera de 0 até o número de partidas do jogador (exclusivo).
Dentro do loop, o programa solicita ao usuário que insira o número de gols marcados pelo jogador em cada partida, utilizando a função input(). O valor digitado é convertido para um inteiro usando int(), e é adicionado à lista gols.
Após o término do loop, o programa calcula o total de gols somando todos os elementos da lista gols usando a função sum(), e o resultado é armazenado na variável total.
O programa adiciona a lista gols ao dicionário jogador com a chave 'gols'.
O programa adiciona a variável total ao dicionário jogador com a chave 'total'.
Em seguida, o programa imprime uma linha de separação contendo o caractere - repetido 60 vezes.
O programa imprime o dicionário jogador.
O programa imprime outra linha de separação.
Um loop for é utilizado para percorrer todas as chaves e valores do dicionário jogador.
A cada iteração do loop, o programa imprime o nome da chave seguido por seu respectivo valor.
Dentro do loop, há uma verificação condicional if para verificar se a chave atual é igual ao valor de 'partidas' no dicionário jogador. Se for igual, a lista jogos é criada contendo apenas o valor atual da chave.
Após o loop, o programa imprime outra linha de separação.
O programa imprime a quantidade de partidas jogadas pelo jogador, utilizando o valor da chave 'partidas' do dicionário jogador.
Um loop for com a função enumerate() é usado para percorrer a lista de gols do jogador.
A cada iteração do loop, o programa imprime o número da partida (índice) e o número de gols marcados naquela partida.
O programa imprime o total de gols do jogador, utilizando o valor da variável total.
Finalmente, o programa imprime mais uma linha de separação.'''
