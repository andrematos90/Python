'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu programa deverá analisar se a expressão passada está com os parêntes abertos e fechados
na ordem correta.'''

expressao = str(input('Digite uma expressão: '))
pilha = []


for c in expressao:
    if c == '(':
        pilha.append(c)
        if c == ')':
            if len(pilha) == 0:
                print('Expressão inválida : há um parêntese de fechamento sem um parêntese de abertura correspondente.')
                break
            else:
                pilha.pop()
if len(pilha) == 0:
     print('Expressão válida!')
else:
     print('Expressão inválida!')
            


