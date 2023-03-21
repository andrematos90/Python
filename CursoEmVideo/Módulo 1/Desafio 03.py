# programa que le algo no teclado e mostre na tela o teu tipo primitivo e todas as informações
#possiveis sonre ela

a = input('Digite alguma coisa:')
print(type(a))
print((a.isupper()))
print(a.isalnum())
print(a.isalpha())
print('O que você digitou tem ', len(a), 'caracteres')