'''104 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante á função 
input() do python, só que fazendo a validação para aceitar apenas um valor númerico.
EX: n = leiaInt('Digite um n')'''

def leiaInt(n):
   if n.isnumeric():
      print(f'número digitado: {n}')
      return n
   else:
      while n != n.isnumeric():
        print('\033[31mErro!\033[0m digite um número ')
        n = input('número: ').strip()

numero = input('número: ').strip()
leiaInt(numero)

'''
A função leiaInt é definida com um parâmetro n, que representa o número a ser verificado.

A função começa verificando se a variável n é composta apenas por dígitos numéricos usando o método isnumeric(). Esse método retorna True se todos os caracteres da string forem dígitos e False caso contrário.

Se a condição n.isnumeric() for verdadeira, o código entra no bloco if. Ele exibe uma mensagem na tela informando o número digitado usando uma f-string formatada, com a variável n incorporada na mensagem. Em seguida, retorna o número n.

Se a condição n.isnumeric() for falsa, o código entra no bloco else. Isso significa que o número digitado não é um valor numérico.

Dentro do bloco else, há um loop while que continua repetindo até que o número digitado seja um valor numérico válido.

Dentro do loop, uma mensagem de erro é exibida na tela usando a sequência de escape \033[31m para definir a cor do texto como vermelho e \033[0m para redefinir a cor do texto de volta ao padrão.

Em seguida, o código solicita ao usuário que insira um novo número usando a função input(). A função strip() é usada para remover quaisquer espaços em branco adicionais no início ou no final da entrada do usuário.

O novo número digitado é atribuído à variável n, substituindo o valor original.

O loop continua repetindo até que a condição n.isnumeric() seja verdadeira e o número digitado seja um valor numérico válido.

Quando o número digitado é um valor numérico válido, a função leiaInt é concluída e o programa principal continua sua execução.'''
