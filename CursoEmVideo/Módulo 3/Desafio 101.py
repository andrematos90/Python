''' 101 - Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornado um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.'''

def voto(ano):
    from datetime import date
    ano_atual = date.today()
    idade = ano_atual.year - ano
    if idade < 16:
        return f'{idade} anos, Voto Negado!'
    elif idade >= 18 and idade <= 65:
        return f'{idade} anos, Voto Obrigatório!'
    else:
        return f'{idade} anos, voto Opcional!'

#prorgama principal
nascimento = int(input('Ano de nascimento: '))
print(voto(nascimento))


'''
O programa principal solicita ao usuário que insira o ano de nascimento.
O valor inserido pelo usuário é armazenado na variável nascimento.
A função voto(ano) é chamada, passando o valor de nascimento como argumento.
Dentro da função voto, o módulo datetime é importado para obter a data atual.
A data atual é armazenada na variável ano_atual.
A idade é calculada subtraindo-se o ano de nascimento (ano) do ano atual (ano_atual.year).
O código verifica as seguintes condições:
Se a idade for menor que 16, a função retorna uma mensagem formatada indicando a idade e "Voto Negado!".
Se a idade estiver entre 18 e 65 (inclusive), a função retorna uma mensagem formatada indicando a idade e "Voto Obrigatório!".
Caso contrário, a função retorna uma mensagem formatada indicando a idade e "Voto Opcional!".
O valor retornado pela função é armazenado na variável resultado.
A mensagem de resultado é impressa na tela.'''