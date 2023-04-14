'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, 
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa 
vai informar quantas cédulas de cada valor serão entregues.

Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
'''

valor = int(input('Valor de Saque R$: '))
cedula_50 = cedula_20 = cedula_10 = cedula_1 = 0

while valor >= 50:
    valor = valor - 50 
    cedula_50 = cedula_50 + 1

while valor >= 20:
    valor = valor - 20
    cedula_20 = cedula_20 + 1

while valor >= 10:
    valor = valor - 10
    cedula_10 = cedula_10 + 1

while valor >= 1:
    valor = valor - 1
    cedula_1 = cedula_1 + 1

print(f'{cedula_50} notas de R$50')
print(f'{cedula_20} notas de R$20')
print(f'{cedula_10} notas de R$10')
print(f'{cedula_1} notas de R$1')

'''
O objetivo do programa é calcular a quantidade de cédulas necessárias para realizar
 um saque no caixa eletrônico. Para isso, o programa começa pedindo para o usuário 
 digitar o valor que ele deseja sacar, usando a função input() e armazenando o valor 
 em uma variável valor_saque.

Em seguida, o programa declara quatro variáveis que serão usadas para armazenar
 a quantidade de cédulas de cada valor: cedulas_50, cedulas_20, cedulas_10 e cedulas_1.
   Essas variáveis são inicializadas com o valor zero.

O primeiro loop while verifica se o valor do saque ainda é maior ou igual a R$ 50. 
Se for, o programa subtrai R$ 50 do valor do saque usando a expressão valor_saque -= 50,
 e incrementa o contador de cédulas de R$ 50, usando a expressão cedulas_50 += 1. 
 Esse processo continua até que o valor do saque seja menor do que R$ 50.

O segundo loop while verifica se o valor do saque ainda é maior ou igual a R$ 20. 
Se for, o programa subtrai R$ 20 do valor do saque e incrementa o contador de cédulas
 de R$ 20. Esse processo continua até que o valor do saque seja menor do que R$ 20.

O terceiro loop while verifica se o valor do saque ainda é maior ou igual a R$ 10.
 Se for, o programa subtrai R$ 10 do valor do saque e incrementa o contador de cédulas
   de R$ 10. Esse processo continua até que o valor do saque seja menor do que R$ 10.

O último loop while verifica se o valor do saque ainda é maior ou igual a R$ 1. 
Se for, o programa subtrai R$ 1 do valor do saque e incrementa o contador de cédulas
 de R$ 1. Esse processo continua até que o valor do saque seja menor do que R$ 1.

Depois que o programa calcula a quantidade de cédulas de cada valor, ele exibe essas
 quantidades na tela usando a função print(), mostrando a quantidade de cédulas
   de cada valor usando as variáveis que foram calculadas anteriormente.

Espero que esta explicação tenha sido mais clara e tenha ajudado a entender melhor
 como o programa funciona. Se ainda tiver alguma dúvida, por favor, não hesite em 
 perguntar.



                                     USANDO WHILE TRUE

                                     while True:
    valor_saque = int(input("Qual o valor a ser sacado? R$ "))
    
    if valor_saque % 1 != 0 or valor_saque <= 0:
        print("Valor inválido! Digite um valor positivo inteiro.")
        continue
    
    cedulas_50 = 0
    cedulas_20 = 0
    cedulas_10 = 0
    cedulas_1 = 0

    while valor_saque >= 50:
        valor_saque -= 50
        cedulas_50 += 1

    while valor_saque >= 20:
        valor_saque -= 20
        cedulas_20 += 1

    while valor_saque >= 10:
        valor_saque -= 10
        cedulas_10 += 1

    while valor_saque >= 1:
        valor_saque -= 1
        cedulas_1 += 1

    print(f"Quantidade de cédulas: \n"
          f"R$50: {cedulas_50} \n"
          f"R$20: {cedulas_20} \n"
          f"R$10: {cedulas_10} \n"
          f"R$1: {cedulas_1}")
          
    sair = input("Deseja sair do programa? (s/n) ")
    if sair.lower() == "s":
        break
        

Nesse código, o while True cria um loop infinito que só é interrompido quando o 
usuário decide sair do programa. Dentro desse loop, pedimos ao usuário que digite
 o valor que ele deseja sacar, usando a função input(), e armazenamos o valor em uma
   variável valor_saque.

Em seguida, verificamos se o valor do saque é válido. Se o valor for inválido 
(não inteiro ou menor ou igual a zero), o programa exibe uma mensagem de erro e 
continua o loop usando o comando continue, o que significa que o código abaixo desse
 comando não será executado e o programa volta para o início do loop.

Se o valor do saque for válido, o programa calcula a quantidade de cédulas de cada
valor usando o mesmo código que foi utilizado nos exemplos anteriores.

Depois que as quantidades de cédulas são calculadas, o programa imprime essas
 quantidades na tela, da mesma forma que nos exemplos anteriores.

Por fim, o programa pergunta ao usuário se ele deseja sair do programa. 
Se o usuário digitar "s", o loop é interrompido usando o comando break, o que significa que o programa termina. Se o usuário digitar "n", o loop continua e o programa volta para o início, pedindo novamente o valor do saque.


                                   CÓDIGO GUANABARA 


print('=' * 30)
print('{:^30}'.format('BANCO MATOS'))
print('='* 30)
valor_do_saque = int(input('Valor do Saque: R$'))
total = valor_do_saque
cedula = 50
total_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedula = total_cedula + 1
    else:
        if total_cedula > 0:
         print(f'Total de {total_cedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break

A primeira linha imprime 30 sinais de igual na tela.
A segunda linha imprime "BANCO MATOS" centralizado em 30 caracteres usando o método 
format().
A terceira linha imprime novamente 30 sinais de igual na tela.
A quarta linha pede ao usuário para digitar o valor do saque em reais (R$).
A quinta linha define uma variável "total" com o valor do saque digitado pelo usuário.
A sexta linha define a variável "cedula" como 50, que será usada para determinar 
qual nota deve ser entregue ao usuário.
A sétima linha define a variável "total_cedula" como 0, que será usada para contar
o número de notas entregues.
A partir da oitava linha começa um loop while infinito que só será interrompido com
o comando "break".
Na nona linha, o programa verifica se o valor total é maior ou igual ao valor da 
cédula. Se for, então uma nota é entregue e a variável "total_cedula" é incrementada
em 1. Em seguida, o valor da cédula é subtraído do valor total.
Se o valor total não for maior ou igual ao valor da cédula, o programa verifica se a
variável "total_cedula" é maior que 0. Se for, o programa imprime o número de notas
entregues e o valor da cédula correspondente.
A partir da linha 14, o programa verifica qual é a próxima cédula menor que deve ser 
entregue (de 50 para 20, de 20 para 10, de 10 para 1). A variável "cedula" é 
atualizada com o novo valor.
A partir da linha 17, a variável "total_cedula" é redefinida como zero e o loop 
continua até que o valor total seja igual a zero, momento em que o loop é interrompido.
                                   
                                     
                                       
                                           '''