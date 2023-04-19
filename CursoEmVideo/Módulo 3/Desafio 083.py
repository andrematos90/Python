'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu programa deverá analisar se a expressão passada está com os parêntes abertos e fechados
na ordem correta.'''

expr = str(input('Digite uma expressão: '))
pilha = []

for i in expr:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão está correta!')
else:
    print('A expressão está incorreta!')


'''
Pede-se ao usuário que digite uma expressão que use parênteses, e armazena-se a 
expressão na variável expr como uma string.
Cria-se uma lista vazia chamada pilha, que será usada como uma pilha (ou stack) 
para verificar se os parênteses estão na ordem correta.
Inicia-se um loop usando a estrutura for para percorrer cada caractere da expressão 
digitada pelo usuário.
Verifica-se se o caractere atual é um parêntese de abertura (ou seja, um parêntese
esquerdo). Se sim, adiciona-se um elemento '(' à pilha usando o método append().
Se o caractere atual for um parêntese de fechamento (ou seja, um parêntese direito),
verifica-se se a pilha não está vazia e o último elemento da pilha é um parêntese 
de abertura (ou seja, um parêntese esquerdo). Se sim, remove-se o último elemento 
da pilha usando o método pop(), indicando que um parêntese de abertura correspondente
foi encontrado. Caso contrário, adiciona-se um elemento ')' à pilha usando o método
append() e interrompe-se o loop usando a instrução break.
Após percorrer todos os caracteres da expressão, verifica-se se a pilha está vazia 
usando a função len(). Se a pilha estiver vazia, significa que todos os parênteses de
abertura têm correspondência com os parênteses de fechamento, e imprime-se a mensagem
"A expressão está correta!". Caso contrário, imprime-se a mensagem "A expressão está 
incorreta!".'''
