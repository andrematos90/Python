num = int(input('Dgite um número: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEZADECIMAL''')
opcao = int(input('Digite Sua opção: '))

if opcao == 1:
  print('{} convertido para binário é: {}'.format(num, bin(num)[2:]))

elif opcao == 2:
  print('{} convertido para octal é: {}'.format(num, oct(num)[2:]))

elif opcao == 3:
  print('{} convertido para hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
  print('Opção inválida!')
