'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros
elementos de uma sequência de fibonacci'''
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('-' * 30)
print('{} → {}'.format(t1, t2))
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    t3 = t2 + t3
    cont+= 1
print(' → Fim')


'''outra forma 

numero = int(input('quantidade de termos: '))
t1 = 0
t2 = 1
print(f'{t1} ➝  {t2} ➝  ', end='')
cont = 3
while cont <= numero:
   t3 = t1 + t2
   print(f'{t3} ➝  ', end='')
   t1 = t2
   t2 = t3
   cont += 1
   
   
Solicitamos ao usuário que insira a quantidade de termos da sequência de Fibonacci que deseja gerar. O valor é armazenado na variável numero.
Inicializamos duas variáveis, t1 e t2, com os primeiros termos da sequência de Fibonacci: 0 e 1, respectivamente.
Utilizando a função print, exibimos os primeiros dois termos da sequência de Fibonacci na tela, formatados usando uma f-string. O parâmetro end='' é utilizado para evitar a quebra de linha após a impressão.
Inicializamos a variável cont com o valor 3. Essa variável será usada como um contador para controlar o número de termos que já foram gerados.
Iniciamos um loop while que continuará até que o contador cont alcance ou ultrapasse o valor de numero. Isso garantirá que geremos a quantidade de termos especificada pelo usuário.
Dentro do loop, calculamos o próximo termo t3 somando os valores de t1 e t2.
Utilizando novamente a função print, exibimos o valor do próximo termo t3 na tela, formatado usando uma f-string. O parâmetro end='' é utilizado para evitar a quebra de linha após a impressão.
Atualizamos os valores de t1 e t2, movendo-os para o próximo par de termos da sequência.
Incrementamos o contador cont em 1 para acompanhar o número de termos gerados.'''