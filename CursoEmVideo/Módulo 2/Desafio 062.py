'''Melhore o desafio 061, perguntando para o usúario se ele quer mostrar mais alguns termos. O programa encerra 
quando ele disser que quer mostrar 0 termos'''


primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termo = primeiro_termo
cont = 1
mais = 10
total = 1

while mais != 0:  
    total = total + mais
    while cont <= total:
        print('{} '.format((termo)))
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quer mostrar mais quantos temos? '))
print('fim')

