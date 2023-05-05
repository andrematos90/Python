'''Crie um prorgama que jogue jokenpo com você'''

from random import randint
from time import sleep

numero = randint(0,2)

if numero == 0:
    computador = 'pedra'

elif numero == 1:
    computador = 'tesoura' 

else:
    computador = 'papel'



usuario = str(input('Digite "pedra, "tesoura" ou "papel": ')).lower()
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print(computador)
sleep(1)


if computador == usuario:
    print('Ninguem ganha!')
elif numero == 0 and usuario == 'tesoura':
    print('Eu venci você!')
elif numero == 0 and usuario =='papel':
    print('Você me venceu!')
elif numero == 1 and usuario == 'pedra':
     print('Você me venceu!')
elif numero == 1 and usuario =='papel':
       print('Eu venci você!')
elif numero == 2 and usuario == 'pedra':
       print('Eu venci você!')
elif numero == 2 and usuario == 'tesoura':
     print('Você me venceu!')


'''
outra forma 

from random import choice
from time import sleep

OPCOES = ['pedra', 'papel', 'tesoura']

def jogar():
    escolha_computador = choice(OPCOES)
    escolha_usuario = input('Pedra, Papel ou Tesoura? "sair" para sair: ').lower().strip()
    
    if escolha_usuario == 'sair':
        return 'sair'
    
    if escolha_usuario not in OPCOES:
        print('Escolha inválida. Tente novamente.')
        return jogar()
    
    print('...')
    sleep(2)
    
    resultado = verificar_vencedor(escolha_usuario, escolha_computador)
    print(f'Computador: {escolha_computador}\n{resultado}')
    
    return resultado == 'Empate'

def verificar_vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return 'Empate!'
    elif escolha_usuario == 'pedra' and escolha_computador == 'tesoura':
        return 'Você venceu!'
    elif escolha_usuario == 'papel' and escolha_computador == 'pedra':
        return 'Você venceu!'
    elif escolha_usuario == 'tesoura' and escolha_computador == 'papel':
        return 'Você venceu!'
    else:
        return 'Você perdeu!'

def main():
    while True:
        empates = 0
        sair = False
        
        while empates < 3 and not sair:
            resultado = jogar()
            
            if resultado == 'sair':
                sair = True
                break
            elif resultado:
                empates += 1
            else:
                empates = 0
        
        if sair:
            print('Jogo encerrado.')
            break
        
        print(f'Parabéns, você venceu {empates} vezes seguidas! Vamos jogar mais uma vez?')

if __name__ == '__main__':
    main()
'''


