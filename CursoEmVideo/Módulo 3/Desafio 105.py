'''105 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior Nota
- A menor Nota
- A média do aluno
- A situação (opcional)

Adicione tambem docstrings.'''


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de alunos
    :para n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação do aluno
    
    
    """
    dicionario = dict()
    dicionario['total'] = len(n)
    dicionario['maior'] = max(n)
    dicionario['menor'] = min(n)
    dicionario['media'] = sum(n) / len(n)
    if sit:
        if dicionario['media'] == 10:
            dicionario['situação'] = 'Excelente'
        elif dicionario['media'] >= 8 and dicionario['media']<= 9:
            dicionario['situação'] = 'Ótimo'
        elif dicionario['media'] == 7:
            dicionario['situação'] [ 'Aprovado']
        elif dicionario['media'] < 7 and dicionario['media'] > 5:
            dicionario['situação'] = 'Recuperação'
        else:
            dicionario['situação'] = 'Reprovado'
    return dicionario

#programa principal
resp = notas(10, 10, 10, 10, sit=False)
help(notas)

'''
A função é definida usando a palavra-chave def seguida pelo nome da função, notas, e parênteses que contêm os parâmetros da função, *n e sit=False. O parâmetro *n permite passar um número variável de argumentos posicionais, representando as notas dos alunos. O parâmetro sit é um argumento opcional com um valor padrão de False, indicando se deve ou não adicionar a situação do aluno ao dicionário de retorno.

A função tem uma string de documentação, delimitada por três aspas duplas ("""). Essa string de documentação fornece uma breve descrição da função, explicando seus parâmetros e o que ela retorna.

É criado um dicionário vazio chamado dicionario para armazenar as informações sobre a situação do aluno.

O número total de notas é adicionado ao dicionário, utilizando a chave 'total' e o valor len(n), que retorna o comprimento da sequência de notas fornecida.

A maior nota é adicionada ao dicionário, utilizando a chave 'maior' e a função max(n), que retorna o maior valor da sequência de notas.

A menor nota é adicionada ao dicionário, utilizando a chave 'menor' e a função min(n), que retorna o menor valor da sequência de notas.

A média das notas é calculada e adicionada ao dicionário, utilizando a chave 'media' e a expressão sum(n) / len(n), que calcula a soma das notas e divide pelo número total de notas.

Se o parâmetro sit for True (ou seja, foi passado como argumento ao chamar a função), a situação do aluno será calculada com base na média.

Se a média for igual a 10, a situação será definida como 'Excelente'.

Se a média estiver entre 8 e 9 (inclusive), a situação será definida como 'Ótimo'.

Se a média for igual a 7, a situação será definida como 'Aprovado'.

Se a média estiver abaixo de 7 e acima de 5, a situação será definida como 'Recuperação'.

Caso contrário, se a média for menor ou igual a 5, a situação será definida como 'Reprovado'.

O dicionário contendo todas as informações é retornado pela função.

No programa principal, a função notas é chamada com algumas notas como argumentos. Neste exemplo, as notas fornecidas são 10, 10, 10, 10. O argumento sit=False indica que não queremos que a situação do aluno seja incluída no dicionário retornado.

Em seguida, a função help é chamada passando a função notas como argumento. Isso exibe a documentação da função, que foi definida usando a string de documentação no início do código'''