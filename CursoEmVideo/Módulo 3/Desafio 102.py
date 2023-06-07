'''
102 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros. O primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.'''

def fatorial(n, show=False):
   """
   -> Calcúla o Fatorial de um número:
   :parametro n: é o numero a ser calculado.
   :parametro show: (opcional) Mostra ou não a conta.
   :return: O valor do Fatorial é o número n."""
   f = 1
   for c in range(n, 0, -1):
      if show:
         print(c, end='')
         if c > 1:
            print(' X ', end='')
         else:
            print(' = ', end='')
      f *= c
   return f
#programa principal
print(fatorial(5, show=True))
help(fatorial)

'''
A função fatorial recebe dois parâmetros: n, que é o número para o qual queremos calcular o fatorial, e show, que é um parâmetro opcional para determinar se queremos mostrar a conta passo a passo. Por padrão, o valor de show é False, ou seja, a conta não será mostrada.

A variável f é inicializada com o valor 1. Esta variável será usada para acumular o resultado do fatorial.

Em seguida, inicia-se um loop for que vai de n até 1, com passo -1. Isso significa que o loop vai iterar de n até 1, decrementando 1 a cada iteração.

Dentro do loop, há uma verificação para mostrar a conta, caso o parâmetro show seja True. Se show for True, o número atual c é impresso na tela. Se c for maior que 1, é impresso um "X" para indicar a multiplicação. Caso contrário, é impresso um "=" para indicar o fim da conta.

A variável f é multiplicada pelo valor de c em cada iteração do loop, atualizando o resultado do fatorial.

Após o loop, o resultado final do fatorial é retornado pela função.

No programa principal, é chamada a função fatorial passando o argumento 5 e show=True. Isso significa que a conta será mostrada passo a passo. O resultado do fatorial é impresso na tela.

Em seguida, é chamada a função help(fatorial) para exibir a documentação da função fatorial, que contém as informações sobre os parâmetros e o retorno da função.'''








