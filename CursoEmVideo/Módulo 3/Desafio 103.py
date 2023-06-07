''' 104 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetro opcioanais. O nome do jogador e quantos gols ele marcou. O programa deverá ser capar de mostrar a ficha do jogador, mesmo que 
algum dado não tenha sido informado corretamente.'''


def ficha (nome = '<desconhecido>', gols = '0'):
    print(f'Nome do jogdor: {nome}')
    print(f'Gols marcados: {gols}')

jogador = input('Nome do jogador: ')
gol = input('Gols: ')
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jogador.strip() == '':
    ficha(gols=gol)
else:
    ficha(jogador, gol)

'''
A função ficha é definida com dois parâmetros: nome e gols.

Dentro da função, são exibidas duas mensagens na tela usando a função print. A primeira mensagem exibe o nome do jogador e a segunda mensagem exibe a quantidade de gols marcados.

No programa principal, o usuário é solicitado a fornecer o nome do jogador através da função input. O valor digitado pelo usuário é armazenado na variável jogador.

Em seguida, o usuário é solicitado a fornecer a quantidade de gols marcados através da função input. O valor digitado pelo usuário é armazenado na variável gol.

A próxima parte do código verifica se o valor de gol é composto apenas por dígitos usando o método isnumeric(). Isso garante que seja um valor numérico válido.

Se gol for um valor numérico, ele é convertido para um inteiro usando int(gol) e o resultado é atribuído novamente à variável gol. Caso contrário, ou seja, se gol não for um valor numérico válido, gol é definido como 0.

A próxima verificação é feita para determinar se o nome do jogador está em branco. Isso é feito usando o método strip() para remover espaços em branco no início e no final do nome do jogador e, em seguida, verificando se o resultado é uma string vazia.

Se o nome do jogador estiver em branco, a função ficha é chamada passando apenas o valor de gol como argumento nomeado gols. Isso significa que o nome do jogador será definido como <desconhecido> e a quantidade de gols será a que o usuário digitou.

Caso contrário, ou seja, se o nome do jogador não estiver em branco, a função ficha é chamada passando o nome do jogador e a quantidade de gols como argumentos posicionais. Isso significa que o nome do jogador será o valor que o usuário digitou e a quantidade de gols também será a que o usuário digitou.

Dentro da função ficha, as informações são impressas na tela de acordo com os valores fornecidos.'''


