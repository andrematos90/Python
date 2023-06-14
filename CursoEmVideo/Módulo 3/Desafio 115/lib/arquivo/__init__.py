from lib.interface import *
def arquivoExiste(nomedoarquivo):
    try:
        a = open(nomedoarquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criaArquivo(nomedoarquivo):
    try:
        a = open(nomedoarquivo, 'wt+')
        a.close()
    except:
        print('Ocorreu um erro durante a criação do aquivo!')
    else:
        print(f'Arquivo {nomedoarquivo} criado com sucesso!')
        
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[031mERRO![0m na leitura do arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('\033[031mERRO!\031[0mHouve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('\033[31mERRO![0m Um erro ocorreu ao escrever os dados!')
        else:
            print(f'{nome} cadastrado com \033[32mSucesso!\033[0m')
    