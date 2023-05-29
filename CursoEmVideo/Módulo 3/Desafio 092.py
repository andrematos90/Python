'''
92 - Crie um programa que leia o nome, ano de nascimenmto e carteira de trabalho e cadastre - os (com idade) em um dicionário se por acaso o CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. Consierando que para se aposentar tem que ter 35 anos de contribuição'''
from datetime import datetime

trabalhador = {}
trabalhador['nome'] = str(input('Nome: '))
trabalhador['nascimento'] = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year
trabalhador['idade'] = ano_atual - trabalhador['nascimento']
del trabalhador['nascimento']
trabalhador['CTPS'] = int(input('Carteira de tranahlo [ 0 nao tem]: '))
if trabalhador['CTPS'] != 0:
    trabalhador['Ano de Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Sálario R$: '))
    trabalhador['Aposentadoria'] =  trabalhador['idade'] + (trabalhador['Ano de Contratação'] + 40) - datetime.now().year

print('-=' * 30)
for k, v in trabalhador.items():
    print(f' - {k} : {v}')
print('-=' * 30)

'''
A primeira linha importa o módulo datetime da biblioteca padrão do Python.
Em seguida, é criado um dicionário vazio chamado trabalhador.
O código solicita ao usuário que insira o nome do trabalhador utilizando a função input(), e o valor digitado é armazenado no dicionário trabalhador com a chave 'nome'.
Depois, é solicitado ao usuário que insira o ano de nascimento do trabalhador, utilizando novamente a função input(). O valor digitado é convertido para um inteiro usando int(), e é armazenado no dicionário trabalhador com a chave 'nascimento'.
A próxima linha obtém o ano atual utilizando o objeto datetime.now().year e armazena-o na variável ano_atual.
Em seguida, calcula-se a idade do trabalhador subtraindo o ano de nascimento do ano atual, e esse valor é armazenado no dicionário trabalhador com a chave 'idade'.
A linha del trabalhador['nascimento'] remove a chave 'nascimento' do dicionário trabalhador.
O código solicita ao usuário que insira o número da carteira de trabalho do trabalhador utilizando a função input(). O valor digitado é convertido para um inteiro usando int(), e é armazenado no dicionário trabalhador com a chave 'CTPS'.
Se o valor da chave 'CTPS' for diferente de zero (indicando que o trabalhador possui uma carteira de trabalho), o código solicita ao usuário que insira o ano de contratação utilizando a função input(). O valor digitado é convertido para um inteiro usando int(), e é armazenado no dicionário trabalhador com a chave 'Ano de Contratação'.
Em seguida, o código solicita ao usuário que insira o salário do trabalhador utilizando a função input(). O valor digitado é convertido para um número de ponto flutuante usando float(), e é armazenado no dicionário trabalhador com a chave 'Salário'.
A próxima linha calcula o valor da chave 'Aposentadoria'. A fórmula utilizada é a idade do trabalhador + (ano de contratação + 40) - ano atual. O resultado é armazenado no dicionário trabalhador com a chave 'Aposentadoria'.
Em seguida, o código imprime uma linha de separação contendo o caractere - repetido 60 vezes.
Um loop for é utilizado para percorrer todas as chaves e valores do dicionário trabalhador.
A cada iteração do loop, o código imprime o nome da chave seguido por seu respectivo valor.
Após o loop, é impressa outra linha de separação.'''