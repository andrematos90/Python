def leiaInt(n):
   n = input('Numéro:')
   if n.isnumeric():
    
      print(f'número digitado: {n}')
      return n
   else:
      while n != n.isnumeric():
        print('\033[31mErro!\033[0m digite um número ')
        n = input('número: ').strip()

numero = leiaInt('número: ')