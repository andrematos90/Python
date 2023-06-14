def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!\033[0m Digite um número inteiro válido.')
            continue
        else:
           return n

def linha(tamanho = 42):
    return '-' * tamanho

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[0m - \033[34m{item}\033[0m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[0m')
    return opc