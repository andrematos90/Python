# programa que le algo no teclado e mostre na tela o seu
#seu tipo primitivo e todas as informações possiveis sobre o que foi digitado.

a = input('Digite algo:') #a é um objeto, objeto tem caracteristicas e funcionalidades, atributos e métodos
print('o que você digitou é do tipo:',type(a))
print('é em letras maiúsculas?', a.isupper())
print('é numérico?', a.isnumeric())
print('são letras?', a.isalpha())
print('são letras e números?',a.isalnum())
print('só tem espaços?', a.isspace())
print('está capitalizada?', a.istitle()) #nem maiúscula nem minuscula
print('o que você digitou foi "{}"' .format(a), 'que possui', len(a), 'caracteres')