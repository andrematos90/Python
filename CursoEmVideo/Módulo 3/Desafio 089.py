'''
89 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma váriavel composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualemente..
'''
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2:  '))
    media = (nota1 + nota2 / 2)
    resp = str(input('Continuar? [S/N]: '))
    ficha.append([nome, [nota1, nota2],media])
    if resp in 'nN':
        break
print('=-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' *35)
    opc = int(input('Mostrar notas de qual aluno? ("999" interrempe): '))
    if opc == 999:
        print('FINALIZANDO')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc] [0]} são {ficha[opc][1]}')

'''
ficha = [] cria uma lista vazia chamada "ficha".

while True: inicia um loop "while" infinito que solicita informações sobre um aluno e calcula a média de suas notas.

nome = str(input('Nome: ')) solicita ao usuário o nome do aluno e armazena na variável "nome".

nota1 = float(input('Nota 1: ')) solicita ao usuário a primeira nota do aluno e armazena na variável "nota1".

nota2 = float(input('Nota 2: ')) solicita ao usuário a segunda nota do aluno e armazena na variável "nota2".

media = (nota1 + nota2 / 2) calcula a média das notas e armazena na variável "media".

resp = str(input('Continuar? [S/N]: ')) pergunta ao usuário se ele deseja continuar adicionando alunos à lista e armazena a resposta na variável "resp".

ficha.append([nome, [nota1, nota2],media]) adiciona uma lista com informações do aluno (nome, notas e média) à lista "ficha".

if resp in 'nN': break verifica se o usuário deseja continuar adicionando alunos à lista e, se ele digitar "n" ou "N", interrompe o loop "while".

print('=-' * 30) imprime uma linha de separação para indicar o final da etapa de entrada de dados.

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}') imprime o cabeçalho da tabela com informações dos alunos.

print('-' * 26) imprime uma linha de separação para separar o cabeçalho do restante da tabela.

for i, a in enumerate(ficha): inicia um loop "for" que percorre a lista "ficha" e extrai as informações de cada aluno.

print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}') imprime uma linha da tabela com informações de um aluno específico.

while True: inicia outro loop "while" infinito que solicita ao usuário o número de um aluno cujas notas ele deseja ver.

print('-' * 35) imprime uma linha de separação para indicar o início da etapa de consulta.

opc = int(input('Mostrar notas de qual aluno? ("999" interrompe): ')) solicita ao usuário o número de um aluno e armazena na variável "opc".

if opc == 999: print('FINALIZANDO') break verifica se o usuário digitou "999" para encerrar o programa e, se sim, interrompe o loop "while".

if opc <= len(ficha) - 1: verifica se o número fornecido pelo usuário é válido, ou seja, está dentro do intervalo de alunos na lista "ficha".

print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}') imprime as notas do aluno correspondente ao número fornecido pelo usuário.'''

   