from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'dadosdosistema.txt'

if arquivoExiste(arq):
    print('Arquivo Encontrado!')
else:
    print('Arquivo inexistente!')
    criaArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas',
                    'Cadastrar nova Pessoa', 
                    'Sair do sistema'])
    if resposta == 1:
        # opção de listar o contéudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('PROGRAMA ENCERRRADO!')
        break
    else:
        cabecalho('\033[31mERRO!\033[0m Digite um opção válida..')
    sleep(2)

